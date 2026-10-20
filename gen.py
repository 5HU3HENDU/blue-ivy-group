# -*- coding: utf-8 -*-
import os
R='/home/sandbox/big'
BASE='https://5hu3hendu.github.io/blue-ivy-group'

LOGO='''<svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true"><rect x="1" y="1" width="28" height="28" rx="8" fill="#0e1a1f"/><path d="M9 21V9h4.2c2.4 0 3.8 1.1 3.8 2.9 0 1.2-.6 2.1-1.7 2.5 1.5.3 2.3 1.4 2.3 2.9 0 2.1-1.6 3.7-4.1 3.7H9zm2.6-7h1.4c1 0 1.6-.5 1.6-1.4s-.6-1.3-1.6-1.3h-1.4V14zm0 4.7h1.7c1.1 0 1.8-.6 1.8-1.6 0-1-.7-1.5-1.8-1.5h-1.7v3.1z" fill="#e9e4d8"/><path d="M20.4 9h2.5v12h-2.5z" fill="#2e9e6b"/></svg>'''

I={
'phone':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
'mail':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/></svg>',
'li':'<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.55V9h3.57v11.45z"/></svg>',
'pin':'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
'arr':'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
'check':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
'star':'<svg width="14" height="14" viewBox="0 0 24 24" fill="#d97706" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.2 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8z"/></svg>',
# tab bar
'home':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
'grid':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
'bldg':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21V7l7-4v18M12 21V11l7 4v6"/><path d="M8 9h.01M8 13h.01M8 17h.01"/></svg>',
'info':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4m0-4h.01"/></svg>',
'call':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
}

NAV=[('index.html','Home','home'),('projects.html','Projects','bldg'),('about.html','About','info'),('contact.html','Contact','call')]
# services hub lives inside index; tab bar uses 4 + services anchor
TAB=[('index.html','Home','home'),('index.html#services','Services','grid'),('projects.html','Projects','bldg'),('about.html','About','info'),('contact.html','Contact','call')]

def page(path, slug, title, desc, body, depth=0, extra_head='', active=''):
    p='../'*depth
    def on(cls): return ' class="on"' if cls else ''
    navd=''.join('<a href="%s%s"%s>%s</a>' % (p,h,on(t==active),t) for h,t,_ in NAV)
    tab=''.join('<a href="%s%s"%s>%s<span>%s</span></a>' % (p,h,on(t==active or (active=="Services" and t=="Services")),I[i],t) for h,t,i in TAB)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Blue Ivy Group">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{BASE}/assets/img/og-cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e1a1f">
<link rel="icon" href="{p}assets/img/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="{p}assets/img/icon-180.png">
<link rel="manifest" href="{p}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,560;9..144,640&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
{extra_head}
</head>
<body>
<header class="topbar"><div class="wrap topbar-in">
<a class="brand" href="{p}index.html">{LOGO}<span class="wm">Blue Ivy Group</span></a>
<nav class="nav-d" aria-label="Main">{navd}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="foot">
<a class="l" href="{p}index.html">{LOGO}<span>Blue Ivy Group</span></a>
<div class="r">301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086<br>&copy; 2026 Blue Ivy Group</div>
</div>
<div class="demo">Redesign concept demo. Official site: <a href="https://blueivygroup.in/">blueivygroup.in</a>. Sections marked Under construction are placeholders awaiting confirmed company information.</div>
</div></footer>
<nav class="tabbar" aria-label="Main">{tab}</nav>
<script src="{p}assets/js/main.js" defer></script>
</body>
</html>'''

def W(path, html):
    fp=os.path.join(R,path); os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'w').write(html); print('wrote',path,len(html)//1024,'KB')

UC='<span class="uc">Under construction</span>'

CTAS=f'''<div class="cta-row">
<a class="icobtn" href="tel:+912225161818">{I['phone']}022 2516 1818</a>
<a class="icobtn ghost" href="mailto:info@blueivygroup.in">{I['mail']}Email</a>
<a class="icobtn ghost" href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">{I['li']}LinkedIn</a>
</div>'''

# ---------------- home ----------------
home_body=f'''
<div class="wrap">
<div class="head">
<span class="eyebrow"><span class="dot"></span>Ghatkopar West, Mumbai</span>
<h1>Built with care.<br>Delivered with <em>precision.</em></h1>
<p class="lede">Blue Ivy Group is a Mumbai construction, interiors and redevelopment firm. Residential, commercial and turnkey projects, managed end to end.</p>
{CTAS}
</div>
</div>

<section><div class="wrap">
<div class="strip">
<div><div class="b" style="display:flex;align-items:center;gap:6px">{I['star']}4.3 on Google</div><div class="s">8 reviews on the Google Business listing</div></div>
<div><div class="b">Ghatkopar West</div><div class="s">Excel Arcade, LBS Marg, Mumbai 400 086</div></div>
<div><div class="b">One roof</div><div class="s">Approvals to handover, turnkey</div></div>
</div>
</div></section>

<section id="services"><div class="wrap">
<div class="kicker">What we do</div>
<div class="sec-h"><h2>Services</h2></div>
<div class="sgrid">
<a class="scard" href="services/redevelopment.html"><div class="t">Redevelopment</div><div class="d">Society and building redevelopment with legal, technical and design precision.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/residential-construction.html"><div class="t">Residential Construction</div><div class="d">Homes, villas and gated communities, built for quality and safety.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/commercial-projects.html"><div class="t">Commercial Projects</div><div class="d">Towers, corporate buildings, hospitals, schools, colleges and malls.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/turnkey-construction.html"><div class="t">Turnkey Construction</div><div class="d">From approvals to handover, every stage under one roof.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/interior-design.html"><div class="t">Interior Design &amp; Execution</div><div class="d">Full-scope interiors for residential and commercial spaces.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/industrial-construction.html"><div class="t">Industrial Construction</div><div class="d">Industrial spaces, upgrades and facility construction.</div><span class="go">View {I['arr']}</span></a>
<a class="scard" href="services/project-management-consultancy.html"><div class="t">Project Management &amp; Consultancy</div><div class="d">Planning, approvals and execution oversight for your project.</div><span class="go">View {I['arr']}</span></a>
</div>
</div></section>

<section><div class="wrap">
<div class="kicker">Recent work</div>
<div class="sec-h"><h2>Projects</h2><a class="more" href="projects.html">All projects</a></div>
<div class="pgrid">
<div class="pcard"><img src="assets/img/amravati-mall.jpg" alt="Design render of the commercial mall project in Amravati" loading="lazy"><div class="pb"><div class="t">Commercial Mall</div><div class="l">{I['pin']}Amravati</div><div class="tags"><span class="tag">Commercial</span><span class="tag render">Design render</span></div></div></div>
<div class="pcard"><img src="assets/img/pahuja.jpg" alt="Design render of Pahuja Business Avenue in Sakinaka" loading="lazy"><div class="pb"><div class="t">Pahuja Business Avenue</div><div class="l">{I['pin']}Sakinaka, Mumbai</div><div class="tags"><span class="tag">Commercial</span><span class="tag render">Design render</span></div></div></div>
<div class="pcard"><img src="assets/img/siddhanchal.jpg" alt="Design render of Siddhanchal Residency in Ghatkopar" loading="lazy"><div class="pb"><div class="t">Siddhanchal Residency</div><div class="l">{I['pin']}Ghatkopar, Mumbai</div><div class="tags"><span class="tag">Residential</span><span class="tag render">Design render</span></div></div></div>
</div>
</div></section>

<section><div class="wrap">
<div class="kicker">Credentials</div>
<div class="sec-h"><h2>Registrations</h2></div>
<div class="sgrid">
<div class="ucard">{UC}<div class="t">GST registration</div><div class="d">GSTIN will be published here once confirmed by the company.</div></div>
<div class="ucard">{UC}<div class="t">MahaRERA registration</div><div class="d">RERA numbers for applicable projects will be listed once confirmed.</div></div>
<div class="ucard">{UC}<div class="t">Company registration</div><div class="d">Registration details will be published once confirmed.</div></div>
</div>
</div></section>

<section><div class="wrap">
<div class="kicker">People</div>
<div class="sec-h"><h2>Leadership</h2></div>
<div class="person"><div class="avatar">SK</div><div><div class="n">Shekhar B. Kale</div><div class="r">Director</div></div></div>
<div style="margin-top:12px"><div class="ucard">{UC}<div class="t">Full team</div><div class="d">The wider engineering and design team will be introduced here once details are confirmed.</div></div></div>
</div></section>

<section><div class="wrap">
<div class="kicker">Word of mouth</div>
<div class="sec-h"><h2>Testimonials</h2></div>
<div class="ucard">{UC}<div class="t">Client words, verified first</div><div class="d">Testimonials will appear here after clients confirm them for publication. Until then, nothing is quoted.</div></div>
</div></section>

<section><div class="wrap">
<div class="kicker">Start a conversation</div>
<div class="sec-h"><h2>Contact</h2></div>
<div class="cblock">
<div class="cline">{I['pin']}<span>301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086</span></div>
<div class="cline">{I['phone']}<a href="tel:+912225161818">022 2516 1818</a></div>
<div class="cline">{I['mail']}<a href="mailto:info@blueivygroup.in">info@blueivygroup.in</a></div>
<div style="margin-top:14px">{CTAS}</div>
</div>
</div></section>
'''

jsonld='''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"GeneralContractor","name":"Blue Ivy Group","url":"'''+BASE+'''/","image":"'''+BASE+'''/assets/img/og-cover.jpg","telephone":"+91-22-2516-1818","email":"info@blueivygroup.in","address":{"@type":"PostalAddress","streetAddress":"301, Excel Arcade, LBS Marg, Ghatkopar West","addressLocality":"Mumbai","addressRegion":"Maharashtra","postalCode":"400086","addressCountry":"IN"},"geo":{"@type":"GeoCoordinates","latitude":19.087315,"longitude":72.903306},"sameAs":["https://www.linkedin.com/company/blue-ivy-group","https://blueivygroup.in/"]}
</script>'''

W('index.html', page('index.html','home','Blue Ivy Group - Construction, Interiors & Redevelopment in Mumbai','Blue Ivy Group is a Mumbai construction, interiors and redevelopment firm based in Ghatkopar West. Residential, commercial and turnkey projects, managed end to end.', home_body, active='Home', extra_head=jsonld))

# ---------------- about ----------------
about_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; About</div>
<div class="head">
<span class="eyebrow"><span class="dot"></span>About</span>
<h1>The group behind <em>the work.</em></h1>
</div>
<div class="split">
<div class="prose">
<p><b>Blue Ivy Group</b> is a construction, interiors and redevelopment firm working from Ghatkopar West, Mumbai. The firm takes on residential, commercial, redevelopment, turnkey and interior projects, and manages them from approvals through handover.</p>
<p>Recent and ongoing work spans Mumbai and beyond, including a commercial mall in Amravati, Pahuja Business Avenue in Sakinaka and Siddhanchal Residency in Ghatkopar.</p>
<p>The office is at 301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086, reachable on 022 2516 1818 and info@blueivygroup.in.</p>
</div>
<div>
<div class="facts">
<div class="row"><span class="k">Based in</span><span class="v">Ghatkopar West, Mumbai</span></div>
<div class="row"><span class="k">Phone</span><span class="v">022 2516 1818</span></div>
<div class="row"><span class="k">Email</span><span class="v">info@blueivygroup.in</span></div>
<div class="row"><span class="k">Google rating</span><span class="v">4.3 (8 reviews)</span></div>
<div class="row"><span class="k">LinkedIn</span><span class="v"><a href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">blue-ivy-group</a></span></div>
</div>
<div style="margin-top:12px" class="ucard">{UC}<div class="t">Founding year, registrations, team size</div><div class="d">Company milestones and registration details will be published here once confirmed.</div></div>
</div>
</div>
<section>
<div class="kicker">People</div>
<div class="sec-h"><h2>Leadership</h2></div>
<div class="person"><div class="avatar">SK</div><div><div class="n">Shekhar B. Kale</div><div class="r">Director</div></div></div>
<div style="margin-top:12px" class="ucard">{UC}<div class="t">Full team</div><div class="d">Profiles of the engineering, design and site teams will be added once confirmed.</div></div>
</section>
</div>
'''
W('about.html', page('about.html','about','About - Blue Ivy Group, Mumbai','About Blue Ivy Group: a construction, interiors and redevelopment firm from Ghatkopar West, Mumbai, led by Director Shekhar B. Kale.', about_body, active='About'))

# ---------------- projects ----------------
proj_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Projects</div>
<div class="head">
<span class="eyebrow"><span class="dot"></span>Portfolio</span>
<h1>Work across <em>Mumbai and beyond.</em></h1>
<p class="lede">A selection of named projects. Renders are labelled as renders; photography of completed work is being collected.</p>
</div>
<section style="padding-top:6px">
<div class="pgrid">
<div class="pcard"><img src="assets/img/amravati-mall.jpg" alt="Design render of the commercial mall project in Amravati" loading="lazy"><div class="pb"><div class="t">Commercial Mall</div><div class="l">{I['pin']}Amravati</div><div class="tags"><span class="tag">Commercial</span><span class="tag render">Design render</span></div></div></div>
<div class="pcard"><img src="assets/img/pahuja.jpg" alt="Design render of Pahuja Business Avenue in Sakinaka" loading="lazy"><div class="pb"><div class="t">Pahuja Business Avenue</div><div class="l">{I['pin']}Sakinaka, Mumbai</div><div class="tags"><span class="tag">Commercial</span><span class="tag render">Design render</span></div></div></div>
<div class="pcard"><img src="assets/img/siddhanchal.jpg" alt="Design render of Siddhanchal Residency in Ghatkopar" loading="lazy"><div class="pb"><div class="t">Siddhanchal Residency</div><div class="l">{I['pin']}Ghatkopar, Mumbai</div><div class="tags"><span class="tag">Residential</span><span class="tag render">Design render</span></div></div></div>
<div class="pcard"><img src="assets/img/interior.jpg" alt="Interior design and execution work" loading="lazy"><div class="pb"><div class="t">Interior Design &amp; Execution</div><div class="l">{I['pin']}Mumbai</div><div class="tags"><span class="tag">Interiors</span></div></div></div>
</div>
<div style="margin-top:12px" class="ucard">{UC}<div class="t">Institutional and society projects</div><div class="d">Further named projects, including institutional client work, will be listed here once the company confirms what may be published.</div></div>
<div style="margin-top:12px" class="ucard">{UC}<div class="t">Case studies</div><div class="d">Per-project case studies with scope, timelines and outcomes are being prepared.</div></div>
</section>
</div>
'''
W('projects.html', page('projects.html','projects','Projects - Blue Ivy Group, Mumbai','Named projects by Blue Ivy Group: a commercial mall in Amravati, Pahuja Business Avenue in Sakinaka, Siddhanchal Residency in Ghatkopar, and interior work across Mumbai.', proj_body, active='Projects'))

# ---------------- contact ----------------
contact_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Contact</div>
<div class="head">
<span class="eyebrow"><span class="dot"></span>Contact</span>
<h1>Talk to <em>the team.</em></h1>
</div>
<section style="padding-top:6px">
<div class="cgrid">
<div class="cblock">
<h3>Reach us</h3>
<div class="cline">{I['pin']}<span>301, Excel Arcade, LBS Marg,<br>Ghatkopar West, Mumbai 400 086</span></div>
<div class="cline">{I['phone']}<a href="tel:+912225161818">022 2516 1818</a></div>
<div class="cline">{I['mail']}<a href="mailto:info@blueivygroup.in">info@blueivygroup.in</a></div>
<div class="cline">{I['li']}<a href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">linkedin.com/company/blue-ivy-group</a></div>
<div style="margin-top:12px">{UC} <span style="font-size:12.5px;color:var(--ink2)">WhatsApp line to be confirmed</span></div>
<div class="map"><iframe title="Map - Blue Ivy Group, Ghatkopar West" src="https://www.google.com/maps?q=19.087315,72.903306&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
<div class="cblock">
<h3>Request a quote</h3>
<form class="qform" id="qform">
<input name="name" autocomplete="name" placeholder="Your name" required>
<input name="phone" autocomplete="tel" inputmode="tel" placeholder="Phone" required>
<textarea name="msg" rows="5" placeholder="Tell us about the project" required></textarea>
<button type="submit">Send enquiry</button>
<div class="form-note">Opens your email app with the enquiry addressed to info@blueivygroup.in. Nothing is stored on this site.</div>
</form>
</div>
</div>
</section>
</div>
'''
W('contact.html', page('contact.html','contact','Contact - Blue Ivy Group, Ghatkopar West, Mumbai','Contact Blue Ivy Group: 301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086. Call 022 2516 1818 or email info@blueivygroup.in.', contact_body, active='Contact'))

# ---------------- services ----------------
SERVICES=[
('redevelopment','Redevelopment','Society and building redevelopment in Mumbai, handled with legal, technical and design precision - Blue Ivy Group.',
 'Society and building redevelopment, handled with legal, technical and design precision.',
 ['Permissions, planning and approvals','Structural assessment and design','Construction and interiors under one roof','Resident communication through the project'],
 'redevelopment.jpg','Redevelopment project in progress'),
('residential-construction','Residential Construction','Residential construction in Mumbai: homes, villas and gated communities built for quality and safety - Blue Ivy Group.',
 'Premium homes, villas and gated communities, built with a focus on quality, safety and elegant design.',
 ['New residential buildings and villas','Gated communities','Quality-checked materials','Milestone-based progress updates'],
 'siddhanchal.jpg','Design render of a residential project'),
('commercial-projects','Commercial Projects','Commercial construction: towers, corporate buildings, hospitals, schools, colleges and malls - Blue Ivy Group, Mumbai.',
 'High-rise towers, corporate buildings, hospitals, schools, colleges, malls and more.',
 ['Corporate and commercial buildings','Institutional buildings: hospitals, schools, colleges','Retail and mall construction','Design, approvals and execution'],
 'amravati-mall.jpg','Design render of a commercial project'),
('turnkey-construction','Turnkey Construction','Turnkey construction solutions from approvals to handover, every stage under one roof - Blue Ivy Group, Mumbai.',
 'From approvals to handover, every stage of the project managed under one roof.',
 ['Single point of responsibility','Approvals, design, construction, interiors','Transparent milestone-based billing','Handover with post-construction support'],
 'hero.jpg','A completed project by Blue Ivy Group'),
('interior-design','Interior Design & Execution','Interior design and execution for residential and commercial spaces - Blue Ivy Group, Mumbai.',
 'Full-scope interior services for residential and commercial spaces.',
 ['Space planning and design','Material selection and execution','Residential and commercial interiors','Coordination with civil work'],
 'interior.jpg','Interior design and execution work'),
('industrial-construction','Industrial Construction','Industrial construction and facility upgrades - Blue Ivy Group, Mumbai.',
 'Industrial construction, facility upgrades and transformation of existing spaces.',
 ['Industrial buildings and facilities','Upgrades and remodelling of existing spaces','Safety-first execution'],
 None,None),
('project-management-consultancy','Project Management & Consultancy','Project management and construction consultancy: planning, approvals and execution oversight - Blue Ivy Group, Mumbai.',
 'Project management and consultancy across planning, approvals and execution.',
 ['Project planning and budgeting','Approvals and compliance coordination','On-site execution oversight','Vendor and contractor management'],
 None,None),
]
for slug,name,desc,sub,scope,img,alt in SERVICES:
    media=f'<div class="svc-hero"><img src="../assets/img/{img}" alt="{alt}" loading="lazy"></div>' if img else ''
    lis=''.join(f'<li>{I["check"]}{s}</li>' for s in scope)
    body=f'''
<div class="wrap">
<div class="crumb"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#services">Services</a> &nbsp;/&nbsp; {name}</div>
<div class="head">
<span class="eyebrow"><span class="dot"></span>Service</span>
<h1>{name}</h1>
<p class="lede">{sub}</p>
{CTAS.replace('href="tel','href="tel').replace('class="icobtn','class="icobtn')}
</div>
{media}
<section>
<div class="kicker">Scope</div>
<div class="sec-h"><h2>What this covers</h2></div>
<ul class="scope">{lis}</ul>
</section>
<section>
<div class="ucard">{UC}<div class="t">Case studies and past {name.lower()} work</div><div class="d">Named examples with scope, timelines and outcomes will be published once confirmed by the company.</div></div>
</section>
</div>
'''
    W(f'services/{slug}.html', page(f'services/{slug}.html',slug,f'{name} - Blue Ivy Group, Mumbai',desc,body,depth=1,active='Services'))

# ---------------- 404 ----------------
W('404.html', page('404.html','404','Page not found - Blue Ivy Group','This page does not exist.', f'''
<div class="wrap"><div class="head">
<h1>Lost on <em>site.</em></h1>
<p class="lede">This page does not exist. The homepage has everything current.</p>
<div class="cta-row"><a class="icobtn" href="index.html">{I['home']} Go home</a></div>
</div></div>''', active=''))
print('PAGES DONE')
