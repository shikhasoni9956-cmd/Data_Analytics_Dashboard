import streamlit as st

st.set_page_config(
    page_title="Student Analytics Login",
    page_icon="🎓",
    layout="wide"
)

# ====== MODERN POWER BI + APPLE VISION PRO STYLING ======
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 50%, rgba(15, 52, 96, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(0, 217, 255, 0.15) 0%, transparent 50%),
                    linear-gradient(135deg, #0a0e27 0%, #16213e 50%, #0f3460 100%);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        overflow-x: hidden;
    }
    
    [data-testid="stMainBlockContainer"] {
        padding: 60px 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Sidebar Branding */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 39, 0.7) !important;
        border-right: 2px solid rgba(0, 217, 255, 0.2) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    [data-testid="stSidebar"] h1 {
        background: linear-gradient(135deg, #00d9ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.8em !important;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }
    h1 {
        color: #00d9ff;
        font-size: 3.5em;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #00d9ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 217, 255, 0.5);
        animation: glow-text 3s ease-in-out infinite;
    }
    
    @keyframes glow-text {
        0%, 100% { 
            filter: drop-shadow(0 0 10px rgba(0, 217, 255, 0.3)) 
                    drop-shadow(0 0 20px rgba(0, 255, 136, 0.2));
        }
        50% { 
            filter: drop-shadow(0 0 20px rgba(0, 217, 255, 0.6)) 
                    drop-shadow(0 0 40px rgba(0, 255, 136, 0.4));
        }
    }
    
    h2 {
        color: #00d9ff;
        font-size: 2em;
    }
    
    .stCaption {
        color: #94a3b8;
        font-size: 1.2em;
        margin-bottom: 40px;
        letter-spacing: 1px;
        font-weight: 300;
    }
    
    /* Login Container */
    div[data-testid="stVerticalBlock"] {
        background: rgba(10, 14, 39, 0.4) !important;
    }
    
    /* Input Fields - Vision Pro Style */
    input {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 2px solid rgba(0, 217, 255, 0.4) !important;
        color: #00d9ff !important;
        border-radius: 16px !important;
        padding: 16px 20px !important;
        font-size: 1.1em !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.1),
                    inset 0 0 15px rgba(0, 217, 255, 0.05) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    input::placeholder {
        color: rgba(0, 217, 255, 0.3) !important;
    }
    
    input:focus {
        background: rgba(255, 255, 255, 0.08) !important;
        border-color: #00ffff !important;
        box-shadow: 0 0 40px rgba(0, 217, 255, 0.6),
                    0 0 60px rgba(0, 255, 136, 0.3),
                    inset 0 0 20px rgba(0, 217, 255, 0.1) !important;
        outline: none !important;
        transform: translateY(-2px) !important;
    }
    
    /* Buttons - Power BI Style */
    button {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.8) 0%, rgba(0, 217, 255, 0.8) 100%) !important;
        border: 2px solid #00d9ff !important;
        color: white !important;
        border-radius: 14px !important;
        padding: 14px 32px !important;
        font-weight: 600 !important;
        font-size: 1.05em !important;
        cursor: pointer !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 0 25px rgba(0, 217, 255, 0.4),
                    0 8px 32px rgba(0, 102, 255, 0.2) !important;
        backdrop-filter: blur(15px) !important;
    }
    
    button:hover {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.9) 0%, rgba(0, 255, 136, 0.9) 100%) !important;
        box-shadow: 0 0 50px rgba(0, 217, 255, 0.8),
                    0 0 80px rgba(0, 255, 136, 0.5),
                    0 12px 48px rgba(0, 102, 255, 0.3) !important;
        transform: translateY(-4px) !important;
    }
    
    button:active {
        transform: translateY(-2px) !important;
    }
    
    /* Download Button - Premium Styling */
    div[data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.7) 0%, rgba(0, 255, 136, 0.7) 100%) !important;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.4), 0 0 50px rgba(0, 255, 136, 0.2) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-testid="stDownloadButton"] button:hover {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.9) 0%, rgba(0, 217, 255, 0.9) 100%) !important;
        box-shadow: 0 0 50px rgba(0, 217, 255, 0.7), 0 0 80px rgba(0, 255, 136, 0.5) !important;
        transform: translateY(-6px) scale(1.02) !important;
    }
    
    /* Section Headers - Premium Styling */
    h2 {
        position: relative;
        padding-left: 20px;
    }
    
    h2::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 30px;
        background: linear-gradient(180deg, #00d9ff, #00ff88);
        border-radius: 2px;
    }
    
    /* Alert Messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.08) !important;
        border: 2px solid #22c55e !important;
        border-radius: 14px !important;
        color: #86efac !important;
        padding: 16px 20px !important;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.08) !important;
        border: 2px solid #ef4444 !important;
        border-radius: 14px !important;
        color: #fca5a5 !important;
        padding: 16px 20px !important;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.08) !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 14px !important;
        color: #93c5fd !important;
        padding: 16px 20px !important;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Scrollbar - Premium Styling */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00d9ff, #0066ff);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.6);
        transition: all 0.3s ease;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #00ffff, #0088ff);
        box-shadow: 0 0 25px rgba(0, 217, 255, 0.8);
    }
    
    /* Divider */
    hr {
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
        margin: 40px 0 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.95em;
        padding: 40px 0;
        border-top: 1px solid rgba(0, 217, 255, 0.15);
        margin-top: 60px;
        letter-spacing: 0.5px;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"] {
            padding: 30px 20px;
        }
        
        h1 {
            font-size: 2.2em !important;
        }
        
        h2 {
            font-size: 1.6em !important;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Analytics Dashboard")
st.caption("Premium Analytics Platform for Student Performance Tracking")

# Hero Section Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📊 Pages", "4", "Analytics Hub")
with col2:
    st.metric("👥 Students", "8", "Total Data")
with col3:
    st.metric("📈 Subjects", "3", "Core Topics")
with col4:
    st.metric("🎯 Features", "Premium", "Dashboard")

# Login Container
st.markdown("---")
st.subheader("🔐 Secure Login")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        if st.button("🚀 Login", use_container_width=True):
            if username == "admin" and password == "1234":
                st.session_state["login"] = True
                st.success("✅ Login Successful! Welcome back!")
                st.info("📍 Open the Dashboard from the left sidebar menu")
            else:
                st.error("❌ Invalid Username or Password")
    
    with col_b:
        st.caption("📌 Demo: admin / 1234")

# Professional About Section
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(0, 102, 255, 0.08) 0%, rgba(0, 217, 255, 0.05) 100%); 
            border: 1.5px solid rgba(0, 217, 255, 0.2); border-radius: 18px; padding: 30px; 
            backdrop-filter: blur(10px); margin-top: 50px;">
    <h3 style="color: #00d9ff; margin-bottom: 15px;">📌 About This Dashboard</h3>
    <p style="color: #cbd5e1; line-height: 1.8; font-size: 0.95em;">
    Welcome to the <strong>Student Performance Analytics Dashboard</strong> - a premium, modern analytics platform 
    built with cutting-edge technology. This dashboard provides comprehensive insights into student performance across 
    multiple subjects and metrics.<br><br>
    <strong>✨ Features:</strong> Real-time analytics • Multi-page insights • Advanced visualizations • 
    Professional reports • Secure authentication
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div style="color: #94a3b8; font-size: 0.9em; margin-bottom: 10px;">
    🔐 Secure • 📊 Reliable • ⚡ Fast
    </div>
    <p style="color: #64748b; margin: 15px 0; font-size: 0.9em;">
    © 2024 Student Performance Dashboard • All Rights Reserved
    </p>
    <p style="color: #475569; font-size: 0.85em;">
    Built with <span style="color: #00d9ff;">●</span> Streamlit • Plotly • Python
    </p>
</div>
""", unsafe_allow_html=True)