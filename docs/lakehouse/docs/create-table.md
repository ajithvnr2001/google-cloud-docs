---
url: https://docs.cloud.google.com/lakehouse/docs/create-table/
title: Create a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:45.669429+00:00
---

# Create a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/create-table/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Create a table Stay organized with collections  Save and categorize content based on your preferences. 

Creating an Apache Iceberg table initializes new table metadata and storage within a namespace in the _Lakehouse runtime catalog_.

If you want to make an existing Apache Iceberg table available in the catalog, see [Register a table](https://docs.cloud.google.com/lakehouse/docs/register-table).

If you don't specify an explicit storage location at the namespace or table level during table creation, the system automatically constructs the table's metadata and data directories under the catalog's default location (derived from the catalog's base Cloud Storage bucket) by appending the namespace and table identifiers.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to create a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Create a table: 
    * BigLake Admin (`roles/biglake.admin`) - your project 
    * Storage Admin (`roles/storage.admin`) - the target Cloud Storage bucket 



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



## Create a table

Create an Iceberg table.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. Select an existing namespace or create one if you don't have one.

  4. In the menu bar, click **\+ Create Table**.

  5. For **Table format** , select **Iceberg**.

  6. For **Table name** , enter a unique table name.

  7. Optional: In the **Properties** section, configure table properties. Predefined properties such as `gcp.biglake.bigquery-dml.enabled` and `gcp.biglake.table-management.enabled` are listed.

For example, you can change these values to `true` to enable BigQuery DML or automatic table management. For more information, see [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).

  8. Click **Create**.




Your table appears on the **Namespace details** page.

###  Spark 
    
    
    spark.sql("CREATE TABLE NAMESPACE_NAME.TABLE_NAME (id int, data string) USING ICEBERG;")
    

Replace the following values:

  * `NAMESPACE_NAME`: the name of your [namespace](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#create_a_namespace_or_schema).
  * `TABLE_NAME`: a name for your table.



To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (preview), add the properties to the `TBLPROPERTIES` clause:
    
    
    TBLPROPERTIES (
      'gcp.biglake.bigquery-dml.enabled' = true,
      'gcp.biglake.table-management.enabled' = true
    )
    

###  Trino 
    
    
    CREATE TABLE SCHEMA_NAME.TABLE_NAME (id int, data varchar);
    

Replace the following values:

  * `SCHEMA_NAME`: the name of your [schema](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#create_a_namespace_or_schema).
  * `TABLE_NAME`: a name for your table.



To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (Preview), add these properties to the `WITH` clause:
    
    
    WITH (
      "gcp.biglake.bigquery-dml.enabled" = 'true',
      "gcp.biglake.table-management.enabled" = 'true'
    )
    

###  gcloud 

To create a table using `gcloud`, run the [`gcloud biglake iceberg tables create` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/create).
    
    
    gcloud biglake iceberg tables create \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        --namespace="NAMESPACE_NAME" \
        --create-from-file="TABLE_DEFINITION_FILE"

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.
  * `TABLE_DEFINITION_FILE`: the path to a JSON file containing the Iceberg table definition.



###  BigQuery 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create an Apache Iceberg table in the Lakehouse runtime catalog from BigQuery, use the following GoogleSQL `CREATE TABLE` statement. When you create a table from BigQuery, BigQuery DML and automatic table management are enabled by default.
    
    
    CREATE TABLE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME` (id int, data string);
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `CATALOG_ID`: your Lakehouse runtime catalog ID
  * `NAMESPACE`: your Iceberg namespace name
  * `TABLE_NAME`: a name for your Iceberg table



###  REST 

To create an Iceberg table using the REST API, make a `POST` request to the [`CreateIcebergTable`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/create) endpoint:
    
    
    POST /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables
    

The request body must contain a valid Iceberg `CreateTableRequest` JSON payload defining the table schema, partition spec, and initial properties.

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.



## What's next

  * Learn how to [list tables](https://docs.cloud.google.com/lakehouse/docs/list-tables).
  * Learn how to [insert data into a table](https://docs.cloud.google.com/lakehouse/docs/insert-data).
  * Learn how to [manage table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
