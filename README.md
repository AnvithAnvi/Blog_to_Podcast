# 🎧 Blog to Podcast Agent

**Blog to Podcast Agent** is a Streamlit-based AI application that converts any public blog post into an engaging podcast episode.  
It uses **OpenAI GPT-4** for summarization, **Firecrawl API** for scraping blog content, and **ElevenLabs** for realistic voice narration.  

Turn written blogs into immersive audio experiences in seconds 🎙️

---

## 🧠 Features
- 🕸️ Smart Blog Scraping (Firecrawl + BeautifulSoup fallback)
- ✍️ AI Summarization using GPT-4
- 🎤 Podcast Generation via ElevenLabs
- 💾 MP3 Download Support
- 🔒 Secure API key handling with .env or Streamlit Secrets
- ⚙️ Works locally and on Streamlit Cloud

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/<your-username>/blog_to_podcast.git
cd blog_to_podcast
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Create a `.env` file:
```
OPENAI_API_KEY=sk-your-key
FIRECRAWL_API_KEY=fc-your-key
ELEVENLABS_API_KEY=sk-your-key
```

### Run the app:
```bash
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud

1. Push this repo to GitHub  
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App** → choose repo → set main file path as `app.py`
4. Add your keys in **Settings → Edit Secrets**:

```toml
OPENAI_API_KEY = "sk-your-openai-key"
FIRECRAWL_API_KEY = "fc-your-firecrawl-key"
ELEVENLABS_API_KEY = "sk-your-elevenlabs-key"
```

---

## 🧾 Project Structure
```
blog_to_podcast/
│
├── app.py
├── requirements.txt
├── .env
└── utils/
    ├── scrape_blog.py
    ├── summarize_blog.py
    └── generate_podcast.py
```
---

## 👨‍💻 Author
**Krishna Anvith Vattikuti** 
