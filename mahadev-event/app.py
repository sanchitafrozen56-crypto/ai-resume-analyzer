"""Streamlit entry point for MAHADEV EVENT."""
from __future__ import annotations

from datetime import date

import streamlit as st


st.set_page_config(page_title="MAHADEV EVENT | Your Vision, Our Celebration", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")

PHONE = "8210529582"
SECONDARY_PHONE = "6207872146"
EMAIL = "hello@mahadevevent.in"
WHATSAPP = "https://wa.me/918210529582"
INSTAGRAM = "https://www.instagram.com/mahadev_event_management123?mdxt=cDhhcWloN2poZ2tn"
MAP_URL = "RANCHI JHARKHAND INDIA"

SERVICES = [
    ("01", "Wedding Planning & Management", "A beautifully orchestrated wedding, from first moodboard to final farewell.", "https://images.unsplash.com/photo-1519741497674-611481863552?w=1200&q=85"),
    ("02", "Pre-Wedding Functions", "Intimate haldi, mehendi and cocktail celebrations with a signature point of view.", "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?w=1200&q=85"),
    ("03", "Engagement Ceremony", "A refined beginning designed around the people and story you want to celebrate.", "https://images.unsplash.com/photo-1606800052052-a08af7148866?w=1200&q=85"),
    ("04", "Haldi & Mehendi Ceremony", "Colour, florals, music and joyful details for the most loved pre-wedding days.", "https://images.unsplash.com/photo-1606216794074-735e91aa2c92?w=1200&q=85"),
    ("05", "Sangeet Night", "Choreographed energy, cinematic production and a night your guests will replay.", "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=1200&q=85"),
    ("06", "Reception & Grand Wedding", "Regal settings, warm hospitality and seamless guest experiences at every scale.", "https://images.unsplash.com/photo-1544078751-58fee2d8a03b?w=1200&q=85"),
    ("07", "Dandiya & Garba Nights", "High-energy celebrations with exceptional sound, lighting, artists and crowd flow.", "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200&q=85"),
    ("08", "Navratri Celebrations", "Tradition meets spectacle in a festive experience made for the whole city.", "https://images.unsplash.com/photo-1604608672516-f1b9d1c9a9dc?w=1200&q=85"),
    ("09", "Birthday Parties", "Personal, playful and polished parties that feel unmistakably yours.", "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=1200&q=85"),
    ("10", "Anniversary Celebrations", "Meaningful milestones wrapped in atmosphere, taste and effortless hosting.", "https://images.unsplash.com/photo-1519225421980-715cb0215aed?w=1200&q=85"),
    ("11", "College Festivals", "Big stages, safe operations and electric programming for young audiences.", "https://images.unsplash.com/photo-1506157786151-b8491531f063?w=1200&q=85"),
    ("12", "Corporate Events", "Brand-led experiences that make teams connect and businesses stand apart.", "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=1200&q=85"),
    ("13", "Concerts & Live Shows", "Production-led live entertainment with the detail behind the spectacle.", "https://images.unsplash.com/photo-1501386761578-eac5c94b800a?w=1200&q=85"),
    ("14", "DJ Nights & Musical Events", "A magnetic sound and light experience built for the last song.", "https://images.unsplash.com/photo-1571266028243-d220c9c3b4e8?w=1200&q=85"),
    ("15", "Religious & Cultural Events", "Respectful, rooted celebrations delivered with calm, capable planning.", "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=1200&q=85"),
    ("16", "Private Parties", "An unforgettable room, a generous host experience and not a detail out of place.", "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=1200&q=85"),
]

GALLERY = {
    "Weddings": [SERVICES[0][3], SERVICES[2][3], SERVICES[5][3], SERVICES[3][3]],
    "Dandiya Nights": [SERVICES[6][3], SERVICES[7][3], SERVICES[13][3], SERVICES[12][3]],
    "Birthday Parties": [SERVICES[8][3], SERVICES[15][3], SERVICES[9][3], SERVICES[4][3]],
    "Corporate Events": [SERVICES[11][3], SERVICES[10][3], SERVICES[12][3], SERVICES[14][3]],
    "Cultural Events": [SERVICES[14][3], SERVICES[7][3], SERVICES[6][3], SERVICES[5][3]],
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');
:root { --ink:#160f0c; --maroon:#4b1018; --gold:#c89a50; --gold-light:#e4c384; --cream:#f6f0e7; --muted:#8d8177; --line:rgba(200,154,80,.25); }
.stApp { background:var(--ink); color:var(--cream); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1400px; padding:0 4rem 5rem; }
header[data-testid="stHeader"] { background:transparent; }
[data-testid="stSidebar"] { background:#21110f; border-right:1px solid var(--line); }
h1,h2,h3,h4 { font-family:'Cormorant Garamond',serif !important; color:var(--cream) !important; letter-spacing:0 !important; }
.hero { min-height:650px; display:flex; align-items:flex-end; padding:7rem 0 5rem; position:relative; background:linear-gradient(90deg,rgba(22,15,12,.98) 0%,rgba(22,15,12,.78) 42%,rgba(22,15,12,.15)),url('https://images.unsplash.com/photo-1519741497674-611481863552?w=2000&q=90') center/cover; border-bottom:1px solid var(--line); }
.eyebrow { color:var(--gold-light); text-transform:uppercase; letter-spacing:.24em; font-size:.72rem; font-weight:600; }
.hero h1 { font-size:clamp(4rem,8vw,8.5rem) !important; line-height:.82; max-width:800px; margin:1.5rem 0; }
.hero p { max-width:620px; color:#dacfc2; font-size:1.1rem; line-height:1.7; }
.brandmark { color:var(--gold-light); font-family:'Cormorant Garamond',serif; font-size:1.7rem; font-weight:700; letter-spacing:.14em; }
.brandline { display:flex; justify-content:space-between; align-items:center; padding:1.5rem 0; border-bottom:1px solid var(--line); }
.powered { font-size:.68rem; letter-spacing:.16em; text-transform:uppercase; color:var(--muted); }
.powered strong { color:var(--gold-light); font-weight:500; }
.section { padding:6rem 0 1rem; }
.section-title { font-size:clamp(2.8rem,5vw,5.4rem) !important; line-height:.9; margin:.6rem 0 1.5rem; }
.section-copy { color:var(--muted); line-height:1.7; max-width:620px; }
.gold-rule { width:80px; height:2px; background:var(--gold); margin:1.5rem 0; }
.service-card { background:#211614; border:1px solid rgba(200,154,80,.15); margin-bottom:1.4rem; overflow:hidden; transition:transform .3s ease,border .3s ease; }
.service-card:hover { transform:translateY(-5px); border-color:var(--gold); }
.service-card img { width:100%; height:220px; object-fit:cover; filter:saturate(.8); }
.service-body { padding:1.3rem 1.3rem 1.5rem; }
.service-number { color:var(--gold); font-size:.7rem; letter-spacing:.14em; }
.service-card h3 { font-size:1.7rem !important; margin:.35rem 0 .4rem; }
.service-card p { color:var(--muted); font-size:.88rem; line-height:1.6; min-height:68px; }
.pill { display:inline-block; padding:.4rem .8rem; border:1px solid var(--line); color:var(--gold-light); font-size:.68rem; letter-spacing:.1em; text-transform:uppercase; }
.feature-band { background:linear-gradient(120deg,var(--maroon),#250d13); margin:5rem -4rem 0; padding:5rem 4rem; border-top:1px solid var(--line); border-bottom:1px solid var(--line); }
.feature-list { color:#dacfc2; line-height:2.1; columns:2; padding-left:1.2rem; }
.stat { border-top:1px solid var(--line); padding-top:1rem; }
.stat strong { display:block; font-family:'Cormorant Garamond',serif; color:var(--gold-light); font-size:3.5rem; line-height:1; }
.stat span { color:var(--muted); font-size:.75rem; text-transform:uppercase; letter-spacing:.12em; }
.quote { padding:3rem; border:1px solid var(--line); background:rgba(75,16,24,.38); text-align:center; }
.quote p { font-family:'Cormorant Garamond',serif; font-size:2rem; line-height:1.1; color:var(--cream); }
.quote span { color:var(--gold-light); font-size:.75rem; letter-spacing:.15em; text-transform:uppercase; }
.contact-band { background:var(--cream); color:var(--ink); margin:6rem -4rem 0; padding:5rem 4rem 3rem; }
.contact-band h2 { color:var(--ink) !important; }
.contact-band p,.contact-band a { color:#634c40; }
.footer { padding:2rem 0; color:var(--muted); font-size:.75rem; display:flex; justify-content:space-between; border-top:1px solid var(--line); }
.whatsapp { position:fixed; right:1.5rem; bottom:1.5rem; z-index:10; background:#b89555; color:#160f0c !important; border-radius:50%; width:56px; height:56px; display:flex; align-items:center; justify-content:center; font-size:1.35rem; text-decoration:none; box-shadow:0 8px 24px rgba(0,0,0,.4); }
.stButton > button { border-radius:0; border:1px solid var(--gold); background:transparent; color:var(--gold-light); padding:.75rem 1.2rem; font-size:.72rem; letter-spacing:.13em; text-transform:uppercase; }
.stButton > button:hover { background:var(--gold); color:var(--ink); border-color:var(--gold); }
div[data-testid="stForm"] { background:#211614; border:1px solid var(--line); padding:2rem; }
label { color:var(--gold-light) !important; }
input,textarea,[data-baseweb="select"] > div { background:#160f0c !important; color:var(--cream) !important; border-color:var(--line) !important; border-radius:0 !important; }
@media (max-width:760px) { .block-container { padding:0 1.2rem 3rem; } .hero { min-height:600px; padding:5rem 0 3rem; } .hero h1 { font-size:4rem !important; } .feature-band,.contact-band { margin-left:-1.2rem; margin-right:-1.2rem; padding-left:1.2rem; padding-right:1.2rem; } .feature-list { columns:1; } .brandline { display:block; } .powered { margin-top:.5rem; } .footer { display:block; } }
</style>
""", unsafe_allow_html=True)

if "inquiries" not in st.session_state:
    st.session_state.inquiries = []

st.markdown('<div class="brandline"><div class="brandmark">✦ MAHADEV EVENT</div><div class="powered">Powered by <strong>Devendra Adhikary</strong></div></div>', unsafe_allow_html=True)
st.markdown('<div class="hero"><div><div class="eyebrow">Luxury event management · Ahmedabad & beyond</div><h1>WE CREATE<br><em>MOMENTS</em><br>THAT LAST.</h1><p>Your vision, our celebration. From grand weddings to electrifying Dandiya nights, we make every celebration extraordinary.</p></div></div></div>', unsafe_allow_html=True)

nav_a, nav_b, nav_c = st.columns([1, 1, 1])
with nav_a:
    if st.button("Explore our events", key="hero_explore", use_container_width=True):
        st.session_state.scroll_target = "services"
with nav_b:
    if st.button("Book your event", key="hero_book", use_container_width=True):
        st.session_state.scroll_target = "inquiry"
with nav_c:
    st.markdown('<a class="pill" href="#contact">✦ Available for 2026 celebrations</a>', unsafe_allow_html=True)

st.markdown('<div id="services" class="section"><div class="eyebrow">What we do</div><h2 class="section-title">THE ART OF<br>CELEBRATION.</h2><div class="gold-rule"></div><p class="section-copy">A thoughtful, end-to-end event house for celebrations with character. We bring together creative direction, meticulous production and generous hospitality.</p></div>', unsafe_allow_html=True)

for row_start in range(0, len(SERVICES), 4):
    cols = st.columns(4, gap="medium")
    for col, (number, title, description, image) in zip(cols, SERVICES[row_start:row_start + 4]):
        with col:
            st.markdown(f'<div class="service-card"><img src="{image}" alt="{title}"><div class="service-body"><div class="service-number">{number}</div><h3>{title}</h3><p>{description}</p></div></div>', unsafe_allow_html=True)
            if st.button("Explore more", key=f"service_{number}", use_container_width=True):
                st.session_state.selected_service = title

st.markdown('<div class="feature-band"><div class="eyebrow">The wedding edit</div><h2 class="section-title">YOUR ONCE-IN-A-<br>LIFETIME, ELEVATED.</h2><p class="section-copy">For the days that deserve more than a checklist. We design the feeling, then engineer every moment around it.</p><div class="gold-rule"></div>', unsafe_allow_html=True)
features = ["Royal Wedding Decorations", "Floral Decorations", "Stage Decorations", "Wedding Entry Design", "Mandap Decorations", "Bride & Groom Entry", "Wedding Photography", "Catering Management", "Lighting & Sound", "Complete Wedding Planning"]
st.markdown("<ul class='feature-list'>" + "".join(f"<li>{item}</li>" for item in features) + "</ul></div>", unsafe_allow_html=True)

st.markdown('<div class="section"><div class="eyebrow">The festive edit</div><h2 class="section-title">TURN UP<br>THE COLOUR.</h2><p class="section-copy">From traditional Garba circles to an all-out DJ Dandiya night, our festive productions are built for belonging, movement and memories.</p></div>', unsafe_allow_html=True)
festive_cols = st.columns([1.2, 1, 1])
with festive_cols[0]:
    st.image(SERVICES[6][3], use_container_width=True)
with festive_cols[1]:
    st.markdown('<div class="stat"><strong>09</strong><span>Festive formats</span></div><br><div class="stat"><strong>∞</strong><span>Reasons to dance</span></div>', unsafe_allow_html=True)
with festive_cols[2]:
    st.markdown('<ul class="feature-list"><li>Navratri Dandiya Nights</li><li>Traditional Garba Events</li><li>DJ Dandiya Nights</li><li>Celebrity Performances</li><li>Live Music & Dance</li><li>LED Screens & Lighting</li><li>Food Stalls</li><li>Ticket Management</li></ul>', unsafe_allow_html=True)

st.markdown('<div class="section"><div class="eyebrow">Selected work</div><h2 class="section-title">A LITTLE<br>INSPIRATION.</h2></div>', unsafe_allow_html=True)
gallery_category = st.selectbox("Gallery category", list(GALLERY), label_visibility="collapsed")
gallery_cols = st.columns(4)
for col, image in zip(gallery_cols, GALLERY[gallery_category]):
    with col:
        st.image(image, use_container_width=True)

st.markdown('<div class="section"><div class="eyebrow">The Mahadev standard</div><h2 class="section-title">CREATING EXPERIENCES,<br>CRAFTING MEMORIES.</h2><p class="section-copy">MAHADEV EVENT is a professional event management brand dedicated to transforming ideas into unforgettable celebrations. From intimate gatherings to grand weddings and large-scale cultural events, we bring creativity, planning, passion, and perfection to every occasion.</p></div>', unsafe_allow_html=True)
stats = st.columns(4)
for col, number, label in zip(stats, ["100+", "50+", "20+", "100%"], ["Events managed", "Happy clients", "Wedding celebrations", "Dedication"]):
    with col:
        st.markdown(f'<div class="stat"><strong>{number}</strong><span>{label}*</span></div>', unsafe_allow_html=True)
st.caption("* Planning targets and editable placeholders until verified business data is supplied.")

st.markdown('<div class="section"><div class="quote"><p>“The best celebrations feel effortless because someone cared about every detail.”</p><span>Our promise to every host</span></div></div>', unsafe_allow_html=True)

st.markdown('<div id="inquiry" class="section"><div class="eyebrow">Let’s make it remarkable</div><h2 class="section-title">TELL US<br>YOUR VISION.</h2><p class="section-copy">Share a few details and our team will get back to you with a considered first conversation.</p></div>', unsafe_allow_html=True)
with st.form("event_inquiry"):
    name_col, phone_col = st.columns(2)
    name = name_col.text_input("Customer name *")
    phone = phone_col.text_input("Phone number *")
    email_col, type_col = st.columns(2)
    email = email_col.text_input("Email address *")
    event_type = type_col.selectbox("Event type *", ["Wedding", "Pre-wedding function", "Dandiya / Garba", "Corporate event", "Birthday party", "Concert / live show", "Other"])
    date_col, location_col, guest_col = st.columns(3)
    event_date = date_col.date_input("Event date", min_value=date.today())
    location = location_col.text_input("Event location")
    guests = guest_col.number_input("Expected guests", min_value=1, max_value=100000, value=100, step=10)
    budget = st.selectbox("Budget range", ["Let's discuss", "₹2L – ₹5L", "₹5L – ₹10L", "₹10L – ₹25L", "₹25L+"])
    message = st.text_area("Message / requirements", height=120)
    submitted = st.form_submit_button("Book your event", use_container_width=True)
    if submitted:
        if not name.strip() or not phone.strip() or not email.strip() or "@" not in email:
            st.error("Please add your name, phone number and a valid email address.")
        else:
            st.session_state.inquiries.append({"name": name, "phone": phone, "email": email, "event": event_type, "date": str(event_date), "location": location, "guests": guests, "budget": budget, "message": message})
            st.success("Thank you. Your event inquiry is with the Mahadev Event team.")

st.markdown('<div id="contact" class="contact-band"><div class="eyebrow">Start a conversation</div><h2 class="section-title">LET’S MAKE<br>IT UNFORGETTABLE.</h2><p>MAHADEV EVENT · Powered by Devendra Adhikary</p><p><a href="tel:+918210529582">' + PHONE + '</a> · <a href="tel:+916207872146">' + SECONDARY_PHONE + '</a> · <a href="mailto:' + EMAIL + '">' + EMAIL + '</a> · <a href="' + MAP_URL + '" target="_blank">Ahmedabad, Gujarat</a></p><p><a href="' + INSTAGRAM + '" target="_blank">Instagram</a> · <a href="https://facebook.com/" target="_blank">Facebook</a> · <a href="' + WHATSAPP + '" target="_blank">WhatsApp</a></p></div>', unsafe_allow_html=True)
st.markdown('<div class="footer"><span>© 2026 MAHADEV EVENT</span><span>Your Vision, Our Celebration.</span></div>', unsafe_allow_html=True)
st.markdown(f'<a class="whatsapp" href="{WHATSAPP}" target="_blank" title="Chat on WhatsApp">☏</a>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## MAHADEV EVENT")
    st.caption("Private admin view")
    if st.checkbox("Show inquiry dashboard"):
        st.metric("Inquiries this session", len(st.session_state.inquiries))
        for inquiry in st.session_state.inquiries:
            st.write(f"**{inquiry['name']}** · {inquiry['event']}")
            st.caption(f"{inquiry['email']} · {inquiry['date']}")
        if not st.session_state.inquiries:
            st.info("New inquiries will appear here.")
    st.divider()
    st.caption("Contact details are configured in app.py. Update the email, address and Facebook link before launch.")