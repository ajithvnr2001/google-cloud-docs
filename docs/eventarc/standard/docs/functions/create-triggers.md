---
url: https://docs.cloud.google.com/eventarc/standard/docs/functions/create-triggers/
title: Create a trigger for Cloud Run functions \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:33.621391+00:00
---

# Create a trigger for Cloud Run functions  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/functions/create-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Create a trigger for Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

You can create an Eventarc trigger that lets a supported event trigger a Cloud Run function. You must configure a trigger when you create or deploy a function using the Google Cloud CLI or the Google Cloud console.

You can also trigger Cloud Run functions in response to custom events published to an Eventarc channel.

## Create an Eventarc trigger

Create an Eventarc trigger so that your Cloud Run functions service receives notifications of a specific event or set of events. By specifying filters for the trigger, you can configure the routing of the event, including the event type and source. For more information on how to configure an Eventarc trigger for Cloud Run functions, see [Create triggers with Eventarc](https://docs.cloud.google.com/functions/docs/calling/eventarc).

The following event types trigger requests to your service:

  * [An audit log is created](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs) that matches the trigger's filter criteria
  * [A direct event occurs](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source) such as an update to a Cloud Storage bucket or an update to a Firebase Remote Config template
  * [A message is published to a Pub/Sub topic](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-pubsub)



## Trigger functions with custom events

You can trigger Cloud Run functions in response to custom events. These are events produced by special or additional event providers, as opposed to the built-in Firebase events supported by the Firebase SDK for Cloud Run functions, and that are published to an Eventarc channel. For more information, see [Create and handle custom event triggers](https://firebase.google.com/docs/functions/custom-events).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
