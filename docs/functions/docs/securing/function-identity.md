---
url: https://docs.cloud.google.com/functions/docs/securing/function-identity/
title: Function Identity \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:38.404299+00:00
---

# Function Identity  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/function-identity/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Function Identity

This page provides supplemental information for configuring function identity for functions created using the [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest).

If you've created or deployed functions using Cloud Run, see [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) and [Configure service identity for services](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) for a detailed description of configuring service identity. Cloud Run refers to the function identity as the _service identity_. 

For an introduction to the function identity concept, see the Cloud Run [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) guide.

## Add a user-managed service account at deployment

When deploying a function using `gcloud functions deploy`, add the `--service-account` flag. For example:
    
    
    gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL

Replace `FUNCTION_NAME` with your function name, and `SERVICE_ACCOUNT_EMAIL` with the service account email.

## Update the service account of an existing function

You can update the runtime service account of an existing function.

When deploying a function using `gcloud functions deploy`, add the `--service-account` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL

Replace `FUNCTION_NAME` with your function name, and `SERVICE_ACCOUNT_EMAIL` with the service account.

The redeployed function now uses the new runtime service account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
