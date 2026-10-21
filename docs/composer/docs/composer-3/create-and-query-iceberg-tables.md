---
url: https://docs.cloud.google.com/composer/docs/composer-3/create-and-query-iceberg-tables/
title: Create and query BigLake Iceberg tables in BigQuery \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:15.486632+00:00
---

# Create and query BigLake Iceberg tables in BigQuery  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/create-and-query-iceberg-tables/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Create and query BigLake Iceberg tables in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/create-and-query-iceberg-tables "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page explains how to create and modify BigLake Iceberg tables in BigQuery using Airflow operators in your Managed Airflow environment.

## About BigLake Iceberg tables in BigQuery

[BigLake Iceberg tables in BigQuery](https://docs.cloud.google.com/bigquery/docs/iceberg-tables) provide the foundation for building open-format lakehouses on Google Cloud. BigLake Iceberg tables in BigQuery offer the same fully managed experience as standard BigQuery tables, but store data in customer-owned storage buckets. BigLake Iceberg tables in BigQuery support the open Iceberg table format for better interoperability with open-source and third-party compute engines on a single copy of data.

## Before you begin

  * Make sure that you're familiar with [limitations for BigLake Iceberg tables in BigQuery](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#limitations). The same limitations apply when working with BigLake Iceberg tables through Airflow operators.

  * Create a [Cloud Resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection) for the Cloud Storage bucket where your BigLake Iceberg table will be located.

  * Make sure that IAM permissions are assigned as follows:

    * The **[service account of your environment](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account)** must have IAM roles for working with BigLake Iceberg tables in BigQuery. Follow the instructions outlined in [BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#required-roles).

    * The **service account associated with the Cloud Resource connection** must have IAM roles for reading and writing data in Cloud Storage. Follow the instructions outlined in [BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#required-roles).




## Create a BigLake Iceberg table in BigQuery

To create a BigLake Iceberg table in BigQuery, use BigQueryCreateTableOperator in the same way as for other BigQuery tables. In the `biglakeConfiguration` field, provide configuration for the table.
    
    
    import datetime
    
    from airflow.models.dag import DAG
    from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateTableOperator
    
    with DAG(
      "bq_iceberg_dag",
      start_date=datetime.datetime(2025, 1, 1),
      schedule=None,
      ) as dag:
    
      create_iceberg_table = BigQueryCreateTableOperator(
        task_id="create_iceberg_table",
        project_id="PROJECT_ID",
        dataset_id="DATASET_ID",
        table_id="TABLE_NAME",
        table_resource={
          "schema": {
            "fields": [
              {"name": "order_id", "type": "INTEGER", "mode": "REQUIRED"},
              {"name": "customer_id", "type": "INTEGER", "mode": "REQUIRED"},
              {"name": "amount", "type": "INTEGER", "mode": "REQUIRED"},
              {"name": "created_at", "type": "TIMESTAMP", "mode": "REQUIRED"},
            ]
          },
          "biglakeConfiguration": {
            "connectionId": "CONNECTION_NAME",
            "storageUri": "STORAGE_URI",
            "fileFormat": "PARQUET",
            "tableFormat": "ICEBERG",
          }
        }
      )
    

Replace the following:

  * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `DATASET_ID`: an existing dataset.
  * `TABLE_NAME`: the name of the table you're creating.
  * `CONNECTION_NAME`: the name of the [Cloud Resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection) in the `projects/PROJECT_ID/locations/REGION/connections/CONNECTION_ID` format.
  * `STORAGE_URI`: a fully qualified [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for the table. For example, `gs://example-bucket/iceberg-table`.



## Query a BigLake Iceberg table in BigQuery

After you create a BigLake Iceberg table, you can query it with BigQueryInsertJobOperator as usual. The operator doesn't need additional configuration specifically for BigLake Iceberg tables.
    
    
    import datetime
    
    from airflow.models.dag import DAG
    from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
    
    with DAG(
      "bq_iceberg_dag_query",
      start_date=datetime.datetime(2025, 1, 1),
      schedule=None,
      ) as dag:
    
      insert_values = BigQueryInsertJobOperator(
        task_id="iceberg_insert_values",
        configuration={
          "query": {
            "query": f"""
              INSERT INTO `TABLE_ID` (order_id, customer_id, amount, created_at)
              VALUES
                (101, 19, 1, TIMESTAMP '2025-09-15 10:15:00+00'),
                (102, 35, 2, TIMESTAMP '2025-09-14 10:15:00+00'),
                (103, 36, 3, TIMESTAMP '2025-09-12 10:15:00+00'),
                (104, 37, 4, TIMESTAMP '2025-09-11 10:15:00+00')
            """,
            "useLegacySql": False,
            }
          }
      )
    

Replace the following:

  * `TABLE_ID` with the table ID, in the `PROJECT_ID.DATASET_ID.TABLE_NAME` format.



## What's next

  * [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-3/schedule-and-trigger-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
