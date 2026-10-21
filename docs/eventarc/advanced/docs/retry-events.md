---
url: https://docs.cloud.google.com/eventarc/advanced/docs/retry-events/
title: Retry events \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:25.946857+00:00
---

# Retry events  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/retry-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Retry events Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

Configuring retry policies lets you automatically redeliver events after delivery failures. This helps ensure reliable message processing when event receivers experience temporary service disruptions.

An event can be rejected due to _transient errors_ , such as when an event receiver is temporarily unavailable, encounters an error while processing an event, or exhausts service resources. You can retry transient errors like this. In contrast, _persistent errors_ occur when an event fails to match the configured schema or when mediation fails before the message can be routed to its destination.

## Transient errors

Eventarc Advanced provides you with the capability to handle transient errors. These transient errors can be retried and include those with the following error codes:

  * HTTP `408 Request Timeout`
  * HTTP `409 Conflict`
  * HTTP `429 Too Many Requests`
  * HTTP `500 Internal Server Error`
  * HTTP `502 Bad Gateway`
  * HTTP `503 Service Unavailable`
  * HTTP `504 Gateway Time-out`



## Persistent errors

In contrast to transient errors, persistent errors include the following:

  * Errors that occur when the number of configured retries is exhausted
  * Errors that occur when an event fails before it can be routed to its destination
  * Errors that result in an error code that is considered non-retryable; for example, error codes other than those listed for transient errors



You can manually identify persistent errors and handle them appropriately.

## Retry transient errors

Eventarc Advanced uses an exponential backoff delay to handle errors that can be retried. The default retry policy starts with a one-second delay, and the delay is doubled after each failed attempt (up to a maximum of 60 seconds and five attempts).

You can change the default retry policy using the Google Cloud console or the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command.

Note that the default backoff factor of `2` can't be changed.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click the name of the pipeline.

  3. In the **Pipeline details** page, click **Edit**.

  4. On the **Edit pipeline** page, in the **Retry policy** section, modify the following fields:

     * **Max attempts** : the number of delivery attempts; default is `5` attempts. Can be any positive integer. If set to `1`, no retry policy is applied and only one attempt is made to deliver a message.
     * **Min delay (seconds)** : the initial delay in seconds; default is `1` second. Must be between `1` and `600`.
     * **Max delay (seconds)** : the maximum delay in seconds; default is `60` seconds. Must be between `1` and `600`.

You can configure a linear backoff by setting the minimum and maximum delays to the same value.

  5. Click **Save**.




###  gcloud 
    
    
    gcloud eventarc pipelines update PIPELINE_NAME \
        --min-retry-delay=MIN_DELAY \
        --max-retry-delay=MAX_DELAY \
        --max-retry-attempts=MAX_ATTEMPTS
    

Replace the following:

  * `PIPELINE_NAME`: the ID or fully qualified identifier of the pipeline.
  * `MIN_DELAY`: the initial delay in seconds; default is `1` second. Must be between `1` and `600`.
  * `MAX_DELAY`: the maximum delay in seconds; default is `60` seconds. Must be between `1` and `600`.
  * `MAX_ATTEMPTS`: the number of delivery attempts; default is `5` attempts. Can be any positive integer. If set to `1`, no retry policy is applied and only one attempt is made to deliver a message.



The following example configures a linear backoff by setting the minimum and maximum delays to the same value:
    
    
    gcloud eventarc pipelines update my-pipeline \
        --min-retry-delay=4 \
        --max-retry-delay=4 \
        --max-retry-attempts=5
    

## Archive messages to handle persistent errors

You can write messages to a BigQuery table as they are received. This lets you manually identify persistent errors and handle them appropriately.

The following provides an overview of the steps required to archive your event messages, identify persistent errors, and retry the affected events.

  1. [Create a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus). Configure the bus appropriately; for example, to [publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).
  2. [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic). This Pub/Sub topic will be the target destination for your pipeline.
  3. [Create a BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery) for the Pub/Sub topic. A BigQuery subscription is a type of export subscription that writes messages to an existing BigQuery table as they are received. Alternatively, you can create the table when you create the BigQuery subscription.
  4. [Create a pipeline and enrollment](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment) that routes every message received by the bus (using `--cel-match="true"`) to the Pub/Sub topic. Configure a retry policy for the pipeline.

For example, the following commands create a pipeline and an enrollment:
         
         gcloud eventarc pipelines create my-archive-pipeline \
             --destinations=pubsub_topic='my-archive-topic' \
             --min-retry-delay=1 \
             --max-retry-delay=20 \
             --max-retry-attempts=6 \
             --location=us-central1
         
         
         gcloud eventarc enrollments create my-archive-enrollment \
             --cel-match="true" \
             --destination-pipeline=my-archive-pipeline \
             --message-bus=my-message-bus \
             --message-bus-project=my-google-cloud-project \
             --location=us-central1
         

  5. [Route your pipeline logs](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to another BigQuery dataset.

You should now have two separate BigQuery datasets: one that stores every message received by your Eventarc Advanced bus and one that stores your pipeline logs.

  6. To identify messages that have failed, use a [query statement to join](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types) both BigQuery datasets on the `message_uid` field.

  7. After identifying any failed messages, you can publish them to your bus again using the [Eventarc Publishing API](https://docs.cloud.google.com/eventarc/docs/reference/publishing/rest). For example, you can [deploy a Cloud Run service or job](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) to read the messages from BigQuery and [publish them directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format) to the Eventarc Advanced bus.




## Make event handlers idempotent

Event handlers that can be retried should be idempotent, using the following general guidelines:

  * Many external APIs let you supply an idempotency key as a parameter. If you are using such an API, you should use the event source and ID as the idempotency key. (Producers must ensure that [source + id](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel#attributes) is unique for each distinct event.)
  * Additionally, you can use a CloudEvents attribute, `xgooglemessageuid`, to provide idempotency. The value of this attribute is the same as the `message_uid` field in Eventarc Advanced messages. It uniquely identifies the action of publishing an event. For example, if the same event is published twice to a bus, each event will have a different `xgooglemessageuid` value when sent to an event handler.
  * Idempotency works well with at-least-once delivery, because it makes it safe to retry. So a general best practice for writing reliable code is to combine idempotency with retries.
  * Make sure that your code is internally idempotent. For example: 
    * Make sure that mutations can happen more than once without changing the outcome.
    * Query database state in a transaction before mutating the state.
    * Make sure that all side effects are themselves idempotent.
  * Impose a transactional check outside your service, independent of the code. For example, persist state somewhere recording that a given event ID has already been processed.
  * Deal with duplicate calls out-of-band. For example, have a separate clean up process that cleans up after duplicate calls.



## What's next

  * [Troubleshoot issues](https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot)
  * [View audit logs](https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
