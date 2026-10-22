---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/troubleshoot/
title: Troubleshoot Eventarc for Cloud Run \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:32.054591+00:00
---

# Troubleshoot Eventarc for Cloud Run  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot Eventarc for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This page shows you how to resolve issues that you might encounter when using Eventarc for Cloud Run.

For other issues that you might also encounter, refer to troubleshooting for:

  * [Issues common to all destinations](https://docs.cloud.google.com/eventarc/docs/troubleshooting)
  * [Eventarc for GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting)
  * [Eventarc for Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/troubleshoot)



## Cloud Run service is not receiving events

If a service is not receiving events, the following resolutions might help:

###  Cloud Audit Logs events 

  * Check that **Admin Read** , **Data Read** , and **Data Write** access is enabled for the service's audit logs. 

[Go to Audit Logs](https://console.cloud.google.com/iam-admin/audit)

  * Check that enough time has elapsed since creating the trigger. It can take up to two minutes before the trigger is functional.
  * Follow the [prerequisites](https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-cloud-audit-logs-gcloud#before-you-begin) for Eventarc trigger creation.
  * Check that your event filters are not too restrictive. For more information, see [event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal).
  * Confirm that the monitored service is generating audit logs through the **Logs Explorer**. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  * Check the Cloud Run logs on the **Cloud Run** page: 

[Go to Cloud Run](https://console.cloud.google.com/run)

Click the service you created in Cloud Run and navigate to the **Logs** tab. If the logs show that the service received a non-OK status code, the Cloud Run service is rejecting events.



###  Pub/Sub messages 

  * Confirm that the Eventarc trigger is created.
  * Confirm that the Pub/Sub topic is created and attached to the Eventarc trigger.
  * Check that the Pub/Sub topic exists: Go to **Pub/Sub** and search for the topic.
  * Check that enough time has elapsed since creating the trigger. It can take up to two minutes before the trigger is functional.
  * Check the Cloud Run logs on the **Cloud Run** page. 

[Go to Cloud Run](https://console.cloud.google.com/run)

Click the service you created in Cloud Run and navigate to the **Logs** tab. If the logs show that the service received a non-OK status code, the Cloud Run service is rejecting events.



## Trigger is set, but target does not receive events

  * Check that the event payload you are sending does not exceed the limits on [event size (512KB)](https://docs.cloud.google.com/eventarc/docs/quotas). The Pub/Sub push subscriptions are also subject to a set of [resource limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits) such as throughput per publish region. This makes sure that the Pub/Sub event payload is less than 512KB.

  * Locate the Pub/Sub topic associated with the Cloud Run trigger.

    1. Go to **Pub/Sub** > **Topics**.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

    2. Verify that the Pub/Sub topic name includes the name of the created trigger.

  * [Monitor](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_forwarded_undeliverable_messages) if messages are published to the topic with the metric: `topic/send_message_operation_count`. If messages are not published to the topic, check [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#viewing_audit_logs) and make sure the monitored service is emitting logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

  * [Monitor](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions) if messages are pushed successfully with the metric: `subscription/push_request_count` by `response_code`. If push errors are reported, check the Cloud Run service logs. If the receiving endpoint returns a non-OK status code, it indicates that the Cloud Run code is not working as expected and you must [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).




## Cannot find your Pub/Sub topic

The Pub/Sub topic could have been removed or modified. A new Pub/Sub topic is created when you create a trigger, so [delete the existing trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete) and [create it](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-pubsub) again.

## INVALID_ARGUMENT service does not exist error message

If you receive an `INVALID_ARGUMENT: cloud run service "SERVICE_NAME" in region "REGION_NAME" does not exist` error message, the service account has been deleted. Events won't be delivered to Cloud Run if the service account for the target service is deleted. Create a new [Cloud Run service account](https://docs.cloud.google.com/run/docs/configuring/services/service-identity).

## Unexpected cost or traffic due to event delivery retries

Eventarc Standard supports at-least-once event delivery. This means that if a destination fails to acknowledge an event, Eventarc will automatically attempt to redeliver it. If you notice unexpected charges, or if your Cloud Run service isn't configured to handle repeated retries of failed events, you might need to modify your trigger's retry policy.

You can configure a retry policy that specifies a single event delivery attempt with no retries. Or, you can customize the default retry behavior. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

## Cloud Run service is down

Even if the Cloud Run service is down, Pub/Sub retains events for seven days by default and will retry sending events to the target. For more information on Pub/Sub resource limits, see [Quotas and limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits).

## Related information

  * To learn more about Eventarc, see the [overview](https://docs.cloud.google.com/eventarc/standard/docs/overview).
  * For a tutorial on Eventarc troubleshooting, see [Debug a Cloud Run service using Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run).
  * To get additional help, see [Get support](https://docs.cloud.google.com/eventarc/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
