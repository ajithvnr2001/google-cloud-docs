---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-atp-changelog/
title: Change log for WINDOWS_DEFENDER_ATP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:07.615352+00:00
---

# Change log for WINDOWS_DEFENDER_ATP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-atp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_DEFENDER_ATP

Date | Changes  
---|---  
2024-10-15 |  Enhancement:  
\- Added support to parse `ReportId` field correctly.   
2024-06-20 |  Enhancement:  
\- Added support for log when `security_result.summary` is `FileUploadedToCloud`  
2024-05-28 |  Enhancement:  
\- Mapped `properties.Application` to `principal.application`.  
\- Mapped `properties.AccountDisplayName` to `principal.user.user_display_name`.  
\- Mapped `properties.AccountId` to `principal.user.product_object_id`.  
\- Mapped `properties.AccountType` to `principal.user.attribute.labels`.  
\- Mapped `properties.UserAgent` to `network.http.user_agent`.  
\- Mapped `properties.RawEventData.Id`, `properties.RawEventData.item.id`, `properties.RawEventData.ParentFolder.Id`, `properties.AppInstanceId`, `properties.ActivityType`, `properties.ActivityObjects`, `properties.ApplicationId`, `properties.DeviceType`, `properties.EnforcementMode`, `properties.IsAnonymousProxy`, `properties.IsAdminOperation`, `properties.IsExternalUser`, `properties.IsImpersonated`, `properties.RawEventData.MDATPDeviceId`, `properties.AdditionalFields.IsSatelliteProvider`, `properties.RawEventData.DestinationLocationType`, `properties.RawEventData.CreationTime`, `properties.RawEventData.FileExtension`, `properties.RawEventData.Hidden`, `properties.RawEventData.FileType`, `properties.IPCategory`, `properties.ISP`, `properties.IPTags`, `properties.RawEventData.UserType`, `properties.RawEventData.Version` and `properties.RawEventData.Workload`, `properties.UserAgentTags`, `operationName`, `properties.ObjectType`, `properties.RawEventData.Operation`, `properties.ObjectName`, `properties.RawEventData.Scope`,`properties.RawEventData.ClientProcessName`, `properties.RawEventData.ClientInfoString`, `properties.RawEventData.ClientRequestId`, `properties.RawEventData.ClientVersion`, `properties.RawEventData.ExternalAccess`, `properties.RawEventData.LogonType`, `properties.RawEventData.LogonUserSid`, `properties.RawEventData.MailboxGuid`, and `properties.RawEventData.UserKey` to `additional.fields`.  
\- Mapped `properties.RawEventData.ClientIP` and `properties.IPAddress` to `principal.ip`, and `principal.asset.ip`.  
\- Mapped `properties.RawEventData.DeviceName` to `principal.hostname`, and `principal.asset.hostname`.  
\- Mapped `metadata.event_type` to `FILE_CREATION` when `properties.ActionType` is `FolderBind`.   
2024-04-02 |  \- Mapped `properties.AccountObjectId` to `principal.user.userid`.  
\- Mapped `properties.CountryCode` to `principal.location.country_or_region`.  
\- Mapped `properties.City` to `principal.location.city`.  
\- Mapped `properties.RawEventData.Application` to `principal.application`.  
\- Mapped `properties.RawEventData.TargetFilePath` to `target.file.full_path`.  
\- Mapped `properties.IPAddress` to `principal.ip`.  
\- Mapped `properties.RawEventData.DeviceName` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `properties.AccountDisplayName` to `principal.user.user_display_name`.  
\- Mapped `properties.ApplicationId` to `additional.fields`.  
\- Mapped `properties.RawEventData.FileExtension` to `additional.fields`.  
\- Mapped `properties.RawEventData.MDATPDeviceId` to `additional.fields`.  
\- Mapped `properties.RawEventData.FileType` to `additional.fields`.  
\- Mapped `properties.RawEventData.Sha1` to `target.process.file.sha1`.  
\- Mapped `properties.RawEventData.Sha256` to `target.process.file.sha256`.  
\- Mapped `properties.RawEventData.FileSize` to `target.process.file.size`.  
\- Mapped `metadata.event_type` to `FILE_CREATION` when `properties.ActionType` is `FileCreatedOnNetworkShare`.   
2024-03-05 |  \- Mapped `metadata.entity_type` to `ASSET` for logs having asset information.  
\- Mapped `properties.DeviceId` to `entity.asset.asset_id`.   
2023-12-08 |  Bug-fix:  
\- Fixed the mapping of `properties.InitiatingProcessFolderPath` to `principal.process.file.full_path`.   
2023-11-25 |  Enhancement:  
\- Mapped `AdditionalFields` and `properties.AdditionalFields` to `principal.resource.attribute.labels`.  
\- Mapped `tenantId` to `resource_ancestors.product_object_id`.   
2023-10-12 |  Enhancement -  
\- Spell corrected from `FileUploadedCloud` to `FileUploadedToCloud` while checking `properties.ActionType` value.  
\- Mapped `properties.IPAddress` to `principal.ip`.  
\- Mapped `properties.RawEventData.Sha1` to `principal.process.file.sha1`.  
\- Mapped `properties.RawEventData.Sha256` to `principal.process.file.sha256`.  
\- Mapped `properties.RawEventData.FileSize` to `principal.process.file.size`.  
\- Added validation check to `properties.SenderFromAddress` and `properties.RawEventData.UserId` prior mapping to UDM fields.   
2023-10-09 |  Enhancement:  
\- Mapped `properties.ObjectId` to `additional.fields`.  
\- Mapped `properties.RawEventData.Pid` to `target.process.pid`.  
\- Added condition for `Delete NetworkSecurityGroups` Action type for failing logs.  
\- Added regex to parse `properties.SenderFromAddress` field.   
2023-09-20 |  Enhancement -  
\- Mapped `properties.RegistryValueData` to `target.registry.registry_value_data`.  
\- Mapped `properties.RegistryValueName` to `target.registry.registry_value_name`.  
\- Mapped `properties.PreviousRegistryValueName` to `target.resource.attribute.labels` when `properties.RegistryValueName` is also present.  
\- Mapped `properties.PreviousRegistryValueData` to `target.resource.attribute.labels` when `properties.RegistryValueData` is also present.   
2023-09-04 |  Enhancement -  
\- Mapped `properties.RegistryValueData` to `target.registry.registry_value_data`.  
\- Mapped `properties.RegistryValueName` to `target.registry.registry_value_name`.  
\- Mapped `properties.PreviousRegistryValueName` to `target.resource.attribute.labels` when `properties.RegistryValueName` is also present.  
\- Mapped `properties.PreviousRegistryValueData` to `target.resource.attribute.labels` when `properties.RegistryValueData` is also present.  
\- For `properties.ActionType` in `SearchPreviewed`, `FileUploadedCloud`, mapped following fields:  
\- `properties.ApplicationId` mapped to `additional.fields`.  
\- `properties.AccountDisplayName` mapped to `principal.user.user_display_name`.  
\- `properties.AccountObjectId` mapped to `principal.user.userid`.  
\- `properties.RawEventData.UserId` mapped to `principal.user.email_addresses`.  
\- `properties.RawEventData.ObjectId` mapped to `additional.fields`.  
\- `properties.RawEventData.ExchangeLocations` mapped to `security_result.category_details`.  
\- `properties.RawEventData.TargetDomain` mapped to `target.hostname`.  
\- `properties.RawEventData.Query` mapped to `additional.fields`.  
\- Mapped additional fields for `AdvancedHunting-DeviceProcessEvents`:  
\- `properties.InitiatingProcessSignerType` mapped to `additional.fields`.  
\- `properties.InitiatingProcessSignatureStatus` mapped to `additional.fields`.  
\- `properties.ProcessVersionInfoProductName` mapped to `additional.fields`.  
\- `properties.InitiatingProcessVersionInfoProductName` mapped to `additional.fields`.  
\- `properties.ProcessVersionInfoCompanyName` mapped to `principal.user.company_name`.   
2023-06-06 |  Enhancement -  
\- Mapped `properties.Url` mapped to `target.url`.  
\- Mapped `properties.UrlDomain` mapped to `target.hostname`.  
\- Mapped `properties.UrlLocation` mapped to `additional.fields`.   
2023-03-01 |  Enhancement -  
Mapped `properties.InitiatingProcessVersionInfoCompanyName` to `principal.user.company_name`.  
Mapped `properties.InitiatingProcessVersionInfoProductVersion` to `metadata.product_version`.  
Mapped `properties.InitiatingProcessVersionInfoInternalFileName` to `principal.resource.attribute.labels`.  
Mapped `properties.InitiatingProcessVersionInfoOriginalFileName` to `principal.resource.attribute.labels`.  
Mapped `properties.properties.InitiatingProcessVersionInfoFileDescription` to `principal.resource.attribute.labels`.  
Mapped `properties.AlertId` to `metadata.product_log_id`.  
Added a regular expression condition check for the `properties.InitiatingProcessAccountUpn` field.  
Added an on_error check for the `target.hostname` block.   
2022-12-20 |  Bug-fix -  
\- Added on_error check for `properties.AdditionalFields` to reduce flakiness.  
\- Added condition for `Write NetworkSecurityGroups`, `Edit NetworkSecurityGroups` and `FileModifiedExtended` Action type for failing logs.   
2022-10-20 |  Enhancement -  
Mapped `properties.ReportId` to `target.resource.product_object_id`.  
Mapped `properties.DeviceId` to `principal.asset_id`.   
2022-09-20 |  Enhancement - Merged customer specific parsers to default.   
2022-07-29 |  Enhancement - Parsed the logs with EventID's:- `2006`,`2004`,`2033`,`2005`,`2008`,`0`.  
\- Added support for new previously unparsed JSON format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
