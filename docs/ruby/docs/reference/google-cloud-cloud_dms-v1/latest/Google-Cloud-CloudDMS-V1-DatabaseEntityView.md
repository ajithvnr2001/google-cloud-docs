---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView/
title: Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DatabaseEntityView (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:26.015125+00:00
---

# Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DatabaseEntityView (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Module Google::Cloud::CloudDMS::V1::DatabaseEntityView (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API module Google::Cloud::CloudDMS::V1::DatabaseEntityView.

AIP-157 Partial Response view for Database Entity.

## Constants 

### DATABASE_ENTITY_VIEW_UNSPECIFIED

**value:** 0  
Unspecified view. Defaults to basic view.

### DATABASE_ENTITY_VIEW_BASIC

**value:** 1  
Default view. Does not return DDLs or Issues.

### DATABASE_ENTITY_VIEW_FULL

**value:** 2  
Return full entity details including mappings, ddl and issues.

### DATABASE_ENTITY_VIEW_ROOT_SUMMARY

**value:** 3  
Top-most (Database, Schema) nodes which are returned contains summary details for their decendents such as the number of entities per type and issues rollups. When this view is used, only a single page of result is returned and the page_size property of the request is ignored. The returned page will only include the top-most node types.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
