
# MemeTruth — Laugh at the Meme. Check the Facts.

**An AI-powered meme fact-checking tool by Team Runtime Rebel**

MemeTruth helps users check the information behind memes and viral text. It aims to bridge the gap between humor and truth by helping people question claims before believing or sharing them.

---

## 📌 Problem Statement

People often remember the joke in a meme but forget whether the information behind it is actually true.

Memes make information entertaining and easy to share, but factual claims hidden behind humor may go unchecked. This can allow misleading information to spread.

## 💡 Our Solution

MemeTruth bridges the gap between humor and truth.

It allows users to upload a meme image or enter text and receive an AI-generated fact-checking assessment, an explanation, and supporting sources where available.

Our goal is to make fact-checking more accessible and encourage responsible information sharing.

---

## ✨ Features

- **Meme Image Analysis:** Upload a meme image for analysis.
- **Text Fact-Checking:** Enter a claim, caption, or text to investigate.
- **AI-Powered Analysis:** Use Google's Gemini API to analyze submitted content.
- **Web Search Grounding:** Use Google Search grounding when supported by the configured model.
- **Verdict and Explanation:** Display an assessment with a readable explanation.
- **Source Links:** Show supporting sources when available.
- **Uncertainty and Limitations:** Highlight cases where a claim cannot be confidently verified.
- **Downloadable Report:** Download the analysis report for later reference.

> Note: AI-generated assessments may be incorrect or incomplete. Users should review available sources and independently verify important claims.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language and application logic |
| Streamlit | Web application interface |
| Google Gemini API | AI-powered content analysis |
| Google Search grounding | Web-grounded information, where supported |
| Python Requests | HTTP communication with the API |
| Streamlit Community Cloud | Deployment platform |

### Why Python?

Python powers the main application in `app.py`. It handles user inputs, communicates with the Gemini API, processes the response, and displays the results through Streamlit.

Streamlit allows us to build an interactive website using Python.

---

## 🔄 How It Works

1. **User Input:** The user uploads a meme image or enters text.
2. **Content Processing:** The application prepares the submitted content for analysis.
3. **AI Analysis:** The application sends a request to the configured Gemini model.
4. **Fact-Checking:** The model analyzes the claim and may use Google Search grounding, where available.
5. **Results:** MemeTruth displays the assessment, explanation, limitations, and available sources.
6. **Report:** The user can download the analysis report.

---

## 📁 Project Structure

```text
MemeTruth/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

**Important:** The `.streamlit/secrets.toml` file is for local secrets. Do not upload it to GitHub.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.12 recommended
- Git
- A Google Gemini API key
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/gayatrissuryawanshi/MemeTruth.git
cd MemeTruth
```

### Step 2: Create a Virtual Environment

On Windows:

```bash
py -3.12 -m venv .venv
```

Activate it using Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Or using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt or run the virtual environment's Python executable directly.

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Configure the Gemini API Key

Get an API key from Google AI Studio:

https://aistudio.google.com/

For local Streamlit configuration, create the file:

`.streamlit/secrets.toml`

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your actual API key.

**Security:** Never commit your real API key, `.env`, or `secrets.toml` to GitHub.

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL provided by Streamlit. It is usually:

```text
http://localhost:8501
```

---

## 🔑 API Configuration and Troubleshooting

MemeTruth requires a valid Gemini API key for AI-powered analysis.

The configured Gemini model must be available to your API key and compatible with the application's request format.

| Issue | What to Check |
|---|---|
| Invalid API key | Confirm that the key is correct and active |
| Model not found | Configure a model supported by your API key |
| Quota exceeded (429) | Check your API quota and usage limits |
| Network error | Check your internet connection |
| Sources not displayed | Search grounding and source availability may vary |

API access and usage limits depend on the account, model, and current Google API quota.

---

## ☁️ Deployment

MemeTruth can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to GitHub.
2. Visit https://share.streamlit.io/
3. Sign in with GitHub.
4. Select the `MemeTruth` repository.
5. Select `app.py` as the main file.
6. Add the required API key in the app's secrets settings.
7. Deploy the application.
8. Test the deployed app, including image uploads, text analysis, API responses, and report downloads.

### Streamlit Cloud Secrets

Add the following in the app's secrets settings:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

If your application uses a configurable model name, ensure that the configured model matches the one used by `app.py`.

**Deployment status:** Deployment instructions are included. The project should be described as live only after deployment succeeds and the deployed application has been tested.

---

## 👥 Team Runtime Rebel

We are Team Runtime Rebel, working to make fact-checking more accessible in the age of viral memes.

| Team Member | Responsibility |
|---|---|
| Gayatri | Team coordination and project integration |
| Sneha | UI and user experience |
| Janhvi | Setup and deployment |
| Sharayu | Evidence review, testing, and demo preparation |

---

## 🎯 Project Objective

Our objective is to encourage users to think critically about information shared through memes and viral content.

MemeTruth aims to make fact-checking approachable and understandable, helping users distinguish between entertaining content and claims that require verification.

---

## 🔮 Future Scope

- Improve claim extraction from complex meme images.
- Add multilingual meme and text analysis.
- Improve source quality and source comparison.
- Provide clearer confidence and uncertainty indicators.
- Add a history of previous fact-checks.
- Improve performance, accessibility, and mobile usability.
- Expand testing for misleading, ambiguous, and context-dependent claims.

---

## ⚠️ Disclaimer

MemeTruth is an educational prototype and should not be treated as an authoritative source of truth.

AI systems can misunderstand sarcasm, context, or factual claims and may produce inaccurate explanations. Search results may also be incomplete or unreliable.

Always review available evidence and consult trustworthy sources before making decisions based on a fact-check.

---

## 📄 License

No license has been specified yet. A license can be added later to define how others may use, modify, and distribute this project.

---

**MemeTruth — Laugh at the Meme. Check the Facts.**

*Built with curiosity by Team Runtime Rebel.*