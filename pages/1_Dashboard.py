import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Student Analytics Dashboard",
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
        padding: 40px 50px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Section Headers - Premium Styling */
    h2 {
        position: relative;
        padding-left: 20px;
        margin: 50px 0 25px 0 !important;
        animation: slide-in 0.5s ease-out;
    }
    
    @keyframes slide-in {
        from { opacity: 0; transform: translateX(-20px); }
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
    
    /* KPI Cards - Vision Pro Glassmorphism */
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
    
    /* Sidebar - Vision Pro */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 39, 0.6) !important;
        border-right: 1.5px solid rgba(0, 217, 255, 0.2) !important;
        box-shadow: inset -15px 0 40px rgba(0, 217, 255, 0.08) !important;
        backdrop-filter: blur(15px) !important;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
        color: #00d9ff;
        font-weight: 600;
    }
    
    /* Sidebar Controls */
    [data-testid="stSidebar"] button {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.7) 0%, rgba(0, 217, 255, 0.7) 100%) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.5) !important;
        border-radius: 14px !important;
        color: white !important;
        font-weight: 600 !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.3) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    [data-testid="stSidebar"] button:hover {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.9) 0%, rgba(0, 255, 136, 0.9) 100%) !important;
        box-shadow: 0 0 40px rgba(0, 217, 255, 0.7), 0 0 60px rgba(0, 255, 136, 0.4) !important;
        transform: translateY(-3px) !important;
    }
    
    [data-testid="stSidebar"] input {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.3) !important;
        color: #00d9ff !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    [data-testid="stSidebar"] input:focus {
        background: rgba(255, 255, 255, 0.1) !important;
        border-color: #00ffff !important;
        box-shadow: 0 0 30px rgba(0, 217, 255, 0.6) !important;
        outline: none !important;
    }
    
    [data-testid="stSidebar"] select {
        background: rgba(15, 52, 96, 0.5) !important;
        border: 1.5px solid rgba(0, 217, 255, 0.3) !important;
        color: #00d9ff !important;
        border-radius: 12px !important;
        padding: 12px !important;
        transition: all 0.4s ease !important;
        backdrop-filter: blur(10px) !important;
    }
    
    [data-testid="stSidebar"] select:hover {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.4) !important;
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
    
    .stInfo {
        background: rgba(59, 130, 246, 0.08) !important;
        border: 1.5px solid #3b82f6 !important;
        border-radius: 14px !important;
        color: #93c5fd !important;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.2) !important;
        backdrop-filter: blur(10px) !important;
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
        
        div[data-testid="metric-container"] {
            padding: 20px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Performance Analytics Dashboard")
st.caption("Analyze • Visualize • Explore Student Performance")

# ====== Sample Data (Load BEFORE metrics) ======
data = {
    "Student":["Aman","Riya","Rahul","Sneha","Vikas","Priya","Arjun","Neha"],
    "Gender":["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Maths":[85,92,78,88,67,95,73,90],
    "Science":[80,90,75,85,70,96,76,91],
    "English":[75,88,82,90,65,94,70,89]
}

sample_df = pd.DataFrame(data)

# ====== Sidebar File Uploader ======
st.sidebar.title("📂 Dashboard Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ CSV Uploaded Successfully")
else:
    df = sample_df

# ====== Data Transformations (BEFORE metrics) ======
df["Average"] = df[
    ["Maths","Science","English"]
].mean(axis=1)

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x>=40 else "Fail"
)

df["Performance"] = df["Average"].apply(
    lambda x:
    "Excellent" if x>=90 else
    "Good" if x>=75 else
    "Average" if x>=50 else
    "Poor"
)

# ====== Premium Summary Section (NOW df is defined) ======
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📚 Total Students", len(df), "Active Records")
    with col2:
        st.metric("📊 Avg Score", f"{df['Average'].mean():.1f}", "Overall Performance")
    with col3:
        st.metric("⭐ Top Score", f"{df['Average'].max():.1f}", "Highest Mark")
    with col4:
        st.metric("✅ Pass Rate", f"{(len(df[df['Result']=='Pass'])/len(df)*100):.1f}%", "Success Rate")

st.sidebar.info("📊 Using Sample Dataset")
st.sidebar.markdown("---")

search = st.sidebar.text_input("🔍 Search Student")

if search:
    df = df[df["Student"].str.contains(search, case=False)]

gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["Gender"].unique())
)

if gender != "All":
    df = df[df["Gender"] == gender]

# ====== Display Charts and Content ======

ranking = df.sort_values(
    by="Average",
    ascending=False
)

ranking.insert(
    0,
    "Rank",
    range(1,len(ranking)+1)
)

# ====== KPI CARDS ======
st.markdown("## 📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍🎓 Total Students",
        len(df)
    )

with col2:
    st.metric(
        "📈 Average Marks",
        round(df["Average"].mean(), 2)
    )

with col3:
    pass_percent = round(
        (len(df[df["Result"]=="Pass"]) / len(df)) * 100,
        2
    )

    st.metric(
        "✅ Pass Percentage",
        f"{pass_percent}%"
    )

col4, col5, col6 = st.columns(3)

with col4:
    topper = df.loc[
        df["Average"].idxmax(),
        "Student"
    ]

    st.metric(
        "🏆 Top Student",
        topper
    )

with col5:
    st.metric(
        "🔥 Highest Average",
        round(df["Average"].max(),2)
    )

with col6:
    st.metric(
        "📉 Lowest Average",
        round(df["Average"].min(),2)
    )

st.divider()

# ======== STUDENT TABLE ========

st.subheader("📋 Student Data")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# ======== SUBJECT WISE BAR CHART ========

st.subheader("📊 Subject Wise Average Marks")

subject_avg = df[
    ["Maths","Science","English"]
].mean().reset_index()

subject_avg.columns = [
    "Subject",
    "Average"
]

fig = px.bar(
    subject_avg,
    x="Subject",
    y="Average",
    color="Average",
    text="Average",
    title="📊 Average Marks by Subject",
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
    hoverlabel=dict(bgcolor="rgba(0, 217, 255, 0.9)", font_size=12, namelength=-1),
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

st.plotly_chart(fig, use_container_width=True)

# ======== GENDER PIE CHART ========

st.subheader("👥 Gender Distribution")

fig2 = px.pie(
    df,
    names="Gender",
    hole=0.45,
    title="👥 Gender Distribution",
    color_discrete_sequence=["#00d9ff", "#00ff88"]
)

fig2.update_layout(
    template="plotly_dark",
    height=480,
    paper_bgcolor="rgba(15, 52, 96, 0.15)",
    plot_bgcolor="rgba(10, 14, 39, 0.3)",
    title_font=dict(size=22, color="#00d9ff", family="Arial Black"),
    font=dict(size=12, color="#cbd5e1"),
)

fig2.update_traces(
    textposition="auto",
    textinfo="percent+label",
    textfont=dict(size=12, family="Arial Black"),
    marker=dict(
        line=dict(color="rgba(10, 14, 39, 0.9)", width=3),
        colors=["#00d9ff", "#00ff88"]
    ),
    hovertemplate="<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>"
)

st.plotly_chart(fig2, use_container_width=True)

# ======== TOP 5 STUDENTS ========

st.subheader("🏆 Top 5 Students")

top5 = ranking.head(5)

fig3 = px.bar(
    top5,
    x="Average",
    y="Student",
    orientation="h",
    color="Average",
    text="Average",
    color_continuous_scale=["#0066ff", "#00d9ff", "#00ff88"],
    title="🏆 Top 5 Performing Students"
)

fig3.update_layout(
    template="plotly_dark",
    height=450,
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
        title="Student",
        title_font=dict(color="#00d9ff", size=13),
        tickfont=dict(color="#cbd5e1", size=11)
    ),
    margin=dict(l=100, r=50, t=70, b=50),
    hovermode="y unified"
)

fig3.update_traces(
    textposition="outside",
    textfont=dict(color="#00ff88", size=12, family="Arial Black"),
    marker=dict(line=dict(color="rgba(0, 217, 255, 0.6)", width=2))
)

st.plotly_chart(fig3, use_container_width=True)

# ======== MARKS DISTRIBUTION ========

st.subheader("📈 Marks Distribution")

fig4 = px.histogram(
    df,
    x="Average",
    color="Performance",
    nbins=8,
    title="📊 Distribution of Student Average Marks",
    color_discrete_map={
        "Excellent": "#00ff88",
        "Good": "#00d9ff",
        "Average": "#fbbf24",
        "Poor": "#ff6b6b"
    }
)

fig4.update_layout(
    template="plotly_dark",
    height=450,
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
    hovermode="x unified",
    legend=dict(x=0.7, y=0.95)
)

fig4.update_traces(
    marker=dict(
        line=dict(color="rgba(0, 217, 255, 0.4)", width=1),
        cornerradius=4
    )
)

st.plotly_chart(fig4, use_container_width=True)

# ======== PERFORMANCE DISTRIBUTION ========

st.subheader("⭐ Performance Categories")

performance_count = (
    df["Performance"]
    .value_counts()
    .reset_index()
)

performance_count.columns = [
    "Performance",
    "Students"
]

fig5 = px.bar(
    performance_count,
    x="Performance",
    y="Students",
    color="Performance",
    text="Students",
    title="⭐ Student Performance Distribution",
    color_discrete_map={
        "Excellent": "#00ff88",
        "Good": "#00d9ff",
        "Average": "#fbbf24",
        "Poor": "#ff6b6b"
    }
)

fig5.update_layout(
    template="plotly_dark",
    height=450,
    paper_bgcolor="rgba(15, 52, 96, 0.15)",
    plot_bgcolor="rgba(10, 14, 39, 0.3)",
    title_font=dict(size=22, color="#00d9ff", family="Arial Black"),
    xaxis=dict(
        title_font=dict(color="#00d9ff", size=13),
        tickfont=dict(color="#cbd5e1", size=11),
        showgrid=False
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

fig5.update_traces(
    textposition="outside",
    textfont=dict(color="#00ff88", size=12, family="Arial Black"),
    marker=dict(
        line=dict(color="rgba(0, 217, 255, 0.6)", width=2),
        cornerradius=8
    )
)

st.plotly_chart(fig5, use_container_width=True)

# =====================================================
# TOP 3 TABLE
# =====================================================

st.subheader("🥇 Top 3 Performers")

st.table(
    top5.head(3)[
        [
            "Student",
            "Average",
            "Performance"
        ]
    ]
)

# =====================================================
# ANALYTICS INSIGHTS
# =====================================================

best_subject = df[
    [
        "Maths",
        "Science",
        "English"
    ]
].mean().idxmax()

weak_subject = df[
    [
        "Maths",
        "Science",
        "English"
    ]
].mean().idxmin()

st.markdown("## 🤖 Analytics Insights")

st.success(f"""
🏆 **Best Subject:** {best_subject}

📉 **Needs Improvement:** {weak_subject}

✅ **Pass Students:** {len(df[df['Result']=='Pass'])}

❌ **Fail Students:** {len(df[df['Result']=='Fail'])}

⭐ **Top Student:** {topper}
""")

# =====================================================
# DOWNLOAD REPORT
# =====================================================

csv = ranking.to_csv(index=False)

st.download_button(
    "📥 Download Student Report",
    csv,
    file_name="Student_Report.csv",
    mime="text/csv"
)

st.divider()

st.markdown(
"""
<center>

### 🎓 Student Performance Analytics Dashboard

Developed using **Python • Streamlit • Pandas • Plotly**

</center>
""",
unsafe_allow_html=True
)

st.balloons()
# =====================================================
# SUBJECT COMPARISON
# =====================================================

st.markdown("## 📚 Subject Comparison")

subject_df = df.melt(
    id_vars=["Student"],
    value_vars=["Maths", "Science", "English"],
    var_name="Subject",
    value_name="Marks"
)

fig6 = px.box(
    subject_df,
    x="Subject",
    y="Marks",
    color="Subject",
    points="all",
    title="Subject-wise Marks Distribution"
)

fig6.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig6, use_container_width=True)

# =====================================================
# STUDENT PERFORMANCE SCATTER
# =====================================================

st.markdown("## 🎯 Student Performance Analysis")

fig7 = px.scatter(
    df,
    x="Maths",
    y="Science",
    size="Average",
    color="Performance",
    hover_name="Student",
    title="Maths vs Science Performance"
)

fig7.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig7, use_container_width=True)

# =====================================================
# PERFORMANCE SUMMARY
# =====================================================

st.markdown("## 📋 Performance Summary")

excellent = len(df[df["Performance"] == "Excellent"])
good = len(df[df["Performance"] == "Good"])
average = len(df[df["Performance"] == "Average"])
poor = len(df[df["Performance"] == "Poor"])

summary = pd.DataFrame({
    "Category": ["Excellent", "Good", "Average", "Poor"],
    "Students": [excellent, good, average, poor]
})

st.dataframe(summary, use_container_width=True)

# =====================================================
# TOP & BOTTOM STUDENTS
# =====================================================

left, right = st.columns(2)

with left:
    st.markdown("### 🏆 Top 5 Students")
    st.dataframe(
        ranking.head(5)[["Student", "Average"]],
        use_container_width=True
    )

with right:
    st.markdown("### 📉 Bottom 5 Students")
    st.dataframe(
        ranking.tail(5)[["Student", "Average"]],
        use_container_width=True
    )

# =====================================================
# PROJECT INFO
# =====================================================

with st.expander("ℹ️ About This Dashboard"):
    st.write("""
This dashboard provides:

- Student Performance Analysis
- Subject-wise Analytics
- Interactive Charts
- Gender Analysis
- Ranking System
- CSV Upload Support
- Downloadable Reports

**Technology Used**
- Python
- Streamlit
- Pandas
- Plotly
    """)

# Professional Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 30px 0; color: #64748b; font-size: 0.9em;">
    <p style="color: #94a3b8; margin-bottom: 10px;">🎓 Student Performance Dashboard v1.0</p>
    <p style="color: #475569; margin: 10px 0;">Built with <span style="color: #00d9ff;">●</span> Streamlit • Plotly • Pandas</p>
    <p style="color: #475569; font-size: 0.85em;">© 2024 Analytics Platform • All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)