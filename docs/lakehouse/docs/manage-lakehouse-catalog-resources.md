---
url: https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources/
title: Create and manage resources in the Lakehouse runtime catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:43.589359+00:00
---

# Create and manage resources in the Lakehouse runtime catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Create and manage resources in the Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ supports resource management through the _Lakehouse runtime catalog_.

This shared catalog eliminates the requirement to maintain multiple catalogs for open source workloads across different data processing engines. Supported operations include creating, viewing, modifying, and deleting resources such as namespaces and tables.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigQuery, BigQuery Storage, and Managed Service for Apache Spark APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,bigquerystorage.googleapis.com,dataproc.googleapis.com)




### Required roles

To get the permissions that you need to manage Apache Iceberg resources in the Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles on your project: 

  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create catalog resources

The following sections describe how to create resources in the Lakehouse runtime catalog.

### Create namespaces

Select one of the following options:

###  API 

Use the [`datasets.insert` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/insert), and specify the [`ExternalCatalogDatasetOptions` field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#externalcatalogdatasetoptions) in the [dataset resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) that you pass in.
    
    
    {
      "datasetReference": {
        "projectId": "PROJECT_ID",
        "datasetId": "DATASET_ID"
      },
      "externalCatalogDatasetOptions": {
        "defaultStorageLocationUri": "URI",
        "parameters": {
          ...
        }
      },
      "location": "LOCATION"
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains your target dataset.
  * `DATASET_ID`: the ID of your target dataset.
  * `URI`: the [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for all tables in the dataset.
  * `LOCATION`: the [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations) that you want to create the dataset in.



###  Apache Spark SQL 
    
    
    CREATE NAMESPACE SPARK_CATALOG.NAMESPACE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your new namespace.



###  Terraform 
    
    
    provider "google" {
      project = "PROJECT_ID"
    }
    
    resource "google_bigquery_dataset" "default" {
      dataset_id = "DATASET_ID"
      location   = "LOCATION"
    
      external_catalog_dataset_options {
        default_storage_location_uri = "URI"
        parameters = {
          ...
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains your target dataset.
  * `DATASET_ID`: the ID of your target dataset.
  * `LOCATION`: the [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations) that you want to create the dataset in.
  * `URI`: the [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for all tables in the dataset.



### Create Apache Iceberg tables

Select one of the following options:

###  API 

Use the [`tables.insert` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/insert), and specify the [`ExternalCatalogTableOptions` field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#ExternalCatalogTableOptions) in the [table resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) that you pass in.
    
    
    {
      "tableReference": {
        "projectId": "PROJECT_ID",
        "datasetId": "DATASET_ID",
        "tableId": "TABLE_ID"
      },
      "externalCatalogTableOptions": {
        "parameters": {
          "table_type": "iceberg",
          "metadata_location": "METADATA_URI"
        },
        "connection_id": "CONNECTION_ID"
      }
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains your target table.
  * `DATASET_ID`: the ID of the dataset that contains your target table.
  * `TABLE_ID`: the ID of your target table.
  * `METADATA_URI`: the [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for the latest Apache Iceberg metadata file. For example, `gs://mybucket/mytable/metadata/1234.metadata.json`.
  * `CONNECTION_ID`: the ID of your connection to Cloud Storage.



###  Apache Spark SQL 
    
    
    CREATE TABLE SPARK_CATALOG.NAMESPACE.TABLE
      (id bigint, data string) USING iceberg;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.
  * `TABLE`: the name of your new table.



###  Terraform 
    
    
    resource "google_bigquery_table" "default" {
      deletion_protection = false
      dataset_id          = google_bigquery_dataset.default.dataset_id
      table_id            = "TABLE"
    
      external_catalog_table_options {
        storage_descriptor {
          location_uri  = "STORAGE_URI"
          input_format  = "org.apache.hadoop.mapred.FileInputFormat"
          output_format = "org.apache.hadoop.mapred.FileOutputFormat"
        }
        parameters = {
          "table_type"        = "iceberg"
          "metadata_location" = "METADATA_URI"
          "write.parquet.compression-codec" : "zstd"
          "EXTERNAL" : "TRUE"
        }
      }
    }

Replace the following:

  * `TABLE`: the name of the target table.
  * `STORAGE_URI`: the Cloud Storage URI where the table data is stored, starting with `gs://`.
  * `METADATA_URI`: the [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for the latest Apache Iceberg metadata file. For example, `gs://mybucket/mytable/metadata/1234.metadata.json`.



## View catalog resources

The following sections describe how to view resources in the Lakehouse runtime catalog.

### View namespaces

Select one of the following options:

###  API 

Use the [`datasets.list` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/list) to view all namespaces, or use the [`datasets.get` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/get) to view information about a defined namespace.

###  Apache Spark SQL 

To view all namespaces in a catalog, use the following statement:
    
    
    SHOW { DATABASES | NAMESPACES } IN SPARK_CATALOG;

Replace `SPARK_CATALOG` with the name of your Apache Spark catalog.

To view information about a defined namespace, use the following statement:
    
    
    DESCRIBE { DATABASE | NAMESPACE } [EXTENDED]
    SPARK_CATALOG.NAMESPACE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.



### View tables

Select one of the following options:

###  API 

Use the [`tables.list` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/list) to view all tables in a namespace, or use the [`tables.get` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/get) to view information about a defined table.

###  Apache Spark SQL 

To view all tables in a namespace, use the following statement:
    
    
    SHOW TABLES IN SPARK_CATALOG.NAMESPACE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.



To view information about a defined table, use the following statement:
    
    
    DESCRIBE TABLE [EXTENDED]
    SPARK_CATALOG.NAMESPACE.TABLE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.
  * `TABLE`: the name of your table.



## Modify catalog resources

**Caution:** Modifying Lakehouse runtime catalog resources using the BigQuery API risks making changes that are incompatible with the external engine.

The following sections describe how to modify resources in the Lakehouse runtime catalog.

### Update namespaces

Select one of the following options:

###  API 

Use the [`datasets.patch` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/patch), and update the [`ExternalCatalogDatasetOptions` field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#externalcatalogdatasetoptions) in the [dataset resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets). The `datasets.update` method is not recommended because it replaces the entire dataset resource.

###  Apache Spark SQL 

Use the [`ALTER DATABASE` statement](https://spark.apache.org/docs/3.5.1/sql-ref-syntax-ddl-alter-database.html).

### Update Apache Iceberg tables

Select one of the following options:

###  API 

Use the [`tables.patch` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/patch), and update the [`ExternalCatalogTableOptions` field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#ExternalCatalogTableOptions) in the [table resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables). The `tables.update` method is not recommended because it replaces the entire table resource.

To update the schema or metadata file, use the `tables.patch` method and set the `autodetect_schema` property to true:
    
    
    PATCH https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID?autodetect_schema=true

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the table that you want to update.
  * `DATASET_ID`: the ID of the dataset that contains the table that you want to update.
  * `TABLE_ID`: the ID of the table that you want to update.



In the body of the request, specify the updated value for each field. For example, to update the Apache Iceberg table's metadata location, specify the updated value for the `metadata_location` field:
    
    
    {
      "externalCatalogTableOptions": {
        "parameters": {"metadata_location": "METADATA_URI"}
      },
      "schema": null
    }'

Replace `METADATA_URI` with the [Cloud Storage URI](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#gcs-uri) for the latest Apache Iceberg metadata file. For example, `gs://mybucket/mytable/metadata/1234.metadata.json`.

###  Apache Spark SQL 

Use the [`ALTER TABLE` statement](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table).

## Delete catalog resources

The following sections describe how to delete resources in the Lakehouse runtime catalog.

### Delete namespaces

Select one of the following options:

###  API 

Use the [`datasets.delete` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/delete). Set the `deleteContents` parameter to true to delete the tables in your namespace.

###  Apache Spark SQL 
    
    
    DROP NAMESPACE SPARK_CATALOG.NAMESPACE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.



### Delete tables

Select one of the following options:

###  API 

Use the [`tables.delete` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/delete) and specify the name of the table. This method doesn't delete the associated files in Cloud Storage.

###  Apache Spark SQL 

To only drop the table, use the following statement:
    
    
    DROP TABLE SPARK_CATALOG.NAMESPACE.TABLE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.
  * `TABLE`: the name of the table to drop.



To drop the table and delete the associated files in Cloud Storage, use the following statement:
    
    
    DROP TABLE SPARK_CATALOG.NAMESPACE.TABLE PURGE;

Replace the following:

  * `SPARK_CATALOG`: the name of your Apache Spark catalog.
  * `NAMESPACE`: the name of your namespace.
  * `TABLE`: the name of the table to delete.



## What's next

  * Learn about [additional Lakehouse runtime catalog features](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
