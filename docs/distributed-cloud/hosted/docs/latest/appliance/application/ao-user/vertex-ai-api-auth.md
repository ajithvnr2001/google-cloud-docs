---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth/
title: Authenticate API requests \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:49.536794+00:00
---

# Authenticate API requests  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Authenticate API requests Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI on Google Distributed Cloud (GDC) air-gapped appliance provides APIs and services that require authentication. Authentication is how you prove your identity to access services by using tokens.

Tokens are digital objects that verify a caller provided proper credentials and that they have been successfully exchanged for the token. The token carries information about the identity of the requesting account and the specific access it is authorized to have.

This page describes how to authenticate to Vertex AI APIs programmatically. Depending on whether you access the Vertex AI APIs as a user or with a service account, this page describes the steps to get an authentication token for your API requests.

Choose one of the following options to get an authentication token:

###  User account 

Follow these steps to get an authentication token with user permissions:

  1. Note [the endpoint of the API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status) you want to use.

  2. Gain access to the Vertex AI service you want to use by granting your user account the corresponding role listed in [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions).

  3. Sign in to GDC air-gapped appliance with the user account you have to interact with the API:
         
         gdcloud auth login
         

  4. Get the authentication token:
         
         gdcloud auth print-identity-token --audiences=https://ENDPOINT
         

Replace `ENDPOINT` with the service endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).

Depending on the intended use of the authentication token, you might need to include the port after the service endpoint in the audiences path as follows:

     * If you use a [client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) for your request, you must include port `:443` after the service endpoint in the audiences path. Therefore, the `--audiences` path in the command must be `https://ENDPOINT:443`.
     * If you use gRPC, `curl`, or programmatic REST calls for your request, don't include the port. Therefore, the `--audiences` path in the command must be `https://ENDPOINT`.



The output displays the authentication token. Add the token to the header of the command-line requests you make, as in the following example:
    
    
    -H "Authorization: Bearer TOKEN"
    

Replace `TOKEN` with the value for the authentication token that the output displays.

###  Service account 

Follow these steps to get an authentication token with a service account:

  1. Note [the endpoint of the API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status) you want to use.

  2. [Set up the service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service) you want to use to access the Vertex AI service.

  3. Grant the service account the corresponding role listed in [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions) to let it gain access to the service you want to use.

  4. [Get the service key pairs of your service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/service-identity#create_and_add_key_pairs).

  5. Install the `google-auth` client library:
         
         pip install google-auth
         

  6. Add the following code to a Python script:
         
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
     * `ENDPOINT`: the service endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status). Depending on the intended use of the authentication token, you might need to include the port after the service endpoint in the audience path as follows:

       * If you use a [client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) for your request, you must include port `:443` after the service endpoint in the audience path. Therefore, the `audience` path in the script must be `"https://ENDPOINT:443"`.
       * If you use gRPC, `curl`, or programmatic REST calls for your request, don't include the port. Therefore, the `audience` path in the script must be `"https://ENDPOINT"`.
  7. Save the Python script.

  8. Run the Python script to fetch the token:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `token.py`.




The output displays the authentication token. Add the token to the header of the command-line requests you make, as in the following example:
    
    
    -H "Authorization: Bearer TOKEN"
    

Replace `TOKEN` with the value for the authentication token that the output displays.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
