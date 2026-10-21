---
url: https://docs.cloud.google.com/lakehouse/docs/insert-data/
title: Insert data into a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:45.902138+00:00
---

# Insert data into a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/insert-data/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Insert data into a table Stay organized with collections  Save and categorize content based on your preferences. 

Inserting data appends new records to your Apache Iceberg table.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to insert data into a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Write table data in [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode): BigLake Editor (`roles/biglake.editor`) - the project 
  * Write table data in non-credential vending mode: 
    * BigLake Editor (`roles/biglake.editor`) - the project 
    * Storage Object User (`roles/storage.objectUser`) - the Cloud Storage bucket 



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



## Insert data into the table

Insert sample data into the table.

To insert data from BigQuery, the table must have BigQuery DML enabled (`gcp.biglake.bigquery-dml.enabled = true`). See [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options) for detailed instructions.

###  Spark 
    
    
    spark.sql("INSERT INTO TABLE_NAME VALUES (1, \"first row\"), (2, \"second row\"), (3, \"third row\");")
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (preview), add the properties to the `TBLPROPERTIES` clause:
    
    
    TBLPROPERTIES (
      'gcp.biglake.bigquery-dml.enabled' = true,
      'gcp.biglake.table-management.enabled' = true
    )
    

###  Trino 
    
    
    INSERT INTO TABLE_NAME VALUES (1, 'first row'), (2, 'second row'), (3, 'third row');
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (Preview), add these properties to the `WITH` clause:
    
    
    WITH (
      "gcp.biglake.bigquery-dml.enabled" = 'true',
      "gcp.biglake.table-management.enabled" = 'true'
    )
    

###  BigQuery 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To insert data into an Apache Iceberg table in the Lakehouse runtime catalog from BigQuery, the table must have BigQuery DML enabled. Use the following GoogleSQL `INSERT` statement:
    
    
    INSERT INTO `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME` VALUES (1, "foo");
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: your Lakehouse runtime catalog ID.
  * `NAMESPACE`: your Iceberg namespace name.
  * `TABLE_NAME`: the name of your Iceberg table.



## What's next

  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
