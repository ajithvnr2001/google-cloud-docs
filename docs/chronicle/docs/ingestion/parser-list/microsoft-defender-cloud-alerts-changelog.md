---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-cloud-alerts-changelog/
title: Change log for MICROSOFT_DEFENDER_CLOUD_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:29:33.097315+00:00
---

# Change log for MICROSOFT_DEFENDER_CLOUD_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-cloud-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_DEFENDER_CLOUD_ALERTS

Date | Changes  
---|---  
2026-08-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `record.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `record.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.assessmentEventDataEnrichment.action`, `record.assessmentEventDataEnrichment.apiVersion`, `record.assessmentEventDataEnrichment.isSnapshot`, `record.securityEventDataEnrichment.action`, `record.securityEventDataEnrichment.apiVersion`, `record.securityEventDataEnrichment.isSnapshot`, `record.name` and `Properties.risk.isContextualRisk` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `item.policyInitiativeName`, `item.policyInitiativeId` and `item.assessmentStatus.code` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Properties.risk.level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field when `Properties.risk.level` is an enum value.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `Properties.risk.level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field when `Properties.risk.level` is not an enum value.   
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `record.ExtendedProperties.clientIpAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `record.ExtendedProperties.clientPrincipalName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `record.ExtendedProperties.clientApplication` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `record.ExtendedProperties.Potential causes` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.ExtendedProperties.investigationSteps`, `record.ExtendedProperties.alertId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Entity.FriendlyName`, `Entity.SourceAddress.Type`, `Entity.EntityIds`, `Entity.Metadata.IsGraphCenter`, `record.ExtendedProperties` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` based on required data.  
\- `event.idm.read_only_udm.extensions.auth.type`: Updated `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `tar_port` field with `event.idm.read_only_udm.target.port` UDM field.   
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed `Entities.Name` raw log field from `event.idm.read_only_udm.additional.fields` UDM field when `Entities.Type` is `account`, `file`, `blob-container` and `malware` to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `Entities.Name` raw log field from `event.idm.read_only_udm.target.user.userid` UDM field when `Entities.Type` is `account`.  
\- `event.idm.read_only_udm.target.file.full_path`: Mapped `Entities.Name` raw log field from `event.idm.read_only_udm.target.file.full_path` UDM field when `Entities.Type` is `file`.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `Entities.Name` raw log field from `event.idm.read_only_udm.target.resource.name` UDM field when `Entities.Type` is `blob-container`.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `Entities.Name` raw log field from `event.idm.read_only_udm.security_result.threat_name` UDM field when `Entities.Type` is `malware`.  
\- `event.idm.read_only_udm.additional.fields`: Removed `Entities.FriendlyName` raw log field from `event.idm.read_only_udm.additional.fields` UDM field when it is a valid IP address to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `Entities.FriendlyName` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when it is a valid IP address.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `Entities.FileHashes.FriendlyName` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field when it is a valid SHA1 hash.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `Entities.FileHashes.FriendlyName` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field when it is a valid MD5 hash.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `Entities.FileHashes.FriendlyName` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field when it is a valid SHA256 hash.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `Entities.AzureResourceId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Entities.AzureResourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `Entities.ResourceType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `Entities.ResourceType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly Mapped `event.idm.read_only_udm.target.resource.resource_subtype` UDM field as `VIRTUAL_MACHINE` when `Entities.ResourceType` is `Virtual Machine`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `Entities.ResourceName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Entities.ResourceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.location.country_or_region`: Newly mapped `Entities.SourceAddress.Location.CountryName` raw log field with `event.idm.read_only_udm.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.location.city`: Newly mapped `Entities.SourceAddress.Location.City` raw log field with `event.idm.read_only_udm.location.city` UDM field.  
\- `event.idm.read_only_udm.location.state`: Newly mapped `Entities.SourceAddress.Location.State` raw log field with `event.idm.read_only_udm.location.state` UDM field.  
\- `event.idm.read_only_udm.location.region_coordinates.longitude`: Newly mapped `Entities.SourceAddress.Location.Longitude` raw log field with `event.idm.read_only_udm.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.location.region_coordinates.latitude`: Newly mapped `Entities.SourceAddress.Location.Latitude` raw log field with `event.idm.read_only_udm.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Entities.SourceAddress.Location.Asn` and `Entities.SourceAddress.Location.Carrier` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.network.organization_name`: Newly mapped `Entities.SourceAddress.Location.Organization` raw log field with `event.idm.read_only_udm.principal.network.organization_name` UDM field.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `RecommendationLink` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.last_updated_time`: Newly mapped `Properties.status.statusChangeDate` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.last_update_time`: Newly mapped `StatusChangeDate` raw log field with `event.idm.read_only_udm.target.resource.attribute.last_update_time` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_TimeReceived` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.observer.resource.product_object_id`: Newly mapped `Properties.additionalData.scanId` raw log field with `event.idm.read_only_udm.observer.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.product_object_id`: Newly mapped `Properties.additionalData.parentResource` raw log field with `event.idm.read_only_udm.target.resource_ancestors.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `Properties.additionalData.databasePlatform` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `Properties.metadata_data.techniques.0` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.name` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `Properties.links.azurePortal` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `Properties.displayName` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `Properties.additionalData.ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.observer.resource.name`: Newly mapped `Properties.additionalData.scanner` raw log field with `event.idm.read_only_udm.observer.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Properties.resourceDetails.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Properties.resourceDetails.resourceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Newly mapped `Properties.resourceDetails.resourceProvider` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `FirstEvaluationDate` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `DiscoveredTimeUTC` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RecommendationDisplayName` (key: `Recommendation DisplayName`), `RecommendationId` (key: `Recommendation Id`), `RecommendationName` (key: `Recommendation Name`), `RecommendationSeverity` (key: `Recommendation Severity`), `RecommendationState` (key: `Recommendation State`), `RemediationDescription` (key: `Remediation_Description`), `SourceSystem` (key: `Source System`), `_ItemId` (key: `Item Id`), `Properties.metadata_data.displayName` (key: `Metadata Display Name`), `Properties.metadata_data.assessmentType` (key: `Assessment Type`), `Properties.metadata_data.policyDefinitionId` (key: `Policy Definition Id`), `Properties.metadata_data.description` (key: `Metadata Description`), `Properties.metadata_data.remediationDescription` (key: `Remediation Description`), `Properties.metadata_data.preview` (key: `Preview`), `Properties.metadata_data.severity` (key: `Metadata Severity`), `Properties.metadata_data.userImpact` (key: `User Impact`), `Properties.metadata_data.implementationEffort` (key: `Implementation Effort`), `Properties.metadata_data.publishDates.public` (key: `Public Publish Date`), `Properties.metadata_data.cloudProviders` (key: `Cloud Providers %{index}`), `Properties.metadata_data.managementProvider` (key: `Management Provider`), `Properties.metadata_data.securityIssue` (key: `Security Issue`), `Properties.metadata_data.recommendationCategory` (key: `Recommendation Category`), `_IsBillable` (key: `Is Billable`), `_BilledSize` (key: `Billed Size`), `IsSnapshot` (key: `Is Snapshot`), `ResourceTenantId` (key: `Resource Tenant ID`), `Properties.additionalData.hasBaseline` (key: `Has Baseline`), `Properties.additionalData.query` (key: `Query`), `Properties.additionalData.remediationDescription` (key: `Additional Remediation Description`), `Properties.additionalData.remediationQuery` (key: `Remediation Query`), `Properties.additionalData.impact` (key: `Impact`), `benchmarks.json_array2.item.reference` (key: `Benchmark Reference`), `Properties.status.firstEvaluationDate` (key: `First Evaluation Date`), `Properties.resourceDetails.nativeResourceId` (key: `Native Resource ID`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `benchmarks.json_array2.item.benchmark` raw log fields as a list with `Benchmark` key to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Properties.metadata_data.securityCategories` raw log field (iterated) with `Security Categories` key to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Properties.metadata_data.categories` raw log field (iterated) with `Metadata Categories` key to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Properties.additionalData.scanTime` (key: `scanTime`) raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `Properties.metadata_data.tactics.0` raw log field with `name` set to `Properties.metadata_data.tactics.0`.  
\- `event.idm.read_only_udm.security_result.outcomes`: Newly mapped `Properties.status.code` (key: `Status Code`), `Properties.status.cause` (key: `status_cause`) raw log fields with `event.idm.read_only_udm.security_result.outcomes` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`:  
\- If `Properties.additionalData.severity` is `informational`, Set the value of `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL`.  
\- If `Properties.additionalData.severity` is `low`, Set the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- If `Properties.additionalData.severity` is `medium`, Set the value of `event.idm.read_only_udm.security_result.severity` to `MEDIUM`.  
\- If `Properties.additionalData.severity` is `high`, Set the value of `event.idm.read_only_udm.security_result.severity` to `HIGH`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly merged `Properties.additionalData.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.category`: If `Properties.additionalData.category` is `auth`, Set the value of `event.idm.read_only_udm.security_result.category` to `AUTH_VIOLATION`.  
\- `event.idm.read_only_udm.intermediary.resource.product_object_id`: If `_Internal_WorkspaceResourceId` is not empty, Set the value of `event.idm.read_only_udm.intermediary.resource.product_object_id` to `_Internal_WorkspaceResourceId`.  
\- `event.idm.read_only_udm.target.resource.resource_type`:  
\- If `Properties.resourceDetails.resourceType` is `database`, Set the value of `event.idm.read_only_udm.target.resource.resource_type` to `DATABASE`.  
\- If `Properties.resourceDetails.resourceType` is `device`, Set the value of `event.idm.read_only_udm.target.resource.resource_type` to `DEVICE`.  
\- If `Properties.resourceDetails.resourceType` is `cloud_project`, Set the value of `event.idm.read_only_udm.target.resource.resource_type` to `CLOUD_PROJECT`.  
\- If `Properties.resourceDetails.resourceType` is `virtual_machine`, Set the value of `event.idm.read_only_udm.target.resource.resource_type` to `VIRTUAL_MACHINE`.  
\- Otherwise, Newly mapped `Properties.resourceDetails.resourceType` (key: `Resource Type`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.cloud.environment`:  
\- If `Environment` is `azure`, Set the value of `event.idm.read_only_udm.principal.resource.attribute.cloud.environment` to `MICROSOFT_AZURE`.  
\- If `Environment` is `aws`, Set the value of `event.idm.read_only_udm.principal.resource.attribute.cloud.environment` to `AMAZON_WEB_SERVICES`.  
\- If `Environment` is `gcp`, Set the value of `event.idm.read_only_udm.principal.resource.attribute.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.environment`:  
\- If `Properties.resourceDetails.source` is `azure`, Set the value of `event.idm.read_only_udm.target.resource.attribute.cloud.environment` to `MICROSOFT_AZURE`.  
\- If `Properties.resourceDetails.source` is `aws`, Set the value of `event.idm.read_only_udm.target.resource.attribute.cloud.environment` to `AMAZON_WEB_SERVICES`.  
\- If `Properties.resourceDetails.source` is `gcp`, Set the value of `event.idm.read_only_udm.target.resource.attribute.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `record.TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `record.ExtendedProperties.suspiciousProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `record.ExtendedProperties.suspiciousProcess` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `record.ExtendedProperties.suspiciousCommandLine` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `record.ExtendedProperties.userName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `record.ExtendedProperties.compromisedHost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `record.ExtendedProperties.accountSessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.   
2026-02-20 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `SourceDeviceAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SourceDeviceAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `DestinationDeviceAddress` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `DestinationDeviceAddress` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `SourceDevice` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `SourceDevice` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `DestinationDevice` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `DestinationDevice` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `SourceComputerId` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `CompromisedEntityId` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `SensorId` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `AlertManagementUri` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.VendorOriginalId` (key: `VendorOriginalId`), `ProductComponentName` (key: `ProductComponentName`), `ViolationCount` (key: `ViolationCount`), `isNew` (key: `isNew`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.ProviderName` (key: `ProviderName`), `DeviceId` (key: `ExtendedProperties_DeviceId`), `_ItemId` (key: `_ItemId`), `_TimeReceived` (key: `_TimeReceived`), `_IsBillable` (key: `_IsBillable`), `_BilledSize` (key: `_BilledSize`), `Type` (key: `Type`), `BACnet Service` (key: `bacnet_service`), `Protocol` (key: `Protocol`), `isLearnable` (key: `isLearnable`), `RemediationSteps` (key: `RemediationSteps`), `Techniques` (key: `Techniques`), `Alert generation status` (key: `Alert generation status`), `ProcessedBySentinel` (key: `ProcessedBySentinel`), fields from `record.Entities` array items (key: `Entity: %{key}_%{index}`), `IoTHub.ResourceId` (key: `IoTHub_ResourceId_%{index}`), `IoTHub.Type` (key: `IoTHub_Type_%{index}`), `Owners` array elements (key: `Owners_%{index}_%{owner_index}`), `Nics` array sub-fields (key: `Nics_%{index}_%{nic_index}_IpAddress_%{sub_key}` or `Nics_%{index}_%{nic_index}_%{key}`), and `Protocols` array elements (key: `Protocols_%{index}`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true` and `has_target` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true` and `has_target` is `false`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2025-12-24 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.Intent` raw log field and fields from `Threat Information` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `record.AzureResourceId` raw log field to `event.idm.read_only_udm.target.resource.id`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.RemediationSteps`, `record.Entities`, `record.ResourceIdentifiers` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `record.ExtendedProperties.threatCategory` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- Enhanced mapping for event.idm.read_only_udm.security_result.rule_name to use `record.AlertDisplayName` as a fallback if `record.properties.alertDisplayName` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.principal.resource.attribute.labels` (for `AlertUri`) to use `AlertUri` as a fallback if `record.properties.alertUri` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.principal.resource.attribute.labels` (for `correlationKey`) to use `CorrelationKey` as a fallback if `record.properties.correlationKey` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.additional.fields` (for `StartTime`) to use `StartTimeUtc` as a fallback if `record.properties.startTimeUtc` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.additional.fields` (for `EndTime`) to use `EndTimeUtc` as a fallback if `record.properties.endTimeUtc` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.security_result.severity` to use `record.Severity` as a fallback if `record.properties.severity` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.additional.fields` (for `TenantId`) to use `record.ExtendedProperties.TenantId` as a fallback if `record.TenantId` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.principal.resource.name` to use `record.ExtendedProperties.resourceType` as a fallback if the value from `record.properties.resourceIdentifiers` or `record.properties.extendedProperties.resourceType` is not available.  
\- Enhanced mapping for `event.idm.read_only_udm.principal.resource.attribute.labels` (for `productComponentName`) to use `record.ExtendedProperties.ProductComponentName` as a fallback if the value from `record.properties.extendedProperties.productComponentName` is not available.  
\- Added gsub to replace `Threat Category` with `threatCategory` in the raw message before JSON parsing.   
2025-12-04 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `record.properties.RawEventData.ClientProcessName` raw log field(s) with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `record.properties.RawEventData.ClientRequestId` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `record.properties.RawEventData.LogonUserSid` raw log field(s) with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `record.properties.RawEventData.MailboxOwnerUPN` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `record.properties.ISP` raw log field(s) with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `record.properties.RawEventData.OriginatingServer` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `record.properties.Application` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `record.properties.ReportId` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.properties.IsImpersonated`, `record.properties.IsAdminOperation` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `zone_interface` (extracted from clientIpAddress), `record.properties.extendedProperties.potential causes`, `record.properties.extendedProperties.productComponentName`, `record.properties.extendedProperties.effectiveSubscriptionId`, `record.properties.extendedProperties.sql server name`, `record.properties.extendedProperties.sql instance name`, `record.properties.supportingEvidence`, `record.properties.systemAlertId` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `record.properties.RawEventData.UserId` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.properties.RawEventData.Id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
