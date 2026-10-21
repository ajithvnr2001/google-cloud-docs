---
url: https://docs.cloud.google.com/functions/docs/tutorials/ocr/
title: Cloud Run function triggers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:25.487355+00:00
---

# Cloud Run function triggers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/tutorials/ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Cloud Run function triggers Stay organized with collections  Save and categorize content based on your preferences. 

After you [create and deploy your Cloud Run function](https://docs.cloud.google.com/run/docs/deploy-functions), you can set your function to execute in response to various scenarios by specifying a trigger. This page provides an overview of the triggers supported by Cloud Run functions.

## Types of triggers

By default, all functions deployed on Cloud Run are [Cloud Run source-deployed services](https://docs.cloud.google.com/run/docs/resource-model#source) that have an HTTP endpoint (`run.app` URL). If you previously created a function with the [`gcloud functions` command](https://docs.cloud.google.com/functions/docs/deploy) or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis), by default, the function has a `cloudfunctions.net` HTTP endpoint.

How your function is invoked or triggered depends on the type of function you specify when [writing your code](https://docs.cloud.google.com/run/docs/write-functions#signature_type).

  * **Event-driven triggers** : Reacts to events within your Google Cloud project and corresponds to [event-driven functions](https://docs.cloud.google.com/run/docs/write-functions#write-event-driven-functions) (also called _CloudEvent functions_). You must use Eventarc, Google's implementation of the CloudEvents spec that supports building event-driven architectures, to trigger functions in response to specified events.
  * **HTTP triggers** : Reacts to HTTP(S) requests and correspond to [HTTP functions](https://docs.cloud.google.com/run/docs/write-functions#write-http-functions). You can use other Google Cloud services (non-Eventarc) as an event provider to invoke the function through HTTP(S) requests.



To trigger a function to react to events within your Google Cloud project, you specify triggers as part of deploying the function in the Google Cloud console or after function is deployed when using the gcloud CLI.

You cannot bind the same function to more than one trigger at a time, but you can have the same event cause multiple functions to execute by deploying multiple functions with the same trigger settings.

**Note:** Trigger binding does not happen instantaneously. It may take several minutes for a deployed function to start triggering on incoming events.

## Example triggers

The following are example triggers supported by Cloud Run functions:

  * Event-driven triggers:

    * [Pub/Sub events triggered by Eventarc](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers)
    * [Cloud Storage events triggered by Eventarc](https://docs.cloud.google.com/run/docs/triggering/storage-triggers)
    * [Firestore events triggered by Eventarc](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers)
    * [Other event triggers](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events)
      * Supports any [event type supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events), including 90+ event sources using Cloud Audit Logs
  * HTTP triggers:

    * [Invoke with an HTTP request](https://docs.cloud.google.com/run/docs/triggering/https-request)
    * [Invoke services as part of a workflow with Workflows](https://docs.cloud.google.com/run/docs/triggering/invoke-services-from-workflows)
    * [Invoke services on a schedule with Cloud Scheduler](https://docs.cloud.google.com/run/docs/triggering/using-scheduler)
    * [Use Cloud Tasks to execute asynchronous tasks](https://docs.cloud.google.com/run/docs/triggering/using-tasks)
    * [Trigger services from a Pub/Sub push subscription](https://docs.cloud.google.com/run/docs/tutorials/pubsub)
      * Pub/Sub messages can be routed directly to a function through HTTP requests or wrapped under Eventarc as an event-driven trigger.



All event-driven functions use Eventarc for event delivery. Pub/Sub triggers and Cloud Storage triggers are implemented as particular types of Eventarc triggers.

**Note:** Eventarc does not support direct events from Google Analytics for Firebase, or Firebase Authentication.

## Additional triggers using Pub/Sub and webhooks

Because Cloud Run functions can be triggered by messages on a Pub/Sub topic, you can integrate Cloud Run functions with any other Google service that supports Pub/Sub as an event bus. In addition, by using HTTP triggers you can also integrate with any service that provides HTTP callbacks (webhooks). The following sections describe some example integrations.

### Cloud Logging

Cloud Logging can route logs to a Pub/Sub topic, where they can then be consumed by Cloud Run functions. See [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in the Cloud Logging documentation for more information.

### Cloud Scheduler

You can schedule an HTTP function by creating a Cloud Scheduler job that triggers an action using HTTP.

You can also schedule an event-driven function when your function should be triggered directly in response to events within your Google Cloud project; for example, when a message is published to a Pub/Sub topic.

### Cloud Tasks

Cloud Tasks HTTP Target tasks enable you to run task handlers at any HTTP endpoint, so an HTTP function with an HTTP trigger can be used as a task handler. You can also use tasks to throttle or rate-limit function invocations. See [Create HTTP Target tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) in the Cloud Tasks documentation for more information.

### Gmail

Using the Gmail [Push Notification API](https://developers.google.com/gmail/api/guides/push), you can send Gmail events to a Pub/Sub topic and consume them with Cloud Run.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
