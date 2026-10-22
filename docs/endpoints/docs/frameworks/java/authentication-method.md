---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/authentication-method/
title: Choosing an authentication method \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:40.879453+00:00
---

# Choosing an authentication method  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/authentication-method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Choosing an authentication method Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints Frameworks supports multiple authentication methods that are suited to different applications and use cases. Endpoints Frameworks uses the authentication method that you have specified in your annotation to validate incoming requests before passing them to your API backend. This document provides an overview and sample use cases for each supported authentication method.

## API keys

An API key is a simple encrypted string that identifies a Google Cloud project for quota, billing, and monitoring purposes. A developer generates an API key in a project in the Google Cloud console and embeds that key in every call to your API as a query parameter.

If you specify an API key requirement in your annotation, Endpoints Frameworks uses the API key to look up the Google Cloud project that the API key is associated with. Endpoints Frameworks rejects requests unless the API key was generated in your Google Cloud project or within other Google Cloud projects in which your API has been enabled. For more information, see [Restricting API access with API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks)

Unlike credentials that use short-lived tokens or signed requests and are sent in the request header, clients send an API key as a query parameter. Even though query parameters get encrypted in HTTPS, API keys aren't secure. For example, some servers might store the entire URL of each request in clear text in a server log. For security reasons, don't use API keys by themselves when API calls contain user data. You can use API keys in addition to one of the following authentication methods.

For best practices on securing and adding restrictions to API keys, see [Using API keys](https://docs.cloud.google.com/docs/authentication/api-keys#securing_an_api_key). Although "Using API keys" is targeted for clients using Google APIs, the best practices are applicable to APIs that you create using Endpoints Frameworks.

### Use case

If you want to use Endpoints features such as [quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview), each request must pass in an API key so that Endpoints can identify the Google Cloud project that the client application is associated with.

For more information about API keys, see [Why and when to use API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/java/when-why-api-key).

## Firebase authentication

[Firebase authentication](https://firebase.google.com/docs/auth/) provides backend services, SDKs, and libraries to authenticate users to a mobile or web app. It authenticates users using a variety of credentials such as Google, Facebook, Twitter, or GitHub.

The Firebase client library signs a [JSON Web Token (JWT)](https://jwt.io/) with a private key after the user has successfully signed in. Endpoints Frameworks validates that the JWT was signed by Firebase and that the "iss" (issuer) claim in the JWT, which identifies your Firebase application, matches the `issuer` setting in the annotation.

### Use case

Because Firebase authentication integrates tightly with other Firebase services, it is well-suited for mobile or web apps that use Firebase. See [Authenticating with Firebase Auth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users#authenticating_with_firebase_auth).

## Auth0

[Auth0](https://auth0.com/) authenticates and authorizes apps and APIs regardless of identity provider, platform, stack, and device.

Auth0 supports a large number of providers and the [Security Assertion Markup Language](https://wiki.oasis-open.org/security/FrontPage) specification. It provides backend services, SDKs, and user interface libraries for authenticating users in web and mobile apps. Auth0 integrates with several third-party identity providers and also provides custom user account management.

The client library provided by Auth0 generates and signs a JWT once the user has signed in. Endpoints Frameworks validates the JWT was signed by Auth0 and that the "iss" claim in the JWT, which identifies your Auth0 application, matches the `issuer` setting in the annotation.

### Use case

Auth0 is well-suited for consumer and enterprise web and mobile apps. For more information, see [Authenticating with Auth0](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users#authenticating_with_auth0).

## Google ID token authentication

Authentication using a [Google ID token](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#google_id_token) lets users authenticate by signing in with a Google Account. Once authenticated, the user has access to all Google services. You can use Google ID tokens to make calls to Google APIs and APIs that you have implemented using Endpoints Frameworks. Endpoints Frameworks validates the Google ID token using the public key and ensures that the "iss" claim in the JWT is `https://accounts.google.com` or `accounts.google.com`.

### Use case

Authentication using a Google ID token is recommended when all users have Google accounts. You might choose to use Google ID token authentication, for example, if your API accompanies Google Workspace Applications (for example, a Google Drive companion). Google ID token authentication lets users authenticate by signing in with a Google Account. Once authenticated, the user has access to all Google services.

For more information, see [Authenticating with Google ID tokens](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users#google-id-tokens).

## JWTs and service accounts

A [JSON Web Token](https://jwt.io/) (JWT) is commonly used to share claims or assertions between connected applications. A JWT representing a service account can be signed either by:

  * The service account.

  * Google's authorization service. (A JWT signed by Google's authorization service is referred to as a Google ID token.)




Authenticating a request using a JWT signed by a service account might be easier to implement, but if you have a large number of service accounts, or if you want to accept credentials from service accounts you don't own, using a Google ID token is recommended because you only need to allow `https://accounts.google.com` or `accounts.google.com` as an issuer for all service accounts.

### Use case

JWTs and service accounts are well-suited for microservices. For more information, see [Authenticating with a service account](https://docs.cloud.google.com/endpoints/docs/frameworks/java/service-account-authentication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
