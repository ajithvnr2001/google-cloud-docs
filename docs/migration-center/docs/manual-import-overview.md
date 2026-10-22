---
url: https://docs.cloud.google.com/migration-center/docs/manual-import-overview/
title: Manual data import overview \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:12.823690+00:00
---

# Manual data import overview  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/manual-import-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Manual data import overview Stay organized with collections  Save and categorize content based on your preferences. 

If you don't want to install and run the [discovery client](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) or run the[`mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview) in your infrastructure, you can manually upload your infrastructure data into Migration Center.

This page describes the options available for manually importing data based on your source environment, and helps you choose the best method for your needs.

## Choose an import method

You can manually import data into Migration Center by uploading files that contain data collected from your source environment by using tools such as RVTools. The import method that you choose depends on your source environment and on the type of assets that you want to import.

To manually import your infrastructure data in Migration Center, you typically perform two steps:

  1. Create data files about your infrastructure, or collect data using discovery tools.
  2. Upload or export the data to Migration Center where it is processed and analyzed.



Use the following table to find an import method for your use case.

Import data from | Recommended method | Description  
---|---|---  
**Servers and VMs** | **Manual table upload** | If you want to upload data that can't be collected by using discovery client or `mcdc` CLI, use the [available data templates](https://docs.cloud.google.com/migration-center/docs/import-data-tables#available_data_templates) and then [upload the tables](https://docs.cloud.google.com/migration-center/docs/import-data-tables#upload_the_tables) to Migration Center.  
**VMware vCenter** | **RVTools file upload** | Use [RVTools](https://www.robware.net/rvtools/) version 4.3.1 or later to export your VM data to an XLSX or CSV file, then [Import RVTools data](https://docs.cloud.google.com/migration-center/docs/import-data-rvtools) to Migration Center.  
**Databases** | **Database discovery scripts** | To import data from Microsoft SQL Server, MySQL, or PostgreSQL databases, see [discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases).  
  
## Limitations

Regardless of the method you use to import your infrastructure data into Migration Center, you can create a maximum of 100,000 assets per project.

Learn more about [Quotas and limits](https://docs.cloud.google.com/migration-center/docs/quotas).

## What's next

  * Learn how to [manually fill in and upload data with template tables](https://docs.cloud.google.com/migration-center/docs/import-data-tables).
  * Learn how to [import data generated with RVTools](https://docs.cloud.google.com/migration-center/docs/import-data-rvtools).
  * Learn how to [discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
