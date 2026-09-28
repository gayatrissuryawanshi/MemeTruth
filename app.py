import base64
import json
import re
from typing import Any

import requests
import streamlit as st

APP_NAME = "MemeTruth"
DEFAULT_MODEL = "gemini-3.8-flash"

st.set_page_config(
    page_title="MemeTruth — Laugh at the meme. Know the truth.",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');
    :root { --ink:#171717; --yellow:#fff176; --cream:#fffdf0; --purple:#a78bfa; --teal:#21c7bd; --red:#ff574f; }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color:var(--ink); }
    .stApp { background: #fff8b8; }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1180px; padding-top: 1rem; padding-bottom: 2rem; }
    .brand { font-family:'Baloo 2',sans-serif; font-weight:800; font-size:1.35rem; letter-spacing:-.5px; }
    .hero { border:3px solid #171717; border-radius:20px; padding:28px 30px; background:#fff176; box-shadow:7px 7px 0 #171717; margin:8px 0 24px 0; }
    .hero h1 { font-family:'Baloo 2',sans-serif; font-size:clamp(2.6rem,6vw,5rem); line-height:.95; margin:0; letter-spacing:-2px; color:#171717; }
    .hero p { font-size:1.08rem; margin:14px 0 0 0; max-width:650px; }
    .ticker { overflow:hidden; white-space:nowrap; border-top:2px solid #171717; border-bottom:2px solid #171717; background:#fff; padding:7px 0; margin:18px 0 24px 0; font-family:'Baloo 2',sans-serif; font-weight:800; }
    .panel { border:2px solid #171717; border-radius:16px; background:#fffdf0; padding:20px; box-shadow:5px 5px 0 #171717; }
    .section-title { font-family:'Baloo 2',sans-serif; font-weight:800; font-size:1.65rem; margin-bottom:6px; }
    .small-muted { color:#555; font-size:.92rem; }
    .verdict { display:inline-block; border:2px solid #171717; border-radius:999px; padding:7px 14px; font-weight:800; background:#fff176; }
    .source-card { border:1.5px solid #171717; border-radius:12px; background:white; padding:12px 14px; margin:8px 0; }
    .footer { text-align:center; font-size:.85rem; color:#333; padding:22px 0 8px 0; }
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button { border:2px solid #171717; border-radius:10px; font-weight:800; box-shadow:3px 3px 0 #171717; min-height:46px; }
    div.stButton > button[kind="primary"], div[data-testid="stFormSubmitButton"] > button[kind="primary"] { background:#ff574f; color:#171717; }
    div[data-testid="stFileUploader"] section { border:2px dashed #171717; border-radius:12px; background:#fff; }
    div[data-testid="stTextArea"] textarea { border:1.5px solid #171717; border-radius:10px; background:#fff; color:#171717 !important; }

    /* Strong readable contrast for Streamlit's native widgets and text */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {
        color: #171717 !important;
    }
    .stApp p,
    .stApp label,
    .stApp span,
    .stApp li,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp [data-testid="stMarkdownContainer"],
    .stApp [data-testid="stCaptionContainer"] {
        color: #171717;
    }
    .stApp a { color: #5b21b6 !important; }
    .stApp button,
    .stApp input,
    .stApp textarea {
        color: #171717 !important;
    }
    [data-testid="stFileUploader"] section,
    [data-testid="stFileUploader"] section * {
        color: #171717 !important;
    }
    [data-testid="stTabs"] button,
    [data-testid="stTabs"] button p {
        color: #171717 !important;
    }
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary * {
        color: #171717 !important;
    }
    /* ---------- Accessible widget contrast ---------- */
    /* Streamlit/BaseWeb controls can inherit dark-theme colors. Force light
       surfaces and dark text so inputs remain readable in either theme. */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-baseweb="input"] input,
    [data-baseweb="textarea"] textarea {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #171717 !important;
        -webkit-text-fill-color: #171717 !important;
        caret-color: #171717 !important;
        border-color: #171717 !important;
        opacity: 1 !important;
    }

    [data-testid="stTextInput"] [data-baseweb="input"],
    [data-testid="stTextArea"] [data-baseweb="textarea"],
    [data-baseweb="input"] > div,
    [data-baseweb="textarea"] > div {
        background: #ffffff !important;
        background-color: #ffffff !important;
        border-color: #171717 !important;
    }

    [data-testid="stTextInput"] input::placeholder,
    [data-testid="stTextArea"] textarea::placeholder,
    [data-baseweb="input"] input::placeholder,
    [data-baseweb="textarea"] textarea::placeholder {
        color: #777777 !important;
        -webkit-text-fill-color: #777777 !important;
        opacity: 1 !important;
    }

    [data-testid="stExpander"] {
        background: #fffdf0 !important;
        background-color: #fffdf0 !important;
        border: 1.5px solid #171717 !important;
        border-radius: 12px !important;
    }

    [data-testid="stExpander"] details,
    [data-testid="stExpander"] details > div,
    [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        background: #fffdf0 !important;
        background-color: #fffdf0 !important;
    }

    [data-testid="stExpander"] summary {
        background: #fff176 !important;
        background-color: #fff176 !important;
        color: #171717 !important;
    }

    [data-testid="stExpander"] summary *,
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] label,
    [data-testid="stExpander"] [data-testid="stMarkdownContainer"] {
        color: #171717 !important;
    }

    [data-testid="stFileUploader"] section,
    [data-testid="stFileUploader"] section * {
        background-color: #ffffff;
        color: #171717 !important;
    }

    [data-testid="stTabs"] button,
    [data-testid="stTabs"] button p {
        color: #171717 !important;
    }

    /* Ensure the primary action remains high-contrast */
    div.stButton > button[kind="primary"],
    div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
        background: #ff574f !important;
        background-color: #ff574f !important;
        color: #171717 !important;
        -webkit-text-fill-color: #171717 !important;
    }

    @media (max-width:700px) { .hero { padding:22px 18px; } .hero h1 { font-size:3rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helpers ----------
def get_secret(name: str, default: str = "") -> str:
    try:
        value = st.secrets.get(name, default)
        if value:
            return str(value)
    except Exception:
        pass
    import os
    return os.getenv(name, default)

def build_prompt(user_text: str) -> str:
    return f"""
You are MemeTruth, a careful fact-checking assistant. Analyze the factual claim behind the supplied meme/text.
Use Google Search grounding to look for reliable, relevant evidence. Prefer primary sources, reputable research institutions,
government/educational sources, and established fact-checking organizations. Do not treat a joke, caption, or viral popularity
as evidence. Do not invent sources or claim certainty beyond the evidence.

USER-PROVIDED MEME TEXT / CONTEXT:
{user_text.strip() or "[No text provided; analyze text visible in the attached image.]"}

Return the answer in this exact readable structure:
CLAIM: [one concise factual claim; if none can be identified, say so]
VERDICT: [SUPPORTED / FALSE / MISLEADING / INSUFFICIENT EVIDENCE / NO FACTUAL CLAIM]
EXPLANATION: [2-4 short sentences, plain language; preserve nuance and context]
WHAT TO REMEMBER: [one short takeaway]
LIMITATIONS: [briefly state uncertainty, missing context, or that the meme may be satire, if relevant]

Important:
- A claim can be partly true but misleading; explain why.
- If evidence is weak, conflicting, or absent, use INSUFFICIENT EVIDENCE.
- Distinguish the meme's humorous framing from factual assertions.
- Never infer a claim that is not reasonably present.
"""

def analyze_with_gemini(api_key: str, model: str, user_text: str, uploaded_file) -> tuple[str, list[dict[str, str]]]:
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    parts: list[dict[str, Any]] = [{"text": build_prompt(user_text)}]
    if uploaded_file is not None:
        raw = uploaded_file.getvalue()
        mime = uploaded_file.type or "image/jpeg"
        parts.append({
            "inline_data": {
                "mime_type": mime,
                "data": base64.b64encode(raw).decode("utf-8"),
            }
        })
    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "tools": [{"google_search": {}}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 1200},
    }
    response = requests.post(
        endpoint,
        params={"key": api_key},
        json=payload,
        timeout=75,
    )
    if not response.ok:
        try:
            detail = response.json().get("error", {}).get("message", response.text)
        except Exception:
            detail = response.text
        raise RuntimeError(f"Gemini API returned {response.status_code}: {detail[:700]}")
    data = response.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError("The AI returned no answer. Try a clearer image or paste the meme text.")
    candidate = candidates[0]
    answer = "\n".join(
        p.get("text", "") for p in candidate.get("content", {}).get("parts", [])
        if p.get("text")
    ).strip()
    grounding = candidate.get("groundingMetadata", {})
    chunks = grounding.get("groundingChunks", []) or []
    sources: list[dict[str, str]] = []
    seen = set()
    for chunk in chunks:
        web = chunk.get("web", {})
        uri = web.get("uri", "")
        title = web.get("title", "") or uri
        if uri and uri not in seen:
            seen.add(uri)
            sources.append({"title": title, "url": uri})
    return answer, sources

def parse_verdict(answer: str) -> str:
    match = re.search(r"VERDICT\s*:\s*(SUPPORTED|FALSE|MISLEADING|INSUFFICIENT EVIDENCE|NO FACTUAL CLAIM)", answer, re.I)
    return match.group(1).upper() if match else "REVIEW THE EXPLANATION"

def verdict_color(verdict: str) -> str:
    if verdict == "SUPPORTED":
        return "#b9f6ca"
    if verdict == "FALSE":
        return "#ffaaa5"
    if verdict == "MISLEADING":
        return "#ffd180"
    if verdict == "INSUFFICIENT EVIDENCE":
        return "#d7ccff"
    return "#fff176"

# ---------- Header ----------
top1, top2 = st.columns([3, 2])
with top1:
    st.markdown('<div class="brand">🕵️ MEMETRUTH <span style="font-size:.8rem;font-weight:600;">— FACTS, NOT JUST MEMES</span></div>', unsafe_allow_html=True)
with top2:
    st.markdown("<div style='text-align:right;font-weight:700;padding-top:8px;'>HOME　 HOW IT WORKS　 ABOUT</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
      <h1>MEME IT.<br>CHECK IT.</h1>
      <p>We check the facts behind viral memes, so you can laugh without falling for misinformation.</p>
    </div>
    <div class="ticker">✦ MEME TRUTH　 ✦ CLAIM → EVIDENCE → VERDICT　 ✦ MEME TRUTH　 ✦ CLAIM → EVIDENCE → VERDICT　 ✦</div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="section-title">🧩 Check a meme</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-muted">Upload an image, paste its text, or do both. For best results, use a clear image and include any context.</div>', unsafe_allow_html=True)
    tab_image, tab_text = st.tabs(["📷 Upload image", "✍️ Paste text"])
    with tab_image:
        uploaded = st.file_uploader("Choose a meme image", type=["png", "jpg", "jpeg", "webp"], help="Image is sent to the AI service for analysis; do not upload private images.")
        if uploaded:
            st.image(uploaded, caption="Your meme", use_container_width=True)
        meme_text_image = st.text_area("Optional: add context or paste the meme text", key="image_context", height=95, placeholder="What does the meme say? Add context if needed...")
    with tab_text:
        meme_text_only = st.text_area("Paste the meme caption or factual claim", key="text_context", height=160, placeholder="Example: Humans only use 10% of their brain...")
        st.caption("Tip: Paste the exact wording. The tool will separate the factual claim from the joke.")

    api_key = get_secret("GEMINI_API_KEY")
    model = get_secret("GEMINI_MODEL", DEFAULT_MODEL)
    with st.expander("⚙️ API setup / settings", expanded=not bool(api_key)):
        st.write("Use a Gemini API key. The key is used only for this session if entered below.")
        session_key = st.text_input("Gemini API key", type="password", value="", help="Get a key from Google AI Studio. Never share it or commit it to GitHub.")
        model = st.text_input("Model", value=model)
        if session_key.strip():
            api_key = session_key.strip()
        st.caption("For deployment, add GEMINI_API_KEY under Streamlit Cloud → App settings → Secrets.")

    combined_text = (meme_text_image if uploaded else meme_text_only).strip()
    submitted = st.button("🔎 CHECK THE FACTS", type="primary", use_container_width=True)

if submitted:
    if not uploaded and not combined_text:
        st.warning("Upload a meme image or paste the meme text first.")
    elif not api_key:
        st.error("Add your Gemini API key in the settings above, or configure GEMINI_API_KEY in Streamlit secrets.")
    else:
        with st.spinner("Reading the meme, searching for evidence, and checking the claim…"):
            try:
                answer, sources = analyze_with_gemini(api_key, model.strip() or DEFAULT_MODEL, combined_text, uploaded)
                verdict = parse_verdict(answer)
                st.session_state["last_answer"] = answer
                st.session_state["last_sources"] = sources
                st.session_state["last_verdict"] = verdict
                st.session_state["last_input"] = combined_text
            except requests.exceptions.Timeout:
                st.error("The request timed out. Try again with a smaller image or paste the text.")
            except requests.exceptions.RequestException as exc:
                st.error(f"Network error: {exc}")
            except Exception as exc:
                st.error(str(exc))

if "last_answer" in st.session_state:
    st.markdown('<div class="ticker">✦ RESULTS　 ✦ READ THE EVIDENCE　 ✦ RESULTS　 ✦ READ THE EVIDENCE　 ✦</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧾 Fact-check result</div>', unsafe_allow_html=True)
    verdict = st.session_state.get("last_verdict", "REVIEW THE EXPLANATION")
    color = verdict_color(verdict)
    st.markdown(
        f'<div style="display:inline-block;background:{color};border:2px solid #171717;border-radius:999px;padding:8px 16px;font-weight:900;margin:6px 0 14px 0;">VERDICT: {verdict}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(st.session_state["last_answer"])
    st.markdown('</div>', unsafe_allow_html=True)

    sources = st.session_state.get("last_sources", [])
    st.markdown("### 🔗 Sources found")
    if sources:
        for i, source in enumerate(sources, start=1):
            title = source["title"].replace("<", "&lt;").replace(">", "&gt;")
            url = source["url"]
            st.markdown(
                f'<div class="source-card"><b>{i}. {title}</b><br><a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></div>',
                unsafe_allow_html=True,
            )
    else:
        st.info("The search tool did not return source links for this response. Treat the answer as unverified and try again.")
    result_text = st.session_state["last_answer"] + "\n\nSources:\n" + "\n".join(s["title"] + " — " + s["url"] for s in sources)
    st.download_button("⬇️ Download fact-check (.txt)", data=result_text, file_name="memetruth_fact_check.txt", mime="text/plain")
    st.caption("AI-generated fact-checks can be wrong. Open the sources and verify important claims independently.")

with st.expander("ℹ️ How MemeTruth works"):
    st.markdown("""
    1. **Read:** The model reads the supplied text and/or image.
    2. **Extract:** It identifies the factual claim behind the joke.
    3. **Search:** Google Search grounding retrieves relevant web evidence.
    4. **Explain:** The model returns a verdict with caveats and source links.

    **Important:** A verdict is a starting point for checking, not an official determination of truth. Satire, missing context, and changing information can affect results.
    """)

st.markdown(
    '<div class="footer">MemeTruth · Laugh at the meme. Know the truth. · Built for the Crack the Clock competition</div>',
    unsafe_allow_html=True,
)
