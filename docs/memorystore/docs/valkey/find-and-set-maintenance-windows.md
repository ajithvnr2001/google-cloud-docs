---
url: https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows/
title: Find and set maintenance windows \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:03:07.721892+00:00
---

# Find and set maintenance windows  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Find and set maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Valkey updates instances routinely by performing maintenance on them to ensure that the service is reliable, performant, secure, up-to-date, and has a zero downtime impact. In addition to Memorystore for Valkey performing maintenance on your instances, you can customize maintenance schedules to align with your application's needs and to minimize disruptions. To customize your maintenance schedules, you can configure maintenance windows for your instances.

This page provides instructions on how to complete the following tasks for customizing maintenance windows:

  * Create an instance with maintenance windows
  * Set a preferred window for maintenance
  * Turn on maintenance notifications
  * Find the scheduled maintenance
  * Reschedule maintenance
  * Remove a maintenance policy from an instance



For an overview of maintenance updates and maintenance windows, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).

## Create an instance with maintenance windows

You can create a Memorystore for Valkey instance with maintenance windows by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important:** Before following the steps in this section, complete the steps in the [Before you begin](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#before-you-begin) and [Set up networking](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#set-up-networking) sections.

### Console

To create an instance with maintenance windows, see [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

### gcloud

To create an instance with maintenance windows, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command:
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --psc-auto-connections=network=projects/PROJECT_ID/global/networks/NETWORK_ID \
    --shard-count=SHARD_COUNT \
    --maintenance-policy-weekly-window=day=DAY,startTime=hours=HOUR
    

Make the following replacements:

  * INSTANCE_ID: the ID of the Memorystore for Valkey instance that you're creating. The instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * PROJECT_ID: the project ID or number of the Google Cloud project where you want to create the instance.

  * REGION_ID: the region where you want the instance to be located.

**Note:** You can create instances only in the [supported regions](https://docs.cloud.google.com/memorystore/docs/valkey/locations#supported_regions) for Memorystore for Valkey.
  * NETWORK_ID: the ID of the network that you want to use to create the instance.

  * SHARD_COUNT: the number of shards in the instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * DAY: the day that you want maintenance to occur. Acceptable values are   
`MONDAY` \- `SUNDAY`.

  * HOUR: the hour of the day (in UTC time) when the maintenance window starts. Acceptable values are `0` \- `23`.




For example:
    
    
    gcloud memorystore instances create my-instance \
    --project=my-project \
    --location=us-central1 \
    --psc-auto-connections=network=projects/my-project/global/networks/default \
    --shard-count=8 \
    --maintenance-policy-weekly-window=day=MONDAY,startTime=hours=9
    

By default, when you create an instance with maintenance windows, [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) is deactivated and the authorized network is `default`.

## Set a preferred window for maintenance

You can set a maintenance window for a Memorystore for Valkey instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to set a preferred window.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Maintenance window** field, click **Edit** (_edit_).

If a day and time appear next to the field, then you already set the maintenance window for the instance.

  5. In the **Edit maintenance window** dialog, do the following:

     1. Select **Custom**.
     2. From the **Day** menu, select the day that you want maintenance to occur.
     3. From the **Time** menu, select the hour when you want the maintenance window to start.
     4. Click **Update instance**.



### gcloud

To set a maintenance window for an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command:
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --maintenance-policy-weekly-window=day=DAY,startTime=hours=HOUR
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance.
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the instance.
  * REGION_ID: the region where the instance is located.
  * DAY: the day that you want maintenance to occur. Acceptable values are   
`MONDAY` \- `SUNDAY`.
  * HOUR: the hour of the day (in UTC time) when the maintenance window starts. Acceptable values are `0` \- `23`.



## Turn on maintenance notifications

If you schedule maintenance for a Memorystore for Valkey instance, then you can use the Google Cloud console to turn on maintenance notifications for the instance.

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to turn on maintenance notifications.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

  4. Click **Edit notification preferences**.

If this link is deactivated, then you haven't scheduled maintenance for the instance.

  5. Click **Product Notifications**.

  6. From the menu, select your Google Cloud project.

  7. In the row for Memorystore, toggle the email button to **ON**.




A maintenance notification email uses this title: `"Upcoming maintenance for your Cloud Memorystore instance [your-instance-name]"`. Each email address that needs to receive notifications must opt in separately.

You set maintenance notifications at the project level rather than on instances. Memorystore for Valkey sends notifications to the email address associated with your Google Account. You can't configure a custom email alias (for example, a team email alias).

## Find the scheduled maintenance

If you schedule maintenance for a Memorystore for Valkey instance, then you can view the maintenance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to find the scheduled maintenance.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

Next to the **Maintenance window** field, the day and time of the scheduled maintenance appear.




### gcloud

To find the scheduled maintenance for an instance, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the instance
  * REGION_ID: the region where the instance is located



The output for scheduled maintenance is, as follows:
    
    
    maintenancePolicy:
      weeklyMaintenanceWindow:
      - day: DAY
          duration: 3600 seconds
      - startTime
           hour: HOUR
    maintenanceSchedule:
      endTime: 'END_DATE_AND_TIME_STAMP'
      scheduleDeadlineTime: 'SCHEDULED_DATE_AND_TIME_STAMP'
      startTime: 'START_DATE_AND_TIME_STAMP'
    

Where:

  * `maintenancePolicy` displays information about the creation time of the preferred maintenance policy.
  * `weeklyMaintenanceWindow` displays information about the weekly maintenance window for the instance. 
    * `DAY` is the day of the week when maintenance occurs.
    * `HOUR` is the hour (in UTC time) when maintenance begins.
  * `maintenanceSchedule` displays information about the scheduled maintenance for the instance. 
    * `END_DATE_AND_TIME_STAMP` indicates when a scheduled maintenance update ends for the instance.
    * `SCHEDULED_DATE_AND_TIME_STAMP` indicates when a maintenance update is scheduled to be completed for the instance.
    * `START_DATE_AND_TIME_STAMP` indicates when a scheduled maintenance update begins for the instance.



## Reschedule maintenance

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to reschedule maintenance for a Memorystore for Valkey instance. As a result, you can defer a maintenance update for up to two weeks from when the update is scheduled originally for the instance.

**Caution:** Although Memorystore for Valkey doesn't provide you with the option to reschedule maintenance for multiple instances at once, you can reschedule maintenance in bulk programmatically. If you reschedule in bulk, then batch your operations into appropriate-sized requests. We recommend that you limit the batch size to 100 instances and wait for ample time between requests. Otherwise, you might have failed rescheduling events. For more information, see [Scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#scheduled_maintenance).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to reschedule maintenance.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Upcoming maintenance** field, click **Edit** (_edit_).

If the **No maintenance scheduled right now** status appears next to this field, then maintenance isn't scheduled for the instance.

  5. In the **Reschedule upcoming maintenance** dialog, do the following:

     1. From the **Choose a new time** menu, select **Specific time**.
     2. From the **Date** field, click **Calendar** (_date_range_), and then select the date that you want maintenance to occur.
     3. From the **Time** menu, designate a specific time for the update. This time must be no more than 14 days from the time of the original maintenance window.
     4. Click **Reschedule**.

You can also use the **Reschedule upcoming maintenance** dialog to have Memorystore for Valkey perform maintenance on the instance immediately. From this dialog, select **Update now** from the **Choose a new time** menu, and then click **Update now**.




### gcloud

To reschedule maintenance for an instance, use the [`gcloud memorystore instances reschedule-maintenance`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance) command.
    
    
    gcloud memorystore instances reschedule-maintenance INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --reschedule-type=RESCHEDULE_TYPE [--schedule-time=RESCHEDULE_TIME]
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance.
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the instance.
  * REGION_ID: the region where the instance is located.
  * RESCHEDULE_TYPE: the type of rescheduled update. Available values are:

    * `IMMEDIATE`: start the maintenance update immediately.
    * `SPECIFIC_TIME`: designate a specific time for the update. This time must be no more than 14 days from the time of the original maintenance window.
  * RESCHEDULE_TIME: the date and time when Memorystore for Valkey reschedules the maintenance update.

**Note:** To specify a value for the RESCHEDULE_TIME parameter, you must set the RESCHEDULE_TYPE parameter to `SPECIFIC_TIME`. This value uses the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard (for example, `2025-02-16T16:56:00.000Z`). The time is set in UTC time.



## Remove a maintenance policy from an instance

If you no longer need a maintenance policy for a Memorystore for Valkey instance, and you want to use the service's default setting for maintenance instead, then you can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to remove the policy from the instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to remove a maintenance policy.

  3. On the **Instance at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Maintenance window** field, click **Edit** (_edit_).

If a day and time _don't_ appear next to the field, then you already removed the maintenance policy from the instance.

  5. In the **Edit maintenance window** dialog, do the following:

     1. Select **Default**.
     2. Click **Update instance**.



### gcloud

To remove a maintenance policy from an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --clear-maintenance-policy-weekly-window
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance from which you want to remove the maintenance policy
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the instance
  * REGION_ID: the region where the instance is located



## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/valkey/access-control#permissions_and_their_roles) that you need to manage maintenance windows for a Memorystore for Valkey instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
