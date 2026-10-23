---
url: https://docs.cloud.google.com/memorystore/docs/memcached/find-and-set-maintenance-windows/
title: Find and set maintenance windows \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:53.133661+00:00
---

# Find and set maintenance windows  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/find-and-set-maintenance-windows/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Find and set maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions how to find scheduled maintenance, set maintenance windows, reschedule planned maintenance, and more. For an overview of maintenance updates and maintenance windows, see [Maintenance policy](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy).

## Set a preferred window for maintenance on an instance

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the instance ID of the instance you want to set a maintenance window for.

  3. Click **Edit**.

  4. Under the **Maintenance** section, select the desired day, time, and duration for the maintenance window. The time is set in your local time zone.

  5. Click **Save**.




### gcloud

Run the following command to set a maintenance window for a Memcached instance:
    
    
    gcloud memcache instances update INSTANCE_ID --region=REGION --maintenance-window-day=DAY --maintenance-window-start-time=START_TIME --maintenance-window-duration=DURATION
    

Where:

  * INSTANCE_ID is the ID of the instance.
  * REGION is the region where your instance is located.
  * DAY is the day you want maintenance to occur. Acceptable values are: `MONDAY`,`TUESDAY`,`WEDNESDAY`,`THURSDAY`,`FRIDAY`,`SATURDAY`,`SUNDAY`.
  * START_TIME is the hour of day (0 to 23) for the start of the maintenance window, in the UTC time zone.
  * DURATION is a window between 3 and 8 hours in length. Acceptable values are `3h` through `8h`, integers only.



For reference information, see [`gcloud memcached instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/update)

## Opt in to maintenance notifications

**Note:** Even if you turn on maintenance notifications, you do not receive notifications unless you [set a maintenance window](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#set_maintenance) for that instance.

To turn on maintenance notifications:

  1. Go to the **Communication** page in the Google Cloud console:

[Communication](https://console.cloud.google.com/user-preferences/communication)

  2. Click the **Product Notifications** tab.

  3. Select your project from the dropdown menu.

  4. In the row for Memorystore, toggle the email button to **ON**.




A maintenance notification email uses the title, `"Upcoming maintenance for your Cloud Memorystore instance [your-instance-name]"`. Each person who needs to needs to receive notifications must opt in separately.

Maintenance notifications are set at the project level rather than on instances. Email notifications are sent to the email address associated with your Google account. It is not possible to configure a custom email alias (for instance, a team email alias).

## Find scheduled maintenance

If maintenance has been scheduled for your instance, you can view it using the following instructions:

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the instance ID of the instance that you want to view scheduled maintenance for.

  3. Under the **Maintenance** section, you can view the date and time of any scheduled maintenance updates.




### gcloud
    
    
    gcloud memcache instances describe INSTANCE-ID --region=REGION
    

where:

  * INSTANCE_ID is the ID of the instance
  * REGION is the region where your instance is located



The output for scheduled maintenance is as follows:
    
    
    maintenancePolicy:
    createTime: 'TIME_STAMP'
    updateTime: 'TIME_STAMP'
    maintenanceWindow:
    - day: DAY
      duration: 180 minutes
      hour: HOUR
    maintenanceSchedule:
     endTime: 'TIME_STAMP'
     startTime: 'TIME_STAMP'
    

Where:

  * `maintenancePolicy` shows information on the creation time of your preferred maintenance policy and the last time the policy was updated.
  * `createTime` is when the maintenance policy is first created.
  * `updateTime` is when the maintenance policy was last updated.
  * `DAY` indicates the day of the week maintenance occurs.
  * `duration` indicates the length of the maintenance window in minutes.
  * `HOUR` indicates the hour in UTC time that maintenance begins.
  * `startTime` indicates the specific start time for a maintenance update that is scheduled for your instance.
  * `endTime` indicates the specific ending time for a maintenance update that is scheduled for your instance.
  * `TIME_STAMP` uses the RFC 3339 format.



## Reschedule planned maintenance

**Caution:** if you programmatically reschedule maintenance in bulk requests (not natively supported by Memorystore for Memcached), limit batch reschedule sizes to 100 instances per batch. For more information, see [Rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#rescheduling_maintenance).

To reschedule maintenance, see the instructions below:

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)

  2. Click the instance ID of the instance you want to reschedule maintenance for.

  3. Under the **Maintenance** section, click **RESCHEDULE**.

     * You can only reschedule maintenance if you [have a scheduled update](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#find_scheduled_maintenance), for your instance.
  4. Choose between **Update now** , **Defer to next scheduled window** , and **Custom day and time**. For more information, see the [overview of rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#rescheduling_maintenance).

     * If you want to update your instance immediately, select **Update now** and click **Update**.

     * If you want to delay the scheduled maintenance by one week, select **Defer to the next scheduled window** and click **Reschedule**.

     * If you want to designate a specific time, select **Custom day and time** , choose the new time, and click **Reschedule**.




### gcloud
    
    
    gcloud memcache instances reschedule-maintenance INSTANCE_ID --region=REGION --reschedule-type=RESCHEDULE_TYPE [--schedule-time=RESHEDULE_TIME]
    

where:

  * INSTANCE_ID is the ID of the instance
  * REGION is the region where your instance is located
  * RESCHEDULE_TYPE is the type of rescheduled update. Available values are:

    * `IMMEDIATE`: Starts the maintenance update immediately
    * `NEXT_AVAILABLE_WINDOW`: Defers maintenance until the next maintenance window. The next window is one week from the window in which maintenance was originally scheduled
    * `SPECIFIC_TIME`: Allows you to designate a specific time for the update. The rescheduled time must be no more than seven days from time of the original maintenance window
  * RESHEDULE_TIME You can only specify this value if you set `--reschedule-type` to `SPECIFIC TIME`. This value uses the ISO 1801 format. For example, `2020-01-16T16:56:00.000Z`. The time is set in UTC time.




For reference information, see [gcloud memcache instances reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/memcache).

## Manually applying maintenance updates

After you receive a notification of upcoming maintenance you have the option to apply the maintenance update to nodes manually. Manual maintenance is only available after a maintenance event is scheduled for your instance, and you must opt in to maintenance notifications and set a maintenance window to be informed of this upcoming maintenance. For more information, see [Manual maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#manual_maintenance).

#### Updating individual nodes in the Memcached cluster

To update individual nodes in your cluster, run the following command, replacing VARIABLES with appropriate values:
    
    
    
    gcloud beta memcache instances apply-software-update INSTANCE_NAME --node-ids=NODE_ID_1,NODE_ID_2 --region=REGION
    
    

#### Updating all nodes in the Memcached cluster

To update all nodes in your cluster, run the following command, replacing VARIABLES with appropriate values:
    
    
    
    gcloud beta memcache instances apply-software-update INSTANCE_NAME --apply-all --region=REGION
    
    

## Checking for available updates and verifying node updates

Signing up for maintenance notifications is the best way to learn when an update is available, but you can also use the command to below to manually check if maintenance is available. The following command also shows what nodes have been updated for your instance.
    
    
    gcloud memcache instances describe INSTANCE_NAME --region=REGION --format="table(updateAvailable.yesno(yes="YES",no="NO"),memcacheNodes:format='table(nodeId,updateAvailable.yesno(yes="YES", no="NO"))')"
    

## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/memcached/access-control#maintenance_policy_permissions) required to manage maintenance windows for your Memcached instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
