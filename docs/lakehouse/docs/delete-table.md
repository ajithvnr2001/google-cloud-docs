---
url: https://docs.cloud.google.com/lakehouse/docs/delete-table/
title: Delete a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:55.114257+00:00
---

# Delete a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/delete-table/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Delete a table Stay organized with collections  Save and categorize content based on your preferences. 

Deleting or dropping a table only removes the table registration and metadata from the _Lakehouse runtime catalog_. The underlying data files stored in Cloud Storage aren't purged or deleted.

You can delete a table by using the Google Cloud console, SQL drop commands in Spark and Trino, or the REST API.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to delete a table, ask your administrator to grant you the following IAM roles on your project: 

  * Delete a table: BigLake Admin (`roles/biglake.admin`) - your project 



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



Deleting a table registration from the catalog removes the table regardless of whether it's a standard Iceberg table or a table enabled for BigQuery managed capabilities. See [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options) to understand how table deletion interacts with background table management jobs.

## Delete a table

Delete a table.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the **Namespace details** table, select a table and expand the menu options.

  4. Click **Delete**.

  5. Confirm the deletion by entering the table name in the dialog.

  6. Click **Delete**.




###  Spark 
    
    
    spark.sql("DROP TABLE TABLE_NAME;")
    
    
    
    DROP TABLE TABLE_NAME;
    

###  gcloud 

To delete a table using `gcloud`, run the [`gcloud biglake iceberg tables delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/delete).
    
    
    gcloud biglake iceberg tables delete TABLE_NAME \
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

To delete an Apache Iceberg table registration in the Lakehouse runtime catalog from BigQuery, use the following GoogleSQL `DROP TABLE` statement:
    
    
    DROP TABLE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`;
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: your Lakehouse runtime catalog ID.
  * `NAMESPACE`: your Iceberg namespace name.
  * `TABLE_NAME`: the name of your Iceberg table.



###  REST 

To delete an Iceberg table registration by using the REST API, make a `DELETE` request to the [`DeleteIcebergTable`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/delete) endpoint:
    
    
    DELETE /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your catalog.
  * `NAMESPACE_NAME`: the name of your catalog namespace.
  * `TABLE_NAME`: the name of your Iceberg table.



## What's next

  * See the [Apache Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
