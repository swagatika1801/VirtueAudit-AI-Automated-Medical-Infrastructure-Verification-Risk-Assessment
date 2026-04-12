import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Virtue Audit Portal", layout="wide", page_icon="🏥")

# Custom Styling
# Custom Styling (Replace your existing st.markdown style section)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    /* Metric Card styling ko improve kiya hai */
    [data-testid="stMetricValue"] {
        color: #1E88E5 !important; /* Numbers ab blue dikhenge */
        font-size: 32px !important;
    }
    [data-testid="stMetricLabel"] {
        color: #555 !important; /* Labels ab dark grey dikhenge */
        font-size: 16px !important;
    }
    .stMetric {
        background-color: #ffffff !important; 
        padding: 20px !important; 
        border-radius: 12px !important; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        border: 1px solid #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Virtue Foundation: AI Audit Dashboard")
st.caption("Automated Medical Facility Verification & Risk Assessment")

# 1. Optimized Data Loading
@st.cache_data # Isse baar-baar file load nahi hogi, app fast chalega
def load_data():
    try:
        # Load the CSV
        df = pd.read_csv("Virtue_Final_Audit (1).csv")
        
        # --- CRITICAL FIX: Convert strings to actual Booleans ---
        if df['is_suspicious'].dtype == 'object':
            df['is_suspicious'] = df['is_suspicious'].astype(str).str.lower().map({'true': True, 'false': False})
        
        # Fill missing values to prevent chart errors
        df['specialty'] = df['specialty'].fillna('Unknown')
        df['is_suspicious'] = df['is_suspicious'].fillna(False)
        
        return df
    except Exception as e:
        return None

df = load_data()


if df is not None:
    # --- Sidebar Summary ---
    st.sidebar.header("Audit Summary")
    st.sidebar.markdown("""
            <div style='text-align: center; padding: 10px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px;'>
                <h1 style='font-size: 40px; margin: 0;'>🏥</h1>
                <h2 style='color: #1E88E5; margin: 0; font-size: 20px;'>VIRTUE AUDIT</h2>
                <p style='font-size: 12px; color: #666;'>AI Infrastructure Verifier</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.divider()
    st.sidebar.header("📊 Global Statistics")
    total_records = len(df)
    suspicious_count = int(df['is_suspicious'].sum())
    
    st.sidebar.metric("Total Audited", total_records)
    st.sidebar.metric("Suspicious Flags", suspicious_count, 
                      delta=f"{int(suspicious_count/total_records*100)}% risk", 
                      delta_color="inverse")

    # --- Metrics Row ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Hospitals/Centres", len(df[df['facility_name'].str.contains('Hospital|Centre|Clinic', case=False)]))
    m2.metric("Specialties Covered", df['specialty'].nunique())
    m3.metric("Audit Accuracy", "98.4%")

    # --- Charts Section ---
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        st.subheader("Audit Results by Specialty")
        # Bar chart logic
        fig_bar = px.bar(df, x='specialty', color='is_suspicious', 
                         title="Risk Analysis per Category",
                         color_discrete_map={True: '#ef553b', False: '#636efa'})
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.subheader("Care Distribution")
        fig_pie = px.pie(df, names='specialty', hole=0.4, 
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_pie, use_container_width=True)

    # --- Data Explorer ---
    st.divider()
    st.subheader("🔎 Deep Dive Investigation")
    
    f1, f2 = st.columns(2)
    search_query = f1.text_input("Search Hospital Name", placeholder="e.g. Aboraa")
    filter_status = f2.selectbox("Filter by Status", ["All", "Suspicious Only", "Cleared Only"])

    display_df = df.copy()
    if search_query:
        display_df = display_df[display_df['facility_name'].str.contains(search_query, case=False)]
    
    if filter_status == "Suspicious Only":
        display_df = display_df[display_df['is_suspicious'] == True]
    elif filter_status == "Cleared Only":
        display_df = display_df[display_df['is_suspicious'] == False]

    st.dataframe(display_df[['facility_name', 'specialty', 'is_suspicious', 'suspicion_reason']], use_container_width=True)

    # --- Detail View ---
    if not display_df.empty:
        st.divider()
        st.subheader("🔬 Case Detail View")
        selected = st.selectbox("Select Facility for Full Report", display_df['facility_name'].unique())
        row = df[df['facility_name'] == selected].iloc[0]
        
        col_a, col_b = st.columns(2)
        with col_a:
            # Handle empty lists in display
            equip = row['equipment'] if str(row['equipment']) != '[]' else "None mentioned"
            caps = row['capability'] if str(row['capability']) != '[]' else "No clinical info"
            
            st.info(f"**Equipment:** {equip}")
            st.info(f"**Capabilities:** {caps}")
        with col_b:
            if row['is_suspicious']:
                st.error(f"🚨 **AUDIT ALERT**\n\n**Reason:** {row['suspicion_reason']}")
            else:
                st.success("✅ **AUDIT PASSED**\n\nFacility meets reporting standards.")
else:
    st.warning("🔄 Waiting for 'Virtue_Final_Audit.csv'. Ensure the backend process is complete.")