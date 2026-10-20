# -*- coding: utf-8 -*-
import os
R=os.environ.get('OUT','.')
BASE='https://5hu3hendu.github.io/blue-ivy-group'

LOGO='''<svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true"><rect x="1" y="1" width="28" height="28" rx="8" fill="#0e1a1f"/><path d="M9 21V9h4.2c2.4 0 3.8 1.1 3.8 2.9 0 1.2-.6 2.1-1.7 2.5 1.5.3 2.3 1.4 2.3 2.9 0 2.1-1.6 3.7-4.1 3.7H9zm2.6-7h1.4c1 0 1.6-.5 1.6-1.4s-.6-1.3-1.6-1.3h-1.4V14zm0 4.7h1.7c1.1 0 1.8-.6 1.8-1.6 0-1-.7-1.5-1.8-1.5h-1.7v3.1z" fill="#e9e4d8"/><path d="M20.4 9h2.5v12h-2.5z" fill="#2e9e6b"/></svg>'''

I={
'phone':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
'mail':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/></svg>',
'li':'<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.55V9h3.57v11.45z"/></svg>',
'pin':'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
'arr':'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
'check':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
'star':'<svg width="15" height="15" viewBox="0 0 24 24" fill="#d97706" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.2 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8z"/></svg>',
'menu':'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
'x':'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>',
'chev':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
}

NAV=[('index.html','Home'),('index.html#services','Services'),('projects.html','Projects'),('about.html','About'),('contact.html','Contact')]

def page(path, title, desc, body, depth=0, extra_head='', active='', inner=True, absolute=False):
    p='/blue-ivy-group/' if absolute else '../'*depth
    navd=''.join('<a href="%s%s"%s>%s</a>' % (p,h,' class="on"' if t==active else '',t) for h,t in NAV)
    mlinks=''.join('<a href="%s%s"%s>%s</a>' % (p,h,' class="on"' if t==active else '',t) for h,t in NAV)
    bodycls=' class="inner"' if inner else ''
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
<meta name="theme-color" content="#0c110e">
<link rel="icon" href="{p}assets/img/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="{p}assets/img/icon-180.png">
<link rel="manifest" href="{p}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
{extra_head}
</head>
<body{bodycls}>
<header class="topbar" id="topbar"><div class="wrap topbar-in">
<a class="brand" href="{p}index.html">{LOGO}<span class="wm">Blue Ivy Group</span></a>
<nav class="nav-d" aria-label="Main">{navd}</nav>
<div class="hact">
<a class="hico" href="tel:+912225161818" aria-label="Call Blue Ivy Group">{I['phone']}</a>
<button class="hico" id="menuBtn" aria-label="Open menu" type="button">{I['menu']}</button>
</div>
</div></header>
<div class="menu" id="menu" aria-hidden="true">
<button class="mclose" id="menuClose" aria-label="Close menu" type="button">{I['x']}</button>
<nav class="mlinks" aria-label="Menu">{mlinks}</nav>
<div class="mfoot"><a href="tel:+912225161818">022 2516 1818</a><a href="mailto:info@blueivygroup.in">info@blueivygroup.in</a><span>301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086</span></div>
</div>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="foot">
<a class="l" href="{p}index.html">{LOGO}<span>Blue Ivy Group</span></a>
<div class="r">301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086<br>&copy; 2026 Blue Ivy Group</div>
</div>
<div class="demo">Redesign concept demo. Official site: <a href="https://blueivygroup.in/" style="color:var(--ivy);font-weight:600">blueivygroup.in</a>. Sections marked as awaiting confirmation are placeholders until the company confirms the details.</div>
</div></footer>
<script src="{p}assets/js/main.js" defer></script>
</body>
</html>'''

def W(path, html):
    fp=os.path.join(R,path); os.makedirs(os.path.dirname(os.path.abspath(fp)),exist_ok=True)
    open(fp,'w').write(html); print('wrote',path,len(html)//1024,'KB')

UCL='<span class="ucl">Awaiting confirmed information</span>'

CTA=f'''<div class="ctarow">
<a class="btn" href="tel:+912225161818">{I['phone']}022 2516 1818</a>
<a class="tlink" href="mailto:info@blueivygroup.in">Email the team {I['arr']}</a>
</div>'''

PROJECTS=[
('siddhanchal.jpg','Design render of Siddhanchal Residency in Ghatkopar','Siddhanchal Residency','Ghatkopar, Mumbai','Residential','Design render'),
('amravati-mall.jpg','Design render of the commercial mall project in Amravati','Commercial Mall','Amravati','Commercial','Design render'),
('pahuja.jpg','Design render of Pahuja Business Avenue in Sakinaka','Pahuja Business Avenue','Sakinaka, Mumbai','Commercial','Design render'),
('interior.jpg','Interior design and execution work','Interior Design &amp; Execution','Mumbai','Interiors',''),
]
def pitem(img,alt,name,loc,cat,cap,depth=0):
    p='../'*depth
    c=f'<div class="pc">{cap}</div>' if cap else ''
    return f'''<a class="pitem" href="{p}projects.html" data-rv>
<div class="pimg plx"><img src="{p}assets/img/{img}" alt="{alt}" loading="lazy"></div>
<div class="pt">{name}</div>
<div class="pl">{loc} &middot; {cat}</div>{c}
</a>'''

# ---------------- home ----------------
home_body=f'''
<section class="hero">
<div class="hero-img"><img src="assets/img/siddhanchal.jpg" alt="Design render of Siddhanchal Residency, Ghatkopar, at dusk" fetchpriority="high"></div>
<div class="hero-scrim"></div>
<div class="hero-txt"><div class="wrap">
<div class="hero-kick">Blue Ivy Group &middot; Ghatkopar West, Mumbai</div>
<h1>End-to-end construction, interiors and redevelopment.</h1>
</div></div>
<a class="hero-scroll" href="#statement" aria-label="Scroll to content">{I['chev']}</a>
</section>

<section class="stmt" id="statement"><div class="wrap">
<p class="big" data-rv>Based in Ghatkopar West, the firm manages residential, commercial and turnkey work across Mumbai and beyond, from approvals to handover.</p>
<div class="facts" data-rv>
<div class="fact"><div class="fv">{I['star']}<span data-count="4.3" data-dec="1">4.3</span></div><div class="fk">Google rating, 8 reviews</div></div>
<div class="fact"><div class="fv">Ghatkopar West</div><div class="fk">Excel Arcade, LBS Marg, Mumbai 400 086</div></div>
<div class="fact"><div class="fv">End to end</div><div class="fk">Approvals to handover, turnkey</div></div>
</div>
</div></section>

<section><div class="wrap">
<div class="secrow" data-rv><span class="kick">Recent work</span><a class="tlink" href="projects.html">All projects {I['arr']}</a></div>
<div class="plist">
{pitem(*PROJECTS[0])}
{pitem(*PROJECTS[1])}
{pitem(*PROJECTS[2])}
</div>
</div></section>

<section id="services"><div class="wrap">
<div class="secrow" data-rv><span class="kick">What we do</span></div>
<div class="slist">
<a class="srow" href="services/redevelopment.html" data-rv><span class="sn">01</span><span class="st">Redevelopment<small>Society and building redevelopment with legal, technical and design precision.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/residential-construction.html" data-rv><span class="sn">02</span><span class="st">Residential Construction<small>Homes, villas and gated communities, built for quality and safety.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/commercial-projects.html" data-rv><span class="sn">03</span><span class="st">Commercial Projects<small>Towers, corporate buildings, hospitals, schools, colleges and malls.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/turnkey-construction.html" data-rv><span class="sn">04</span><span class="st">Turnkey Construction<small>From approvals to handover, every stage under one roof.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/interior-design.html" data-rv><span class="sn">05</span><span class="st">Interior Design &amp; Execution<small>Full-scope interiors for residential and commercial spaces.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/industrial-construction.html" data-rv><span class="sn">06</span><span class="st">Industrial Construction<small>Industrial spaces, upgrades and facility construction.</small></span><span class="sa">{I['arr']}</span></a>
<a class="srow" href="services/project-management-consultancy.html" data-rv><span class="sn">07</span><span class="st">Project Management &amp; Consultancy<small>Planning, approvals and execution oversight for your project.</small></span><span class="sa">{I['arr']}</span></a>
</div>
</div></section>

<section><div class="wrap">
<div class="secrow" data-rv><span class="kick">People</span></div>
<div class="person" data-rv><div class="avatar">SK</div><div><div class="n">Shekhar B. Kale</div><div class="r">Director</div></div></div>
<div style="margin-top:14px" class="uc" data-rv>{UCL}<b>Full team.</b> The wider engineering and design team will be introduced here once details are confirmed.</div>
</div></section>

<section><div class="wrap">
<div class="secrow" data-rv><span class="kick">Credentials</span></div>
<div class="ucg">
<div class="uc" data-rv>{UCL}<b>GST registration.</b> The GSTIN will be published here once confirmed by the company.</div>
<div class="uc" data-rv>{UCL}<b>MahaRERA registration.</b> RERA numbers for applicable projects will be listed once confirmed.</div>
<div class="uc" data-rv>{UCL}<b>Company registration.</b> Registration details will be published once confirmed.</div>
</div>
</div></section>

<section><div class="wrap">
<div class="secrow" data-rv><span class="kick">Word of mouth</span></div>
<div class="uc" data-rv>{UCL}<b>Client words, verified first.</b> Testimonials will appear here after clients confirm them for publication. Until then, nothing is quoted.</div>
</div></section>

<section><div class="wrap">
<h2 class="big2" data-rv>Start a conversation.</h2>
<div data-rv>{CTA}</div>
<div class="clines" data-rv>
<div class="cline">{I['pin']}<span>301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086</span></div>
<div class="cline">{I['mail']}<a class="tlink" href="mailto:info@blueivygroup.in">info@blueivygroup.in</a></div>
<div class="cline">{I['li']}<a class="tlink" href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">linkedin.com/company/blue-ivy-group</a></div>
</div>
</div></section>
'''

jsonld='''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"GeneralContractor","name":"Blue Ivy Group","url":"'''+BASE+'''/","image":"'''+BASE+'''/assets/img/og-cover.jpg","telephone":"+91-22-2516-1818","email":"info@blueivygroup.in","address":{"@type":"PostalAddress","streetAddress":"301, Excel Arcade, LBS Marg, Ghatkopar West","addressLocality":"Mumbai","addressRegion":"Maharashtra","postalCode":"400086","addressCountry":"IN"},"geo":{"@type":"GeoCoordinates","latitude":19.087315,"longitude":72.903306},"sameAs":["https://www.linkedin.com/company/blue-ivy-group","https://blueivygroup.in/"]}
</script>'''

W('index.html', page('index.html','Blue Ivy Group - Construction, Interiors & Redevelopment in Mumbai','Blue Ivy Group is a Mumbai construction, interiors and redevelopment firm based in Ghatkopar West. Residential, commercial and turnkey projects, managed end to end.', home_body, active='Home', inner=False, extra_head=jsonld))

# ---------------- about ----------------
about_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; About</div>
<div class="head">
<span class="kick">About</span>
<h1>The group behind the work.</h1>
</div>
<div class="split">
<div class="prose" data-rv>
<p><b>Blue Ivy Group</b> is a construction, interiors and redevelopment firm working from Ghatkopar West, Mumbai. The firm takes on residential, commercial, redevelopment, turnkey and interior projects, and manages them from approvals through handover.</p>
<p>Recent and ongoing work spans Mumbai and beyond, including a commercial mall in Amravati, Pahuja Business Avenue in Sakinaka and Siddhanchal Residency in Ghatkopar.</p>
<p>The office is at 301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086, reachable on 022 2516 1818 and info@blueivygroup.in.</p>
</div>
<div data-rv>
<div class="facts2">
<div class="row"><span class="k">Based in</span><span class="v">Ghatkopar West, Mumbai</span></div>
<div class="row"><span class="k">Phone</span><span class="v">022 2516 1818</span></div>
<div class="row"><span class="k">Email</span><span class="v">info@blueivygroup.in</span></div>
<div class="row"><span class="k">Google rating</span><span class="v">4.3 (8 reviews)</span></div>
<div class="row"><span class="k">LinkedIn</span><span class="v"><a class="tlink" href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">blue-ivy-group</a></span></div>
</div>
<div style="margin-top:12px" class="uc">{UCL}<b>Founding year, registrations, team size.</b> Company milestones and registration details will be published here once confirmed.</div>
</div>
</div>
<section>
<div class="secrow" data-rv><span class="kick">People</span></div>
<div class="person" data-rv><div class="avatar">SK</div><div><div class="n">Shekhar B. Kale</div><div class="r">Director</div></div></div>
<div style="margin-top:14px" class="uc" data-rv>{UCL}<b>Full team.</b> Profiles of the engineering, design and site teams will be added once confirmed.</div>
</section>
</div>
'''
W('about.html', page('about.html','About - Blue Ivy Group, Mumbai','About Blue Ivy Group: a construction, interiors and redevelopment firm from Ghatkopar West, Mumbai, led by Director Shekhar B. Kale.', about_body, active='About'))

# ---------------- projects ----------------
proj_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Projects</div>
<div class="head">
<span class="kick">Portfolio</span>
<h1>Named projects.</h1>
<p class="lede">A selection of current work. Renders are labelled as renders; photography of completed work is being collected.</p>
</div>
<section style="padding-top:22px">
<div class="plist">
{pitem(*PROJECTS[0])}
{pitem(*PROJECTS[1])}
{pitem(*PROJECTS[2])}
{pitem(*PROJECTS[3])}
</div>
<div style="margin-top:26px" class="uc" data-rv>{UCL}<b>Institutional and society projects.</b> Further named projects, including institutional client work, will be listed here once the company confirms what may be published.</div>
<div style="margin-top:12px" class="uc" data-rv>{UCL}<b>Case studies.</b> Per-project case studies with scope, timelines and outcomes are being prepared.</div>
</section>
</div>
'''
W('projects.html', page('projects.html','Projects - Blue Ivy Group, Mumbai','Named projects by Blue Ivy Group: a commercial mall in Amravati, Pahuja Business Avenue in Sakinaka, Siddhanchal Residency in Ghatkopar, and interior work across Mumbai.', proj_body, active='Projects'))

# ---------------- contact ----------------
contact_body=f'''
<div class="wrap">
<div class="crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Contact</div>
<div class="head">
<span class="kick">Contact</span>
<h1>Start a conversation.</h1>
</div>
<section style="padding-top:18px">
<div class="cgrid">
<div class="cblock" data-rv>
<h3>Reach us</h3>
<div class="clines">
<div class="cline">{I['pin']}<span>301, Excel Arcade, LBS Marg,<br>Ghatkopar West, Mumbai 400 086</span></div>
<div class="cline">{I['phone']}<a class="tlink" href="tel:+912225161818">022 2516 1818</a></div>
<div class="cline">{I['mail']}<a class="tlink" href="mailto:info@blueivygroup.in">info@blueivygroup.in</a></div>
<div class="cline">{I['li']}<a class="tlink" href="https://www.linkedin.com/company/blue-ivy-group" rel="noopener">linkedin.com/company/blue-ivy-group</a></div>
</div>
<div style="margin-top:12px" class="uc">{UCL}<b>WhatsApp line.</b> A WhatsApp number will be published once confirmed.</div>
<div class="map"><iframe title="Map - Blue Ivy Group, Ghatkopar West" src="https://www.google.com/maps?q=19.087315,72.903306&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
<div class="cblock" data-rv>
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
W('contact.html', page('contact.html','Contact - Blue Ivy Group, Ghatkopar West, Mumbai','Contact Blue Ivy Group: 301, Excel Arcade, LBS Marg, Ghatkopar West, Mumbai 400 086. Call 022 2516 1818 or email info@blueivygroup.in.', contact_body, active='Contact'))

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
    media=f'<div class="svc-hero" data-rv><img src="../assets/img/{img}" alt="{alt}" loading="lazy"></div>' if img else ''
    lis=''.join(f'<li>{I["check"]}{s}</li>' for s in scope)
    body=f'''
<div class="wrap">
<div class="crumb"><a href="../index.html">Home</a> &nbsp;/&nbsp; <a href="../index.html#services">Services</a> &nbsp;/&nbsp; {name}</div>
<div class="head">
<span class="kick">Service</span>
<h1>{name}</h1>
<p class="lede">{sub}</p>
{CTA}
</div>
{media}
<section>
<div class="secrow" data-rv><span class="kick">Scope</span></div>
<ul class="scope" data-rv>{lis}</ul>
</section>
<section>
<div class="uc" data-rv>{UCL}<b>Case studies and past {name.lower()} work.</b> Named examples with scope, timelines and outcomes will be published once confirmed by the company.</div>
</section>
</div>
'''
    W(f'services/{slug}.html', page(f'services/{slug}.html',f'{name} - Blue Ivy Group, Mumbai',desc,body,depth=1,active='Services'))

# ---------------- 404 (absolute paths + trailing-slash redirect) ----------------
redir='''<script>(function(){var p=location.pathname;if(p.length>1&&p.charAt(p.length-1)==='/'){var q=p.replace(/\\/+$/,'');location.replace(q+'.html'+location.search+location.hash);}})();</script>'''
W('404.html', page('404.html','Page not found - Blue Ivy Group','This page does not exist.', redir+f'''
<div class="wrap"><div class="head" style="padding-top:80px">
<h1>Lost on site.</h1>
<p class="lede">This page does not exist. The homepage has everything current.</p>
<div class="ctarow"><a class="btn" href="/blue-ivy-group/index.html">Go home</a></div>
</div></div>''', active='', absolute=True))
print('PAGES DONE')
