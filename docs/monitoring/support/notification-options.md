---
url: https://docs.cloud.google.com/monitoring/support/notification-options/
title: Create and manage notification channels \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:22.001401+00:00
---

# Create and manage notification channels  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/support/notification-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create and manage notification channels Stay organized with collections  Save and categorize content based on your preferences. 

Notification channels in Cloud Monitoring let you notify yourself or your on-call team whenever an alerting policy triggers. Using the Google Cloud console, you can configure notification channels and attach them to your alerting policies—for example, to publish alerts for Compute Engine instances to a Pub/Sub topic and notify an on-call Slack channel. Because notifications might contain sensitive data, review your regulatory practices before you create a channel.

To configure channels programmatically instead of using the Google Cloud console, see [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api). For details about delivery behavior, see [Notification latency](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#notification-latency) and [When Monitoring sends notifications and creates alerts](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#notify-alert-policy).

This feature is supported only for Google Cloud projects. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

## Before you begin

To get the permissions that you need to view and configure notification channels by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Decide which notification channels to create

We recommend that you create multiple types of notification channels for redundancy purposes due to the following reasons:

  * Google Cloud has no control over many of the delivery systems after it has passed a notification to those systems.
  * Cloud Mobile App, PagerDuty, webhooks, and Slack notifications are all powered by the same Google Cloud internal service and therefore share a single point of failure. If you use one of these notification channels, then use email or Pub/Sub as the redundant channel.
  * SMS isn't a fully reliable notification channel type, and it might not be available in certain regions. Whenever you use an SMS notification channel, also use a different notification channel type as a backup.



If you plan to use automation tools to read, reroute, transform, or otherwise act on notifications, then use the webhook or Pub/Sub channels. We don't recommend using other channel types with automation tools because the notification format is subject to change.

## Create a notification channel

When you are creating an alerting policy, you can select any configured notification channel and add it to your policy. You can pre-configure your notification channels, or you can configure them as part of the process of creating an alerting policy. For more information, see Create a channel on demand.

To create a notification channel by using the Google Cloud console, follow the channel-specific instructions contained in the following table:

### Email

To add an email notification channel, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **Edit notification channels**.
  4. In the **Email** section, click **Add New**.
  5. Enter a single email address and a description.
  6. Click **Save**.



If you use a group email address as the notification channel for an alerting policy, then configure the group to accept mail from `alerting-noreply@google.com`.

You can create email channels during the creation of an alerting policy. For more information, see Create a channel on demand.

###  Mobile App 

Use the [Google Cloud console Mobile App](https://cloud.google.com/app) to monitor your Google Cloud console resources and Monitoring information from anywhere. Google Cloud console Mobile App notifications are either sent to a specific device or to a specific user:

![List of Google Cloud console Mobile App notification channels.](https://docs.cloud.google.com/static/monitoring/images/notification-mobileapp.png)

  * **Device** indicates that notifications are sent only to the specific device that created the notification channel. For device-scoped notification channels, the **Display name** field includes device information.
  * **User** indicates that the notifications are sent to all of your devices that have the Google Cloud console Mobile App installed.



Cloud Monitoring determines the notification scope when the channel is created. You can't select or change the scope.

To configure a Google Cloud console Mobile App notification channel for a specific Google Cloud project, do the following: 

  1. Install the Google Cloud console Mobile App from your mobile device's app store. 
  2. Select a project for viewing in the Google Cloud console Mobile App.

After you select a project, a data exchange between the app and the selected Google Cloud project occurs. A notification channel is created when one doesn't exist, and after a few minutes, this channel is listed under the **Mobile Devices** section of the **Notification channels** page.




To add your mobile device as a notification channel for an alerting policy, in the alerting **Notifications** section, select **Google Cloud console (mobile)** and then choose your mobile device from the list.

### PagerDuty

PagerDuty supports two-way synchronization with Monitoring. As a result, the following are true: 

  * If an alert is created in Monitoring, then an alert is opened in PagerDuty.
  * You can't use PagerDuty to close an alert in Monitoring.
  * If you resolve an alert in PagerDuty and if Monitoring has the alert open, then the alert is reopened in PagerDuty.



To set up PagerDuty notifications, do the following:

  1. In your **PagerDuty** account, configure the integration in a new service or add the integration to an existing service. 
     1. Create an account or sign in to an existing account.
     2. Go to the **Services** page.
        * To create a service, do the following: 
          1. Click **\+ New Service**.
          2. Enter a service name and description, and then click **Next**.
          3. Configure an escalation policy, and then click **Next**.
          4. If your PagerDuty account supports alert grouping and transient alerts, configure them, and then click **Next**.
          5. On the integrations setup page, in the **Search for an integration(s)** toolbar, enter `Events API v1`, and then click **Create Service**. You are then returned to the **Integrations** panel of your new service.
        * To edit an existing service, do the following: 
          1. Select a service from your Service Directory.
          2. On your service page, select the **Integrations** panel.
          3. Click **\+ Add another integration** to go to the integrations setup page.
          4. On the integrations setup page, in the **Search for an integration(s)** toolbar, enter `Events API v1`, and then click **Add**. You are then returned to the **Integrations** panel of your edited service.
     3. On your service's **Integrations** panel, find the listing for your new integration, expand its menu, and then copy the integration key. 
     4. Optional: Configure PagerDuty to accurately map alert severity values from Monitoring.
  2. In Cloud Monitoring, add the PagerDuty notification channel: 
     1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
     3. Click **Edit notification channels**.
     4. In the **PagerDuty** section, click **Add New**.
     5. Enter the **Display Name**. This name should match the name of the PagerDuty service where you configured your new integration in Step 1.
     6. Paste the integration key that you copied in Step 1 into the **Service Key** field.
     7. Click **Save**.



When you create an alerting policy, select **PagerDuty** in the **Notifications** section and choose your PagerDuty configuration.

The JSON packet for PagerDuty has the following format:
    
    
     {
         "description": A string of various fields in the alert,
         "details": JSON payload with schema version 1.2.
     }
    

To view an example and the schema for the `details` field, expand the following sections.

#### JSON examples

By default, the alerting backend attempts to generate a JSON packet with version 1.2 formatting. For more information about this formatting, see the next section.

The following is an example of such a packet:
    
    
    {
      "incident": {
        "incident_id": "0.opqiw61fsv7p",
        "renotify": true,
        "scoping_project_id": "internal-project",
        "scoping_project_number": 12345,
        "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.lxfiw61fsv7p?project=internal-project",
        "severity": "no severity",
        "started_at": 1577840461,
        "ended_at": 1577877071,
        "state": "closed",
        "resource_id": "11223344",
        "resource_name": "internal-project gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_display_name": "gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_type_display_name": "VM Instance",
        "resource": {
          "type": "gce_instance",
          "labels": {
            "instance_id": "11223344",
            "project_id": "internal-project",
            "zone": "us-central1-c"
          }
        },
        "metric": {
          "type": "compute.googleapis.com/instance/cpu/utilization",
          "displayName": "CPU utilization",
          "labels": {
            "instance_name": "the name of the VM instance"
          }
        },
        "metadata": {
          "system_labels": { "labelkey": "labelvalue" },
          "user_labels": { "labelkey": "labelvalue" }
        },
        "policy_name": "Monitor-Project-Cluster",
        "policy_user_labels" : {
            "user-label-1" : "important label",
            "user-label-2" : "another label"
        },
        "condition_name": "VM Instance - CPU utilization [MAX]",
        "threshold_value": "0.9",
        "observed_value": "0.835",
        "condition": {
          "name": "projects/internal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789",
          "displayName": "VM Instance - CPU utilization [MAX]",
          "conditionThreshold": {
            "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\" metadata.system_labels.\"state\"=\"ACTIVE\"",
            "aggregations": [
              {
                "alignmentPeriod": "120s",
                "perSeriesAligner": "ALIGN_MEAN"
              }
            ],
            "comparison": "COMPARISON_GT",
            "thresholdValue": 0.9,
            "duration": "0s",
            "trigger": {
              "count": 1
            }
          }
        },
        "documentation": {
          "content": "TEST ALERT\n\npolicy.name=projects/internal-project/alertPolicies/1234567890123456789\n\npolicy.display_name=Monitored-Project-NO-GROUPBY\n\ncondition.name=projects/nternal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789\n\ncondition.display_name=VM Instance - CPU utilization [MAX]\n\nproject=internal-project\n\nresrouce.project=internal-project \n\nDONE\n",
          "mime_type": "text/markdown",
          "subject": "ALERT - No severity",
          "links": [
            {
              "displayName": "Playbook",
              "url": "https://myownpersonaldomain.com/playbook?name=${resource.name}"
            }
          ]
        },
        "summary": "CPU utilization for internal-project gke-cluster-1-16-default-pool-e2df4cbd-dgp3 with metric labels {instance_name=gke-cluster-1-default-pool-e2df4cbd-dgp3} and system labels {state=ACTIVE} returned to normal with a value of 0.835."
      },
      "version": "1.2"
    }
    

#### Schema structure, version 1.2

This section describes version 1.2 of the payload schema. Some fields might not appear in all returned packets or might have empty values, depending on the configuration of the alerting policy, the state of the incident, or the resource being monitored. Some fields take embedded structures as values; these structures are described by reference because their contents can also vary.

In a returned packet, the fields can occur in any order. In the description that follows, they are organized into related groups.

`{`  
` **"version"** : "1.2",`  
` **"incident"** : {`  
` `  
` `Information about the incident.  
` `  
` **"incident_id"**`: string, generated ID for this incident.  
` **"renotify"**`: bool, optional. Set to `true` when the message is a repeated notification.  
` **"scoping_project_id"**`: string, the project ID that hosts the metrics scope.  
` **"scoping_project_number"**`: number, the project number of the scoping project.  
` **"url"**`: string, Google Cloud console URL for this incident.  
` **"started_at"**`: number, time (in Unix epoch seconds) when the incident was opened.  
` **"ended_at"**`: number, time (in Unix epoch seconds) when the incident was closed. Populated only when `state` is `closed`.  
` **"state"**`: string, state of the incident: `open` or `closed`. If `open`, then `ended_at` is null.  
` **"summary"**`: string, generated textual summary of the incident.  
` **"apigee_url"**`: string, [Apigee](https://docs.cloud.google.com/apigee/docs) URL for this incident, only for Apigee resource types [ `Environment` and `Proxy*`](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment).  
` **"observed_value"**`: string, observed value that triggered/resolved the alert, may be empty if the condition is expired.  
` `  
` `Information about the monitored resource for which the incident was opened.  
` `  
` **"resource"** : {`  
` **"type"**`: string, identifier of the monitored resource type being alerted on, for example, `gce_instance`; see [List of monitored resources](https://docs.cloud.google.com/monitoring/api/resources).  
` **"labels"**`: object, key-value pairs for labels associated with the monitored resource.  
` },`  
` **"resource_type_display_name"**`: string, display name of the monitored resource type.  
` **"resource_id"**`: string, instance ID of the monitored resource, same value as `resource.labels.instance_id`.  
` **"resource_display_name"**`: string, display name of the monitored resource.  
` **"resource_name"**`: string, generated name of this monitored resource; consists of values from other fields.  
` `  
` `Information about the metric type of the time-series data.  
` `  
` **"metric"** : {`  
` **"type"**`: string, identifier of the metric type being alerted on, for example, `compute.googleapis.com/instance/cpu/utilization`; see [List of metrics](https://docs.cloud.google.com/monitoring/api/metrics).  
` **"displayName"**`: string, display name of the metric type.  
` **"labels"**`: object, key-value pairs for labels associated with the metric.  
` },`  
` **"metadata"** : {`  
` **"system_labels"**`: object, key-value pairs for system metadata labels.  
` **"user_labels"**`: object, key-value pairs for user metadata labels.  
` },`  
` `  
` `Information about the alerting policy and condition that opened/resolved the incident.  
` `The values are drawn from the relevant [ `AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object.  
` `  
` **"policy_name"**`: string, display name for the alerting policy.  
` **"policy_user_labels"**`: object, key-value pairs for any user labels attached to the policy.  
` **"documentation"**`: object, an embedded structure of the form [ `Documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).  
` **"condition"**`: object, an embedded structure of the form [ `Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition).  
` **"condition_name"**`: string, display name of the condition, same value as `condition.displayName`.  
` **"severity"**`: string, severity level of incidents. If this field isn't defined during alerting policy creation, then Cloud Monitoring sets the alerting policy severity to `no severity`.  
` **"threshold_value"**`: string, the threshold value of this condition, may be empty if the condition isn't a threshold condition.  
` },`  
`}`  


#### Deprecation policy

The payload schema is subject to the Google Cloud deprecation policy outlined in Section 1.4(d) of the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms). Note that the schema does not control the formats of generated field values, and these formats can change without notice. For example, `incident.summary`, `incident.documentation.content`, and `incident.url` are meant to include data pertaining to their fields, but the schema doesn't have constraints to guarantee accurate parsing of these fields. You can consume the value as a whole and expect that it adheres to the deprecation policy, but don't rely on parsing the generated fields. 

#### Configure PagerDuty to map severity levels

By default, PagerDuty notifications show all alert severity levels as "critical". You can configure event orchestration rules in PagerDuty so that the PagerDuty alert severity matches the Monitoring alert severity:

  1. In your PagerDuty account, go to the **Services** page.
  2. Select the PagerDuty service where you receive Google Cloud notifications.
  3. Click **Settings**.
  4. Go to the **Event Management** section and then click **View Orchestration Rules**.
  5. Click **New Rule**.
  6. For each Monitoring severity value that you want to convert, create a conditional rule that maps the severity value to an equivalent PagerDuty value: 
     1. In the menu under **Step 1: When should this rule be applied?** , select **If events match certain conditions**.
     2. Select the code editor.
     3. In the **If** section, enter `event.custom_details.incident.severity matches part` 'VALUE', where VALUE is the name of a Monitoring severity value, and then click **Next**.
     4. Under **Step 2: What action(s) should be applied?** , select **Alert Data**.
     5. Set the alert severity to a value that matches the Monitoring value that you entered in Step C, and then save your changes.
  7. Optional: To add additional rules, click **Else rule**.



### SMS

To configure SMS notifications, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **Edit notification channels**.
  4. In the **SMS** section, click **Add New**.
  5. Complete the dialog and click **Send Verification Code**.

A verification code is sent to the contact number you provided.

  6. Enter the code and click **Verify**.

If you don't receive a code, see [SMS notification messages or verification codes aren't received](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#sms-messages-codes).




When you set up your alerting policy, select the **SMS** notification type and choose a verified phone number from the list. 

### Slack

**Note:** To complete these steps, you must be a Slack Workspace Owner or Admin. For more information, see [Managing invite requests](https://api.slack.com/admins/inviting).

The Monitoring Slack integration allows your alerting policies to post to a Slack channel when a new alert is created. To set up Slack notifications, do the following:

  1. **In Slack** : Create a Slack workspace and channel at the [Slack site](https://www.slack.com/). Record the channel URL.

  2. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

  4. Click **Edit notification channels**.

  5. In the **Slack** section, click **Add New** to open the Slack sign-in page:

     1. Select your Slack workspace.
     2. Click **Allow** to enable Cloud Monitoring access to your Slack workspace. This action takes you back to the Monitoring configuration page for your notification channel.
     3. In the **Slack Channel Name** field, enter the name of the Slack channel you want to use for notifications.
     4. In the **Cloud Alerting Display Name** field, enter a short descriptive statement. Monitoring displays the value of this field on the **Notification channels** page.
     5. Optional: To test the connection between Cloud Monitoring and your Slack workspace, click **Send test notification**. If the connection is successful, then you see a message `This is a test alert notification...` in the Slack notification channel that you specified. Check the notification channel to confirm receipt.
  6. If the Slack channel you want to use for notifications is a private channel, then you must manually invite the Monitoring app to the channel:

     1. Open Slack.
     2. Go to the channel you specified as your Monitoring notification channel.

     3. Invite the Monitoring app to the channel by entering and sending the following message in the channel:
            
            /invite @Google Cloud Monitoring

You must invite the Monitoring app to the private channel you specified when creating the notification channel in Monitoring. Inviting the Monitoring app to public channels is optional.

When you create an alerting policy, select **Slack** in the **Notifications** section and choose your Slack configuration. 




### Webhooks

Before you configure a webhook notification channel, consider the following:

  * Webhooks only support public endpoints. A public endpoint is fully accessible from the public internet, such as by HTTP (`port:80`) or HTTPS (`port:443`). The notification service must be able to establish a connection to the endpoint and, in the case of HTTPS, verify the server's security certificate. If you need notifications sent to an endpoint that isn't public, then create a Pub/Sub notification channel and configure a subscription to the Pub/Sub topic. For more information, see [Webhook notifications fail when configured for a private endpoint](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#webhook). 
  * If a Cloud Run function is configured as a webhook endpoint for a notification channel, then ensure the user invoking the function has the required authentication permission. For more information, see [Authenticate for invocation](https://docs.cloud.google.com/functions/docs/securing/authenticating) and [Enabling access to a function](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#enabling_access_to_a_function). 
  * To send notification data from Monitoring to Microsoft Teams, you must use an intermediary service such as Power Automate or [Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions). Configure the service to receive the Monitoring webhook notification, convert the data into a Teams-compatible format, and forward the data to the appropriate Microsoft Teams channel. 



#### Configure webhook notification channels

To configure webhook notifications, do the following:

  1. **The webhook handler** : Identify the public endpoint URL to receive webhook data from Monitoring.
  2. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  4. Click **Edit notification channels**.
  5. In the **Webhook** section, click **Add New**.
  6. Complete the dialog.
  7. Click **Test Connection** to send a test payload to the webhook endpoint. You can go to the receiving endpoint to verify delivery.
  8. Click **Save**.



When you create an alerting policy, select **Webhook** in the **Notifications** section and choose your webhook configuration. The notifications sent by Error Reporting follow the [1.0 schema](https://docs.cloud.google.com/error-reporting/docs/notifications#webhooks), whereas notifications sent by Monitoring follow the 1.2 schema:

#### JSON examples

By default, the alerting backend attempts to generate a JSON packet with version 1.2 formatting. For more information about this formatting, see the next section.

The following is an example of such a packet:
    
    
    {
      "incident": {
        "incident_id": "0.opqiw61fsv7p",
        "renotify": true,
        "scoping_project_id": "internal-project",
        "scoping_project_number": 12345,
        "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.lxfiw61fsv7p?project=internal-project",
        "severity": "no severity",
        "started_at": 1577840461,
        "ended_at": 1577877071,
        "state": "closed",
        "resource_id": "11223344",
        "resource_name": "internal-project gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_display_name": "gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_type_display_name": "VM Instance",
        "resource": {
          "type": "gce_instance",
          "labels": {
            "instance_id": "11223344",
            "project_id": "internal-project",
            "zone": "us-central1-c"
          }
        },
        "metric": {
          "type": "compute.googleapis.com/instance/cpu/utilization",
          "displayName": "CPU utilization",
          "labels": {
            "instance_name": "the name of the VM instance"
          }
        },
        "metadata": {
          "system_labels": { "labelkey": "labelvalue" },
          "user_labels": { "labelkey": "labelvalue" }
        },
        "policy_name": "Monitor-Project-Cluster",
        "policy_user_labels" : {
            "user-label-1" : "important label",
            "user-label-2" : "another label"
        },
        "condition_name": "VM Instance - CPU utilization [MAX]",
        "threshold_value": "0.9",
        "observed_value": "0.835",
        "condition": {
          "name": "projects/internal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789",
          "displayName": "VM Instance - CPU utilization [MAX]",
          "conditionThreshold": {
            "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\" metadata.system_labels.\"state\"=\"ACTIVE\"",
            "aggregations": [
              {
                "alignmentPeriod": "120s",
                "perSeriesAligner": "ALIGN_MEAN"
              }
            ],
            "comparison": "COMPARISON_GT",
            "thresholdValue": 0.9,
            "duration": "0s",
            "trigger": {
              "count": 1
            }
          }
        },
        "documentation": {
          "content": "TEST ALERT\n\npolicy.name=projects/internal-project/alertPolicies/1234567890123456789\n\npolicy.display_name=Monitored-Project-NO-GROUPBY\n\ncondition.name=projects/nternal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789\n\ncondition.display_name=VM Instance - CPU utilization [MAX]\n\nproject=internal-project\n\nresrouce.project=internal-project \n\nDONE\n",
          "mime_type": "text/markdown",
          "subject": "ALERT - No severity",
          "links": [
            {
              "displayName": "Playbook",
              "url": "https://myownpersonaldomain.com/playbook?name=${resource.name}"
            }
          ]
        },
        "summary": "CPU utilization for internal-project gke-cluster-1-16-default-pool-e2df4cbd-dgp3 with metric labels {instance_name=gke-cluster-1-default-pool-e2df4cbd-dgp3} and system labels {state=ACTIVE} returned to normal with a value of 0.835."
      },
      "version": "1.2"
    }
    

#### Schema structure, version 1.2

This section describes version 1.2 of the payload schema. Some fields might not appear in all returned packets or might have empty values, depending on the configuration of the alerting policy, the state of the incident, or the resource being monitored. Some fields take embedded structures as values; these structures are described by reference because their contents can also vary.

In a returned packet, the fields can occur in any order. In the description that follows, they are organized into related groups.

`{`  
` **"version"** : "1.2",`  
` **"incident"** : {`  
` `  
` `Information about the incident.  
` `  
` **"incident_id"**`: string, generated ID for this incident.  
` **"renotify"**`: bool, optional. Set to `true` when the message is a repeated notification.  
` **"scoping_project_id"**`: string, the project ID that hosts the metrics scope.  
` **"scoping_project_number"**`: number, the project number of the scoping project.  
` **"url"**`: string, Google Cloud console URL for this incident.  
` **"started_at"**`: number, time (in Unix epoch seconds) when the incident was opened.  
` **"ended_at"**`: number, time (in Unix epoch seconds) when the incident was closed. Populated only when `state` is `closed`.  
` **"state"**`: string, state of the incident: `open` or `closed`. If `open`, then `ended_at` is null.  
` **"summary"**`: string, generated textual summary of the incident.  
` **"apigee_url"**`: string, [Apigee](https://docs.cloud.google.com/apigee/docs) URL for this incident, only for Apigee resource types [ `Environment` and `Proxy*`](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment).  
` **"observed_value"**`: string, observed value that triggered/resolved the alert, may be empty if the condition is expired.  
` `  
` `Information about the monitored resource for which the incident was opened.  
` `  
` **"resource"** : {`  
` **"type"**`: string, identifier of the monitored resource type being alerted on, for example, `gce_instance`; see [List of monitored resources](https://docs.cloud.google.com/monitoring/api/resources).  
` **"labels"**`: object, key-value pairs for labels associated with the monitored resource.  
` },`  
` **"resource_type_display_name"**`: string, display name of the monitored resource type.  
` **"resource_id"**`: string, instance ID of the monitored resource, same value as `resource.labels.instance_id`.  
` **"resource_display_name"**`: string, display name of the monitored resource.  
` **"resource_name"**`: string, generated name of this monitored resource; consists of values from other fields.  
` `  
` `Information about the metric type of the time-series data.  
` `  
` **"metric"** : {`  
` **"type"**`: string, identifier of the metric type being alerted on, for example, `compute.googleapis.com/instance/cpu/utilization`; see [List of metrics](https://docs.cloud.google.com/monitoring/api/metrics).  
` **"displayName"**`: string, display name of the metric type.  
` **"labels"**`: object, key-value pairs for labels associated with the metric.  
` },`  
` **"metadata"** : {`  
` **"system_labels"**`: object, key-value pairs for system metadata labels.  
` **"user_labels"**`: object, key-value pairs for user metadata labels.  
` },`  
` `  
` `Information about the alerting policy and condition that opened/resolved the incident.  
` `The values are drawn from the relevant [ `AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object.  
` `  
` **"policy_name"**`: string, display name for the alerting policy.  
` **"policy_user_labels"**`: object, key-value pairs for any user labels attached to the policy.  
` **"documentation"**`: object, an embedded structure of the form [ `Documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).  
` **"condition"**`: object, an embedded structure of the form [ `Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition).  
` **"condition_name"**`: string, display name of the condition, same value as `condition.displayName`.  
` **"severity"**`: string, severity level of incidents. If this field isn't defined during alerting policy creation, then Cloud Monitoring sets the alerting policy severity to `no severity`.  
` **"threshold_value"**`: string, the threshold value of this condition, may be empty if the condition isn't a threshold condition.  
` },`  
`}`  


#### Basic authentication

In addition to the webhook request sent by Cloud Monitoring, basic authentication utilizes the HTTP specification for the username and password. Cloud Monitoring requires your server to return a 401 response with the proper `WWW-Authenticate` header. For more information about basic authentication, see the following:

  * [RFC Specification](https://www.ietf.org/rfc/rfc2617.txt)
  * [Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)



#### Token authentication

Token authentication requires a query string parameter in the endpoint URL and a key that the server expects to be secret between itself and Monitoring. The following is a sample URL that includes a token:

`https://www.myserver.com/stackdriver-hook?auth_token=1234-abcd`

If Monitoring posts an alert to the endpoint URL, your server can validate the attached token. This method of authentication is most effective when used with SSL/TLS to encrypt the HTTP request, preventing unauthorized third parties from learning the token.

For an example server in Python, see this [sample server](https://gist.github.com/tschieggm/7604940).

#### Deprecation policy

The payload schema is subject to the Google Cloud deprecation policy outlined in Section 1.4(d) of the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms). Note that the schema does not control the formats of generated field values, and these formats can change without notice. For example, `incident.summary`, `incident.documentation.content`, and `incident.url` are meant to include data pertaining to their fields, but the schema doesn't have constraints to guarantee accurate parsing of these fields. You can consume the value as a whole and expect that it adheres to the deprecation policy, but don't rely on parsing the generated fields. 

###  Pub/Sub 

This section describes how to configure Pub/Sub notification channels. For redundancy, we recommend that you create multiple notification channels. Pairing Pub/Sub with Google Cloud console Mobile App, PagerDuty, webhooks, or Slack is recommended because Pub/Sub uses a different delivery mechanism.

If you configure a message storage policy or data residency restrictions for your topic, then Monitoring might not be able to publish to the topic. For more information, see [`FAILED_PRECONDITION` error](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#pubsub-failed-precondition). 

To configure a Pub/Sub notification channel, do the following:

  1. Enable required APIs and create a topic
  2. Configure the notification channel for a topic
  3. Authorize a service account
  4. Set the notification channel in an alerting policy



To understand the data schema, see Schema example.

To receive the alert notifications, you must also create one of the following subscriptions: [pull](https://docs.cloud.google.com/pubsub/docs/create-subscription), [push](https://docs.cloud.google.com/pubsub/docs/create-push-subscription), or [BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).

When the subscription is in a different project than the topic, create a service account in the subscriber project and grant it the role of [ `roles/pubsub.subscriber`](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber).

#### Before you begin

When you add the first Pub/Sub notification channel to a Google Cloud project, Cloud Monitoring creates a service account for that project. It also grants the Identity and Access Management role [Monitoring Notification Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) to the service account. This service account lets Monitoring send notifications to Pub/Sub-based notification channels in this project. 

The service account has the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com

The name of the notifications service account includes a unique Google Cloud project _number_. You can find the project name, ID, and number on the project's dashboard in the Google Cloud console, or you can retrieve the project number with the following command:
    
    
    gcloud projects describe PROJECT_ID --format="value(project_number)"

You can view and edit the service account by using the Google Cloud console or the Google Cloud CLI.

#### Enable required APIs and create a topic

In the Google Cloud project where you plan to create the notification channel and Pub/Sub topic, do the following: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Pub/Sub and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub.googleapis.com,monitoring.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Pub/Sub and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub.googleapis.com,monitoring.googleapis.com)

  8. Create a Pub/Sub topic. For information about how to create a topic, see [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic). For example, to create a topic called `notificationTopic` by using the Google Cloud CLI, run the following command: 
         
         gcloud pubsub topics create notificationTopic


**Note:** If you plan to create your notification channel and Pub/Sub topic in different Google Cloud projects, then ensure that you enable the Pub/Sub and Monitoring APIs in both projects.

Next, configure your Pub/Sub notification channels.

#### Configure notifications for a topic

To create a Pub/Sub notification channel, you can use the Monitoring API, the Google Cloud CLI, or the Google Cloud console. After you create the notification channel, authorize the notifications service account to publish to each topic that you are using as a notification channel.

For information about using the Monitoring API or the Google Cloud CLI to create the notification channel, see [Creating channels](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#api-create-channels).

To use the Google Cloud console to create the notification channel, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the Google Cloud project that contains the Pub/Sub topic you created.
  4. Click **Edit notification channels**.
  5. In the **Pub/Sub** section, click **Add New**.

The **Create Pub/Sub Channel** dialog displays the name of the service account that Monitoring created.

  6. Authorize the service account. Your service account can publish to all topics or to specific topics:

     * To publish to all topics, select **Manage roles** and add the role of **Pub/Sub Publisher**.

After you complete these steps that configure the notification channel, skip the next section, which is titled **Authorize service account** , and proceed to Set the notification channel in an alerting policy. 

     * To publish to specific topics, proceed to the next step and authorize the service account to publish specific topics after you complete configuring the notification channel. For instructions to authorize the service account, see Authorize service account. 
  7. Enter a display name for your channel and the Pub/Sub topic name.
  8. Optional: To verify that the channel is correctly configured, click **Send test notification**.
  9. Select **Add channel**.



Next, authorize the service account.

#### Authorize service account

**Note:** Complete this step when you create the notification channel by using the API or the Google Cloud CLI, and when you have skipped the authorization step when using the Google Cloud console.

Authorization lets the notifications service account publish to each Pub/Sub topic that you are using as a notification channel. This section describes how you can do the following: 

  * Authorize a service account for a specific topic.
  * Authorize a service account for all topics.



##### Authorize a service account for a specific topic

You can authorize a service account to publish to a specific topic by using the Google Cloud console or the Google Cloud CLI. This section describes both approaches.

To authorize your service account for a specific topic by using the Google Cloud console, do the following: 

  1. In the Google Cloud console, go to the **Topics** page: 

[Go to **Topics**](https://console.cloud.google.com/cloudpubsub/topicList)

If you use the search bar to find this page, then select the result whose subheading is **Pub/Sub**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the topic.
  4. In the **Permissions** tab, select **Add principal**.
  5. In the **New principal** field, enter the name of the notifications service account. The service account has the following naming convention: 
         
         service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com

  6. Select the role **Pub/Sub Publisher** , and then select **Save**.



To authorize your service account for a specific topic by using the Google Cloud CLI, grant the `pubsub.publisher` IAM role for the topic to the service account. For example, the following command configures the IAM role for the `notificationTopic` topic:
    
    
    gcloud pubsub topics add-iam-policy-binding \
    projects/PROJECT_NUMBER/topics/notificationTopic --role=roles/pubsub.publisher \
    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
     

A response to a successful execution of the `add-iam-policy-binding` command is similar to the following:
    
    
     Updated IAM policy for topic [notificationTopic].
     bindings:
     ‐ members:
        ‐ serviceAccount:service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com
        role: roles/pubsub.publisher
     etag: BwWcDOIw1Pc=
     version: 1
     

For more information, see the `pubsub topics add-iam-policy-binding` [reference page](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/add-iam-policy-binding).

##### Authorize a service account for all topics

To authorize your service account for all topics, do the following: 

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select **Include Google-provided role grants** as shown in the following image:  
![Select the Include Google-provided role grants option.](https://docs.cloud.google.com/static/monitoring/images/check-include-google-provided-role-grants.png)
  4. Search for the service account that has the following format: 
         
         service-PROJECT_NUMBER@gcp-sa-monitoring-notification.iam.gserviceaccount.com

Reload the page when the service account isn't listed.

  5. Select _edit_ **Edit** for the notifications service account, select **Add another role** , and then add the role **Pub/Sub Publisher**. 



Next, set the notification channel in an alerting policy.

#### Set the notification channel in an alerting policy 

To use a Pub/Sub notification channel in an alerting policy, select **Pub/Sub** as the channel type, and then select the topic.

#### Schema example

To view an example JSON packet and the schema, expand the following sections.

#### JSON examples

By default, the alerting backend attempts to generate a JSON packet with version 1.2 formatting. For more information about this formatting, see the next section.

The following is an example of such a packet:
    
    
    {
      "incident": {
        "incident_id": "0.opqiw61fsv7p",
        "renotify": true,
        "scoping_project_id": "internal-project",
        "scoping_project_number": 12345,
        "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.lxfiw61fsv7p?project=internal-project",
        "severity": "no severity",
        "started_at": 1577840461,
        "ended_at": 1577877071,
        "state": "closed",
        "resource_id": "11223344",
        "resource_name": "internal-project gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_display_name": "gke-cluster-1-default-pool-e2df4cbd-dgp3",
        "resource_type_display_name": "VM Instance",
        "resource": {
          "type": "gce_instance",
          "labels": {
            "instance_id": "11223344",
            "project_id": "internal-project",
            "zone": "us-central1-c"
          }
        },
        "metric": {
          "type": "compute.googleapis.com/instance/cpu/utilization",
          "displayName": "CPU utilization",
          "labels": {
            "instance_name": "the name of the VM instance"
          }
        },
        "metadata": {
          "system_labels": { "labelkey": "labelvalue" },
          "user_labels": { "labelkey": "labelvalue" }
        },
        "policy_name": "Monitor-Project-Cluster",
        "policy_user_labels" : {
            "user-label-1" : "important label",
            "user-label-2" : "another label"
        },
        "condition_name": "VM Instance - CPU utilization [MAX]",
        "threshold_value": "0.9",
        "observed_value": "0.835",
        "condition": {
          "name": "projects/internal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789",
          "displayName": "VM Instance - CPU utilization [MAX]",
          "conditionThreshold": {
            "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\" metadata.system_labels.\"state\"=\"ACTIVE\"",
            "aggregations": [
              {
                "alignmentPeriod": "120s",
                "perSeriesAligner": "ALIGN_MEAN"
              }
            ],
            "comparison": "COMPARISON_GT",
            "thresholdValue": 0.9,
            "duration": "0s",
            "trigger": {
              "count": 1
            }
          }
        },
        "documentation": {
          "content": "TEST ALERT\n\npolicy.name=projects/internal-project/alertPolicies/1234567890123456789\n\npolicy.display_name=Monitored-Project-NO-GROUPBY\n\ncondition.name=projects/nternal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789\n\ncondition.display_name=VM Instance - CPU utilization [MAX]\n\nproject=internal-project\n\nresrouce.project=internal-project \n\nDONE\n",
          "mime_type": "text/markdown",
          "subject": "ALERT - No severity",
          "links": [
            {
              "displayName": "Playbook",
              "url": "https://myownpersonaldomain.com/playbook?name=${resource.name}"
            }
          ]
        },
        "summary": "CPU utilization for internal-project gke-cluster-1-16-default-pool-e2df4cbd-dgp3 with metric labels {instance_name=gke-cluster-1-default-pool-e2df4cbd-dgp3} and system labels {state=ACTIVE} returned to normal with a value of 0.835."
      },
      "version": "1.2"
    }
    

#### Schema structure, version 1.2

This section describes version 1.2 of the payload schema. Some fields might not appear in all returned packets or might have empty values, depending on the configuration of the alerting policy, the state of the incident, or the resource being monitored. Some fields take embedded structures as values; these structures are described by reference because their contents can also vary.

In a returned packet, the fields can occur in any order. In the description that follows, they are organized into related groups.

`{`  
` **"version"** : "1.2",`  
` **"incident"** : {`  
` `  
` `Information about the incident.  
` `  
` **"incident_id"**`: string, generated ID for this incident.  
` **"renotify"**`: bool, optional. Set to `true` when the message is a repeated notification.  
` **"scoping_project_id"**`: string, the project ID that hosts the metrics scope.  
` **"scoping_project_number"**`: number, the project number of the scoping project.  
` **"url"**`: string, Google Cloud console URL for this incident.  
` **"started_at"**`: number, time (in Unix epoch seconds) when the incident was opened.  
` **"ended_at"**`: number, time (in Unix epoch seconds) when the incident was closed. Populated only when `state` is `closed`.  
` **"state"**`: string, state of the incident: `open` or `closed`. If `open`, then `ended_at` is null.  
` **"summary"**`: string, generated textual summary of the incident.  
` **"apigee_url"**`: string, [Apigee](https://docs.cloud.google.com/apigee/docs) URL for this incident, only for Apigee resource types [ `Environment` and `Proxy*`](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/Environment).  
` **"observed_value"**`: string, observed value that triggered/resolved the alert, may be empty if the condition is expired.  
` `  
` `Information about the monitored resource for which the incident was opened.  
` `  
` **"resource"** : {`  
` **"type"**`: string, identifier of the monitored resource type being alerted on, for example, `gce_instance`; see [List of monitored resources](https://docs.cloud.google.com/monitoring/api/resources).  
` **"labels"**`: object, key-value pairs for labels associated with the monitored resource.  
` },`  
` **"resource_type_display_name"**`: string, display name of the monitored resource type.  
` **"resource_id"**`: string, instance ID of the monitored resource, same value as `resource.labels.instance_id`.  
` **"resource_display_name"**`: string, display name of the monitored resource.  
` **"resource_name"**`: string, generated name of this monitored resource; consists of values from other fields.  
` `  
` `Information about the metric type of the time-series data.  
` `  
` **"metric"** : {`  
` **"type"**`: string, identifier of the metric type being alerted on, for example, `compute.googleapis.com/instance/cpu/utilization`; see [List of metrics](https://docs.cloud.google.com/monitoring/api/metrics).  
` **"displayName"**`: string, display name of the metric type.  
` **"labels"**`: object, key-value pairs for labels associated with the metric.  
` },`  
` **"metadata"** : {`  
` **"system_labels"**`: object, key-value pairs for system metadata labels.  
` **"user_labels"**`: object, key-value pairs for user metadata labels.  
` },`  
` `  
` `Information about the alerting policy and condition that opened/resolved the incident.  
` `The values are drawn from the relevant [ `AlertPolicy`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy) object.  
` `  
` **"policy_name"**`: string, display name for the alerting policy.  
` **"policy_user_labels"**`: object, key-value pairs for any user labels attached to the policy.  
` **"documentation"**`: object, an embedded structure of the form [ `Documentation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation).  
` **"condition"**`: object, an embedded structure of the form [ `Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition).  
` **"condition_name"**`: string, display name of the condition, same value as `condition.displayName`.  
` **"severity"**`: string, severity level of incidents. If this field isn't defined during alerting policy creation, then Cloud Monitoring sets the alerting policy severity to `no severity`.  
` **"threshold_value"**`: string, the threshold value of this condition, may be empty if the condition isn't a threshold condition.  
` },`  
`}`  


#### Deprecation policy

The payload schema is subject to the Google Cloud deprecation policy outlined in Section 1.4(d) of the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms). Note that the schema does not control the formats of generated field values, and these formats can change without notice. For example, `incident.summary`, `incident.documentation.content`, and `incident.url` are meant to include data pertaining to their fields, but the schema doesn't have constraints to guarantee accurate parsing of these fields. You can consume the value as a whole and expect that it adheres to the deprecation policy, but don't rely on parsing the generated fields. 

###  Google Chat 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Google Cloud Monitoring app allows your Google Chat spaces to receive notifications.

#### Before you begin

If you are in an organization, then to install the Google Cloud Monitoring app, you must have access to the Google Cloud Monitoring app. If you don't have access, then request that a Google Workspace administrator do the following:

  1. [Add the app to the Marketplace apps allowlist and enable access at the top organizational unit](https://support.google.com/a/answer/6089179).
  2. [Configure Marketplace app user install settings so that users can install the app](https://support.google.com/a/answer/172931).



#### Install the Google Cloud Monitoring app

You must use the following procedure to install the Google Cloud Monitoring app. Installation from the [Google Workspace Marketplace listing](https://workspace.google.com/marketplace/app/google_cloud_monitoring/642447156236) isn't supported.

To install the app and configure a space as a notification channel, do the following:

  1. In Google Chat, open or create the space where you want to receive notifications.

  2. Install the Google Cloud Monitoring app:

     1. Select your space name and then select **Apps and Integrations**.

     2. If the Google Cloud Monitoring app doesn't appear in the Apps list, then return to your space, enter `@Google Cloud Monitoring`, and then press **Enter**.

     3. Click **Add to space**.

  3. Copy the chat space ID to your clipboard.

If you installed the Google Cloud Monitoring app, then the chat space ID is included in the installation confirmation. Otherwise, you can find the chat space ID as the series of numbers and letters following `space/` at the end of your chat space URL.

  4. Open a new browser tab and then configure the notification channel:

     1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

     3. Click **Edit notification channels**.

     4. Go to the **Google Chat** section and click **Add New**.

     5. Enter your chat space ID in the **Chat Space ID** field and then click **Save**.


**Note:** You can't view or manage the alert by using the Google Cloud Monitoring app. To acknowledge the alert or snooze the related alerting policy, use the Google Cloud console, the Google Cloud CLI, or the Cloud Monitoring API.

### Create a channel on demand

When adding a notification channel to an alerting policy, you must select a channel from a list. To update the list of options when you are creating an alerting policy, use the following process:

  1. In the notification dialog, click **Manage Notification Channels**. You're taken to the **Notification channels** window in a new browser tab.
  2. To add a new notification channel, locate the channel type, click **Add new** , and then follow the channel-specific instructions contained in the previous table.
  3. Return to the original tab, and in the notification dialog, click _refresh_ **Refresh**.

![Notification dialog displaying the refresh and manage channels buttons.](https://docs.cloud.google.com/static/monitoring/images/notification-dialog-with-buttons.png)

  4. Select the notification channel from the updated list.




### Get notified on an unsupported channel

If your preferred notification channel isn't supported, consider creating a pipeline that relies on sending your notifications to Pub/Sub. For a Python example that uses Flask, see [Creating custom notifications with Cloud Monitoring and Cloud Run](https://cloud.google.com/blog/products/operations/write-and-deploy-cloud-monitoring-alert-notifications-to-third-party-services). For other examples, see the [cloud-alerting-notification-forwarding Git repository](https://github.com/googlecloudplatform/cloud-alerting-notification-forwarding).

## Test a notification channel

Cloud Monitoring doesn't support a test option for notification channels. However, you can verify that a notification channel is properly configured by creating an alerting policy and configuring the condition to be met.

To manually test your notification channels, you can create an alerting policy that monitors the CPU utilization of one of your virtual machine (VM) instances:

  1. Optional: If you don't have a VM in your Google Cloud project yet or want to use a different VM for testing, then create a VM:

     1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

     2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
     3. Select **Create instance** , and then configure your VM. For more information about creating VMs, see [Create a VM instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage).
  2. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

  4. Select **Create policy**.

  5. Use the **Select a metric** menu to select the **CPU Utilization** metric for a VM instance.

  6. Click **Add filter** and add a filter for your VM.

  7. Update the **Configure trigger** fields as follows:

     1. Select **Below threshold** for the **Threshold position** field.
     2. Select a value that is larger than the CPU utilization for your instance. or example, if the chart shows a CPU utilization of about 5%, then set the threshold to 10%.

These settings configure the condition to be met when the CPU utilization of a VM instance is less than the specified threshold. Because you selected a threshold that is larger than the CPU utilization of your VM instance, the condition of the alerting policy is met.

  8. Add the notification channels to your policy.

  9. Expand **Alert autoclose duration** and select **30 min**.

  10. Enter a policy name and click **Create policy**.

  11. After the condition is met, verify that you receive a notification on each notification channel.

  12. Delete the alerting policy. The alert is closed automatically after the autoclose duration expires.

  13. If you created a VM instance for this test, then delete it.




If you aren't receiving expected notifications, then you can search the Logs Explorer for log entries with information about the missing notifications. For more information, see [Notifications aren't received](https://docs.cloud.google.com/monitoring/alerts/troubleshoot-missing-notifications#no-notifications).

## Edit and delete notification channels

To edit or delete a notification channel by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Edit notification channels**.

The **Notification channels** dashboard contains a section for each type of notification channel. Each section lists all configurations for that type:

     * To modify an entry, click _edit_ **Edit**. Click **Save** after your changes are complete.
     * To delete an entry, click delete **Delete**. Click **Delete** in the confirmation dialog.

**Note:** You can't delete a notification channel by using the Google Cloud console when the channel is associated with an alerting policy. However, you can delete the channel by using the Google Cloud CLI or the Cloud Monitoring API. For more information, see [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api).

## View notification channel logs

You can use the Logs Explorer to view notification channel errors:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Enter and run your query. For queries specific to notification channel errors, see [Cloud Monitoring queries](https://docs.cloud.google.com/logging/docs/view/query-library#monitoring-filters).



## What's next

For information about alerts, see the following documents:

  * [Alerts for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events)
  * [Alerts for log-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/log-based-incidents)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
