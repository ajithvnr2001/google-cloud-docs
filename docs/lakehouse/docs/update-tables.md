---
url: https://docs.cloud.google.com/lakehouse/docs/update-tables/
title: Upgrade Iceberg V1 tables to V2 \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:40.714370+00:00
---

# Upgrade Iceberg V1 tables to V2  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/update-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Upgrade Iceberg V1 tables to V2 Stay organized with collections  Save and categorize content based on your preferences. 

If you have existing version 1 (V1) Apache Iceberg tables, you must upgrade them using your query engine before using them with the Apache Iceberg REST catalog endpoint. For more information, see [Alter a table](https://docs.cloud.google.com/lakehouse/docs/alter-table).

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to upgrade a table, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Upgrade table in [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode): BigLake Editor (`roles/biglake.editor`) - the project 
  * Upgrade table in non-credential vending mode: 
    * BigLake Editor (`roles/biglake.editor`) - the project 
    * Storage Object User (`roles/storage.objectUser`) - the Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Upgrade a table

To upgrade an Iceberg V1 table to V2, run the following command in your query engine:

###  Spark 
    
    
    ALTER TABLE CATALOG_NAME.SCHEMA_NAME.TABLE_NAME SET TBLPROPERTIES ('format-version'='2');
    

Replace the following:

  * `CATALOG_NAME`: the name of your catalog.
  * `SCHEMA_NAME`: the name of your schema.
  * `TABLE_NAME`: the name of your table.



## What's next

  * Learn how to [configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).
  * Learn how to [alter a table](https://docs.cloud.google.com/lakehouse/docs/alter-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
