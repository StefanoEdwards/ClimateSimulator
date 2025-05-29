'''
ENERGY BUDGET:
Visible light from the Sun carries energy to the earth. This light is absorbed by the
planet's surface. This energy is then re-emitted as infrared radiation. The planet will
continue to warm until the incoming energy = the outgoing energy.

ENERGY IN:
Satellites measure insolation at 1361 watts of power per m^2. To calculate the total amt
of energy arriving at earth, we have to multimply area * insolation. The area lit is calculated
by taking the area of a flat disk with the earth's diameter(since only 1/2 of earth) can be
in the sun at a time. 

Therefore:
E_intercepted = K_solar*π*R_Earth^2

Plugging in the earth's radius(6,371,000 m) and the insolation constant we find that our planet 
absorbs about 174 petawatts of sunlight. Earth reflects away about 30% of this energy because it is not 
completely black(this is called albedo).

So our final equation for energy flowing into earth is:
E_absorbed = K_solar*(1-albedo)*πR_earth^2

ENERGY OUT:
In the 1800s scientists determined that the amt of radiation emitted by an object depends
on its temperature. The equation for this relationship is called the Stefan-Boltzmann Law. It
states that the amount of energy emitted by an object is directly proportional to the fourth 
power of its surface temp. In other words, energy emissions go up a ton as temperature rises!

So: j = σ*T^4
j = energy per unit of time per unit area(watts per m^2)
σ = Stefan-Boltzmann constant = 5.67 * 10^-8 watts/m^2/K^4
T = temperature in Kelvin

This tells us how much IR radiation earth will emit per unit of area. We need to multiply it by
total area of earth's area to calculate the amount of energy emitted in total. Earth's entire surface 
is emitting radiation since it rotates, so we can't use the disk area from before(when only a part of 
the earth was recieving energy at a time). Formula for surface area is 4*π*r^2.

So our final equation for energy being emitted by earth is: 
E_emitted = σT^4*4πR_earth^2

σ = Stefan-Boltzmann constant = 5.67 * 10^-8 watts/m^2/K^4
T = Temperature in Kelvin(K)

FINDING BASELINE EQUILIBRIUM:
According to the law of conservation of energy, we know energy emitted must equal energy absorbed, if
we set out two values equal, we can sub in the expressions for each.

Therefore:
K_solar*(1-albedo)*πR_earth^2 = σT^4*4πR_earth^2

Simplifying:
K_solar*(1-albedo) = σT^4*4

Plugging in the solar constant(K_solar), Earth's albedo and Stefan-Boltzmann constant(σ) we can solve
for temperature(T). If we restructure the equation we find that:

T = ((K_solar*(1-albedo))/4σ)^0.25

Solving for temp with an albedo of 30%:
T = ((1361*(1-0.30))/(4*5.67*10^-8))^0.25 = 254.58K = -18.57C

Our calculated temp is much colder than the earth really is, the difference is that certain gasses
trap heat, preventing the escape of the emitted IR radation. This phenomena is called the greenhouse effect, 
and functions in a similar way to how a blanket traps heat, warming you up.

CO2 FORCING:
In my simple model, we treat the greenhouse contribution as an extra forcing on top of this equilibrium
temperature. Radiative transfer models translate downward radiation into a radiative forcing(ΔF-> W/m^2),
this effectively tells us how much energy is reaching the Earth's surface. Studies have shown that these
transfer models match up with the observed increase in energy, with very good accuracy(Puckrin et al 2004).

Scientists have derived a formula for calculating radiative forcing based on change in the amount of each 
GHG in the atmosphere(Myhre et al.). Each gas has a different radiative forcing formula, but the most important
is that of CO2: dF = 5.35 ln(C/C0)

dF = Radiative forcing in w/m^2
C = Atmospheric CO2 concentration
C0 = Pre-industrial CO2 concentration(280 ppm)

CLIMATE SENSITIVITY:
Now that we know how to calculate forcing, we need to cacluate its associated temperature change. We use
the climate sensitivity value to tell us how much the planet will warm or cool in response to a change in 
radiative forcing. The relationship between temperature change and radiative forcing is proportional and
the climate sensitivity value is the coefficient of proportionality.

The formula is: dT = λ*dF

dT = Change in earth's average surface temp
λ = Climate sensitivity(C/w/m^2)
dF = Radiative forcing

According to studies(IPCC 2007), we know that climate sensitivity values range from 2-4.5 degrees C of warming
for a doubling of CO2. We can plug in these values for climate sensitivity, to get the units we need:

λ = dT/dF = dT/(5.35*ln(n)) = (2 to 4.5 C)/3.7 = 0.54 to 1.2 C(/w/m^2) -> typical is 0.8K(/w/m^2)

Using this range of climate sensitivity values, we can plug in λ to calculate the expected temperature change. For 
example the CO2 concentration in 2010 was 390 ppm. Using this we can solve for the temperature:
dT = λ*dF = λ * 5.35 * ln(390/280) = 1.8*λ

Plugging in our possible climate sensitivity values, we can expect a surface temperature change of 1 - 2.2 degrees C 
of warming with the most likely value being 1.4C. The temperature change we calculate only takes CO2 forcing into account, 
but for our simulation this is good enough to get a reasonable estimation of climate change.

ALBEDO EFFECTS AND FEEDBACKS:
Albedo(α) determines how much solar energy is absorbed. As the planet warms, ice and show melt which reduces α. This 
is an example of a positive feedback loop. As well, warmer air holds more water vapor, amplifying greenhouse warming.
In our model we linearly adjust albedo with temperature to compensate for these loops, so even a small drop in α adds 
extra forcing, boosting temp.

LOCAL TEMP PROJECTION:
Toronto’s temperature mirrors the global temperature curve, but is amplified due to regional factors. High-latitude land areas (like Canada) are 
warming at about twice the global average due to polar amplification and regional feedbacks. Southern Ontario warms somewhat less but is still amplified, 
so for a rough estimate we multiply the global temp by a factor (~1.2x) to reflect this.

RCP SCENARIOS:
The IPCC (Intergovernmental Panel on Climate Change) developed a set of standardized emissions pathways known as RCPs (Representative 
Concentration Pathways). Each scenario describes a different trajectory of greenhouse gas emissions and concentrations, land use, and 
radiative forcing over time. They are named after their expected radiative forcing level by the year 2100 relative to preindustrial levels.

• RCP 2.6 “Strong Mitigation”: Radiative forcing peaks at 2.6 W/m² before 2100, then declines. This scenario requires immediate 
and aggressive emissions cuts, large-scale deployment of negative emissions technologies, and rapid decarbonization. Warming is kept below 2°C.
• RCP 4.5 “Stabilization”: Radiative forcing stabilizes at 4.5 W/m² by 2100. Emissions peak around 2040 then decline. This assumes 
moderate policy intervention and adoption of cleaner technology. Warming is likely to exceed 2°C but stay below 3C.
• RCP 6.0 “Delayed Stabilization”: Radiative forcing reaches 6.0 W/m² by 2100. Emissions continue rising until late in the century. This 
scenario assumes limited climate policies and higher reliance on fossil fuels for longer. Warming approaches 3C – 3.5C.
• RCP 8.5 “Business As Usual / High Emissions”: Radiative forcing reaches 8.5 W/m² by 2100. Assumes continued high population growth, fossil 
fuel dominance, and minimal climate mitigation efforts. CO₂ levels exceed 900 ppm by 2100. Global temperatures may rise 4C–5C or more, with 
devastating impacts.

Each of these scenarios is reflected in the simulation by adjusting the CO₂ growth rate and post-peak decline rate accordingly. The model 
uses those values to project atmospheric CO₂ and the resulting radiative forcing using Myhre’s formula (ΔF = 5.35 * ln(C/C0)). This feeds into 
the temperature calculation via climate sensitivity(λ).

EXPLAINING SHAPES OF CURVES:
The shapes of the curves in the simulation arise from exponential CO₂ growth and the resulting nonlinear response of temperature.

-CO₂ CURVE:
Initially, CO₂ follows exponential growth due to the annual growth rate. Once a peak year is reached, CO₂ may plateau or decline depending 
on the chosen scenario's mitigation strength (decline rate). The more aggressive the mitigation, the earlier and steeper the curve drops.

-GLOBAL TEMPERATURE CURVE:
The temperature curve follows a logarithmic response to CO₂ increase (because of the ln(C/C0) formula), but when coupled with exponential CO₂ 
growth, it creates an S-shaped curve. Initially, warming is slow, then it accelerates sharply before eventually plateauing, unless CO₂ levels 
continue rising unchecked, in which case warming continues.

ADDITIONAL NOTES:
This simulation simplifies the real Earth system but captures the core physics:
-It assumes radiative equilibrium without accounting for oceanic thermal inertia or internal variability (volcanic activity etc).
-It models only CO₂ forcing, excluding other GHGs like methane or aerosols, which can have cooling or warming effects.
-Feedbacks are simplified using a temperature-dependent albedo rather than modeling dynamic Earth systems like ice sheet collapse or permafrost melt.

Still, despite these simplifications, this kind of energy budget and radiative forcing model provides a scientifically sound and educational look into 
climate behavior and the importance of proper emissions policy.

SOURCES:
https://www.sciencedirect.com/topics/physics-and-astronomy/stefan-boltzmann-law
https://web.archive.org/web/20210605120431/https://scied.ucar.edu/earth-system/planetary-energy-balance-temperature-calculate
https://earthobservatory.nasa.gov/images/84499/measuring-earths-albedo
https://skepticalscience.com/empirical-evidence-for-co2-enhanced-greenhouse-effect-advanced.htm
https://www.carbonbrief.org/explainer-how-scientists-estimate-climate-sensitivity/
https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/temperature-change.html
https://en.wikipedia.org/wiki/Radiative_forcing
https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf
https://www.carbonbrief.org/explainer-the-high-emissions-rcp8-5-climate-scenario/
https://www.ipcc-data.org/guidelines/pages/glossary/glossary_r.html
'''

import streamlit as st
import math
import matplotlib.pyplot as plt

# CONSTANTS
S0 = 1361  # Solar constant (S0), total energy received from the sun per m^2 of earth's surface
sigma = 5.67e-8  # Stefan–Boltzmann constant(σ) relates temp to radiated energy
C0 = 280.0  # Pre-industrial CO₂ level (ppm), used as baseline for radiative forcing

T0_global = 15.0  # Baseline global average temp (historical avg)
T0_toronto = 9.0  # Baseline Toronto average temp
amplification_factor = 1.2  # Toronto warms faster than global avg (landlocked, loss of winter snow cover)
ocean_heat_delay = 0.02  # Fraction of heat absorbed annually by oceans

lambda_base = 0.8  # Climate sensitivity (degree per W/m²), how much temp rises per extra forcing
k_albedo = 0.005  # Albedo feedback coefficient, how albedo reduces as temp increases
alpha0 = 0.30  # Average global albedo

# ADJUST LAMBDA TO SIMULATE POSITIVE FEEDBACK LOOPS
def adjusted_lambda(current_temp):
    # Feedbacks (e.g., water vapor, ice melt) increase warming sensitivity
    # We increase λ slightly as global temperature rises
    return lambda_base * (1 + 0.01 * max(0, current_temp - T0_global))


# SIMULATE CLIMATE OVER COURSE OF 100 YEARS
def simulate(model_type, co2_initial, growth_rate, peak_year, decline_rate, decline_type):
    start_year = 2025
    end_year = 2125
    years = list(range(start_year, end_year + 1))

    co2 = co2_initial
    global_temp = T0_global
    toronto_temp = T0_toronto

    co2_values, global_temps, toronto_temps = [], [], []

    for year in years:
        # Apply growth or decline based on peak year and decline type
        if year <= peak_year:
            # Before peak: normal exponential growth
            co2 *= (1 + growth_rate)
        else:
            # After peak: apply decline based on selected method
            if decline_type == "Growth Rate Reduction":
                # Original method: gradually reduce growth rate
                current_growth = max(-decline_rate, growth_rate - decline_rate * (year - peak_year))
                co2 *= (1 + current_growth)
            else:  # "Direct CO₂ Decline"
                # New method: direct percentage decline in CO₂
                co2 *= (1 - decline_rate)

        # Radiative forcing from CO2 is equal to ΔF = 5.35 × ln(C/C0), C0 is preindustrial CO₂ level
        delta_F = 5.35 * math.log(co2 / C0)

        # Adjust climate sensitivity based on feedbacks if nonlinear
        if model_type == "Feedback Incorporated":
            lambda_eff = adjusted_lambda(global_temp)
        else:
            lambda_eff = lambda_base

        # Temperature rise is equal to climate sensitivity times radiative forcing: ΔT = λ × ΔF
        delta_T = lambda_eff * delta_F

        # Apply ocean delay to limit how fast temperature increases
        global_temp += (T0_global + delta_T - global_temp) * (1 - ocean_heat_delay)

        # Account for Toronto's amplified warming
        toronto_temp = T0_toronto + amplification_factor * (global_temp - T0_global)

        # Save simulation results to their arrays
        co2_values.append(co2)
        global_temps.append(global_temp)
        toronto_temps.append(toronto_temp)

    return years, co2_values, global_temps, toronto_temps


# DESCRIBE IMPACT OF CLIMATE CHANGE BASED ON PEAK TEMP
def get_impact_message(peak_temp):
    delta = peak_temp - T0_global
    if delta < 1.0:
        return "✅ Below 1°C warming: Minimal climate impacts."
    elif delta < 1.5:
        return "🟢 Up to 1.5°C: Manageable, but ecosystems stressed. Ice melt increases."
    elif delta < 2.0:
        return "🟠 Up to 2°C: High risk of floods, droughts, and biodiversity loss."
    elif delta < 3.0:
        return "🔴 Up to 3°C: Dangerous change—severe heatwaves, water stress, food threats."
    else:
        return "🚨 Above 3°C: Major tipping points, irreversible sea level rise, global disruption."


# PRESET SCENARIOS FROM IPCC (RCPs) WITH DETAILED DESCRIPTIONS
RCP_SCENARIOS = {
    "Custom": {
        "description": "Create your own custom emission scenario with manual parameter control.",
        "params": {}
    },
    "RCP2.6 - Strong Mitigation (2.6 W/m²)": {
        "description": "🌱 AGGRESSIVE ACTION: Immediate massive emissions cuts, carbon capture technology, global cooperation. Warming limited to ~1.5-2°C. Requires transforming energy systems within 10-15 years.",
        "params": {
            "co2_initial": 390,
            "growth_rate": 0.005,
            "peak_year": 2030,
            "decline_rate": 0.015
        }
    },
    "RCP4.5 - Moderate Action (4.5 W/m²)": {
        "description": "🔄 STEADY PROGRESS: Moderate climate policies, clean energy adoption, emissions peak by 2040s then decline. Warming ~2-3°C. Achievable with current technology + political will.",
        "params": {
            "co2_initial": 400,
            "growth_rate": 0.008,
            "peak_year": 2040,
            "decline_rate": 0.008
        }
    },
    "RCP6.0 - Delayed Action (6.0 W/m²)": {
        "description": "⏰ TOO LITTLE, TOO LATE: Limited climate action, emissions continue growing until 2080s. Heavy fossil fuel use persists. Warming ~3-4°C with serious consequences.",
        "params": {
            "co2_initial": 400,
            "growth_rate": 0.010,
            "peak_year": 2080,
            "decline_rate": 0.003
        }
    },
    "RCP8.5 - Business as Usual (8.5 W/m²)": {
        "description": "🔥 WORST CASE: No climate action, continued fossil fuel dominance, CO₂ >900ppm by 2100. Warming 4-5°C+ causing catastrophic impacts: sea level rise, ecosystem collapse, food crises.",
        "params": {
            "co2_initial": 420,
            "growth_rate": 0.012,
            "peak_year": 2100,
            "decline_rate": 0.000
        }
    }
}


# STREAMLIT UI
st.title("🌍 Climate Change Simulator")

st.markdown("""
Explore future CO₂ levels and temperatures under different emission pathways. 
Based on IPCC Representative Concentration Pathways (RCPs) and energy balance physics.
""")

# Select emission scenario and model type
scenario = st.selectbox(
    "Select Emission Scenario", 
    list(RCP_SCENARIOS.keys()),
    help="Choose from IPCC standardized scenarios representing different levels of climate action"
)

# Display scenario description
if scenario in RCP_SCENARIOS:
    st.info(RCP_SCENARIOS[scenario]["description"])

model_type = st.selectbox(
    "Climate Model Type", 
    ["Linear", "Feedback Incorporated"],
    help="Linear uses constant climate sensitivity. Feedback Incorporated includes amplifying feedbacks like water vapor and ice-albedo effects."
)

# Load scenario defaults
defaults = RCP_SCENARIOS.get(scenario, {}).get("params", {})

# Advanced options
with st.expander("🔧 Simulation Parameters"):
    col1, col2 = st.columns(2)
    
    with col1:
        co2_initial = st.slider(
            "Initial CO₂ (ppm)", 
            300, 500, 
            defaults.get("co2_initial", 420),
            help="Starting atmospheric CO₂ concentration in 2025"
        )
        growth_rate = st.slider(
            "Annual CO₂ Growth Rate (%)", 
            0.1, 3.0, 
            defaults.get("growth_rate", 0.012) * 100,
            help="Yearly percentage increase in CO₂ before emissions peak"
        ) / 100
    
    with col2:
        peak_year = st.slider(
            "Emissions Peak Year", 
            2025, 2125, 
            defaults.get("peak_year", 2060),
            help="Year when global emissions reach maximum and begin declining"
        )
        
        decline_type = st.selectbox(
            "Post-Peak Decline Method",
            ["Direct CO₂ Decline", "Growth Rate Reduction"],
            help="Direct decline shows dramatic CO₂ drops. Growth rate reduction is more gradual."
        )
        
        if decline_type == "Direct CO₂ Decline":
            decline_rate = st.slider(
                "Annual CO₂ Decline After Peak (%)", 
                0.1, 1.5, 
                min(1.5, defaults.get("decline_rate", 0.008) * 100),
                help="Direct yearly CO₂ reduction (kept realistic - max 1.5%/year)"
            ) / 100
        else:
            decline_rate = st.slider(
                "Annual Growth Rate Reduction After Peak (%)", 
                0.1, 3.0, 
                defaults.get("decline_rate", 0.008) * 100,
                help="Rate of emissions reduction after peak year"
            ) / 100

# RUN SIMULATION
years, co2_vals, global_temps, toronto_temps = simulate(
    model_type, co2_initial, growth_rate, peak_year, decline_rate, decline_type
)

# PLOT GLOBAL & TORONTO AVERAGE TEMPERATURES
fig1, ax1 = plt.subplots(figsize=(12, 7))
ax1.plot(years, global_temps, label="Global Average Temperature", color="red", linewidth=2)
ax1.plot(years, toronto_temps, label="Toronto Average Temperature", color="orange", linewidth=2)
ax1.axhline(T0_global + 1.5, linestyle="--", color="green", alpha=0.7, label="1.5°C Paris Target")
ax1.axhline(T0_global + 2.0, linestyle="--", color="orange", alpha=0.7, label="2.0°C Paris Limit")
ax1.axhline(T0_global + 3.0, linestyle="--", color="red", alpha=0.7, label="3.0°C Danger Zone")
ax1.axvline(peak_year, linestyle=":", color="gray", alpha=0.7, label=f"Emissions Peak ({peak_year})")
ax1.set_title("Projected Temperature Changes", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Temperature (°C)", fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

# PLOT CO2 CONCENTRATION
fig2, ax2 = plt.subplots(figsize=(12, 7))
ax2.plot(years, co2_vals, label="Atmospheric CO₂", color="green", linewidth=2)
ax2.axhline(C0, linestyle="--", color="blue", alpha=0.7, label=f"Pre-industrial ({C0} ppm)")
ax2.axhline(450, linestyle="--", color="orange", alpha=0.7, label="450 ppm (2°C target)")
ax2.axhline(550, linestyle="--", color="red", alpha=0.7, label="550 ppm (danger zone)")
ax2.axvline(peak_year, linestyle=":", color="gray", alpha=0.7, label=f"Emissions Peak ({peak_year})")
ax2.set_title("Projected Atmospheric CO₂ Levels", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("CO₂ Concentration (ppm)", fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# SUMMARY STATISTICS
st.subheader("Simulation Results")

col1, col2, col3, col4 = st.columns(4)

peak_temp = max(global_temps)
peak_co2 = max(co2_vals)
temp_2100 = global_temps[75] if len(global_temps) > 75 else global_temps[-1]  # Temperature in 2100
co2_2100 = co2_vals[75] if len(co2_vals) > 75 else co2_vals[-1]  # CO₂ in 2100

with col1:
    st.metric("Peak Global Warming", f"{peak_temp - T0_global:.1f}°C", f"vs. pre-industrial")

with col2:
    st.metric("Peak CO₂ Level", f"{peak_co2:.0f} ppm", f"{peak_co2 - C0:.0f} ppm above pre-industrial")

with col3:
    st.metric("Warming by 2100", f"{temp_2100 - T0_global:.1f}°C", f"Global average")

with col4:
    st.metric("CO₂ by 2100", f"{co2_2100:.0f} ppm", f"Atmospheric concentration")

# CLIMATE IMPACT ASSESSMENT
impact_summary = get_impact_message(peak_temp)
st.subheader("Climate Impact Assessment")
st.markdown(f"**Peak Global Temperature:** {peak_temp:.2f}°C (+{peak_temp - T0_global:.1f}°C above pre-industrial)")
st.info(impact_summary)

# ADDITIONAL INSIGHTS
if decline_type == "Direct CO₂ Decline" and peak_year < 2100:
    final_co2 = co2_vals[-1]
    if final_co2 < peak_co2 * 0.8:
        st.success(f"✅ Significant CO₂ reduction achieved: {peak_co2:.0f} ppm → {final_co2:.0f} ppm by 2125")
    
if peak_temp - T0_global > 3.0:
    st.error("⚠️ **CRITICAL WARNING**: This scenario leads to dangerous climate change with potentially catastrophic consequences.")
elif peak_temp - T0_global < 2.0:
    st.success(f"✅ **GOOD NEWS**: This scenario keeps warming below 2°C, avoiding the worst climate impacts.")

# METHODOLOGY DISPLAY
with st.expander("📚 About This Simulation"):
    st.markdown("""
    **Physics-Based Model**: This simulation uses real climate physics including:
    - Stefan-Boltzmann Law for Earth's energy balance
    - Logarithmic CO₂ radiative forcing (Myhre et al.)
    - Climate sensitivity from IPCC studies
    - Ocean thermal inertia effects
    
    **Limitations**: Simplified model excludes other greenhouse gases, aerosols, 
    detailed feedback mechanisms, and natural climate variability.
    
    **Data Sources**: IPCC AR6, NASA Earth Observatory, peer-reviewed climate studies.
    """)