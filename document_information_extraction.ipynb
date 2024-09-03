# Import Document Information Extraction (DOX) API client
from sap_business_document_processing import DoxApiClient
# CONTENT_TYPE_UNKNOWN lets the library fetch the content type automatically based on the file's extension
from sap_business_document_processing.document_information_extraction_client.constants import CONTENT_TYPE_PDF
import json

# Insert your DOX service key json here and change true -> True
service_key = {}

# Assign service key values to authenticate
url = service_key['url']
uaa_url = service_key['uaa']['url']
client_id = service_key['uaa']['clientid']
client_secret = service_key['uaa']['clientsecret']

# Instantiate object used to communicate with Document Information Extraction REST API
api_client = DoxApiClient(url, client_id, client_secret, uaa_url)

# OPTIONAL: Token can be used to interact with e.g. swagger UI to explore DOX API
print(api_client.session.token)
print(f"\nYou can use this token to authorize here and explore the API via Swagger UI: \n{api_client.base_url}")

# Specify the fields that should be extracted
header_fields = [
         "recipe_name",
         "portions"
    ]
line_item_fields = [
         "ingredients",
         "quantity"
    ]

# Extract information from invoice document
document_result = api_client.extract_information_from_document(document_path='<PATH TO YOUR FILE/YOUR FILENAME>', 
                                                               client_id='default', 
                                                               document_type='custom', 
                                                               schema_id='YOUR SCHEMA ID',
                                                               mime_type=CONTENT_TYPE_PDF, 
                                                               header_fields=header_fields, 
                                                               line_item_fields=line_item_fields)

# Print the extracted data
print(json.dumps(document_result, indent=2))
