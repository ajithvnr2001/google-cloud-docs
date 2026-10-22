---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users/
title: Authenticating users \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:40.723124+00:00
---

# Authenticating users  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Authenticating users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add support in your API for user authentication from client applications using Cloud Endpoints Frameworks. Note that Android and JavaScript clients are currently supported.

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




## Authenticating with Firebase Auth

To support calls from clients that use Firebase Auth:

  1. If you haven't already done so, create a Firebase project. Firebase projects are Google Cloud console projects that use Firebase services. For more information, see [What is a Firebase project?](https://support.google.com/firebase/answer/6399760?hl=en) and the [Firebase documentation](https://firebase.google.com/docs/).

  2. Add the following to your [`@Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations) or method annotation:

     * Add an `authenticators` parameter to your annotation, set to the value `{EspAuthenticator.class}`.
     * Add an `issuers` parameter containing an `@ApiIssuer` set to Firebase.
     * Add an `issuerAudiences` parameter containing an `@ApiIssuerAudience` set to Firebase and your project ID.

For example:
    
    @Api(
        name = "YOUR_API_NAME",
        version = "VERSION_NUMBER",
        authenticators = {EspAuthenticator.class},
        issuers = {
            @ApiIssuer(
                name = "firebase",
                issuer = "https://securetoken.google.com/YOUR_PROJECT_ID",
                jwksUri = "https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com")
        },
        issuerAudiences = {
            @ApiIssuerAudience(name = "firebase", audiences = "YOUR_PROJECT_ID")
        })
    

     * Replace `YOUR_API_NAME` with the name of your API.
     * Replace `VERSION_NUMBER` with your API version, for example, `v1`.
     * Replace both instances of `YOUR_PROJECT_ID` with your Firebase project ID.
  3. In your API implementation code, import `Users`:
         
         import com.google.api.server.spi.auth.common.User;
         

  4. In each API method where you want to check for proper authentication, check for a valid `User` and throw an exception if there isn't one, as shown in this sample method definition:
         
         @ApiMethod(httpMethod = ApiMethod.HttpMethod.GET)
         public Email getUserEmail(User user) throws UnauthorizedException {
           if (user == null) {
             throw new UnauthorizedException("Invalid credentials");
           }
         
           Email response = new Email();
           response.setEmail(user.getEmail());
           return response;
         }
         

  5. [Redeploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy) whenever you add new clients.




### Adding Firebase authentication to a client

You can add Firebase authentication to your code as described in the [Firebase](https://firebase.google.com/docs/auth/) documentation. The client must have a Google Cloud project associated with it, and the project ID must be listed in the API's Firebase issuer configuration as shown in the preceding section.

## Authenticating with Auth0

To support calls from clients that use Auth0:

  1. Add the following to your [`@Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations) or method annotation:

     * Add an `authenticators` parameter to your annotation, set to the value `{EspAuthenticator.class}`.
     * Add an `issuers` parameter containing an `@ApiIssuer` set to Auth0.
     * Add an `issuerAudiences` parameter containing an `@ApiIssuerAudience` set to Auth0 and your Auth0 client ID.

For example:
    
    @Api(
        name = "YOUR_API_NAME",
        version = "VERSION_NUMBER",
        authenticators = {EspAuthenticator.class},
        issuers = {
            @ApiIssuer(
                name = "auth0",
                issuer = "https://YOUR_ACCOUNT_NAME.auth0.com/",
                jwksUri = "https://YOUR_ACCOUNT_NAME.auth0.com/.well-known/jwks.json")
         },
         issuerAudiences = {
             @ApiIssuerAudience(name = "auth0", audiences = "AUTH0_CLIENT_ID")
        })
    

     * Replace `YOUR_API_NAME` with the name of your API.
     * Replace `VERSION_NUMBER` with your API version, for example, `v1`.
     * Replace `YOUR_ACCOUNT_NAME` with the Auth0 account name used for the client.
     * Replace `AUTH0_CLIENT_ID` with the ID you want to use for your client.
  2. In your API implementation code, import `Users`:
         
         import com.google.api.server.spi.auth.common.User;
         

  3. In each API method where you want to check for proper authentication, check for a valid `User` and throw an exception if there isn't one, as shown in this sample method definition:
         
         @ApiMethod(httpMethod = ApiMethod.HttpMethod.GET)
         public Email getUserEmail(User user) throws UnauthorizedException {
           if (user == null) {
             throw new UnauthorizedException("Invalid credentials");
           }
         
           Email response = new Email();
           response.setEmail(user.getEmail());
           return response;
         }
         

  4. [Redeploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy) whenever you add new clients.




### Adding Auth0 authentication to a client

You can add Auth0 authentication to your code as described in the [Auth0](http://auth0.com) documentation. The client must be listed in the API's Auth0 issuer configuration.

## Authenticating with Google ID tokens

To support calls from clients that authenticate using Google ID tokens:

  1. Obtain an OAuth 2 client ID for each client application. The client application owner must generate the client ID from the Google Cloud console. For instructions, see [Creating client IDs](https://docs.cloud.google.com/endpoints/docs/frameworks/java/creating-client-ids).

  2. Add a `clientIds` entry containing the client ID for each client app you are granting access to, and an `audiences` entry as well for each Android client, in your [`@Api` annotation](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations).

For example:
         
         @Api(
            name = "YOUR_API_NAME",
            version = "VERSION_NUMBER",
            clientIds = {"YOUR_CLIENT_ID"},
            audiences = {"YOUR_CLIENT_ID"}
         )
         

     * Replace `YOUR_API_NAME` with the name of your API.
     * Replace `VERSION_NUMBER` with your API version, for example, `v1`.
     * Replace `YOUR_CLIENT_ID` with the OAuth 2 client ID that was generated in the client application project.
  3. In your API implementation code, import `Users`:
         
         import com.google.api.server.spi.auth.common.User;
         

  4. In each API method where you want to check for proper authentication, check for a valid `User` and throw an exception if there isn't one, as shown in this sample method definition:
         
         @ApiMethod(httpMethod = ApiMethod.HttpMethod.GET)
         public Email getUserEmail(User user) throws UnauthorizedException {
           if (user == null) {
             throw new UnauthorizedException("Invalid credentials");
           }
         
           Email response = new Email();
           response.setEmail(user.getEmail());
           return response;
         }
         

  5. [Redeploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy) whenever you add new clients.




### Adding Google ID tokens authentication to a client

For information on adding authentication code to clients, see the following:

  * [Android app](https://docs.cloud.google.com/endpoints/docs/frameworks/java/calling-from-android)



## Sending a JWT in your client

If you use a JWT in your client to send authenticated requests to the API, the JWT must be in the authorization header of a HTTP request. The JWT should have the following required claims:

  * `iss`
  * `sub`
  * `aud`
  * `iat`
  * `exp`



## What's next

For background information about user authentication and how it differs from API key authorization, see [When and why to use API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/java/when-why-api-key).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
