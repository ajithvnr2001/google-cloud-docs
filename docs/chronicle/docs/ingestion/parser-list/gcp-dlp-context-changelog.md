---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dlp-context-changelog/
title: Change log for GCP_DLP_CONTEXT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:02.655106+00:00
---

# Change log for GCP_DLP_CONTEXT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dlp-context-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_DLP_CONTEXT

Date | Changes  
---|---  
2025-01-29 |  Enhancement:  
\- When `tableDataProfile.datasetId` is missing, then mapped `tableDataProfile.cloudSqlDatabaseResourceIdentifier.database` to `entity.resource.product_object_id`.   
2024-09-23 |  Enhancement:  
\- When `fileStoreDataProfile.dataSourceType.dataSource` is `aws`, mapped value `AMAZON S3 BUCKET` to `resource_subtype`.  
\- When `fileStoreDataProfile.dataSourceType.dataSource` is `aws`, mapped value `AMAZON_WEB_SERVICES` to `cloud.environment`.  
\- When `fileStoreDataProfile.dataSourceType.dataSource` is `aws`, mapped value `awsAccountId` as `key` instead of `projectId` for the attribute.label.   
2024-07-31 |  Enhancement:  
\- Changed key for `fileStoreDataProfile.projectId` from `GCS bucket name` to `projectId`.  
\- Mapped `file_store_data_profile.file_store_path`, and `fileStoreDataProfile.fileStorePath` to `entity.resource.product_object_id`.  
\- If `fileStoreDataProfile.fileStorePath` is not present, then mapped `fileStoreDataProfile.name` to `entity.resource.product_object_id`.  
\- Mapped `fileStoreDataProfile.file_store_path` to `entity.file.full_path`.   
2024-06-11 |  Enhancement:  
\- Added support for a new log format type with `fileStoreDataProfile` data fields.   
2022-12-19 |  Bug-fix  
\- Modified mapping of `entity.resource.product_object_id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
