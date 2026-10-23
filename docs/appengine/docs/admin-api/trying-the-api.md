---
url: https://docs.cloud.google.com/appengine/docs/admin-api/trying-the-api/
title: Trying Out the Admin API \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:23.754628+00:00
---

# Trying Out the Admin API  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/trying-the-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Trying Out the Admin API Stay organized with collections  Save and categorize content based on your preferences. 

There are two options for trying out the Admin API, either the **OAuth 2.0 Playground** or the **APIs Explorer**.

## OAuth 2.0 Playground

Use the **OAuth 2.0 Playground** to preview an authentication flow, obtain access tokens, and also send HTTP requests. To use the OAuth 2.0 Playground:

  1. Open the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/#step1&scopes=https%3A//www.googleapis.com/auth/cloud-platform&url=https%3A//appengine.googleapis.com/v1/apps/%7BappsId%7D/services/default&content_type=application/json&http_method=GET&useDefaultOauthCred=unchecked&oauthEndpointSelect=Google&oauthAuthEndpointValue=https%3A//accounts.google.com/o/oauth2/v2/auth&oauthTokenEndpointValue=https%3A//oauth2.googleapis.com/token&includeCredentials=unchecked&accessTokenType=bearer&autoRefreshToken=unchecked&accessType=offline&forceAprovalPrompt=checked&response_type=code).
  2. In Step 1, the **https://www.googleapis.com/auth/cloud-platform** scope is pre-selected for you. Click **Authorize APIs** to start the authentication flow.
  3. Follow the "implicit authentication flow" by clicking **Allow** to authorize the Google OAuth 2.0 Playground access to your Google Cloud services.
  4. In Step 2, click **Exchange authorization code for tokens** to receive an access token.

**Note:** You can use these access tokens in HTTP requests that you want to run from the command line, as long as you do so prior to their expiration time. For example, use these access tokens to run cURL commands.
  5. In Step 3, the **Request URI** field is pre-populated with the example URI:
         
         https://appengine.googleapis.com/v1/apps/{appsId}/services/default
         

You must replace `{appsId}` with your Google Cloud Platform project ID and then click `Send the request` to view the details about the `default` service of your project.

Use this URI field to send HTTP requests against the resources that you specify in your project. For more information about specifying resources in request URIs, see [REST in the Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/rest-in-the-api).

**Tip:** You can also click **List possible operations** and then scroll to the **App Engine Admin API** section to view a list of HTTP request. If you select an operation, it will populate the **Request URI** field with a template URI, in which you must specify the IDs of your resources before sending the request.



## APIs Explorer

Use the **APIs Explorer** to view a list of all the Admin API methods, fields, and their descriptions. You can then click the items in the list to generate URIs and send HTTP requests against the resources that you specify.

**Tip:** You can also use the APIs Explorer widgets in each of the API methods, for example [ `apps.get`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/get#try-it).

To use the APIs Explorer:

  1. Open the [APIs Explorer](http://developers.google.com/apis-explorer/#p/appengine/v1/).
  2. Select the method that you want to try out.
  3. Specify the IDs of the resources in your project as well as any supported fields.
  4. Click **Execute** to send the HTTP request against your project and then view both the generated request URI and HTTP response.



## What's next

  * [Accessing the API](https://docs.cloud.google.com/appengine/docs/admin-api/accessing-the-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
