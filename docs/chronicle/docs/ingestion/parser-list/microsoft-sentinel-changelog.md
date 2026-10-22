---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sentinel-changelog/
title: Change log for MICROSOFT_SENTINEL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:43.192709+00:00
---

# Change log for MICROSOFT_SENTINEL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sentinel-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_SENTINEL

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `object.properties.alerts.properties.additionalData` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when the key is `IP Addresses`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `object.properties.relatedEntities.properties.address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_metadata.event_timestamp`, `incidentUpdates.updatedTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `event_metadata.ingestion_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_metadata.event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_metadata.event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `incidentUpdates.updatedBy.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `incidentUpdates.updatedBy.source` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `object.properties.relatedEntities.properties.friendlyName` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `object.properties.relatedEntities.properties.friendlyName` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `object.properties.relatedEntities.properties.additionalData.MailAddress` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `object.properties.relatedEntities.properties.additionalData.UserType`, `object.properties.relatedEntities.properties.additionalData.JobTitle`, `object.properties.relatedEntities.properties.additionalData.Sources`, `object.properties.relatedEntities.properties.additionalData.GivenName`, `object.properties.relatedEntities.properties.additionalData.Surname`, `object.properties.relatedEntities.properties.additionalData.Country`, `object.properties.relatedEntities.properties.friendlyName`, `object.properties.relatedEntities.properties.additionalData.IsDeleted`, `object.properties.relatedEntities.properties.additionalData.IsEnabled`, `object.properties.relatedEntities.properties.additionalData.UpnName`, `object.properties.relatedEntities.properties.additionalData.SyncFromAad` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `object.properties.relatedEntities.name`, `object.properties.relatedEntities.properties.appId`, `object.properties.relatedEntities.properties.appName`, `object.properties.relatedEntities.properties.instanceName`, `object.properties.relatedEntities.kind`, `object.properties.relatedEntities.id`, `object.properties.relatedEntities.type`, `object.properties.relatedEntities.properties.aadTenantId`, `object.properties.alerts.properties.resourceIdentifiers.workspaceId` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `security_result.rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `security_result.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `security_result.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `security_result.severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `security_result.threat_name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `security_result.attack_details.tactics` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `incidentUpdates.updatedFields`, `metadata.source_system`, `metadata.log_type`, `security_result.detection_fields.AlertDisplayName`, `security_result.detection_fields.AlertStatus`, `security_result.detection_fields.ProductName`, `security_result.detection_fields.ProviderName`, `security_result.detection_fields.DetectionSource` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `object.properties.alerts.properties.status`, `object.properties.alerts.id`, `object.properties.alerts.type`, `object.properties.alerts.kind` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-09 |  Enhancement:  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `AlertLink` from `event.idm.read_only_udm.principal.labels` UDM field since `AlertLink` is directly related to the security alert being reported.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Mapped `AlertLink` raw log field to `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `AlertName` from `event.idm.read_only_udm.security_result.rule_name` UDM field as `AlertName` represents threat name.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `AlertName` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Removed mapping of `AlertType` from `event.idm.read_only_udm.security_result.threat_name` UDM field as `AlertType` represents rule name.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `AlertType` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `DestinationDevice` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents destination device name.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `DestinationDevice` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `SensorId` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents observer device name.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Mapped `SensorId` raw log field to `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `SourceDevice` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents source device name.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `SourceDevice` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_TimeReceived`, `_IsBillable`, `_BilledSize`, `entity.id`, `Nic.IpAddress.id`, `Nic.id`, `entity.Protocols`, `entity.Owners`, `entity.IoTHub.id`, `SystemAlertId`, `TenantId`, `VendorOriginalId`, `_Internal_WorkspaceResourceId`, `_ItemId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `Nic.MacAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `entity.Manufacturer`,`entity.FirmwareVersion`, `entity.Model`, `entity.DeviceName`, `Nic.Type`, `Nic.IpAddress.Type`, `Nic.IpAddress.Address`, `entity.Vendor`, `entity.Type`, `entity.DeviceSubType`, `entity.DevicePageLink`, `entity.IsScanner`, `entity.IsAuthorized`, `entity.IsProgramming`, `entity.PurdueLayer`, `entity.Importance`, `entity.Sensor`, `entity.Zone`, `entity.Site`, `entity.DeviceTypeId`, `entity.DeviceType`, `entity.IoTSecurityAgentId`, `entity.Source`, `entity.DeviceId`, `entity.IoTHub.Type`, `entity.IoTHub.ResourceId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `RemediationSteps`, `isNew`, `AlertManagementUri`, `S7Comm_Control_Function`, `ViolationCount`, `isLearnable` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when both principal machine and target machine data are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when user and resource data are present.   
2025-10-16 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `eventUniqueId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `object.properties.title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `object.properties.labels.labelName` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques: Newly mapped `object.properties.additionalData.techniques` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics: Newly mapped `object.properties.additionalData.tactics` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `object.properties.relatedEntities.properties.mailboxPrimaryAddress` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `object.properties.relatedEntities.properties.recipient` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `object.properties.relatedEntities.properties.p1Sender` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `object.properties.relatedEntities.properties.additionalData.UserPrincipalName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `object.properties.relatedEntities.properties.senderIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `object.properties.relatedEntities.properties.senderIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `object.properties.relatedEntities.properties.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `object.properties.relatedEntities.properties.additionalData.DomainName` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `object.properties.labels.labelType, `object.properties.additionalData.alertsCount, `object.properties.alerts.properties.systemAlertId, `object.properties.alerts.properties.alertDisplayName, `object.properties.alerts.properties.description, `object.properties.alerts.properties.severity, `object.properties.alerts.properties.alertType, `object.properties.alerts.properties.providerAlertId, `object.properties.alerts.properties.confidenceLevel, `object.properties.alerts.properties.endTimeUtc, `object.properties.alerts.properties.processingEndTime, `object.properties.alerts.properties.startTimeUtc, `object.properties.alerts.properties.timeGenerated, `object.properties.alerts.properties.friendlyName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `object.properties.additionalData.tactics, `object.properties.additionalData.alertProductNames, `object.properties.additionalData.bookmarksCount, `object.properties.additionalData.commentsCount, `object.properties.relatedEntities.properties.recipient, `object.properties.relatedEntities.properties.p1Sender, `object.properties.relatedEntities.properties.networkMessageId, `object.properties.relatedEntities.properties.internetMessageId, `object.properties.alerts.properties.alertLink, `object.properties.alerts.properties.vendorName, `object.properties.alerts.properties.productName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `object.properties.relatedEntities.properties.additionalData.UserPrincipalName, `object.properties.relatedEntities.properties.upnSuffix, `object.properties.relatedEntities.properties.isDomainJoined, `object.properties.relatedEntities.properties.additionalData.AccountName, `object.properties.relatedEntities.properties.displayName, `object.properties.relatedEntities.properties.upn` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `object.properties.relatedEntities.properties.accountName, `object.properties.relatedEntities.properties.sid, `object.properties.relatedEntities.properties.aadUserId, `object.properties.relatedEntities.properties.additionalData.DomainName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-08-13 |  Enhancement:  
\- Added support for parsing errors.  
\- event.idm.read_only_udm.principal.hostname: Newly Mapped `entity_Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly Mapped `entity_Hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `entity_SenderIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `Client_IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `Client_IP_Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `entity_SenderIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `entity_Name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly Mapped `entity_DisplayName` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly Mapped `entity_AadUserId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly Mapped `entity_UPNSuffix` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Alert_generation_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `OriginalQuery` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Query` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `SystemAlertId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Data_Sources` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Correlation_Id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `_Internal_WorkspaceResourceId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `_ItemId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Event_Grouping` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Query_End_Time_UTC` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Query_Start_Time_UTC` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Trigger_Threshold` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Trigger_Operator` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Search_Query_Results_Overall_Count` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Query_Period` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly Mapped `Analytic_Rule_Ids` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly Mapped `AlertType` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `Previous_IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `Previous_IP_Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly Mapped `Custom_Details` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.   
2025-02-03 |  Enhancement:  
\- Added support for JSON logs.   
2023-11-03 |  Enhancement:  
\- Mapped `ResourceId` to `target.resource.name`.  
\- When `ResourceId` is `not null` and event has one of `principal` or `target` as `not null`, then map `metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2023-08-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
