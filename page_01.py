import requests
import streamlit as st
import numpy as np

st.set_page_config(page_title="Hello", page_icon="Cao")

st.markdown("Streamlit je super")

query=st.text_input("Pretraga gifa")
url= "https://api.giphy.com/v1/gifs/search"
params= {"api_key": st.secrets.api_key, "q": query, "limit":10 }
response= requsts.get(url=url, params=params).json()

while not query:
    st.stop()
    
gif_url=response["data"][np.random.randint(0, 10)]["embed_url"]
st.write(
    f'<iframe src="{gif_url}" width="480" height="240">',
    unsafe_allow_html=True,
)