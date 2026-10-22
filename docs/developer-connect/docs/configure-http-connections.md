---
url: https://docs.cloud.google.com/developer-connect/docs/configure-http-connections/
title: Configure and use generic HTTP connections \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:55.356934+00:00
---

# Configure and use generic HTTP connections  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/configure-http-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Configure and use generic HTTP connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a connection to a generic HTTP endpoint.

In addition to the Git repository connections and [account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors), you can also set up a Developer Connect connection to a generic HTTP endpoint. This lets you establish and manage connections to many third-party developer tools, services, and APIs, as long as those tools are accessible using HTTP endpoints.

## Create an HTTP connection

HTTP connections support [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) (username and password) and [bearer token authentication](https://datatracker.ietf.org/doc/html/rfc6750). Both authentication types require that you [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) in Secret Manager.

###  Bearer token auth 

  1. Use Secret Manager to [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and a secret version, containing your token.

The token is your personal access token or API token that give you access to the tool for which you're creating this connection.

  2. To create the connection using bearer token authentication, run the following command:
         
         gcloud developer-connect connections create CONNECTION_ID \
         --location=REGION \
         --project=PROJECT_ID \
         --http-config-host-uri=HOST_URI \
         --http-config-bearer-token-authentication-secret-version=TOKEN_SECRET_VERSION \
         --http-config-service-directory=SERVICE_DIRECTORY_SERVICE \
         --http-config-ssl-ca-certificate=SSL_CERTIFICATE_FILE_PATH \
         --git-proxy-config-enabled
         

Replace the following:

     * CONNECTION_ID with a unique ID for this new connection.
     * REGION with the Google Cloud region in which you're creating this connection.
     * PROJECT_ID with the Google Cloud project ID.
     * HOST_URI with the base HTTPS endpoint (for example, https://api.myservice.com).
     * TOKEN_SECRET_VERSION with the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret version resource name for the authentication token.
     * SERVICE_DIRECTORY_SERVICE with the [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) resource name for private network access. This is optional.
     * SSL_CERTIFICATE_FILE_PATH with the path to a local file containing the SSL CA certificate content. This is optional.
     * Include the `--git-proxy-config-enabled` option to access this connection using the [Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).



###  Basic auth 

  1. Use Secret Manager to [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and a secret version, containing your username and password.

  2. To create the connection using basic authentication, run the following command:
         
         gcloud developer-connect connections create CONNECTION_ID \
         --location=REGION \
         --project=PROJECT_ID \
         --http-config-host-uri=HOST_URI \
         --http-config-basic-authentication-username=USERNAME \
         --http-config-basic-authentication-password-secret-version=PASSWORD_SECRET_VERSION \
         --http-config-service-directory=SERVICE_DIRECTORY_SERVICE \
         --http-config-ssl-ca-certificate=SSL_CERTIFICATE_FILE_PATH \
         --git-proxy-config-enabled \
         

Replace the following:

     * CONNECTION_ID with a unique ID for this new connection.
     * REGION with the Google Cloud region in which you're creating this connection.
     * PROJECT_ID with the Google Cloud project ID.
     * HOST_URI with the base HTTPS endpoint (for example, https://api.myservice.com).
     * USERNAME with the username for basic username-password authentication.
     * PASSWORD_SECRET_VERSION with the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret version resource name for the password, for basic username-password authentication. (For example: `projects/01234567890/secrets/exampletool-api-pw/versions/1`.)
     * SERVICE_DIRECTORY_SERVICE with the [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) resource name for private network access. This is optional.
     * SSL_CERTIFICATE_FILE_PATH with the path to a local file containing the SSL CA certificate content. This is optional.
     * Include the `--git-proxy-config-enabled` option to access this connection using the [Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).



After the connection is created, you can access it using the connection resource name in Developer Connect.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
