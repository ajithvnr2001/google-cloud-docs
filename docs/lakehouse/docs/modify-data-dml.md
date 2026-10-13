---
url: https://docs.cloud.google.com/lakehouse/docs/modify-data-dml/
title: Modify data with DML statements \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:46.431946+00:00
---

# Modify data with DML statements  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/modify-data-dml/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Modify data with DML statements Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Modifying data lets you update, delete and merge records in your Apache Iceberg tables in the _Lakehouse runtime catalog_.

When [BigQuery DML is enabled](https://docs.cloud.google.com/lakehouse/docs/table-options) on your table, you can run standard DML statements from BigQuery alongside open source engines like Spark and Trino, achieving full write interoperability on a single copy of data stored in Cloud Storage.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to modify data in a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

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



## Update data

Update existing rows in the table:

###  Spark 
    
    
    ALTER TABLE TABLE_NAME SET TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = true);
    
    UPDATE TABLE_NAME SET data = 'updated row' WHERE id = 1;
    

###  Trino 
    
    
    ALTER TABLE TABLE_NAME SET PROPERTIES "gcp.biglake.bigquery-dml.enabled" = 'true';
    
    UPDATE TABLE_NAME SET data = 'updated row' WHERE id = 1;
    

###  BigQuery 
    
    
    UPDATE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`
    SET data = "updated row"
    WHERE id = 1;
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: your Lakehouse runtime catalog ID.
  * `NAMESPACE`: your Iceberg namespace name.
  * `TABLE_NAME`: the name of your Iceberg table.



## Delete data

Delete specific rows from the table:

###  Spark 
    
    
    ALTER TABLE TABLE_NAME SET TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = true);
    
    DELETE FROM TABLE_NAME WHERE id = 1;
    

###  Trino 
    
    
    ALTER TABLE TABLE_NAME SET PROPERTIES "gcp.biglake.bigquery-dml.enabled" = 'true';
    
    DELETE FROM TABLE_NAME WHERE id = 1;
    

###  BigQuery 
    
    
    DELETE FROM `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`
    WHERE id = 1;
    

## Merge data

Merge data from a source table into your target Iceberg table:

###  Spark 
    
    
    ALTER TABLE TARGET_TABLE SET TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = true);
    
    MERGE INTO TARGET_TABLE t
    USING SOURCE_TABLE s
    ON t.id = s.id
    WHEN MATCHED THEN
      UPDATE SET t.data = s.data
    WHEN NOT MATCHED THEN
      INSERT (id, data) VALUES (s.id, s.data);
    

###  Trino 
    
    
    ALTER TABLE TARGET_TABLE SET PROPERTIES "gcp.biglake.bigquery-dml.enabled" = 'true';
    
    MERGE INTO TARGET_TABLE t
    USING SOURCE_TABLE s
    ON t.id = s.id
    WHEN MATCHED THEN
      UPDATE SET t.data = s.data
    WHEN NOT MATCHED THEN
      INSERT (id, data) VALUES (s.id, s.data);
    

###  BigQuery 
    
    
    MERGE `PROJECT_ID.CATALOG_ID.NAMESPACE.TARGET_TABLE` t
    USING `PROJECT_ID.CATALOG_ID.NAMESPACE.SOURCE_TABLE` s
    ON t.id = s.id
    WHEN MATCHED THEN
      UPDATE SET data = s.data
    WHEN NOT MATCHED THEN
      INSERT (id, data) VALUES (id, data);
    

## What's next

  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).
  * Learn how to [configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
