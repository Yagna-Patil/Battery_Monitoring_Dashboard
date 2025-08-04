import streamlit as st

# === PAGE SETUP ===
st.set_page_config(page_title="Battery Cell Monitoring", layout="wide")

st.markdown(
    """
    <style>
        .stNumberInput > div {
            max-width: 150px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# === TITLE ===
st.title("🔋 Battery Cell Monitoring Dashboard")

# === SIDEBAR CONFIGURATION ===
st.sidebar.title("⚙️ Configuration")

num_cells = st.sidebar.slider("Select number of cells", min_value=1, max_value=16, value=4)

voltages = []
currents = []
temperatures = []
capacities = []
modes = []

mode_options = ["Charging", "Discharging", "Idle"]

for i in range(num_cells):
    with st.sidebar.expander(f"🔋 Cell {i+1} Input", expanded=False):
        voltages.append(st.number_input(f"Voltage (V) - Cell {i+1}", value=3.7, step=0.01, key=f"voltage_{i}"))
        currents.append(st.number_input(f"Current (A) - Cell {i+1}", value=0.0, step=0.01, key=f"current_{i}"))
        temperatures.append(st.number_input(f"Temperature (°C) - Cell {i+1}", value=25.0, step=0.1, key=f"temp_{i}"))
        capacities.append(st.number_input(f"Capacity (%) - Cell {i+1}", min_value=0, max_value=100, value=100, key=f"cap_{i}"))
        modes.append(st.selectbox(f"Mode - Cell {i+1}", options=mode_options, index=2, key=f"mode_{i}"))

# === CELL STATUS CARDS ===
st.markdown("### 🔋 Battery Cell Overview")
cell_rows = [st.columns(4) for _ in range((num_cells + 3) // 4)]

mode_colors = {'Charging': '#28a745', 'Discharging': '#dc3545', 'Idle': '#6c757d'}

for i in range(num_cells):
    cap = capacities[i]
    cap_color = "#28a745" if cap > 60 else "#ffc107" if cap > 30 else "#dc3545"
    
    battery_bar = f"""
        <div style='height: 24px; width: 100%; background-color: #ddd; border-radius: 12px; overflow: hidden; margin-top: 8px;'>
            <div style='width: {cap}%; height: 100%; background-color: {cap_color};'></div>
        </div>
    """

    with cell_rows[i // 4][i % 4]:
        st.markdown(f"""
        <div style='border: 1px solid #e0e0e0; border-radius: 16px; padding: 16px; background-color: #f9fcff;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.06); margin-bottom: 12px;'>
            <h4 style='text-align:center; color:#0078D4;'>🔋 Cell {i+1}</h4>
            <p style='margin: 4px 0;'>🔌 <b>Voltage:</b> {voltages[i]:.2f} V</p>
            <p style='margin: 4px 0;'>⚡ <b>Current:</b> {currents[i]:.2f} A</p>
            <p style='margin: 4px 0;'>🌡️ <b>Temp:</b> {temperatures[i]:.1f} °C</p>
            <p style='margin: 4px 0;'>📈 <b>Capacity:</b> {cap}%</p>
            {battery_bar}
           # <p style='margin: 8px 0; color: {mode_colors[modes[i]]}; font-weight:bold; font-size : 14px'>🔄 {modes[i]}</p>
        </div>
        """, unsafe_allow_html=True)

