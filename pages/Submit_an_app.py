import streamlit as st
from os import mkdir
from os.path import exists, join

st.title('Submit an App')

with st.form('app_form'):
    app_name = st.text_input('App name:')
    app_main_file = st.file_uploader('App main file:')
    app_files = st.file_uploader('App files:', accept_multiple_files=True)

    if st.form_submit_button('Submit'):
        if not app_name:
            st.write('Please enter app name!')
            st.stop()

        if not app_main_file:
            st.write('Please choose app main file!')
            st.stop()

    app_slug = app_name.replace(' ', '_')
    app_path = join('apps', app_slug)

    st.write(app_main_file.getvalue())
    # st.write(app_slug)
    # st.write(app_path)

    if app_files and not exists(app_path):
        mkdir(app_path)

    # for file in uploaded_files:
