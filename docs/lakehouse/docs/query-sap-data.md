---
url: https://docs.cloud.google.com/lakehouse/docs/query-sap-data/
title: Query SAP Business Data Cloud data \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:49.235732+00:00
---

# Query SAP Business Data Cloud data  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/query-sap-data/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Query SAP Business Data Cloud data Stay organized with collections  Save and categorize content based on your preferences. 

After the connection is established and data products are shared, you can discover and query the SAP data in BigQuery. For information on how these products are shared in SAP, see [Working with Data Products in SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/sap-business-data-cloud-connect/working-with-data-products-in-sap-business-data-cloud-connect?locale=en-US&version=LATEST) in the SAP documentation.

By default, borderless Lakehouse automatically refreshes catalog metadata in the background every 5 minutes (`5m` or `300s`). To change the refresh interval for your catalog, update the catalog using `gcloud`:
    
    
    gcloud biglake delta-sharing catalogs update CATALOG_ID \
      --project="PROJECT_ID" \
      --refresh-interval="REFRESH_INTERVAL"

Replace the following:

  * `CATALOG_ID`: the ID of your Lakehouse Delta Sharing catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REFRESH_INTERVAL`: the interval for refreshing metadata, specified as a duration string with units (for example, `5m` for 5 minutes, `300s` for 300 seconds, or `1h` for 1 hour).



The data appears in a hierarchical structure:

`CATALOG_ID.SHARE_NAME.SCHEMA_NAME.TABLE_NAME`.

## List the shares in the catalog

To list shares, use one of the following options:

###  gcloud 
    
    
    gcloud biglake delta-sharing shares list \
      --catalog="CATALOG_ID" \
      --project="PROJECT_ID"

###  REST 
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-Visibility: DELTA_SHARING_PREVIEW" \
      "https://biglake.googleapis.com/deltasharing/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/shares"

Replace the following:

  * `CATALOG_ID`: the ID of your Lakehouse Delta Sharing catalog.
  * `PROJECT_ID`: your Google Cloud project ID.



## List schemas in a share

To list schemas, use one of the following options:

###  gcloud 
    
    
    gcloud biglake delta-sharing schemas list \
      --catalog="CATALOG_ID" \
      --share="SHARE_NAME" \
      --project="PROJECT_ID"

###  REST 
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-Visibility: DELTA_SHARING_PREVIEW" \
      "https://biglake.googleapis.com/deltasharing/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/shares/SHARE_NAME/schemas"

Replace the following:

  * `CATALOG_ID`: the ID of your Lakehouse Delta Sharing catalog.
  * `SHARE_NAME`: the name of the share.
  * `PROJECT_ID`: your Google Cloud project ID.



## List tables in a schema

To list tables, use one of the following options:

###  gcloud 
    
    
    gcloud biglake delta-sharing tables list \
      --catalog="CATALOG_ID" \
      --share="SHARE_NAME" \
      --schema="SCHEMA_NAME" \
      --project="PROJECT_ID"

###  REST 
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-Visibility: DELTA_SHARING_PREVIEW" \
      "https://biglake.googleapis.com/deltasharing/v1/projects/PROJECT_ID/catalogs/CATALOG_ID/shares/SHARE_NAME/schemas/SCHEMA_NAME/tables"

Replace the following:

  * `CATALOG_ID`: the ID of your Lakehouse Delta Sharing catalog.
  * `SHARE_NAME`: the name of the share.
  * `SCHEMA_NAME`: the name of the schema.
  * `PROJECT_ID`: your Google Cloud project ID.



## Query the tables

Query the tables by using standard GoogleSQL in the `bq` CLI, the Google Cloud console, or BigQuery client libraries. Use backticks for each part of the five-part table name when querying:
    
    
    SELECT * FROM `PROJECT_ID`.`CATALOG_ID`.`SHARE_NAME`.`SCHEMA_NAME`.`TABLE_NAME` LIMIT 10

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `CATALOG_ID`: the ID of your Lakehouse Delta Sharing catalog.
  * `SHARE_NAME`: the name of the share.
  * `SCHEMA_NAME`: the name of the schema.
  * `TABLE_NAME`: the name of the table.



## What's next

  * [Publish Data Products to SAP BDC](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc).
  * [Troubleshoot SAP BDC access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
