---
url: https://docs.cloud.google.com/eventarc/docs/troubleshooting/
title: Troubleshoot issues \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:24.562162+00:00
---

# Troubleshoot issues  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This page shows you how to resolve issues that you might encounter when using Eventarc.

For destination-specific issues that you might also encounter, refer to troubleshooting for:

  * [Eventarc for Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/troubleshoot)
  * [Eventarc for GKE](https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting)
  * [Eventarc for Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/troubleshoot)



## Eventarc provider

This section provides troubleshooting tips for issues at the source of events (the provider).

### Provider doesn't exist

Check that [the provider exists](https://docs.cloud.google.com/eventarc/docs/list-providers) and that you have [specified the trigger filters](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) appropriately.

### Events are produced from the provider, but are not received at the target

Check that you are filtering for events from providers that are in a supported region for the target destination. For more information, see [locations supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/locations) and [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations).

### Trigger is not delivering events

  1. Verify that the provider is generating events. Check the [Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/reference/audit-logs#viewing_logs) and make sure the monitored service is writing logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

  2. Verify that a Pub/Sub topic with the same trigger name exists.

     1. To list triggers in all locations, run:
            
            gcloud eventarc triggers list --location=-
            

     2. To list Pub/Sub topics, run:
            
            gcloud pubsub topics list
            

Verify that the Pub/Sub topic name includes the name of the created trigger. If the Pub/Sub topic is missing, [create a topic when you create the trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).

     3. To describe triggers and detect any issues with the condition of the trigger, run:
            
            gcloud eventarc triggers describe TRIGGER_ID \
              --location=LOCATION
            

Replace the following:

        * `TRIGGER_ID`: the ID of the trigger or a fully qualified identifier.
        * `LOCATION`: the location of the Eventarc trigger.
     4. The previous command returns the condition of the trigger. If there is an issue with the Pub/Sub topic, one of the following conditions is returned:
            
            conditions:
            transport.pubsub.topic:
              code: NOT_FOUND
              message: Pub/Sub topic not found. Try recreating the trigger.

or
            
            conditions:
            transport.pubsub.topic:
              code: UNKNOWN
              message: Pub/Sub topic status is unknown. Try requesting the trigger description again.

If applicable, do the following:

        * If `Pub/Sub topic not found` is returned, recreate the trigger for a specific provider, event type, and destination](/eventarc/standard/docs/event-providers-targets#triggers) and then create the topic.

        * If `Pub/Sub topic status is unknown` is returned, run the command to describe the trigger again.

        * If the problem persists, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support). For more information, see [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers).

  3. Verify the health of the Pub/Sub topic:

     1. Verify the Pub/Sub topic configuration. Go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

     2. [Monitor](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_forwarded_undeliverable_messages) if messages are published to the topic with the metric: `topic/send_message_operation_count`. If messages are not published to the topic, check [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#viewing_audit_logs) and make sure the monitored service is emitting logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

     3. [Monitor](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions) if messages are pushed successfully with the metric: `subscription/push_request_count` by `response_code`. If push errors are reported, check the service logs. If the receiving endpoint returns a non-OK status code, it indicates that the Cloud Run code is not working as expected and you must [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).




## Eventarc trigger

This section provides troubleshooting tips for issues at the trigger.

### Permission denied errors

  * If you encounter a `Failed to load service details: permission denied` error, confirm that the trigger permissions are configured correctly, and that the Pub/Sub service account is granted the `iam.serviceAccountTokenCreator` role. For more information, see [Access control with IAM](https://docs.cloud.google.com/eventarc/standard/docs/access-control).

  * If you encounter the following error while trying to create a trigger, wait a few minutes ([potentially, seven](https://docs.cloud.google.com/iam/docs/access-change-propagation)), and then try creating the trigger again:
        
        Permission denied while using the Eventarc Service Agent. If you recently started to use
        Eventarc, it may take a few minutes before all necessary permissions are propagated to the
        Service Agent. Otherwise, verify that it has Eventarc Service Agent role.
        

A service agent acts as the identity of a given Google Cloud service for a particular project. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) and view the Identity and Access Management (IAM) permissions for the [Eventarc Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.serviceAgent) (`roles/eventarc.serviceAgent`).

If you are still running into the previous error after attempting to create your resource again, complete the following steps to verify that the Eventarc service agent exists in your Google Cloud project and has the necessary role:

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

    2. On the **View by principals** tab, select the **Include Google-provided role grants** checkbox.
    3. In the list of principals, locate the Eventarc service agent, which uses the following format:

`service-`PROJECT_NUMBER`@gcp-sa-eventarc.iam.gserviceaccount.com`

    4. Verify that the service agent has the **Eventarc Service Agent** role. If the service agent doesn't have the role, then [grant the role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).
**Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).
  * If you are trying to use a cross-project service account and you encounter a permission denied error for `iam.serviceAccounts.getAccessToken` or `iam.serviceAccounts.actAs`, or if you receive an error message similar to `...cross-project service accounts are disabled` or `Failed to impersonate...`, confirm that permissions are configured correctly. For more information, see [Use a cross-project service account](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account).




### Pub/Sub topic not displaying CMEK key

[Enabling an Eventarc channel with a customer-managed encryption key](https://docs.cloud.google.com/eventarc/docs/use-cmek) (CMEK) protects the Pub/Sub topic used as a transport layer by Eventarc Standard. However, the CMEK key is not displayed through the Google Cloud console. You can verify that a CMEK key is enabled for the Pub/Sub topic by using the Google Cloud CLI:

  1. Describe the Eventarc trigger:
         
         gcloud eventarc triggers describe TRIGGER_ID \
               --location=LOCATION
         

Replace the following:

     * `TRIGGER_ID`: the ID of your Eventarc trigger
     * `LOCATION`: the location of the trigger

The Pub/Sub topic ID is returned. For example: `topic: projects/PROJECT_ID/topics/TOPIC_ID`

  2. Describe the Pub/Sub topic:
         
         gcloud pubsub topics describe TOPIC_ID
         

Replace `TOPIC_ID` with the Pub/Sub topic ID retrieved in the previous step.

The CMEK key name is returned. For example:
         
         kmsKeyName: projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME/grants/GRANT_ID
         




### Unexpected charges when using Eventarc

When you create a trigger, check if the filters configured could lead to triggers being set off indefinitely. To help avoid unexpected charges on your bill, set budgets and alerts using Google Cloud's billing console. For more information, see [Create a budget](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget).

## Related information

  * To learn more about Eventarc, see the [overview](https://docs.cloud.google.com/eventarc/standard/docs/overview).
  * For a tutorial on Eventarc troubleshooting, see [Debug a Cloud Run service using Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run).
  * For event publishing issues, see [Troubleshoot event publishing](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/troubleshoot-providers).
  * To get additional help, see [Get support](https://docs.cloud.google.com/eventarc/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
