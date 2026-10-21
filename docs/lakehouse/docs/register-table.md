---
url: https://docs.cloud.google.com/lakehouse/docs/register-table/
title: Register a table \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:00.513037+00:00
---

# Register a table  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/register-table/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Register a table Stay organized with collections  Save and categorize content based on your preferences. 

Registering an existing Apache Iceberg table integrates its metadata into the _Lakehouse runtime catalog_ , making table data available for querying and management within a namespace. This process differs from table creation, which initializes a new, empty table structure and its associated storage.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to register a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Register a table: 
    * BigLake Admin (`roles/biglake.admin`) - your project 
    * Storage Admin (`roles/storage.admin`) - the target Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Register a table

Register an existing Iceberg table.

###  gcloud 

To register a table using `gcloud`, run the [`gcloud biglake iceberg tables register` command](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/register).
    
    
    gcloud biglake iceberg tables register TABLE_NAME \
        --project="PROJECT_ID" \
        --catalog="CATALOG_ID" \
        --namespace="NAMESPACE_NAME" \
        --metadata-location="METADATA_LOCATION" \
        [--overwrite]

Replace the following:

  * `TABLE_NAME`: the name to assign to the registered table.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `CATALOG_ID`: the catalog ID.
  * `NAMESPACE_NAME`: the catalog namespace name.
  * `METADATA_LOCATION`: the Cloud Storage URI of the latest metadata JSON file for the table, for example, `gs://my-bucket/path/to/metadata/00001.metadata.json`.
  * `--overwrite`: (Optional) Overwrite the table if it already exists.



###  REST 

To register an Iceberg table using the REST API, make a `POST` request to the [`RegisterIcebergTable`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces/register) endpoint:
    
    
    POST /iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/namespaces/NAMESPACE_NAME/register
    

The request body must contain a JSON payload with the following structure:
    
    
    {
      "name": "TABLE_NAME",
      "metadata-location": "METADATA_LOCATION",
      "overwrite": OVERWRITE
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `CATALOG_ID`: the catalog ID.
  * `NAMESPACE_NAME`: the catalog namespace name.
  * `TABLE_NAME`: the name of the registered table.
  * `METADATA_LOCATION`: the Cloud Storage URI of the latest metadata JSON file for the table.
  * `OVERWRITE`: `true` to overwrite if the table exists, otherwise `false`.



## What's next

  * Learn how to [list tables](https://docs.cloud.google.com/lakehouse/docs/list-tables).
  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).
  * Learn how to [manage table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
