---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veeam-changelog/
title: Change log for VEEAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:57:16.299483+00:00
---

# Change log for VEEAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veeam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VEEAM

Date | Changes  
---|---  
2026-05-26 |  Enhancement:  
\- Added new grok patterns to parse new log formats.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `DeploymentType`, `ConnectionType_RegionType`, `ConnectionType_AuthType`, `ConnectionType_CustomVeeamAppEnabled`, `eoc_grp`, `eoc_ucs`, `eoc_aat`, `soc_enabled`, `soc_grp`, `soc_aat`, `mtc_enabled`, `mtcga_enabled`, `mc_enabled`, and `eoc_enabled` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `BackupAccountsCount` and `BackupAppsCount` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `process_thread_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `OrganizationID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2024-10-24 |  \- Added a Grok pattern to parse new pattern of logs.  
\- Mapped `enterpriseId` to `additional.fields`.  
\- Mapped `recipient_emailid` to `additional.fields`.  
\- Mapped `subject` to "additional.fields.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `version` to `additional.fields`.  
\- Mapped `categoryId` to `additional.fields`.  
\- Mapped `instanceId` to `additional.fields`.  
\- Mapped `UserName` to principal.user_display_name.  
\- Mapped `VbrVersion` to `metadata.product_version`.   
2024-09-23 |  \- Added a Grok pattern to parse new pattern of logs.   
2024-05-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
