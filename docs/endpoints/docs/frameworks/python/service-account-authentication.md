---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/service-account-authentication/
title: Authenticating with a service account \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:55.244112+00:00
---

# Authenticating with a service account  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/service-account-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Authenticating with a service account Stay organized with collections  Save and categorize content based on your preferences. 

## Prerequisites

This page assumes that you have already:

  * [Created a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  * [Added API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).




## Configuring authentication

To authenticate with a service account:

  1. Import the App Engine Endpoints API in your API class:
         
         import endpoints
         

  2. Add an issuer object for the service account to the [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi). For example:
         
         @endpoints.api(
             name='echo',
             version='v1',
             issuers={'serviceAccount': endpoints.Issuer(
                 'YOUR_SERVICE_ACCOUNT_EMAIL',
                 'https://www.googleapis.com/robot/v1/metadata/x509/YOUR_SERVICE_ACCOUNT_EMAIL')},
             audiences={'serviceAccount': ['YOUR_AUDIENCE']})
         

     * Replace `echo` with the name of your API.
     * Replace `v1` with your API version.
     * Replace `YOUR_SERVICE_ACCOUNT_EMAIL` with your service account email.
     * Replace `YOUR_AUDIENCE` with the value in the `aud` field sent by the calling service.
  3. In each API method where you want to check for proper authentication, check for a valid `User` and raise error `401`if there isn't one, as shown in this sample method definition:
         
         user = endpoints.get_current_user()
         # If there's no user defined, the request was unauthenticated, so we
         # raise 401 Unauthorized.
         

  4. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy). You need to redeploy the API whenever you add new clients.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
