import streamlit as st
import requests

url = 'https://<here>.ngrok.io'


st.title('text to video')
start = st.container()

with start:
    col1, col2 = st.columns([1,2])
    num_frames = col1.selectbox('Select a frame number', options=range(10,30), index=0)
    prompt = col2.text_input('prompt', '')
    
    if len(prompt)>0:
        
        
        response = requests.get(url,params = {'prompt':prompt, 'num_frames':num_frames})
        if response.status_code == 200:
            st.video(response.content, format="video/mp4")
        else:
            st.write('error_status {}'.format(response.status_code))
            st.write('error_message {}'.format(response.content))