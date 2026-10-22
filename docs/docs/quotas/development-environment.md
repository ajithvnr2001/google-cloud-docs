---
url: https://docs.cloud.google.com/docs/quotas/development-environment/
title: Set up the Cloud Quotas API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:45.959226+00:00
---

# Set up the Cloud Quotas API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/development-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Set up the Cloud Quotas API Stay organized with collections  Save and categorize content based on your preferences. 

To use the Cloud Quotas API, you must first enable it for your Google Cloud project. This document describes how to enable the Cloud Quotas API.

## Enable the API

You can enable the Cloud Quotas API by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. Go to the Google Cloud console **API Library** page. 

[Go to API Library](https://console.cloud.google.com/project/_/apis/library/cloudquotas.googleapis.com)

  2. Select the Google Cloud project that you want to access the API.

  3. On the API Library page, enable **Cloud Quotas API**.

  4. Make sure that your user account has the required [IAM roles](https://docs.cloud.google.com/docs/quotas/permissions).




### gcloud

## Before you begin

Authenticate to the gcloud CLI before you use it to enable APIs. For more information about the authentication process, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate).

## Enable the API

  1. Run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command and specify the Cloud Quotas API:
         
         gcloud services enable cloudquotas.googleapis.com --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project that needs access to the Cloud Quotas API. You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

  2. To confirm that the Cloud Quotas API is enabled in your project, run the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command and filter for `cloudquotas.googleapis.com` by passing the output to a command such as `grep` or using a gcloud CLI [`filter`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
         
         gcloud services list --filter="cloudquotas.googleapis.com"
         




## What's next

  * About the [Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/api-overview)

  * Cloud Quotas API [reference](https://docs.cloud.google.com/docs/quotas/reference/rest)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
