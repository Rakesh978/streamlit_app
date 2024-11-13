import streamlit as st
st.title("Thevenin's Theroem")

def caluclate_thevenins(vth,Rth,RL):
    il=vth/(Rth+RL)
    pl=il*il*RL
    return il,pl

tab1,tab2=st.tabs(["Compute","Explain"])
with tab1:
    col1,col2=st.columns(2)

    with col1:
        with st.container(border=True):
            vth=st.number_input("Vth (V)",value=10)
            Rth=st.number_input("Rth (Ohms)",value=100)
            RL=st.number_input("RL (Ohms)",value=100)
            compute=st.button("Computes")
    with col2:
        if compute:
            il,pl=caluclate_thevenins(vth,Rth,RL)
            st.write(f"load current={il} A")    
            st.write(f"load power={pl} W") 

with tab2:
    st.write("This is explanation tab")