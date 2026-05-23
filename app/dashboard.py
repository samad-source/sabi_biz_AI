import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="SabiBiz AI - Agent System",
    layout="wide"
)

# -----------------------------
# PREMIUM UI STYLE
# -----------------------------
st.markdown(
    """
    <style>

    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, #0b1220, #060913);
        color: white;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* MAIN TITLE */
    .title {
        font-size: 56px;
        font-weight: 900;
        text-align: center;
        margin-top: 50px;
        letter-spacing: 1px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        opacity: 0.7;
        margin-bottom: 30px;
    }

    /* AGENT CARDS */
    .agent-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    }

    .agent-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .agent-desc {
        font-size: 14px;
        opacity: 0.75;
    }

    /* SYSTEM LOGS */
    .log {
        font-family: monospace;
        background: rgba(255,255,255,0.05);
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 14px;
        border-left: 3px solid #3b82f6;
    }

    /* STATUS */
    .status {
        text-align: center;
        font-size: 18px;
        margin-top: 25px;
        opacity: 0.85;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">SabiBiz AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multi-Agent Intelligence System for Business Discovery & Reviews</div>', unsafe_allow_html=True)

# -----------------------------
# AGENT VIEW
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="agent-box">
            <div class="agent-title">🧠 Review Intelligence Agent</div>
            <div class="agent-desc">
                Analyzes user behavior and generates human-like business reviews using sentiment reasoning.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="agent-box">
            <div class="agent-title">🎯 Recommendation Agent</div>
            <div class="agent-desc">
                Matches users to best businesses using AI ranking + contextual understanding.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# SYSTEM BOOT SEQUENCE (AUTO PLAY)
# -----------------------------
st.markdown("---")

placeholder = st.empty()

boot_sequence = [
    "Initializing SabiBiz AI Core Engine...",
    "Loading Multi-Agent Framework...",
    "Connecting Review Intelligence Agent...",
    "Connecting Recommendation Agent...",
    "Loading Business Dataset (data/businesses.csv)...",
    "Calibrating AI Ranking Models...",
    "Activating Memory Layer...",
    "System Ready for Query Processing ✔"
]

for step in boot_sequence:
    placeholder.markdown(
        f"<div class='status'>⚙️ {step}</div>",
        unsafe_allow_html=True
    )
    time.sleep(1.2)

# -----------------------------
# LIVE AGENT ACTIVITY FEED
# -----------------------------
st.markdown("### 🧾 Agent Activity Stream")

logs = [
    "Router Agent: Initialized",
    "Review Agent: Model loaded successfully",
    "Recommendation Agent: Ranking engine active",
    "Memory Layer: User profiling enabled",
    "System: Awaiting external queries"
]

for log in logs:
    st.markdown(f"<div class='log'>▶ {log}</div>", unsafe_allow_html=True)
    time.sleep(0.6)

# -----------------------------
# FINAL STATUS
# -----------------------------
st.success("🚀 SabiBiz AI System Fully Operational — Ready for Live Demo")