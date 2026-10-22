---
url: https://docs.cloud.google.com/endpoints/docs/grpc/authentication-method/
title: Choosing an Authentication Method \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:23.349728+00:00
---

# Choosing an Authentication Method  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/authentication-method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Choosing an Authentication Method Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

Cloud Endpoints supports multiple authentication methods that are suited to different applications and use cases. The [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) uses the authentication method that you specify in your service configuration to validate incoming requests before passing them to your API backend. This document provides an overview and sample use cases for each supported authentication method.

## API keys

An API key is an encrypted string that identifies a Google Cloud project for quota, billing, and monitoring purposes. A developer generates an API key in a project in the Google Cloud console and embeds that key in every call to your API as a query parameter.

If you specify an API key requirement in your service configuration, ESP uses the API key to look up the Google Cloud project that the API key is associated with. ESP rejects requests unless the API key was generated in your Google Cloud project or within other Google Cloud projects in which your API has been enabled. For more information, see [Restricting API access with API keys](https://docs.cloud.google.com/endpoints/docs/grpc/restricting-api-access-with-api-keys)

Unlike credentials that use short-live tokens or signed requests, API keys are a part of the request and are therefore considered to be vulnerable to [man-in-the-middle attacks](https://wikipedia.org/wiki/Man-in-the-middle_attack) and therefore less secure. You can use API keys in addition to one of the authentication methods described as follows. For security reasons, don't use API keys by themselves when API calls contain user data.

### Use case

If you want to use Endpoints features such as [quotas](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-overview), each request must pass in an API key so that Endpoints can identify the Google Cloud project that the client application is associated with.

For more information about API keys, see [Why and when to use API keys](https://docs.cloud.google.com/endpoints/docs/grpc/when-why-api-key).

## Firebase Authentication

[Firebase Authentication](https://firebase.google.com/docs/auth/) provides backend services, SDKs, and libraries to authenticate users to a mobile or web app. It authenticates users by using a variety of credentials such as Google, Facebook, Twitter, or GitHub.

The Firebase client library signs a [JSON Web Token (JWT)](https://jwt.io/) with a private key after the user successfully signs in. ESP validates that the JWT was signed by Firebase and that the `iss` (issuer) claim in the JWT, which identifies your Firebase application, matches the `issuer` setting in the service configuration.

### Use case

We recommend using Firebase when the API calls involve any user data and the API is intended to be used in flows where the user has a user interface for example, from mobile and web apps. For more information, see the Firebase tab in [Authenticating users](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users). 

## Auth0

[Auth0](https://auth0.com/) authenticates and authorizes applications and APIs regardless of identity provider, platform, stack and device.

Auth0 supports a large number of providers and the [Security Assertion Markup Language](https://wiki.oasis-open.org/security/FrontPage) specification. It provides backend services, SDKs, and user interface libraries for authenticating users in web and mobile apps. Auth0 integrates with several third-party identity providers and also provides custom user account management.

The client library provided by Auth0 generates and signs a JWT once the user signs in. ESP validates the JWT was signed by Auth0 and that the `iss` claim in the JWT, which identifies your Auth0 application, matches the `issuer` setting in the service configuration.

### Use case

Auth0 is suited for consumer and enterprise web and mobile apps. For more information, see the Auth0 tab in For more information, see the Auth0 tab [Authenticating users](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users). 

## Google ID token authentication

Authentication with a [Google ID token](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#google_id_token) allows users to authenticate by signing in with a Google Account. Once authenticated, the user has access to all Google services. You can use Google ID tokens to make calls to Google APIs and to APIs managed by Endpoints. ESP validates the Google ID token by using the public key and makes sure that the `iss` claim in the JWT is `https://accounts.google.com`.

### Use case

Authentication with a Google ID token is recommended when all users have Google Accounts. You might choose to use Google ID token authentication, for example, if your API accompanies a Google application, such as Google Drive companion. Google ID token authentication allows users to authenticate by signing in with a Google Account. Once authenticated, the user has access to all Google services. For more information, see the Google ID token tab in [Authenticating users](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users). 

## Service accounts

To identify a service that sends requests to your API, you use a [service account](https://docs.cloud.google.com/docs/authentication#service_accounts). The calling service uses the service account's private key to sign a secure [JSON Web Token (JWT)](https://jwt.io/) and sends the signed JWT in the request to your API.

### Use case

JWTs and service accounts are well suited for microservices. For more information, see [Authentication between services](https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication).

## Custom authentication

You can use other authentication platforms to authenticate users as long as it conforms to the JSON Web Token [RFC 7519](https://tools.ietf.org/html/rfc7519).

For more information, see the Custom tab in [Authenticating users](https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
