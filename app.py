from io import BytesIO
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from utiltest import preprocess_image, classify_face_shape  # Import utility functions
from about_page import about_page
from sidebar_style import apply_sidebar_style
from facedetector   import detect_face
from hairstyles_text import hairstyle_tips

# Load the trained models
model = load_model('face_shape_cnn_model.h5')
model.compile(optimizer='adam', loss='binary_cross entropy', metrics=['accuracy'])


def main_page():
    #st.title("Hairstyle Recommendation System", font_size="2rem")
    with st.container():
        st.title("Hairstyle Recommendation System")
    #st.write("Use one of the options below to provide your face image and get hairstyle recommendations:")

    # Load the image
    banner = Image.open("images/about/banner.png")

    # Display the image
    st.image(banner, use_column_width=True)
    # Option for uploading an image
    st.markdown("""
              <h5 style="text-align: left;">Please upload an image or capture one using the webcam.</h5>
          """, unsafe_allow_html=True)

    uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if st.button("Take Selfie"):
        camera_input = st.camera_input("")
        st.markdown("""
                        <div style="color: red; font-size: 1rem; text-align: center;">
                            Please click again the "Take selfie" button to see the result.
                        </div>
                    """, unsafe_allow_html=True)
    else:
        camera_input = None

    # Option for capturing an image from the webcam
    #camera_input = st.camera_input("Or capture image from webcam")

    # Choose between uploaded image and camera input
    if uploaded_image:
        # Convert uploaded image to PIL format
        image = Image.open(uploaded_image)
        #st.write("Analyzing your face shape...")
        #face_detected, face_image= detect_face

        #st.image(image, caption="Uploaded Image")
    elif camera_input:
        # Convert camera input to image
        image = Image.open(BytesIO(camera_input.read()))
        #face_detected, face_image = detect_face(image)
        #sst.write("Analyzing your face shape...")
        #st.image(image, caption="Captured Image", use_column_width=True)
        #st.image(image, caption="Detected Face")
    else:
        st.write("")
        st.stop()


    #st.write("Detecting face...")
    face_detected, face_image = detect_face(image)
    #st.write(f"Face detected: {face_detected}")
    if not face_detected:
        st.error("No face detected.")
        st.markdown("""
            <div style="color: red; font-size: 1rem; text-align: center;">
                Please ensure the face is clearly visible and try again.
            </div>
        """, unsafe_allow_html=True)
        st.stop()
    if face_detected:

        st.image(face_image, caption="Detected Face")



    # Process the image
    processed_image = preprocess_image(image)
    face_shape = classify_face_shape(model, processed_image)
    #Result container
    face_shape_container = st.container()
    st.markdown("""
        <style>
            .face-shape-container {
                text-align: center;
            }
            .face-shape-text {
                font-size: 1rem;
                font-weight: bold;
            }
            .face-shape-result {
                font-size: 3rem;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display face shape text and result in the center
    with face_shape_container:
        st.markdown(
            f"<div class='face-shape-container'>"
            f"<div class='face-shape-text'>Your face shape is</div>"
            f"<div class='face-shape-result' style='color: #5e17eb '>{face_shape.capitalize()}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

    #st.write(f"### Recommended Hairstyles for {face_shape.capitalize()} face:")
    #st.write(f"Your face shape is: **{face_shape.capitalize()}**")



    #st.markdown(f"### Recommended Hairstyles for a {face_shape.capitalize()} Face")
    st.markdown(f"""
      #### Tips for a **{face_shape.capitalize()}-shaped face:**
      {hairstyle_tips[face_shape]}
      """, unsafe_allow_html=True)
    #st.write(f"### Recommended Hairstyles for {face_shape.capitalize()} face:")
    st.write(f"### Recommended Hairstyles")

    # Load and display recommended hairstyle images
    #aspect_ratio = image.width / image.height
    #target_height = 300
    #target_width = int(target_height * aspect_ratio)
    def crop(result_pic):
        # Resize the image to the target width and height while maintaining the aspect ratio
        width, height = result_pic.size

        aspect_ratio = height / width
        target_height= 300
        target_width = int(target_height * aspect_ratio)
        return result_pic.resize((target_width, target_height))
    try:
        recommended_image1 = Image.open(f'src/data//{face_shape}/recommended_1.jpg')
        recommended_image2 = Image.open(f'src/data/{face_shape}/recommended_2.jpg')



        #recommended_resize1 = crop(recommended_image1)
        #recommended_resize2 = crop(recommended_image2)
        #recommended_resize2 = resize_image(recommended_image2, target_width, target_height)
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image1, caption='')
            st.markdown("<h6 style='text-align: center;'>For Female</h6>", unsafe_allow_html=True)

        with col2:
            st.image(recommended_image2, caption='')
            st.markdown("<h6 style='text-align: center;'>For Male</h6>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.write("Recommended hairstyle images not found for this face shape.")

    st.write(f"### Hairstyles to Avoid:")

    # Load and display avoided hairstyle images
    try:
        avoid_image1 = Image.open(f'src/data/{face_shape}/avoid_1.jpg')
        avoid_image2 = Image.open(f'src/data/{face_shape}/avoid_2.jpg')

        #avoid_resize1 = crop(avoid_image1)
        #avoid_resize2 = crop(avoid_image2)
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(avoid_image1, caption='')
            st.markdown("<h6 style='text-align: center;'>For Female</h6>", unsafe_allow_html=True)
        with col2:
            st.image(avoid_image2, caption='')
            st.markdown("<h6 style='text-align: center;'>For Male</h6>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.write("Avoided hairstyle images not found for this face shape.")


# Sidebar navigation
apply_sidebar_style()
#page = st.sidebar.selectbox("Main menu", ["Application", "About"])
st.sidebar.markdown("<h1>Main Menu</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["Application", "About"])
if page == "Application":
    main_page()
elif page == "About":
    about_page()

