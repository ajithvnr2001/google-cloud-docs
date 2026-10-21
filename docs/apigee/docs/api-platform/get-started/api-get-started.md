---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started/
title: Getting started using the Apigee API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:00.527222+00:00
---

# Getting started using the Apigee API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Getting started using the Apigee API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee API can be used to programmatically develop and manage APIs with a set of RESTful operations.

You can use the Apigee API to integrate API proxy management into your organization's software development lifecycle (SDLC). A common usage of the Apigee API is to write scripts or code that deploy API proxies or that migrate API proxies from one environment to another, as part of a larger automated process that also deploys or migrates other applications.

For more information, see [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

**Important usage note for data residency:** To support data residency, when provisioning or using Apigee you must use a regional endpoint. For more information, see [Use regional endpoints for data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint). 

## Enabling the Apigee API

Ensure that you have enabled the Apigee API. The simplest way to enable an API for your project is to use the Apigee UI. For complete details, see [Step 1: Enable required APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis). 

## Obtaining an OAuth 2.0 access token

The Apigee API supports OAuth 2.0 for user authentication. With OAuth 2.0, you exchange your Google Cloud credentials for an access token that you can then use to make secure calls to the Apigee API. Once you obtain a token, you do not need to exchange your credentials again until the token expires.

**Note:** Short-lived service account credentials are useful for scenarios where you need to grant limited access to resources for trusted service accounts, and they reduce the risk compared to using long-lived credentials like service account keys. For more information, see [Generating an OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth).

###  Get a token using Google Cloud credentials 

To get a token using your Google Cloud credentials: 

  1. Authorize [gcloud](https://docs.cloud.google.com/sdk/docs) to access the Cloud Platform with your Google user credentials: 
         
         gcloud auth login

  2. Get a token for the currently active account: 
         
         export TOKEN=$(gcloud auth print-access-token)

  3. When you call an Apigee API, pass the access token in the Authorization header. For example: 
         
         curl "https://apigee.googleapis.com/v1/organizations" -H "Authorization: Bearer $TOKEN"




###  Get a token using a Google Cloud service account key 

To get a token using a service account key for authorization: 

  1. Generate a key for your service account using the Google Cloud console, as described in [Creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). 

A JSON file that contains your service account credentials is downloaded to your computer.

  2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path where the service account key is located:
         
         export GOOGLE_APPLICATION_CREDENTIALS=your_sa_credentials_file.json

  3. When you call an Apigee API, use the Google Cloud CLI to add an access token to the Authorization header. For example: 
         
         curl "https://apigee.googleapis.com/v1/organizations" -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"




## Setting environment variables for Apigee API requests

The Apigee API and gcloud CLI examples provided throughout the documentation use one or more of the environment variables defined in the following table.

By setting the environment variables upfront to meaningful values in your environment, you can copy and paste the example requests to execute them in your own environment with minimal or no modifications. 

Environment variable | Description  
---|---  
`$API` | Name of your API proxy.  
`$APIPRODUCT` | Name of the API product.  
`$APP` | ID of an app.  
`$DEVELOPER_EMAIL` | Email address of the developer.  
`$ENV` | Name of your environment, such as `test` or `prod`.  
`$ID` | Resource ID.  
`$KEY` | Consumer key.  
`$NAME` | Name of your resource.  
`$ORG` | Your Apigee organization.  
`$REV` | Revision number of your API proxy.  
`$SHAREDFLOW` | Name of your shared flow.  
`$TYPE` | [Resource type](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes).  
  
## Using curl

The examples within this section use [`curl`](https://curl.haxx.se/) to demonstrate how to develop applications using the Apigee API. `curl` is an open source, command-line tool for transferring data with URL syntax, supporting common protocols such as HTTP and HTTPS.

The following table summarizes the curl command-line options used in the examples.

Option | Description  
---|---  
`-d '{}' --data @filename  
--data-binary @filename` | Defines the request body, which you can pass directly or by specifying a filename.  
`-F file=@filename  
--form file=@filename` | Defines form-based data that you can pass by specifying a filename.  
`-H  
--header` | Defines a request header. You must pass the following information in the request header: 

  * `Authorization` header: OAuth 2.0 token for user authentication, as described in Obtaining an OAuth 2.0 access token.
  * `Content-Type` header: Content type of the request body being sent when creating or updating a resource (POST, PATCH, PUT) using the API.

  
`-X` | Specifies the type of request (GET, POST, and so on).  
  
For example:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/$ORG/apis" \
       -X GET \
       -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
