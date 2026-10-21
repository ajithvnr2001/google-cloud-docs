---
url: https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-single-time-series-forecasting-tutorial/
title: Forecast a single time series with a TimesFM multivariate model \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:13.903829+00:00
---

# Forecast a single time series with a TimesFM multivariate model  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-single-time-series-forecasting-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

#  Forecast a single time series with a TimesFM multivariate model Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial teaches you how to perform multivariate forecasting across a single time series by using the [`AI.FORECAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast) with the [`TimesFM 3.0` model](https://docs.cloud.google.com/bigquery/docs/timesfm-model) that's built into BigQuery ML. Multivariate forecasting helps you improve forecast accuracy by incorporating other variables that influence the target.

This tutorial demonstrates how to forecast vodka and whiskey sales by incorporating historical transaction values (a past covariate) and whether the date is a weekend (a future covariate).

## Objectives

  * Prepare a single unified dataset for multivariate forecasting.
  * Use the `AI.FORECAST` function with the `TimesFM 3.0` model to generate predictions.



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

## Prepare the input data

Unlike other multivariate models that might require separate tables for historical and future covariates, the `AI.FORECAST` function with `TimesFM 3.0` expects a single input table or query.

Before running a forecast, ensure your data meets these requirements:

  * Historical rows: contain non-null values for timestamps, targets, and past covariates.
  * Future rows: contain non-null values for timestamps and future covariates only. Target columns and past covariate columns must be set to `NULL` for these future rows.



Your input table must contain columns with the following data:

  * The date of the sales.
  * The number of vodka bottles sold on that date. This is a target column.
  * The number of whiskey bottles sold on that date. This is a target column.
  * The average transaction value on that date. This is a past covariate used in the forecast.
  * Whether the date is a weekend. This is a future covariate used in the forecast.



## Forecast the single multivariate time series

The following query forecasts number of vodka and whiskey bottles sold for the first two weeks of July, 2023 at store number 2633. It uses the average transaction value as a past covariate and whether the date is a weekend as a future covariate.

Follow these steps to forecast data with the `TimesFM 3.0` model:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, paste in the following query and click **Run** :
         
         WITH historical_sales AS (
           SELECT
             date AS sales_date,
             store_number,
             SUM(CASE WHEN category_name LIKE '%VODKA%' THEN bottles_sold ELSE 0 END) AS vodka_bottles,
             SUM(CASE WHEN category_name LIKE '%WHISKEY%' THEN bottles_sold ELSE 0 END) AS whiskey_bottles,
             AVG(sale_dollars) AS avg_transaction_value,                          -- Past covariate
             IF(EXTRACT(DAYOFWEEK FROM date) IN (1, 7), 1.0, 0.0) AS is_weekend   -- Future covariate
           FROM `bigquery-public-data.iowa_liquor_sales.sales`
           WHERE date BETWEEN '2023-01-01' AND '2023-06-30'
             AND store_number = '2633'
           GROUP BY sales_date, store_number
         ),
         future_horizon AS (
           SELECT
             future_date AS sales_date,
             store_number,
             CAST(NULL AS INT64) AS vodka_bottles,
             CAST(NULL AS INT64) AS whiskey_bottles,
             CAST(NULL AS FLOAT64) AS avg_transaction_value,
             IF(EXTRACT(DAYOFWEEK FROM future_date) IN (1, 7), 1.0, 0.0) AS is_weekend
           FROM UNNEST(GENERATE_DATE_ARRAY('2023-07-01', '2023-07-14')) AS future_date
           CROSS JOIN (SELECT DISTINCT store_number FROM historical_sales)
         ),
         combined_sales AS (
           SELECT * FROM historical_sales
           UNION ALL
           SELECT * FROM future_horizon
         )
         SELECT
           FORMAT_DATE('%Y-%m-%d', sales_date) AS sales_date,
           vodka_bottles.value AS vodka_value,
           vodka_bottles.prediction_interval_lower_bound AS vodka_lower,
           vodka_bottles.prediction_interval_upper_bound AS vodka_upper,
           whiskey_bottles.value AS whiskey_value,
           whiskey_bottles.prediction_interval_lower_bound AS whiskey_lower,
           whiskey_bottles.prediction_interval_upper_bound AS whiskey_upper
         FROM AI.FORECAST(
           TABLE combined_sales,
           model => 'TimesFM 3.0',
           timestamp_col => 'sales_date',
           target_cols => ['vodka_bottles', 'whiskey_bottles'],
           past_covariate_cols => ['avg_transaction_value'],
           future_covariate_cols => ['is_weekend'],
           id_cols => ['store_number'],
           horizon => 14,
           confidence_level => 0.90
         );
         




The output is similar to the following, with values rounded for clarity:
    
    
    +------------+-------------+-------------+-------------+---------------+---------------+---------------+
    | sales_date | vodka_value | vodka_lower | vodka_upper | whiskey_value | whiskey_lower | whiskey_upper |
    +------------+-------------+-------------+-------------+---------------+---------------+---------------+
    | 2023-07-01 | 408         | -334        | 1977        | 21            | -34           | 113           |
    | 2023-07-02 | 806         | -281        | 2992        | 29            | -23           | 149           |
    | ...        | ...         | ...         | ...         | ...           | ...           | ...           |
    +------------+-------------+-------------+-------------+---------------+---------------+---------------+
    

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
  * Learn how to [forecast single or multiple time series with a TimesFM univariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-time-series-forecasting-tutorial).
  * Learn how to [forecast multiple time series with a TimesFM multivariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-multi-time-series-forecasting-tutorial).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
