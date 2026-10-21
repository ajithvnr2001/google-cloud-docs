---
url: https://docs.cloud.google.com/datastream/docs/best-practices-migration-toolkit/
title: Datastream BigQuery Migration Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:44.502702+00:00
---

# Datastream BigQuery Migration Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/best-practices-migration-toolkit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Datastream BigQuery Migration Toolkit Stay organized with collections  Save and categorize content based on your preferences. 

  


This page describes best practices when using Datastream to migrate from the [Dataflow Datastream to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-bigquery) to the [Datastream built-in BigQuery replication solution](https://docs.cloud.google.com/datastream-for-bigquery).

## Before you begin

The instructions on this page assume the following:

  * You are familiar with, and have installed [Docker](https://docs.docker.com/installation/#installation).
  * You know how to clone repositories from services like GitHub.
  * You know how to run streams in Datastream.
  * You have installed the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



## Migration toolkit overview

The Datastream BigQuery Migration Toolkit is an open source software offered by Google Cloud. The toolkit lets you migrate off the Dataflow [Datastream to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/datastream-to-bigquery), but you can also use it when migrating from other pipelines, as explained in the Migrate from other pipelines section that follows.

To migrate your BigQuery tables using the toolkit, you need to perform the following steps:

  1. Create, start and pause a Datastream stream with a BigQuery destination.
  2. Run the migration on each BigQuery table that needs to be migrated.
  3. Resume the stream.



The toolkit does the following:

  * Retrieves the source table schema using the Datastream [discover API](https://docs.cloud.google.com/datastream/docs/using-datastream-apis#creating_and_managing_connection_profiles).
  * Creates a Datastream-compatible BigQuery table based on the retrieved schema.
  * Fetches the schema of the BigQuery table from which you're migrating to determine the necessary data type conversions.
  * Copies all existing rows from the original table to the new table, including appropriate column type [casts](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/conversion_functions#cast).



For more information about the way the toolkit is structured, and the arguments it uses, see the toolkit [`README.md` file](https://github.com/GoogleCloudPlatform/datastream-bigquery-migration-toolkit).

## Set up the migration toolkit

To run the migration toolkit using Docker, perform the following steps:

  1. Clone the repository and change directory into it:
         
         git clone https://github.com/GoogleCloudPlatform/datastream-bigquery-migration-toolkit &&
         cd datastream-bigquery-migration-toolkit
         

  2. Build the image:
         
         docker build -t migration-service .
         

  3. Authenticate with your Google Cloud CLI credentials:
         
         docker run -ti \
         --name gcloud-config migration-service gcloud auth application-default login
         

  4. Set your Google Cloud project property:
         
         docker run -ti --volumes-from gcloud-config migration-service \
         gcloud config set project PROJECT_ID
         

Replace PROJECT_ID with the identifier of your Google Cloud project.




## Migrate from Dataflow to the Datastream built-in solution

  1. Create a Datastream [stream with a BigQuery destination](https://docs.cloud.google.com/datastream/docs/quickstart-replication-to-bigquery#define-stream-settings)

**Note:** When configuring the source, make sure to choose [manual backfill](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedb) under **Choose backfill mode for historical data**.
  2. Start the stream, and immediately pause it. This allows Datastream to capture the position from which it captures changes before the migration starts.

**Note:** Between starting and pausing, Datastream might processes some events and create one or more tables in BigQuery. In such a case, you must manually delete the tables in BigQuery before proceeding with the migration, otherwise the migration fails.
  3. Drain the Datastream and Dataflow pipeline:

     1. Pause the existing Cloud Storage destination stream.
     2. Check the total latency metric for the stream and wait for at least as long as the current latency to ensure that any in-flight events are written to the destination.
     3. [Drain the Dataflow job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain).
  4. Execute the migration:

     1. Run the migration in `dry_run` mode. The `dry_run` mode lets you generate the `CREATE TABLE` DDL statement and the SQL statement for copying data, without executing them:
            
            docker run -v output:/output -ti --volumes-from gcloud-config \
            migration-service python3 ./migration/migrate_table.py dry_run \
            --project-id PROJECT_ID \
            --stream-id STREAM_ID \
            --datastream-region STREAM_REGION \
            --source-schema-name SOURCE_SCHEMA_NAME \
            --source-table-name SOURCE_TABLE_NAME \
            --bigquery-source-dataset-name BIGQUERY_SOURCE_DATASET_NAME \
            --bigquery-source-table-name BIGQUERY_SOURCE_TABLE_NAME
            

Replace the following:

        * PROJECT_ID: The unique identifier of your Google Cloud project.
        * STREAM_ID: The unique identifier of your BigQuery destination stream.
        * STREAM_REGION: The location of your stream, for example `us-central1`.
        * SOURCE_SCHEMA_NAME: The name of the source schema.
        * SOURCE_TABLE_NAME: The name of the source table.
        * BIGQUERY_SOURCE_DATASET_NAME: The name of the existing BigQuery dataset.
        * BIGQUERY_SOURCE_TABLE_NAME: The name of the existing BigQuery table.
     2. Inspect the `.sql` files under `output/create_target_table` and `output/copy_rows`. These are the SQL commands that will be executed in your Google Cloud project:
            
            docker run -v output:/output -ti migration-service find output/create_target_table \
            -type f -print -exec cat {} \;
            
            
            docker run -v output:/output -ti migration-service find output/copy_rows \
            -type f -print -exec cat {} \;
            

     3. To execute the SQL commands, run the migration in `full` mode. The `full` mode lets you create a table in BigQuery and copy all rows from the existing BigQuery table:
            
            docker run -v output:/output -ti --volumes-from gcloud-config \
            migration-service python3 ./migration/migrate_table.py full \
            --project-id PROJECT_ID \
            --stream-id STREAM_ID \
            --datastream-region STREAM_REGION \
            --source-schema-name SOURCE_SCHEMA_NAME \
            --source-table-name SOURCE_TABLE_NAME \
            --bigquery-source-dataset-name BIGQUERY_SOURCE_DATASET_NAME \
            --bigquery-source-table-name BIGQUERY_SOURCE_TABLE_NAME
            

  5. Resume the paused stream.

  6. Open the Google Cloud Logs Explorer, and look for Datastream logs with the following query:
         
         resource.type="datastream.googleapis.com/Stream"
         resource.labels.stream_id=STREAM_ID
         

Look for the following log, where `%d` is a number:
         
         Completed writing %d records into..
         

This log indicates that the new stream successfully loaded data into BigQuery. It only appears if there is CDC data to load.




## Migrate from other pipelines

The toolkit also lets you migrate from other pipelines to the Datastream built-in BigQuery solution. The toolkit can generate `CREATE TABLE` DDLs for Datastream-compatible BigQuery tables, based on the source database schema by using the `dry_run` mode:
    
    
      docker run -v output:/output -ti --volumes-from gcloud-config \
      migration-service python3 ./migration/migrate_table.py dry_run \
      --project-id PROJECT_ID \
      --stream-id STREAM_ID \
      --datastream-region STREAM_REGION \
      --source-schema-name SOURCE_SCHEMA_NAME \
      --source-table-name SOURCE_TABLE_NAME \
      --bigquery-source-dataset-name BIGQUERY_SOURCE_DATASET_NAME \
      --bigquery-source-table-name BIGQUERY_SOURCE_TABLE_NAME
    

Because the BigQuery table schemas might vary, it is difficult to provide a universal SQL statement for copying rows. You can use the schemas in the source table DDL directory (`output/source_table_ddl`) and the destination table DDL directory (`output/create_target_table`) to create a SQL statement with appropriate [casts](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/conversion_functions) on the source columns.

The following is an example SQL statement format that you can use:
    
    
      INSERT INTO DESTINATION_TABLE (DESTINATION_COLUMN1, DESTINATION_COLUMN2...)
      SELECT SOURCE_COLUMN1, SOURCE_COLUMN2
      FROM SOURCE_TABLE;
    

Replace the following:

  * DESTINATION_TABLE: The name of your destination table in BigQuery.
  * DESTINATION_COLUMN: The name of the column in your destination table.
  * SOURCE_COLUMN: The name of the column in your source table.
  * SOURCE_TABLE: The name of your source table.



## Limitations

The toolkit has the following limitations:

  * The column names in the existing and new BigQuery tables need to match (ignoring metadata columns). The migration fails if you apply [Dataflow user-defined functions](https://docs.cloud.google.com/dataflow/docs/guides/templates/create-template-udf) (UDFs) that change the names of the columns in the existing tables (for example, by adding a prefix or changing case).
  * Cross-region and cross-project migrations aren't supported.
  * The migration works on a per-table basis.
  * Only Oracle and MySQL sources are supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
