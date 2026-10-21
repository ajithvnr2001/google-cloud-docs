---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-changelog/
title: Change log for AZURE_MDM_INTUNE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:20:54.372843+00:00
---

# Change log for AZURE_MDM_INTUNE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_MDM_INTUNE

Date | Changes  
---|---  
2026-08-05 |  Enhancement:  
\- Added support to parse new format of logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.metadata.vendor_name`: Set `event.idm.entity.metadata.vendor_name` as `Microsoft` for logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.metadata.product_name`: Set `event.idm.entity.metadata.product_name` as `AZURE MDM INTUNE` for logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.metadata.entity_type`: Set `event.idm.entity.metadata.entity_type` as `ASSET` for logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.metadata.collected_timestamp`: Newly mapped `time` raw log field with `event.idm.entity.metadata.collected_timestamp` UDM field.  
\- `event.idm.entity.metadata.product_entity_id`: Newly mapped `properties.BatchId` raw log field with `event.idm.entity.metadata.product_entity_id` UDM field.  
\- `event.idm.entity.entity.asset.asset_id`: Newly mapped `properties.DeviceId` raw log field with `event.idm.entity.entity.asset.asset_id` UDM field.  
\- `event.idm.entity.entity.asset.asset_id`: If `properties.DeviceId` is not empty or null, updated the value of `event.idm.entity.entity.asset.asset_id` to Device ID:%{properties.DeviceId}.  
\- `event.idm.entity.entity.asset.hostname`: Newly mapped `properties.DeviceName` raw log field with `event.idm.entity.entity.asset.hostname` UDM field.  
\- `event.idm.entity.entity.asset.hardware.serial_number`: Newly mapped `properties.SerialNumber` raw log field with `event.idm.entity.entity.asset.hardware.serial_number` UDM field.  
\- `event.idm.entity.entity.asset.hardware.model`: Newly mapped `properties.Model` raw log field with `event.idm.entity.entity.asset.hardware.model` UDM field.  
\- `event.idm.entity.entity.asset.hardware.manufacturer`: Newly mapped `properties.Manufacturer` raw log field with `event.idm.entity.entity.asset.hardware.manufacturer` UDM field.  
\- `event.idm.entity.entity.asset.mac`: Newly mapped `properties.WifiMacAddress` raw log field with `event.idm.entity.entity.asset.mac` UDM field.  
\- `event.idm.entity.entity.asset.platform_software.platform`: Newly mapped `properties.OS` raw log field with `event.idm.entity.entity.asset.platform_software.platform` UDM field.  
\- `event.idm.entity.entity.asset.platform_software.platform_version`: Newly mapped `properties.OSVersion` raw log field with `event.idm.entity.entity.asset.platform_software.platform_version` UDM field.  
\- `event.idm.entity.relations.entity.user.email_addresses`: Newly mapped `properties.UserEmail` raw log field with `event.idm.entity.relations.entity.user.email_addresses` UDM field.  
\- `event.idm.entity.relations.entity.user.email_addresses`: Newly mapped `properties.UPN` raw log field with `event.idm.entity.relations.entity.user.email_addresses` UDM field.  
\- `event.idm.entity.relations.entity.user.user_display_name`: Newly mapped `properties.UserName` raw log field with `event.idm.entity.relations.entity.user.user_display_name` UDM field.  
\- `event.idm.entity.relations.entity.user.product_object_id`: Newly mapped `properties.PrimaryUser` raw log field with `event.idm.entity.relations.entity.user.product_object_id` UDM field.  
\- `event.idm.entity.relations.entity.user.phone_numbers`: Newly mapped `properties.PhoneNumber` raw log field with `event.idm.entity.relations.entity.user.phone_numbers` UDM field.  
\- `event.idm.entity.additional.fields`: Newly mapped `properties.CreatedDate`, `properties.ReferenceId`, `properties.EncryptionStatusString`, `properties.SubscriberCarrierNetwork`, `properties.JoinType`, `properties.SupervisedStatusString`, `properties.StorageTotal`, `properties.StorageFree`, `properties.AndroidPatchLevel`, `properties.MEID`, `properties.JailBroken`, `properties.SkuFamily`, `properties.EasID` raw log fields with `event.idm.entity.additional.fields` UDM field.  
\- `event.idm.entity.entity.labels`: Newly mapped `properties.CompliantState`, `properties.Ownership`, `properties.ManagedBy`, `properties.DeviceState`, `properties.IMEI`, `properties.DeviceRegistrationState`, `properties.ManagedDeviceName`, `properties.GraphDeviceIsManaged`, `properties.CategoryName` raw log fields with `event.idm.entity.entity.labels` UDM field.  
\- `event.idm.entity.relations.entity_type`: Set `event.idm.entity.relations.entity_type` as `USER` for logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.relations.relationship`: Set `event.idm.entity.relations.relationship` as `OWNS` for logs with `operationName` or `category` as `Devices`.  
\- `event.idm.entity.metadata.description`: Newly mapped `operationName` raw log field with `event.idm.entity.metadata.description` UDM field.   
2025-12-26 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_type: If `event_type` is `GENERIC_EVENT` and (`has_principal_labels` == `true` || `has_principal` == `true` || `has_target` == `true` || `has_target_resources` == `true`), updated to `USER_RESOURCE_ACCESS`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resources.auditResourceType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-10-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `actor.applicationId` raw log field to `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `actor.auditActorType`, and `actor.type` raw log fields to `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `activityOperationType`, `activityResult`, `componentName`, `correlationId`, `displayName`,`actor.userPermissions`, `resources[*].modifiedProperties` and `id` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-02-13 |  Enhancement:  
\- Mapped `resultType`, `properties.AADDeviceId`, `properties.IntuneDeviceId`, `properties.IntuneUserId`, `properties.MessageId`, `properties.ScaleUnit`, and `properties.Os` to `additional.fields`.  
\- Mapped `properties.EnrollmentType` and `properties.FailureReason` to `additional.fields`.  
\- Mapped `properties.OsVersion`, `principal.platform_version`, and `properties.StartTimeUtc` to `additional.fields`.  
\- Mapped `properties.OperationalLogCategory`, `properties.ScenarioName`, `properties.UserDisplayName`, `properties.UPNSuffix`, `properties.DeviceOperatingSystem`, `AlertDisplayNameproperties.AlertDisplayName, `properties.DeviceDnsDomain`, `properties.DeviceNetBiosName`, and `properties.DeviceHostName` to `security_result.detection_fields".  
\- Mapped `properties.AlertType` to `security_result.description`.  
\- Mapped `Description` to `metadata.description`.   
2024-04-10 |  Enhancement:  
\- Mapped `properties.Actor.Application` to `principal.application`.  
\- Mapped `properties.Actor.UPN` to `principal.user.userid`.  
\- Mapped `operationName` to `metadata.product_event_type`.  
\- Mapped `identity` to `target.user.email_addresses`.  
\- Mapped `identity` and `user_id` to `target.user.userid`.  
\- Mapped `properties.DeviceName` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `properties.UserEmail` to `principal.user.email_addresses`.  
\- Mapped `properties.SerialNumber` to `_hardware.serial_number`.  
\- Mapped `_hardware` to `principal.asset.hardware`.  
\- Mapped `properties.UserName` to `principal.user.user_display_name`.  
\- Mapped `properties.OS` to `principal.platform`.  
\- Mapped `properties.OSVersion` to `principal.platform_version`.  
\- Mapped `properties.DeviceId` to `principal.asset.asset_id` and `principal.asset_id`.  
\- Mapped `properties.BatchId` to `metadata.product_log_id`.  
\- Mapped `tenantId`, `properties.IntuneAccountId`, `properties.AADTenantId`, `properties.LastContact`, `properties.DeviceHealthThreatLevel_loc`, `properties.ComplianceState`, `properties.InGracePeriodUntil`, `properties.RetireAfterDatetime`, `properties.ManagementAgents`, and `properties.ManagementAgents_loc` to `additional.fields`.  
\- Mapped `properties.OS_loc` and `properties.OSDescription` to `security_result.detection_fields`.   
2022-08-17 |  \- Added conditional check when `event_type` is mapped to `USER_RESOURCE_UPDATE_CONTENT`.  
\- Added conditional check for fields `software2`,`software3`,`software4` and Mapped it to `target.asset.software`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
