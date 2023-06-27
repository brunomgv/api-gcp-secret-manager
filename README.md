# Project Name

A simple Flask application for retrieving secrets from Google Cloud Secret Manager.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Endpoints](#endpoints)
  - [License](#license)

## Description

This project is a Flask application that allows you to retrieve secrets stored in Google Cloud Secret Manager. It provides an endpoint that accepts a secret ID as a query parameter and returns the corresponding secret value.

The application uses the `google-cloud-secret-manager` library to access the secrets and requires a service account key with the necessary permissions to authenticate with Google Cloud.

## Prerequisites

Before running this application, ensure that you have the following prerequisites:

- Python 3.x installed on your system
- A Google Cloud project with Secret Manager enabled
- A service account key file (in JSON format) with Secret Manager read access

## Installation

1. Clone this repository to your local machine or download the source code.
2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt

## Usage
Place the service account key file (service-account-key.json) in the project directory.

Modify the project_id variable in the app.py file and replace it with your Google Cloud project ID.

Optionally, if you want to use a specific version of the secret, modify the version_id variable in the app.py file.

Run the application using the following command:

```shell
python app.py
```

The Flask application will start running on http://localhost:5000.

Use an HTTP client (e.g., cURL, Postman) to send a GET request to the /get-secret endpoint with the secret_id query parameter set to the ID of the secret you want to retrieve. For example:

```shell
GET http://localhost:5000/get-secret?secret_id=my-secret
```

The application will return the secret value if it exists.

## Endpoints
- `/get-secret`: GET request to retrieve a secret from Google Cloud Secret Manager.

Query Parameters:

- secret_id (required): The ID of the secret to retrieve.
Response:

- If the secret is found, the response body will contain the secret value.
- If the secret is not found or if the secret_id parameter is missing, an error message will be returned.
  
## License
This project is licensed under the MIT License.

