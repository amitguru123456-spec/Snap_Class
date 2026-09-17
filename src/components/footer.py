import streamlit as st

def footer_home():
    logo_url="app/static/footer.png"
    st.markdown(f"""
     <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; item-align:center">
    <p style="font-weight:bold; color:black;">Created by</p>
<img src="{logo_url}" style="max-height:40px; margin-top:-7px; margin-left:-14px;">
</div>
""",unsafe_allow_html=True)


def footer_dashboard():
    logo_url="app/static/footer.png"
    st.markdown(f"""
     <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; item-align:center">
    <p style="font-weight:bold; color:black;">Created by</p>
<img src="{logo_url}" style="max-height:40px; margin-top:-7px; margin-left:-14px;"/>
</div>
""",unsafe_allow_html=True)
    