import streamlit as st
import re
import random
import webbrowser
from datetime import datetime
import wikipedia
import pywhatkit as pwk

now = datetime.now()
day = str(now)
time = now.day, now.month, now.year
wikipedia.set_lang("id")
sapabot = "iya ada yang bisa aku bantu?"
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .css-1q1n0ol{display: none}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.title("AI Chan Bot")
with st.container():
    user = st.text_input("masukan pertanyaan")
    btn = st.button("tanya?",'#00f900')

if btn:
        if re.findall(r'sekarang|tanggal',user,):
            st.info(f"bot\t : sekarang tanggal{time}")
        elif re.findall(r'haii|hallo|hello|Hallo|Haii|Hello',user):
            st.info(f"bot\t: {sapabot}")
        elif re.findall(r'namaku',user):
            st.info("bot\t: namamu adalah salman")
        elif re.findall(r'namamu',user):
            st.info("bot\t: namaku adalah AI Chan")
        elif re.findall(r'putar|Putar', user):
            st.info("bot\t: ini sudah ku Putarkan")
            video = user.replace('open','')
            pwk.playonyt(video)
        elif re.findall(r'aku sayang kamu|sayang',user):
            st.info("bot\t: maaf aku hanyalah sebuah program yang dibuat oleh manusia 😔")
        elif re.findall(r'ngapain',user):
            st.info("bot\t: aku lagi nganggur liatin kamu 😁")
        elif re.findall(r'bantuin', user):
            st.info("bot\t: aku siap kok bantuin kamu 😁")
        elif re.findall(user,user):
            st.info("bot\t: ini sudah ku carikan")
            try:
                wiki = wikipedia.summary(user)
                st.info(f"bot\t: {wiki}")
            except:
                try:
                    read = webbrowser.open("https://www.google.com/search?q="+user)
                except:
                    st.info("bot\t: maaf Tidak Mengerti")      
        