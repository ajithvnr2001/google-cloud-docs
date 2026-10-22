---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users/
title: Authenticating users \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:34.346080+00:00
---

# Authenticating users  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Authenticating users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add support in your API for user authentication from client applications by using Cloud Endpoints Frameworks. Note that Android and JavaScript clients are currently supported.

Endpoints Frameworks supports user authentication from client applications that use any of the following methodologies:

  * [Firebase Auth](https://firebase.google.com/docs/auth/)
  * [Auth0](http://auth0.com)
  * [Google ID tokens](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#google_id_token)



No matter which authentication method you use, in each API method where you want to check for proper authentication, you must check for a valid `User` as described in the following sections:

  * Authenticating with Firebase Auth
  * Authenticating with Auth0
  * Authenticating with Google ID tokens



## Prerequisites

This page assumes that you have already:

  * Created a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  * [Added API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).

  * If you use JWT in your client to send authenticated requests to the API, the JWT must be in the authorization header of a HTTP request. The JWT should have the following required claims: 
    * `iss`
    * `sub`
    * `aud`
    * `iat`
    * `exp`




## Authenticating with Firebase Auth

To support calls from clients that use Firebase Auth:

  1. Import the App Engine Cloud Endpoints API in your API class:
         
         import endpoints
         

  2. Add a Firebase issuer object for each client to the [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi). For example:
         
         @endpoints.api(
             name='YOUR_API_NAME',
             version='VERSION_NUMBER',
             issuers={'firebase': endpoints.Issuer(
                 'https://securetoken.google.com/YOUR_PROJECT_ID,
                 'https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com')})
         

     * Replace `YOUR_API_NAME` with the name of your API.
     * Replace `VERSION_NUMBER` with your API version, for example, `v1`.
     * Replace code>YOUR_PROJECT_ID with the Google Cloud project ID of the client.
  3. In each API method where you want to check for proper authentication, check for a valid `User` and raise `error 401` if there isn't one, as shown in this sample method definition:
         
         user = endpoints.get_current_user()
         # If there's no user defined, the request was unauthenticated, so we
         # raise 401 Unauthorized.
         

  4. [Deploy the Endpoints API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy). You need to redeploy the Endpoints API whenever you add new clients.




### Adding Firebase authentication to a client

You can add Firebase authentication to your code as described in the [Firebase](https://firebase.google.com/docs/auth/) documentation. The client must have a Google Cloud project associated with it, and the project ID must be listed in the API's Firebase issuer configuration.

## Authenticating with Auth0

To support calls from clients that use Auth0:

  1. Import the App Engine Endpoints API in your API class:
         
         import endpoints
         

  2. Add an Auth0 issuer object for each client to the [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi). For example:
         
         @endpoints.api(
             name='YOUR_API_NAME',
             version='VERSION_NUMBER',
             issuers={'auth0': endpoints.Issuer(
                 'https://YOUR_ACCOUNT_NAME.auth0.com',
                 'https://YOUR_ACCOUNT_NAME.auth0.com/.well-known/jwks.json')})
         

     * Replace `YOUR_API_NAME` with the name of your API.
     * Replace `VERSION_NUMBER` with your API version, for example, `v1`.
     * Replace `YOUR_ACCOUNT_NAME` with the Auth0 account name used for the client.
  3. In each API method where you want to check for proper authentication, check for a valid `User` and raise `error 401` if there isn't one, as shown in this sample method definition:
         
         user = endpoints.get_current_user()
         # If there's no user defined, the request was unauthenticated, so we
         # raise 401 Unauthorized.
         

  4. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy). You need to redeploy the API whenever you add new clients.




### Adding Auth0 authentication to a client

You can add Auth0 authentication to your code as described in the [Auth0](http://auth0.com) documentation. The client must be listed in the API's Auth0 issuer configuration.

## Authenticating with Google ID tokens

To support calls from clients that authenticate using Google ID tokens:

  1. Obtain an OAuth 2 client ID for each client application. The client application owner must generate the client ID from the Google Cloud console. For instructions, see [Creating client IDs](https://docs.cloud.google.com/endpoints/docs/frameworks/python/creating-client-ids).

  2. Import the App Engine Endpoints API in your API class:
         
         import endpoints
         

  3. Specify all of the client IDs you want to grant access to your API in the `allowed_client_ids`, and also specify client IDs belonging to Android clients in the`audiences` field in the [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi). For example:
         
         @endpoints.api(
             name='YOUR_API_NAME',
             version='VERSION_NUMBER',
             allowed_client_ids=ALLOWED_CLIENT_IDS,
             audiences=[ANDROID_AUDIENCE])
         class AuthedGreetingApi(remote.Service):
             # ...
         

Replace `ALLOWED_CLIENT_IDS` with the list of OAuth 2 client IDs generated from each client's project, and replace `ANDROID_AUDIENCE` with the list of Android web client IDs. The web client ID is the client ID with `.apps.googleusercontent.com` appended, for example: `YOUR_CLIENT_ID.apps.googleusercontent.com`.

  4. In each API method where you want to check for proper authentication, check for a valid `User` and raise `error 401` if there isn't one, as shown in this sample method definition:
         
         user = endpoints.get_current_user()
         # If there's no user defined, the request was unauthenticated, so we
         # raise 401 Unauthorized.
         

  5. [Deploy the Endpoints API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy). You need to redeploy the Endpoints API whenever you add new clients.




### Adding Google ID token authentication to a client

For information on adding authentication code to clients, see the following:

  * [Android app](https://docs.cloud.google.com/endpoints/docs/frameworks/python/consume_android)
  * [Python client](https://docs.cloud.google.com/endpoints/docs/frameworks/python/access_from_python)



## What's next

For background information about user authentication and how it differs from API key authorization, see [When and why to use API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/python/when-why-api-key).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
