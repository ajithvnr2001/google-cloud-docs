---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/business-insights-with-bigquery-ml/
title: Business insights in SAP with BigQuery ML \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:39.559135+00:00
---

# Business insights in SAP with BigQuery ML  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/business-insights-with-bigquery-ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Business insights in SAP with BigQuery ML Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for using [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) to build a machine learning solution in your SAP environment, by using the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/all-guides). With the help of the reference architecture explained in this document, you can build solutions that extract data-driven insights to accelerate your business decision-making processes within SAP.

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects. The document assumes that you're familiar with [BigQuery](https://docs.cloud.google.com/bigquery) and SQL.

## Architecture

The following diagram shows a reference architecture for a machine learning solution that provides business insights based on the data from an SAP ERP system:

![Machine learning solution for business insights in SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-sap-business-insights-with-bigquery-ml.svg)

This machine learning solution architecture includes the following components:

Component | Subsystem | Details  
---|---|---  
1 | Data source | An SAP ERP system such as SAP S/4HANA, which is the source of enterprise data.  
2 | Data warehouse | BigQuery, which stores raw data from source systems and ML generated insights.  
3 | Machine learning: Training | Machine learning models, which are trained on source data to generate business insights.  
4 | Machine learning: Serve Insights | Components that return ML generated business insights for consumption to SAP.  
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview): Helps you develop ABAP applications that connect your SAP systems to Google Cloud services, such as BigQuery.
  * [BigQuery](https://docs.cloud.google.com/bigquery): Helps you manage and analyze your enterprise data.



## Use cases

BigQuery ML empowers SAP users to derive valuable insights for improved decision-making and business outcomes by using the enterprise data stored in BigQuery. This section provides examples of use cases for which you can use BigQuery ML to build machine learning solutions.

### Forecasting

Forecasting in BigQuery ML involves analyzing historical time series data to predict future trends. For example, you can analyze historical sales data from several store locations to predict future sales at those locations. You can perform forecasting by using the [`ML.FORECAST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-forecast) function with the [`ARIMA_PLUS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series) or [`ARIMA_PLUS_XREG`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series) model.

### Anomaly detection

Anomaly detection finds unusual patterns in data, enabling proactive response to potential problems or opportunities. With labeled data, you can utilize various supervised machine learning models for this task. You can use the [linear and logistic regression](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm), [boosted trees](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree), [random forests](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest), [deep neural networks](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-dnn-models), [wide-and-deep models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models), or [AutoML](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-automl) model for anomaly detection.

### Recommendation systems

Recommendation systems are powerful tools for businesses, helping users discover relevant content within vast collections. These systems use machine learning to suggest items that users might not find on their own, overcoming the limitations of search. Recommendation systems primarily employ two approaches:

  * [Content-based filtering](https://developers.google.com/machine-learning/recommendation/content-based/basics), which recommends items based on similarity.
  * [Collaborative filtering](https://developers.google.com/machine-learning/recommendation/collaborative/basics), which uses similarities between users and their preferences.



## Design considerations

This section provides guidance to help you use this reference architecture to develop architectures that help you to meet your specific requirements for security, privacy, compliance, cost, and performance.

### Security, privacy, and compliance

To implement data governance policies, you can use BigQuery features. Data governance manages data security and quality throughout its lifecycle to ensure access and accuracy comply with policies and regulations. For more information, see [Introduction to data governance in BigQuery](https://docs.cloud.google.com/bigquery/docs/data-governance).

### Cost and performance

For an estimate of the cost of the Google Cloud resources that the data warehouse with BigQuery solution uses, see the precalculated estimate in the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator/).

As you begin to scale with BigQuery, you have a number of ways available to help improve your query performance and to reduce your total spend. These methods include changing how your data is physically stored, modifying your SQL queries, and using slot reservations to ensure cost performance. For more information about ways to help scale and run your data warehouse, see [Introduction to optimizing query performance](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-overview).

## Design alternative

While this document focuses on the on-premises or any cloud edition of ABAP SDK for Google Cloud, you can achieve similar results by using the [SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/all-guides). You can adapt the provided resources to build similar solutions within your SAP BTP environment.

## Deployment

This section shows you how to load data from your source SAP system into BigQuery, create a machine learning model suitable for your business requirements, and finally generate insights that can be used for business decisions in SAP.

### Before you begin

Before implementing a solution based on this reference architecture, make sure that you have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. For information about how to confirm that billing is enabled for your project, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The [on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

  * Authentication to access Google Cloud APIs is set up. For information about how to set up authentication, see [Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

  * The [BigQuery API](https://console.cloud.google.com/project/_/apis/library/bigquery.googleapis.com) is enabled in your Google Cloud project.

  * You have a BigQuery [dataset](https://docs.cloud.google.com/bigquery/docs/datasets) and a [table](https://docs.cloud.google.com/bigquery/docs/tables#create-table) to store your data.




### Load data from an SAP source system into BigQuery

To load data from an SAP source system into a BigQuery table by using the ABAP SDK for Google Cloud, you use the [`INSERT_ALL_TABLEDATA`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigquery_v2#insert_all_tabledata) method of the `/GOOG/CL_BIGQUERY_V2` class. This data serves as the foundation for training the machine learning models.

The following code sample illustrates how to load data from an SAP source system into a BigQuery table:
    
    
    TRY.
        DATA(lo_client) = NEW /goog/cl_bigquery_v2( iv_key_name = 'CLIENT_KEY' ).
    
        TYPES:
          BEGIN OF t_timeseries,
            date  TYPE string,   "YYYY-MM-DD
            value TYPE string,   "Numeric value
          END OF t_timeseries.
    
        DATA: lt_data TYPE STANDARD TABLE OF t_timeseries.
        "Developer TODO - populate lt_data
    
        DATA: ls_input        TYPE /goog/cl_bigquery_v2=>ty_133.
    
        LOOP AT lt_data INTO FIELD-SYMBOL(<ls_data>).
          APPEND INITIAL LINE TO ls_input-rows ASSIGNING FIELD-SYMBOL(<ls_row>).
          CREATE DATA <ls_row>-json TYPE t_timeseries.
          FIELD-SYMBOLS: <lfs_json> TYPE t_timeseries.
          ASSIGN <ls_row>-json->* TO <lfs_json> CASTING.
          <lfs_json> = <ls_data>.
        ENDLOOP.
    
        "Call API method: bigquery.tabledata.insertAll
        CALL METHOD lo_client->insert_all_tabledata
          EXPORTING
            iv_p_dataset_id = 'BIGQUERY_DATASET'
            iv_p_project_id = CONV #( lo_client->gv_project_id )
            iv_p_table_id   = 'BIGQUERY_TABLE'
            is_input        = ls_input
          IMPORTING
            es_output       = DATA(ls_output)
            ev_ret_code     = DATA(lv_ret_code)
            ev_err_text     = DATA(lv_err_text).
    
        lo_client->close( ).
    
      CATCH cx_root.
        "handle error
    ENDTRY.
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `BIGQUERY_DATASET`: The ID of the target BigQuery dataset.
  * `BIGQUERY_TABLE`: The ID of the target BigQuery table.



Alternatively, if you are looking for a no-code BigQuery data ingestion solution that handles both initial load and delta (CDC) handling, then you could consider [BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new), [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion), or [SAP Datasphere](https://docs.cloud.google.com/sap/docs/sap-datasphere-replication-bigquery-overview).

### Create a machine learning model

BigQuery provides a comprehensive list of [machine learning models and AI resources](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) to derive insights from enterprise data. One such model is [`ARIMA_PLUS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series), which you can use to forecast future time series values based on historical data. For example, you can use the `ARIMA_PLUS` model to predict future sales volumes based on historical data. To train a new model with the SAP data that you have loaded into BigQuery, you use the `CREATE MODEL` statement. Depending on the size of your data, this might take a few minutes or hours to run. After the model is created, you can view the model in [BigQuery Studio](https://docs.cloud.google.com/bigquery/docs/query-overview#bigquery-studio).

To create and train your model, run the `CREATE MODEL` statement:

  1. In the [Google Cloud console](https://console.cloud.google.com/bigquery), click the **Compose new query** button.

  2. Enter the following GoogleSQL query in the **Query editor** :
         
         CREATE OR REPLACE MODEL `MODEL_NAME`
                OPTIONS
                (model_type = 'ARIMA_PLUS',
                time_series_timestamp_col = 'TIME_SERIES_TIMESTAMP_COL',
                time_series_data_col = 'TIME_SERIES_DATA_COL',
                auto_arima = TRUE,
                data_frequency = 'AUTO_FREQUENCY',
                decompose_time_series = TRUE
                  ) AS
              SELECT
                {timestamp_column_name},
                {timeseries_data_column_name}
              FROM
                `{BigQuery_table}`
         

Replace the following:

     * `MODEL_NAME`: The name of your model that you have trained for generating insights.
     * `TIME_SERIES_TIMESTAMP_COL`: The name of the column that provides the time points used in training the model.
     * `TIME_SERIES_DATA_COL`: The name of the column that contains the data to forecast.

For more information about the arguments, see the [`CREATE MODEL` syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series#create_model_syntax).

  3. Click **Run**. Your model appears in the navigation panel.




### Generate and serve insights

You can generate insights by using your machine learning model. For example, if you created an `ARIMA_PLUS` model, then you can use it to generate insights for time series values such as future sales predictions.

#### Generate insights

To generate insights based on a trained model, perform the following steps:

  1. In the [Google Cloud console](https://console.cloud.google.com/bigquery), click the **Compose new query** button.

  2. Enter the following GoogleSQL query in the **Query editor** :
         
         SELECT
         *
         FROM
         ML.FORECAST(MODEL `MODEL_NAME`,
         STRUCT(HORIZON AS horizon, CONFIDENCE_LEVEL AS confidence_level));
         

Replace the following:

     * `MODEL_NAME`: The name of your model that you have trained for generating insights.
     * `HORIZON`: An `INT64` value that specifies the number of time points to forecast.
     * `CONFIDENCE_LEVEL`: A `FLOAT64` value that specifies percentage of the future values that fall in the prediction interval.

For more information about the arguments, see the [The `ML.FORECAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-forecast).

  3. Click **Run**. The ML model provides an output of forecasted values for future dates.

  4. When the query is complete, click the **Results** tab. The results should look like the following:

![Generate and serve insights by using BigQuery ML](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-bq-query-results.png)




#### Serve insights

To serve generated predictions for data driven business decisions from your SAP application by using the ABAP SDK for Google Cloud, you use the [`QUERY_JOBS`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigquery_v2#query_jobs) method of the `/GOOG/CL_BIGQUERY_V2` class.

To help you deploy the example solution explained in this section with minimal effort, a code sample is provided in [GitHub](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/ZGOOG_SDK_BQML_RECIPE). This code sample shows an end-to-end example of generating forecasts of future time series values by using the `ARIMA_PLUS` model and the on-premises or any cloud edition of ABAP SDK for Google Cloud.

## What's next

  * For an overview of BigQuery ML, see [Introduction to BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).
  * To evaluate the available BigQuery machine learning models for your business process and requirements, see [End-to-end user journey for each model](https://docs.cloud.google.com/bigquery/docs/e2e-journey).
  * Instead of performing ad-hoc queries to get BigQuery ML predictions, you can use [Cloud Run](https://cloud.google.com/blog/topics/developers-practitioners/how-trigger-cloud-run-actions-bigquery-events) to automatically generate insights for new or changed data in BigQuery. The generated insights can be written to a temporary BigQuery table, and then retrieved by an SAP application.
  * To extract greater value and insights from your SAP data, you can use the Google Cloud [Cortex Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation) that provides a scalable and extensible data foundation, along with prebuilt data models and pipelines for common business use cases related to SAP.
  * To learn more about the Google Cloud console, see [Using the Google Cloud console](https://docs.cloud.google.com/bigquery/bigquery-web-ui).
  * To learn about ABAP SDK for Google Cloud, see [Overview of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview).
  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Author: [Ajith Urimajalu](https://www.linkedin.com/in/ajith-urimajalu/) | SAP Application Engineer Team Lead

Other contributor: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
