# ScamWatcher Pacific

The review dashboard, inbox worker and website for **ScamWatcher Pacific**, an independent scam-checking service for Pacific communities and Pacific families abroad.

It is a separate copy of the ScamWatcher (Australia) MVP, with its own mailbox, database and dashboard, so Pacific submissions never mix with Australian ones.

## What's in here

| Part | What it does |
|---|---|
| `site/index.html` | The public website. Self-contained, deploy it as a static page. Its "Get it checked" form posts to the dashboard's `/intake`. |
| `app.py` | The review dashboard (Flask). Also receives the website form at `/intake`. |
| `inbox_worker.py` + `email_reader.py` | Checks `check@scamwatcherpacific.com` every 30 seconds, runs the automatic review and files each email in the dashboard. |
| `analyzer.py`, `review_checks.py`, `scoring_model.py`, `trust_lists.py` | The rule-based review engine. Pacific scam patterns are at the end of `SCAM_PATTERNS` in `review_checks.py`. |
| `uploads.py` | Stores screenshots (from the form and from emails) with random file names. |

## How a submission flows

**By email** to `check@scamwatcherpacific.com`
1. The inbox worker picks it up and runs the four automatic checks (sender, content, links, known scams).
2. If it contains a **screenshot or photo** (an image over 30 KB), the image is saved and the submission goes to **Needs manual review**, because the checks can't read images.
3. Otherwise a reply is drafted and waits in **Needs approval**.

**By the website form**
1. `/intake` validates the email address, accepts up to 5 screenshots and checks each really is an image (PNG, JPG, GIF, WebP or HEIC, up to 10 MB each), and rate-limits each connection.
2. The submission always goes to **Needs manual review**. No automatic reply is sent to the address typed into the form.
3. The person is sent back to the website with a confirmation message.

**Automatic screenshot review**
When `ANTHROPIC_API_KEY` is set, every screenshot (from the form or an email) is sent to Claude, which reads the message, translates any Pacific-language text, and drafts an assessment, scam type, advice and observations. The rule-based checks also run on the text it read, as a cross-check. The submission then moves to **Needs approval** with a "Draft written by the automatic review" note, and the text read from the screenshot is shown next to the image. A person still approves every reply, and screenshot submissions are never auto-sent.

If the review fails (or the photo is an iPhone HEIC, which Claude can't read), the submission stays in **Needs manual review** with the reason shown, and **Review the screenshot again** retries it. Screenshots that arrived before the key was set are reviewed when the app next starts. The model is set with `CLAUDE_MODEL` (default `claude-sonnet-5-5`).

Because screenshots go to Anthropic for reading, the website's privacy section says so. Keep that wording if you keep the feature on.

**Replying to a manual submission**
Open it, look at the screenshot, choose an assessment, write what they should do and what you noticed, then **Save reply**. Check the preview and **Approve and send**. The reply comes from `check@scamwatcherpacific.com`.

Screenshot submissions are **never auto-sent**, even if `AUTO_SEND_ENABLED=true`.

## Privacy, retention and deletion

The website promises submissions are only used to review and reply, seen only by the review team, never sold or shared, deleted after a set number of days, and deleted sooner on request. The app supports this as follows:

- **Retention:** set `RETENTION_DAYS` to the number on the website. Every hour the app deletes older submissions, their screenshots, and the matching emails in the inbox **and Sent** folders. On Gmail these go to Bin, which Gmail empties after 30 days.
- **Delete on request:** every submission has a **Delete permanently** button. It removes the record, its screenshots and the inbox email.
- **No copies outside the team:** `AUDIT_BCC_EMAIL` is empty by default. The Australian version BCCs an audit address; this one doesn't unless you set it.
- **Screenshots** are only served to signed-in reviewers.

Until `RETENTION_DAYS` is set, nothing is deleted automatically and the logs say so.

## Setting it up

1. **Mailbox.** Create `check@scamwatcherpacific.com` (Google Workspace is simplest), turn on 2-step verification and create an app password.
2. **Email authentication.** In your domain's DNS, set up SPF, DKIM and DMARC for `scamwatcherpacific.com`. Replies then land in inboxes rather than spam, and scammers find it harder to send emails as you.
3. **Deploy on Render with the Blueprint** (`render.yaml`):
   - In Render choose **New > Blueprint** and pick this repository.
   - Render creates two services in Singapore: `scamwatcherpacific-dashboard` (Starter plan, with a 1 GB disk at `/var/data`) and `scamwatcherpacific-site` (the website, free static hosting).
   - It asks for three values: `ADMIN_PASSWORD`, `EMAIL_PASSWORD` (the mailbox app password) and `RETENTION_DAYS`. `SECRET_KEY` is generated for you.
   - The website's form is pointed at the dashboard automatically when the site builds, and `SITE_URL` starts as the site's Render address.
4. **Custom domains.** Add `scamwatcherpacific.com` to the site service, then change the dashboard's `SITE_URL` to `https://scamwatcherpacific.com`. Optionally give the dashboard its own address (for example `review.scamwatcherpacific.com`). If you do, redeploy the site so its form uses the new address, or set `DASHBOARD_HOST` on the site to it.

   Not using Render? Build with `pip install -r requirements.txt`, start with `gunicorn app:app --workers 1 --threads 4`, keep a persistent disk at `/var/data`, and replace `YOUR-DASHBOARD-URL` in `site/index.html` yourself. Keep it to **one worker**: the inbox checker runs inside the app.
5. **Fill the site placeholders** (response time, retention days, reporting contacts and so on). The response time also appears in the form's confirmation message.

## Privacy policy and terms

`site/privacy.html` and `site/terms.html` are built from the wording in `build_legal_pages.py`, using the site's own header, footer and styles. Edit the wording there and run `python build_legal_pages.py`. Keep it true to how the service works: if the retention period, AI provider, hosting, or whether a person checks every reply changes, update it.

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # then fill in ADMIN_PASSWORD and SECRET_KEY
DB_PATH=./local.db SESSION_COOKIE_SECURE=false INBOX_WORKER_ENABLED=false FLASK_DEBUG=1 python app.py
```

Open `http://127.0.0.1:5000`. To try the form locally, change the website form's action to `http://127.0.0.1:5000/intake` and set `SITE_URL` to wherever you open the page from.

## Keeping it current

- New scam campaigns: add to `SCAM_PATTERNS` in `review_checks.py` (Pacific ones are at the end).
- Organisations people are impersonated as: add to `BRANDS` with their official domains.
- Confirmed scam domains: add to `BLOCKED_DOMAINS` in `trust_lists.py`.
- Where to report, by country: edit `report_contacts.py` (checked contacts with their sources). It feeds the "Where to report" line in replies; run `python report_contacts.py --html` and paste the output into the website's "Where to report, by country" card.

## Important

This is a validation MVP, not a production-grade detection engine. Keep a person reviewing every reply, especially anything involving screenshots.
