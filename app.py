import pandas as pd
import streamlit as st
import numpy as np
import os
import joblib
import sklearn

model = joblib.load("music_recommender.pkl")

df = pd.DataFrame({
    "male" : [10 , 20 , 30 , 40],
    "female" : [20 , 40 , 50 , 60]
})




with st.sidebar:
    st.image(os.path.join(os.getcwd() , "static" , "BG.jpg"))
    st.title("muscic recommender")
    choice = st.radio("Navigation" , ["About Us" , "Here's How" , "Our Product"])
    st.info("This will showcase a basic on what will be our presntation on YIC program")

if choice == "About Us":
    st.title("ABOUT US")
    st.subheader("Project Overview")
    st.write('''
                We are a passionate team dedicated to blending technology and creativity to create innovative solutions. Our goal is to explore the potential of machine learning in understanding human preferences, starting with something we all love—music!

                Through this project, we aim to predict your favorite music genre and recommend personalized playlists. This is just the beginning, and we are excited to showcase what our technology can achieve.

                Thank you for joining us on this journey of innovation!

             ''')
    st.divider()
    st.subheader("Motivation")
    st.write('''
                "We are passionate about exploring AI's potential to positively impact lives. Our goal is to recommended the best possible music base on your gender and age" ''')

    st.divider()
    st.subheader("Technology Used")
    st.write('''
            "Our project is powered by cutting-edge machine learning algorithms, including support vector machines (SVM) and Naive Bayes. We've also built an interactive platform using Streamlit for music-recommender"  ''')

    st.divider()
    st.subheader("Special Thanks")
    st.write("Special thanks to Madam Mimi and Sir haedir for mentoring us in this journey")

    st.divider()
    st.subheader("Contanct Information")
    st.write("Contact Us We’d love to hear from you! If you have any questions, feedback, or collaboration inquiries, feel free to reach out.")
    st.write("Email: contact@music-recommender.ai")
    st.write("Address: 123 AI Innovation Street, Gambang , Malaysia")
    st.write("Social Media:")
    st.write("\tInstagram : @YourPersonalMusicRecommender")
    st.write("\tTwitter : @YourPersonalMusicRecommender")
    st.write("\tFacebook : @YourPersonalMusicRecommender")


if choice == "Here's How":
    st.title("LET'S LEARN")
    st.write("In this section we will learn how we make our model")

    st.write("Base on our survay using google form there's been in high demand on music playlist recommender")
    st.write("This can be shown by the graph below")
    st.line_chart(df)

    st.divider()
    st.subheader("Key Feature's")
    st.write("Music taste detection: Using our latest machine learning model we can recommend you the best suited genre of music ")
    st.write("Music recommender playlist: Base on you prefered genre we will will give the best playlist you can have")

    st.divider()
    st.subheader("User statisfactory")
    st.bar_chart(df)

if choice == "Our Product":
    gender = st.selectbox("Enter your gende" , ["male" , "female"])
    age = st.slider("Enter your age")

    if gender == "male":
        genderInput = 1
    else:
        genderInput = 0 


    X = np.array([[age , genderInput]])

    if st.button("Predict Your music Taste"):
        prediction = model.predict(X)[0]
        st.success(f"You maybe like {prediction}")
    
        playlists = {
            "HipHop": ["HipHop Playlist 1 (Spotify Link)", "HipHop Playlist 2 (YouTube Link)"],
            "Classical": ["Classical Playlist 1 (Spotify Link)", "Classical Playlist 2 (YouTube Link)"],
            "Dance": ["Dance Playlist 1 (Spotify Link)", "Dance Playlist 2 (YouTube Link)"],
            "Jazz": ["Jazz Playlist 1 (Spotify Link)", "Jazz Playlist 2 (YouTube Link)"],
        }

        if prediction in playlists:
            st.write("here's some playlist for you")
            for playlist in playlists[prediction]:
                st.write(f"-{playlist}")

        else:
            st.write("Sorry there's no playlist in this genre yet")
    