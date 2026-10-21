---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-ios-changelog/
title: Change log for MICROSOFT_DEFENDER_ENDPOINT_IOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:57:51.067258+00:00
---

# Change log for MICROSOFT_DEFENDER_ENDPOINT_IOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-ios-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_DEFENDER_ENDPOINT_IOS

Date | Changes  
---|---  
2026-08-05 |  \- Updated the parser `Category` details.   
2025-03-10 |  \- Mapped `_TimeReceivedBySvc` to `additional.fields`.  
\- Mapped `properties.DeviceId` to `principal.asset.asset_id`.  
\- Mapped `properties.InitiatingProcessVersionInfoCompanyName` to `principal.user.company_name`.  
\- Mapped `properties.DeviceName` to `principal.hostname and principal.asset.hostname`.  
\- Mapped `properties.InitiatingProcessId` to `principal.process.pid`.  
\- Mapped `properties.InitiatingProcessUniqueId` to `additional.fields`.  
\- Mapped `properties.InitiatingProcessCreationTime` to `principal.resource.attribute.labels`.  
\- Mapped `properties.MachineGroup` to `additional.fields`.  
\- Mapped `properties.Timestamp` to `metadata.event_timestamp`.  
\- Mapped `properties.ProcessTokenElevation` to `target.resource.attribute.labels`.  
\- Mapped `properties.IsProcessRemoteSession` to `additional.fields`.  
\- Mapped `properties.InitiatingProcessCommandLine` to `principal.process.command_line`.  
\- Mapped `properties.IsInitiatingProcessRemoteSession` to `additional.fields`.  
\- Mapped `properties.InitiatingProcessParentFileName` to `principal.process.parent_process.file.full_path`.  
\- Mapped `properties.InitiatingProcessParentId` to `principal.process.parent_process.pid`.  
\- Mapped `properties.InitiatingProcessSessionId` to `additional.fields`.  
\- Mapped `properties.InitiatingProcessParentCreationTime` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessSHA1` to `principal.process.file.sha1`.  
\- Mapped `properties.InitiatingProcessMD5` to `principal.process.file.md5`.  
\- Mapped `properties.InitiatingProcessFileName` to `principal.process.file.names`.  
\- Mapped `properties.InitiatingProcessFolderPath` to `principal.process.file.full_path`.  
\- Mapped `properties.InitiatingProcessVersionInfoOriginalFileName` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessVersionInfoFileDescription` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessVersionInfoInternalFileName` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessAccountName` to `principal.user.userid`.  
\- Mapped `properties.InitiatingProcessAccountDomain` to `principal.administrative_domain`.  
\- Mapped `properties.InitiatingProcessVersionInfoProductVersion` to `metadata.product_version`.  
\- Mapped `properties.InitiatingProcessAccountUpn` to `principal.user.email_addresses`.  
\- Mapped `properties.AdditionalFields` to `additional.fields`.  
\- Mapped `properties.InitiatingProcessVersionInfoProductName` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessAccountSid` to `principal.user.windows_sid`.  
\- Mapped `properties.AppGuardContainerId` to `security_result.detection_fields`.  
\- Mapped `properties.InitiatingProcessSHA256` to `principal.process.file.sha256`.  
\- Mapped `properties.RemoteUrl` to `target.url`.  
\- Mapped `properties.ActionType` to `security_result.summary`.  
\- Mapped `properties.InitiatingProcessLogonId` to `principal.resource.attribute.labels`.  
\- Mapped `properties.InitiatingProcessFileSize` to `target.process.file.size`.   
2024-11-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
