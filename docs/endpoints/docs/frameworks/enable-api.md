---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api/
title: Enabling an API in your Google Cloud project \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:17.016506+00:00
---

# Enabling an API in your Google Cloud project  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Enabling an API in your Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

When an API requires an API key and the API is associated with a Google Cloud project that you don't have access to, you have the following options to obtain an API key:

  * **Option 1** : Ask a security admin to create an API key for you.

  * **Option 2** : Ask a security admin to [grant you access to the project](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-access) so that you can create an API key in the same project that the API is associated with.

  * **Option 3** : Ask a security admin to [grant you access to enable the API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers) in your own Google Cloud project so that you can create an API key.




## Before you begin

[Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

## Enabling an API

If you used option 3 and asked someone to grant you access to enable the API, follow the steps below to enable the API in your own Google Cloud project.

To enable an API:

### Console

  1. In the Google Cloud console, go to APIs & services for your project. 

[Go to APIs & Services](https://console.cloud.google.com/apis)

  2. On the **Library** page, click **Private APIs**. If you don't see the API listed, that means you haven't been granted access to enable the API.
  3. Click the API you want to enable. If you need help finding the API, use the search field.
  4. In the page that displays information about the API, click **Enable**.



### gcloud

  1. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list
         

  2. Using the applicable project ID from the previous step, set the default project to the one in which you want to enable the API:
         
         gcloud config set project YOUR_PROJECT_ID
         

  3. Get a list of services that you can enable in your project:
         
         gcloud services list --available
         

If you don't see the API listed, that means you haven't been granted access to enable the API.

  4. Using the applicable service name from the previous step, enable the service:
         
         gcloud services enable SERVICE_NAME
         




For more information on the preceding commands, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
