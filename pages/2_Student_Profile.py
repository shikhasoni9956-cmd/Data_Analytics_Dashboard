import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Student Profile",
    page_icon="👤",
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
    h2 {
        position: relative;
        padding-left: 20px;
        margin: 40px 0 25px 0 !important;
        animation: section-reveal 0.6s ease-out;
    }
    
    @keyframes section-reveal {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
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
    
    h2 {
        color: #00d9ff;
        font-size: 1.9em;
        font-weight: 600;
        letter-spacing: 1px;
        margin: 35px 0 25px 0;
    }
    
    h3 {
        color: #e2e8f0;
        font-size: 1.3em;
        font-weight: 500;
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
    
    /* Selectbox */
    select {
        background: rgba(15, 52, 96, 0.5) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.3) !important;
        color: #00d9ff !important;
        border-radius: 14px !important;
        padding: 12px !important;
        transition: all 0.4s ease !important;
        backdrop-filter: blur(10px) !important;
    }
    
    select:hover {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.4) !important;
    }
    
    /* Divider */
    hr {
        border: 1px solid rgba(0, 217, 255, 0.15) !important;
        margin: 35px 0 !important;
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
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00d9ff, #0066ff);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.6);
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
        
        h2 {
            font-size: 1.5em !important;
            padding-left: 15px !important;
        }
        
        h2::before {
            height: 25px;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 Student Profile Dashboard")
st.caption("View individual student performance details and analysis")

# ====== Sample Data (Load BEFORE metrics) ======
data = {
    "Student":["Aman","Riya","Rahul","Sneha","Vikas","Priya","Arjun","Neha"],
    "Gender":["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Maths":[85,92,78,88,67,95,73,90],
    "Science":[80,90,75,85,70,96,76,91],
    "English":[75,88,82,90,65,94,70,89]
}

df = pd.DataFrame(data)

# ====== Data Transformations (BEFORE metrics) ======
df["Average"] = df[
    ["Maths","Science","English"]
].mean(axis=1)

df["Rank"] = df["Average"].rank(
    ascending=False
).astype(int)

df["Result"] = df["Average"].apply(
    lambda x:"Pass" if x>=40 else "Fail"
)

df["Performance"] = df["Average"].apply(
    lambda x:
    "Excellent" if x>=90 else
    "Good" if x>=75 else
    "Average" if x>=50 else
    "Poor"
)

# Professional Intro
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📖 Total Records", len(df), "Students")
    with col2:
        st.metric("📊 Avg Performance", f"{df['Average'].mean():.1f}/100", "Dashboard")
    with col3:
        st.metric("🎯 Success Rate", f"{(len(df[df['Result']=='Pass'])/len(df)*100):.1f}%", "Pass Rate")

search = st.text_input("🔍 Search Student")

students = df["Student"]

if search:
    students = df[
        df["Student"].str.contains(search,case=False)
    ]["Student"]

student = st.selectbox(
    "👤 Select Student",
    students
)

student_data = df[
    df["Student"]==student
].iloc[0]

# ========== PROFILE SUMMARY ==========

st.markdown("## 🎓 Student Report Card")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👤 Name", student_data["Student"])
    st.metric("🚻 Gender", student_data["Gender"])

with col2:
    st.metric("📈 Average", round(student_data["Average"],2))
    st.metric("🏅 Rank", int(student_data["Rank"]))

with col3:
    st.metric("✅ Result", student_data["Result"])
    st.metric("⭐ Performance", student_data["Performance"])

st.divider()

# ========== SUBJECT MARKS ==========

marks = pd.DataFrame({
    "Subject":["Maths","Science","English"],
    "Marks":[
        student_data["Maths"],
        student_data["Science"],
        student_data["English"]
    ]
})

st.subheader("📚 Subject Wise Marks")

st.dataframe(
    marks,
    use_container_width=True
)

st.divider()

# ========== BAR CHART ==========

fig = px.bar(
    marks,
    x="Subject",
    y="Marks",
    color="Marks",
    text="Marks",
    title=f"📊 {student} Subject Performance",
    color_continuous_scale=["#0066ff", "#00d9ff", "#00ff88"]
)

fig.update_layout(
    template="plotly_dark",
    height=480,
    paper_bgcolor="rgba(15, 52, 96, 0.15)",
    plot_bgcolor="rgba(10, 14, 39, 0.3)",
    title_font=dict(size=22, color="#00d9ff", family="Arial Black"),
    xaxis=dict(
        title_font=dict(color="#00d9ff", size=13),
        tickfont=dict(color="#cbd5e1", size=11),
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0, 217, 255, 0.05)"
    ),
    yaxis=dict(
        title_font=dict(color="#00d9ff", size=13),
        tickfont=dict(color="#cbd5e1", size=11),
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(0, 217, 255, 0.05)"
    ),
    margin=dict(l=50, r=50, t=70, b=50),
    hovermode="x unified"
)

fig.update_traces(
    marker=dict(
        line=dict(color="rgba(0, 217, 255, 0.6)", width=2),
        cornerradius=8
    ),
    textposition="outside",
    textfont=dict(color="#00ff88", size=12, family="Arial Black")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ========== RADAR CHART ==========

st.subheader("🕸️ Subject Performance Radar")

radar = px.line_polar(
    marks,
    r="Marks",
    theta="Subject",
    line_close=True,
    title=f"🎯 {student} Performance Radar"
)

radar.update_traces(
    fill="toself",
    line=dict(color="#00d9ff", width=3),
    fillcolor="rgba(0, 217, 255, 0.25)"
)

radar.update_layout(
    template="plotly_dark",
    height=500,
    paper_bgcolor="rgba(15, 52, 96, 0.15)",
    plot_bgcolor="rgba(10, 14, 39, 0.3)",
    title_font=dict(size=22, color="#00d9ff", family="Arial Black"),
    polar=dict(
        radialaxis=dict(
            tickfont=dict(color="#cbd5e1", size=11),
            gridcolor="rgba(0, 217, 255, 0.1)",
            showgrid=True
        ),
        angularaxis=dict(
            tickfont=dict(color="#cbd5e1", size=11),
            gridcolor="rgba(0, 217, 255, 0.1)"
        )
    ),
    margin=dict(l=50, r=50, t=70, b=50)
)

st.plotly_chart(
    radar,
    use_container_width=True
)
# PROGRESS
# ==========================================================

st.subheader("📈 Overall Progress")

progress = student_data["Average"] / 100

st.progress(progress)

st.write(f"Overall Score : **{round(student_data['Average'],2)} / 100**")

# ==========================================================
# GRADE
# ==========================================================

avg = student_data["Average"]

if avg >= 90:
    grade = "A+ 🏆"
elif avg >= 80:
    grade = "A 🥇"
elif avg >= 70:
    grade = "B 🥈"
elif avg >= 60:
    grade = "C 🥉"
else:
    grade = "D"

st.metric(
    "🎖 Grade",
    grade
)

# ==========================================================
# PERFORMANCE INSIGHTS
# ==========================================================

best_subject = marks.loc[
    marks["Marks"].idxmax(),
    "Subject"
]

weak_subject = marks.loc[
    marks["Marks"].idxmin(),
    "Subject"
]

st.markdown("## 🤖 AI Performance Insights")

st.success(f"""
### {student}

🏆 Best Subject : **{best_subject}**

📉 Needs Improvement : **{weak_subject}**

⭐ Overall Performance : **{student_data['Performance']}**

🏅 Current Rank : **{int(student_data['Rank'])}**

📚 Average Marks : **{round(student_data['Average'],2)}**
""")

# ==========================================================
# SUGGESTIONS
# ==========================================================

st.subheader("💡 Improvement Suggestions")

if avg >= 90:
    st.success("Excellent performance! Keep maintaining consistency. 🚀")

elif avg >= 75:
    st.info("Very good performance. Focus more on the weakest subject to reach the top rank.")

elif avg >= 60:
    st.warning("You are doing well, but regular practice will improve your score.")

else:
    st.error("Needs improvement. Spend more time on basic concepts and practice daily.")

st.divider()

st.markdown("""
<div style="text-align: center; padding: 30px 0; color: #64748b; font-size: 0.9em;">
    <p style="color: #94a3b8; margin-bottom: 10px;">👨‍🎓 Student Profile Analytics</p>
    <p style="color: #475569; margin: 10px 0;">Built with <span style="color: #00d9ff;">●</span> Streamlit • Plotly • Pandas</p>
    <p style="color: #475569; font-size: 0.85em;">© 2024 Analytics Platform • All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)