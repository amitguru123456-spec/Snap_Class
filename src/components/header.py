import streamlit as st

def header_home():
    logo_url="app/static/header_logo.png"
    st.markdown(f"""
<style>
.logo-img {{
    margin-bottom:5px;
    animation: float 3s ease-in-out infinite;
    transition: filter 0.3s ease, transform 0.3s ease;
    filter: drop-shadow(0 0 10px rgba(140,140,255,0.4));
}}
.logo-img:hover {{
    filter: drop-shadow(0 0 25px rgba(180,180,255,0.8));
    transform: scale(1.05);
}}
@keyframes float {{
    0%, 100% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-10px); }}
}}
</style>
 <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
    <img class="logo-img" src="{logo_url}" height="100">
    <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
</div>
""", unsafe_allow_html=True)


def header_dashboard():
    logo_url="app/static/header_logo.png"
    st.markdown(f"""
   
<div style="display:flex; align-items:center; justify-content:center; gap:0px">
    <img src="{logo_url}" style="height:90px; margin-right:-15px; top:-9px; position:relative; "/>
    <h2 style="margin:0; padding:0; text-align:left; color:#5865F2; white-space: nowrap;">SNAP<br/>CLASS</h2>
</div>


""",unsafe_allow_html=True)