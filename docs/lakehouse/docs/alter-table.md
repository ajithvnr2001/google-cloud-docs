---
url: https://docs.cloud.google.com/lakehouse/docs/alter-table/
title: Alter a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:18.063295+00:00
---

# Alter a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/alter-table/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Alter a table Stay organized with collections  Save and categorize content based on your preferences. 

Altering a table lets you evolve the schema (such as adding columns) and update table metadata properties.

Modifications are managed by the _Lakehouse runtime catalog_.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to alter a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Alter table in [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode): BigLake Editor (`roles/biglake.editor`) - the project 
  * Alter table in non-credential vending mode: 
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



See [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options) for detailed instructions.

## Alter a table

Add a column to the table:

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the **Namespace details** table, select a table and expand the menu options.

  4. Click **Edit**.

  5. Update the table values in the dialog. In the **Properties** section, you can add or modify properties such as `gcp.biglake.bigquery-dml.enabled` and `gcp.biglake.table-management.enabled` to enable or disable BigQuery DML or automatic table management.

For example, you can set these values to `true` to enable these capabilities. For more information, see [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).

  6. Click **Save**.




###  Spark 
    
    
    spark.sql("ALTER TABLE TABLE_NAME ADD COLUMNS ( desc string);")
    spark.sql("DESCRIBE NAMESPACE_NAME.TABLE_NAME").show()
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options), set the properties using the `SET TBLPROPERTIES` clause:
    
    
    SET TBLPROPERTIES (
      'gcp.biglake.bigquery-dml.enabled' = true,
      'gcp.biglake.table-management.enabled' = true
    )
    

###  Trino 
    
    
    ALTER TABLE TABLE_NAME ADD COLUMN desc varchar;
    DESCRIBE SCHEMA_NAME.TABLE_NAME;
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options), you can configure the following table properties:

  * `'gcp.biglake.bigquery-dml.enabled' = true`
  * `'gcp.biglake.table-management.enabled' = true`



###  gcloud 

To update table properties using `gcloud`, run the [`gcloud biglake iceberg tables update` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/update).
    
    
    gcloud biglake iceberg tables update TABLE_NAME \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        --namespace="NAMESPACE_NAME" \
        --update-properties="KEY=VALUE,..."

Replace the following:

  * `TABLE_NAME`: the name of your Iceberg table.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.
  * `KEY=VALUE,...`: table properties to add or update.



###  BigQuery 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To update table properties for an Apache Iceberg table in the Lakehouse runtime catalog from BigQuery (such as enabling BigQuery DML or automatic table management), use the following GoogleSQL `ALTER TABLE` statement:
    
    
    ALTER TABLE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`
    SET OPTIONS (`properties.gcp.biglake.table-management` = "enabled");
    

To update the schema and add a column in an Apache Iceberg table in the Lakehouse runtime catalog from BigQuery, use the following GoogleSQL `ALTER TABLE` statement:
    
    
    ALTER TABLE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`
    ADD COLUMN new_column STRING;
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: your Lakehouse runtime catalog ID.
  * `NAMESPACE`: your Iceberg namespace name.
  * `TABLE_NAME`: the name of your Iceberg table.



###  REST 

To commit changes to an Iceberg table using the REST API, make a `POST` request to the [`UpdateIcebergTable`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/updateIcebergTable) (`CommitTable`) endpoint:
    
    
    POST /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME
    

The request body must contain a valid Iceberg `CommitTableRequest` JSON payload defining the base requirement and the list of metadata updates to apply.

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.
  * `TABLE_NAME`: the name of your Iceberg table.



## What's next

  * Learn how to [delete a table](https://docs.cloud.google.com/lakehouse/docs/delete-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
