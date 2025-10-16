from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(file):
    try:
        credential = AzureKeyCredential(Config.KEY)
        doc_intelligence_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        card_info = doc_intelligence_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=file)
        )
        result = card_info.result()
        for document in result.documents:
            fields = document.fields
            return {
                "Card Number": fields.get("CardNumber").value if fields.get("CardNumber") else None,
                "Expiration Date": fields.get("ExpirationDate").value if fields.get("ExpirationDate") else None,
                "Cardholder Name": fields.get("CardholderName").value if fields.get("CardholderName") else None,
                "Bank Name": fields.get("BankName").value if fields.get("BankName") else None,
                "Issuer": fields.get("Issuer").value if fields.get("Issuer") else None,
            }
    except Exception as e:
        print(f"Error analyzing credit card: {e}")
        return None