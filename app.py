from pytube import YouTube
import streamlit as st

# def download_youtube_video_in_audio(url):
#     yt = YouTube(url)

#     audios = yt.streams.filter(only_audio=True).order_by('abr').asc()
#     audios_map = dict(map(lambda x:(audios.index(x),x),audios))

#     audio_quality = list(map(lambda x:int(x.abr[:-4]),audios))

#     max_audio_quality_index = audio_quality.index(max(audio_quality))
#     selected = audios_map[max_audio_quality_index]
#     selected.download()

    # print('Successfully downloaded')
    # st.header('This is a header')

st.header('Audio Convertor')
st.text('Youtube Video ➡ Audio')
url = st.text_input('Enter the youtube url','')
try:
    if url == '':
        st.warning('You need to enter a correct URL to get the download button')
        st.button('Download Audio',on_click=None)
    else:
        yt = YouTube(url)

        audios = yt.streams.filter(only_audio=True).order_by('abr').asc()
        audios_map = dict(map(lambda x:(audios.index(x),x),audios))

        audio_quality = list(map(lambda x:int(x.abr[:-4]),audios))

        max_audio_quality_index = audio_quality.index(max(audio_quality))
        selected = audios_map[max_audio_quality_index]

        st.download_button('Download Audio', selected.download())
except:
    st.error('YouTube Url is incorrect')