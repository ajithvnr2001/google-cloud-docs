---
url: https://docs.cloud.google.com/lakehouse/docs/list-tables/
title: List tables \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:46.206979+00:00
---

# List tables  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/list-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  List tables Stay organized with collections  Save and categorize content based on your preferences. 

Listing tables lets you view all registered table entities within a namespace in the _Lakehouse runtime catalog_.

Query engines can list tables using standard SQL commands, and you can retrieve table identifiers using the REST API.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to list tables, ask your administrator to grant you the following IAM roles on your project: 

  * List tables: BigLake Viewer (`roles/biglake.viewer`) - your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Table capabilities and support

When using tables in the Lakehouse runtime catalog, it's helpful to [understand the difference between table types](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables). To learn more about using Apache Iceberg tables specifically, see [Overview of Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

**Supported Iceberg tables**

Only Apache Iceberg V2 (GA) and V3 (Preview) tables are supported. Iceberg V1 tables aren't supported. To upgrade existing V1 tables, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).

## List tables

List tables.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.




Your tables appear on the **Namespace details** page.

###  Spark 
    
    
    spark.sql("SHOW TABLES").show()
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (preview), add the properties to the `TBLPROPERTIES` clause:
    
    
    TBLPROPERTIES (
      'gcp.biglake.bigquery-dml.enabled' = true,
      'gcp.biglake.table-management.enabled' = true
    )
    

###  Trino 
    
    
    SHOW TABLES;
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (Preview), add these properties to the `WITH` clause:
    
    
    WITH (
      "gcp.biglake.bigquery-dml.enabled" = 'true',
      "gcp.biglake.table-management.enabled" = 'true'
    )
    

###  gcloud 

To list tables using `gcloud`, run the [`gcloud biglake iceberg tables list` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/list).
    
    
    gcloud biglake iceberg tables list \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        --namespace="NAMESPACE_NAME"

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.



###  BigQuery 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To list Apache Iceberg tables in the Lakehouse runtime catalog from BigQuery, you can explore the **Explorer** pane in the BigQuery console or use the `bq ls` command.

###  REST 

To list table identifiers within a namespace using the REST API, make a `GET` request to the [`ListIcebergTableIdentifiers`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/list) endpoint:
    
    
    GET /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables
    

The response contains a JSON array of table identifiers registered under the specified namespace.

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.



## What's next

  * Learn how to [get table details](https://docs.cloud.google.com/lakehouse/docs/get-table-details).
  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
