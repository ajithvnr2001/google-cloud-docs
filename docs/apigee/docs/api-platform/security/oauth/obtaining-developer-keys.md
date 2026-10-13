---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/obtaining-developer-keys/
title: Obtaining client credentials \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:26.106573+00:00
---

# Obtaining client credentials  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/obtaining-developer-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Obtaining client credentials Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic discusses obtaining client credentials (also called developer keys) for use in the OAuth 2.0 authorization flow.

## What are client credentials?

To participate in any OAuth 2.0 authorization flow, all client apps must be registered with Apigee (the authorization server). When you register your app, you will be assigned two credentials: a Key and a Secret. The Key is a public key and Secret must never be made public. These credential keys allow Apigee to uniquely identify the client app.

**Note:** Terminology: The [IETF OAuth 2.0 specification](https://tools.ietf.org/html/draft-ietf-oauth-v2-31) refers to client credentials as the client identifier and client secret. The Apigee UI refers to them as the Credential Key and Secret. These terms are synonymous. 

##  Getting the key and secret from the Apigee UI 

See [ Viewing an API key and secret](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api#view-api-key).

## Getting the key and secret with Apigee APIs

Use an API to get the list of apps in your organization:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apps" \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

This call returns a list of apps by **app ID**.
    
    
    [ "da496fae-2a04-4a5c-b2d0-709278a6f9db", "50e3e831-175b-4a05-8fb6-05a54701af6e" ]

To retrieve an app's profile:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apps/**$APP** " \
       -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

For example:
    
    
    $ curl https://apigee.googleapis.com/v1/organizations/myorg/apps/da496fae-2a04-4a5c-b2d0-709278a6f9db \
      -H "Authorization: Bearer $TOKEN"
    

The API returns the profile of the app you specified. For example, an app profile for **weatherapp** has the following JSON representation:
    
    
    {
      "accessType" : "read",
      "apiProducts" : [ ],
      "appFamily" : "default",
      "appId" : "da496fae-2a04-4a5c-b2d0-70928a6f9db",
      "attributes" : [ ],
      "callbackUrl" : "http://weatherapp.com",
      "createdAt" : 1380290158713,
      "createdBy" : "noreply_admin@apigee.com",
      "credentials" : [ {
        "apiProducts" : [ {
          "apiproduct" : "PremiumWeatherAPI",
          "status" : "approved"
        } ],
        "attributes" : [ ],
        "consumerKey" : "bBGAQrXgivA9lKu7NMPyYpVKNhGar6K",
        "consumerSecret" : "hAr4Gn0gA9vyvI4",
        "expiresAt" : -1,
        "issuedAt" : 1380290161417,
        "scopes" : [ ],
        "status" : "approved"
      } ],
      "developerId" : "5w95xGkpnjzDBT4",
      "lastModifiedAt" : 1380290158713,
      "lastModifiedBy" : "noreply_admin@apigee.com",
      "name" : "weatherapp",
      "scopes" : [ ],
      "status" : "approved"
    }

Note the values for `consumerKey` and `consumerSecret`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
