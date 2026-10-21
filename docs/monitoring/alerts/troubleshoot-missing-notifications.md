---
url: https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications/
title: Troubleshoot missing notifications \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:31.050623+00:00
---

# Troubleshoot missing notifications  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot missing notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can diagnose and resolve missing Cloud Monitoring alert notifications by inspecting `notification_channel_events` logs in Logs Explorer. You can then fix delivery and configuration issues across webhook, Pub/Sub, and SMS channels, or adjust alerting policies for virtual machine (VM) shutdowns and request-count metrics.

## Notifications aren't received

If you don't receive any notifications through any configured notification channels, then do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the appropriate Google Cloud project.
  3. Query the logs for notification channel events:

     1. Expand the **Log name** menu and select **notification_channel_events**.
     2. Expand the **Severity** menu and select **Error**.
     3. Optional: To select a custom time range, use the time-range selector.
     4. Click **Run query**.

The previous steps create the following query:
    
    resource.type:"stackdriver_notification_channel"
    logName="projects/PROJECT_ID/logs/monitoring.googleapis.com%2Fnotification_channel_events"
    severity=ERROR
    

The summary line and the `jsonPayload` field typically contain failure information. For example, when a gateway error occurs, the summary line includes "failed with 502 Bad Gateway".




## Webhook notifications aren't received

This section applies when you don't receive notifications through a configured webhook notification channel.

### Private endpoint

If you have a private endpoint, then use [Pub/Sub notifications](https://docs.cloud.google.com/monitoring/support/notification-options#pubsub) combined with a [pull subscription](https://docs.cloud.google.com/pubsub/docs/pull) to that notification topic. You can't use webhooks for notifications to private endpoints.

When you configure a Pub/Sub notification channel, alert notifications are sent to a Pub/Sub queue that has Identity and Access Management controls. Any service that can query for, or listen to, a Pub/Sub topic can consume these notifications. For example, applications running on App Engine, Cloud Run, or Compute Engine virtual machines can consume these notifications.

If you use a pull subscription, then a request is sent to Google that waits for a message to arrive. These subscriptions require access to Google, but they don't require rules for firewalls or inbound access.

### Public endpoint

To identify why the delivery failed, examine your Cloud Logging log entries for failure information.

For example, you can search for log entries for the notification channel resource by using the Logs Explorer, with a filter like the following:
    
    
    resource.type="stackdriver_notification_channel"

## Pub/Sub notifications aren't received

If you don't receive notifications through a configured Pub/Sub notification channel, then the logs can help you diagnose and resolve the failure. This section describes the log entries that the system writes when a notification fails to be sent. You can use the information in this section to resolve the reason for the failure.

### Logs include a `Failed to authenticate as service account` error

When you query the `notification_channel_events` log for errors, you might find a log entry whose `summary` field includes the following message:
    
    
    Failed to authenticate as service account service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
    

This error occurs when the notifications service account doesn't exist. As a result, notifications aren't sent.

To verify that the service account exists, do the following:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Search for a service account that has the following naming convention:
         
         service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
         

If this service account isn't listed, then select **Include Google-provided role grants**.




To trigger Monitoring to create the notifications service account, begin the process of creating a Pub/Sub notification channel:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Edit notification channels**.
  3. In the **Pub/Sub** section, click **Add new**.

Monitoring creates the notifications service account when one doesn't exist. The **Create Pub/Sub Channel** dialog shows the name of the notifications service account.

**Note:** You don't need to finish creating the Pub/Sub notification channel for Monitoring to create the notifications service account.
  4. If you don't want to add a notification channel, click **Cancel**. Otherwise, finish creating the notification channel and click **Add channel**.

  5. Grant the service account permissions to publish to your Pub/Sub topics:

     1. In a new browser tab, open the [Create a notification channel](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels) document.
     2. Select the **Pub/Sub** tab, and then follow the steps in the **Authorize service account** section of the page.



### Logs include a `PERMISSION_DENIED` error

When you query the `notification_channel_events` log for errors, you might find a log entry whose `summary` field includes the following message:
    
    
    An error occurred while publishing notification to Cloud Pub/Sub topic TOPIC_ID. Possible causes: 1) you don't have the required role (https://cloud.google.com/monitoring/support/notification-options#pubsub); or 2) Cloud Pub/Sub API is not enabled in your project: PERMISSION_DENIED
    

This error occurs when the notifications service account hasn't been authorized to send notifications for the Pub/Sub topics of interest, or when the Pub/Sub API isn't enabled in your project.

To view the permissions for a service account, you can use the Google Cloud console or the Google Cloud CLI command:

  * The **IAM** page in the Google Cloud console lists the roles for each service account.
  * The Pub/Sub **Topics** page in the Google Cloud console lists each topic. When you select a topic, the **Permissions** tab lists the roles granted to service accounts.
  * To list all service accounts and their roles, run the following Google Cloud CLI command:
        
        gcloud projects get-iam-policy PROJECT_ID
        

The following is a partial response for this command:
        
        serviceAccount:service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
           role: roles/monitoring.notificationServiceAgent
           - members:
           [...]
           role: roles/owner
           - members:
           - serviceAccount:service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
           role: roles/pubsub.publisher
        

The command response includes only roles; it doesn't include per-topic authorization.

  * To list the IAM bindings for a specific topic, run the following command:
        
        gcloud pubsub topics get-iam-policy TOPIC_ID
        

The following is a sample response for this command:
        
        bindings:
        - members:
           - serviceAccount:service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
           role: roles/pubsub.publisher
        etag: BwXPRb5WDPI=
        version: 1
        




For information about how to authorize the notifications service account, see [Authorize service account](https://docs.cloud.google.com/monitoring/support/notification-options#auth-pubsub-service-account).

### Logs include a `FAILED_PRECONDITION` error

When you query the `notification_channel_events` log for errors, you might find a log entry whose `summary` field includes the following message:
    
    
    An error occurred while publishing notification to Cloud Pub/Sub topic TOPIC_ID: FAILED_PRECONDITION
    

This error occurs when Pub/Sub rejects a publish request from Monitoring because the target topic doesn't meet a required precondition. Common causes for this error include the following:

  * **Message storage policy and data residency restrictions** : Your topic's [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) restricts the Google Cloud regions where messages can be processed or stored:

    * **In-transit enforcement in a disallowed region** : The topic's message storage policy has `enforceInTransit` set to `true`, and the publish request arrives in a region that isn't in `allowedPersistenceRegions`. When `enforceInTransit` is `true`, Pub/Sub rejects requests from disallowed regions instead of redirecting them. If the topic uses [AI inference single message transforms](https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt), then the publish region must also be allowed by the transform.
    * **Restricted allowed persistence regions** : The topic has `enforceInTransit` set to `false` and the publish request arrives outside `allowedPersistenceRegions`, but Pub/Sub can't redirect the request because no viable cluster is available and `allowedPersistenceRegions` contains only private or restricted regions.
    * **Cross-region synchronous replication without a valid secondary region** : The topic uses cross-region synchronous replication and has a message storage policy, but `allowedPersistenceRegions` doesn't include a valid secondary replication region for the publish location.
    * **Regional endpoint without in-transit enforcement** : The publish request is routed to a [regional endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#list_regional_endpoints), but the topic's message storage policy has `enforceInTransit` set to `false`.

To resolve message storage policy errors, update your topic's message storage policy or single message transform region configuration so that `allowedPersistenceRegions` includes the publish region and any required secondary replication region, or set `enforceInTransit` to `false` if in-transit regional enforcement isn't required.

  * **Customer-managed encryption key (CMEK) errors** : Your topic is configured to use a [customer-managed encryption key](https://docs.cloud.google.com/pubsub/docs/encryption) from Cloud Key Management Service (Cloud KMS), and Pub/Sub can't encrypt the published message:

    * **Permission denied on the Cloud KMS key** : Cloud KMS returns a `PERMISSION_DENIED` error when Pub/Sub attempts to encrypt the message, which Pub/Sub reports as `FAILED_PRECONDITION`. For example, this error occurs when the Pub/Sub service agent doesn't have the CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the key.
    * **Unusable Cloud KMS key state** : Cloud KMS returns a `FAILED_PRECONDITION` error because the key version is disabled or destroyed, or because an external key manager key is unreachable.

To resolve CMEK errors, verify that the Cloud KMS key version is enabled and reachable, and ensure that the Pub/Sub service agent has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the key.




## You aren't notified when a VM shuts down

To get notified when a virtual machine (VM) shuts down, create an [uptime check](https://docs.cloud.google.com/monitoring/alerts/uptime-checks) to periodically interrogate the VM and then create an alerting policy to monitor that uptime check. If you are using a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs), then you might need to create a [private uptime check](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

An alerting policy that monitors the [`compute.googleapis.com/instance/uptime`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/instance/uptime) metric won't notify you when the VM shuts down. For this metric, alerting policies only monitor time series for VM instances that are in the `RUNNING` state. If a VM is in any other state, such as `STOPPED` or `DELETED`, then it isn't monitored. For information on VM instance states, see [VM instance life cycle](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

## Notifications for request-count alerting policies aren't received

If you don't receive notifications for an alerting policy that monitors the [`serviceruntime.googleapis.com/api/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) metric, then make sure that the policy's [alignment period](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#alignment_period) is no more than 7 hours 30 minutes.

## SMS notification messages or verification codes aren't received

If you don't receive SMS notifications or verification codes, then make sure that you haven't reached the [SMS message limit](https://docs.cloud.google.com/monitoring/quotas#sms_limits). There might be logs that confirm this error. Check your logs for `Denied quota token`.

Note that SMS isn't a reliable notification channel type and might not be available in certain regions. Avoid relying solely on SMS channels for notifications. Instead, configure additional notification channels such as email.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
