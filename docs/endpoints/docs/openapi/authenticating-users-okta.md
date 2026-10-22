---
url: https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users-okta/
title: Using Okta to authenticate users \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:44.741639+00:00
---

# Using Okta to authenticate users  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users-okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Using Okta to authenticate users Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This page describes how to support user authentication in Cloud Endpoints.

To authenticate a user, a client application must send a [JSON Web Token (JWT)](https://jwt.io/) in the authorization header of the HTTP request to your backend API. The [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/glossary#extensible_service_proxy) validates the token on behalf of your API, so you don't have to add any code in your API to process the authentication. However, you do need to configure your OpenAPI document to support your chosen authentication methods.

ESP validates a JWT in a performant way by using the JWT's issuer's public keys. ESP caches the public keys for five minutes. In addition, ESP caches validated JWTs for five minutes or until JWT expiry, whichever happens first.

## Before you begin

  * Add authentication code to your client application, following the [Okta integration guide for Google Cloud Endpoints](https://www.okta.com/sites/default/files/OktaIntegrationGuide_GoogleCloudEndpoints_Feb2019.pdf).



  * When your client application sends an HTTP request, the authorization header in the request must contain the following JWT claims: 
    * `iss` (issuer)
    * `sub` (subject)
    * `aud` (audience)
    * `iat` (issued at)
    * `exp` (expiration time)



## Configuring ESP to support client authentication

You must have a [security requirement object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#securityRequirementObject) and a [security definitions object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#securityDefinitionsObject) in your OpenAPI document for ESP to validate the claims in the signed JWT. 

As explained in the _Okta integration guide for Google Cloud Endpoints_ , you make the following changes to your OpenAPI document:

### OpenAPI 2.0

  1. Add the following to your OpenAPI specification: 
         
         securityDefinitions:
           okta_jwt:
             authorizationUrl: ""
             flow: "implicit"
             type: "oauth2"
             x-google-issuer: "https://YOUR_OKTA_TENANT_NAME.com"
             x-google-jwks_uri: "https://YOUR_OKTA_TENANT_NAME.com/oauth2/v1/keys"
             x-google-audiences: "YOUR_OKTA_CLIENT_ID"

Where:

     * YOUR_OKTA_TENANT_NAME is the name of your Okta tenant.
     * YOUR_OKTA_CLIENT_ID is the client ID that you created in your Okta tenant.
  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
            -   okta_jwt: []




### OpenAPI 3.x

  1. Add the following to your OpenAPI specification: 
         
         components:
           securitySchemes:
             okta_jwt:
               type: oauth2
               flows:
                implicit:
                  authorizationUrl: ""
                  scopes: {}
               x-google-auth:
                 issuer: https://YOUR_OKTA_TENANT_NAME.com
                 jwksUri: https://YOUR_OKTA_TENANT_NAME.com/oauth2/v1/keys
                 # Optional.
                 audiences:
                   - YOUR_OKTA_CLIENT_ID

Where:

     * YOUR_OKTA_TENANT_NAME is the name of your Okta tenant.
     * YOUR_OKTA_CLIENT_ID is the client ID that you created in your Okta tenant.
  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
           - okta_jwt: []




You can define multiple security definitions in the OpenAPI document, but each definition must have a different issuer. If you use security sections at both the API level and at the method level, the method-level settings override the API-level settings. 

The `x-google-audiences` or `audiences` field isn't required. ESP accepts all JWTs with the backend service name in the form of `https://SERVICE_NAME` in the `aud` claim. To allow additional client IDs to access the backend service, you can specify the allowed client IDs in the `x-google-audiences` or `audiences` field by using comma-separated values. ESP then accepts the JWTs with any of the specified client IDs in the `aud` claim. 

You can also customize JWT locations by adding `x-google` extensions. For details, see [OpenAPI 2.0 extensions or ](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-jwt-locations)[OpenAPI 3.x extensions](https://docs.cloud.google.com/endpoints/docs/openapi/oasv3-extensions). 

## Making an authenticated call to an Endpoints API

When you send a request using an authentication token, for security reasons, we recommend that you put the token in the `Authorization:Bearer` header. For example:
    
    
    curl -H "Authorization: Bearer <var>TOKEN</var>" "<var>ENDPOINTS_HOST</var>/echo"
    

Here, replace the ENDPOINTS_HOST and TOKEN variables with your API hostname and authentication token, respectively. See [Making an authenticated request to an Endpoints API](https://docs.cloud.google.com/endpoints/docs/openapi/service-account-authentication#making_an_authenticated_request). for sample code that sends a request using the `Authorization:Bearer` header.

If you cannot use the header when sending the request, you can put the authentication token in a query parameter called `access_token`. For example:
    
    
    curl "<var>ENDPOINTS_HOST</var>/echo?access_token=<var>TOKEN</var>"
    

## Receiving authenticated results in your API

ESP usually forwards all headers it receives. However, it overrides the original `Authorization` header when the backend address is specified by `x-google-backend` in OpenAPI specification or `BackendRule` in gRPC service configuration. 

ESP will send the authentication result in the `X-Endpoint-API-UserInfo` to the backend API. We recommend using this header instead of the original `Authorization` header. This header is a string that `base64url` encodes a JSON object. The JSON object format differs between ESPv2 and ESP. For ESPv2, the JSON object is exactly the original JWT payload. For ESP, the JSON object uses different field names and put original JWT payload under `claims` field. See [Handle JWTs in the backend service](https://docs.cloud.google.com/endpoints/docs/openapi/migrate-to-esp-v2#handle-jwt) for more information on the format.

## What's next

  * [Troubleshooting JWT validation](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-jwt)
  * [Authentication between services](https://docs.cloud.google.com/endpoints/docs/openapi/service-account-authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
