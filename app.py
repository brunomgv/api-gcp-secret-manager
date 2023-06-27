from flask import Flask, request
from google.cloud import secretmanager
from google.oauth2 import service_account

app = Flask(__name__)

# Var definition
project_id = ""
version_id = "latest"
auth_file = "service-account-key.json"

# Function to retrieve the secret from GCP
def get_secret(secret_id):
    credentials = service_account.Credentials.from_service_account_file(auth_file)
    client = secretmanager.SecretManagerServiceClient(credentials=credentials)
    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": secret_name})
    return response.payload.data.decode("UTF-8")

# Endpoint
@app.route("/get-secret")
def get_secret_endpoint():
    secret_id = request.args.get("secret_id")
    if secret_id is None:
        return "Error: No secret ID provided.", 400

    secret_value = get_secret(secret_id)
    return secret_value

if __name__ == "__main__":
    app.run()