---
url: https://docs.cloud.google.com/looker/docs/looker-core-maintenance/
title: Manage maintenance policies for a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:19:57.639199+00:00
---

# Manage maintenance policies for a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Manage maintenance policies for a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

Once per month, Looker (Google Cloud core) schedules maintenance periods during which your instance will be upgraded. During a maintenance period, your instance will be restarted and you will be temporarily unable to access your instance. You can specify a maintenance window for your instance in the form of a day of the week and time of day during which maintenance will take place. If you don't specify a preferred maintenance window, upgrades will take place within two weeks of the rollout of a new Looker (Google Cloud core) version. You can also specify a **Deny Maintenance Period** to block maintenance from taking place during the time that you specified.

If you specify a **Deny Maintenance Period** during which Looker (Google Cloud core) instances are being upgraded to the next supported Looker version, the features that are available in your Looker (Google Cloud core) instance may differ from the settings that the Google Cloud console states are available in the upgraded release.

**Note:** Downtime associated with maintenance doesn't apply towards the Looker (Google Cloud core) Service Level Agreement.

This documentation page discusses finding information about scheduled maintenance, setting a preferred window for maintenance, specifying a maintenance deny period, and configuring notifications about upcoming maintenance updates for a Looker (Google Cloud core) instance.

## Release channels and maintenance policies

**Note:** The release channels feature is in [preview](https://cloud.google.com/products#product-launch-stages).

If a Looker (Google Cloud core) instance is enrolled in a [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels), the maintenance settings that you can configure depend on your instance's release channel:

  * **Rapid channel** : Maintenance windows and deny maintenance periods are **not supported**. If you enroll in the Rapid channel, any maintenance windows or deny maintenance periods that were previously set for the instance will be removed.
  * **Regular channel** : You can specify a preferred maintenance window and a deny maintenance period.
  * **No channel** : You can specify a preferred maintenance window and a deny maintenance period.



## Required role

To get the permissions that you need to configure maintenance settings for a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Maintenance settings

Looker (Google Cloud core) lets you configure maintenance updates through a set of maintenance settings.

You can configure maintenance to be scheduled at times when brief downtime causes the lowest impact to your instance. You can configure the following:

  * **Maintenance Window**: The day of the week and the hour in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour.

  * **Deny Maintenance Period**: A block of days in which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.




You can update maintenance policies when you [create your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) or by [editing the configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit) for an existing instance.

## Set a preferred window for maintenance

**Important:** Security upgrades may be applied outside of a preferred maintenance window and may take place without notifications.

To specify a preferred window during which Looker (Google Cloud core) will schedule maintenance, select one of the following options:

### console

  1. In the Google Cloud console, [create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) or [edit the configuration for an existing Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit).

  2. Under **Maintenance Window** , in the **Preferred Maintenance** section, configure the following settings for the maintenance window:

     * **Day** : The day of the week on which your instance will be updated

     * **Time window** : The approximate time of the day that the instance maintenance will begin

**Note:** Maintenance of your instance will start within an hour of the start time that you specified and will take approximately one hour.
  3. Click **Save**.




If you have enrolled your instance in the Rapid release channel, this option won't be available in the Google Cloud console.

### gcloud

Use the `gcloud looker instances create` command if you're creating the instance, or use the `gcloud looker instances update` command if you're updating the instance, and include the following parameters:
    
    
    --maintenance-window-day=MAINTENANCE_WINDOW_DAY
    --maintenance-window-time=MAINTENANCE_WINDOW_TIME
    

Replace the following:

  * `MAINTENANCE_WINDOW_DAY`: the day of the week on which your instance will be updated. Must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`.
  * `MAINTENANCE_WINDOW_TIME`: the start time of the maintenance window in UTC 24-hour format (for example, `13:00`, `17:45`).



If you have enrolled a Looker (Google Cloud core) instance in the Rapid channel of the [release channels](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) preview feature, you won't be able to set a maintenance window for that instance.

Once you have specified a maintenance window, your changes to the setting will take up to a week to take effect.

## Configure a deny maintenance period

If you want to defer the scheduled maintenance to a later time, you can change the instance's deny maintenance period. A deny maintenance period can be up to 60 days long.

You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.

**Important:** Security upgrades may be applied during a deny maintenance period and may take place without notifications.

To specify a preferred window during which Looker (Google Cloud core) won't perform maintenance, select one of the following options:

### console

  1. In the Google Cloud console, [create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create), or [edit the configuration for an existing Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit).

  2. Under the **Deny Maintenance Period** section, configure the following settings for the deny maintenance period:



  * **Start date** : Choose the start date of the period during which maintenance won't occur.

  * **End date** : Choose the end date of the period during which maintenance won't occur.

  * **Start/End time** : Define the specific time at which the **Deny Maintenance Period** begins (on the date you specified for **Start date**) and ends (on the date you specified for **End date**).



  1. Click **Save**.



If you have enrolled your instance in the Rapid release channel, this option won't be available in the Google Cloud console.

### gcloud

Use the `gcloud looker instances create` command if you're creating the instance, or use the `gcloud looker instances update` command if you're updating the instance, and include the following parameters:
    
    
    --deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
          --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
          --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME
    

Replace the following:

  * `DENY_MAINTENANCE_PERIOD_START_DATE`: the start date of the deny period in `YYYY-MM-DD` format.
  * `DENY_MAINTENANCE_PERIOD_END_DATE`: the end date of the deny period in `YYYY-MM-DD` format.
  * `DENY_MAINTENANCE_PERIOD_TIME`: the start and end time in UTC 24-hour format (for example, `13:00`, `17:45`).



If you have enrolled a Looker (Google Cloud core) instance in the Rapid channel of the [release channels](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) preview feature, you won't be able to set a deny maintenance period for that instance.

## Maintenance example

As an example, you can set your production instance's maintenance settings as follows:

  * **Maintenance Window** : Sundays between 12:00 AM and 1:00 AM ET
  * **Deny Maintenance Period** : December 1 at 10:00 PM through January 15 at 10:00 PM



## Upcoming maintenance notifications

**Important:** Security upgrades may take place without notifications, even if you turn on maintenance notifications.

You can have a notification about upcoming maintenance sent to your email up to one week before maintenance is scheduled. If you want to set an email filter for notifications, the email title is **[Looker (Google Cloud core) Advanced Maintenance Notification] Your instance is scheduled for maintenance.**

Maintenance notifications aren't sent out by default. If you want to be notified about an upcoming maintenance update, you must complete both these steps:

  1. Set a maintenance window.
  2. Opt in to maintenance notifications at the project level, or set up log-based alerts.
  3. To receive notification about your scheduled maintenance, you need to complete both steps at least seven days before the next scheduled maintenance update for your Looker (Google Cloud core) instance.



Notifications that are configured through the Google Cloud console are sent to the email address that's associated with your Google Account. You can use a custom email alias (such as a team email alias).

If your Looker (Google Cloud core) instance uses SAML or OpenID Connect (OIDC) for authentication, or if you want to route notifications to third-party communication channels such as Slack, PagerDuty, or custom webhooks, you can set up log-based alerts.

You can opt into maintenance notifications for all Looker (Google Cloud core) instances that have maintenance windows in a given project. You receive one notification per instance.

### Opt in to maintenance notifications

**Note:** Even if you turn on maintenance notifications, you don't receive notifications unless you set a maintenance window for that instance.

To turn on maintenance notifications in the Google Cloud console, follow these steps:

  1. Go to the **Communication** page in the Google Cloud console:

[Communication](https://console.cloud.google.com/user-preferences/communication)

  2. Select the **Product Notifications** tab.

  3. Select your project from the drop-down menu.

  4. In the row for Looker (Google Cloud core), set the email toggle to **ON**.




### Set up log-based alerts for maintenance events

If you authenticate to Google Cloud using Workforce Identity Federation, the Google Cloud console cannot send maintenance notifications to your federated accounts. Additionally, you might want to route notifications to services such as Slack, PagerDuty, or custom webhooks. To receive notifications in these scenarios, you can configure [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in Cloud Logging.

When Looker (Google Cloud core) schedules, starts, completes, or cancels a maintenance update, it writes an activity log entry to Logging. You can create alerting policies that match these log entries and send notifications to your configured [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

To create a log-based alert for a maintenance event, follow the instructions in the [Create a log-based alerting policy by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition) documentation to create an alerting policy. For examples of queries to use in the policy, see Maintenance log queries.

#### Maintenance log queries

Use the following queries to create log-based alerts for different stages of the maintenance lifecycle.

Replace `LOOKER_INSTANCE_NAME` with the name of your Looker (Google Cloud core) instance.

  * **Advance notification (scheduled)** : Notifies you when maintenance is scheduled for your instance.
        
        log_id("maintenance.googleapis.com/activity_log") AND
        resource.type = "gce_instance" AND
        labels.activity_type_name = "LookerRolloutAdvanced" AND
        labels.instance_id = "LOOKER_INSTANCE_NAME"
        

  * **Started notification** : Notifies you when maintenance begins on your instance.
        
        log_id("maintenance.googleapis.com/activity_log") AND
        resource.type = "gce_instance" AND
        labels.activity_type_name = "LookerRolloutInProgress" AND
        labels.is_completed = "false" AND
        labels.is_failed = "false" AND
        labels.instance_id = "LOOKER_INSTANCE_NAME"
        

  * **Completed notification (success)** : Notifies you when maintenance finishes successfully.
        
        log_id("maintenance.googleapis.com/activity_log") AND
        resource.type = "gce_instance" AND
        labels.activity_type_name = "LookerRolloutInProgress" AND
        labels.is_completed = "true" AND
        labels.is_failed = "false" AND
        labels.instance_id = "LOOKER_INSTANCE_NAME"
        

  * **Failed or canceled notification** : Notifies you if maintenance fails or is canceled.
        
        log_id("maintenance.googleapis.com/activity_log") AND
        resource.type = "gce_instance" AND
        (labels.is_failed = "true" OR labels.activity_type_name = "LookerRolloutCanceled") AND
        labels.instance_id = "LOOKER_INSTANCE_NAME"
        




## Find scheduled maintenance

If maintenance has been scheduled for your instance, you can view it by following these steps:

  1. Go to the **Looker (Google Cloud core)** page in the Google Cloud console.

  2. Select the name of the instance that you want to view scheduled maintenance for.

  3. When you [view configuration details for your instance](https://docs.cloud.google.com/looker/docs/looker-core-view-console), on the **Details** page, you can view the following information:

     * [**Maintenance Window**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#maintenance_window)
     * [**Scheduled Maintenance**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#scheduled_maintenance)
     * [**Deny Maintenance Period**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#deny_maintenance_period)
     * [**Last Deny Maintenance Period**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#last_deny_maintenance_period)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
