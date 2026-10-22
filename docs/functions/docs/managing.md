---
url: https://docs.cloud.google.com/functions/docs/managing/
title: Manage functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:45.316242+00:00
---

# Manage functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/managing/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage functions

This guide shows you how to manage and detach a function that was created with the `gcloud functions` command. To learn how to manage a function that was created with the `gcloud run` command, see [Manage Cloud Run services](https://docs.cloud.google.com/run/docs/managing/services).

**Note:** If you created a Cloud Run function using `gcloud run` commands or the Cloud Run Admin API, you can't manage that function with `gcloud functions` commands or the Cloud Functions v2 API.

Functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis) (for example, by using `gcloud functions`, the REST API, or Terraform) can be managed with the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/cloud-run-admin-api-overview) as well as the Cloud Functions v2 API. For example, you can update an existing function using either `gcloud functions` or `gcloud run` commands:

###  gcloud functions 
    
    
      gcloud functions deploy FUNCTION_NAME \
        --runtime=nodejs24 \
        --source= . \
        --entry-point=ENTRYPOINT
        --trigger-http
    

###  gcloud run 
    
    
    gcloud run deploy FUNCTION_NAME \
      --source= . \
      --function=ENTRYPOINT
      --base-image=google-22-full/nodejs24
    

## Detach

The [`gcloud functions detach`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/detach) command lets you detach a Cloud Functions v2 function from its existing API environment. After you detach a function, you can only manage it using the Cloud Run Admin API. You might want to do this if your workloads need to stay within the `run.googleapis.com` API boundary for [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview), or to ensure that your workloads use the [Cloud Run SKU](https://cloud.google.com/skus/sku-groups/cloud-run).

### Prepare your function for detach

When preparing to detach your function, consider the following:

  * The detach operation is not reversible.
  * The detach operation cannot be applied to Cloud Run functions (1st gen).
  * Familiarize yourself with how to [deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions) using the Google Cloud console, Google Cloud CLI, and Terraform.
  * HTTP functions will retain their assigned URLs.
  * Triggers attached to event-driven functions will be retained.
  * Triggers cannot be managed through the `run.googleapis.com` API directly. Be sure to familiarize yourself with the trigger management guides for [Eventarc](https://docs.cloud.google.com/eventarc/docs) or [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).
  * Disabling [retry on failure](https://docs.cloud.google.com/functions/docs/bestpractices/retries#event_driven_functions_created_with_v2_api) is not a supported feature on Cloud Run. 
    * During the detach operation, Cloud Run functions modifies the triggers attached to functions configured with [no retry on failure](https://docs.cloud.google.com/functions/docs/bestpractices/retries#event_driven_functions_created_with_v2_api), to ensure that the underlying Pub/Sub topic makes a maximum of five delivery attempts. When the detach operation is completed, a [dead letter queue](https://docs.cloud.google.com/pubsub/docs/handling-failures#how_dead_letter_topics_work) topic stores the undelivered messages, which you can retrieve by creating a new subscription to the dead letter queue. If you want to use a customer-managed encryption key for the DLQ topic, you can [update CMEK for the topic](https://docs.cloud.google.com/pubsub/docs/encryption#update_cmek_for_a_topic) after detach.
  * When a function is successfully detached, a new Cloud Run revision is created. Starting from that revision onwards, the function will be billed using the [Cloud Run SKU](https://cloud.google.com/skus/sku-groups/cloud-run).



### Detach your function

You can detach your function using the following command:
    
    
    gcloud functions detach FUNCTION_NAME
    

Replace FUNCTION_NAME with the name of your function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
