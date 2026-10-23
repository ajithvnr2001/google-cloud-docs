---
url: https://docs.cloud.google.com/appengine/docs/admin-api/accessing-the-api/
title: Accessing the Admin API \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:47.467021+00:00
---

# Accessing the Admin API  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/accessing-the-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Accessing the Admin API Stay organized with collections  Save and categorize content based on your preferences. 

Before users or applications can use the App Engine Admin API, you as a Google Cloud project owner must first enable the API in your project and then create credentials that users or applications can use to authorize HTTP requests.

For example, an owner must first create an initial Google Cloud project and then create credentials in that project before anyone can send HTTP requests to the Admin API. After the owner sets up and configures the initial project, that project can then be used for administrative purposes to programmatically create and manage other resources, for example:

  * Creating other Google Cloud projects.
  * Creating App Engine applications for all newly created projects.
  * Deploying app versions to newly created App Engine applications.
  * Managing resources in all of the versions that you deployed.



## Before you begin

To complete the following task, you must be an owner of the Google Cloud project where you want to enable the Admin API for users and applications to access.

**Tip:** You can use both the OAuth 2.0 Playground and APIs Explorer to [try out the Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/trying-the-api) before you start configuring your project.

## Configuring your project and creating credentials

To configure your Google Cloud project and create credentials:

  1. Enable both the App Engine Admin API and Cloud Storage API in your Google Cloud project:

[Enable both APIs](https://console.cloud.google.com/apis/enableflow?apiid=appengine,storage_component)

  2. Create credentials that users and applications use to access the Admin API in your project.

To create credentials, review the [Google Cloud Platform Auth Guide](https://docs.cloud.google.com/docs/authentication) and then choose the OAuth 2.0 authorization flow that meets your app's requirements.

**Important:** This API requires that you request access to one of the following OAuth 2.0 scopes in your code: 
     * `https://www.googleapis.com/auth/appengine.admin`
     * `https://www.googleapis.com/auth/cloud-platform`
     * `https://www.googleapis.com/auth/cloud-platform.read-only`
The **Authorization** section on each method's reference page describes which OAuth scopes are required. Also see the list of methods, permissions, and related roles in [Controlling Access](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#permissions_and_roles) to help you determine which OAuth scope is adequate for your needs.



## Examples

To demonstrate an authentication flow, the examples below use the client-side OAuth 2.0 flow to obtain a token. The token is used to authorize requests to the Admin API using the cURL command-line tool to deploy the example app to the App Engine application of the project `[MY_PROJECT_ID]`.

### Authentication example

In this example, the client-side authorization flow known as the _implicit grant flow_ , requires the user to authorize the client application for access to the Admin API on behalf of the user. The access token that is returned is valid for approximately 60 minutes or generally while the user is active on your application.

**Tip:** For more information about the implicit grant flow and how the URL below is formed, see [using OAuth 2.0 for client-side web applications](https://developers.google.com/identity/protocols/OAuth2UserAgent#formingtheurl).

#### HTTP request

The following URL uses a client ID that was created in the Google Cloud console to request an access token and then redirect the user to an authorized URI where your app receives the token:
    
    
    https://accounts.google.com/o/oauth2/v2/auth?
      response_type=token&
      client_id=[MY_CLIENT_ID].apps.googleusercontent.com&
      scope=https://www.googleapis.com/auth/cloud-platform&
      redirect_uri=[MY_REDIRECT_URI]
    

Where:

  * `[MY_CLIENT_ID]` is a **Client ID** from one of your credentials in the [Google Cloud console](https://console.cloud.google.com/apis/credentials).
  * `[MY_REDIRECT_URI]` is the corresponding **Authorized redirect URIs** from the same credential in the [Google Cloud console](https://console.cloud.google.com/apis/credentials). If no redirect URI is specified, you must specify a trusted URI, for example `https://www.google.com`. The redirect URI defines where the HTTP response is sent. For production, you must specify your application's auth endpoint, which handles responses from the OAuth 2.0 server. For more information, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/OAuth2WebServer#creatingcred).



#### HTTP response

When the application uses the URL to request authorization, the access token is returned in a response, for example:
    
    
    https://www.google.com/#access_token=[MY_ACCESS_TOKEN]&
      token_type=Bearer&
      expires_in=3600
    

Where `[MY_ACCESS_TOKEN]` is the returned access token that you requested.

After you obtain an access token, you can use it to access the Admin API. For example, your application's auth endpoint can programmatically extract the access token from the response. See the following example for how to manually use your token in a cURL command.

### HTTP request example using cURL

The following cURL command demonstrates how you can use your `[MY_ACCESS_TOKEN]` access token to make an HTTP `POST` request. This cURL command deploys the resources defined in the `app.json` configuration file to the `v1` version of the `default` service in the application of project `MY_PROJECT_ID`.
    
    
    curl -X POST -T "app.json" -H "Content-Type: application/json" -H "Authorization: Bearer [MY_ACCESS_TOKEN]" https://appengine.googleapis.com/v1/apps/[MY_PROJECT_ID]/services/default/versions
    

## What's next

  * [Deploying Versions To Your Application](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
