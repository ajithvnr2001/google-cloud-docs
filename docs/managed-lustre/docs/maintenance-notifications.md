---
url: https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications/
title: Maintenance notifications and logs \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:36.380238+00:00
---

# Maintenance notifications and logs  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Maintenance notifications and logs Stay organized with collections  Save and categorize content based on your preferences. 

Managed Lustre provides email notifications and Cloud Logging records to help you track automated maintenance events across your instances.

## Email notifications

You can subscribe to email notifications for upcoming automated maintenance events to plan for potential disruption. Subscriptions to maintenance notifications are managed through your Google Cloud console Communication page:

[Go to the **Communication** page](https://console.cloud.google.com/user-preferences/communication)

Once subscribed, email notifications are sent based on whether a [maintenance policy](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies) is configured for the instance.

Instances with a maintenance policy receive the following notifications:

  * **Advance notification** : Sent 7 to 14 days before a scheduled maintenance event, or after a maintenance event has been rescheduled.
  * **Canceled** : Sent if a scheduled maintenance event is canceled by Google, rescheduled, or automatically canceled following a successful self-service upgrade.
  * **In progress** : Sent when a scheduled maintenance event starts.
  * **Completed** : Sent when a scheduled maintenance event is completed.



Instances without a maintenance policy receive **In progress** and **Completed** notifications when automated maintenance occurs.

[Self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance) doesn't send email notifications or write maintenance logs. See [Track maintenance progress](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance#track_maintenance_progress) for how to monitor self-service maintenance progress.

## View maintenance logs

Managed Lustre uses Cloud Logging to log maintenance events, including the following activity types:

  * `LustreAdvancedNotification`: Maintenance has been scheduled for the instance. Only sent for instances with a maintenance policy.
  * `LustreOngoingNotification`: Maintenance has started on the instance. Once complete, another `LustreOngoingNotification` event is logged with `is_completed=true`.
  * `LustreCancelledNotification`: Maintenance has been cancelled. Only sent for instances with a maintenance policy.



You can view maintenance logs using Logs Explorer or by using gcloud CLI.

###  Logs Explorer 

To view Managed Lustre maintenance logs using Logs Explorer, do the following:

  1. In the Google Cloud console, go to the **Cloud Logging** > **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

  2. Enter the following filter into the query editor and click **Run query** :
         
         resource.type="lustre.googleapis.com/Instance"
         resource.labels.instance_id="INSTANCE_ID"
         resource.labels.location="LOCATION"
         logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmaintenance"
         

Replace the following:

     * INSTANCE_ID: The ID of your Managed Lustre instance.
     * LOCATION: The location of your Managed Lustre instance.
     * PROJECT_ID: The ID of your Google Cloud project.



###  gcloud CLI 

To view maintenance logs with gcloud CLI, run the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
    
    
    gcloud logging read 'resource.type="lustre.googleapis.com/Instance" resource.labels.instance_id="INSTANCE_ID" resource.labels.location="LOCATION" logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmaintenance"' --project=PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: The ID of the Managed Lustre instance.
  * `LOCATION`: The zone where the instance is located.
  * `PROJECT_ID`: The project ID of the project where the instance is located.



## What's next

  * [Maintenance overview](https://docs.cloud.google.com/managed-lustre/docs/maintenance)
  * [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies)
  * [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
