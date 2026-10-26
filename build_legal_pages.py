"""Builds site/privacy.html and site/terms.html.

The pages reuse the website's own styles, header and footer (taken from
site/index.html), so run this again after changing the site's design or the
wording below:

    python build_legal_pages.py

Keep the wording true to how the service actually works. If anything below
changes (retention days, AI provider, hosting, whether a person checks every
reply), update it here and rebuild.
"""

import re
from pathlib import Path

SITE = Path(__file__).parent / "site"
UPDATED = "October 2026"
CONTACT = "info@scamwatcherpacific.com"

PRIVACY = f"""
<h1>Privacy policy</h1>
<p class="updated">Last updated: {UPDATED}</p>
<p class="intro">ScamWatcher Pacific is an independent scam-checking service for Pacific communities. People send us messages they're unsure about, and those messages often contain names, phone numbers or account details. This policy explains what we collect, why, who sees it, and how long we keep it.</p>
<p>ScamWatcher Pacific is not a government agency, bank, telco or police service, and is not affiliated with the Australian Government's Scamwatch.</p>

<h2>1. What we collect</h2>
<h3>When you email us a message to check</h3>
<p>When you forward a message to <a href="mailto:check@scamwatcherpacific.com">check@scamwatcherpacific.com</a>, we receive the whole email: your email address, the forwarded message, its sender details, subject, links, attachments and any images or screenshots.</p>
<h3>When you use the form on our website</h3>
<p>We receive the email address you give us, your country, where you received the message, the screenshots you upload and any notes you add.</p>
<h3>Information about other people</h3>
<p>The messages you send us may include details about other people, such as the sender's name, phone number or account. We use these only to check the message.</p>
<h3>When you visit our website</h3>
<ul>
<li>Our hosting provider keeps standard technical logs, such as your IP address, browser type and the pages requested.</li>
<li>We use your IP address briefly to stop the same connection sending too many form submissions.</li>
<li>Our website loads its fonts from Google Fonts, which receives your IP address when the page loads.</li>
<li>We don't use analytics or advertising cookies. If you choose a country under "Where to report", your browser remembers that choice on your device. It is not sent to us.</li>
</ul>

<h2>2. How we use it</h2>
<ul>
<li>To check the message you sent and email you our assessment and advice.</li>
<li>To answer your follow-up questions.</li>
<li>To keep the service secure and prevent misuse.</li>
<li>To improve how we spot scams, for example by adding a new type of scam to our checks.</li>
</ul>
<p>We don't sell your information, and we don't use it for marketing or advertising.</p>

<h2>3. How messages are checked, including AI</h2>
<p>Emails are checked by our own automatic checks, which look at who sent the message, what it asks for, where its links go and whether it matches a known scam.</p>
<p>Screenshots and images are also read by an AI service, Anthropic's Claude. It reads the text in the image, translates Pacific languages into English and drafts an assessment.</p>
<p>Most replies are sent to you automatically. If the system is unsure, for example because an image is hard to read, a member of our team checks the assessment before the reply is sent.</p>

<h2>4. Who we share it with</h2>
<p>We share your information only with the service providers that run ScamWatcher Pacific, and only so they can provide that service to us:</p>
<ul>
<li><strong>Anthropic</strong>: reads screenshots and images (AI service).</li>
<li><strong>Render</strong>: hosts our website and review system.</li>
<li><strong>Google Workspace</strong>: our email.</li>
</ul>
<p>We may also disclose information if the law requires us to.</p>

<h2>5. Information handled overseas</h2>
<p>Our review system is hosted in Singapore, our AI service is based in the United States, and our email provider stores data in several countries. By using the service, you understand that your information may be handled outside your own country. We take reasonable steps to choose providers that protect it.</p>

<h2>6. How long we keep it</h2>
<p>We keep what you send only long enough to review it and answer follow-up questions. Everything is deleted automatically after <strong>30 days</strong>: the submission, any screenshots, your email in our inbox and our reply in our sent mail.</p>
<p>Deleted emails stay in our email provider's bin for up to 30 more days before they are removed for good. Our service providers may also keep short-term logs or backups under their own policies.</p>

<h2>7. Your choices</h2>
<ul>
<li><strong>Delete sooner:</strong> email <a href="mailto:{CONTACT}?subject=Please%20delete%20what%20I%20sent">{CONTACT}</a> from the address you used and ask us to delete what you sent. We'll confirm once it's done.</li>
<li><strong>Access or correct:</strong> email us from the same address to ask what we hold about you, or to correct it.</li>
<li><strong>Share less:</strong> feel free to cover account numbers before sending a screenshot. Never send us passwords, PINs or full card numbers. We will never ask for them.</li>
</ul>
<p>We only act on requests that come from the email address used to send the message, so nobody can see or delete someone else's submission.</p>

<h2>8. Security</h2>
<p>Only our review team can see submissions, after signing in to our review system. Our website and review system use encrypted connections. No online service can be completely secure, but we take reasonable steps to protect what you send.</p>

<h2>9. Questions and complaints</h2>
<p>Email <a href="mailto:{CONTACT}">{CONTACT}</a>. If you aren't happy with our response, you can contact the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au/" rel="noopener">oaic.gov.au</a>, or the privacy regulator in your country.</p>

<h2>10. Changes to this policy</h2>
<p>We may update this policy as the service changes. The date at the top shows when it last changed.</p>
"""

TERMS = f"""
<h1>Terms of use</h1>
<p class="updated">Last updated: {UPDATED}</p>
<p class="intro">These terms apply when you use ScamWatcher Pacific, including our website and our email checking service. Please read them with our <a href="privacy.html">privacy policy</a>.</p>

<h2>1. Accepting these terms</h2>
<p>By using ScamWatcher Pacific, including sending us a message or screenshot to check, you agree to these terms.</p>

<h2>2. What the service is</h2>
<p>ScamWatcher Pacific is an independent advisory service. We look for warning signs in messages you send us and give you general guidance on what to do next. We are not a government agency, bank, telco or police service, and we are not affiliated with the Australian Government's Scamwatch.</p>

<h2>3. No guarantees</h2>
<p>We can't confirm for certain whether a message is safe or a scam, and we can't verify who sent it. Scammers change their methods often, so our assessments are advice, not a final answer.</p>

<h2>4. Your decisions are your own</h2>
<p>You are responsible for what you do after reading our advice. Before acting on any message, check it through contact details you already trust, such as the official app or the number on your card or bill. Take extra care with requests for money, personal details or passwords. Our advice is there to help you decide, not to decide for you.</p>

<h2>5. Not professional or emergency advice</h2>
<p>We don't provide legal, financial or cybersecurity advice, and we can't respond in an emergency. If you have lost money, contact your bank or mobile money provider straight away. If you are in danger, call your local emergency number.</p>

<h2>6. Our liability</h2>
<p>As far as the law allows, ScamWatcher Pacific is not liable for any loss or harm from relying on our assessments, from a scam we didn't identify, from an inaccurate assessment, or from anything you do as a result. This includes financial loss, loss of data, and harm to reputation or business.</p>

<h2>7. Availability</h2>
<p>We don't guarantee that the service will always be available or that we will reply within a set time. We may change, pause or stop the service at any time.</p>

<h2>8. What you send us</h2>
<p>By sending us a message or screenshot, you confirm that you are allowed to share it, even if it contains other people's information. You give us permission to process it to check it, as described in our privacy policy. You still own what you send; we don't claim ownership of it.</p>

<h2>9. Fair use</h2>
<p>Don't use the service for anything unlawful, send harmful or malicious files, or try to disrupt or overload it. We may limit or block access if the service is misused.</p>

<h2>10. Our content</h2>
<p>The ScamWatcher Pacific name, logo, website and the assessments we write belong to us. You're welcome to use our advice for yourself, your family or your organisation, and to share it to warn others. Please don't sell or republish it as your own without our permission.</p>

<h2>11. Privacy</h2>
<p>How we handle your information is explained in our <a href="privacy.html">privacy policy</a>.</p>

<h2>12. Changes to these terms</h2>
<p>We may update these terms. The date at the top shows when they last changed. If you keep using the service after a change, you accept the updated terms.</p>

<h2>13. Governing law</h2>
<p>These terms are governed by the laws of Australia.</p>

<h2>14. Contact</h2>
<p>Questions about these terms? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<div class="principle"><strong>The key principle</strong>We give guidance, not certainty. We're here to help you pause, check and decide more safely. Always check before you click, pay or share.</div>
"""

EXTRA_CSS = """
.legal{padding:var(--s7) 0 var(--s8)}
.legal .wrap{max-width:780px}
.legal .back{display:inline-block;margin-bottom:var(--s5);color:var(--teal);font-weight:600;text-decoration:none}
.legal .back:hover{text-decoration:underline}
.legal h1{font-family:var(--display);font-size:var(--fs-xl);line-height:1.1;margin:0 0 var(--s2);color:var(--ink-strong)}
.legal .updated{color:var(--muted);font-size:var(--fs-xs);margin:0 0 var(--s5)}
.legal .intro{font-size:var(--fs-md);color:var(--ink)}
.legal h2{font-size:var(--fs-lg);margin:var(--s7) 0 var(--s3);padding-top:var(--s5);border-top:1px solid var(--line)}
.legal h3{font-size:var(--fs-base);margin:var(--s5) 0 var(--s2)}
.legal p,.legal li{max-width:68ch}
.legal ul{padding-left:1.25em;margin:var(--s2) 0 var(--s4)}
.legal li{margin-bottom:var(--s2)}
.legal a{color:var(--teal)}
.legal .principle{margin-top:var(--s7);padding:var(--s5);background:var(--lagoon-soft);border-radius:var(--r-md);color:var(--ink-strong)}
.legal .principle strong{display:block;font-family:var(--display);font-size:var(--fs-md);margin-bottom:var(--s2)}
"""

MENU_JS = """<script>
(function(){
  document.documentElement.classList.add('js');
  var btn=document.querySelector('.menu-btn'), nav=document.getElementById('site-nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=btn.getAttribute('aria-expanded')!=='true';btn.setAttribute('aria-expanded',String(o));nav.classList.toggle('open',o);});}
})();
</script>"""


def _link_home(fragment):
    """Point in-page links (#how, #top) back at the home page."""
    fragment = re.sub(r'href="#top"', 'href="index.html"', fragment)
    # Not <use href="#sw-logo">: that points at the logo drawn on this page.
    return re.sub(r'(?<!<use )href="#([a-z][\w-]*)"', r'href="index.html#\1"', fragment)


def build(name, title, description, body):
    index = (SITE / "index.html").read_text(encoding="utf-8")
    head_end = index.index("</head>")
    head = index[:head_end]
    head = re.sub(r"<title>.*?</title>", f"<title>{title} | ScamWatcher Pacific</title>", head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">', head, count=1)
    head = head.replace("</style>", EXTRA_CSS + "</style>", 1)
    page_url = f"https://www.scamwatcherpacific.com/{name}"
    head = head.replace('href="https://www.scamwatcherpacific.com/"', f'href="{page_url}"')
    head = head.replace('content="https://www.scamwatcherpacific.com/"', f'content="{page_url}"')
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title} | ScamWatcher Pacific">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{description}">', head)

    body_start = index.index("<body", head_end)
    header_end = index.index("</header>", body_start) + len("</header>")
    top = _link_home(index[body_start:header_end])

    footer_start = index.index('<footer class="site-footer">')
    footer_end = index.index("</footer>", footer_start) + len("</footer>")
    footer = _link_home(index[footer_start:footer_end])

    page = (
        head + "</head>\n" + top + "\n\n"
        f'<main id="main" class="legal">\n  <div class="wrap">\n    <a class="back" href="index.html">← Back to ScamWatcher Pacific</a>\n'
        + body + "\n  </div>\n</main>\n\n" + footer + "\n" + MENU_JS + "\n</body>\n</html>\n"
    )
    (SITE / name).write_text(page, encoding="utf-8")
    print(f"Wrote site/{name}")


if __name__ == "__main__":
    build("privacy.html", "Privacy policy",
          "How ScamWatcher Pacific collects, uses, shares and deletes the messages you send us.", PRIVACY)
    build("terms.html", "Terms of use",
          "The terms for using ScamWatcher Pacific's independent scam-checking service.", TERMS)
