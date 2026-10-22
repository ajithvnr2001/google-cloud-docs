---
url: https://docs.cloud.google.com/api-gateway/docs/authenticating-users-jwt/
title: Using JWT to authenticate users \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:04.208879+00:00
---

# Using JWT to authenticate users  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/authenticating-users-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using JWT to authenticate users

This page describes how to support user authentication in API Gateway.

To authenticate a user, a client application must send a [JSON Web Token (JWT)](https://jwt.io/) in the authorization header of the HTTP request to your backend API. API Gateway validates the token on behalf of your API, so you don't have to add any code in your API to process the authentication. However, you do need to configure the API config for your gateway to support your chosen authentication methods.

API Gateway validates a JWT in a performant way by using the JWT issuer's [JSON Web Key Set (JWKS)](https://tools.ietf.org/html/rfc7517). The location of the JWKS is specified in the gateway's API config. API Gateway caches the JWKS for five minutes and refreshes it every five minutes.

## Before you begin

  * Add authentication code to your client application, following the authentication provider's documentation.



  * When your client application sends an HTTP request, the authorization header in the request must contain the following JWT claims: 
    * `iss` (issuer)
    * `sub` (subject)
    * `aud` (audience)
    * `iat` (issued at)
    * `exp` (expiration time)



## Configure API Gateway to support client authentication

You must have a security section in your API config for API Gateway to validate the claims in the signed JWT. The schema used to define the security methods depends on the version of the OpenAPI spec you use.

To support JWT authentication:

### OpenAPI 2.0

  1. Add the following to your API config: 
         
         securityDefinitions:
           your_custom_auth_id:
             authorizationUrl: ""
             flow: "implicit"
             type: "oauth2"
             # The issuer value should be unique
             x-google-issuer: "ISSUER"
             x-google-jwks_uri: "URL_PUBLIC_KEY"
             # Optional.
             x-google-audiences: "CLIENT_ID"

Where:

     * ISSUER is the issuer of the token.
     * URL_PUBLIC_KEY is the URL to the public key.
     * CLIENT_ID is the client ID.
  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
           - your_custom_auth_id: []




### OpenAPI 3.x

  1. Add the following to your API config: 
         
         components:
           securitySchemes:
             SCHEME_NAME:
               type: oauth2
               flows:
                implicit:
                  authorizationUrl: ""
                  scopes: {}
               x-google-auth:
                 issuer: ISSUER
                 jwksUri: URL_PUBLIC_KEY
                 # Optional. Replace CLIENT_ID with your client ID(s) as a list of strings.
                 audiences:
                   - CLIENT_ID
                 jwtLocations:
                   - header: Authorization
                     valuePrefix: "Bearer "

Where:

     * ISSUER is the issuer of the token.
     * URL_PUBLIC_KEY is the URL to the public key.
     * CLLIENT_ID is a list of client IDs as strings.
  2. Add a security section at either the API level to apply to the entire API, or at the method level to apply to a specific method. 
         
         security:
           - SCHEME_NAME: []




You can define multiple security definitions in the API config, but each definition must have a different issuer. If you use security sections at both the API level and at the method level, the method-level settings override the API-level settings. 

The `x-google-audiences` field (OpenAPI 2.0) or `audiences` field (OpenAPI 3.x) is _not_ required. API Gateway accepts all JWTs with the backend service name in the form of `https://SERVICE_NAME` in the `aud` claim.

**Note** : API Gateway does not accept the following URI types in the `aud` claim: 

  * Internal addresses
  * IPv4 or IPv6 addresses



To allow additional client IDs to access the backend service, you can specify the allowed client IDs in the applicable `audiences` field. Multiple audiences are specified as comma-separated values in OpenAPI 2.0 and with a list in OpenAPI 3.x. by using comma-separated values. API Gateway then accepts the JWTs with any of the specified client IDs in the `aud` claim. 

The `x-google-jwks_uri` (OpenAPI 2.0) or `jwksUri` (OpenAPI 3.x) field _is_ required. API Gateway supports two asymmetric public key formats defined by this OpenAPI extension: 

  * [JWK set format](https://tools.ietf.org/html/rfc7517#section-5). For example: 

### OpenAPI 2.0
        
        x-google-jwks_uri: "https://YOUR_ACCOUNT_NAME.YOUR_AUTH_PROVIDER_URL/.well-known/jwks.json"
        

### OpenAPI 3.x
        
        jwksUri: "https://YOUR_ACCOUNT_NAME.YOUR_AUTH_PROVIDER_URL/.well-known/jwks.json"
        

  * [X509](https://tools.ietf.org/html/rfc5280). For example: 

### OpenAPI 2.0
        
        x-google-jwks_uri: "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com"
        

### OpenAPI 3.x
        
        jwksUri: "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com"
        

If you are using a symmetric key format, set the `x-google-jwks_uri` (OpenAPI 2.0) or `jwksUri` (OpenAPI 3.x) to the URI of a file that contains the base64url-encoded key string. 

**Note** : When API Gateway sends requests to the `x-google-jwks_uri` or `jwksUri`, the request will contain the `x-forwarded-proto` header.

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

    * ### Products and pricing

      * [ See all products ](https://cloud.google.com/products/)
      * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
      * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
      * [ Contact sales ](https://cloud.google.com/contact/)
    * ### Support

      * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
      * [ Support ](https://cloud.google.com/support-hub/)
      * [ Release Notes ](https://docs.cloud.google.com/release-notes)
      * [ System status ](https://status.cloud.google.com)
    * ### Resources

      * [ GitHub ](https://github.com/googlecloudPlatform/)
      * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
      * [ Code samples ](https://docs.cloud.google.com/docs/samples)
      * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
      * [ Training and Certification ](https://cloud.google.com/learn/training/)
      * [ Builders Hub ](https://me.developers.google.com/)
    * ### Engage

      * [ Blog ](https://cloud.google.com/blog/)
      * [ Events ](https://cloud.google.com/events/)
      * [ X (Twitter) ](https://x.com/googlecloud)
      * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
      * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)

[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)
    * [ Android ](https://developer.android.com/)
    * [ Chrome ](https://developer.chrome.com/)
    * [ Firebase ](https://firebase.google.com/)
    * [ Google AI ](https://ai.google.com/)
    * [ About Google ](https://about.google/)
    * [ Privacy ](https://policies.google.com/privacy)
    * [ Site terms ](https://policies.google.com/terms?hl=en)
    * [ Google Cloud terms ](https://cloud.google.com/product-terms)
    * Manage cookies 
    * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
    * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)
    * English
    * Deutsch
    * Español
    * Español – América Latina
    * Français
    * Indonesia
    * Italiano
    * Português
    * Português – Brasil
    * עברית
    * 中文 – 简体
    * 中文 – 繁體
    * 日本語
    * 한국어



