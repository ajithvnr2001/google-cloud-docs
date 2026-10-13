---
url: https://docs.cloud.google.com/lakehouse/docs/query-table/
title: Query a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:47.128501+00:00
---

# Query a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/query-table/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Query a table Stay organized with collections  Save and categorize content based on your preferences. 

Querying a table reads data from the underlying Cloud Storage files using the metadata managed by the _Lakehouse runtime catalog_.

You can run queries from open source engines like Spark and Trino, or directly from BigQuery using a four-part table name syntax (P.C.N.T syntax).

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to query a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Read table data in [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode): BigLake Viewer (`roles/biglake.viewer`) - the project 
  * Read table data in non-credential vending mode: 
    * BigLake Viewer (`roles/biglake.viewer`) - the project 
    * Storage Object Viewer (`roles/storage.objectViewer`) - the Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Table capabilities and support

When using tables in the Lakehouse runtime catalog, it's helpful to [understand the different table types and their opt-in capabilities](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables). To learn more about using Apache Iceberg tables specifically, see [Overview of Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

**Supported Iceberg tables**

Only Apache Iceberg V2 (GA) and V3 (Preview) tables are supported. Iceberg V1 tables aren't supported. To upgrade existing V1 tables, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).

**Use table options (Preview)**

You can opt in to use BigQuery managed capabilities, such as BigQuery Data Manipulation Language (DML) and automatic table management, by configuring specific table properties. These features are enabled in different ways depending on where the table is created:

  * **From BigQuery:** BigQuery DML and automatic table management are enabled by default.
  * **From open source engines:** To opt-in, you must explicitly configure table properties. See [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options) for more information.



When querying tables from BigQuery, you can access standard Iceberg tables as well as tables enabled for BigQuery managed capabilities. See [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options) for detailed instructions.

## Query a table

Select all data from the table:

###  Spark 
    
    
    spark.sql("SELECT * FROM TABLE_NAME;").show()
    

###  Trino 
    
    
    SELECT * FROM TABLE_NAME;
    

###  BigQuery 

To query Apache Iceberg tables in the Lakehouse runtime catalog from BigQuery, use the four-part table name in your query with the following format: `PROJECT_NAME.CATALOG_ID.NAMESPACE_OR_SCHEMA_NAME.TABLE_NAME`.
    
    
    SELECT * FROM `PROJECT_NAME.CATALOG_ID.NAMESPACE_OR_SCHEMA_NAME.TABLE_NAME`;
    

Replace the following values:

  * `PROJECT_NAME`: the Google Cloud project that owns the catalog in the Lakehouse runtime catalog. The selected Google Cloud project in the Google Cloud console is billed for the query.

  * `CATALOG_ID`: the ID of the Lakehouse runtime catalog catalog specified when the catalog was created. This identifier is used as the catalog name in BigQuery queries.

This identifier is also the name of your Cloud Storage bucket.

For example, if you created your bucket to store your catalog and named it `iceberg-bucket`, both your catalog name and bucket name are `iceberg-bucket`. This is used later when you query your catalog in BigQuery, using the P.C.N.T syntax. For example, `my-project.catalog_id.quickstart_namespace.quickstart_table`.

  * `NAMESPACE_OR_SCHEMA_NAME`: the table namespace if using Spark or table schema name if using Trino.

  * `TABLE_NAME`: the name of your table.




## Query using time travel

You can query historical data from your managed Apache Iceberg tables using time travel. You can time travel from BigQuery using the `FOR SYSTEM_TIME AS OF` clause, or from open source engines like Spark using snapshot IDs, timestamps, tags, or branches.

### Query by timestamp

To query data as of a specific timestamp:

###  Spark 
    
    
    SELECT * FROM NAMESPACE.TABLE_NAME TIMESTAMP AS OF '2026-02-26 01:21:00';
    

###  BigQuery 
    
    
    SELECT * FROM `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME` FOR SYSTEM_TIME AS OF '2026-02-26 01:21:00';
    

### Query by snapshot ID

To query data as of a specific snapshot ID:

###  Spark 
    
    
    SELECT * FROM NAMESPACE.TABLE_NAME VERSION AS OF 10963874102873;
    

### Query by tag

To create a tag and query data as of that tag:

###  Spark 
    
    
    -- Create tag 'historical-snapshot'
    ALTER TABLE NAMESPACE.TABLE_NAME CREATE TAG 'historical-snapshot' AS OF VERSION 123456789012345;
    
    -- Query by tag
    SELECT * FROM NAMESPACE.TABLE_NAME VERSION AS OF 'historical-snapshot';
    

### Query by branch

To create a branch and query data as of that branch:

###  Spark 
    
    
    -- Create branch 'audit-branch'
    ALTER TABLE NAMESPACE.TABLE_NAME CREATE BRANCH 'audit-branch' AS OF VERSION 123456789012345;
    
    -- Query by branch
    SELECT * FROM NAMESPACE.TABLE_NAME VERSION AS OF 'audit-branch';
    

## What's next

  * Learn how to [alter a table](https://docs.cloud.google.com/lakehouse/docs/alter-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
