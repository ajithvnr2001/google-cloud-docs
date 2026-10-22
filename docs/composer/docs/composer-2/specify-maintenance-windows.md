---
url: https://docs.cloud.google.com/composer/docs/composer-2/specify-maintenance-windows/
title: Specify maintenance windows \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:41.966531+00:00
---

# Specify maintenance windows  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/specify-maintenance-windows/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Specify maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/specify-maintenance-windows "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/specify-maintenance-windows "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to define maintenance windows for your environments.

## About maintenance windows

A maintenance window is a time period where you permit Managed Airflow to perform maintenance operations. For example, you can make sure that your critical task executions are not interrupted by specifying maintenance windows outside of the DAG schedule times.

With maintenance windows, you have control over the time periods where maintenance can happen for your environment:

  * If you define custom maintenance windows for your environment, Managed Airflow performs maintenance during these defined periods.

  * If you do not define custom maintenance windows for your environment, Managed Airflow performs maintenance during the default maintenance windows.


**Note:** Always configure maintenance windows through Managed Airflow interfaces like Google Cloud console, Google Cloud SDK, Terraform, and Cloud Composer API. Avoid configuring maintenance windows on your environment's cluster level unless you are guided to do so by Cloud Customer Care team.

## How maintenance windows work

Maintenance windows work in the following way:

  * Maintenance operations require at least 12 hours of time allocated in a single week.

  * You can use several time slots, but each slot duration must be at least 4 hours.

  * Your environment stays available during maintenance windows. Some components of your environment might become temporarily unavailable when maintenance operations are ongoing.

  * The 12 hours are required so that Managed Airflow has enough time to schedule and perform all maintenance operations. This does not mean that maintenance operations take full 12 hours or even happen every week.




You can still run your DAGs during maintenance windows, as long as it is acceptable that some tasks can be interrupted and retried. If you run DAGs during maintenance windows, make sure that you enable task retries. You can configure task retries at the Airflow configuration, DAG, or task level.

Tasks that take less than 55 minutes to execute are generally not impacted by maintenance operations, but they still need to have retries enabled to withstand scheduler restarts. Scheduler might restart during standard Managed Airflow operations, outside maintenance windows.

Managed Airflow informs Airflow workers that a maintenance operation is about to happen. An Airflow worker finishes already started tasks and does not pick new tasks. These new tasks are executed by Airflow workers that do not undergo maintenance operations.

If you use a [highly resilient environment](https://docs.cloud.google.com/composer/docs/composer-2/set-up-highly-resilient-environments), then Airflow components of your environment are likely to be restarted at different times during a maintenance operation (this depends on the type of maintenance operation). Overall, using a highly resilient environment reduces the downtime of your environment during maintenance operations.

Maintenance operations have the following effects on your environment:

  * Airflow UI might be temporarily not available.

  * Changing some parameters of your environment or upgrading to a later version might not be possible temporarily.

  * Direct SQL queries to the Airflow database might take longer than usual and might require retrying.

  * Some Airflow tasks that take longer than 55 minutes to execute can be interrupted. After the maintenance operation completes, Airflow schedules retries for these tasks (if not configured otherwise).




## Default maintenance windows

Default maintenance windows in Managed Airflow (Gen 2) are from 00:00:00 to 04:00:00 (GMT) on Friday, Saturday, and Sunday every week.

## Maintenance outside of maintenance windows

Managed Airflow might perform maintenance outside of configured maintenance windows in the following cases:

  * In emergency situations, for example, when fixing a critical security vulnerability, some maintenance operations might be performed outside of regular maintenance windows.

  * If Managed Airflow couldn't perform regular maintenance operations during maintenance windows for 30 days, it performs critical maintenance operations outside of the specified maintenance windows. This is a fallback mechanism for cases when maintenance windows are misconfigured and Managed Airflow repeatedly can't perform maintenance on an environment.




## How to use maintenance windows

Maintenance operations might impact the execution of your DAGs and Airflow tasks, so we recommend you to do the following:

  1. Define maintenance windows for your Managed Airflow environments.

  2. Schedule DAG runs outside of specified maintenance windows by using [`start_date` and `schedule`](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html) parameters in your DAGs.




## Specify maintenance windows for new environments

You can specify maintenance windows when you create an environment. For more information, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#maintenance-windows).

## Specify maintenance windows for existing environments

###  Console 

To define or change maintenance windows for an existing environment, [update the environment](https://docs.cloud.google.com/composer/docs/composer-2/update-environments):

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select your environment.

  3. Go to the **Environment configuration** tab.

  4. Next to the **Maintenance windows** entry, click **Edit**.

  5. In the **Maintenance windows** dialog, select the **Set custom time for maintenance windows** checkbox.

  6. Set **Start time** , **Timezone** , **Days** , and **Length** , so that combined time for the specified schedule is at least 12 hours in a 7-day rolling window. For example, a period of 4 hours every Monday, Wednesday, and Friday provides the required amount of time.

  7. Click **Save** and wait until your environment updates.




###  gcloud 

When you update an environment, the following arguments define maintenance windows parameters:

  * `--maintenance-window-start` sets the start time of a maintenance window.
  * `--maintenance-window-end` sets the end time of a maintenance window.
  * `--maintenance-window-recurrence` sets the [maintenance window recurrence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).


    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --maintenance-window-start 'DATETIME_START' \
        --maintenance-window-end 'DATETIME_END' \
        --maintenance-window-recurrence 'MAINTENANCE_RECURRENCE'
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

  * The `FREQ=DAILY` format specifies a daily recurrence.

  * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.




The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023 date is ignored.
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --maintenance-window-start '2023-01-01T01:00:00Z' \
      --maintenance-window-end '2023-01-01T07:00:00Z' \
      --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=SU,WE,SA'
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.maintenanceWindow` mask.

     2. In the request body, specify the parameters for maintenance windows.



    
    
    {
      "config": {
        "maintenanceWindow": {
          "startTime": "DATETIME_START",
          "endTime": "DATETIME_END",
          "recurrence": "MAINTENANCE_RECURRENCE"
        }
      }
    }
    

Replace:

  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

    * The `FREQ=DAILY` format specifies a daily recurrence.
    * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.



The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, Sundays. The 1 January, 2023 date is ignored.
    
    
      // PATCH https://composer.googleapis.com/v1/projects/example-project/
      // locations/us-central1/environments/example-environment?updateMask=
      // config.maintenanceWindow
    
      {
        "config": {
          "maintenanceWindow": {
            "startTime": "2023-01-01T01:00:00Z",
            "endTime": "2023-01-01T07:00:00Z",
            "recurrence": "FREQ=WEEKLY;BYDAY=SU,WE,SA"
          }
        }
      }
    

###  Terraform 

The `maintenance_window` block specifies the maintenance windows for your environment:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        maintenance_window {
          start_time = "DATETIME_START"
          end_time = "DATETIME_END"
          recurrence = "MAINTENANCE_RECURRENCE"
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

    * The `FREQ=DAILY` format specifies a daily recurrence.
    * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.



The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023 date is ignored.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        maintenance_window {
          start_time = "2023-01-01T01:00:00Z"
          end_time = "2023-01-01T07:00:00Z"
          recurrence = "FREQ=WEEKLY;BYDAY=SU,WE,SA"
        }
      }
    }
    

## What's next

  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Updating environments](https://docs.cloud.google.com/composer/docs/composer-2/update-environments)
  * [Clean up the Airflow database](https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
