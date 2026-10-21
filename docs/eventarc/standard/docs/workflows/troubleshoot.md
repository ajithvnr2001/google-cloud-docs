---
url: https://docs.cloud.google.com/eventarc/standard/docs/workflows/troubleshoot/
title: Troubleshoot Eventarc for Workflows \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:58.055440+00:00
---

# Troubleshoot Eventarc for Workflows  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/workflows/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot Eventarc for Workflows Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This page shows you how to resolve issues that you might encounter when using Eventarc for Workflows.

For other issues that you might also encounter, refer to troubleshooting for:

  * [Issues common to all destinations](https://docs.cloud.google.com/eventarc/docs/troubleshooting)
  * [Eventarc for Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/troubleshoot)
  * [Eventarc for GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting)



### Trigger creation fails because workflow target does not exist

You receive an error message similar to the following: 
    
    
    cloud workflow "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_ID" does not exist
    

This output includes the following values: 

  * `PROJECT_ID`: your Google Cloud project ID
  * `LOCATION`: the location of your workflow
  * `WORKFLOW_ID`: the name of your workflow



This occurs when Eventarc is not able to find the target workflow. To resolve this:

  1. Ensure that the target workflow exists and is ACTIVE: 
         
         gcloud workflows list --location -

The output should be similar to the following: 
         
         NAME                                                          STATE   REVISION_ID  UPDATE_TIME
         projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_ID  ACTIVE  000004-c0c   2021-11-19T14:29:27.530185556Z

  2. Ensure that you have provided the correct workflow ID and workflow location when creating the trigger.




### Trigger is created successfully but target is not receiving events

Check that enough time has elapsed since creating the trigger. It can take up to two minutes before events are sent.

If the trigger still doesn't work and events are not being delivered:

  1. Events sent from Pub/Sub to the target might be getting dropped. To ensure that events aren't dropped, [set up a Pub/Sub subscription retry policy](https://docs.cloud.google.com/pubsub/docs/subscription-retry-policy) or [forward undelivered messages to a dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics) (also known as a _dead-letter queue_).

Before setting the dead-letter topic, retrieve the trigger's topic and subscription:
         
         gcloud eventarc triggers describe TRIGGER \
         --location=LOCATION

Replace the following:

     * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger.

  2. Use the Google Cloud console to [monitor](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_forwarded_undeliverable_messages) if messages are published to the Pub/Sub topic with the metric: `topic/send_message_operation_count`.

  3. If messages are not being published to Pub/Sub topic, verify that the source is generating events:

     * For events from Cloud Audit Logs, check the [logs](https://docs.cloud.google.com/eventarc/docs/reference/audit-logs#viewing_logs) and make sure that the monitored service is writing logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).
     * For events from Cloud Storage, check notifications for your bucket: 
           
           gcloud storage buckets notifications list gs://BUCKET_NAME

Replace `BUCKET_NAME` with the name of the bucket. The output should be similar to the following: 
           
           projects/_/buckets/BUCKET_NAME/notificationConfigs/NOTIFICATION_CONFIG_ID
           Cloud Pub/Sub topic: projects/PROJECT_ID/topics/TOPIC_ID
           Filters:
             Event Types: OBJECT_ARCHIVE

This output includes the following values:

       * `TOPIC_ID`: the ID of the existing Pub/Sub topic.
       * `NOTIFICATION_CONFIG_ID`: the ID of the notification configuration.
  4. If events are being delivered but no workflow executions are being triggered, this is likely due to an unauthenticated invocation. Ensure that the trigger is associated with a service account that has permission to create workflow executions. For more information, follow the instructions to create a user-managed service account in the "Prepare to create a trigger" section when creating a trigger for a [specific provider, event type, and Workflows destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) .

  5. If messages are published to a Pub/Sub topic but no workflow executions are being triggered, make sure that the Eventarc payload is not more than 512 KB. For more information on resource limits, see [Quotas and Limits](https://docs.cloud.google.com/workflows/quotas#resource_limit).

     1. In the Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription/list)

     2. Monitor unacknowledged messages in the subscription. For more information, see [Monitoring forwarded undeliverable messages](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_forwarded_undeliverable_messages).

     3. If there are unacknowledged messages, monitor the workflow logs for the [`TriggerPubsubExecution` method](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#methodname_119). For more information on viewing workflow logs, see [View workflow logs](https://docs.cloud.google.com/workflows/docs/log-workflow#viewing-logs).

        * Use the filter `Permission 'workflows.executions.create' denied` to verify if the trigger is associated with a service account that has permission to trigger workflow executions. For more information on how to grant the appropriate roles to the service account, follow the instructions in the "Prepare to create a trigger" section when creating a trigger for a [specific provider, event type, and Workflows destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).
        * Use the key word `event size exceeded` to verify if the event size is over 512 KB.
     4. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).




## Related information

  * For other issues specific to Workflows, see [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting).
  * To get additional help, see [Get support](https://docs.cloud.google.com/eventarc/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
