---
url: https://docs.cloud.google.com/api-gateway/docs/authenticate-api-keys/
title: Use API Keys \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:19.645644+00:00
---

# Use API Keys  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/authenticate-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use API Keys

This page describes how to use API keys in API Gateway.

## Overview

An API key is a string that identifies a Google Cloud project for quota, billing, and monitoring purposes. Developers generate an API key in a project in the Google Cloud console. They then embed that key in every call to your API as a query parameter or in a request header.

If you specify an API key requirement in your API config, API Gateway uses the API key to look up the associated Google Cloud project. API Gateway rejects requests unless the API key was generated in your Google Cloud project or within other Google Cloud projects in which your API has been enabled.

**Note:** Unlike credentials that use short-lived tokens or signed requests, API keys are included as part of the API request. As a result, API keys are susceptible to [man-in-the-middle attacks](https://wikipedia.org/wiki/Man-in-the-middle_attack) and are less secure than other authentication credentials. You can use API keys in addition to one of the other [supported forms of authentication](https://docs.cloud.google.com/api-gateway/docs/authentication-method), but we don't recommend using _only_ API keys when API calls contain sensitive data.

## Create an API key

Create an API key, or view API keys already available within your Google Cloud project, go to the **APIs & Services** > **Credentials** page and complete the steps described in [Create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key). 

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

## Configure API key authentication for API Gateway

Configure API key authentication for API Gateway to secure access to your gateway using an API key, as described in the following sections.

  1. Enable API key support for your service. 

### Google Cloud console

Do the following:

     1. In the Google Cloud console, go to **APIs & Services > Library**. 

[Go to APIs & Services Library](https://console.cloud.google.com/apis/library)

     2. In the search bar, enter the Managed Service name of the API. You can find this value in the **Managed Service** column for your API on the APIs landing page. For example: 
            
            my-api-123abc456def1.apigateway.my-project.cloud.goog

     3. Click the service card to view the landing page.
     4. On the landing page for your service, click **Enable**. **Note** : There may be a delay of up to 30 minutes or more between the time you create your API and the time it appears in the Library.

### Google Cloud CLI

Enter the following command, where MANAGED_SERVICE_NAME specifies the name of the managed service created when you deployed the API. This can be viewed in the Managed Service property listed with the `gcloud api-gateway apis describe` command.
    
    gcloud services enable MANAGED_SERVICE_NAME

For example:
    
    gcloud services enable my-api-123abc456def1.apigateway.my-project.cloud.goog

  2. Modify the OpenAPI specification used to create your API config to include instructions to enforce an API key validation security policy on all traffic. Add the `security` type and `securityDefinitions` or `securitySchemes` as shown: 

### OpenAPI 2.0
         
         # openapi2-functions.yaml
           swagger: '2.0'
           info:
             title: API_ID optional-string
             description: Sample API on API Gateway with a Google Cloud Functions backend
             version: 1.0.0
           schemes:
             - https
           produces:
             - application/json
           paths:
             /hello:
               get:
                 summary: Greet a user
                 operationId: hello
                 x-google-backend:
                   address: https://GCP_REGION-PROJECT_ID.cloudfunctions.net/helloGET
                 **security :
                 - api_key: []**
                 responses:
                   '200':
                     description: A successful response
                     schema:
                       type: string
           **securityDefinitions :
             # This section configures basic authentication with an API key.
             api_key:
               type: "apiKey"
               name: "key"
               in: "query"**

The `securityDefinition` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the spec.

### OpenAPI 3.x
         
         # openapi-functions.yaml
         openapi: 3.0.4
         info:
           title: API_ID optional-string
           description: Sample API on API Gateway with a Google Cloud Functions backend
           version: 1.0.0
         # Define reusable components in x-google-api-management
         x-google-api-management:
           backends:
             functions_backend:
               address: https://GATEWAY_LOCATION-PROJECT_ID.cloudfunctions.net/helloGET
               pathTranslation: APPEND_PATH_TO_ADDRESS
               protocol: "http/1.1"
         # Apply the backend configuration by referencing it by name. Set at the root so this applies to all operations unless overridden.
         x-google-backend: functions_backend
         components:
         # This section configures basic authentication with an API key.
           **securitySchemes :
             google_api_key:
               type: apiKey
               name: x-api-key
               in: header
         security:
           - google_api_key: []**
         paths:
           /hello:
             get:
               summary: Greet a user
               operationId: hello
               responses:
                 '200':
                   description: A successful response
                   content:
                     application/json:
                       schema:
                         type: string

The `securitySchemes` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the spec.

  3. Create a new API config with the modified OpenAPI description using the following command: 
         
         gcloud api-gateway api-configs create NEW_CONFIG_ID \
         --api=API_ID --openapi-spec=NEW_API_DEFINITION \
         --project=PROJECT_ID --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

For example: 
         
         gcloud api-gateway api-configs create **my-config-key** \
           --api=**my-api** --openapi-spec=**openapi-functions.yaml** \
           --project=**my-project** --backend-auth-service-account=**0000000000000compute@developer.gserviceaccount.com**

  4. Run the following command to [update your existing gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api#updating_a_gateway) with the new API config: 
         
         gcloud api-gateway gateways update GATEWAY_ID \
           --api=API_ID --api-config=NEW_CONFIG_ID \
           --location=GATEWAY_LOCATION --project=PROJECT_ID

For example: 
         
         gcloud api-gateway gateways update **my-gateway** \
           --api=**my-api** --api-config=**my-config-key** \
           --location=**us-central1** --project=**my-project**




## Restrict API keys

By default, API keys are unrestricted, which makes them vulnerable to unauthorized use. Add [application restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#adding-application-restrictions) and [API restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#adding-api-restrictions) whenever possible.

API restrictions specify which APIs can be called using the API key. All API keys used by production applications should have API restrictions.

Application restrictions specify which websites, IP addresses, or apps can use an API key. For more information, see [Add application restrictions](https://docs.cloud.google.com/authentication/api-keys#adding-application-restrictions).

Aside: **Note** : If you use **HTTP referrers (websites)** as an application restriction, you must include a scheme (for example, `https://`) when you add the website restriction. For example, `https://example.com/*` is a valid restriction, but `example.com/*` is not.

To add API restrictions:

  1. Find the title of the API as noted in your API Config. In the following example, the API title is `My Example Config`: 

### OpenAPI 2.0
         
         # openapi.yaml
         swagger: '2.0'
         info:
           **title : My Example Config**
           description: Sample API on API Gateway
           version: 1.0.0
         ...

### OpenAPI 3.x
         
         # openapi.yaml
         openapi: 3.0.4
         info:
           **title : My Example Config**
           description: Sample API on API Gateway
           version: 1.0.0
         ...

  2. In the Google Cloud console, go to the **APIs & Services** > **Credentials** page. 

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  3. Select the name of the API key you want to use for your API.

  4. In the **API restrictions** section of the API key detail page, click **Restrict key**.

  5. Select the API that your API key will be used to access from the drop-down list of available APIs. For example, select `My Example Config`.

  6. Click **Save**.




Your restriction should take effect momentarily.

## Use API keys

To use API Gateway features such as [quotas](https://docs.cloud.google.com/api-gateway/docs/quotas-overview), you can pass in an API key so that API Gateway can identify the Google Cloud project that the client application is associated with.

For example, you can pass it using the `key` query parameter in a curl call, as follows:
    
    
    https://GATEWAY_URL/hello?key=API_KEY

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
