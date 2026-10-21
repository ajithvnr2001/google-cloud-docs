---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-audit-changelog/
title: Change log for AZURE_AD_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:34:10.227509+00:00
---

# Change log for AZURE_AD_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_AD_AUDIT

Date | Changes  
---|---  
2026-10-01 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `initiatedBy.user.ipAddress` and `InitiatedBy.user.ipAddress` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field when the IP address is `RFC 1918 private IP` or `loggedByService` contains `AAD Management UX` value in it.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `initiatedBy.user.ipAddress` and `InitiatedBy.user.ipAddress` raw log fields with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field when the IP address is `RFC 1918 private IP` or `loggedByService` contains `AAD Management UX` value in it.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `USER_LOGIN` to `event.idm.read_only_udm.metadata.event_type` UDM field and `MACHINE` to `event.idm.read_only_udm.extensions.auth.type` UDM field when the log contains target user data, else mapped `USER_RESOURCE_ACCESS` to `event.idm.read_only_udm.metadata.event_type` UDM field when the log contains target resource data and principal user data.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `initiatedBy.user.agentType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-09-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.isReplay`, `properties.initiatedBy.user.agentType`, `properties.resultReason`, `properties.targetResources.administrativeUnits` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `properties.initiatedBy.user.userPrincipalName`, `properties.initiatedBy.app.displayName` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `properties.initiatedBy.user.displayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.initiatedBy.user.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.initiatedBy.user.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `properties.initiatedBy.user.roles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.authenticationAppDeviceDetails.operatingSystem` (key: `authenticationAppDeviceDetails_operatingSystem`), `properties.authenticationAppDeviceDetails.deviceId` (key: `authenticationAppDeviceDetails_deviceId`), `properties.authenticationAppDeviceDetails.clientApp` (key: `authenticationAppDeviceDetails_clientApp`), `properties.authenticationAppDeviceDetails.appVersion` (key: `authenticationAppDeviceDetails_appVersion`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `adminConfiguration` (key: `authAppPolicy_adminConfiguration_%{index}`), `authenticationEvaluation` (key: `authAppPolicy_authenticationEvaluation_%{index}`), `status` (key: `authAppPolicy_status_%{index}`), `policyName` (key: `authAppPolicy_policyName_%{index}`) raw log fields from the `properties.authenticationAppPolicyEvaluationDetails` array with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `expirationRequirement` (key: `sessionLifetimePolicy_expirationRequirement_%{index}`), `detail` (key: `sessionLifetimePolicy_detail_%{index}`) raw log fields from the `properties.sessionLifetimePolicies` array with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `id` (key: `auth_id_%{index}`), `detail` (key: `auth_detail_%{index}`) raw log fields from the `properties.authenticationContextClassReferences` array with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `displayName` (key: `policy_displayName_%{index}`), `conditionsSatisfied` (key: `policy_conditionsSatisfied_%{index}`), `result` (key: `policy_result_%{index}`), `enforcedGrantControls` (key: `enforcedGrantControls_%{index}_%{i}`), `enforcedSessionControls` (key: `enforcedSessionControls_%{index}_%{i}`), `conditionsNotSatisfied` (key: `policy_conditionsNotSatisfied_%{index}`), `id` (key: `policy_id_%{index}`) raw log fields from the `properties.appliedConditionalAccessPolicies` array with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.riskLevelAggregated` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.isThroughGlobalSecureAccess` , `properties.tokenProtectionStatusDetails.signInSessionStatus`, `properties.operationType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.initiatedBy.app.appId` (key: `App Id`) raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Added a grok pattern to parse the new format of SYSLOG+JSON raw logs.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.isThroughGlobalSecureAccess` (key: `isThroughGlobalSecureAccess`), `properties.signInIdentifierType` (key: `signInIdentifierType`), `properties.processingTimeInMilliseconds` (key: `processingTimeInMilliseconds`), `@version` (key: `prop_log_version`), `properties.isInteractive` (key: `properties_isInteractive`), `properties.appDisplayName` (key: `appDisplayName`), `name` (key: `event_name`), `properties.isTenantRestricted` (key: `isTenantRestricted`), `properties.agent.agentType` (key: `agentType`), `properties.agent.agentSubjectType` (key: `agentSubjectType`), `properties.mfaDetail.authMethod` (key: `prop_mfa_auth_method`), `properties.tokenProtectionStatusDetails.signinSessionStatus` (key: `signinSessionStatus`), `properties.tokenProtectionStatusDetails.signInSessionStatusCode` (key: `sign_in_session_status_code`), `properties.mfaDetail.authDetail` (key: `mfaAuthDetail`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.clientAppUsed` (key: `clientAppType`) raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.appId` (key: `appId`) raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `properties.deviceDetail.isManaged` (key: `isManaged`), `properties.deviceDetail.isCompliant` (key: `isCompliant`) raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `authenticationdetails.StatusSequence` (key: `statusSequence`), `authenticationdetails.authenticationMethodDetail` (key: `authenticationMethodDetail`), `authenticationdetails.RequestSequence` (key: `requestSequence`), `networkLocation.networkType` (key: `networkType`), `networkLocation.networkNames` (key: `networkName`), `authenticationRequirementPolicy.requirementProvider` (key: `requirementProvider`), `authenticationRequirementPolicy.detail` (key: `detail`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `properties.resourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `properties.signInIdentifier`, `properties.userPrincipalName`, `properties.alternateSignInName` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.status.additionalDetails` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `properties.location.countryOrRegion` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `properties.location.city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `properties.location.state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Newly mapped `properties.location.geoCoordinates.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Newly mapped `properties.location.geoCoordinates.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `properties.riskDetail` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `logcollector_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-02-20 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `properties.activityDateTime` and time raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `properties.initiatedBy.Id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `properties.sourceIdentity.details.UserPrincipalName` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `properties.sourceIdentity.details.DisplayName` and `properties.sourceIdentity.Name` raw log field(s) with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `properties.servicePrincipal.Name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `properties.sourceSystem.Id` raw log field(s) with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.sourceIdentity.Id` and `properties.sourceIdentity.details.id` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: Newly mapped `properties.sourceIdentity.details.odatatype` and `properties.sourceIdentity.identityType` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `properties.targetIdentity.Id` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `properties.targetIdentity.Name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles.name`: Newly mapped `properties.targetIdentity.identityType` raw log field with `event.idm.read_only_udm.target.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `properties.targetSystem.Id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `properties.provisioningStatusInfo.Status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.provisioningStatusInfo.errorInformation` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `properties.sourceSystem.Name` and `properties.servicePrincipal.Id` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.action` with key `properties_action`, `properties.changeId` with key `changeId`, `properties.cycleId` with key `cycleId`, `properties.jobId` with key `jobId`, `properties.initiatedBy.Name` with key `initiatedBy_Name`, `properties.initiatedBy.Type` with key `initiatedBy_Type`, `properties.provisioningAction` with key `provisioningAction`, and `properties.tenantId` and `tenantId` raw log field(s) with key `TenantId`.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `properties.targetSystem.Name` with key `targetSystem_Name`, `properties.targetSystem.details.ApplicationId` with key `targetSystem_ApplicationId`, `properties.targetSystem.details.ServicePrincipalDisplayName` with key `targetSystem_ServicePrincipalDisplayName`, and `properties.targetSystem.details.ServicePrincipalId` raw log field(s) with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.statusInfo.Status` raw log field with key `Status`, and `resultType` raw log field with key `resultType` with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-29 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `properties.initiatedBy.app.agentType`, `properties.category`, `properties.correlationId`, `targetResources.agentType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `properties.loggedByService` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `properties.result` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `properties.result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `properties.initiatedBy.app.servicePrincipalId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `properties.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `properties.initiatedBy.app.displayName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- Renamed from `properties.targetResources` to `targetResources`.  
\- Renamed from `properties.additionalDetails` to `additionalDetails`.  
\- Added gsub to replace `\`event\`` with `\`eventValue\`` in the raw message.   
2025-12-12 |  Enhancement:  
\- Modified conditional check to parse new format of logs.  
\- event.idm.read_only_udm.security_result.severity: Changed the conditional logic for mapping this field. The previous logic based on the `Level` raw field is now only applied if `event.idm.read_only_udm.security_result.severity_details` is empty.  
\- Modified the timestamp handling to only convert `_time` if a timestamp has not already been successfully extracted.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ActivityDateTime` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field only if `_time` field is empty.   
2025-11-27 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Removed mapping of `Identity` from `event.idm.read_only_udm.principal.application` UDM field, as this application should be associated with the resource principal.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `Identity` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `InitiatedBy.app.displayName` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field, as this is a display name it should be associated with the application principal.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `InitiatedBy.app.displayName` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `InitiatedBy.user.userPrincipalName` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `InitiatedBy.user.displayName` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `InitiatedBy.user.id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `InitiatedBy.user.ipAddress` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `InitiatedBy.user.ipAddress` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-11-20 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `properties.TargetDisplayNames.0` raw log field. with `event.idm.read_only_udm.target.user.user_display_name`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `properties.TargetObjectIds.0` raw log field with `event.idm.read_only_udm.target.resource.product_object_id`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `properties.Actor.ApplicationName` raw log field with `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `properties.Actor.Application` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.Actor.ObjectId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `properties.Actor.UPN` raw log field with `event.idm.read_only_udm.principal.user.email_addresses`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `properties.AuditEventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `resultDescription` raw log field with `event.idm.read_only_udm.metadata.description`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.CorrelationId`,`properties.RelationId`,`properties.Category`,`properties.AdditionalDetails`,`properties.ActivityType`,`properties.ActivityResultStatus`,`properties.ActivityDate`,`identity` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `resultType` raw log field with `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.Actor.PartnerTenantId`,`properties.Actor.Name`,`properties.Actor.IsDelegatedAdmin` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.metadata.event_type`: When `has_target_resource` is `true` then set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2025-11-05 |  Enhancement:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `principal_userid_present` is true.  
\- Added support for JSON format wrapped in `cribl_data.original_message` field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `_time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `AADOperationType` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `AADTenantId` raw log field to `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ActivityDateTime` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Category` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `CorrelationId` raw log field to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `Id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Identity` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `InitiatedBy.app.displayName` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `InitiatedBy.app.servicePrincipalId` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Level` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `OperationName` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `OperationVersion` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `Resource` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `ResourceId` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `TargetResources.id` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `TargetResources.displayName` raw log field to `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped `TargetResources.type` raw log field to `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TargetResources.modifiedProperties.displayName` and `TargetResources.modifiedProperties.newValue` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `ResourceGroup` and `TenantId` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Result` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Result` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `Type` raw log field to `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `TimeGenerated` raw log field to `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `_TimeReceived` raw log field to `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cribl_pipe`, `cribl_data.cribl_enrichment.cribl_source`, `cribl_data.cribl_enrichment.topic_name`, `SourceSystem` and `_Internal_WorkspaceResourceId` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `DurationMs`, `LoggedByService`, `ResultSignature`, `_ItemId` and `AdditionalDetails` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `ActivityDisplayName` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.   
2025-11-03 |  Enhancement:  
\- Added a grok pattern on `client_ip` field to validate if it's a valid IP address before merging it into `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.   
2025-10-08 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record.operationName` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `record.properties.message` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `record.RoleLocation` raw log field to `event.idm.read_only_udm.principal.location.name`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `record.callerIpAddress` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `record.callerIpAddress` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `record.identity.authorization.evidence.principalId` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `record.identity.authorization.evidence.principalType` raw log field to `event.idm.read_only_udm.principal.resource.resource_subtype`.  
\- event.idm.read_only_udm.principal.user.attribute.roles.name: Newly mapped `record.identity.authorization.evidence.role` raw log field to `event.idm.read_only_udm.principal.user.attribute.roles.name`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `record.identity.authorization.scope` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `authorization_scope`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `record.category` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `record.properties.eventCategory` raw log field to `event.idm.read_only_udm.security_result.category_details` (if different from `record.category`).  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `record.resultType` raw log field to `event.idm.read_only_udm.security_result.summary`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `record.resultSignature` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `record.level` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `record.identity.authorization.action` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `record.correlationId` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped the following raw log fields to `event.idm.read_only_udm.additional.fields`: `record.resourceId` (key: `resourceId`), `record.ReleaseVersion` (key: `ReleaseVersion`), `record.Stamp` (key: `Stamp`), `record.tenantId` (key: `tenantId`), `record.identity.claims.appid` (key: `App Id`), `record.identity.claims.aud` (key: `claims_aud`), `record.identity.claims.iss` (key: `claims_iss`), `record.identity.claims.iat` (key: `claims_iat`), `record.identity.claims.nbf` (key: `claims_nbf`), `record.identity.claims.exp` (key: `claims_exp`), `record.identity.claims.appidacr` (key: `claims_appidacr`), `record.identity.claims.idtyp` (key: `claims_idtyp`), `record.identity.claims.nameidentifier` (key: `claims_nameidentifier`), `record.identity.claims.tenantid` (key: `claims_tenantid`), `record.identity.claims.ver` (key: `claims_ver`), `record.identity.claims.aio` (key: `claims_aio`), `record.identity.claims.rh` (key: `claims_rh`), `record.identity.claims.uti` (key: `claims_uti`), `record.identity.claims.xms_ftd` (key: `claims_xms_ftd`), `record.identity.claims.xms_idrel` (key: `claims_xms_idrel`), `record.identity.claims.xms_rd` (key: `claims_xms_rd`), `record.identity.claims.xms_tcdt` (key: `claims_xms_tcdt`), `record.durationMs` (key: `durationMs`), `record.identity.authorization.evidence.roleAssignmentId` (key: `roleAssignmentId`), `record.identity.authorization.evidence.roleDefinitionId` (key: `roleDefinitionId`), `record.identity.authorization.evidence.roleAssignmentScope` (key: `roleAssignmentScope`), `record.properties.eventCategory` (key: `eventCategory` \- if equal to `record.category`), `record.properties.hierarchy` (key: `hierarchy`), `record.properties.statusCode` (key: `properties_statusCode`), `record.properties.serviceRequestId` (key: `properties_serviceRequestId`).  
\- Set `event.idm.read_only_udm.metadata.vendor_name` to `Microsoft`.  
\- Set `event.idm.read_only_udm.metadata.product_name` to `Azure AD Directory Audit`.  
\- Conditionally set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on the presence of user or principal information.  
\- Conditionally set `event.idm.read_only_udm.security_result.action` to `ALLOW` or `BLOCK` based on `record.resultType` containing `success` or `failure`.   
2025-07-03 |  Enhancement:  
\- Added a Grok pattern to support new pattern of JSON logs.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `properties.resourceDisplayName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `resultSignature`, `properties.resourceOwnerTenantId`, `properties.appOwnerTenantId`, `properties.sessionId`, `properties.signInTokenProtectionStatus`, `properties.resourceServicePrincipalId`, `properties.appServicePrincipalId`, `properties.authenticationProtocol`, `properties.incomingTokenType`, `properties.authenticationStrengths`, `properties.uniqueTokenIdentifier`, `properties.authenticationProcessingDetails`, `properties.homeTenantId`, `properties.resourceTenantId`, `properties.clientCredentialType` and `durationMs` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT` and `principal_ip_present` is true.   
2025-04-16 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `identity` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Removed mapping of `user_name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- If principal_ip_present is `true` AND activityDisplayName is `Validate user authentication` and principal_userid_present is `true`, then set event.idm.read_only_udm.metadata.event_type to USER_UNCATEGORIZED.  
\- If principal_ip_present is `true` AND activityDisplayName is `Validate user authentication` `has_target_hostname` is `true`, set event.idm.read_only_udm.metadata.event_type to NETWORK_CONNECTION.  
\- Added a condition `has_target_hostname` is true when `event.idm.read_only_udm.target.hostname` is mapped.   
2025-03-20 |  Enhancement:  
\- Mapped `temp_display_name` to `target.hostname` and `target.asset.hostname`.  
\- When `modifiedProperties.displayName` equals `AppId` then mapped `modifiedProperties.newvalue` to `target.process.pid`.   
2025-02-19 |  Enhancement:  
\- Mapped `initiatedBy.user.displayName` to `about.user.user_display_name`.   
2024-11-28 |  Enhancement:  
\- Mapped `properties.deviceDetail.displayName` to `principal.asset.hardware.model`.  
\- Mapped `properties.authenticationDetails.authenticationMethod`, `properties.authenticationDetails.authenticationStepDateTime`, `properties.authenticationDetails.authenticationStepRequirement`, `properties.authenticationDetails.authenticationStepResultDetail`, and `properties.authenticationDetails.succeeded` to `security_result.detection_fields`.  
\- Mapped `properties.userAgent` to `network.http.user_agent`.  
\- Mapped `properties.deviceDetail.deviceId` to `principal.asset.asset_id` and `principal.asset_id`.  
\- Mapped `properties.deviceDetail.trustType` to `additional.fields`.  
\- Mapped `properties.deviceDetail.browser` to `principal.resource.attribute.labels`.  
\- Mapped `properties.deviceDetail.operatingSystem` to `principal.platform_version`.   
2024-09-04 |  Enhancement:  
\- When `activityDisplayName` is `Add member to group`, then mapped `objectId` to `target.group.product_object_id`.  
\- When `activityDisplayName` is `Add member to group`, then mapped `DisplayName` to `target.group.group_display_name`.   
2024-07-30 |  Enhancement:  
\- When `principal.user.userid` or `target.user.userid` is present, mapped only `metadata.event_type` to `USER_CHANGE_PERMISSIONS`.   
2024-06-26 |  Enhancement:  
\- Mapped delta between `targetResources.modifiedProperties.newValue` and `targetResources.modifiedProperties.oldValue` to `additional.fields`.   
2024-06-10 |  Enhancement:  
\- When `initiatedBy.user.ipAddress` is having an IP, then set `principal_ip_present` to `true`.  
\- Added a condition to set `metadata.event_type` to `USER_DELETION` only when `principal_ip_present` is `true`.   
2024-06-03 |  Enhancement:  
\- Added a JSON block to parse unparsed logs.  
\- Added a conditional check for `event_type` `USER_DELETION`.   
2024-05-20 |  Bug-Fix:  
\- Modified the mapping of the `targetResource`.  
\- Mapped first iteration of the `targetResource` to `target` and the following iteration of `targetResource` to `about`.  
\- Changed key name of `loggedByService` field to `loggedByService` from `log_Service`.  
\- Changed mapping of `resourceId` from `target.resource.id` to `additional_fields`.  
\- When `targetResources.type` = `Application`, `Policy`, `Role`, `Directory`, `RoleAssignment`, `Request`, `Provider`, `Other`, then mapped `targetResources.displayName` to `noun.resource.name`; `targetResources.id` to `noun.resource.product_object_id`; `noun.resource.resource_type` = `UNSPECIFIED` and `targetResource.type` to `noun.resource.resource_subtype`.  
\- When `targetResources.type` = `User`, then mapped `targetResources.displayName` to `noun.resource.name`; `targetResources.id` to `noun.resource.product_object_id`; `noun.resource.resource_type` = `UNSPECIFIED`; `targetResource.type` to `noun.resource.resource_subtype`; `targetResources.displayName` to `noun.user.user_display_name`; `targetResources.id` to `noun.user.product_object_id`; `targetResources.userPrincipalName` to `noun.user.userid`.  
\- When `targetResources.type` = `ServicePrincipal`, then mapped `targetResources.displayName` to `noun.resource.name`, `targetResources.id` to `noun.resource.product_object_id`, `noun.resource.resource_type` = `SERVICE_ACCOUNT`, `targetResource.type` to `noun.resource.resource_subtype`, `targetResources.displayName` to `noun.user.user_display_name`, `targetResources.id` to `noun.user.product_object_id` and `targetResources.userPrincipalName` to `noun.user.userid`.  
\- When `targetResources.type` = `Group`, then mapped `targetResources.displayName` to `noun.resource.name`, `targetResources.id` to `noun.resource.product_object_id`, `noun.resource.resource_type` = `UNSPECIFIED` , `targetResource.type` to `noun.resource.resource_subtype`, `targetResources.displayName` to `noun.group.group_display_name`, `targetResources.id` to `noun.group.product_object_id`, and `groupType` to `noun.group.attribute.labels`.   
2024-05-17 |  Enhancement:  
\- Mapped `initiatedBy.user.id` to `principal.user.product_object_id`.  
\- Mapped `initiatedBy.user.userPrincipalName` to `principal.user.userid`.   
2024-03-18 |  Enhancement:  
\- Displayed `targetResources.modifiedProperties.displayname`, `targetResources.modifiedProperties.newValue` and `targetResources.modifiedProperties.oldValue` fields even when value is null.  
\- Mapped `callerIpAddress` to `principal.ip`.   
2024-03-12 |  Bug-Fix:  
\- Synced mappings of Azure Monitor envelope format log mappings to Microsoft Graph API format logs.  
\- Mapped `target.resource.resource_type` based on `targetResources.type`.  
\- Mapped `targetResources.type` to `target.resource.type`.   
2024-03-04 |  Enhancement:  
\- Mapped `user_principal_name` from `initiatedBy.user.userPrincipalName` to `principal.resource.attribute.labels`.  
\- Mapped `domain` from `initiatedBy.user.userPrincipalName` to `principal.administrative_domain`.  
\- Mapped `loggedByService` and `properties.loggedByService` to `additional.fields`.  
\- Changed mapping of `initiatedBy.user.id` from `principal.user.product_object_id` to `principal.user.userid`.  
\- Mapped `tgt_user_principal_name` from `target.userPrincipalName` to `target.resource.attribute.labels`.  
\- Mapped `domain` from `target.userPrincipalName` to `target.administrative_domain`.  
\- Mapped `category` to `additional.fields`.  
\- When `additionalDetails[n].key` is `AppId`, then mapped `additionalDetails[n].value` to `target.process.pid`.  
\- When `additionalDetails[n].key` is `User-Agent`, then mapped `additionalDetails[n].value` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `metadata.event_type` based on `loggedByService`, `category` and `activityDisplayName`.  
\- Mapped `targetResources.modifiedProperties.displayname`, `targetResources.modifiedProperties.newValue` and `targetResources.modifiedProperties.oldValue` to `additional.fields`.   
2024-02-21 |  Enhancement:  
\- Added conditional check if `principal.user.userid` is present before setting `metadata.event_type` to `USER_CREATION`.  
\- Changed mapping of `initiatedBy.user.id` from `principal.user.userid` to `principal.user.product_object_id`.  
\- Changed mapping of `initiatedBy.app.servicePrincipalId` from `principal.user.userid` to `principal.user.product_object_id`.  
\- Changed mapping of `initiatedBy.app.servicePrincipalName` from `principal.user.user_display_name` to `principal.user.userid`.  
\- Changed mapping of `properties.initiatedBy.user.id` from `principal.user.userid` to `principal.user.product_object_id`.  
\- Changed mapping of `properties.initiatedBy.app.servicePrincipalId` from `principal.user.userid` to `principal.user.product_object_id`.  
\- Changed mapping of `properties.initiatedBy.app.servicePrincipalName` from `principal.user.user_display_name` to `principal.user.userid`.  
\- If `targetResourceType` value is similar to `User` or `ServicePrincipal`, then changed mapping of `target.id` from `target.user.userid` to `target.user.product_object_id`.  
\- If `targetResourceType` value is similar to `User` or `ServicePrincipal`, then mapped `target.userPrincipalName` to `target.user.userid`.  
\- If `targetResourceType` value is similar to `User` or `ServicePrincipal`, then mapped `target.displayName` to `target.user.user_display_name`.   
2024-02-12 |  Enhancement:  
\- Added conditional check for `modifiedProperty.displayName`, `modifiedProperty.newValue`, and `modifiedProperty.oldValue`.  
\- When `targetResource.id` is `User` or `ServicePrincipal`, then mapped it to `target.user.userid`.   
2024-01-08 |  Bug-Fix:  
\- Added a Grok pattern to validate email values before mapping them to `principal.user.email_addresses` and `target.user.email_addresses`.   
2023-12-19 |  Enhancement:  
\- Mapped `targetResource.modifiedProperties.newValue`, `targetResource.modifiedProperties.oldValue`, and `targetResource.modifiedProperties.displayName` to `additional.fields`.   
2023-11-23 |  \- Mapped `targetResources.0.modifiedProperties.newValue/oldValue` fields to `event.idm.read_only_udm.additional.fields`.  
\- Added ip_address format check to `initiatedBy.user.ipAddress` prior mapping to udm.   
2023-10-16 |  Enhancement: Modified the following mappings:  
\- Changed `metadata.event_type` from `USER_UNCATEGORIZED` to `USER_RESOURCE_ACCESS` where `target.type is not `user'.  
\- Changed mapping of `target.id` from `principal.user.userid, to `principal.user.group_or_identifiers` where `target.type` is not `user'.  
\- Mapped the field which has been mapped to `target.resource.id` to `target.resource.product_object_id` as well because `target.resource.id` is deprecated.   
2023-08-03 |  Enhancement: Modified the following mappings:  
\- Changed `metadata.event_type` from `USER_UNCATEGORIZED` to `USER_CREATION` where `activityDisplayName` is `Add user`.  
\- Changed mapping of `activityDisplayName` from `metadata.description, to `metadata.product_event_type'.  
\- Mapped appropriate `metadata.event_type` where `activityDisplayName` is `Add member to group`, `Add owner to group`.  
\- All fields under `targetResources` should be part of the UDM target.user. fields.  
\- `target.user.userid` mapped against the correct `id` under `targetResource`.  
\- For `activityDisplayName` as `Add member to role outside of PIM (permanent)` in activityDisplayName` mapped `target.user.xxx` when resource type is `User'.  
\- For `activityDisplayName` as `Add Member to Role` mapped `Role.WellKnownObjectName` to `target.resource.attribute.roles.name`.   
2023-07-24 |  Enhancement: Mapped `targetResources.modifiedProperties.newValue` to `target.user.title` when `targetResources.modifiedProperties.displayName` value contains `Role.DisplayName`.   
2023-05-25 |  Bug-fix: Changed mapping from `target.resource.attribute.labels.value` to `target.user.userid` when `targetResources.modifiedProperties.displayName` equals `mailNickname`.   
2023-05-05 |  Enhancement: Modified the following mappings-  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.product_object_id` when `targetResources.modifiedProperties.displayName` equals `objectId`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.user_display_name` when `targetResources.modifiedProperties.displayName` equals `displayName`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.first_name` when `targetResources.modifiedProperties.displayName` equals `givenName`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.title` when `targetResources.modifiedProperties.displayName` equals `jobTitle`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.email_addresses` when `targetResources.modifiedProperties.displayName` equals `mail`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.last_name` when `targetResources.modifiedProperties.displayName` equals `surname`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.department` when `targetResources.modifiedProperties.displayName` equals `department`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.office_address.name` when `targetResources.modifiedProperties.displayName` equals `physicalDeliveryOfficeName`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.employee_id` when `targetResources.modifiedProperties.displayName` equals `employeeId`.  
\- Changed mapping from `target.resource.attribute.labels.value` to `target.user.phone_numbers` when `targetResources.modifiedProperties.displayName` equals `mobile`.   
2023-04-18 |  Enhancement:  
\- `initiatedBy.user.userPrincipalName` mapped to `principal.user.user_display_name` or `principal.user.userid` or `principal.user.email_addresses`.  
\- `targetResources.type` mapped to `target.resource.attribute.labels`.   
2023-04-12 |  Enhancement -  
\- Mapped `initiatedBy.user.userPrincipalName` to `principal.user.email_addresses` and `event_type` to `USER_UNCATEGORIZED`.  
when `initiatedBy.user.userPrincipalName` is not null.  
\- If `targetResources.modifiedProperties.displayName` is `userPrincipalName` than mapped it to `principal.user.email_addresses`.  
\- Mapped `event_type` to `USER_UNCATEGORIZED` when `activityDisplayName` is in [`Issue an id_token to the application`, `Set Company Information`].   
2023-02-20 |  Bug-Fix -  
\- Mapped multiple IP addresses coming under key `additionalDetails.ClientIpAddress` to `principal.ip`.  
\- Mapped metadata.event_type as `USER_UNCATEGORIZED` when `activityDisplayName` equals `Delete user` and `initiatedBy.user.userPrincipalName` field is not present.   
2023-02-02 |  Enhancement - Mapped the following when `activityDisplayName` equals `Delete user` :  
\- Mapped `event_type` to `USER_DELETION`.  
\- Mapped `initiatedBy.user.userPrincipalName` to `principal.user.userid`.   
2022-11-24 |  Enhancement -  
\- Mapped `modifiedProperties.newValue` to `target.resource.attribute.labels`.  
\- Mapped `modifiedProperties.oldValue` to `src.resource.attribute.labels`.   
2022-11-07 |  Enhancement -  
\- Mapped `target.modifiedProperties.TargetId.DeviceId` to `event.idm.read_only_udm.target.asset.asset_id`.   
2022-09-16 |  Enhancement -  
\- Mapped `properties.initiatedBy.user.ipAddress` to `principal.ip`.  
\- Mapped `properties.initiatedBy.user.userPrincipalName` to `principal.user.userid`.  
\- Mapped `properties.resultReason` to `security_result.description`.  
\- Mapped `identity` to `target.user.userid`.  
\- Mapped `operationName` to `metadata.product_event_type`.  
\- Mapped `metadata.event_type` to `USER_UNCATEGORIZED` where `properties.activityDisplayName` is `Get resource properties of a tenant`.  
\- Mapped `category` and `properties.category` to `security_result.category_details`.  
\- Mapped `resultDescription` to `metadata.description`.  
\- Mapped `resultType` to `security_result.rule_id`.   
2022-06-20 |  Enhancement - Enhanced the parser to parse the logs with category : `AuditLogs` and `SignInLogs` by adding following mappings :  
\- Mapped the field `properties.id` to `metadata.product_log_id`.  
\- Mapped the field `properties.loggedByService` to `target.application`.  
\- Mapped the field `Level` to `security_result.severity` and `security_result.severity_details`.  
\- Mapped the field `properties.result` to `security_result.summary` and `security_result.action`.  
\- Mapped the field `properties.operationType` to `security_result.action_details`.  
\- Mapped the field `properties.activityDisplayName` to `metadata.description`.  
\- Mapped the field `properties.category` to `metadata.product_event_type`.  
\- Mapped the field `properties.resultReason` to `security_result.description`.  
\- Mapped the field `properties.initiatedBy.app.displayName` to `principal.application`.  
\- Mapped the field `properties.ipAddress` to `principal.ip`.  
\- Mapped the field `properties.initiatedBy.app.servicePrincipalId` to `principal.user.userid`.  
\- Mapped the field `properties.initiatedBy.app.servicePrincipalName` to `principal.user.user_display_name`.  
\- Mapped the field `properties.appId` and `properties.initiatedBy.app.appId` to `principal.resource.attribute.labels`.  
\- Mapped the field `properties.location.city` to `principal.location.city`.  
\- Mapped the field `properties.location.state` to `principal.location.state`.  
\- Mapped the field `properties.location.countryOrRegion` to `principal.location.country_or_region`.  
\- Mapped the field `properties.location.geoCoordinates.latitude` to `principal.location.region_latitude`.  
\- Mapped the field `properties.location.geoCoordinates.longitude` to `principal.location.region_longitude`.  
\- Mapped the fields `properties.targetResources.modifiedProperties` to `target.user.attribute.labels`.  
\- Mapped the field `targetResources.displayName` to `target.user.user_display_name`.  
\- Mapped the field `targetResources.id` to `target.user.userid`.  
\- Mapped the fields `properties.additionalDetails`, `properties.riskDetail`, `properties.riskEventTypes`, `properties.riskEventTypes_v2`, `properties.riskLevelAggregated`, `properties.riskLevelDuringSignIn`, `properties.riskState`, `properties.conditionalAccessStatus`, `tenantId` to `additional.fields`.  
\- Mapped the field `operationVersion` to `metadata.product_version`.  
\- Mapped the field `properties.appliedConditionalAccessPolicies.displayName` to `about.user.user_display_name`.  
\- Mapped the field `properties.appliedConditionalAccessPolicies..id` to `about.user.userid`.  
\- Mapped the field `properties.appliedConditionalAccessPolicies.result` to `about.labels`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
