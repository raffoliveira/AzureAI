import streamlit as st
from services.blob_service import upload_to_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title("Card Generator :card_file_box:")
    uploaded_file = st.file_uploader("Upload your image here", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        file_name = uploaded_file.name
        blob_url = upload_to_blob(uploaded_file, file_name)
        if blob_url:
            st.write(f"File uploaded successfully!")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("File upload failed. Please try again.")

def show_image_and_validation(image_url, credit_card_info):
    st.image(image_url, caption="Uploaded Image", use_column_width=True)
    st.write("Extracted Credit Card Information:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Valid Card</h1>", unsafe_allow_html=True)
        st.write(f"**Card Name:** {credit_card_info['card_name']}")
        st.write(f"**Bank Name:** {credit_card_info['bank_name']}")
        st.write(f"**Expiration Date:** {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Invalid Card</h1>", unsafe_allow_html=True)
        st.write("The uploaded image does not contain a valid credit card.")


if __name__ == "__main__":
    configure_interface()
