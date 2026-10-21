---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-borderless-lakehouse-databricks/
title: Troubleshoot borderless Lakehouse for Databricks Unity Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:51.731270+00:00
---

# Troubleshoot borderless Lakehouse for Databricks Unity Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-borderless-lakehouse-databricks/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot borderless Lakehouse for Databricks Unity Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

This page shows you how to resolve common issues when querying remote data in Databricks Unity Catalog with borderless Lakehouse. For general borderless Lakehouse troubleshooting (including connectivity and routing over private interconnects), see [Troubleshoot borderless Lakehouse issues](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

## Tables are empty or not discovered during refresh

If the catalog background metadata refresh indicates success (such as `Refresh successfully completed`), but tables in the federated catalog do not appear or listing tables returns 0 items, check the following:

  * **`EXTERNAL USE SCHEMA` privilege:** Verify that the Databricks Service Principal has been granted the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog in Unity Catalog. Without this privilege, background metadata refresh and credential vending for queries will fail.
  * **External data access setting:** Verify that **External data access** is enabled on the Databricks Unity Catalog metastore.
  * **External location:** Verify that the Databricks Unity Catalog and tables use an external storage location (such as Cloud Storage or Amazon S3) rather than default storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
