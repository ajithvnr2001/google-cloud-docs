---
url: https://docs.cloud.google.com/lakehouse/docs/get-table-details/
title: Get table details \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:00.816293+00:00
---

# Get table details  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/get-table-details/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Get table details Stay organized with collections  Save and categorize content based on your preferences. 

Viewing table details exposes the underlying schema, table properties, and configuration metadata for an Apache Iceberg table in the _Lakehouse runtime catalog_.

In credential vending mode, query engines also retrieve short-lived access credentials to interact safely with underlying Cloud Storage files without requiring direct IAM storage permissions.

You can inspect table details using the Google Cloud console, SQL `DESCRIBE` commands in Spark and Trino, or the REST API.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to view table details, ask your administrator to grant you the following IAM roles on your project: 

  * View table details: BigLake Viewer (`roles/biglake.viewer`) - your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Table capabilities and support

When using tables in the Lakehouse runtime catalog, it's helpful to [understand the different table types and their opt-in capabilities](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables). To learn more about using Apache Iceberg tables specifically, see [Overview of Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

**Supported Iceberg tables**

Only Apache Iceberg V2 (GA) and V3 (Preview) tables are supported. Iceberg V1 tables aren't supported. To upgrade existing V1 tables, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).

## Get table details

Inspect table schema and properties.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the **Namespace details** table, click the name of the table you want to inspect.

  4. On the **Table details** page, explore the table's schema, partition specification, and metadata properties.




###  Spark 
    
    
    spark.sql("DESCRIBE EXTENDED NAMESPACE_NAME.TABLE_NAME").show()
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (preview), add the properties to the `TBLPROPERTIES` clause:
    
    
    TBLPROPERTIES (
      'gcp.biglake.bigquery-dml.enabled' = true,
      'gcp.biglake.table-management.enabled' = true
    )
    

###  Trino 
    
    
    DESCRIBE SCHEMA_NAME.TABLE_NAME;
    

To enable [read/write interoperability and table management](https://docs.cloud.google.com/lakehouse/docs/table-options) (Preview), add these properties to the `WITH` clause:
    
    
    WITH (
      "gcp.biglake.bigquery-dml.enabled" = 'true',
      "gcp.biglake.table-management.enabled" = 'true'
    )
    

###  gcloud 

To describe a table using `gcloud`, run the [`gcloud biglake iceberg tables describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/describe).
    
    
    gcloud biglake iceberg tables describe TABLE_NAME \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        --namespace="NAMESPACE_NAME"

Replace the following:

  * `TABLE_NAME`: the name of your Iceberg table.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.



###  BigQuery 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view table details and metadata properties for an Apache Iceberg table in the Lakehouse runtime catalog from BigQuery, you can examine the table details in the BigQuery console or use the `bq show` command.

###  REST 

To retrieve table metadata using the REST API, make a `GET` request to the [`GetIcebergTable`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/get) endpoint:
    
    
    GET /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME
    

To load short-lived table credentials in credential vending mode, make a `GET` request to the [`LoadIcebergTableCredentials`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/credentials) endpoint:
    
    
    GET /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME/credentials
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your Lakehouse runtime catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.
  * `TABLE_NAME`: the name of your Iceberg table.



## What's next

  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).
  * Learn how to [alter a table](https://docs.cloud.google.com/lakehouse/docs/alter-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
