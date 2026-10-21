---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/
title: Cloud Run functions triggers (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.928766+00:00
---

# Cloud Run functions triggers (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Run functions triggers (1st gen)

You can set up Cloud Run functions to execute in response to various scenarios by specifying a _trigger_ for your function. Triggers can be HTTP(S) requests or one of a number of supported events. This page provides an overview of the triggers supported by Cloud Run functions.

Broadly, triggers fall into two categories:

  * **HTTP triggers** , which react to HTTP(S) requests, and correspond to [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions).

  * **Event triggers** , which react to events within your Google Cloud project, and correspond to [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions).




You specify triggers as part of [function deployment](https://docs.cloud.google.com/functions/1stgendocs/deploy). You cannot bind the same function to more than one trigger at a time, but you can have the same event cause multiple functions to execute by deploying multiple functions with the same trigger settings.

**Note:** Trigger binding does not happen instantaneously. It may take several minutes for a deployed function to start triggering on incoming events.

## Supported triggers

Cloud Run functions supports the following types of triggers:

  * [HTTP triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/http)
  * Event triggers: 
    * [Pub/Sub triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub)
    * [Cloud Storage triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/storage)
    * [Firestore triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/cloud-firestore-1st-gen)
    * [Google Analytics for Firebase triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/google-analytics-firebase)
    * [Firebase Realtime Database triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/realtime-database)
    * [Firebase Authentication triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/firebase-auth)
    * [Firebase Remote Config triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/firebase-remote-config)



## Additional triggers via Pub/Sub and webhooks

Because Cloud Run functions can be triggered by messages on a Pub/Sub topic, you can integrate Cloud Run functions with any other Google service that supports Pub/Sub as an event bus. In addition, by using HTTP triggers you can also integrate with any service that provides HTTP callbacks (webhooks). The following sections describe some example integrations.

### Cloud Logging

Cloud Logging can route logs to a Pub/Sub topic, where they can then be consumed by Cloud Run functions. See [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in the Cloud Logging documentation for more information.

### Cloud Scheduler

Cloud Scheduler jobs can send messages to a Pub/Sub topic, where they can then be consumed by Cloud Run functions. See the Cloud Scheduler tutorial [Using Pub/Sub to trigger a Cloud Run function](https://docs.cloud.google.com/scheduler/docs/tut-gcf-pub-sub) for more information.

### Cloud Tasks

Cloud Tasks HTTP Target tasks enable you to run task handlers at any HTTP endpoint, so a Cloud Run function with an HTTP trigger can be used as a task handler. You can also use tasks to throttle or rate-limit function invocations. See [Create HTTP Target tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) in the Cloud Tasks documentation for more information.

### Gmail

Using the Gmail [Push Notification API](https://developers.google.com/gmail/api/guides/push), you can send Gmail events to a Pub/Sub topic and consume them with Cloud Run functions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
