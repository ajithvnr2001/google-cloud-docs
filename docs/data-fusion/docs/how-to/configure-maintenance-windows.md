---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-maintenance-windows/
title: Configure maintenance windows \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:21.132594+00:00
---

# Configure maintenance windows  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Configure maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Maintenance windows in Cloud Data Fusion let you control when automated updates and routine maintenance occur. Setting designated time frames helps you prevent service disruptions during peak operational hours.

Maintenance windows are supported for Cloud Data Fusion instances in versions 6.8.0 and later.

## About maintenance windows

A maintenance window in Cloud Data Fusion is a time period where you permit it to perform maintenance operations, reducing the risk of service disruptions during peak usage times. Scheduling maintenance windows during off-peak hours, or times when your activity is lower, minimizes their impact on your Cloud Data Fusion instances and your pipeline executions.

Configuring maintenance windows lets you control when maintenance operations occur in your instance:

  * If the maintenance window is defined, maintenance operations are performed by Cloud Data Fusion within the defined periods.
  * If the maintenance window isn't defined, maintenance can be performed at any time.



## About maintenance operations

To ensure system security and compliance, Cloud Data Fusion conducts regular maintenance operations. These operations include applying critical updates and security patches to mitigate vulnerabilities and protect user data. Scheduled maintenance windows ensure that the updates are efficiently applied, preserving system integrity and minimizing disruption to instances and pipeline executions.

  * When you configure the maintenance windows, you must allocate at least 12 hours per week for maintenance operations. Each window must be between 4 and 12 hours.
  * During the maintenance window hours, certain operations might be impacted. We recommend having maintenance windows during non-peak usage times. The maintenance operation can affect Cloud Data Fusion in following ways:

    * The Cloud Data Fusion Studio interface might be temporarily unavailable.
    * Pipeline execution might be impacted, causing failure.
    * Cloud Data Fusion services might be down temporarily, causing API calls to fail.
    * Instances might not be fully functional for up to an hour during maintenance window hours. We recommend that you set up maintenance windows when your pipelines either aren't running or aren't scheduled to run.

**Note:** If there are critical security vulnerabilities that need immediate remediation, maintenance windows might be overridden.

## Specify maintenance windows while creating an instance

###  Console 

To set the maintenance window when you create an instance, follow these steps:

  1. Go to the Cloud Data Fusion **Instances** page, and click **Create instance**. 

[ Create an instance](https://console.cloud.google.com/data-fusion/instance-create)

  2. Enter an **Instance name** and **Edition**. For more information about each field, see [Create an instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance#create_an_instance).
  3. Expand the **Advanced options** section.
  4. Expand the **Maintenance** section and follow these steps: 
     1. Select the **Enable maintenance window** checkbox.
     2. In the **Start time** field, enter a time in a supported format.
     3. In the **TimeZone** list, select a time zone.
     4. In the **Days** and **Length** lists, select days of the week and duration of window. For more information about these settings, see About maintenance operations.
     5. Click **Create**.



For more information, see Configure maintenance window times and recurrence (RRULE).

###  REST API 

  1. Set the `Instance` configuration using the [`instance.create`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create) API:


    
    
    {
      "name": string,
      "description": string,
      …
      …
      "maintenancePolicy": {
        "maintenanceWindow": {
          "recurringTimeWindow": {
            "window": {
                "startTime": "START_TIME",
                "endTime": "END_TIME"
            },
            "recurrence": "MAINTENANCE_RECURRENCE"
          }
        },
      }
    }
    

Replace the following:

  * `START_TIME`: time window start time, in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format.
  * `END_TIME`: time window end time, in the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format.
  * `MAINTENANCE_RECURRENCE`: an [RRULE](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for the maintenance window's recurrence. Cloud Data Fusion only supports the following formats:

    * `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` or `BYDAY=SU,MO,TU,WE,TH,FR,SA,MO;FREQ=WEEKLY`. This specifies the weekly recurrence of the window on the selected days, starting at the `startTime`, and for the specified duration.



For more information, see Configure maintenance window times and recurrence (RRULE).

The following example creates an instance with a six-hour maintenance window between 10 AM to 4 PM (UTC) on Saturday and Sunday every week. For more information, see the [instances API documentation](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Instance).
    
    
    // POST https://datafusion.googleapis.com/v1/projects/example-project/locations/us-central1/instances?instanceID=example-instance
    
    {
      "maintenancePolicy": {
          "maintenanceWindow": {
              "recurringTimeWindow": {
                  "window": {
                      "startTime": "2024-01-01T10:00:00Z",
                      "endTime": "2024-01-01T16:00:00Z",
                  },
                  "recurrence": "FREQ=WEEKLY;BYDAY=SA,SU"
              }
          },
      }
    }
    
    

###  gcloud 

You can specify the maintenance window while creating an instance using the [`gcloud beta data-fusion instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create) command.

The following parameters must be defined for a maintenance window:

  * `--maintenance-window-start` sets the window's start time.
  * `--maintenance-window-end` sets the window's end time.
  * `--maintenance-window-recurrence` sets an [RRULE](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for the maintenance window's recurrence.


    
    
    gcloud beta data-fusion instances create INSTANCE_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --maintenance-window-start=START_TIME \
        --maintenance-window-end=END_TIME \
        --maintenance-window-recurrence=MAINTENANCE_RECURRENCE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `PROJECT_NAME`: the name of the project.
  * `LOCATION`: the name of the region of the instance.
  * `START_TIME`: the window's start time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `END_TIME`: the window's end time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start time.
  * `MAINTENANCE_RECURRENCE`: an [RRULE](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for the maintenance window's recurrence. Cloud Data Fusion only supports the following formats:

    * `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` or `BYDAY=SU,MO,TU,WE,TH,FR,SA,MO;FREQ=WEEKLY`. This specifies the weekly recurrence of the window on the selected days, starting at the `--maintenance-window-start` time, and for the specified duration.



For more information, see Configure maintenance window times and recurrence (RRULE).

The following command creates an instance with a six-hour maintenance window between 12 PM to 6 PM (UTC) on Saturday and Sunday every week.
    
    
    gcloud beta data-fusion instances create example-instance \
        --project='example-project' \
        --location='us-east1' \
        --maintenance-window-start='2024-01-01T12:00:00Z' \
        --maintenance-window-end='2024-01-01T18:00:00Z' \
        --maintenance-window-recurrence='FREQ=WEEKLY;BYDAY=SA,SU'
    

## Update the maintenance windows for an instance

###  Console 

To update the maintenance window in an existing instance in the Google Cloud console, follow these steps:

  1. Go to the Cloud Data Fusion **Instances** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click the instance name to view the instance details.

  3. On the **Instance details** page, navigate to the **Maintenance window** field and click **Edit**.

  4. Maintenance window fields are opened in the edit mode. Update the values, as needed:

     1. Select the **Enable maintenance window** checkbox.
     2. In the **Start time** field, enter a time in a supported format.
     3. In the **TimeZone** list, select a time zone.
     4. In the **Days** and **Length** lists, select days of week and duration of window. For more information about these settings, see About maintenance operations.
  5. Click **Save**.




For more information, see Configure maintenance window times and recurrence (RRULE).

###  REST API 

For existing instances, update the maintenance windows using the [`instances.patch`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Instance) API request. This overrides the existing maintenance window configuration, if present. Otherwise, a new configuration is set, as mentioned in the request body.

Construct an API request as follows:

  1. In the `updateMask` parameter, specify the `maintenance_policy` mask.
  2. In the request body, specify the maintenance window in the maintenance policy configuration:


    
    
    {
      "maintenancePolicy": {
        "maintenanceWindow": {
            "recurringTimeWindow": {
              "window": {
                  "startTime": "START_TIME",
                  "endTime": "END_TIME"
              },
              "recurrence": "MAINTENANCE_RECURRENCE"
            }
        },
      }
    }
    

For more information, see Configure maintenance window times and recurrence (RRULE).

The following example updates the maintenance policy configuration of the instance with a four-hour maintenance window between 11 AM to 3 PM (UTC) on Friday, Saturday, and Sunday every week.
    
    
    // PATCH https://datafusion.googleapis.com/v1/projects/example-project/locations/us-central1/instances/example-instance?updateMask=maintenance_policy
    
    {
    "maintenancePolicy": {
      "maintenanceWindow": {
        "recurringTimeWindow": {
          "window": {
              "startTime": "2024-01-01T11:00:00Z",
              "endTime": "2024-01-01T15:00:00Z",
            },
          "recurrence": "FREQ=WEEKLY;BYDAY=FR,SA,SU"
        }
      },
    }
    }
    

###  gcloud 

You can update the maintenance window of an instance using the [`gcloud beta data-fusion instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update) command.

The following parameters must be defined for a maintenance window:

  * `--maintenance-window-start` sets the window's start time.
  * `--maintenance-window-end` sets the window's end time.
  * `--maintenance-window-recurrence` sets an [RRULE](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for the maintenance window's recurrence.


    
    
    gcloud beta data-fusion instances update INSTANCE_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --maintenance-window-start=START_TIME \
        --maintenance-window-end=END_TIME \
        --maintenance-window-recurrence=MAINTENANCE_RECURRENCE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `PROJECT_NAME`: the name of the project.
  * `LOCATION`: the name of the region of the instance.
  * `START_TIME`: the window's start time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `END_TIME`: the window's end time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start time.
  * `MAINTENANCE_RECURRENCE`: an [RRULE](https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for the maintenance window's recurrence. Cloud Data Fusion only supports the following formats:

    * `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` or `BYDAY=SU,MO,TU,WE,TH,FR,SA,MO;FREQ=WEEKLY`. This specifies the weekly recurrence of the window on the selected days, starting at the `--maintenance-window-start` time, and for the specified duration.



The following command updates the instance `example-instance` with a six-hour maintenance window between 12 PM to 6 PM (UTC) on Saturday and Sunday every week.
    
    
    gcloud beta data-fusion instances update example-instance \
        --project='example-project' \
        --location='us-east1' \
        --maintenance-window-start='2024-01-01T12:00:00Z' \
        --maintenance-window-end='2024-01-01T18:00:00Z' \
        --maintenance-window-recurrence='FREQ=WEEKLY;BYDAY=SA,SU'
    

## Configure maintenance window times and recurrence (RRULE)

When you configure start and end times for the maintenance window, the date components of the provided timestamps are ignored. Only the time of the day and duration between start and end time are considered. Times are stored in UTC, but you can use UTC or your time zone offset when scheduling maintenance windows using REST API or the gcloud CLI.

When you configure recurrence, keep in mind that RRULE follows UTC days, so adjust accordingly if your time zone differs. For example, if your time zone is PDT (UTC-7) and you want a maintenance window to start at 21:00 on Wednesdays in your time zone (which corresponds to 4:00 UTC on Thursdays), specify `TH` instead of `WE` in the `BYDAY` option of the RRULE.

**Important:** Using UTC while specifying maintenance window through REST API or gcloud CLI is **highly recommended**.

## Remove the maintenance window for an instance

###  Console 

To remove the maintenance window in an existing instance in the Google Cloud console, follow these steps:

  1. Go to the Cloud Data Fusion **Instances** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click the instance name to view the instance details.

  3. On the **Instance details** page, navigate to the **Maintenance window** field and click **Edit**.

  4. To remove the maintenance window from the instance, clear the **Enable maintenance window** checkbox.

  5. Click **Save**.




###  REST API 

To remove the maintenance window from an instance, pass an empty maintenance policy object in the request body.
    
    
    // PATCH https://datafusion.googleapis.com/v1/projects/example-project/locations/us-central1/instances/example-instance?updateMask=maintenance_policy
    
    {
        "maintenancePolicy": {}
    }
    

###  gcloud 

To remove the maintenance window from an instance, use [`gcloud beta data-fusion instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update) command with the `--clear-maintenance-window` flag.
    
    
    gcloud beta data-fusion instances update INSTANCE_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --clear-maintenance-window
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `PROJECT_NAME`: the name of the project.
  * `LOCATION`: the name of the region of the instance.



## View maintenance events and receive notifications

Cloud Data Fusion reports scheduled maintenance events for your instances through [Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview). To view these events and receive notifications about them, you need to set up each separately:

  * To view maintenance events on the [Cloud Hub **Maintenance** page](https://docs.cloud.google.com/hub/docs/maintenance) in the Google Cloud console, or to query the Unified Maintenance API directly, you must enable the API in your project.
  * To receive notifications, you must configure log-based alerting policies in Cloud Logging. Enabling the API doesn't subscribe you to notifications.



### Enable the Unified Maintenance API

To view maintenance events in the Google Cloud console, enable the Unified Maintenance API (`maintenance.googleapis.com`) in your project. Unified Maintenance doesn't display historical events that were scheduled before you enabled the API.

###  Console 

  1. In the **API Library** , go to the **Maintenance API** page.

[Go to Maintenance API](https://console.cloud.google.com/apis/library/maintenance.googleapis.com)

  2. Click **Enable**.




###  gcloud 

Use the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
    
    
    gcloud services enable maintenance.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

### Configure notifications

Unified Maintenance writes maintenance event logs with the log ID `maintenance.googleapis.com/maintenance_events` to Logging automatically, regardless of whether the Unified Maintenance API is enabled. To receive notifications through channels such as email, Pub/Sub, Slack, PagerDuty, or webhooks, create log-based alerting policies that match these logs. For more information, see [Configure alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications).

## What's next

  * Refer to the [instances API documentation](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Instance).
  * Learn how to [view maintenance activities in Cloud Hub](https://docs.cloud.google.com/hub/docs/maintenance).
  * Learn how to [configure alerts and notifications for maintenance events](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications).
  * Learn more about [Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
