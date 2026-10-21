---
url: https://docs.cloud.google.com/managed-lustre/docs/maintenance/
title: Maintenance events and policies \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:28:15.568681+00:00
---

# Maintenance events and policies  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Maintenance events and policies Stay organized with collections  Save and categorize content based on your preferences. 

To keep your Google Cloud Managed Lustre instances up-to-date, Google Cloud periodically performs maintenance on them. Maintenance events can include updates to the underlying software or infrastructure. These events may cause a temporary downtime, during which I/O operations to the instance may stop responding. Affected I/O operations resume once maintenance is complete. Downtime is typically between 2 to 25 minutes.

While maintenance is in progress, an instance's status is `UPGRADING`. Once maintenance has completed, the instance returns to `ACTIVE` status.

_Maintenance policies_ allow you to control when these maintenance events occur. You can configure a maintenance policy for each instance to specify windows for maintenance and periods where maintenance should be excluded. If no maintenance policy is configured on an instance, maintenance can occur at any time.

You can also reschedule a maintenance event so that it starts immediately, during the next available window, or at a specific time up to 28 days later.

## About maintenance policies

You can configure a maintenance policy on each Managed Lustre instance. A maintenance policy includes the following:

  * **Weekly maintenance window** : A recurring one-hour window during the week when it is acceptable for Managed Lustre to start a maintenance event.
  * **Maintenance exclusion window** : A period during which Managed Lustre is not allowed to start a maintenance event. You can define one exclusion window per instance, with a maximum duration of two weeks. If no year is specified in the start and end dates, the exclusion window recurs annually.



An exclusion window takes precedence over a regular maintenance window. If a scheduled event falls within this period, Managed Lustre defers the event to the next available window or skips it entirely. The update is applied during the next maintenance cycle.

## Maintenance notifications

You can subscribe to email notifications for upcoming maintenance events to help you plan for any potential disruption. Subscriptions to maintenance notifications are managed through your Google Cloud console Communication page:

[Go to the **Communication** page](https://console.cloud.google.com/user-preferences/communication)

Once subscribed, the following notifications are sent:

  * **Advance notification** : Sent 7 to 14 days before a scheduled maintenance event, or after a maintenance event has been rescheduled by the customer.
  * **Canceled** : Sent if a scheduled maintenance event is canceled by Google or rescheduled by the customer.
  * **In progress** : Sent when a maintenance event starts.
  * **Completed** : Sent when a maintenance event is completed.



You can also view upcoming maintenance schedules on the instance details page in the Google Cloud console or you can use Cloud Logging to view maintenance logs.

## Configure a maintenance window

A maintenance window requires a day of the week and a UTC start time for the one-hour window.

###  Google Cloud console 

To configure a maintenance window when creating an instance, see [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

###  gcloud 

Create an instance with a maintenance window by specifying the `--maintenance-policy-weekly-windows` flag:
    
    
    gcloud lustre instances create INSTANCE_ID \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY_GIB \
      --filesystem=FS_NAME \
      --location=LOCATION \
      --network=NETWORK_PATH \
      --maintenance-policy-weekly-windows='dayOfWeek=DAY,startTime={START_TIME}'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * PER_UNIT_STORAGE_THROUGHPUT is the [performance tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. To specify the [Dynamic tier][dynamic-tier], set this to `0` and include the `--dynamic-tier-options-mode=DEFAULT_CACHE` flag.
  * CAPACITY: The capacity of your instance in GiB.
  * FS_NAME: The name of your file system.
  * LOCATION: The location of your Managed Lustre instance.
  * NETWORK_PATH: The full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).
  * DAY: The day of the week for the maintenance window (e.g., `TUESDAY`).
  * START_TIME: The UTC start time of the maintenance window in dictionary format (e.g., `{hours=1,minutes=0}`).



For more details about creating an instance, see [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

###  REST API 

To specify a maintenance window for an instance, include the `maintenancePolicy` object when creating an instance.

The following is an example of a `maintenancePolicy` object:
    
    
    "maintenancePolicy": {
      "weeklyMaintenanceWindows": [
        {
          "dayOfWeek": "DAY",
          "startTime": {
            "hours": HOURS,
            "minutes": MINUTES
          }
        }
      ]
    }
    

Replace the following:

  * DAY: The day of the week for the maintenance window (e.g., `TUESDAY`).
  * HOURS: The hour of the day for the maintenance window start time (e.g., `1`).
  * MINUTES: The minute of the hour for the maintenance window start time (e.g., `0`).



## Configure an exclusion window

To prevent maintenance from occurring during certain periods, such as holidays or business events, you can define one maintenance exclusion window in your maintenance policy. Exclusion windows can be up to two weeks long. To create an annually-recurring exclusion window, don't specify a year in the start and end dates.

You can combine a weekly maintenance window and an exclusion window in the same policy.

###  Google Cloud console 

To configure an exclusion window when creating an instance, see [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

###  gcloud 

Create an instance with an exclusion window by specifying the `--maintenance-policy-exclusion-window` flag:
    
    
    gcloud lustre instances create INSTANCE_ID \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY_GIB \
      --filesystem=FILESYSTEM \
      --location=LOCATION \
      --network=NETWORK_PATH \
      --maintenance-policy-exclusion-window='startDate={START_DATE},endDate={END_DATE},time={TIME}'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * PER_UNIT_STORAGE_THROUGHPUT is the [performance tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. To specify the [Dynamic tier][dynamic-tier], set this to `0` and include the `--dynamic-tier-options-mode=DEFAULT_CACHE` flag.
  * CAPACITY: The capacity of your instance in GiB.
  * FS_NAME: The name of your file system.
  * LOCATION: The location of your Managed Lustre instance.
  * NETWORK_PATH: The full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).
  * START_DATE: The start date of the maintenance exclusion window in dictionary format (e.g., `{day=08,month=06,year=2026}`). To recur annually, omit the `year` key.
  * END_DATE: The end date of the maintenance exclusion window in dictionary format (e.g., `{day=08,month=06,year=2026}`). To recur annually, omit the `year` key.
  * TIME: The UTC start and end time of the exclusion window in dictionary format (e.g., `{hours=1,minutes=0}`).



###  REST API 

The following is an example of a `maintenancePolicy` object with an exclusion window:
    
    
    "maintenancePolicy": {
      "maintenanceExclusionWindow": [
        {
          "startDate": {
            "day": START_DAY,
            "month": START_MONTH,
            "year": START_YEAR
          },
          "endDate": {
            "day": END_DAY,
            "month": END_MONTH,
            "year": END_YEAR
          },
          "time": {
            "hours": HOURS,
            "minutes": MINUTES
          }
        }
      ]
    }
    

Replace the following:

  * START_YEAR: The year of the exclusion window start date (e.g., `2026`). Omit this field and `END_YEAR` to create an annually-recurring window.
  * START_MONTH: The month of the exclusion window start date (e.g., `12`).
  * START_DAY: The day of the exclusion window start date (e.g., `24`).
  * END_YEAR: The year of the exclusion window end date (e.g., `2027`). Omit this field and `START_YEAR` to create an annually-recurring window.
  * END_MONTH: The month of the exclusion window end date (e.g., `1`).
  * END_DAY: The day of the exclusion window end date (e.g., `7`).
  * HOURS: The hour of the day for the exclusion window time (e.g., `0`).
  * MINUTES: The minute of the hour for the exclusion window time (e.g., `0`).



## Update a maintenance policy

To add or modify the maintenance policy for an existing instance:

###  Google Cloud console 

To update the maintenance policy for an instance, see [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  gcloud 

The following `gcloud` example updates the maintenance policy for an instance:
    
    
    gcloud lustre instances update INSTANCE_ID \
    --location=LOCATION \
    --maintenance-policy-weekly-windows='dayOfWeek=DAY,startTime={START_TIME}'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The location of your Managed Lustre instance.
  * DAY: The day of the week for the maintenance window (e.g., `TUESDAY`).
  * START_TIME: The UTC start time of the maintenance window in dictionary format (e.g., `{hours=1,minutes=0}`).



###  REST API 

To specify a maintenance window for an instance, include the `maintenancePolicy` object when updating an instance. You must also specify the `maintenancePolicy` in the `updateMask` query parameter.

The following `curl` example updates the maintenance policy for an instance:
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "maintenancePolicy": {
        "weeklyMaintenanceWindows": [
          {
            "dayOfWeek": "DAY",
            "startTime": {
              "hours": HOURS,
              "minutes": MINUTES
            }
          }
        ]
      }
    }' "https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=maintenancePolicy"
    

Replace the following:

  * PROJECT_ID: The ID of your Google Cloud project.
  * LOCATION The location of the Managed Lustre instance.
  * INSTANCE_ID The ID of the Managed Lustre instance.
  * DAY: The day of the week for the maintenance window (e.g., `TUESDAY`).
  * HOURS The hour of the day for the maintenance window start time (e.g., `3`).
  * MINUTES The minute of the hour for the maintenance window start time (e.g., `45`).



## Remove a maintenance policy

To remove a maintenance policy from an instance, clear all weekly maintenance windows and exclusion windows from the policy.

###  Google Cloud console 

To remove a maintenance policy from an instance, edit the instance and clear the maintenance policy fields. See [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  gcloud 

Use the `gcloud lustre instances update` command with the `--clear-maintenance-policy-weekly-windows` and `--clear-maintenance-policy-exclusion-window` flags:
    
    
    gcloud lustre instances update INSTANCE_ID \
    --location=LOCATION \
    --clear-maintenance-policy-weekly-windows \
    --clear-maintenance-policy-exclusion-window

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The location of your Managed Lustre instance.



###  REST API 

To remove a maintenance policy using the REST API, use the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) method with an empty `maintenancePolicy` object and the `updateMask` query parameter set to `maintenancePolicy`:
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "maintenancePolicy": {}
    }' "https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=maintenancePolicy"
    

Replace the following:

  * PROJECT_ID: The ID of your Google Cloud project.
  * LOCATION: The location of the Managed Lustre instance.
  * INSTANCE_ID: The ID of the Managed Lustre instance.



## View maintenance logs

Managed Lustre uses Cloud Logging to log maintenance events, including the following activity types:

  * `LustreAdvancedNotification`: Maintenance has been scheduled for the instance.
  * `LustreOngoingNotification`: Maintenance has started on the instance. Once complete, another `LustreOngoingNotification` event is logged, this time with `is_completed=true`.
  * `LustreCancelledNotification`: Maintenance has been canceled.



You can view maintenance logs using Logs Explorer or by using Google Cloud CLI.

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
     * LOCATION: The location of the Managed Lustre instance.
     * PROJECT_ID: The ID of your Google Cloud project.



###  gcloud CLI 

To view maintenance logs with Google Cloud CLI, run the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command:
    
    
    gcloud logging read 'resource.type="lustre.googleapis.com/Instance" resource.labels.instance_id="INSTANCE_ID" resource.labels.location="LOCATION" logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmaintenance"' --project=PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: The ID of the Managed Lustre instance.
  * `LOCATION`: The zone where the instance is located.
  * `PROJECT_ID`: The project ID of the project where the instance is located.



## Reschedule maintenance

If a scheduled maintenance event conflicts with your needs, you can reschedule it. When rescheduling, you have the following options:

  * **Immediately** : Reschedule the maintenance event to start as soon as possible. This option ignores any maintenance windows and exclusion windows that are configured on the instance.
  * **Next available window** : Reschedule the maintenance event to the next available maintenance window. This typically shifts the update by one week.
  * **By date** : Reschedule the maintenance event to a specific date and time. You can delay maintenance by a maximum of 28 days from the originally scheduled time. This option ignores any maintenance windows and exclusion windows that are configured on the instance.



To reschedule maintenance:

###  gcloud 

To start the maintenance event as soon as possible:
    
    
    gcloud lustre instances reschedule-maintenance INSTANCE_ID \
    --location=LOCATION \
    --reschedule-type=immediate

To reschedule maintenance to the next available window:
    
    
    gcloud lustre instances reschedule-maintenance INSTANCE_ID \
    --location=LOCATION \
    --reschedule-type=next-available-window

To reschedule maintenance to a specific time:
    
    
    gcloud lustre instances reschedule-maintenance INSTANCE_ID \
    --location=LOCATION \
    --reschedule-type=by-time \
    --reschedule-schedule-time=TIMESTAMP

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The location of your Managed Lustre instance.
  * TIMESTAMP: The start time in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format (for example, `2026-04-30T10:00:00Z`). This must be no later than 28 days from the originally scheduled time.



###  REST API 

Use the [`instances.rescheduleMaintenance`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/rescheduleMaintenance) method.

The following `curl` example starts the maintenance event as soon as possible:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "reschedule": {
        "rescheduleType": "IMMEDIATE"
      }
    }' "https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance"
    

The following `curl` example reschedules maintenance to the next available window:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "reschedule": {
        "rescheduleType": "NEXT_AVAILABLE_WINDOW"
      }
    }' "https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance"
    

The following `curl` example reschedules maintenance to a specific time:
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
      "reschedule": {
        "rescheduleType": "BY_TIME",
        "scheduleTime": "TIMESTAMP"
      }
    }' "https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance"
    

Replace the following:

  * PROJECT_ID: The ID of your Google Cloud project.
  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The location of your Managed Lustre instance.
  * TIMESTAMP: The start time in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format (for example, `2026-04-30T10:00:00Z`). This must be no later than 28 days from the originally scheduled time.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
