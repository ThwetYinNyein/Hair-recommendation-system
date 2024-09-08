import streamlit as st

def about_page():
    st.title("About Face Shapes")
    #st.subheader("Find the Perfect Hairstyle for Your Face Shape")

    # Photo banner
    #st.image("images/about/banner.png", use_column_width=True)

    st.write("Here's a brief overview of five common face shapes:")

    st.write("<h3 style='color:#5e17eb'>Oval</h3>", unsafe_allow_html=True)
    st.image("web_assets/about_oval.jpg", width=200)
    st.write(
        "An oval face shape is characterized by a balanced and symmetrical appearance. The forehead is slightly wider than the chin, and the cheeks are the widest part of the face. Oval faces can typically wear a wide variety of hairstyles."
    )

    st.write("<h3 style='color:#5e17eb'>Heart</h3>", unsafe_allow_html=True)
    st.image("web_assets/about_heart.jpg", width=200)
    st.write(
        "A heart-shaped face has a wider forehead and cheekbones with a narrow chin. Hairstyles that balance the width of the forehead with the narrow chin are ideal for heart-shaped faces."
    )

    st.write("<h3 style='color:#5e17eb'>Square</h3>", unsafe_allow_html=True)
    st.image("web_assets/about_squre.jpg", width=200)
    st.write(
        "A square face shape has a strong jawline and a forehead that is roughly the same width as the cheekbones. Hairstyles that soften the angles of the face and add height on top work well."
    )

    st.write("<h3 style='color:#5e17eb'>Round</h3>", unsafe_allow_html=True)
    st.image("web_assets/about_round.jpg", width=200)
    st.write(
        "A round face shape features full cheeks and a rounded jawline. The width and length of the face are roughly equal. Hairstyles that add height and create an illusion of length are recommended."
    )

    st.write("<h3 style='color:#5e17eb'>Oblong</h3>", unsafe_allow_html=True)
    st.image("web_assets/about_oblong.jpg", width=200)
    st.write(
        "An oblong face shape is longer than it is wide, with a straight cheek line and sometimes a high forehead. Hairstyles that add width and balance the length of the face are beneficial."
    )
    # Add the "Analyze Now" button
    #if st.button("Analyze Now"):
    #    st.session_state["page"]="Application"
    #st.experimental_return() to update streamlit version
    #if st.session_state["page"]=="Application":
    #    main_page()


