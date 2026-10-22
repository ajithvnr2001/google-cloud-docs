---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-activity-changelog/
title: Change log for AZURE_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:58.192543+00:00
---

# Change log for AZURE_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-activity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_ACTIVITY

Date | Changes  
---|---  
2026-10-01 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.resource_type`: Removed hardcoded mapping of `STORAGE_BUCKET` from `event.idm.read_only_udm.target.resource.resource_type` since resource type is now dynamically assigned based on the `operationName`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `eventcategory` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `caller_identity_role` raw log field to `event.idm.read_only_udm.principal.user.attribute.roles`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `hierarchy` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `appid` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels`.  
\- Updated `event_type` mapping logic to assign `NETWORK_CONNECTION` when both principal machine data and target machine data are present.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Updated `resource_type` according to the `operationName` value mapping to `CLUSTER`, `VPC_NETWORK`, `VIRTUAL_MACHINE`, `CLOUD_PROJECT`, `SERVICE`, `ACCESS_POLICY` and `SETTING`.   
2026-09-30 |  Enhancement:  
\- Converted `properties.test.severity` to string before mapping to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: When `properties_severity` is not empty, Set the value of `event.idm.read_only_udm.security_result.severity_details` to `properties_severity`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `LogicalServerName`, `properties.test.DatabaseName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.test.error_number`, `properties.test.query_hash`, `properties.test.query_plan_hash`, `properties.test.state`, `properties.test.user_defined` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-09-23 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `event`, `Tenant`, `properties.test.apiName`, `properties.test.modelDeploymentName`, `properties.test.modelName`, `properties.test.modelVersion`, `properties.test.requestTime` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EnqueueTime`, `properties.test.requestLength`, `properties.test.responseLength`, `properties.test.streamType`, `properties.test.promptTokens`, `properties.test.completionTokens` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.test.callerObjectId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `properties.test.objectId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `callerIpAddress` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event_type` is `GENERIC_EVENT` and principal user data is present, updated `event_type` to `USER_RESOURCE_ACCESS`.   
2026-08-20 |  Enhancement:  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.project.id`: Removed mapping of `rscgrp` raw log field from `event.idm.read_only_udm.target.asset.attribute.cloud.project.id` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.project.product_object_id`: Mapped `rscgrp` raw log field to `event.idm.read_only_udm.target.asset.attribute.cloud.project.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Removed mapping of `STORAGE_BUCKET` value with `event.idm.read_only_udm.target.resource.resource_type` UDM field when `operationName` is `Sign-in activity` as it is a managed service, not file storage.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `SERVICE` value with `event.idm.read_only_udm.target.resource.resource_type` UDM field when `operationName` is `Sign-in activity` to ensure accurate log categorization and avoid false storage alarms.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `AssetIdentity` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `workspaces`, `NodeType`, `isBillable`, `statsWorkspaceCount`, `statsRegionCount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `properties.workspaceRegion` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.   
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.principal.platform`: Mapped `properties.test.deviceDetail.operatingSystem` raw log field with `event.idm.read_only_udm.principal.platform` UDM field when it contains `Ios`.   
2026-08-04 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `correlationId` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as since `correlationId` is unique and mapping it to `event.idm.read_only_udm.metadata.product_log_id` UDM field is more appropriate.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `identity.claims.appid` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents the application originating the event .  
\- `event.idm.read_only_udm.metadata.product_log_id`: Mapped `correlationId` raw log fields to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `identity.claims.appid` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `VmSku` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-21 |  Enhancement:  
\- `event.idm.read_only_udm.target.cloud.environment`: Removed mapping of `event.idm.read_only_udm.target.cloud.environment` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.environment`: Newly mapped `event.idm.read_only_udm.target.resource.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `properties.test.responseCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `properties.test.aadObjectId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `properties.test.aadEmail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `properties.test.requestClientApp` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource_sub_type` field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.test.aadTenantId`, `properties.test.aadClientId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.test.responseDurationMs`, `properties.test.statsCPUTimeMs`, `properties.test.statsDataProcessedEnd`, `properties.test.statsDataProcessedStart`, `properties.test.responseRowCount`, `properties.test.queryThumbprint` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.test.queryText` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field to ALLOW when `properties.test.responseCode` is `200`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `operationName`, principal user data and target resource data are not null, set `event.idm.read_only_udm.metadata.event_type` to RESOURCE_READ.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `event.idm.read_only_udm.target.resource.resource_subtype` UDM field when `operationName` and principal user data is not null.   
2026-06-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `properties.test.deviceDetail.isCompliant`, `properties.test.deviceDetail.isManaged` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.model`: Mapped `properties.test.deviceDetail.displayName` raw log field with `event.idm.read_only_udm.principal.asset.hardware.model` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `properties.test.deviceDetail.browser`, `properties.test.deviceDetail.trustType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Mapped `properties.test.sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.   
2026-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_TimeReceived` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `Claims_d.objectidentifier` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.test.message_data` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.test.resource` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_IsBillable`, `xms_ftd` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `objectidentifier`,`scope`, `tenantid`, `acrs`, `ipaddr` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `appid`, `identityprovider`, `scope`, `objectidentifier`, `tenantid`, `onprem_sid`, `puid`, `sid`, `aio`, `appidacr`, `aud`, `exp`, `iat`, `iss`, `nbf`, `rh`, `uti`, `ver`, `xms_tcdt`, `wids`, `xms_idrel`, `acrs`, `ipaddr`, `xms_act_fct`, `xms_rd`, `xms_sub_fct`, `idtyp` raw log fields with `security_result.detection_fields` UDM field.   
2026-05-14 |  Enhancement:  
\- Modified the grok pattern to parse the new format of logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `identity.claims.xms_act_fct`, `identity.claims.xms_rd` and `identity.claims.xms_sub_fct` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `_time` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.   
2026-03-07 |  Enhancement:  
\- If `operationName` is `MICROSOFT.NETWORK/LOADBALANCERS/WRITE`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_WRITTEN`.  
\- If `operationName` is `MICROSOFT.COMPUTE/VIRTUALMACHINES/EXTENSIONS/WRITE`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_WRITTEN`.  
\- If `operationName` is `MICROSOFT.AUTHORIZATION/POLICIES/AUDIT/ACTION` and `MICROSOFT.AUTHORIZATION/POLICIES/AUDITIFNOTEXISTS/ACTION`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_READ`.  
\- If `operationName` is `MICROSOFT.NETWORK/LOADBALANCERS/WRITE`, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to `LOAD_BALANCER`.  
\- If `operationName` is `MICROSOFT.COMPUTE/VIRTUALMACHINES/EXTENSIONS/WRITE`, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to `VIRTUAL_MACHINE`.  
\- If `operationName` is `MICROSOFT.AUTHORIZATION/POLICIES/AUDIT/ACTION` and `MICROSOFT.AUTHORIZATION/POLICIES/AUDITIFNOTEXISTS/ACTION`, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to `ACCESS_POLICY`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ancestors`, `isComplianceCheck`, `forceUpdateTag`, `publisher`, `typeHandlerVersion`, `settings`, `autoUpgradeMinorVersion`, `enableAutomaticUpgrade` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties_message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-02-18 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Justification` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SKU`, `subscriptionId`, `resourceGroupName`, `tenantId`, `resourceProviderName`, `RoleAssignmentRequestId`, `resource_Type` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.test.CallerInfo.CallerIdentityValue`, `OriginRoleAssignmentId`, `RoleDefinitionOriginId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ActionType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.user.role_name`: Newly mapped `RoleDefinition` raw log field with `event.idm.read_only_udm.target.user.role_name` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `SubjectID` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `SubjectName` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `CRPVmId` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `serviceName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `identity_value` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `identity_type` is UPN.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `identity_value` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field when `identity_type` is ObjectID.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `identity_value` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field when `identity_type` is Name.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `identity_value` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `identity_type` is Username.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_RESOURCE_ACCESS` when `operationName` is `CALL MANAGEMENT API`.   
2026-02-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly Mapped `identity.authorization.evidence.principalId` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `operationName` contains `MICROSOFT.COMPUTE/SNAPSHOTS/WRITE`, updated `event_type` to `RESOURCE_WRITTEN`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `operationName` contains `MICROSOFT.WORKLOADS/SAPVIRTUALINSTANCES/WRITE`, updated `event_type` to `RESOURCE_WRITTEN`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `operationName` contains `MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/DELETE`, updated `event_type` to `RESOURCE_DELETION`.  
\- Added conditional check for `has_user` to map `identity.authorization.evidence.principalId` to either `event.idm.read_only_udm.principal.user.userid` (if `false`) or `event.idm.read_only_udm.principal.resource.product_object_id` (if `true`).  
\- `Added conditional check for `has_user` to the mapping of `identity.authorization.evidence.principalId` to `event.idm.read_only_udm.principal.user.product_object_id`.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `accessPolicy.enforcedSessionControls`, `flaggedForReview`, `properties.test.authenticationContextClassReferences`, `properties.test.appliedConditionalAccessPolicies.displayName`, `properties.test.appliedConditionalAccessPolicies.conditionsNotSatisfied`, `properties.test.appliedConditionalAccessPolicies.conditionsSatisfied`, `properties.test.appliedConditionalAccessPolicies.enforcedGrantControls`, `properties.test.conditionalAccessAudiences`, `properties.test.signInEventTypes`, `properties.test.tokenProtectionStatusDetails.signInSessionStatus`, `properties.test.tokenProtectionStatusDetails.signInSessionStatusCode`, `properties.test.agent.agentSubjectType`, `properties.test.agent.agentType`, `properties.test.isTenantRestricted`, `properties.test.resourceOwnerTenantId`, `properties.test.authenticationProtocol`, `properties.test.isThroughGlobalSecureAccess` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `properties.test.deviceDetail.isCompliant`, `properties.test.deviceDetail.isManaged` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.test.sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.test.appOwnerTenantId`, `properties.test.appliedConditionalAccessPolicies.id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.test.appliedConditionalAccessPolicies.result`, `properties.test.networkLocationDetails.networkNames`, `properties.test.networkLocationDetails.networkType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added conditional check on the `message` field was refined for more accurate parsing of raw log content.   
2026-02-09 |  Enhancement:  
\- event.idm.read_only_udm.network.http.method: Newly mapped `properties.test.requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `properties.test.requestUri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `C_Iat`, `C_Idtyp`, `properties.test.signInActivityId`, `properties.test.servicePrincipalId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `requestId`, `__UDI_RequiredFields_EventTime`, `__UDI_RequiredFields_RegionScope`, `__UDI_RequiredFields_TenantId`, `__UDI_RequiredFields_UniqueId`, `properties.responseSizeBytes`, `properties.responseStatusCode`, `properties.clientAuthMethod`, `properties.wids`, `properties.tokenIssuedAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `properties.test.primaryIPv4Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `properties.test.primaryIPv4Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `properties.test.roles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `properties.test.timeGenerated` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-07-16 |  Enhancement:  
\- Modified grok patterns to extract the first value of SUBSCRIPTIONS.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `SUBSCRIPTIONS` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field and mapped `first_subscription` instead.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped TenantId raw log field to event.idm.read_only_udm.metadata.product_deployment_id.  
\- event.idm.read_only_udm.additional.fields: Newly mapped durationMs raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped SERVICE raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped wids, xms_idrel, statusCode and serviceRequestId raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `xms_ftd` raw log field to event.idm.read_only_udm.additional.fields.  
event.idm.read_only_udm.principal.user.attribute.labels and event.idm.read_only_udm.security_result.detection_fields: Newly mapped `identity.claims.ipaddr` and `identity.claims.acrs` raw log field to event.idm.read_only_udm.principal.user.attribute.labels and event.idm.read_only_udm.security_result.detection_fields.   
2025-06-16 |  Enhancement:  
\- Added gsub to replace `http://schemas.microsoft.com/identity/claims/` with "".  
\- Added Grok pattern to retrieve `resource_value`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`  
\- Updated the mapping of event.idm.read_only_udm.target.resource.attribute.labels to utilize a generalized map for fields `pod`, `compromisedEntity`, `attackedResourceType`, `resourceId`, `resourceTenantId`, `resourceServicePrincipalId`, `appId`, `resource`, `namespace`, `name`, and `apiVersion`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.detection_fields` to utilize a generalized map for fields `currentHealthStatus`, `previousHealthStatus`, `type`, `cause`, `principalType`, `principalId`, `roleAssignmentId`, `roleAssignmentScope`, `roleDefinitionId`, `appid`, `identityprovider`, `scope`, `objectidentifier`, `tenantid`, `onprem_sid`, `puid`, `sid`, `aio`, `appidacr`, `aud`, `exp`, `iat`, `iss`, `nbf`, `rh`, `uti`, `ver`, `xms_tcdt`, `eventDataId`, `roleDefinitionId`, `principalId`, `operationId`, `eventcategory`, `legacyEventDataId`, `legacyChannels`, `legacyResourceGroup`, `subscriptionId`, `resourceGroup`, `resourceProviderValue`, `legacyresourceId`, `legacyResourceType`, `id`, `legacySubscriptionId`, `legacyResourceProviderName`, `correlationId`, and `uniqueTokenIdentifier`.  
\- Updated the mapping of `event.idm.read_only_udm.principal.user.attribute.labels` to utilize a generalized map for fields `objectidentifier`, `scope`, and `tenantid`.  
\- Updated the mapping of `event.idm.read_only_udm.principal.user.product_object_id` to utilize a generalized map for fields `objectidentifier`.  
\- Updated the mapping of `event.idm.read_only_udm.additional.fields` to utilize a generalized map for fields `conditionalAccessStatus`, `stream`, `signInTokenProtectionStatus`, `originalTransferMethod`, `incomingTokenType`, `clientCredentialType`, `processingTimeInMilliseconds`, `riskDetail`, `riskLevelAggregated`, `riskLevelDuringSignIn`, `riskState`, `homeTenantId`, `autonomousSystemNumber`, `crossTenantAccessType`, `privateLinkDetails`, `operationType`, `authenticationRequirement`, `tokenIssuerType`, `hierarchy`, `entity`, `etag`, `objectKey`, `responseMd5`, `serviceType`, `clientRequestId`, `CallerCredentialType`, `EventChannel`, and `EventSource`.  
\- Removed redundant code for `event.idm.read_only_udm.metadata.event_type` and `event.idm.read_only_udm.target.resource.resource_type`.   
2025-06-03 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `DISKS` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field   
2025-05-30 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `identity.claims.http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- Added null check conditions before UDM mappings of `properties.test.tlsVersion`, `principalType`, `role` and `principal_role` fields.   
2025-03-12 |  Enhancement:  
\- Mapped `properties.responseBody.tags`, `properties.responseBody.type`, `_ItemId`, `jobId`, `jobType`, `properties.pod`, `properties.log,objectRef.resource`, `properties.log.objectRef.namespace`, `properties.log.objectRef.name` and `properties.log.objectRef.apiVersion` to `target.resource.attribute.labels`.  
\- Mapped `properties.responseBody.location` to `target.location.country_or_region`.  
\- Mapped "`identity.claims.name` and `properties.log.user.username` to `principal.user.user_display_name`.  
\- Mapped `identity.claims.groups` and `properties.log.user.groups` to `principal.user.group_identifiers`.  
\- Mapped `identity.claims.onprem_sid`, `identity.claims.puid` and `identity.claims.sid` to `security_result.detection_fields`.  
\- Mapped `identity.claims.idtyp` to `principal.user.attribute.labels`.  
\- Mapped `AppRoleInstance`, `AppRoleName`, `AppVersion`, `PerformanceBucket`, `ResultCode` and `TimeGenerated` to `principal.resource.attribute.labels`.  
\- Mapped `ClientOS` to `principal.asset.attribute.labels`.  
\- Mapped `Url` to `principal.url`.  
\- Mapped `_Internal_WorkspaceresourceId`, `Stamp`, `properties.stream`, `serviceBuild`, `properties.log.apiVersion`, `properties.log.kind`, `properties.log.level` `properties.log.stage`, `properties.log.verb`, `properties.log.stageTimestamp` and `properties.log.requestReceivedTimestamp` to `additional.fields`.  
\- Mapped `ReleaseVersion` to `metadata.product_version`.  
\- Mapped `properties.containerID` to `principal.resource.id`.  
\- Mapped `properties.log.sourceIPs` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `properties.log.requestURI` to `target.url`.  
\- Mapped `properties.log.userAgent` to `network.http.user_agent`.  
\- Mapped `properties.log.responseStatus.code` to `network.http.response_code`.   
2025-02-12 |  Enhancement:  
\- Mapped `properties.allowBlobPublicAccess` to `security_result.detection_fields`.   
2024-11-07 |  Enhancement:  
\- Mapped `identity.claims.http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` to `target.user.email_addresses`.  
\- Mapped `identity.claims.http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier` to `target.user.userid`.  
\- Mapped `identity.claims.http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name` to `target.user.user_display_name`.   
2024-09-25 |  Enhancement:  
\- Mapped `DOMAIN_ACCOUNT_TYPE` to `principal.user.account_type` when identity.claims.idtyp` is equal to `user"  
\- Mapped `SERVICE_ACCOUNT_TYPE` to `principal.user.account_type` when identity.claims.idtyp` is equal to `app"  
\- Mapped `identity.claims.http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` to `principal.user.userid`.  
\- Mapped `identity.claims.http://schemas.microsoft.com/identity/claims/objectidentifier` to `principal.user.product_object_id`.   
2024-08-21 |  Enhancement:  
\- Mapped `identity.authorization.evidence.principalId` to `principal.user.userid`.   
2024-08-08 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-07-10 |  Enhancement:  
\- If `identity.authorization.evidence.principalType` is equal to `Group`, then mapped `identity.authorization.evidence.principalId` to `principal.group.product_object_id`.  
\- If `identity.authorization.evidence.principalType` is equal to `User` or `ServicePrincipal`, then mapped `identity.authorization.evidence.principalId` to `principal.user.product_object_id`.  
\- Added gsub to change field `properties` to `properties.test` and removed the field starting with only `properties`.   
2024-07-08 |  Enhancement:  
\- Mapped `properties.compromisedEntity`, `properties.attackedResourceType`, and `properties.intent` to `target.resource.attribute.labels`.  
\- Mapped `properties.severity` to `security_result.severity`.   
2024-06-18 |  Enhancement:  
\- Mapped `operationVersion` to `metadata.product_version`.  
\- Mapped `properties.authenticationRequirementPolicies.requirementProvider` and `properties.authenticationRequirementPolicies.detail` to `security_result.detection_fields`.  
\- Mapped `properties.authenticationDetails.StatusSequence`, `properties.correlationId`, `properties.uniqueTokenIdentifier` and `properties.authenticationDetails.RequestSequence` to `security_result.detection_fields`.  
\- Mapped `properties.appDisplayName` to `target.application`.  
\- Mapped `properties.conditionalAccessStatus`, `properties.appliedConditionalAccessPolicies`, `properties.authenticationContextClassReferences`, `properties.signInTokenProtectionStatus`, `properties.originalRequestId`, `properties.authenticationProcessingDetails`, `properties.clientCredentialType`, `properties.processingTimeInMilliseconds`, `properties.riskDetail`, `properties.riskLevelAggregated`, `properties.riskLevelDuringSignIn`, `properties.riskState` and `properties.originalTransferMethod` to `additional.fields`.  
\- Mapped `properties.riskEventTypes`, `properties.riskEventTypes_v2`, `properties.homeTenantId`, `properties.autonomousSystemNumber`, `properties.autonomousSystemNumber` and `properties.privateLinkDetails` to `additional.fields`.  
\- Mapped `properties.resourceId`, `properties.resourceTenantId` and `properties.resourceServicePrincipalId` to `target.resource.attribute.labels`.  
\- Mapped `properties.userType` to `principal.user.attribute.roles`.  
\- Mapped `properties.userPrincipalName` to `principal.user.email_addresses`.  
\- Mapped `properties.clientAppUsed` to `principal.application`.  
\- Mapped `properties.deviceDetail.deviceId` to `principal.asset.asset_id` and `principal.asset_id`.  
\- Mapped `properties.appId` to `target.resource.attribute.labels`.  
\- Mapped `properties.status.additionalDetails` to `security_result.description`.  
\- Mapped `properties.responseBody.name` to `security_result.rule_name`.  
\- Mapped `properties.responseBody.properties.sourcePortRanges` and `properties.responseBody.properties.destinationPortRanges` to `additional.fields`.  
\- When `properties.responseBody.properties.sourceAddressPrefixes` is a single ip address, then mapped it to `principal.ip`.  
\- When `properties.responseBody.properties.sourceAddressPrefixes` is a range of ip addresses, then mapped it to `additional.fields`.  
\- When `properties.responseBody.properties.sourceAddressPrefix` is a single ip address or ip address with port, then mapped it to `principal.ip` and `principal.port`.  
\- When `properties.responseBody.properties.sourceAddressPrefix` is a range of ip addresses, then mapped it to `additional.fields`.  
\- When `properties.responseBody.properties.destinationAddressPrefixes` is a single ip address, then mapped it to `target.ip`.  
\- When `properties.responseBody.properties.destinationAddressPrefixes` is a range of ip addresses, then mapped it to `additional.fields`.  
\- When `properties.responseBody.properties.destinationAddressPrefix` is a single ip address or ip address with port, then mapped it to `target.ip` and `target.port`.  
\- When `properties.responseBody.properties.destinationAddressPrefix` is a range of ip addresses, then mapped it to `additional.fields`.  
\- When `properties.responseBody.properties.sourcePortRange` is a single port, then mapped it to `principal.port`.  
\- When `properties.responseBody.properties.sourcePortRange` is a range of ports, then mapped it to `additional.fields`.  
\- When `properties.responseBody.properties.destinationPortRange` is a single port, then mapped it to `target.port`.  
\- When `properties.responseBody.properties.destinationPortRange` is a range of ports, then mapped it to `additional.fields`.  
\- Mapped `properties.id` and `properties.status.errorCode` to `security_result.detection_fields`.  
\- Mapped `properties.isInteractive` to `extensions.auth.mechanism`.  
\- When `properties.deviceDetail.operatingSystem` is `ANDROID`, then mapped `principal.platform` to `ANDROID`.   
2024-06-03 |  Enhancement:  
\- Mapped `SUBSCRIPTIONS`, `RESOURCEGROUPS`, `STORAGEACCOUNTS`, `PROVIDERS` and `SNAPSHOTS` from `resourceId` to `target.resource.attribute.labels`.   
2024-05-21 |  Enhancement:  
\- If `identity.authorization.evidence.principalType` is equal to `User`, `Group`, `Application`, then map `principal.resource.type` to `UNSPECIFIED`.  
\- Mapped `identity.authorization.evidence.role` to `principal.user.role_name`.  
\- Mapped `identity.authorization.evidence.principalType` to `principal.resource.resource_subtype`.  
\- Mapped `identity.authorization.evidence.principalId` to `principal.user.product_object_id`.  
\- Mapped `identity.authorization.evidence.roleAssignmentId`, `identity.authorization.evidence.roleAssignmentScope`, `identity.authorization.evidence.roleDefinitionId` to `principal.resource.attribute.labels`.   
2024-05-03 |  Enhancement:  
\- When `category` is `SignInLogs`, then mapped `properties.userDisplayName` to `principal.user.user_display_name`.  
\- Mapped `properties.requestbody.properties.priority` and `properties.response.properties.priority` to `security_result.detection_fields`.  
\- Mapped `properties.requestbody.properties.protocol` to `network.ip_protocol`.  
\- Mapped `properties.requestbody.properties.direction` to `network.direction`.  
\- Mapped `properties.response.properties.protocol` to `network.ip_protocol`.  
\- Mapped `properties.response.properties.direction` to `network.direction`.  
\- Mapped `properties.response.properties.destinationPortRange` to `target.port`.   
2024-04-26 |  Enhancement:  
\- Mapped `operationName.value` to `metadata.product_event_type`.  
\- Mapped `category.value` to `security_result.category_details`.  
\- Mapped `httpRequest.uri` to `network.http.referral_url`.  
\- Mapped `httpRequest.method` to `network.http.method`.  
\- Mapped `httpRequest.clientIpAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `eventDataId` to `security_result.detection_fields`.  
\- Mapped `httpRequest.clientRequestId` to `additional.fields`.   
2024-04-16 |  Enhancement:  
\- Added support to map `network.application_protocol` if `protocol` is known, else mapped `protocol` to `additional.fields`.   
2024-04-12 |  Enhancement:  
\- Mapped `properties.requestbody.properties.allowBlobPublicAccess` to `security_result.detection_fields`.   
2024-04-10 |  Enhancement:  
\- Mapped `resourceId` to `target.resource.name`.  
\- When `resourceId` is present, then mapped `targetResources.displayName`, `identity`, `Type`, and `properties.resourceDisplayName` to `target.resource.attribute.labels`.   
2024-03-29 |  \- Mapped `ResourceGUID` to `target.resource.product_object_id`.  
\- Mapped `Type` to `target.resource.name`.  
\- Mapped `ClientCity` to `principal.location.city`.  
\- Mapped `ClientCountryOrRegion` to `principal.location.country_or_region`.  
\- Mapped `ClientIP` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ClientStateOrProvince` to `principal.location.state`.  
\- Mapped `ClientType` to `principal.resource.attribute.labels`.  
\- Mapped `IKey` to `target.resource.attribute.labels`.  
\- Mapped `_BilledSize` and `DurationMs` to `additional.fields`.  
\- Mapped `OperationId`, `SDKVersion`, and `ItemCount` to `properties.operationId`.  
\- Mapped `ParentId`, `Properties.WebtestLocationId`, `Properties.FullTestResultAvailable`, `Properties.SourceId`, `Properties._MS_altIds`, `Properties.WebtestArmResourceName`, `Properties.SyntheticMonitorId`, and `Success` to `security_result.detection_fields`.  
\- Mapped `Message` to `metadata.description`.  
\- Mapped `Id` to `principal.resource.product_object_id`.  
\- Mapped `Name` to `principal.resource.name`.   
2024-03-25 |  \- When `properties.requestbody.Properties.RoleDefinitionId` is not empty, then set `security_result.detection_fields.key` to `RequestBody roleDefinitionId`.  
\- Mapped `properties.roleDefinitionId`, `properties.principalId`, `properties.responseBody.properties.roleDefinitionId`, and `properties.requestbody.Properties.PrincipalId` to `security_result.detection_fields`.   
2024-03-13 |  Enhancement:  
\- Mapped `properties.requestbody.properties.roleDefinitionId` and `properties.requestbody.properties.principalId` to `security_result.detection_fields`.   
2024-03-05 |  Enhancement:  
\- Mapped `resultType` to `security_result.action_details`.  
\- Mapped `properties.requestbody.Properties.PrincipalId` to `principal.user.userid`.  
\- When `resultType` is not empty, then mapped `properties.status.failureReason` to `security_result.detection_fields`.  
\- Mapped `properties.hardwareProfile.vmSize`, `properties.provisioningState`, `properties.requestbody.Properties.RoleDefinitionId` to `security_result.detection_fields`.   
2024-02-13 |  Bug-Fix:  
\- When `identity.UserName` is email, then map to `principal.user.email_addresses`, otherwise map it to `principal.user.user_display_name`.   
2024-02-12 |  Enhancement:  
\- Added support for JSON logs which are getting dropped.  
\- Mapped `OperationNameValue` to `metadata.product_event_type`.  
\- Mapped `properties.eventDataId`, `properties.subscriptionId`, `properties.resourceGroup`, and `properties.resourceProviderValue` to `security_result.detection_fields`.  
\- Mapped `Caller` to `principal.user.userid`.  
\- Mapped `ActivityStatusValue` to `security_result.action`.   
2024-02-01 |  Bug-Fix:  
\- When `category` field is having `NonInteractiveUserSignInLogs` value or `OperationName` is `Sign-in activity`, then changing `metadata.event_type` from `USER_LOGOUT` to `USER_LOGIN`.  
\- Mapped `properties.incomingTokenType` and `properties.deviceDetail.browser` to `additional.fields`.  
\- Mapped `properties.userAgent` to `network.http.user_agent`.  
\- When `properties.userAgent` value does not exist, then only mapped `properties.deviceDetail.browser` to `network.http.user_agent`.  
\- Mapped parsed `user_agent_field` to `network.http.parsed_user_agent`.  
\- Mapped `properties.eventProperties.clientIPAddress` and `callerIpAddress` to `principal.asset.ip`.  
\- Mapped `hostname`, `rscname` and `properties.eventProperties.compromisedHost` to `principal.asset.hostname`.   
2024-01-07 |  Bug-Fix:  
\- Added a Grok pattern to validate `callerIpAddress` as an IP address.  
\- Mapped `properties.accountName` to `principal.user.userid`.  
\- Mapped `uri` to `network.http.refferal_url`.  
\- Mapped `properties.userAgentHeader` to `network.http.user_agent`.  
\- Mapped `properties.tlsVersion` to `network.tls.version`.  
\- Mapped `statusCode` to `network.http.response_code`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `properties.clientRequestId`, `properties.etag`, `properties.objectKey`, `properties.responseMd5` and `resourceType` to `additional.fields`.   
2023-10-09 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- Renamed the following fields:  
From `OperationName` to `operationName`.  
From `CorrelationId` to `correlationId`.  
From `Category` to `category`.  
From `ResourceId` to `resourceId`.  
From `ResultType` to `resultType`.  
\- Mapped `ProviderName`, `ProviderGuid` to `security_result.detection_fields`.  
\- Mapped `ResultDescription` to `metadata.description`.   
2023-09-13 |  Enhancement -  
\- Mapped `properties.eventCategory` to `security_result.detection_fields`.  
\- Mapped `opproperties.operationIderationName` to `security_result.detection_fields`.  
\- Mapped `properties.eventName` to `security_result.summary`.  
\- Mapped `properties.EventName` to `security_result.summary`.  
\- Mapped `properties.legacyResourceType` to `security_result.detection_fields`.  
\- Mapped `properties.CallerCredentialType` to `security_result.detection_fields`.  
\- Mapped `properties.EventChannel` to `security_result.detection_fields`.  
\- Mapped `properties.EventSource` to `security_result.detection_fields`.  
\- Mapped `properties.legacyResourceId` to `security_result.detection_fields`.  
\- Mapped `properties.eventProperties.User` to `principal.user.id` and "principal.user.email_addresses.  
\- Mapped `properties.Caller` to `principal.user.id` and "principal.user.email_addresses.  
\- Mapped `caller` to `principal.user.id` and "principal.user.email_addresses.  
\- Mapped `properties.IpAddress` to `principal.ip`.  
\- Mapped `properties.Description_scrubbed` to `security_result.description`.   
2023-02-22 |  Enhancement -  
\- Mapped `tenantId` to `metadata.product_deployment_id`.  
\- Mapped `operationName` to `metadata.product_event_type`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `callerIpAddress` to `principal.ip`.  
\- Mapped `identity` to `target.resource.name`.  
\- Mapped `result` to `security_result.action_details`.  
\- Mapped `properties.activityDisplayName` to `security_result.summary`.  
\- Mapped `location` to `principal.location.name`.  
\- Mapped `Level` to `security_result.severity_details`.  
\- Mapped `properties.initiatedBy.app.displayName` to `principal.application`.  
\- Mapped `properties.targetResources.displayName` to `target.resource.name`.  
\- Mapped `properties.targetResources.id` to `target.resource.product_object_id`.  
\- Mapped `properties.targetResources.modifiedProperties.displayName` to `target.user.attribute.labels`.  
\- Mapped `properties.additionalDetails` to `additional.fields`.  
\- Mapped `properties.loggedByService` to `target.application`.  
\- Mapped `properties.userId` to `target.user.product_object_id`.  
\- Mapped `properties.resourceDisplayName` to `target.resource.name`.  
\- Mapped `properties.location.city` to `principal.location.city`.  
\- Mapped `properties.location.state` to `principal.location.state`.  
\- Mapped `properties.location.countryOrRegion` to `principal.location.country_or_region`.  
\- Mapped `properties.ipAddress` to `principal.ip`.  
\- Mapped `properties.location.geoCoordinates.latitude` to `principal.location.region_latitude`.  
\- Mapped `properties.location.geoCoordinates.longitude` to `principal.location.region_longitude`.  
\- Mapped `properties.servicePrincipalId` to `principal.user.userid`.  
\- Mapped `properties.servicePrincipalName` to `principal.user.user_display_name`.  
\- Mapped `properties.tokenIssuerType`, `properties.authenticationProcessingDetails.0.value`, `properties.operationType`, `properties.authenticationRequirement`, `properties.deviceDetail.trustType to `additional.fields".  
\- Mapped `resultDescription` to `metadata.description`.  
\- Mapped `properties.userDisplayName` to `target.user.user_display_name`.  
\- Mapped `properties.appDisplayName` to `target.application`.  
\- Mapped `properties.userType` to `principal.user.attribute.roles`.  
\- Mapped `properties.status.failureReason` to `security_result.action_details`.  
\- Mapped `properties.deviceDetail.operatingSystem` to `principal.platform_version`.  
\- Mapped `properties.deviceDetail.displayName` to `principal.asset.hardware`.  
\- Mapped `properties.deviceDetail.browser` to `network.http.user_agent`.  
\- Mapped `properties.userPrincipalName` to `principal.user.email_addresses`.   
2022-11-28 |  Enhancement -  
\- Mapped the field `correlationId` to `security_result.detection_fields`.  
\- Mapped the field `level` to `security_result.severity_details`.  
\- Added following mapping for the category `ResourceHealth` :  
\- Mapped the field `properties.legacyEventDataId` to `security_result.detection_fields`.  
\- Mapped the field `properties.legacyChannels` to `security_result.detection_fields`.  
\- Mapped the field `properties.legacySubscriptionId` to `security_result.detection_fields`.  
\- Mapped the field `properties.legacyResourceGroup` to `security_result.detection_fields`.  
\- Mapped the field `properties.legacyResourceProviderName` to `security_result.detection_fields`.  
\- Mapped the field `properties.eventProperties.currentHealthStatus` to `security_result.detection_fields`.  
\- Mapped the field `properties.eventProperties.previousHealthStatus` to `security_result.detection_fields`.  
\- Mapped the field `properties.eventProperties.type` to `security_result.detection_fields`.  
\- Mapped the field `properties.eventProperties.cause` to `security_result.detection_fields`.   
2022-09-26 |  Enhancement - Added fields.  
Mapped `tenantId ` to `metadata.product_deployment_id`  
2022-06-20 |  Enhancement -  
\- Added conditional check for `entity_properties`.  
\- when `category` is equal to `Security`  
\- Mapped `properties.eventProperties.clientIPAddress` to `principal.ip`.  
\- Mapped `properties.eventProperties.accountSessionId` to `network.session_id`.  
\- Mapped `properties.eventProperties.suspiciousProcess` to `target.process.file.full_path`.  
\- Mapped `properties.eventProperties.suspiciousCommandLine` to `target.process.command_line`.  
\- Mapped `properties.eventProperties.suspiciousProcessId` to `target.process.pid`.  
\- Mapped `properties.eventProperties.compromisedHost` to `principal.hostname`.  
\- Mapped `resultDescription` to `metadata.description`  
\- Mapped `properties.legacySubscriptionId` to `security_result.detection_fields`.  
\- Mapped `properties.legacyResourceProviderName` to `security_result.detection_fields`.   
2022-05-19 |  Enhancement - Added and modified multiple fields.  
\- claims, Identity, aud, tenantid, principalId, action, appidacr, iat, exp, nbf, rh, uti, ver, xms_tcdt, principalType, roleAssignmentId, appid, aio, iss, nameidentifier, roleDefinitionId, scope mapped to security_result.detection_fields  
\- resultSignature, resultType, hierarchy, resource_type, entity, mapped to additional.fields.  
\- RoleLocation mapped to location.name.  
\- category mapped to security_result.category_details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
