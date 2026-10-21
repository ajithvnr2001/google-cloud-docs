---
url: https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app/
title: Manage OAuth application \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:59.881232+00:00
---

# Manage OAuth application  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Manage OAuth application Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to manage OAuth-based application integrations with Google Cloud.

**Important:** OAuth application integration works only with Identity-Aware Proxy.

**Note:** These steps and the `projects.locations.oauthClients` API are only for [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). To create and manage standard OAuth 2.0 client IDs for Google Cloud users or services, go to the Google Cloud console, then go to [**APIs & Services >Credentials**](https://console.cloud.google.com/apis/credentials).

At a high level, to integrate an OAuth-based application, you do the following:

  1. [Create an OAuth client](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#create).
  2. [Create an OAuth client credential](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#create-credential).
  3. In the OAuth client credential, obtain the client secret. To learn about risks associated with storing and accessing the client secret and strategies that can help mitigate them, see [OAuth client and credential security risks and mitigations](https://docs.cloud.google.com/iam/docs/workforce-oauth-app#security).



After you have completed these steps, the OAuth-based application can access Google Cloud products and data. You can use the registered OAuth client credentials to exchange authorization codes or refresh tokens with the [Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview).

## Before you begin

  1. You must have a Google Cloud organization set up.

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. You must have set up a workforce identity pool and provider in the organization in which you will register the OAuth application. Learn how to set up workforce identity federation for [Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id), [Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta), and [other OIDC and SAML 2.0 providers](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).




## Required roles

To get the permissions that you need to register an OAuth application for your organization, ask your administrator to grant you the [IAM OAuth Client Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.oauthClientAdmin) (`roles/iam.oauthClientAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Manage OAuth clients

This section shows you how to manage OAuth clients.

### Create an OAuth client

To create an OAuth client, do the following:

### gcloud
    
    
    gcloud iam oauth-clients create APP_OAUTH_CLIENT_ID \
        --project=PROJECT_ID \
        --location=global \
        --client-type="CONFIDENTIAL_CLIENT" \
        --display-name="My OAuth application" \
        --description="An application registration for MyApp" \
        --allowed-scopes="https://www.googleapis.com/auth/cloud-platform" \
        --allowed-redirect-uris="REDIRECT_URI" \
        --allowed-grant-types="authorization_code_grant"
    

Replace the following:

  * `APP_OAUTH_CLIENT_ID`: a client ID to represent this OAuth client.
  * `PROJECT_ID`: the ID of the project where you created your workforce identity pool and provider. The project must be created in the organization where your workforce pool and provider were created.
  * `REDIRECT_URI`: the redirect URI for the OAuth application—for example, `https://myapp.com/signin-callback`.



### REST
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      -d "{ \
            'allowedGrantTypes': ['AUTHORIZATION_CODE_GRANT'], \
            'allowedRedirectUris': ['REDIRECT_URI'], \
            'allowedScopes': ['https://www.googleapis.com/auth/cloud-platform'], \
            'clientType': 'CONFIDENTIAL_CLIENT', \
            'description': 'My OAuth client description', \
            'disabled': false, \
            'displayName': 'My OAuth client'}" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients\?oauthClientId\=APP_OAUTH_CLIENT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created your workforce identity pool and provider. The project must be created in the organization where your workforce pool and provider were created.
  * `REDIRECT_URI`: the redirect URI for the OAuth application—for example, `https://myapp.com/signin-callback`.
  * `APP_OAUTH_CLIENT_ID`: a client ID to represent this OAuth client.



After you register the application, you create the OAuth client credential and obtain the secret that the OAuth application uses to access Google Cloud.

### List OAuth clients

To list registered OAuth clients, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients list \
        --project=PROJECT_ID \
        --location=global
    

### REST
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients
    

Replace `PROJECT_ID` with the ID of the project where your OAuth applications are registered.

### Describe an OAuth client

To describe an OAuth client, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients describe APP_OAUTH_CLIENT_ID \
        --project PROJECT_ID \
        --location global
    

Replace the following:

  * `APP_OAUTH_CLIENT_ID`: the ID of the OAuth client that you want to to describe
  * `PROJECT_ID`: the ID of the project where you registered your OAuth application



### REST
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the ID of the OAuth client that you want to to describe



### Update an OAuth client

To update an OAuth client, run the following command.

### gcloud
    
    
    gcloud iam oauth-clients update APP_OAUTH_CLIENT_ID \
        --project=PROJECT_ID \
        --location=global \
        --allowed-redirect-uris="REDIRECT_URI"
    

Replace the following:

  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID for the OAuth client that you want to update
  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `REDIRECT_URI`: the redirect URI for the OAuth application



To update other fields, use flags listed in `gcloud iam oauth-clients update`.

### REST
    
    
    curl -d'{"allowedRedirectUris":"REDIRECT_URI"}' \
      -H "Content-Type: application/json" -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID?update_mask=allowed_redirect_uris
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID for the OAuth client that you want to update
  * `REDIRECT_URI`: the redirect URI for the OAuth client



To update other fields, set `update_mask` to the field names listed in `gcloud iam oauth-clients update`.

### Delete an OAuth client

To delete an OAuth client, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients delete APP_OAUTH_CLIENT_ID \
        --project PROJECT_ID \
        --location global
    

Replace the following:

  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID to delete
  * `PROJECT_ID`: the ID of the project where you registered your OAuth application



### REST
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID to delete



## Manage OAuth client credentials

This section shows you how to manage OAuth client credentials for the OAuth client.

### Create an OAuth client credential

To create an OAuth client credential, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients credentials create APP_OAUTH_CLIENT_CREDENTIAL_ID \
        --oauth-client=APP_OAUTH_CLIENT_ID \
        --display-name='My OAuth client credential' \
        --location='global'
    

Replace the following:

  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: an ID that represents this client credential
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID you can obtain by describing the registered OAuth client application



### REST
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      -d "{'disabled': false, 'displayName': 'My OAuth client credential'}" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials\?oauthClientCredentialId=APP_OAUTH_CLIENT_CREDENTIAL_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID you can obtain by describing the registered OAuth client application
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: an ID that represents this client credential



### List OAuth client credentials

To list OAuth client credentials, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients credentials list \
        --oauth-client=APP_OAUTH_CLIENT_ID \
        --project=PROJECT_ID \
        --location=global
    

Replace the following:

  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID for which to list credentials
  * `PROJECT_ID`: the ID of the project where you registered your OAuth application



### REST
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/$PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID for which to list credentials



### Describe an OAuth client credential

To describe an OAuth client credential, run the following command. You can obtain the client secret by inspecting the output.

### gcloud
    
    
    gcloud iam oauth-clients credentials describe APP_OAUTH_CLIENT_CREDENTIAL_ID \
        --oauth-client=APP_OAUTH_CLIENT_ID \
        --location='global'
    

Replace the following:

  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the redirect URI for the OAuth client
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID you can obtain by describing the client application registration



### REST
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
    https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials/APP_OAUTH_CLIENT_CREDENTIAL_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the redirect URI for the OAuth client
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID you can obtain by describing the client application registration



In the output, `clientSecret` is the client secret. This is the secret that the OAuth application uses to access Google Cloud.

**Warning:** The client secret must be stored securely. If the client secret is leaked, you must delete and re-create the client credential. To learn more, see [OAuth client and credential security risks and mitigations](https://docs.cloud.google.com/iam/docs/workforce-oauth-app#security).

### Update an OAuth client credential

To update an OAuth client credential, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients credentials update APP_OAUTH_CLIENT_CREDENTIAL_ID \
        --client-id=APP_OAUTH_CLIENT_ID \
        --display-name="My new credential name" \
        --location=global
    

### REST
    
    
    curl -d'{"displayName":"My new credential name"}' -X PATCH \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials/APP_OAUTH_CLIENT_CREDENTIAL_ID?update_mask=display_name
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the redirect URI for the OAuth client
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID that you can obtain by describing the client application registration



### Disable an OAuth client credential

Before you can delete an OAuth client credential, you must disable it. To disable the OAuth client credential, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients credentials update APP_OAUTH_CLIENT_CREDENTIAL_ID \
        --oauth-client=APP_OAUTH_CLIENT_ID \
        --disabled \
        --project=PROJECT_ID \
        --location=global
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the client credential ID to disable



### REST
    
    
    curl -d'{"disabled":"true"}' \
      -H "Content-Type: application/json" -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials/APP_OAUTH_CLIENT_CREDENTIAL_ID?update_mask=disabled
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the OAuth client ID
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the client credential ID to disable



### Delete an OAuth client credential

To delete an OAuth client credential, run the following command:

### gcloud
    
    
    gcloud iam oauth-clients credentials delete APP_OAUTH_CLIENT_CREDENTIAL_ID \
        --project=PROJECT_ID \
        --oauth-client=APP_OAUTH_CLIENT_ID \
        --location=global
    

Replace the following:

  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the OAuth client ID
  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the client credential ID



### REST
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      https://iam.googleapis.com/v1/projects/PROJECT_ID/locations/global/oauthClients/APP_OAUTH_CLIENT_ID/credentials/APP_OAUTH_CLIENT_CREDENTIAL_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you registered your OAuth application
  * `APP_OAUTH_CLIENT_ID`: the client credential ID
  * `APP_OAUTH_CLIENT_CREDENTIAL_ID`: the OAuth client ID



## What's next

  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Cloud OAuth API overview](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview)
  * [Identity-Aware Proxy with workforce identity federation](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
