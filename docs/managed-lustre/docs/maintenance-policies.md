---
url: https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies/
title: Configure maintenance policies \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:30.226452+00:00
---

# Configure maintenance policies  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Configure maintenance policies Stay organized with collections  Save and categorize content based on your preferences. 

_Maintenance policies_ allow you to control when [automated maintenance events](https://docs.cloud.google.com/managed-lustre/docs/maintenance) occur on your Google Cloud Managed Lustre instances. You can configure a maintenance policy for each instance to define preferred weekly windows for updates and periods where maintenance should be excluded. If no maintenance policy is configured on an instance, automated maintenance can occur at any time.

If a scheduled maintenance event conflicts with your workload needs, you can also reschedule the maintenance event.

## About maintenance policies

You can configure a maintenance policy on each Managed Lustre instance. A maintenance policy includes the following:

  * **Weekly maintenance window** : A recurring one-hour window during the week when it is acceptable for Managed Lustre to start a maintenance event.
  * **Maintenance exclusion window** : A period during which Managed Lustre is not allowed to start a maintenance event. You can define one exclusion window per instance, with a maximum duration of two weeks. An exclusion window can recur annually.



An exclusion window overrides your weekly maintenance window. Google Cloud does not perform automated maintenance during an exclusion window, and will only schedule updates during a weekly maintenance window outside the exclusion period. If an exclusion window extends past the release cycle, Google Cloud skips that update, and the instance is updated during a future maintenance release cycle. You can still apply available updates at any time using [self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance).

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
      --maintenance-policy-weekly-windows='dayOfWeek=DAY,startTime=START_TIME'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * PER_UNIT_STORAGE_THROUGHPUT is the [performance tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. To specify the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier), set this to `0` and include the `--dynamic-tier-options-mode=DEFAULT_CACHE` flag.
  * CAPACITY_GIB: The capacity of your instance in GiB.
  * FS_NAME: The name of your file system.
  * LOCATION: The location of your Managed Lustre instance.
  * NETWORK_PATH: The full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).
  * DAY: The day of the week for the maintenance window, such as `TUESDAY`.
  * START_TIME: The UTC start time of the maintenance window in dictionary format, such as `{hours=1,minutes=0}`, including the curly braces.



For more details about creating an instance, see [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

###  REST 

To specify a maintenance window when creating an instance using the REST API, include the `maintenancePolicy` object in the request body:
    
    
    {
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
    }
    

Where:

  * DAY is the day of the week for the maintenance window, such as `TUESDAY`.
  * HOURS is the hour of the day for the maintenance window start time, such as `1`.
  * MINUTES is the minute of the hour for the maintenance window start time, such as `0`.



See the [`instances.create`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/create) API reference for more details.

## Configure an exclusion window

To prevent maintenance from occurring during certain periods, you can define a maintenance exclusion window up to two weeks in duration. To create an annually-recurring exclusion window, omit the year from the start and end dates.

You can combine a weekly maintenance window and an exclusion window in the same policy.

###  Google Cloud console 

To configure an exclusion window when creating an instance, see [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

###  gcloud 

Create an instance with an exclusion window by specifying the `--maintenance-policy-exclusion-window` flag:
    
    
    gcloud lustre instances create INSTANCE_ID \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY_GIB \
      --filesystem=FS_NAME \
      --location=LOCATION \
      --network=NETWORK_PATH \
      --maintenance-policy-exclusion-window='startDate=START_DATE,endDate=END_DATE,time=TIME'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * PER_UNIT_STORAGE_THROUGHPUT is the [performance tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) in MBps per TiB. Valid values are `0`, `125`, `250`, `500`, and `1000`. To specify the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier), set this to `0` and include the `--dynamic-tier-options-mode=DEFAULT_CACHE` flag.
  * CAPACITY_GIB: The capacity of your instance in GiB.
  * FS_NAME: The name of your file system.
  * LOCATION: The location of your Managed Lustre instance.
  * NETWORK_PATH: The full path of the VPC network to which the instance belongs, in the format `projects/PROJECT_ID/global/networks/NETWORK`. See [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).
  * START_DATE: The start date of the maintenance exclusion window in dictionary format, such as `{day=8,month=6,year=2026}`, including the curly braces. To recur annually, omit the `year` key.
  * END_DATE: The end date of the maintenance exclusion window in dictionary format, such as `{day=8,month=6,year=2026}`, including the curly braces. To recur annually, omit the `year` key.
  * TIME: The UTC start and end time of the exclusion window in dictionary format, such as `{hours=1,minutes=0}`, including the curly braces.



###  REST 

To specify an exclusion window when creating an instance using the REST API, include the `maintenancePolicy` object in the request body:
    
    
    {
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
    }
    

Where:

  * START_YEAR is the year of the exclusion window start date, such as `2026`. Omit this field and `END_YEAR` to create an annually-recurring window.
  * START_MONTH is the month of the exclusion window start date, such as `12`.
  * START_DAY is the day of the exclusion window start date, such as `24`.
  * END_YEAR is the year of the exclusion window end date, such as `2027`. Omit this field and `START_YEAR` to create an annually-recurring window.
  * END_MONTH is the month of the exclusion window end date, such as `1`.
  * END_DAY is the day of the exclusion window end date, such as `7`.
  * HOURS is the hour of the day for the exclusion window time, such as `0`.
  * MINUTES is the minute of the hour for the exclusion window time, such as `0`.



See the [`instances.create`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/create) API reference for more details.

## Update a maintenance policy

To add or modify the maintenance policy for an existing instance:

###  Google Cloud console 

To update the maintenance policy for an instance, see [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  gcloud 

The following `gcloud` example updates the maintenance policy for an instance:
    
    
    gcloud lustre instances update INSTANCE_ID \
    --location=LOCATION \
    --maintenance-policy-weekly-windows='dayOfWeek=DAY,startTime=START_TIME'

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The location of your Managed Lustre instance.
  * DAY: The day of the week for the maintenance window, such as `TUESDAY`.
  * START_TIME: The UTC start time of the maintenance window in dictionary format, such as `{hours=1,minutes=0}`, including the curly braces.



###  REST 

To update a maintenance policy using the REST API, send a `PATCH` request to the instance endpoint:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=maintenancePolicy
    Authorization: Bearer ACCESS_TOKEN
    
    {
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
    }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * INSTANCE_ID is the ID of the Managed Lustre instance.
  * DAY is the day of the week for the maintenance window, such as `TUESDAY`.
  * HOURS is the hour of the day for the maintenance window start time, such as `3`.
  * MINUTES is the minute of the hour for the maintenance window start time, such as `45`.



See the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) API reference for more details.

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



###  REST 

To remove a maintenance policy using the REST API, send a `PATCH` request to the instance endpoint with an empty `maintenancePolicy` object and the `updateMask` query parameter set to `maintenancePolicy`:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=maintenancePolicy
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "maintenancePolicy": {}
    }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * INSTANCE_ID is the ID of the Managed Lustre instance.



See the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) API reference for more details.

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
    --reschedule-type=immediately

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



###  REST 

To start the maintenance event as soon as possible:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "reschedule": {
        "rescheduleType": "IMMEDIATELY"
      }
    }
    

To reschedule maintenance to the next available window:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "reschedule": {
        "rescheduleType": "NEXT_AVAILABLE_WINDOW"
      }
    }
    

To reschedule maintenance to a specific time:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:rescheduleMaintenance
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "reschedule": {
        "rescheduleType": "BY_TIME",
        "scheduleTime": "TIMESTAMP"
      }
    }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * INSTANCE_ID is the ID of the Managed Lustre instance.
  * TIMESTAMP is the start time in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format, such as `2026-04-30T10:00:00Z`. This must be no later than 28 days from the originally scheduled time.



See the [`instances.rescheduleMaintenance`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/rescheduleMaintenance) API reference for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
