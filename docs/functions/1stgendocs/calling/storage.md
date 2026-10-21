---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/storage/
title: Cloud Storage triggers (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:36.349804+00:00
---

# Cloud Storage triggers (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/storage/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Storage triggers (1st gen)

In Cloud Run functions, a Cloud Storage trigger enables a function to be called in response to changes in [Cloud Storage](https://docs.cloud.google.com/storage/docs). When you specify a Cloud Storage trigger for a function, you choose an event type and specify a Cloud Storage bucket. Your function will be called whenever a change occurs on an object (file) within the specified bucket.

**Note:** For a Cloud Run function to be triggered by an event on a Cloud Storage bucket, the function and the bucket must be in the same Google Cloud project.

The following Cloud Storage event types are supported:

Event | Event type | Description  
---|---|---  
_Object finalized_ | 

  * `google.storage.object.finalize`

| Occurs when a new object is created, or an existing object is overwritten and a new generation of that object is created.  
_Object deleted_ | 

  * `google.storage.object.delete`

| Occurs when an object is soft deleted. For more information, see [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).   
_Object archived_ | 

  * `google.storage.object.archive`

| Occurs when a live version of an object becomes a noncurrent version. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).  
_Object metadata updated_ | 

  * `google.storage.object.metadataUpdate`

| Occurs when the [metadata](https://docs.cloud.google.com/storage/docs/metadata) of an existing object changes.  
  
For a function to use a Cloud Storage trigger, it must be implemented as an [event-driven function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions):

  * If you use a [CloudEvent function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#cloudevent-functions), the Cloud Storage event data is passed to your function in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) and the CloudEvent data payload is of type [`StorageObjectData`](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/storage/v1/data.proto).

  * If you use a [background function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions), the Cloud Storage event data payload is passed directly to your function in the [`StorageObjectData`](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/storage/v1/data.proto) format.




The [Google Events](https://github.com/googleapis/google-cloudevents) repository contains additional resources for working with event data.

## Deployment

You can specify a Cloud Storage trigger when you deploy a function. See [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy) for general instructions on how to deploy a function, and see the following for additional information specific to configuring Cloud Storage triggers during deployment.

###  gcloud 

If you are [deploying using the gcloud CLI](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics), you can use the Cloud Storage _Object finalized_ event type with the following flags:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME \
    --no-gen2 \
    --trigger-bucket=YOUR_STORAGE_BUCKET \
    [--retry] \
    ...
    

  * The [`--trigger-bucket`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-bucket) flag specifies the Cloud Storage bucket that the trigger will monitor. _Object finalized_ events within this bucket will trigger calls to your function.
  * The [`--retry`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--retry) flag controls whether failed function calls are automatically retried. See [Retrying event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries) for more information.



To use event types other than _Object finalized_ , use the following flags:
    
    
      gcloud functions deploy YOUR_FUNCTION_NAME   
    
      --no-gen2   
    
      --trigger-event=EVENT_TYPE   
    
      --trigger-resource=YOUR_STORAGE_BUCKET   
    
      ...
      

###  Console 

If you are [deploying using the Google Cloud console](https://docs.cloud.google.com/functions/1stgendocs/deploy#console), you can configure a Cloud Storage trigger in the **Trigger** section:

  1. In the **Trigger type** field, select **Cloud Storage**.
  2. In the **Event type** field, select an event type.
  3. In the **Bucket** field, click **Browse** to select a Cloud Storage bucket for the trigger to monitor. Changes to objects within this bucket will trigger calls to your function.
  4. Select or deselect the **Retry on failure** checkbox to control whether failed function calls are automatically retried. See [Retrying event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries) for more information.



## Event delivery

Cloud Storage triggers are implemented with [Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications). Events are subject to [Pub/Sub notification delivery guarantees](https://docs.cloud.google.com/storage/docs/pubsub-notifications#delivery_guarantees).

A Cloud Storage bucket can have up to 10 notification configurations set to trigger for a specific event. Exceeding the bucket's notifications limits will cause further function deployments to fail with an error like the following:
    
    
    Cloud Storage bucket ...: Pub/Sub notification limit reached
    

You can work around this limitation by [managing your own Pub/Sub topic](https://docs.cloud.google.com/storage/docs/reporting-changes) and registering it for Cloud Storage notifications of the type you want your function to respond to. For example, you could configure a single notification for your chosen event (such as object creation) to a Pub/Sub topic. Then, have as many function subscribers as needed to the topic process the event and fan it out to multiple destinations. For example:

  1. [Create your own Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic).
  2. Create a single [notification configuration](https://docs.cloud.google.com/storage/docs/reporting-changes) on your Cloud Storage bucket that triggers on a specific event (such as `OBJECT_FINALIZE` for object creation) and sends the event to your single Pub/Sub topic.
  3. Create a function (or functions) triggered by your [Pub/Sub topic](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub).



See Cloud Storage [Quotas and limits](https://docs.cloud.google.com/storage/quotas) to learn more about Cloud Storage limitations.

## Next steps

  * Learn how to [write event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions).
  * Learn how to [deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy).
  * See the [Cloud Storage function tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen) for an example of writing, deploying, and calling a function with a Cloud Storage trigger.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
