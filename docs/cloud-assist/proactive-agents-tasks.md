---
url: https://docs.cloud.google.com/cloud-assist/proactive-agents-tasks/
title: Automate actions based on Proactive Agent results \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:27.577655+00:00
---

# Automate actions based on Proactive Agent results  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/proactive-agents-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Automate actions based on Proactive Agent results Stay organized with collections  Save and categorize content based on your preferences. 

You can use Eventarc to automatically monitor and respond to activity from Proactive Mode in Gemini Cloud Assist.

When an agent completes a background task—such as a root-cause investigation or a cost anomaly analysis—it publishes an event that you can route to a webhook, a script, or a workflow.

## Before you begin

  * Ensure you have [set up Proactive Mode](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup).
  * [Install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI if you haven't already done so.



## Create an automation trigger

Gemini Cloud Assist generates a `google.cloud.geminicloudassist.task.v1.completed` event whenever a background investigation or optimization task finishes.

You can route these events to [supported destinations](https://docs.cloud.google.com/eventarc/standard/docs/overview#targets) like Cloud Run, Cloud Run functions, or Workflows, to trigger Slack notifications, PagerDuty incidents, or automated remediations.

For example, to subscribe to these events and route them to Cloud Run, use the following command:
    
    
    gcloud eventarc triggers create TRIGGER_NAME \
        --location=global \
        --destination-run-service=DESTINATION_SERVICE \
        --event-filters="type=google.cloud.geminicloudassist.task.v1.completed" \
        --event-filters="proactive=true" \
        --service-account=SERVICE_ACCOUNT
    

Replace the following:

  * `<var>TRIGGER_NAME</var>`: A unique name for your trigger.
  * `<var>DESTINATION_SERVICE</var>`: The name of your Cloud Run service that will process your Proactive Agent events.
  * `<var>SERVICE_ACCOUNT</var>`: The email address of the IAM service account used to invoke the destination.



For more information on using this command, see [Create triggers with Eventarc](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events).

## Event payload

The payload of a delivered event is in Protobuf format, wrapped in Cloud Events, or JSON. It contains the following key fields:

  * `title`: A summary of the task, such as "Cost Anomaly Investigation" or "Investigation of High Latency".
  * `result_object_reference`: A URI pointing to the created artifact.



### Filtering for specific agents

Because proactive mode uses the same event type, you cannot isolate specific agents using Eventarc attributes alone.

To route events to specific channels, your destination service, such as a Cloud Function, must parse the event payload and filter based on the `title` field:

  * To monitor cost alerts, filter for titles containing "Cost Anomaly" or "Cost Optimization".
  * To monitor troubleshooting, filter for titles containing "Investigation of".



## What's next

  * Learn how to [use Proactive Mode for cost optimization](https://docs.cloud.google.com/cloud-assist/proactive-cost-optimization).
  * Review [IAM requirements](https://docs.cloud.google.com/cloud-assist/iam-requirements) for agents.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
