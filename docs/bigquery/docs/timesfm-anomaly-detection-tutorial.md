---
url: https://docs.cloud.google.com/bigquery/docs/timesfm-anomaly-detection-tutorial/
title: Detect anomalies in multiple time series with the TimesFM model \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:34.671117+00:00
---

# Detect anomalies in multiple time series with the TimesFM model  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/timesfm-anomaly-detection-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

#  Detect anomalies in multiple time series with the TimesFM model Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial teaches you how to use the [`AI.DETECT_ANOMALIES` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies) with BigQuery ML's built-in [TimesFM model](https://docs.cloud.google.com/bigquery/docs/timesfm-model) to detect anomalies in time series data.

This tutorial uses data from the public [`bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=san_francisco_bikeshare&t=bikeshare_trips&page=table) table.

## Objectives

This tutorial guides you through using the `AI.DETECT_ANOMALIES` function with the built-in TimesFM model to detect anomalies in bike share trips. The first section covers how to detect anomalies and visualize results for a single time series. The second section covers how to detect anomalies for multiple time series.

## Costs

This tutorial uses billable components of Google Cloud, including the following:

  * BigQuery
  * BigQuery ML



For more information about BigQuery costs, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.

For more information about BigQuery ML costs, see [BigQuery ML pricing](https://cloud.google.com/bigquery/pricing#bqml).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. BigQuery is automatically enabled in new projects. To activate BigQuery in a pre-existing project, 

Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery)




## Detect anomalies in a single bike share trips time series

Detect anomalies in time series data by using the `AI.DETECT_ANOMALIES` function.

The following query detects anomalies in the number of bike share trips per hour for the month of August 2017, based on the historical data from the previous month. The `anomaly_prob_threshold` argument indicates the threshold for identifying an anomaly.

Follow these steps to detect anomalies with the TimesFM model:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** , the query takes 1-2 minutes to complete:
         
         WITH
           bike_share_trips AS (
             SELECT
               TIMESTAMP_TRUNC(start_date, HOUR) AS trip_hour, COUNT(*) AS num_trips
             FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
             GROUP BY TIMESTAMP_TRUNC(start_date, HOUR)
           )
         SELECT *
         FROM
           AI.DETECT_ANOMALIES(
             (
               SELECT *
               FROM bike_share_trips
               WHERE trip_hour >= TIMESTAMP('2017-07-01') AND trip_hour < TIMESTAMP('2017-08-01')
             ),
             (
               SELECT *
               FROM bike_share_trips
               WHERE trip_hour >= TIMESTAMP('2017-08-01') AND trip_hour < TIMESTAMP('2017-09-01')
             ),
             anomaly_prob_threshold => 0.95,
             timestamp_col => 'trip_hour',
             data_col => 'num_trips');

The results look similar to the following:
         
         +-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | time_series_timestamp   | time_series_data | is_anomaly | lower_bound        | upper_bound         | anomaly_probability | ai_detect_anomalies_status|
         +-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | 2017-08-01 00:00:00 UTC | 13.0             | false      | -1.97939332204...  | 27.604928623830...  | 0.38048622012138... |                           |
         +-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | 2017-08-01 01:00:00 UTC | 6.0              | false      | -9.42939322810...  | 20.154928628380...  | 0.38048622012138... |                           |
         +-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | ...                     | ...              | ...        | ...                | ...                 | ...                 | ...                       |
         +-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         

  3. When the query is finished running, click the **Visualization** tab. The resulting chart looks similar to the following:

![Graph one month timepoints of input data along with the AI.DETECT_ANOMALIES function output data to show anomalies.](https://docs.cloud.google.com/static/bigquery/images/ai-detect-anomalies.png)

You can identify the anomalies where the `time_series_data` value falls outside the `lower_bound` and `upper_bound` range.




## Detect anomalies in multiple bike share trips time series

The following query detects anomalies in the number of bike share trips per subscriber type and per hour for the month of August 2017, based on the historical data from the previous month.

Follow these steps to detect anomalies with the TimesFM model:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** :
         
         WITH
           bike_share_trips AS (
             SELECT
               TIMESTAMP_TRUNC(start_date, HOUR) AS trip_hour, COUNT(*) AS num_trips, subscriber_type
             FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
             GROUP BY TIMESTAMP_TRUNC(start_date, HOUR), subscriber_type
           )
         SELECT *
         FROM
           AI.DETECT_ANOMALIES(
             (
               SELECT *
               FROM bike_share_trips
               WHERE trip_hour >= TIMESTAMP('2017-07-01') AND trip_hour < TIMESTAMP('2017-08-01')
             ),
             (
               SELECT *
               FROM bike_share_trips
               WHERE trip_hour >= TIMESTAMP('2017-08-01') AND trip_hour < TIMESTAMP('2017-09-01')
             ),
             anomaly_prob_threshold => 0.95,
             timestamp_col => 'trip_hour',
             data_col => 'num_trips',
             id_cols => ['subscriber_type']);

The results look similar to the following:
         
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | subscriber_type | time_series_timestamp   | time_series_data | is_anomaly | lower_bound        | upper_bound         | anomaly_probability | ai_detect_anomalies_status|
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | Customer        | 2017-08-01 00:00:00 UTC | 13.0             | false      | -1.97939332204...  | 27.604928623830...  | 0.38048622012138... |                           |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | Customer        | 2017-08-01 01:00:00 UTC | 3.0              | false      | -5.12345678901...  | 10.123456789012...  | 0.12345678901234... |                           |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | ...             | ...                     | ...              | ...        | ...                | ...                 | ...                 | ...                       |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | Subscriber      | 2017-08-01 00:00:00 UTC | 13.0             | false      | -1.97939332204...  | 27.604928623830...  | 0.38048622012138... |                           |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | Subscriber      | 2017-08-01 01:00:00 UTC | 3.0              | false      | -5.12345678901...  | 10.123456789012...  | 0.12345678901234... |                           |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         | ...             | ...                     | ...              | ...        | ...                | ...                 | ...                 | ...                       |
         +-----------------+-------------------------+------------------+------------+--------------------+---------------------+---------------------+---------------------------+
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your project

To delete the project:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * For an overview of BigQuery ML, see [Introduction to AI and ML in BigQuery](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
