---
url: https://docs.cloud.google.com/kms/docs/monitoring/
title: Using Cloud Monitoring with Cloud KMS \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:40.842231+00:00
---

# Using Cloud Monitoring with Cloud KMS  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Using Cloud Monitoring with Cloud KMS Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Monitoring](https://docs.cloud.google.com/monitoring) can be used to monitor operations performed on resources in Cloud Key Management Service.

This topic provides:

  * an example for monitoring when a key version is scheduled for destruction
  * information about monitoring other Cloud KMS resources and operations



## Before you begin

If you haven't already done so, set up a Google Cloud project that has the Cloud Key Management Service API enabled. These steps are documented in the [Cloud KMS Quickstart](https://docs.cloud.google.com/kms/docs/create-encryption-keys#before-you-begin).

## Create a counter metric

Use the [`gcloud logging metrics create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/create) command to create a counter metric that will monitor any occurrence of the scheduled destruction of a key version.
    
    
    gcloud logging metrics create key_version_destruction \
      --description "Key version scheduled for destruction" \
      --log-filter "resource.type=cloudkms_cryptokeyversion \
      AND protoPayload.methodName=DestroyCryptoKeyVersion"
    

You can list your counter metrics using the [`gcloud logging metrics list`](https://docs.cloud.google.com/monitoring/alerts) command:
    
    
    gcloud logging metrics list
    

For more information about creating a counter metric, including via the Google Cloud console and the Monitoring API, see [Creating a counter metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics#creating_a_counter_metric).

## Create an alerting policy

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `key_version` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Global**.
     3. For the **Metric category** , select **Logs-Based Metric**.
     4. For the **Metric** , select **logging/user/key_version_destruction**.
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Complete this page with the settings in the following table.  
**Configure alert trigger** page  
Field |   
Value  
---|---  
**`Alert trigger`** | `Any time series violates`  
**`Threshold position`** | `Above threshold`  
**`Threshold value`** | `0`  
**`Advanced Options: Retest window`** | `No retest`  
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

To test your new notification, [schedule a key version for destruction](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) and then check your email to see if the notification was sent.

This alert will be triggered each time a key version has been scheduled for destruction. Note that the alert will get automatically resolved (even though the key version remains scheduled for destruction), so there will be two email notifications, one for the scheduled destruction, and one for the alert being resolved.

For more information about alert policies, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts). To learn how to turn on, turn off, edit, copy, or delete an alert policy, see [Managing policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#managing_policies).

For information about different types of notifications, see [Notification options](https://docs.cloud.google.com/monitoring/support/notification-options).

**Note:** If you only wanted to test a notification for scheduling destruction of a key version, but you do not want it actually destroyed, [restore the key version](https://docs.cloud.google.com/kms/docs/destroy-restore#restore_a_key_version) that you scheduled for destruction.

## Monitoring administrative activities vs. data access

The scheduled destruction of a key version is an _administrator activity_. Administrator activities are logged automatically. If you want to create an alert for _data access_ of a Cloud KMS resource, e.g. monitoring when a key is used for encryption, you need to [enable Data Access logs](https://docs.cloud.google.com/kms/docs/logging#enabling_data_access_logs) and then create an alert policy as described in this topic.

For more information about logging of Cloud KMS administrative activities and data access, see [Using Cloud Audit Logs with Cloud KMS](https://docs.cloud.google.com/kms/docs/logging).

## Rate quota metrics

Cloud KMS supports the following rate quota metrics:

  * `cloudkms.googleapis.com/crypto_requests`
  * `cloudkms.googleapis.com/external_kms_requests`
  * `cloudkms.googleapis.com/hsm_asymmetric_requests`
  * `cloudkms.googleapis.com/hsm_symmetric_requests`
  * `cloudkms.googleapis.com/read_requests`
  * `cloudkms.googleapis.com/write_requests`



For information about monitoring these quotas using Cloud Monitoring, see [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).

## What's next

  * [Monitor your external key manager usage](https://docs.cloud.google.com/kms/docs/monitor-ekm-usage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
