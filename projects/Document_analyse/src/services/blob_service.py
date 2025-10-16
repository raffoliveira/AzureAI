import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.Config import Config

def upload_to_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(Config.CONTAINER_NAME)
        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(file, overwrite=True)
        blob_url = f"{blob_client.url}"
        return blob_url
    except Exception as e:
        st.error(f"Error uploading file to Blob Storage: {e}")
        return None