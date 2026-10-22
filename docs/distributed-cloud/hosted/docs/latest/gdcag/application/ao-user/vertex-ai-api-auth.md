---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth/
title: Authenticate Vertex AI API requests \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:17.355207+00:00
---

# Authenticate Vertex AI API requests  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Authenticate Vertex AI API requests Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to authenticate calls to Vertex AI services on Google Distributed Cloud (GDC) air-gapped. You must set up token authentication to secure your requests to the Vertex AI API within your air-gapped applications. This process validates your API requests by providing your identity and authorizing your interactions. 

This page is for application developers within application operator groups responsible for setting up their application and development environments to enable AI features. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To authenticate API requests and configure service accounts, request the necessary permissions from your administrator. Also make sure that you have your project set up for Vertex AI. For more information, see [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).

  * Make sure to update your local trust store before you set up authentication in your development environment.



### Request IAM roles

Contact your IAM Project Admin to request the following roles in your project namespace:

  * **IAM Project Admin** (`project-iam-admin`): create service accounts and manage role bindings in the project namespace.
  * **AI OCR Developer** (`ai-ocr-developer`): authenticate requests to the OCR API.
  * **AI Speech Developer** (`ai-speech-developer`): authenticate requests to the Speech-to-Text API.
  * **AI Speech Chirp Developer** (`ai-speech-chirp-developer`): authenticate requests to the Speech-to-Text Chirp model.
  * **AI Text Embedding Developer** (`ai-text-embedding-developer`): authenticate requests to the `Text-Embedding-Gecko` model.
  * **AI Text Embedding Multilingual Developer** (`ai-text-embedding-multilingual-developer`): authenticate requests to the `Text-Multilingual-Embedding` model.
  * **AI Translation Developer** (`ai-translation-developer`): authenticate requests to the Vertex AI Translation API.
  * **Vertex AI Prediction User** (`vertex-ai-prediction-user`): authenticate prediction requests to Online Prediction models.



For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

## Authenticating to Vertex AI services

Interactions with Vertex AI services are done through authentication tokens. Tokens are digital objects that verify your identity and authorization after you provide valid credentials. The token carries specific information about your account and the permissions it has to access and operate with services and resources.

There are two ways you can set up authentication:

  * Authenticate with your user account
  * Authenticate with your service account



### Authenticate with your user account

The following guides you through getting an authentication token for your user account:

  1. Note [the endpoint of the API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status) you want to use.

  2. Gain access to the Vertex AI service or Generative AI model you want to use by granting your user account the corresponding role listed in [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

  3. Sign in to Distributed Cloud with the user account you have to interact with the API:
         
         gdcloud auth login
         

  4. Get the authentication token:
         
         gdcloud auth print-identity-token --audiences=https://ENDPOINT
         

Replace `ENDPOINT` with the API endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

Depending on the intended use of the authentication token, you might need to include the port after the service endpoint in the audiences path as follows:

     * If you use a [client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries) for your request, you must include port `:443` after the service endpoint in the audiences path. Therefore, the `--audiences` path in the command must be `https://ENDPOINT:443`.
     * If you use gRPC, `curl`, or programmatic REST calls for your request, don't include the port. Therefore, the `--audiences` path in the command must be `https://ENDPOINT`.

The output displays the authentication token. Add the token to the header of the command-line requests you make, as in the following example:
    
    -H "Authorization: Bearer TOKEN"
    

Replace `TOKEN` with the value for the authentication token that the output displays.




### Authenticate with your service account

The following guides you through getting an authentication token for your service account:

  1. Note [the endpoint of the API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status) you want to use.

  2. [Set up the service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project#set-up-service) you want to use to access the Vertex AI service or Generative AI model.

  3. Grant the service account the corresponding role listed in [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions) to let it gain access to the service or model you want to use.

  4. [Get the service key pairs of your service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities#list_credentials_for_service_accounts).

  5. Set the following environment variable:
         
         export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_SERVICE_KEY
         

Replace `PATH_TO_SERVICE_KEY` with the path to the JSON file that contains the key pairs of your service account.

  6. Install the `google-auth` client library:
         
         pip install google-auth
         

  7. Add the following code to a Python script:
         
         import os
         import google.auth
         from google.auth.transport import requests
         import requests as reqs
         
         os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PATH_TO_SERVICE_KEY"
         os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "CERT_NAME"
         
         # If you use a client library for your request,
         # you must include port :443 after the service endpoint
         # in the audience path.
         audience = "https://ENDPOINT"
         
         creds, project_id = google.auth.default()
         print(project_id)
         creds = creds.with_gdch_audience(audience)
         
         def test_get_token():
           sesh = reqs.Session()
           req = requests.Request(session=sesh)
           creds.refresh(req)
           print(creds.token)
         
         if __name__=="__main__":
           test_get_token()
         

Replace the following:

     * `PATH_TO_SERVICE_KEY`: the path to the JSON file that contains the key pairs of your service account.
     * `CERT_NAME`: the name of the Certificate Authority (CA) certificate file, such as `org-1-trust-bundle-ca.cert`. You only need this value if you are in a development environment. Otherwise, omit it.
     * `ENDPOINT`: the API endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status). Depending on the intended use of the authentication token, you might need to include the port after the service endpoint in the audience path as follows:

       * If you use a [client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries) for your request, you must include port `:443` after the service endpoint in the audience path. Therefore, the `audience` path in the script must be `"https://ENDPOINT:443"`.
       * If you use gRPC, `curl`, or programmatic REST calls for your request, don't include the port. Therefore, the `audience` path in the script must be `"https://ENDPOINT"`.
  8. Save the Python script.

  9. Run the Python script to fetch the token:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `token.py`.

The output displays the authentication token. Add the token to the header of the command-line requests you make, as in the following example:
         
         -H "Authorization: Bearer TOKEN"
         

Replace `TOKEN` with the value for the authentication token that the output displays.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
