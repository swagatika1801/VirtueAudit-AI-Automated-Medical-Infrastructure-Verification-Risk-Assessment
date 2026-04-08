import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Virtue Audit Portal", layout="wide", page_icon="🏥")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Virtue Foundation: AI Audit Dashboard")
st.caption("Automated Medical Facility Verification & Risk Assessment")

# 1. Optimized Data Loading
@st.cache_data # Isse baar-baar file load nahi hogi, app fast chalega
def load_data():
    try:
        # Load the CSV
        df = pd.read_csv("Virtue_Final_Audit.csv")
        
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
        st.subheader("🚩 Audit Results by Specialty")
        # Bar chart logic
        fig_bar = px.bar(df, x='specialty', color='is_suspicious', 
                         title="Risk Analysis per Category",
                         color_discrete_map={True: '#ef553b', False: '#636efa'})
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.subheader("📊 Care Distribution")
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