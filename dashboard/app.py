import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(page_title="Ethiopia FI Forecast 2027", layout="wide")

st.title("🇪🇹 Ethiopia Financial Inclusion Forecast (2025-2027)")
st.markdown("Exploring the path toward the **70% NFIS-II Target**.")

# 2. Data Loading
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/ethiopia_fi_enriched.csv')
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    return df

df = load_data()

# 3. Sidebar - Scenario Controls
st.sidebar.header("Scenario Settings")
scenario = st.sidebar.selectbox("Select Economic Scenario", 
                                ["Base (Trend)", "Optimistic (Policy Success)", "Pessimistic (Slowdown)"])

fayda_toggle = st.sidebar.checkbox("Include Fayda Digital ID Impact", value=True)
safaricom_toggle = st.sidebar.checkbox("Include Safaricom M-Pesa Impact", value=True)

# 4. Logic: Calculate Forecast (Simplified for Dashboard)
# In a real app, you'd import these from src/models.py
base_val_2027 = 55.0 # Example trend result
impact = 0
if fayda_toggle: impact += 15.0
if safaricom_toggle: impact += 5.5
if scenario == "Pessimistic (Slowdown)": impact -= 10.0

final_2027 = base_val_2027 + impact

# 5. Main Dashboard Layout
col1, col2, col3 = st.columns(3)
col1.metric("Current Ownership (2024)", "49.0%", "+3.1%")
col2.metric("2027 Projected", f"{final_2027}%", f"{final_2027 - 49.0}%")
col3.metric("NFIS-II Target", "70.0%", "Gap: {:.1f}%".format(70.0 - final_2027))

# 6. Visualization - The Trend Line
st.subheader("Inclusion Trajectory & Scenarios")

# Historical Data
hist_df = df[df['indicator_code'] == 'ACC_OWNERSHIP'].sort_values('observation_date')

fig = go.Figure()
# Add Historical
fig.add_trace(go.Scatter(x=hist_df['observation_date'], y=hist_df['value_numeric'], 
                         name='Historical Data', line=dict(color='black', width=4)))

# Add Forecast
forecast_dates = pd.to_datetime(['2025-01-01', '2026-01-01', '2027-01-01'])
forecast_vals = [51.0, 53.0, final_2027] # Simplified step growth
fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_vals, 
                         name='Forecast Path', line=dict(dash='dash', color='blue')))

# Target Line
fig.add_hline(y=70, line_dash="dot", line_color="red", annotation_text="70% Target")

fig.update_layout(xaxis_title="Year", yaxis_title="Account Ownership (%)")
st.plotly_chart(fig, use_container_width=True)

# 7. Impact Table (From Task 3)
st.subheader("Event Impact Breakdown")
st.write("Current factors influencing the 2027 projection:")
impact_data = {
    "Event": ["Fayda ID Rollout", "Safaricom Entry", "Fuel Digitization"],
    "Impact Magnitude": ["+15.0pp", "+5.5pp", "+12.0pp"],
    "Status": ["In Progress", "Active", "Active"]
}
st.table(pd.DataFrame(impact_data))