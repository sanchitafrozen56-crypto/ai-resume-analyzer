# MAHADEV EVENT

**Your Vision, Our Celebration.**

A premium, responsive Streamlit website for **MAHADEV EVENT - Powered by Devendra Adhikary**. The experience is designed for weddings, pre-wedding functions, Dandiya and Garba nights, corporate events, concerts, cultural celebrations, and private parties.

## Included

- Luxury editorial hero section with event photography
- 16 image-led event management services
- Dedicated wedding and Dandiya/Garba sections
- Filterable gallery categories
- Validated event inquiry form with success feedback
- Session-based inquiry dashboard in the Streamlit sidebar
- Clickable phone, email, map, Instagram, Facebook, and WhatsApp links
- Floating WhatsApp inquiry action
- Responsive styling for desktop, tablet, and mobile layouts

## Run locally

```powershell
cd ai-resume-analyzer\mahadev-event
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal.

## Configure before launch

Edit the `PHONE`, `EMAIL`, `WHATSAPP`, and `MAP_URL` constants near the top of `app.py` with verified business details. Replace the placeholder social URLs and remote image URLs with the final business accounts and approved photography.

The inquiry form currently stores submissions in Streamlit session state so the demo works without credentials or infrastructure. For production, connect the form handler to a Node/Express or serverless endpoint backed by MongoDB, and add authentication before exposing the admin dashboard. Email delivery can be added with an SMTP provider or transactional email service at the same integration point.

## Note on business claims

The statistics are intentionally marked as editable planning placeholders. Replace them with verified business data before publishing them as achievements.