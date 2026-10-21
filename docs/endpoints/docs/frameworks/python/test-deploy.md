---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy/
title: Deploying and testing an API \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:20.967992+00:00
---

# Deploying and testing an API  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Deploying and testing an API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy your API.

## Before you begin

  * [Set up your programming environment and download tools](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python#before-you-begin).
  * [Create your API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api).
  * [Create a web server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server) to serve your API.



## Deploying your API to production

To deploy an API:

  1. Set the `ENDPOINTS_GAE_SDK` environment variable to the path of your App Engine SDK folder: `Path_to_Cloud_SDK/platform/google_appengine`.

Replace `Path_to_Cloud_SDK` with the output of the following command:
         
         gcloud info --format="value(installation.sdk_root)"
         

  2. Run the following command in the API main directory:
         
         gcloud app deploy
         

Wait a few moments for the deployment to succeed, ignoring the warning messages. When the deployment completes, a message similar to the following displays:
         
         File upload done.
         Updating service [default]...done.
         

  3. Confirm successful deployment by sending a test request to the API, for example:
         
         curl --request POST \
            --header "Content-Type: application/json" \
            --data '{"content":"echo"}' \
            https://PROJECT_ID.appspot.com/_ah/api/echo/v1/echo?n=2
         

Replace `PROJECT_ID` with your project ID and `echo` with your API name.

The results are:
         
         {
          "content": "echo echo"
         }
         




If you didn't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/frameworks/troubleshoot-response-errors).

## Deploying to multiple app versions

For information on how to do API versioning, and how to deploy to versions, see [Handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/python/handling-api-versioning)

## Testing an API locally

You can use the App Engine local development server to test your API locally. For more information about the local development server, see [Using the local development server](https://docs.cloud.google.com/appengine/docs/standard/python/tools/using-local-server).

To run your API locally:

  1. From the root directory of the project, start the App Engine development server:
         
         dev_appserver.py YOUR_PROJECT_DIR
         

  2. Run `curl` to make an API request, for example:
         
         curl --request POST \
             --header "Content-Type: application/json" \
             --data '{"message":"echo"}' \
             "${HOST}/_ah/api/echo/v1/echo?n=2"
         




## Adding API management

Endpoints Frameworks provides API management features such as:

  * [Monitoring](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api)
  * [Logging](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api#logs)
  * [Quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview)
  * [Developer portal](https://docs.cloud.google.com/endpoints/docs/openapi/dev-portal-overview)



For your API to be managed by Endpoints Frameworks, you must generate and deploy an OpenAPI document that describes your API, as described in [Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
