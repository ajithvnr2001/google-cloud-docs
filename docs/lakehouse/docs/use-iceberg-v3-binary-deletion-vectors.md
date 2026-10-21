---
url: https://docs.cloud.google.com/lakehouse/docs/use-iceberg-v3-binary-deletion-vectors/
title: Use binary deletion vectors in Iceberg V3 tables \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:54.673644+00:00
---

# Use binary deletion vectors in Iceberg V3 tables  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-iceberg-v3-binary-deletion-vectors/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use binary deletion vectors in Iceberg V3 tables Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Lakehouse runtime catalog supports Apache Iceberg V3 tables. A core feature of the Apache Iceberg V3 specification is binary deletion vectors. This optimization stores row-level deletions in `.puffin` files. Instead of performing expensive joins at query time, BigQuery and open-source engines (such as Apache Spark, Apache Flink, and Trino) use these vectors to quickly identify and skip deleted rows.

Using binary deletion vectors can improve performance in the following ways:

  * **High-volume writes:** Improves write performance for tables with high-volume writes.
  * **Efficient reads:** Improves query speeds by allowing BigQuery and open-source engines to identify and skip deleted rows.



This is particularly useful for handling high-volume updates and deletes in Change Data Capture (CDC) pipelines, or for meeting regulatory requirements like GDPR (Right to be Forgotten) by deleting specific rows without the overhead of rewriting entire data files.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to create and manage Iceberg V3 tables, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Create and manage Iceberg V3 tables: 
    * BigLake Admin (`roles/biglake.admin`) - your project 
    * Storage Admin (`roles/storage.admin`) - the target Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up the Iceberg REST catalog

Before creating an Iceberg V3 table, you must [set up the Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog), which includes creating a namespace and a catalog.

Setting up the Iceberg REST catalog can take some time to complete. Ensure that you successfully create both the namespace and the catalog before continuing.

## Limitations

Iceberg V3 tables in the Lakehouse runtime catalog have the following limitations:

  * **New V3 data types:** New Iceberg V3 data types (such as Variant, Geography, Nanosecond timestamp, default values, and unknown data types) are not supported.
  * **Row lineage tracking:** Row lineage tracking is not supported.
  * **BigQuery writes:** BigQuery writes are not supported with V3 tables. You can only read V3 tables from BigQuery. To create and write to V3 tables, you must use open-source engines (such as Apache Spark, Apache Flink, or Trino).



## Engine requirements

Ensure you use an engine version that supports Iceberg V3 and binary deletion vectors. Apache Spark 3.5 or higher is recommended. The examples in this guide use `iceberg-spark-runtime-3.5_2.12:1.10.1`.

When configuring your table and engine session, ensure the following:

  * **Table format version:** Must be set to `format-version='3'`.
  * **Delete mode:** Must be set to `merge-on-read`. This mode ensures that deletions are written to separate files (the deletion vectors) rather than rewriting the original data files (copy-on-write).



**Example Spark session configuration**

The following configuration enables the necessary Iceberg extensions and sets up the REST catalog connection:
    
    
    spark-sql \
        --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.10.1,org.apache.iceberg:iceberg-gcp:1.10.1 \
        --jars https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-gcp-bundle/1.10.1/iceberg-gcp-bundle-1.10.1.jar \
        --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
        --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
        --conf spark.sql.catalog.CATALOG_NAME.type=rest \
        --conf spark.sql.catalog.CATALOG_NAME.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog \
        --conf spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_PATH \
        --conf spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project=PROJECT_ID \
        --conf spark.sql.catalog.CATALOG_NAME.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager \
        --conf spark.sql.catalog.CATALOG_NAME.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO \
        --conf spark.sql.defaultCatalog=CATALOG_NAME

Replace the following:

  * `CATALOG_NAME`: the name of your Apache Iceberg REST catalog endpoint.
  * `WAREHOUSE_PATH`: the URI of the Cloud Storage folder where your data warehouse is stored, starting with `gs://`.
  * `PROJECT_ID`: your Google Cloud project ID.



## Use binary deletion vectors

To use binary deletion vectors in Apache Iceberg V3 tables, you must create a table with formatting version 3, populate the table with data, perform standard database modifications, and query the table. You can run all create, insert, delete, and update statements using Spark SQL.

### Create an Iceberg table with binary deletion vectors

Create a table specifying `format-version='3'` and the `merge-on-read` delete, update, and merge modes in the table properties. Run the following statement in Spark SQL:

###  Spark 
    
    
    CREATE NAMESPACE IF NOT EXISTS my_namespace;
    USE my_namespace;
    
    CREATE TABLE my_namespace.mytable_v3 (
       id BIGINT,
       city STRING,
       state STRING
    ) TBLPROPERTIES (
       'format-version'='3',
       'write.delete.mode'='merge-on-read',
       'write.update.mode'='merge-on-read',
       'write.merge.mode'='merge-on-read'
    );
    

#### Upgrade an Iceberg V2 table to V3

You can upgrade an existing Iceberg V2 table to V3 using `ALTER TABLE` statements. Downgrading a table from V3 to V2 is not supported. Run the following statement in Spark SQL:

###  Spark 
    
    
    ALTER TABLE my_namespace.mytable_v2 SET TBLPROPERTIES ('format-version' = '3');
    

### Insert data into the table

To ensure binary deletion vector files are generated for deletions, the engine must not fall back to copy-on-write. This typically requires a significant amount of data to be present in the table before the delete operation. For example, Apache Spark might optimize small deletes by falling back to copy-on-write. Populate the table by running the following statements in Spark SQL:

###  Spark 
    
    
    -- Create a temporary view with a large number of rows (100,000 rows)
    CREATE OR REPLACE TEMPORARY VIEW large_source AS
    SELECT
      id,
      CAST(id AS STRING) as city,
      'WA' as state
    FROM (
      SELECT row_number() OVER (ORDER BY (SELECT NULL)) as id
      FROM (SELECT 0 FROM range(1000)) a
      CROSS JOIN (SELECT 0 FROM range(100)) b
    );
    
    -- Overwrite the existing table with the generated data
    INSERT OVERWRITE my_namespace.mytable_v3 SELECT * FROM large_source;
    

### Delete data

Execute a `DELETE` statement in Spark SQL. Because the table is configured for `merge-on-read` and has sufficient data, Spark generates delete files using binary deletion vectors.

###  Spark 
    
    
    DELETE FROM my_namespace.mytable_v3 WHERE id = 5000;
    

### Update data

Execute an `UPDATE` statement in Spark SQL. Because the table is configured for `merge-on-read` and has sufficient data, Spark generates delete files using binary deletion vectors.

###  Spark 
    
    
    UPDATE my_namespace.mytable_v3 SET state = 'NY' WHERE id = 1;
    

### Query the table

Queries on the table automatically use the binary deletion vector files to exclude deleted rows. You can query the table using Apache Spark or BigQuery.

###  Spark 
    
    
    -- Should be less than the initial 100,000 rows
    SELECT count(*) FROM my_namespace.mytable_v3;
    
    -- Should return no results
    SELECT * FROM my_namespace.mytable_v3 WHERE id = 5000;
    
    -- Should return 'NY'
    SELECT * FROM my_namespace.mytable_v3 WHERE id = 1;
    

###  BigQuery 

When querying from BigQuery, use the fully qualified table identifier `PROJECT_ID.CATALOG_NAME.my_namespace.mytable_v3`.
    
    
    bq query --nouse_legacy_sql \
        'SELECT * FROM `PROJECT_ID.CATALOG_NAME.my_namespace.mytable_v3` LIMIT 10'

## Verify binary deletion vectors creation

You can verify that binary deletion vectors were created successfully by inspecting the storage directory and snapshot metadata.

### Check for `.puffin` files

Navigate to the table's data directory in your Cloud Storage warehouse (for example, `gs://WAREHOUSE_BUCKET/my_namespace/mytable_v3/data`). You should find `.puffin` files, which store the binary deletion vectors.

### Examine snapshot metadata

The snapshot metadata in the Iceberg table's JSON files contains information about the delete operation. Look for properties such as `added-delete-files`, `added-dvs`, and `operation` in the snapshot summary. This confirms that delete files were added.
    
    
    "summary": {
      "operation": "delete",
      "added-delete-files": "1",
      "added-dvs": "1",
      "added-files-size": "42",
      "added-position-deletes": "1",
      ...
    }
    

## What's next

  * Learn about [Manage Apache Iceberg tables in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
