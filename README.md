# MemeTruth — Crack the Clock starter

A single-page Streamlit prototype for the challenge: identify the factual claim behind a meme, use Gemini with Google Search grounding to look for evidence, and show a verdict with source links.

## Included features
- Meme image upload (PNG/JPG/JPEG/WEBP) and optional context
- Text-only claim input
- Gemini multimodal analysis
- Google Search grounding for evidence retrieval
- Verdict, explanation, limitations, and source links
- Downloadable fact-check result
- Responsive, playful retro/comic UI
- Ready for Streamlit Community Cloud deployment

## Important
This is a competition prototype, not a definitive fact-checking authority. AI may misread a meme or misinterpret sources. Always open the source links and review the result. The app sends the image/text to Google's Gemini API when you analyze it.

## Run locally (Laptop 1 or Laptop 3)
1. Install Python 3.10 or newer.
2. Extract this ZIP.
3. Open a terminal in the extracted `MemeTruth_Competition_Starter` folder.
4. Create and activate a virtual environment (optional but recommended):

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the app:
   ```bash
   streamlit run app.py
   ```
7. Open the local URL shown in the terminal (usually http://localhost:8501).

## API key
The app requires a Gemini API key for live AI analysis.

- Create/get a key through Google AI Studio.
- For a quick local test, open **API setup / settings** inside the app and paste the key. It is held only in the current app session.
- For deployment, add a secret in Streamlit Community Cloud:
  ```toml
  GEMINI_API_KEY = "your-key-here"
  GEMINI_MODEL = "gemini-2.5-flash"
  ```
- Never commit your real key to GitHub or put it in frontend code.

## Deploy to Streamlit Community Cloud
1. One team member creates a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the repository root.
3. Push/commit the files.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Choose **Create app**, select the repository and branch, and set the main file path to `app.py`.
6. In app settings → **Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your-key-here"
   GEMINI_MODEL = "gemini-2.5-flash"
   ```
7. Deploy. Wait for the app to build, then open the public URL on a second device or incognito window.
8. Test both text input and image upload on the deployed URL.

## Team split (4 people, 3 laptops)
### Gayatri — integration / team lead (Laptop 1)
- Own the main GitHub repository and app integration.
- Start the app locally and confirm the first successful analysis.
- Keep the final scope small and coordinate the surprise-round changes.

### Sneha — UI / experience (Laptop 2)
- Run the app and refine labels, copy, spacing, and visual consistency.
- Test mobile layout and the upload/paste flow.
- Do not create a separate frontend; edit the Streamlit UI in `app.py` only after coordinating changes.

### Janhvi — deployment / setup (Laptop 3)
- Create the GitHub repository and deploy to Streamlit Community Cloud.
- Configure secrets safely.
- Verify the public URL works outside the local network.

### Sharayu — evidence QA / demo (Computer lab PC)
- Prepare 3–5 test examples with known source pages.
- Check whether extracted claims preserve the meme's meaning.
- Verify sources actually support/contradict the verdict.
- Write a 60-second demo script and note bugs for the team.

Adjust names/roles as needed. Only one person should edit `app.py` at a time unless you split code into separate files deliberately.

## Two-hour execution plan
- 0–10 min: unzip, install dependencies, obtain API key, create GitHub repo.
- 10–25 min: get app running locally; test one pasted claim.
- 25–45 min: test image upload and inspect output/source links.
- 30–60 min (in parallel): deploy the first version early.
- 60–85 min: fix the most important issues; test the public URL.
- 85–100 min: prepare for the surprise/twist and make changes.
- 100–115 min: retest the live app, confirm secrets and links.
- 115–120 min: freeze changes, prepare submission/demo.

## If something fails
- **No API key:** UI loads, but analysis will not run until a valid key is supplied.
- **API error / quota:** Show the error to the team; do not present sample output as a live fact-check. Try again with a smaller image or use pasted text.
- **No sources returned:** Treat the result as unverified; retry and check the model/API response.
- **Deployment build fails:** Check Python version/dependencies in Streamlit logs; confirm `app.py` is at the repository root.
- **Time is running out:** Keep text-based analysis, source links, and deployment. Drop optional polish first.
