---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub/
title: Pub/Sub triggers (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:35.479254+00:00
---

# Pub/Sub triggers (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Pub/Sub triggers (1st gen)

In Cloud Run functions, a Pub/Sub trigger enables a function to be called in response to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) messages. When you specify a Pub/Sub trigger for a function, you also specify a Pub/Sub topic. Your function will be called whenever a message is published to the specified topic.

For a function to use a Pub/Sub trigger, it must be implemented as an [event-driven function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions):

  * If you use a [CloudEvent function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#cloudevent-functions), the Pub/Sub event data is passed to your function in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) and the CloudEvent data payload is of type [`MessagePublishedData`](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/pubsub/v1/data.proto).

  * If you use a [background function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions), the Pub/Sub event data payload is passed directly to your function in the [`PubsubMessage`](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/pubsub/v1/data.proto) format.




The [Google Events](https://github.com/googleapis/google-cloudevents) repository contains additional resources for working with event data.

## Deployment

You can specify a Pub/Sub trigger when you deploy a function. See [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy) for general instructions on how to deploy a function, and see this section for additional information specific to configuring Pub/Sub triggers during deployment.

###  gcloud 

If you are [deploying using the gcloud CLI](https://docs.cloud.google.com/functions/1stgendocs/deploy#gcloud), the flags shown here are used to configure Pub/Sub triggers:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME \
    --no-gen2 \
    --trigger-topic=YOUR_PUBSUB_TOPIC \
    [--retry] \
    ...
    

  * The [`--trigger-topic`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-topic) flag specifies the Pub/Sub topic that the trigger will monitor. Messages published to this topic trigger calls to your function.
  * The [`--retry`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--retry) flag controls whether failed function calls are automatically retried. See [Retrying event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries) for more information.



**Legacy Pub/Sub events**

Legacy functions in Cloud Run functions (1st gen) use a different event type for Pub/Sub triggers:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME \
    --no-gen2 \
    --trigger-event=providers/cloud.pubsub/eventTypes/topic.publish \
    --trigger-resource=YOUR_PUBSUB_TOPIC \
    ...
    

This event type is supported for legacy functions already consuming these events. However, we recommend using the `--trigger-topic` flag instead, as the legacy event type might be removed at a future date.

###  Console 

If you are [deploying using the Google Cloud console](https://docs.cloud.google.com/functions/1stgendocs/deploy#console), you can configure a Pub/Sub trigger in the **Trigger** section:

  1. In the **Trigger type** field, select **Cloud Pub/Sub**.
  2. In the **Select a Cloud Pub/Sub topic** field, select a topic for the trigger to monitor, or select **Create a topic** to open a window to create a new topic. When a message is published to your function's topic, that triggers a call to your function.
  3. Select or clear the **Retry on failure** checkbox to control whether failed function calls are automatically retried. See [Retrying event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries) for more information.



## Next steps

  * Learn how to [write event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions).
  * Learn how to [deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy).
  * See the [Pub/Sub tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen) for an example of writing, deploying, and calling a function with a Pub/Sub trigger.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
