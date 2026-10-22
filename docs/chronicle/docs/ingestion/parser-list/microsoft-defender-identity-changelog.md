---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-identity-changelog/
title: Change log for MICROSOFT_DEFENDER_IDENTITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:37.240564+00:00
---

# Change log for MICROSOFT_DEFENDER_IDENTITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-identity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_DEFENDER_IDENTITY

Date | Changes  
---|---  
2026-09-23 |  Enhancement:  
\- `event.idm.read_only_udm.observer.cloud.project.id`: Removed mapping of `record.tenantId` from `event.idm.read_only_udm.observer.cloud.project.id` since this UDM field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `record.tenantId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field with key `tenantId`.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `record.properties.ReportId` from `event.idm.read_only_udm.about.labels` since this UDM field is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `record.properties.ReportId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field with key `ReportId`.  
\- Added support for the event `AdvancedHunting-IdentityInfo` and relevant corresponding raw log fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `record.properties.IdentityId`, `record.properties.DistinguishedName`, `record.properties.CloudSid`, `record.properties.SourceProvider`, `record.properties.ChangeSource`, `record.properties.BlastRadius`, `record.properties.DeletedDateTime`, `record.properties.OtherMailAddresses`, `record.properties.RiskLevel`, `record.properties.RiskLevelDetails`, `record.properties.Tags`, `record.properties.UserAccountControl`, `record.properties.SourceProviders`, `record.properties.IdentityEnvironment`, `record.properties.CriticalityLevel`, `record.properties.OnPremObjectId`, `record.properties.RiskScore`, `record.properties.RiskScoreUpdateTime`, `record.properties.PrivilegedEntraPimRoles`, `record.properties.Type`, `record.properties.SipProxyAddress` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.first_name`: Newly mapped `record.properties.GivenName` raw log field to `event.idm.read_only_udm.target.user.first_name` UDM field.  
\- `event.idm.read_only_udm.target.user.last_name`: Newly mapped `record.properties.Surname` raw log field to `event.idm.read_only_udm.target.user.last_name` UDM field.  
\- `event.idm.read_only_udm.target.user.department`: Newly mapped `record.properties.Department` raw log field to `event.idm.read_only_udm.target.user.department` UDM field.  
\- `event.idm.read_only_udm.target.user.title`: Newly mapped `record.properties.JobTitle` raw log field to `event.idm.read_only_udm.target.user.title` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `record.properties.EmailAddress` raw log field to `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.managers.user_display_name`: Newly mapped `record.properties.Manager` raw log field to `event.idm.read_only_udm.target.user.managers.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.personal_address.name`: Newly mapped `record.properties.Address` raw log field to `event.idm.read_only_udm.target.user.personal_address.name` UDM field.  
\- `event.idm.read_only_udm.target.user.personal_address.city`: Newly mapped `record.properties.City` raw log field to `event.idm.read_only_udm.target.user.personal_address.city` UDM field.  
\- `event.idm.read_only_udm.target.user.personal_address.country_or_region`: Newly mapped `record.properties.Country` raw log field to `event.idm.read_only_udm.target.user.personal_address.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.user.phone_numbers`: Newly mapped `record.properties.Phone` raw log field to `event.idm.read_only_udm.target.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.creation_time`: Newly mapped `record.properties.CreatedDateTime` raw log field to `event.idm.read_only_udm.target.user.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `record.properties.OnPremSid` raw log field to `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_authentication_status`: Newly mapped `record.properties.IsAccountEnabled` raw log field to `event.idm.read_only_udm.target.user.user_authentication_status` UDM field.  
\- `event.idm.read_only_udm.target.user.company_name`: Newly mapped `record.properties.CompanyName` raw log field to `event.idm.read_only_udm.target.user.company_name` UDM field.  
\- `event.idm.read_only_udm.target.user.employee_id`: Newly mapped `record.properties.EmployeeId` raw log field to `event.idm.read_only_udm.target.user.employee_id` UDM field.  
\- `event.idm.read_only_udm.target.location.state`: Newly mapped `record.properties.State` raw log field to `event.idm.read_only_udm.target.location.state` UDM field.   
2026-04-15 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.properties.AdditionalFields.IsMfaPerformed` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Modified a grok pattern on `properties_DeviceName` to improve accuracy of IP address extraction for `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- Added a conditional check before already existing mapping of `record.properties.AdditionalFields.ACTOR.DEVICE` to `event.idm.read_only_udm.additional.fields`.   
2025-07-29 |  Enhancement:  
\- Added a conditional mapping based on the `DeviceName` raw log field. A grok pattern is used to identify IP addresses. When an IP is found, it is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`. Otherwise, the existing mapping to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` is used.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `record.properties.OSPlatform` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `record.properties.DeviceType` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `record.properties.TargetDeviceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.src.platform_patch_level: Newly mapped `record.properties.AdditionalFields.SourceComputerOperatingSystemType` raw log field with `event.idm.read_only_udm.src.platform_patch_level` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `record.properties.AdditionalFields.TargetComputerObjectGuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.platform_patch_level: Newly mapped `record.properties.AdditionalFields.TargetComputerOperatingSystem` raw log field with `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- event.idm.read_only_udm.target.platform_patch_level: Newly mapped `record.properties.AdditionalFields.TargetComputerOperatingSystemVersion` raw log field with `event.idm.read_only_udm.target.platform_patch_level` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.properties.AdditionalFields.TargetComputerOperatingSystemType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.properties.UncommonForUser` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.properties.LastSeenForUser` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `properties.AccountUpn` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.   
2025-07-21 |  Enhancement:  
\- Added few Gsubs to ensure proper parsing of JSON format logs.  
\- Added support to generate multiple events based on number of values in `TargetAccountSid` raw log field with duplicate UDM values except `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- If `TargetAccountSid` is single value then it will generate only single UDM event.   
2025-05-21 |  \- event.idm.read_only_udm.security_result.description: Removed mapping of `record.category` from `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Mapped `record.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `record.properties.FailureReason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added a support for new pattern of JSON logs.   
2025-03-03 |  Enhancement:  
\- Added support to parse unparsed logs.   
2025-02-11 |  Enhancement:  
\- Added support to parse unparsed fields.   
2024-10-14 |  Enhancement:  
\- Mapped `device_event_class_id` to `security_result.rule_name`.  
\- Mapped `event_name` to `security_result.description`.  
\- Mapped `app` and `alert_id` to `additional.fields`.  
\- Mapped `externalId` to `metadata.product_log_id`.   
2024-09-12 |  Enhancement:  
\- Added support for array-type logs.   
2024-08-09 |  Enhancement  
\- Added support to parse syslog logs.   
2024-06-25 |  Enhancement  
\- Added support to parse unparsed logs.  
\- If `properties.AdditionalFields.TARGET_OBJECT.USER` is absent, mapped `properties.AccountName` to `target.user.userid`.  
\- If `properties.AccountName` and `properties.AdditionalFields.PRINCIPAL_OBJECT.USER` are absent, mapped `properties.AccountDisplayName` to `principal.user.userid`.  
\- Mapped `properties.Location` to `principal.location.country_or_region`.  
\- Mapped `properties.AccountObjectId` to `principal.user.attribute.labels`.   
2024-04-15 |  Enhancement  
\- Added support to map `DestinationComputerObjectGuid`, `DestinationComputerOperatingSystem`, `DestinationComputerOperatingSystemVersion`, `TO.DEVICE` fields, when the value of these fields is a list instead of a string.   
2022-07-27 |  Enhancement  
-Mapped `metadata.event_type` to `REGISTRY_MODIFICATION` where `properties.ActionType` is not null.  
-Mapped `metadata.event_type` to `REGISTRY_DELETION` where `properties.ActionType` is `RegistryValueDeleted`.  
-Mapped `metadata.event_type` to `REGISTRY_CREATION` where `properties.ActionType` is `RegistryValueCreated`.  
-Mapped `properties.InitiatingProcessFolderPath` to `process.file.full_path`.  
-Mapped `about.labels` to `properties.InitiatingProcessIntegrityLevel`.  
-Mapped `properties.DeviceId` to `principal.asset_id`.  
-Mapped `properties.InitiatingProcessTokenElevation` to `about.labels`.  
-Mapped `properties.InitiatingProcessParentFileName` to `principal.process.parent_process.file.full_path`.  
-Mapped `properties.InitiatingProcessMD5` to `principal.process.file.md5`.  
-Mapped `properties.InitiatingProcessSHA256` to `principal.process.file.sha256`.  
-Mapped `properties.InitiatingProcessSHA1` to `principal.process.file.sha1`.  
-Mapped `properties.InitiatingProcessId` to `principal.process.pid`.  
-Mapped `properties.InitiatingProcessCommandLine` to `principal.process.command_line`.  
-Mapped `properties.InitiatingProcessAccountSid` to `principal.user.windows_sid`.  
-Mapped `properties.InitiatingProcessAccountDomain` to `principal.administrative_domain`.  
-Mapped `properties.RegistryKey` to `target.registry.registry_key`.  
-Mapped `properties.RegistryValueName` to `target.registry.registry_value_name`.  
-Mapped `properties.RegistryValueData` to `target.registry.registry_value_data`.  
-Mapped `properties.PreviousRegistryKey` to `src.registry.registry_key`.  
-Mapped `properties.PreviousRegistryValueName` to `src.registry.registry_value_name`.  
-Mapped `properties.PreviousRegistryValueData` to `src.registry.registry_value_data`.   
2022-04-22 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
