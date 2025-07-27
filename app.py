import streamlit as st

# --- App Title ---
st.title("📈 Refined Tier Profit Calculator")

# --- Initial Tier Data ---
tiers = {
    "T2": {"raw_qty": 100, "raw_price": 75, "refined_value": 8690},
    "T3": {"raw_qty": 316, "raw_price": 86, "refined_value": 48927},
    "T4": {"raw_qty": 499.28, "raw_price": 84, "refined_value": 118222},
    "T5": {"raw_qty": 1183.29, "raw_price": 367, "refined_value": 653197},
    "T6": {"raw_qty": 2492.8, "raw_price": 1699, "refined_value": 5374338},
    "T7": {"raw_qty": 4923.25, "raw_price": 3922, "refined_value": 24882818},
    "T8": {"raw_qty": 7778.8, "raw_price": 10244, "refined_value": 93560202},
}

st.markdown("Edit the raw quantity, raw price, and market value for each tier:")

# --- User Inputs ---
for tier in tiers:
    with st.expander(f"🔧 {tier} Settings"):
        tiers[tier]['raw_qty'] = st.number_input(f"{tier} Raw Quantity", value=float(tiers[tier]['raw_qty']), step=1.0)
        tiers[tier]['raw_price'] = st.number_input(f"{tier} Raw Price", value=float(tiers[tier]['raw_price']), step=1.0)
        tiers[tier]['refined_value'] = st.number_input(f"{tier} Refined Market Value", value=float(tiers[tier]['refined_value']), step=100.0)

# --- Calculation Function ---
def calculate_profits(tiers):
    results = {}
    previous_total_cost = 0
    for tier, data in tiers.items():
        crafting_cost = data["raw_qty"] * data["raw_price"]  # Only this tier
        total_cost = crafting_cost + previous_total_cost     # Cumulative
        profit = data["refined_value"] - total_cost
        profit_percent = (profit / total_cost) * 100 if total_cost != 0 else 0

        results[tier] = {
            "Crafting Cost (This Tier)": round(crafting_cost),
            "Total Cost (Up to Tier)": round(total_cost),
            "Refined Value": round(data["refined_value"]),
            "Profit": round(profit),
            "Profit %": round(profit_percent, 2)
        }

        previous_total_cost = total_cost

    return results

# --- Calculate and Display ---
results = calculate_profits(tiers)

st.subheader("📊 Results Summary")
st.write("Profit is calculated based on total raw cost up to each tier.")

# --- Display Table ---
st.table({
    tier: {
        "Crafting Cost": f"{data['Crafting Cost (This Tier)']:,}",
        "Total Cost": f"{data['Total Cost (Up to Tier)']:,}",
        "Refined Value": f"{data['Refined Value']:,}",
        "Profit": f"{data['Profit']:,}",
        "Profit %": f"{data['Profit %']}%"
    }
    for tier, data in results.items()
})
