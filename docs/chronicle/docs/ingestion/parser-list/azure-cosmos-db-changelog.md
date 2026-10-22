---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-cosmos-db-changelog/
title: Change log for AZURE_COSMOS_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:56.712765+00:00
---

# Change log for AZURE_COSMOS_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-cosmos-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_COSMOS_DB

Date | Changes  
---|---  
2025-01-16 |  Enhancement -  
\- Fixed typo in Azure Cosmos DB CBN and updated timestamp.   
2023-02-22 |  Enhancement -  
\- Mapped `TenantId` to `metadata.product_deployment_id`.  
\- Mapped `Computer` to `principal.hostname`.  
\- Mapped `EventSourceName` to `metadata.product_event_type` and mapped `principal.platform` based on `EventSourceName`.  
\- Mapped `EventID` to `metadata.product_log_id`.  
\- Mapped `Activity` to `metadata.description`.  
\- Mapped `CommandLine` to `target.process.command_line`.  
\- Mapped `Process` to `target.process.file.full_path`.  
\- Mapped `ProcessId` to `target.process.pid`.  
\- Mapped `ParentProcessName` to `target.process.parent_process.file.full_path`.  
\- Mapped `SubjectUserSid` to `principal.user.windows_sid`.  
\- Mapped `SubjectDomainName` to `principal.administrative_domain`.  
\- Mapped `SubjectLogonId` to `principal.user.userid`.  
\- Mapped `SubjectUserName` to `principal.user.user_display_name`.  
\- Mapped `TargetDomainName` to `target.administrative_domain`.  
\- Mapped `TargetLogonId` to `target.user.userid`.  
\- Mapped `TargetUserName` to `target.user.user_display_name`.  
\- Mapped `TargetUserSid` to `target.user.windows_sid`.  
\- Mapped `_ResourceId` to `target.resource.product_object_id`.  
\- Mapped `_Internal_WorkspaceResourceId`, `TokenElevationType` to `target.resource.attribute.labels`  
\- Mapped `Channel`, `Task`, `SourceSystem`, `EventOriginId`, `ManagementGroupName` to `additional.fields`.  
\- Mapped `FilePath` to `target.file.full_path`.  
\- Mapped `FileHash` to `target.file.sha256`.  
\- Mapped `SourceComputerId` to `principal.asset.asset_id`.   
2022-04-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
