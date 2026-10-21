---
url: https://docs.cloud.google.com/api-gateway/docs/authenticating-users-googleid/
title: Using Google ID tokens to authenticate users \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:06.009025+00:00
---

# Using Google ID tokens to authenticate users  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/authenticating-users-googleid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using Google ID tokens to authenticate users

This page describes how to support user authentication in API Gateway.

To authenticate a user, a client application must send a [JSON Web Token (JWT)](https://jwt.io/) in the authorization header of the HTTP request to your backend API. API Gateway validates the token on behalf of your API, so you don't have to add any code in your API to process the authentication. However, you do need to configure the API config for your gateway to support your chosen authentication methods.

API Gateway validates a JWT in a performant way by using the JWT issuer's [JSON Web Key Set (JWKS)](https://tools.ietf.org/html/rfc7517). The location of the JWKS is specified in the gateway's API config. API Gateway caches the JWKS for five minutes and refreshes it every five minutes.

## Before you begin

  * Add authentication code to your client application that allows users to authenticate by signing in with a Google Account. See [Authenticate users with Google Accounts](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts) for details.



  * When your client application sends an HTTP request, the authorization header in the request must contain the following JWT claims: 
    * `iss` (issuer)
    * `sub` (subject)
    * `aud` (audience)
    * `iat` (issued at)
    * `exp` (expiration time)



## Configure API Gateway to support client authentication

You must have a security section in your API config for API Gateway to validate the claims in the signed JWT. The schema used to define the security methods depends on the version of the OpenAPI spec you use.

To support authentication using a Google ID token:

### OpenAPI 2.0

  1. Add the following to your API config: 
         
         securityDefinitions:
           google_id_token:
             authorizationUrl: ""
             flow: "implicit"
             type: "oauth2"
             x-google-issuer: "https://accounts.google.com"
             x-google-jwks_uri: "https://www.googleapis.com/oauth2/v3/certs"
             # Optional. Replace CLIENT_ID with your client ID
             x-google-audiences: "CLIENT_ID"

  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
            -   google_id_token: []




### OpenAPI 3.x

  1. Add the following to your API config: 
         
         components:
           securitySchemes:
             google_id_token:
               type: oauth2
               flows:
                implicit:
                  authorizationUrl: ""
                  scopes: {}
               x-google-auth:
                 issuer: https://accounts.google.com
                 jwksUri: https://www.googleapis.com/oauth2/v3/certs
                 # Optional. Replace CLIENT_ID with your client ID(s) as a list of strings.
                 audiences:
                   - CLIENT_ID

  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
           - google_id_token: []




You can define multiple security definitions in the API config, but each definition must have a different issuer. If you use security sections at both the API level and at the method level, the method-level settings override the API-level settings. 

The `x-google-audiences` field (OpenAPI 2.0) or `audiences` field (OpenAPI 3.x) is _not_ required. API Gateway accepts all JWTs with the backend service name in the form of `https://SERVICE_NAME` in the `aud` claim.

**Note** : API Gateway does not accept the following URI types in the `aud` claim: 

  * Internal addresses
  * IPv4 or IPv6 addresses



To allow additional client IDs to access the backend service, you can specify the allowed client IDs in the applicable `audiences` field. Multiple audiences are specified as comma-separated values in OpenAPI 2.0 and with a list in OpenAPI 3.x. by using comma-separated values. API Gateway then accepts the JWTs with any of the specified client IDs in the `aud` claim. 

## Make an authenticated call to an API Gateway API

When you send a request using an authentication token, we recommend that you put the token in the `Authorization:Bearer` header. For example:
    
    
    curl -H "Authorization: Bearer TOKEN" "GATEWAY_URL/hello"

Here, GATEWAY_URL and TOKEN should be replaced with your deployed gateway URL and authentication token, respectively. See [Making an authenticated request to an API Gateway API](https://docs.cloud.google.com/api-gateway/docs/authenticate-service-account#making_an_authenticated_request) for sample code that sends a request using the `Authorization:Bearer` header.

If you can't use the header when sending the request, you can put the authentication token in a query parameter called `access_token`. For example: 
    
    
    curl "GATEWAY_URL/hello?access_token=TOKEN"

## Receive authenticated results in your API

API Gateway usually forwards all headers it receives. However, it overrides the original `Authorization` header when the backend address is specified by `x-google-backend` in the API config. 

API Gateway will send the authentication result in the `X-Apigateway-Api-Userinfo` to the backend API. It is recommended to use this header instead of the original `Authorization` header. This header is `base64url` encoded and contains the JWT payload. 

## What's next

  * [Authentication between services](https://docs.cloud.google.com/api-gateway/docs/authenticate-service-account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
