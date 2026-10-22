---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-borderless-lakehouse-databricks/
title: Troubleshoot cross-cloud data access for Databricks Unity Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:28:14.429735+00:00
---

# Troubleshoot cross-cloud data access for Databricks Unity Catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-borderless-lakehouse-databricks/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot cross-cloud data access for Databricks Unity Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

Cross-cloud data access in borderless Lakehouse lets you query remote Databricks Unity Catalog tables without moving data. If federated tables don't appear after a metadata refresh, you can diagnose and resolve common permission and storage configuration issues in Unity Catalog. For general cross-cloud data access troubleshooting, such as connectivity and routing over private interconnects, see [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

## Tables are empty or not discovered during refresh

If the catalog background metadata refresh indicates success (such as `Refresh successfully completed`), but tables in the federated catalog do not appear or listing tables returns 0 items, check the following:

  * **`EXTERNAL USE SCHEMA` privilege:** Verify that the Databricks Service Principal has been granted the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog in Unity Catalog. Without this privilege, background metadata refresh and credential vending for queries will fail.
  * **External data access setting:** Verify that **External data access** is enabled on the Databricks Unity Catalog metastore.
  * **External location:** Verify that the Databricks Unity Catalog and tables use an external storage location (such as Cloud Storage or Amazon S3) rather than default storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
