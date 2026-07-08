import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Reports",
    page_icon="📄",
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
        padding: 40px 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Section Headers - Premium Styling */
    h2, h3 {
        position: relative;
        padding-left: 20px;
        margin: 40px 0 25px 0 !important;
        animation: fade-slide 0.6s ease-out;
    }
    
    @keyframes fade-slide {
        from { opacity: 0; transform: translateX(-25px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    h2::before, h3::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 30px;
        background: linear-gradient(180deg, #00d9ff, #00ff88);
        border-radius: 2px;
        box-shadow: 0 0 10px rgba(0, 217, 255, 0.5);
    }
    
    /* Typography */
    h1 {
        background: linear-gradient(135deg, #00d9ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.2em;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 10px;
        animation: glow-gradient 3s ease-in-out infinite;
    }
    
    @keyframes glow-gradient {
        0%, 100% { filter: drop-shadow(0 0 15px rgba(0, 217, 255, 0.4)); }
        50% { filter: drop-shadow(0 0 30px rgba(0, 217, 255, 0.8)) drop-shadow(0 0 20px rgba(0, 255, 136, 0.4)); }
    }
    
    h2, h3 {
        color: #00d9ff;
        font-size: 1.8em;
        font-weight: 600;
        letter-spacing: 1px;
        margin: 35px 0 25px 0;
    }
    
    .stCaption {
        color: #94a3b8;
        font-size: 1.1em;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
        font-weight: 300;
    }
    
    /* KPI Metric Cards - Vision Pro Glassmorphism */
    div[data-testid="metric-container"] {
        background: rgba(15, 52, 96, 0.25) !important;
        backdrop-filter: blur(20px) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.3) !important;
        border-radius: 24px !important;
        padding: 28px !important;
        box-shadow: 0 8px 32px rgba(0, 217, 255, 0.1),
                    inset 0 1px 1px rgba(255, 255, 255, 0.1),
                    0 0 40px rgba(0, 217, 255, 0.15) !important;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    div[data-testid="metric-container"]::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0, 217, 255, 0.1) 0%, transparent 70%);
        animation: shimmer 8s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes shimmer {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(10px, 10px); }
    }
    
    div[data-testid="metric-container"]:hover {
        background: rgba(15, 52, 96, 0.35) !important;
        border-color: #00ffff !important;
        box-shadow: 0 0 60px rgba(0, 217, 255, 0.6),
                    0 0 100px rgba(0, 255, 136, 0.3),
                    inset 0 1px 1px rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-8px) !important;
    }
    
    div[data-testid="metric-container"] label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        font-size: 0.95em !important;
        letter-spacing: 0.8px !important;
        text-transform: uppercase;
    }
    
    div[data-testid="metric-container"] span {
        color: #00ff88 !important;
        font-size: 2.5em !important;
        font-weight: 700 !important;
        text-shadow: 0 0 20px rgba(0, 255, 136, 0.5) !important;
    }
    
    /* Input Fields */
    input {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.3) !important;
        color: #00d9ff !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    input:focus {
        background: rgba(255, 255, 255, 0.1) !important;
        border-color: #00ffff !important;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.6) !important;
        outline: none !important;
    }
    
    /* Buttons */
    button {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.7) 0%, rgba(0, 217, 255, 0.7) 100%) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.5) !important;
        border-radius: 14px !important;
        color: white !important;
        font-weight: 600 !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.3) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    button:hover {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.9) 0%, rgba(0, 255, 136, 0.9) 100%) !important;
        box-shadow: 0 0 40px rgba(0, 217, 255, 0.7), 0 0 60px rgba(0, 255, 136, 0.4) !important;
        transform: translateY(-3px) !important;
    }
    
    /* Data Table */
    div[data-testid="dataframe"] {
        background: rgba(15, 52, 96, 0.2) !important;
        border-radius: 18px !important;
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
        padding: 18px !important;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .dataframe {
        color: #e2e8f0 !important;
    }
    
    .dataframe thead {
        background: rgba(0, 217, 255, 0.08) !important;
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
    }
    
    .dataframe th {
        color: #00d9ff !important;
        font-weight: 600 !important;
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.3) !important;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(0, 217, 255, 0.08) !important;
    }
    
    /* Alert Messages */
    .stSuccess {
        background: rgba(34, 197, 94, 0.08) !important;
        border: 1.5px solid #22c55e !important;
        border-radius: 14px !important;
        color: #86efac !important;
        box-shadow: 0 0 25px rgba(34, 197, 94, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Scrollbar */
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
    
    /* Responsive Design */
    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"] {
            padding: 30px 20px;
        }
        
        h1 {
            font-size: 2.2em !important;
        }
        
        h2, h3 {
            font-size: 1.5em !important;
            padding-left: 15px !important;
        }
        
        h2::before, h3::before {
            height: 25px;
        }
        
        div[data-testid="metric-container"] {
            padding: 20px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("📄 Student Reports")
st.caption("Comprehensive student performance reports and analysis")

# ====== Sample Data (Load BEFORE metrics) ======
data = {
    "Student": ["Aman","Riya","Rahul","Sneha","Vikas","Priya","Arjun","Neha"],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Maths": [85,92,78,88,67,95,73,90],
    "Science": [80,90,75,85,70,96,76,91],
    "English": [75,88,82,90,65,94,70,89]
}

df = pd.DataFrame(data)

# ====== Data Transformations (BEFORE metrics) ======
df["Average"] = df[
    ["Maths","Science","English"]
].mean(axis=1)

df["Rank"] = (
    df["Average"]
    .rank(
        ascending=False
    )
    .astype(int)
)

df["Result"] = df["Average"].apply(
    lambda x:
    "Pass" if x >= 40 else "Fail"
)

# Premium Summary Stats
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Students", len(df), "Records")
    with col2:
        st.metric("📈 Avg Score", f"{df['Average'].mean():.1f}", "Overall")
    with col3:
        st.metric("✅ Pass Rate", f"{(len(df[df['Result']=='Pass'])/len(df)*100):.1f}%", "Success")
    with col4:
        st.metric("🎯 Top Score", f"{df['Average'].max():.1f}", "Maximum")



# Summary Cards

st.subheader("📊 Report Summary")


col1,col2,col3 = st.columns(3)


with col1:
    st.metric(
        "👨‍🎓 Total Students",
        len(df)
    )


with col2:
    st.metric(
        "📈 Average Score",
        round(df["Average"].mean(),2)
    )


with col3:
    pass_rate = (
        len(df[df["Result"]=="Pass"])
        /
        len(df)
    )*100

    st.metric(
        "✅ Pass Rate",
        f"{round(pass_rate,2)}%"
    )



# Search Student

st.subheader("🔍 Search & Filter Students")


search = st.text_input(
    "📝 Enter Student Name"
)


if search:

    result = df[
        df["Student"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )



# Download Report

st.subheader("⬇️ Export Report")


csv = df.to_csv(
    index=False
)


st.download_button(
    "📥 Download CSV Report",
    csv,
    "student_full_report.csv",
    "text/csv"
)



st.success(
    "✅ Report Generated Successfully!"
)

# Professional About Section
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(0, 102, 255, 0.08) 0%, rgba(0, 217, 255, 0.05) 100%); 
            border: 1.5px solid rgba(0, 217, 255, 0.2); border-radius: 18px; padding: 30px; 
            backdrop-filter: blur(10px); margin: 40px 0 20px 0;">
    <h3 style="color: #00d9ff; margin-bottom: 15px;">📊 Report Features</h3>
    <p style="color: #cbd5e1; line-height: 1.8; font-size: 0.95em;">
    <strong>✨ Advanced Capabilities:</strong><br>
    🔍 Student Search & Filtering • 📥 CSV Export • 📊 Performance Metrics • 
    ✅ Pass Rate Analysis • 📈 Complete Student Records
    </p>
</div>
""", unsafe_allow_html=True)

# Professional Footer
st.markdown("""
<div style="text-align: center; padding: 30px 0; color: #64748b; font-size: 0.9em; border-top: 1px solid rgba(0, 217, 255, 0.15); margin-top: 40px;">
    <p style="color: #94a3b8; margin-bottom: 10px;">📄 Student Reports & Analytics</p>
    <p style="color: #475569; margin: 10px 0;">Built with <span style="color: #00d9ff;">●</span> Streamlit • Plotly • Pandas</p>
    <p style="color: #475569; font-size: 0.85em;">© 2024 Analytics Platform • All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)