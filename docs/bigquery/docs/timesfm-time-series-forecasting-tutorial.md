---
url: https://docs.cloud.google.com/bigquery/docs/timesfm-time-series-forecasting-tutorial/
title: Forecast single or multiple time series with a TimesFM univariate model \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:17.479788+00:00
---

# Forecast single or multiple time series with a TimesFM univariate model  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/timesfm-time-series-forecasting-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

#  Forecast single or multiple time series with a TimesFM univariate model Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial teaches you how to perform univariate forecasting across single or multiple time series by using the [`AI.FORECAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast) with the [TimesFM univariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-model) that's built into BigQuery.

This tutorial uses data from the public [`bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=san_francisco_bikeshare&t=bikeshare_trips&page=table) table.

## Objectives

  * Perform univariate forecasting and visualize results for a single time series.
  * Perform univariate forecasting and visualize results for multiple time series.



## Costs

This tutorial uses billable components of Google Cloud, including the following:

  * BigQuery
  * BigQuery ML



For more information, see [BigQuery pricing](https://docs.cloud.google.com/bigquery/pricing) and [BigQuery ML pricing](https://docs.cloud.google.com/bigquery/pricing#bqml).

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

  6. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com)

For new projects, the BigQuery API is automatically enabled.




### Required roles

To get the permissions that you need to complete the tasks in this tutorial, ask your administrator to grant you the following IAM roles: 

  * Create the dataset: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) 
  * Create the model: 
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
    * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * Run inference: 
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
    * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to complete the tasks in this tutorial. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to complete the tasks in this tutorial:

  * Create the dataset: `bigquery.datasets.create`
  * Create the model: 
    * `bigquery.jobs.create`
    * `bigquery.models.create`
    * `bigquery.models.getData`
    * `bigquery.models.updateData`
  * Run inference: 
    * `bigquery.models.getData`
    * `bigquery.jobs.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about IAM roles and permissions in BigQuery, see [Introduction to IAM](https://docs.cloud.google.com/bigquery/docs/access-control). 

## Forecast a single bike share trips time series

Forecast future time series values by using the `AI.FORECAST` function.

The following query forecasts the number of subscriber bike share trips per hour for the next month (approximately 720 hours), based on the previous four months of historical data. The `confidence_level` argument indicates that the query generates a prediction interval with a 95% confidence level.

Follow these steps to forecast data with the TimesFM model:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** :
         
         SELECT *
         FROM
           AI.FORECAST(
             (
               SELECT TIMESTAMP_TRUNC(start_date, HOUR) as trip_hour, COUNT(*) as num_trips
         FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
         WHERE subscriber_type = 'Subscriber' AND start_date >= TIMESTAMP('2018-01-01')
         GROUP BY TIMESTAMP_TRUNC(start_date, HOUR)
             ),
             horizon => 720,
             confidence_level => 0.95,
             timestamp_col => 'trip_hour',
             data_col => 'num_trips');

The results look similar to the following:
         
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | forecast_timestamp      | forecast_value    | confidence_level | prediction_interval_lower_bound | prediction_interval_upper_bound | ai_forecast_status |
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | 2018-05-01 00:00:00 UTC | 26.3045959...     |            0.95  | 21.7088378...                   | 30.9003540...                   |                    |
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | 2018-05-01 01:00:00 UTC | 34.0890502...     |            0.95  | 2.47682913...                   | 65.7012714...                   |                    |
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | 2018-05-01 02:00:00 UTC | 24.2154693...     |            0.95  | 2.87621605...                   | 45.5547226...                   |                    |
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | ...                     | ...               |  ...             | ...                             |  ...                            |                    |
         +-------------------------+-------------------+------------------+---------------------------------+---------------------------------+--------------------+
         




## Compare the forecasted data to the input data

Chart the `AI.FORECAST` function output alongside a subset of the function input data to see how they compare.

Follow these steps to chart the function output:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** :
         
         SELECT *
         FROM
           AI.FORECAST(
             (
               SELECT TIMESTAMP_TRUNC(start_date, HOUR) as trip_hour, COUNT(*) as num_trips
               FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
               WHERE subscriber_type = 'Subscriber' AND start_date >= TIMESTAMP('2018-01-01')
               GROUP BY TIMESTAMP_TRUNC(start_date, HOUR)
             ),
             horizon => 720,
             confidence_level => 0.95,
             timestamp_col => 'trip_hour',
             data_col => 'num_trips',
             output_historical_time_series => true);

  3. When the query is finished running, click the **Visualization** tab in the **Query results** pane. For **Visualization type** , select **Line**. For **Dimension** , select `time_series_timestamp`. For **Measures** , select `time_series_data`, `prediction_interval_lower_bound`, and `prediction_interval_upper_bound`. The resulting chart looks similar to the following:

![Graph 100 time points of input data along with the AI.FORECAST function output data to evaluate their similarity.](https://docs.cloud.google.com/static/bigquery/images/ai-forecast-output-comparison.png)

You can see that the input data and the forecasted data show similar bike share usage. You can also see that the prediction interval lower and upper bounds increase as the forecasted time points get further into the future.




## Forecast multiple bike share trips time series

The following query forecasts the number of bike share trips per subscriber type and per hour for the next month (approximately 720 hours), based on the previous four months of historical data. The `confidence_level` argument indicates that the query generates a prediction interval with a 95% confidence level.

Follow these steps to forecast data with the TimesFM model:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** :
         
         SELECT *
         FROM
           AI.FORECAST(
             (
               SELECT TIMESTAMP_TRUNC(start_date, HOUR) as trip_hour, subscriber_type, COUNT(*) as num_trips
               FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
               WHERE start_date >= TIMESTAMP('2018-01-01')
               GROUP BY TIMESTAMP_TRUNC(start_date, HOUR), subscriber_type
             ),
             horizon => 720,
             confidence_level => 0.95,
             timestamp_col => 'trip_hour',
             data_col => 'num_trips',
             id_cols => ['subscriber_type']);

The results look similar to the following:
         
         +---------------------+--------------------------+------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | subscriber_type     | forecast_timestamp       | forecast_value   | confidence_level | prediction_interval_lower_bound | prediction_interval_upper_bound | ai_forecast_status |
         +---------------------+--------------------------+------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | Subscriber          | 2018-05-01 00:00:00 UTC  | 26.3045959...    |            0.95  | 21.7088378...                   | 30.9003540...                   |                    |
         +---------------------+--------------------------+------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | Subscriber          |  2018-05-01 01:00:00 UTC | 34.0890502...    |            0.95  | 2.47682913...                   | 65.7012714...                   |                    |
         +---------------------+-------------------+------------------+-------------------------+---------------------------------+---------------------------------+--------------------+
         | Subscriber          |  2018-05-01 02:00:00 UTC | 24.2154693...    |            0.95  | 2.87621605...                   | 45.5547226...                   |                    |
         +---------------------+--------------------------+------------------+------------------+---------------------------------+---------------------------------+--------------------+
         | ...                 | ...                      |  ...             | ...              | ...                             |  ...                            |                    |
         +---------------------+--------------------------+------------------+------------------+---------------------------------+---------------------------------+--------------------+
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your project

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
  * Learn how to [forecast single time series with a TimesFM multivariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-single-time-series-forecasting-tutorial).
  * Learn how to [forecast multiple time series with a TimesFM multivariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-multi-time-series-forecasting-tutorial).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
