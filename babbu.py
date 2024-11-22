import streamlit as st

def nortons_theorem(vth, rth, rl):
    # Calculate Norton current (I_N)
    in_ = vth / (rth + rl)
    # Norton resistance (R_N) is equal to Thevenin resistance (R_th)
    rn = rth
    return in_, rn

st.title("Norton's Theorem Calculator")

st.markdown('''
Norton's Theorem states that any linear electrical network with voltage sources and resistances can be replaced with an equivalent current source in parallel with a single resistor. 
This tool helps you calculate the Norton equivalent circuit from given Thevenin voltage, Thevenin resistance, and load resistance.
''')

vth = st.number_input('Enter the Thevenin voltage (V):', min_value=0.0)
rth = st.number_input('Enter the Thevenin resistance (Ω):', min_value=0.0)
rl = st.number_input('Enter the load resistance (Ω):', min_value=0.0)

if st.button('Calculate Norton Equivalent'):
    in_, rn = nortons_theorem(vth, rth, rl)
    st.write(f'Norton Current (I_N): {in_:.2f} A')
    st.write(f'Norton Resistance (R_N): {rn:.2f} Ω')

st.write('''
Example:
- Thevenin Voltage (V_th): 10V
- Thevenin Resistance (R_th): 5Ω
- Load Resistance (R_L): 10Ω
The Norton equivalent current (I_N) is 0.67 A and the Norton equivalent resistance (R_N) is 5Ω.
''')
