---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-changelog/
title: Change log for AZURE_AD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:20:32.229748+00:00
---

# Change log for AZURE_AD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_AD

Date | Changes  
---|---  
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `userDisplayName` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `userId` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `status.additionalDetails`, `isInteractive` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped `isInteractive` raw log field with `event.idm.read_only_udm.extensions.auth.mechanism` UDM field.   
2026-08-04 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.product_object_id`: Removed mapping of `properties.servicePrincipalId` raw log field from `event.idm.read_only_udm.target.user.product_object_id` UDM field for all categories as there was discrepancy in mapping between Third-party API and Azure Event Hub logs.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Mapped `properties.servicePrincipalId` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field when `category` raw log field is `ServicePrincipalSignInLogs`, `AADServicePrincipalSignInLogs`, `ManagedIdentitySignInLogs`, `AADManagedIdentitySignInLogs` else mapped with `properties.userId` raw log field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `properties.servicePrincipalName` raw log field from `event.idm.read_only_udm.target.user.userid` UDM field for all categories as there was discrepancy in mapping between Third-party API and Azure Event Hub logs.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `properties.servicePrincipalName` raw log field to `event.idm.read_only_udm.target.user.userid` UDM fields when `category` raw log field is in `ServicePrincipalSignInLogs`, `AADServicePrincipalSignInLogs`, `ManagedIdentitySignInLogs`, `AADManagedIdentitySignInLogs`.  
\- `event.idm.read_only_udm.target.user.email_addresses`, `event.idm.read_only_udm.target.user.userid`: Updated mapping of `properties.userPrincipalName` raw log field to `event.idm.read_only_udm.target.user.email_addresses` and `event.idm.read_only_udm.target.user.userid` UDM fields when `category` is not in `ServicePrincipalSignInLogs`, `AADServicePrincipalSignInLogs`, `ManagedIdentitySignInLogs`, `AADManagedIdentitySignInLogs`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.status.additionalDetails` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cribl_pipe` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `_time` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-07-02 |  Enhancement:  
\- Modified parser logic to conditionally map `userDisplayName` and `properties.userPrincipalName` based on whether the log type relates to Sign-in/Sign-out events.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `properties.userPrincipalName` from `event.idm.read_only_udm.principal.user.userid` when it contains an email address. This is because email addresses should be mapped to the `email_addresses` field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Mapped `properties.userPrincipalName` to `event.idm.read_only_udm.target.user.email_addresses` when `properties.userPrincipalName` contains an email address AND the category is a Sign-in/Sign-out log.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `properties.userPrincipalName` to `event.idm.read_only_udm.target.user.userid` when `properties.userPrincipalName` does NOT contain an email address AND the event type is a Sign-in/Sign-out log.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Mapped `properties.userPrincipalName` to `event.idm.read_only_udm.principal.user.email_addresses` when `properties.userPrincipalName` contains an email address AND the event type is NOT a Sign-in/Sign-out log.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `properties.userPrincipalName` to `event.idm.read_only_udm.principal.user.userid` when `properties.userPrincipalName` does NOT contain an email address AND the event type is NOT a Sign-in/Sign-out log.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Modified parser logic to map `userDisplayName` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` when the event type is NOT a Sign-in/Sign-out log.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Mapped `userDisplayName` raw log field to `event.idm.read_only_udm.target.user.user_display_name` when the event type is a Sign-in/Sign-out log.  
\- Changed `event.idm.read_only_udm.metadata.event_type` from `USER_UNCATEGORIZED` to `USER_RESOURCE_ACCESS` for some log types to better reflect the event.   
2026-06-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record_properties.responseSizeBytes` and `properties.responseSizeBytes` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: If `event.idm.read_only_udm.metadata.event_type` is `USER_LOGIN` and `event.idm.read_only_udm.extensions.auth.type` is empty , then set `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.   
2026-06-18 |  Enhancement:  
\- Added a grok pattern on `properties.ipAddress` to extract `properties_ip_address` and `port_num` fields.  
\- Added a grok pattern on `caller_ips` to extract `ip` and `port_num` fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `port_num` field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.mfaDetail.authMethod`, `properties.servicePrincipalId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.authenticationDetails.succeeded` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-16 |  Enhancement:  
\- Added support for `properties.responseSizeBytes` raw log field to ensure negative values are not mapped to the UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.callerIpAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `properties.httpStatusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `properties.__UDI_RequiredFields_UniqueId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `properties.durationMs` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `properties.httpMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.apiVersion` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field .  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `properties.actorType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_labels`: Newly mapped `properties.deviceDetail.isCompliant` and `IsCompliant` raw log fields with `event.idm.read_only_udm.security_result.rule_labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.identityProvider` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.env_cloud_role`, `properties.issuedAt`, `properties.tenantId`, `properties.__UDI_RequiredFields_EventTime`, `properties.directAccessSource` and `properties.isReplay` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.asset_id`: When `properties.deviceDetail.deviceId` raw log field is not null, mapped with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.originalRequestId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.   
2026-05-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_resource` is `true` and any of `has_principal_user`, `has_target_user`, or `has_principal` are `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `targets.id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.initiatedBy.app.agentType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `properties.initiatedBy.app.servicePrincipalId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.   
2026-03-25 |  Enhancement:  
\- Added support for `properties.initiatedBy.user.ipAddress` to handle comma-separated IP values.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `callerIpAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `properties.initiatedBy.user.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `targets.groupType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `targets.agentType`,`properties.initiatedBy.user.agentType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.group.product_object_id`: If `modifiedProperty.displayName` is Group.ObjectID, mapped `modifiedProperty_oldValue` raw log fields with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.group.group_display_name`: If `modifiedProperty.displayName` is Group.DisplayName, mapped `modifiedProperty_oldValue` raw log fields with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- The following fields have been added as a result of providing support:  
`event.idm.read_only_udm.metadata.description`  
`event.idm.read_only_udm.metadata.event_type`  
`event.idm.read_only_udm.metadata.product_deployment_id`  
`event.idm.read_only_udm.metadata.product_event_type`  
`event.idm.read_only_udm.metadata.product_log_id`  
`event.idm.read_only_udm.metadata.product_name`  
`event.idm.read_only_udm.metadata.vendor_name`  
`event.idm.read_only_udm.principal.user.userid`  
`event.idm.read_only_udm.security_result.action`  
`event.idm.read_only_udm.security_result.description`  
`event.idm.read_only_udm.security_result.detection_fields.key`  
`event.idm.read_only_udm.security_result.detection_fields.value`  
`event.idm.read_only_udm.security_result.summary`  
`event.idm.read_only_udm.target.user.product_object_id`  
`event.idm.read_only_udm.additional.fields`  
2026-03-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `StatusSequence`, `RequestSequence`,`properties.conditionalAccessAudiences`,`properties.signInEventTypes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.appOwnerTenantId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.agent.agentType`, `properties.agent.agentSubjectType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_labels`: Newly mapped `properties.deviceDetail.isCompliant` raw log field with `event.idm.read_only_udm.security_result.rule_labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `properties.deviceDetail.isManaged` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.   
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `policies.enforcedSessionControls`, `policies.conditionsSatisfied`, `policies.conditionsNotSatisfied` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `riskEventTypes`,`riskEventTypes_v2`,`properties.riskEventTypes` from `event.idm.read_only_udm.additional.fields` UDM field because this UDM was not the correct field to map these raw log fields to.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `riskEventTypes`,`riskEventTypes_v2`,`properties.riskEventTypes` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.riskEventTypes` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-01 |  Enhancement:  
\- Added conditional check for category and properties.userPrincipalName. When properties.servicePrincipalName and properties.appDisplayName are identical, the logic to populate event.idm.read_only_udm.target.user.userid no longer checks resultType. Instead, it now checks if category is `SignInLogs` or if properties.userPrincipalName has a value.   
2025-11-10 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad.   
2025-10-14 |  Enhancement:  
\- Added conditional check for `operationName` to include `User registered security info`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `properties.initiatedBy.user.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `properties.initiatedBy.user.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `properties.additionalDetails` raw log fields with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `type` raw log field with `event.idm.read_only_udm.target.resource.type UDM field`.  
\- event.idm.read_only_udm.target.application: Newly mapped `properties.loggedByService` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- Added new labels to `event.idm.read_only_udm.additional.fields` based on `properties.resultType`, `properties.operationType`, and `properties.category`.   
2025-08-24 |  Enhancement:  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tokenIssuerType`, `clientCredentialType`, `processingTimeInMilliseconds`, `appOwnerTenantId`, `userType`, `originalTransferMethod` and `resourceOwnerTenantId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resourceTenantId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `homeTenantId` and `servicePrincipalId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `flaggedForReview`, `isTenantRestricted`, `tokenProtectionStatusDetails.signInSessionStatus`, `authenticationContextClassReference.id`, and `authenticationContextClassReference.detail` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `failureReason` from `event.idm.read_only_udm.additional.fields` UDM field.  
`event.idm.read_only_udm.security_result.detection_fields`: Mapped `failureReason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-08-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `uniqueTokenIdentifier` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `incomingTokenType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `autonomousSystemNumber` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `crossTenantAccessType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `signInTokenProtectionStatus` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-08-13 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: Removed mapping of `resultType` from event.idm.read_only_udm.security_result.rule_id UDM field as the policy id is also mapped to `event.idm.read_only_udm.security_result.rule_id` UDM field which is creating confusion between the values.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `resultType` raw log field with event.idm.read_only_udm.additional.fields UDM field.   
2025-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped TargetUserName raw log field to event.idm.read_only_udm.target.user.userid.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped TargetUserSid and TargetSid raw log fields to event.idm.read_only_udm.target.user.windows_sid.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped TargetDomainName raw log field to event.idm.read_only_udm.target.administrative_domain.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped SubjectUserName raw log field to event.idm.read_only_udm.principal.user.userid.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped SubjectUserSid raw log field to event.idm.read_only_udm.principal.user.windows_sid.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped SubjectDomainName raw log field to event.idm.read_only_udm.principal.administrative_domain.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped IpAddress and SourceIpAddress raw log fields to event.idm.read_only_udm.principal.ip.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped IpAddress and SourceIpAddress raw log fields to event.idm.read_only_udm.principal.asset.ip.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped IpPort raw log field to event.idm.read_only_udm.principal.port.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped SubjectLogonId raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped TargetLogonId, LmPackageName, ObjectServer, and HandleId raw log fields to event.idm.read_only_udm.target.resource.attribute.labels.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped LogonProcessName raw log field to event.idm.read_only_udm.target.process.file.names.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped LogonType raw log field to event.idm.read_only_udm.extensions.auth.auth_details.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped WorkstationName raw log field to event.idm.read_only_udm.target.hostname.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped WorkstationName raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped ProcessId raw log field to event.idm.read_only_udm.target.process.pid.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped ProcessName raw log field to event.idm.read_only_udm.target.process.file.full_path.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped CallerProcessId raw log field to event.idm.read_only_udm.principal.process.pid.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped CallerProcessName raw log field to event.idm.read_only_udm.principal.process.file.full_path.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped ObjectType raw log field to event.idm.read_only_udm.target.resource.resource_subtype.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped ObjectName raw log field to event.idm.read_only_udm.target.resource.name.  
\- `event.idm.read_only_udm.target.application`: Newly mapped ServiceName raw log field to event.idm.read_only_udm.target.application.  
\- `event.idm.read_only_udm.target.resource.user.windows_sid`: Newly mapped ServiceSid raw log field to event.idm.read_only_udm.target.resource.user.windows_sid.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped EventRecordID (from properties.RecordId) raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- `event.idm.read_only_udm.security_result.about.resource.name`: Newly mapped AuthenticationPackageName raw log field to event.idm.read_only_udm.security_result.about.resource.name.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped resultDescription raw log field to event.idm.read_only_udm.security_result.description.  
\- `event.idm.read_only_udm.about.artifact.last_https_certificate.serial_number`: Newly mapped CertSerialNumber raw log field to event.idm.read_only_udm.about.artifact.last_https_certificate.serial_number.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped KeyLength, ImpersonationLevel, CertIssuerName, and CertThumbprint raw log fields to event.idm.read_only_udm.additional.fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped LogonGuid, TransmittedServices, OldSd, TicketOptions, Status, TicketEncryptionType and NewSd raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Added logic to set event.idm.read_only_udm.metadata.event_type to USER_CHANGE_PERMISSIONS or USER_LOGOUT based on category and resultDescription fields.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped PreAuthType raw log field to event.idm.read_only_udm.extensions.auth.mechanism.   
2025-08-04 |  Enhancement:  
\- event.idm.read_only_udm.security_result.rule_id: Removed mapping of `errorCode` from event.idm.read_only_udm.security_result.rule_id UDM field as the policy id is already mapped in `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `errorCode` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `properties.status.errorCode` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.   
2025-07-04 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record_time` with `event.idm.read_only_udm.metadata.event_timestamp` UDM field by replacing the value of `record.time` with `record_time`.  
\- event.idm.read_only_udm.target.resource.product_object_id : Newly mapped `record_resourceId` field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field by replacing the value of `record.resourceId` with `record_resourceId`.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `record_identity` field with `event.idm.read_only_udm.target.user.user_display_name` UDM field by replacing the value of `record.identity` with `record_identity`.  
\- security_result.severity_details: Newly mapped `record_Level` field with `security_result.severity_details` UDM field by replacing the value of `record.Level` with `record_Level`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record_operationName` with `event.idm.read_only_udm.metadata.product_event_type` UDM field by replacing the value of `record.operationName` with `record_operationName`.  
\- event.idm.read_only_udm.extensions.auth.type: Set to `AUTHTYPE_UNSPECIFIED` if `record_operationName` equals `Sign-in activity` and `has_target_user` is `true`.  
\- Set `event_type` to `USER_LOGIN` if `record_operationName` equals `Sign-in activity` and `has_target_user` is `true`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `record_operationVersion` with `event.idm.read_only_udm.metadata.product_version` UDM field by replacing the value of `record.operationVersion` with `record_operationVersion`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `record_category` with `event.idm.read_only_udm.metadata.description` UDM field by replacing the value of `record.category` with `record_category`.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `record_tenantId` with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field by replacing the value of `record.tenantId` with `record_tenantId`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record_resultType`, `record_durationMs` ,`record_properties_id` with `event.idm.read_only_udm.additional.fields` UDM field by replacing the value of `record.resultType` with `record_resultType`, `record.durationMs` with `record_durationMs` and `record.properties.id` with `record_properties_id`.  
\- Set `event.idm.read_only_udm.security_result.summary` to `Successful login occurred` and `action` to `ALLOW` if `record_resultType` is `0` and `record_operationName` is `Sign-in activity`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `record_resultSignature` ,`record_properties_appId` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field by replacing the value of `record.resultSignature` with `record_resultSignature` and `record.properties.appId` with `record_properties_appId`.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `record_callerIpAddress`, `record_properties_ipAddress` with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields by replacing the value of `record.callerIpAddress` with `record_callerIpAddress` and `record.properties.ipAddress` with `record_properties_ipAddress`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record_correlationId` with `event.idm.read_only_udm.metadata.product_log_id` UDM field by replacing the value of `record.correlationId` with `record_correlationId`.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `record_properties_userDisplayName` with `event.idm.read_only_udm.target.user.attribute.labels` UDM field by replacing the value of `record.properties.userDisplayName` with `record_properties_userDisplayName`.  
\- event.idm.read_only_udm.target.user.email_address: Newly mapped `record_properties_userPrincipalName` with `event.idm.read_only_udm.target.user.email_address` UDM field by replacing the value of `record.properties.userPrincipalName` with `record_properties_userPrincipalName`.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `record_properties_userId` with `event.idm.read_only_udm.target.user.product_object_id` UDM field by replacing the value of `record.properties.userId` with `record_properties_userId`.  
\- event.idm.read_only_udm.target.application: Newly mapped `record_properties_appDisplayName` with `event.idm.read_only_udm.target.application` UDM field by replacing the value of `record.properties.appDisplayName` with `record_properties_appDisplayName`.  
\- if `record_properties_status_errorCode` is `0`, then set `event.idm.read_only_udm.security_result.summary` to `Successful login occurred` and `event.idm.read_only_udm.security_result.action` to `ALLOW` by replacing the value of `record.properties.status.errorCode` with `record_properties_status_errorCode`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `record_properties_clientAppUsed` with `event.idm.read_only_udm.principal.application` UDM field by replacing the value of `record.properties.clientAppUsed` with `record_properties_clientAppUsed`.  
\- event.idm.read_only_udm.network.http.user_agent,event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `record_properties_userAgent` with `event.idm.read_only_udm.network.http.user_agent`,`event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields by replacing the value of `record.properties.userAgent` with `record_properties_userAgent`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `record_properties_UDI_RequiredFields_TenantId` ,`record_properties_UDI_RequiredFields_UniqueId`,`record_properties_UDI_RequiredFields_EventTime`,`record_properties_operationId`,`record_properties_requestId`,`record_properties_resourceDisplayName`,`record_properties_resourceId`,`record_properties_resourceTenantId`,`record_properties_homeTenantId`,`record_properties_tenantId`,`record_properties_resourceOwnerTenantId`,`record_properties_resourceServicePrincipalId` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field by replacing the value of `record.properties.__UDI_RequiredFields_TenantId` with `record_properties_UDI_RequiredFields_TenantId`, `record.properties.__UDI_RequiredFields_UniqueId` with `record_properties_UDI_RequiredFields_UniqueId`, `record.properties.__UDI_RequiredFields_EventTime` with `record_properties_UDI_RequiredFields_EventTime`, `record.properties.operationId` with `record_properties_operationId`, `record.properties.requestId` with `record_properties_requestId`, `record.properties.resourceDisplayName` with `record_properties_resourceDisplayName`, `record.properties.resourceId` with `record_properties_resourceId`, `record.properties.resourceTenantId` with `record_properties_resourceTenantId`, `record.properties.homeTenantId` with `record_properties_homeTenantId`, `record.properties.tenantId` with `record_properties_tenantId`, `record.properties.resourceOwnerTenantId` with `record_properties_resourceOwnerTenantId`, `record.properties.resourceServicePrincipalId` with `record_properties_resourceServicePrincipalId`.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `record_properties_UDI_RequiredFields_RegionScope` with `event.idm.read_only_udm.target.location.country_or_region` UDM field by replacing the value of `record.properties.__UDI_RequiredFields_RegionScope` with `record_properties_UDI_RequiredFields_RegionScope`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `record_properties_clientRequestId` with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field by replacing the value of `record.properties.clientRequestId` with `record_properties_clientRequestId`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record_properties_apiVersion`, `record_properties_agent_agentType` with `event.idm.read_only_udm.security_result.detection_fields` UDM field by replacing the value of `record.properties.apiVersion` with `record_properties_apiVersion` and `record.properties.agent.agentType` with `record_properties_agent_agentType`.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `record_properties_requestMethod` with `event.idm.read_only_udm.network.http.method` UDM field by replacing the value of `record.properties.requestMethod` with `record_properties_requestMethod`.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `record_properties_responseStatusCode` with `event.idm.read_only_udm.network.http.response_code` UDM field by replacing the value of `record.properties.responseStatusCode` with `record_properties_responseStatusCode`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `record_properties_responseSizeBytes` with `event.idm.read_only_udm.network.received_bytes` UDM field by replacing the value of `record.properties.responseSizeBytes` with `record_properties_responseSizeBytes`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record_properties_signInActivityId`, `record_properties_clientAuthMethod`, `record_properties_wids`, `record_properties_C_Idtyp`, `record_properties_C_Iat`, `record_properties_atContentP`, `record_properties_atContentH`, `record_properties_C_Sid`, `record_properties_C_DeviceId`, `record_properties_servicePrincipalId`,`record_properties_tokenIssuedAt`,`record_properties_conditionalAccessStatus`,`record_properties_originalRequestId`,`record_properties_tokenIssuerType`,`record_properties_riskDetail` ,`record_properties_clientCredentialType`,`record_properties_riskLevelAggregated`,`record_properties_riskLevelDuringSignIn`,`record_properties_riskState`,`record_properties_authenticationRequirement`,`record_properties_userType`,`record_properties_uniqueTokenIdentifier` with `event.idm.read_only_udm.additional.fields` UDM field by replacing the value of `record.properties.signInActivityId` with `record_properties_signInActivityId`, `record.properties.clientAuthMethod` with `record_properties_clientAuthMethod`, `record.properties.wids` with `record_properties_wids`, `record.properties.C_Idtyp` with `record_properties_C_Idtyp`, `record.properties.C_Iat` with `record_properties_C_Iat`, `record.properties.atContentP` with `record_properties_atContentP`, `record.properties.atContentH` with `record_properties_atContentH`, `record.properties.C_Sid` with `record_properties_C_Sid`, `record.properties.C_DeviceId` with `record_properties_C_DeviceId`, `record.properties.servicePrincipalId` with `record_properties_servicePrincipalId`, `record.properties.tokenIssuedAt` with `record_properties_tokenIssuedAt`, `record.properties.conditionalAccessStatus` with `record_properties_conditionalAccessStatus`, `record.properties.originalRequestId` with `record_properties_originalRequestId`, `record.properties.tokenIssuerType` with `record_properties_tokenIssuerType`, `record.properties.riskDetail` with `record_properties_riskDetail`, `record.properties.clientCredentialType` with `record_properties_clientCredentialType`, `record.properties.riskLevelAggregated` with `record_properties_riskLevelAggregated`, `record.properties.riskLevelDuringSignIn` with `record_properties_riskLevelDuringSignIn`, `record.properties.riskState` with `record_properties_riskState`, `record.properties.authenticationRequirement` with `record_properties_authenticationRequirement`, `record.properties.userType` with `record_properties_userType`, `record.properties.uniqueTokenIdentifier` with `record_properties_uniqueTokenIdentifier`.  
\- event.idm.read_only_udm.target.user.role_name: Newly mapped `record_properties_roles` with `event.idm.read_only_udm.target.user.role_name` UDM field by replacing the value of `record.properties.roles` with `record_properties_roles`.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `record_properties_UserPrincipalObjectID` with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field by replacing the value of `record.properties.UserPrincipalObjectID` with `record_properties_UserPrincipalObjectID`.  
\- event.idm.read_only_udm.target.url: Newly mapped `record_properties_identityProvider` with `event.idm.read_only_udm.target.url` UDM field by replacing the value of `record.properties.identityProvider` with `record_properties_identityProvider`.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `record_properties_requestUri` with `event.idm.read_only_udm.network.http.referral_url` UDM field by replacing the value of `record.properties.requestUri` with `record_properties_requestUri`.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `record_properties_deviceDetail_operatingSystem` with `event.idm.read_only_udm.principal.platform_version` UDM field by replacing the value of `record.properties.deviceDetail.operatingSystem` with `record_properties_deviceDetail_operatingSystem`.  
\- event.idm.read_only_udm.principal.platform: Set to `WINDOWS`, `MAC`, or `LINUX` based on value in `record_properties_deviceDetail_operatingSystem`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `record_properties_deviceDetail_displayName` with `event.idm.read_only_udm.principal.user.user_display_name` UDM field by replacing the value of `record.properties.deviceDetail.displayName` with `record_properties_deviceDetail_displayName`.  
\- event.idm.read_only_udm.principal.asset.asset_id,event.idm.read_only_udm.principal.asset_id: Newly mapped `record_properties_deviceDetail_deviceId` with `event.idm.read_only_udm.principal.asset.asset_id` ,`event.idm.read_only_udm.principal.asset_id` UDM field by replacing the value of `record.properties.deviceDetail.deviceId` with `record_properties_deviceDetail_deviceId`.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `record_properties_location_countryOrRegion` with `event.idm.read_only_udm.principal.location.country_or_region` UDM field by replacing the value of `record.properties.location.countryOrRegion` with `record_properties_location_countryOrRegion`.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `record_properties_location_city` with `event.idm.read_only_udm.principal.location.city` UDM field by replacing the value of `record.properties.location.city` with `record_properties_location_city`.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `record_properties_location_state` with `event.idm.read_only_udm.principal.location.state` UDM field by replacing the value of `record.properties.location.state` with `record_properties_location_state`.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `record_properties_location_geoCoordinates_latitude` with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field by replacing the value of `record.properties.location.geoCoordinates.latitude` with `record_properties_location_geoCoordinates_latitude`.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `record_properties_location_geoCoordinates_longitude` with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field by replacing the value of `record.properties.location.geoCoordinates.longitude` with `record_properties_location_geoCoordinates_longitude`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly Mapped `record.properties.authenticationProcessingDetails` to `event.idm.read_only_udm.security_result.detection_fields` UDM field by replacing the value of `record.properties.authenticationProcessingDetails` with `record_properties_authenticationProcessingDetails`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `record_properties_sessionId` with `event.idm.read_only_udm.network.session_id` UDM field by replacing the value of `record.properties.sessionId` with `record_properties_sessionId`.  
\- Merged `security_result` with `event.idm.read_only_udm.security_result`.  
\- Rename `event.idm.read_only_udm.additional` to `additional`.  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if `has_principal` is `true` else map it to `GENERIC_EVENT`.  
\- Replaced the value of`record.AADTenantId` in `record_AADTenantId` and added a conditional check before already existing mapping for `record_AADTenantId` to `event.idm.read_only_udm.additional.fields`.  
\- Replaced the value of `record.AlternateSignInName` in `record_AlternateSignInName` and added a conditional check before already existing mapping for `record_AlternateSignInName` to `event.idm.read_only_udm.target.user.userid`.  
\- Replaced the value of `record.AppDisplayName` in `record_AppDisplayName` and added a conditional check before already existing mapping for `record_AppDisplayName` to `event.idm.read_only_udm.target.application`.  
\- Replaced the value of `record.AppId` in `record_AppId` and added a conditional check before already existing mapping for `record_AppId` to `event.idm.read_only_udm.target.asset.asset_id`.  
\- Replaced the value of `record.AuthenticationProcessingDetails` in `record_AuthenticationProcessingDetails` and added a conditional check before already existing mapping for `record_AuthenticationProcessingDetails` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Replaced the value of `record.AuthenticationDetails` in `record_AuthenticationDetails` and added a conditional check before already existing mapping for `record_AuthenticationDetails` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Replaced the value of `record.AuthenticationProtocol` in `record_AuthenticationProtocol` and added a conditional check before already existing mapping for `record_AuthenticationProtocol` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Replaced the value of `record.AuthenticationRequirement` in `record_AuthenticationRequirement` and added a conditional check before already existing mapping for `record_AuthenticationRequirement` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Replaced the value of `record.AutonomousSystemNumber` in `record_AutonomousSystemNumber` and added a conditional check before already existing mapping for `record_AutonomousSystemNumber` to `event.idm.read_only_udm.additional.fields`.  
\- Replaced the value of `record.AuthenticationProtocol` in `record_AuthenticationProtocol` and added a conditional check before already existing mapping for `record_AuthenticationProtocol` to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Replaced the value of `record.Category` in `record_Category` and added a conditional check before already existing mapping for `record_Category` to `event.idm.read_only_udm.security_result.category_details`.  
\- Replaced the value of `record.ClientAppUsed` in `record_ClientAppUsed` and added a conditional check before already existing mapping for `record_ClientAppUsed` to `event.idm.read_only_udm.principal.application`.  
\- Replaced the value of `record.ConditionalAccessStatus` in `record_ConditionalAccessStatus` and added a conditional check before already existing mapping for `record_ConditionalAccessStatus` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.CorrelationId` in `record_CorrelationId` and added a conditional check before already existing mapping for `record_CorrelationId` to `event.idm.read_only_udm.metadata.product_log_id`.  
\- Replaced the value of `record.HomeTenantId` in `record_HomeTenantId` and added a conditional check before already existing mapping for `record_HomeTenantId` to `event.idm.read_only_udm.additional.fields`.  
\- Replaced the value of `record.Id` in `record_Id` and added a conditional check before already existing mapping for `record_Id` to `event.idm.read_only_udm.metadata.product_log_id`.  
\- Replaced the value of `record.CreatedDateTime` in `record_CreatedDateTime` and added a conditional check before already existing mapping for `record_CreatedDateTime` to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- Replaced the value of `record.Identity` in `record_Identity` and added a conditional check before already existing mapping for `record_Identity` to `event.idm.read_only_udm.target.user.user_display_name`.  
\- Replaced the value of `record.IPAddress` in `record_IPAddress` and added a conditional check before already existing mapping for `record_IPAddress` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- Replaced the value of `record.Level` into string in `record_Level` and added a conditional check before already existing mapping for `record_Level` to `Level`.  
\- Replaced the value of `record.LocationDetails.city` in `record_LocationDetails_city` and added a conditional check before already existing mapping for `record_LocationDetails_city` to `properties.location.city`.  
\- Replaced the value of `record.LocationDetails.state` in `record_LocationDetails_state` and added a conditional check before already existing mapping for `record_LocationDetails_state` to `properties.location.state`.  
\- Replaced the value of `record.LocationDetails.countryOrRegion` in `record_LocationDetails_countryOrRegion` and added a conditional check before already existing mapping for `record_LocationDetails_countryOrRegion` to `properties.location.countryOrRegion`.  
\- Replaced the value of `record.LocationDetails.geoCoordinates.latitude` in `record_LocationDetails_geoCoordinates_latitude` and added a conditional check before already existing mapping to `event.idm.read_only_udm.principal.location.region_coordinates.latitude`.  
\- Replaced the value of `record.LocationDetails.geoCoordinates.longitude` in `record_LocationDetails_geoCoordinates_longitude` and added a conditional check before already existing mapping for `record_LocationDetails_geoCoordinates_longitude` to `event.idm.read_only_udm.principal.location.region_coordinates.longitude`.  
\- Replaced the value of `record.OperationName` in `record_OperationName` and added a conditional check before already existing mapping for `record_OperationName` to `event.idm.read_only_udm.metadata.product_event_type`.  
\- Replaced the value of `record.OperationVersion` in `record_OperationVersion` and added a conditional check before already existing mapping for `record_OperationVersion` to `operationVersion`.  
\- Replaced the value of `record.ResultSignature` in `record_ResultSignature` and added a conditional check before already existing mapping for `record_ResultSignature` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.RiskDetail` in `record_RiskDetail` and added a conditional check before already existing mapping for `record_RiskDetail` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.RiskEventTypes` in `record_RiskEventTypes` and added a conditional check before already existing mapping for `record_RiskEventTypes` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.RiskLevelAggregated` in `record_RiskLevelAggregated` and added a conditional check before already existing mapping for `record_RiskLevelAggregated` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.RiskState` in `record_RiskState` and added a conditional check before already existing mapping for `record_RiskState` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.SourceSystem` in `record_SourceSystem` and added a conditional check before already existing mapping for `record_SourceSystem` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.SignInIdentifier` in `record_SignInIdentifier` and added a conditional check before already existing mapping for `record_SignInIdentifier` to `event.idm.read_only_udm.principal.user.userid`.  
\- Replaced the value of `record.TenantId` in `record_TenantId` and added a conditional check before already existing mapping for `record_TenantId` to `tenantId`.  
\- Replaced the value of `record.TokenIssuerType` in `record_TokenIssuerType` and added a conditional check before already existing mapping for `record_TokenIssuerType` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.UniqueTokenIdentifier` in `record_UniqueTokenIdentifier` and added a conditional check before already existing mapping for `record_UniqueTokenIdentifier` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.UserAgent` in `record_UserAgent` and added a conditional check before already existing mapping for `record_UserAgent` to `event.idm.read_only_udm.network.http.user_agent` and parsed into `event.idm.read_only_udm.network.http.parsed_user_agent`.  
\- Replaced the value of `record.UserDisplayName` in `record_UserDisplayName` and added a conditional check before already existing mapping for `record_UserDisplayName` to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- Replaced the value of `record.UserId` in `record_UserId` and added a conditional check before already existing mapping for `record_UserId` to `event.idm.read_only_udm.principal.user.userid`.  
\- Replaced the value of `record.UserPrincipalName` in `record_UserPrincipalName` and added a conditional check before already existing mapping for `record_UserPrincipalName` to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- Replaced the value of `record.UserType` in `record_UserType` and added a conditional check before already existing mapping for `record_UserType` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record._Internal_WorkspaceResourceId` in `record__Internal_WorkspaceResourceId` and added a conditional check before already existing mapping for `record__Internal_WorkspaceResourceId` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record._ItemId` in `record__ItemId` and added a conditional check before already existing mapping for `record__ItemId` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.Resource` in `record_Resource` and added a conditional check before already existing mapping for `record_Resource` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceDisplayName` in `record_ResourceDisplayName` and added a conditional check before already existing mapping for `record_ResourceDisplayName` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceId` in `record_ResourceId` and added a conditional check before already existing mapping for `record_ResourceId` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceIdentity` in `record_ResourceIdentity` and added a conditional check before already existing mapping for `record_ResourceIdentity` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceServicePrincipalId` in `record_ResourceServicePrincipalId` and added a conditional check before already existing mapping for `record_ResourceServicePrincipalId` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceTenantId` in `record_ResourceTenantId` and added a conditional check before already existing mapping for `record_ResourceTenantId` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Replaced the value of `record.ResourceGroup` in `record_ResourceGroup` and added a conditional check before already existing mapping for `record_ResourceGroup` to `event.idm.read_only_udm.target.resource.attribute.labels`.  
-Added a grok pattern for `UserId` field to extract `first_user_id`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `first_user_id` with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- Placed the already existing mapping of `NETWORK_CONNECTION` event type above the mapping of `USER_UNCATEGORIZED` event type.   
2025-06-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `properties.location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- Removed the redundant code block.   
2025-05-06 |  Enhancement:  
\- `event.idm.ready_only_udm.security_result.description`: Newly mapped `policy.result` raw log field with `event.idm.ready_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `apc.displayName` from `event.idm.read_only_udm.security_result.rule_name` UDM field and mapped `policy.displayName` instead  
\- `event.idm.read_only_udm.security_result.rule_id`: Removed mapping of `apc.id` from `event.idm.read_only_udm.security_result.rule_id` UDM field and mapped `policy.id` instead  
\- `event.idm.read_only_udm.security_result.rule_labels`: Removed mapping of `apc.Result` from `event.idm.read_only_udm.security_result.rule_labels` UDM field and mapped `policy.Result` instead  
\- `event.idm.ready_only_udm.about.user.user_display_name`: Removed mapping of `policy.displayName` from `event.idm.ready_only_udm.about.user.user_display_name` UDM field.  
\- `event.idm.ready_only_udm.about.user.userid`: Removed mapping of `policy.id` from `event.idm.ready_only_udm.about.user.userid` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `policy.result` from `event.idm.read_only_udm.about.labels` UDM field.   
2025-04-22 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid` : Newly mapped `properties.servicePrincipalName` raw log field with `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.target.user.product_object_id` : Newly mapped `properties.servicePrincipalId` raw log field with `event.idm.read_only_udm.target.user.product_object_id`.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `properties.riskLevelAggregated` and `properties.riskLevelDuringSignIn` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- Added a null check condition before mapping `properties.authenticationProcessingDetails` to `event.idm.read_only_udm.additional.fields`.   
2025-03-18 |  Enhancement:  
\- Mapped `record.AuthenticationProtocol` to `security_result.detection_fields`.  
\- Mapped `properties.authenticationProtocol` to `security_result.detection_fields`.  
\- Mapped `authenticationProtocol` to `security_result.detection_fields`.  
\- Mapped `properties.sessionId` to `network.session_id`.  
\- Mapped `properties.uniqueTokenIdentifier` to `additional.fields`.  
\- Mapped `properties.appServicePrincipalId` to `additional.fields`.  
\- Mapped `properties.autonomousSystemNumber` to `additional.fields`.  
\- Mapped `properties.resourceOwnerTenantId` to `additional.field`.   
2025-02-27 |  Enhancement:  
\- Mapped `operationName` to `additional.fields`.  
\- Mapped `displayName` to `principal.hostname`.  
\- When `has_target_user` is `true` and `has_principal_user` is `true`, then mapped `metadata.event_type` to `USER_CHANGE_PERMISSIONS`.   
2025-02-13 |  Enhancement:  
\- Mapped `ActorIpAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ClientIP` to `target.ip` and `target.asset.ip`.  
\- Mapped `ApplicationId`, `ActorContextId`, `InterSystemsId`, and `IntraSystemId` to `security_result.detection_fields`.  
\- Mapped `ObjectId` to `principal.resource.product_object_id`.  
\- Mapped `Operation` to `metadata.product_event_type`.  
\- Mapped `OrganizationId` to `principal.resource.id`.  
\- Mapped `RecordType`, `SupportTicketId`, and `TargetContextId` to `security_result.detection_fields`.  
\- Mapped `targets.ID` and `targets.Type` to `target.resource.attribute.labels`.  
\- Mapped `UserId` to `principal.user.userid`.  
\- Mapped `ResultStatus`, `ErrorNumber`, and `Workload` to `additional.fields`.  
\- Mapped `Version` to `metadata.product_version`.  
\- Mapped `UserKey` and `UserType` to `principal.user.attribute.labels`  
\- Mapped `DeviceProperties.ID` to `principal.asset_id`.  
\- Mapped `DeviceProperties.DisplayName` to `principal.user.user_display_name`.  
\- Mapped `DeviceProperties.SessionId` to `network.session_id`.  
\- Mapped `extendedproperty.UserAgent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `Actor.ID` and `Actor.Type` to `principal.resource.attribute.labels`.  
\- Mapped `AssociatedAdminUnits` to `security_result.detection_fields`.  
\- Mapped `AzureActiveDirectoryEventType` to `security_result.summary`.  
\- Mapped `CreationTime` to `metadata.event_timestamp`.   
2025-01-11 |  Enhancement:  
\- Moved `security_result.summary`, `security_result.severity`, `security_result.rule_id`, `security_result.action`, and `security_result.category` out of conditional check.   
2024-12-05 |  Enhancement:  
\- Added support for new format of JSON logs.   
2024-10-07 |  Enhancement:  
\- Mapped `properties.userPrincipalName` to `target.user.userid`.   
2024-09-04 |  Enhancement:  
\- Removed mapping of `correlationId` from `network.session_id`.   
2024-08-22 |  Enhancement:  
\- When `displayName` is `iphone`, then mapped to `principal.resource.attribute.labels`.   
2024-07-05 |  Enhancement:  
\- Mapped `isInteractive` to `security_result.detection_fields`.   
2024-06-03 |  \- Changed mapping of `policies.displayName` from `about.user.user_display_name` to `security_result.rule_name`.  
\- Changed mapping of `policies.id` from `about.user.userid` to `security_result.rule_id`.  
\- Changed mapping of `policies.result` from `about.labels` to `security_result.detection_fields`.   
2024-05-29 |  Enhancement:  
\- When `status.errorCode` is `0`, then set `security_result.action` to `ALLOW`.   
2024-05-13 |  Bug-Fix:  
\- Mapped `userPrincipalName` to `target.user.userid`.   
2024-05-10 |  Enhancement:  
\- Mapped `networkLocationDetails.n.networkNames`, `properties.networkLocationDetails.n.networkNames`, `networkLocationDetails.n.networkType` and `properties.networkLocationDetails.n.networkType` to `additional.fields`.  
\- Mapped `properties.userAgent` and `userAgent` to `network.http.user_agent` and `network.http.parsed_user_agent`.   
2024-05-03 |  Bug-Fix:  
\- Added `on_error` check before mapping `target.modifiedProperties.n.newValue`.  
\- Mapped `target.modifiedProperties.n.oldValue` and `target.modifiedProperties.n.displayName` to `target.resource.attribute.labels`.  
\- Mapped `activityDisplayName` to `security_result.summary`.   
2024-04-30 |  Enhancement:  
\- Mapped `properties.authenticationDetails`, `properties.networkLocationDetails`, `properties.authenticationRequirementPolicies`, `networkLocationDetails` and `authenticationRequirementPolicies` to `security_result.detection_fields`.   
2024-04-02 |  Enhancement:  
\- Mapped `authenticationRequirement` to `additional.fields`.   
2024-02-26 |  Enhancement:  
\- Mapped `appliedConditionalAccessPolicies` to `security_result`.  
\- Mapped `isInteractive` to `extensions.auth.mechanism`.  
\- Mapped `location.geoCoordinates.altitude` to `additional.fields`.   
2024-02-09 |  Enhancement:  
\- Mapped `authenticationDetails.authenticationMethod`, `authenticationDetails.authenticationMethodDetail`, `authenticationDetails.authenticationStepResultDetail`, `authenticationDetails.authenticationStepDateTime`, and `authenticationDetails.authenticationStepRequirement` to `security_result.detection_fields`.  
\- Mapped `authenticationDetails.succeeded` to `security_result.action`.  
\- Mapped `status.additionalDetails` to `security_result.description`.   
2024-01-11 |  Enhancement:  
\- Mapped `correlationId` to `security_result.detection_fields`.   
2023-11-20 |  Enhancement:  
\- Mapped `tenantId` to `metadata.product_deployment_id`.  
\- Mapped `Level` to `security_result.severity_details` and `security_result.severity`.  
\- Mapped `properties.userDisplayName` to `target.user.user_display_name`.  
\- Mapped `identity` to `target.user.user_display_name`.  
\- Mapped `properties.activityDateTime` to `metadata.event_timestamp`.  
\- Mapped `properties.activity` to `security_result.summary`.  
\- Mapped `resultSignature`, `properties.riskLevel`, `properties.isGuest`, `properties.isDeleted`, `properties.isProcessing`,  
`properties.riskLastUpdatedDateTime`, `properties.riskType`, `properties.riskEventType`, `properties.riskState`, `properties.riskDetail`, `properties.source`, `properties.detectionTimingType`  
`properties.detectedDateTime`, `properties.lastUpdatedDateTime`, `properties.tokenIssuerType`, `properties.homeTenantId`, `properties.userType`, `properties.crossTenantAccessType`, `durationMs` to `additional.fields`.  
\- Mapped `resourceId` to `target.resource.product_object_id`.  
\- Mapped `properties.location.geoCoordinates.longitude` and `location.geoCoordinates.longitude` to `principal.location.region_coordinates.longitude`.  
\- Mapped `properties.location.geoCoordinates.latitude` and `location.geoCoordinates.latitude` to `principal.location.region_coordinates.latitude`.   
2023-07-12 |  Enhancement:  
\- Mapped `deviceDetail.isCompliant`, `deviceDetail.isManaged`, `deviceDetail.trustType` to `principal.asset.attribute.labels`.  
\- Mapped `deviceDetail.deviceId` to `principal.asset.asset_id`.  
\- Mapped `deviceDetail.browser` to `network.http.user_agent`.  
\- Mapped `deviceDetail.operatingSystem` to `principal.platform_version`.  
\- Mapped `status.failureReason` to `additional.fields`.  
\- Mapped `status.errorCode` to `security_result.rule_id`.  
\- Mapped `deviceDetail.displayName` to `principal.asset.hardware`.   
2023-03-14 |  Enhancement:  
\- Mapped `browser` to `principal.resource.attribute.labels`.  
\- Mapped `isCompliant`, `isManaged`, `trustType`, to `principal.asset.attribute.labels`.  
\- Mapped `domain` form `userPrincipalName` to `principal.administrative_domain`.   
2022-12-16 |  Enhancement:  
\- Added conditional check for the field `initiatedBy.user.userPrincipalName` and mapped to `principal.user.email_addresses`.   
2022-10-28 |  Enhancement:  
\- Mapped `additionalDetails.0.value` to `network.http.user_agent`.  
\- Mapped `additionalDetails.1.value` to `target.resource.attribute.labels`.  
\- Mapped `Id` to `metadata.product_log_id`.  
\- Mapped `initiatedBy.user.id` to `principal.user.userid`.  
\- Mapped `initiatedBy.user.displayName` to `principal.user.user_display_name`.  
\- Mapped `initiatedBy.user.ipAddress` to `principal.ip`.  
\- Mapped `initiatedBy.user.userPrincipalName` to `principal.user.email_addresses`.  
\- Mapped `operationType` to `security_result.action_details`.  
\- Mapped `target.displayName` to `target.resource.name`.  
\- Mapped `target.id` to `target.resource.id`.  
\- Mapped `target.type` to `target.resource.type`.  
\- Mapped `field.newValue` to `target.resource.product_object_id` if field.displayName is `AppRole.Id` else mapped `field.newValue` to `target.resource.attribute.labels`.  
\- Added check for errorCode.  
\- Mapped `loggedByService` to `target.application`.  
\- Mapped `activityDisplayName` to `metadata.product_event_type`.  
\- Mapped `metadata.event_type` to `USER_RESOURCE_UPDATE_PERMISSIONS` where `activityDisplayName` is `Add app role assignment to service principal`.   
2022-08-25 |  Enhancement:  
\- If `properties.initiatedBy.user.userPrincipalName` matches `email regex pattern` then mapped to `principal.user.email_addresses` else mapped to `principal.user.userid`.  
\- If `properties.userPrincipalName` or `userPrincipalName` matches `email regex pattern` then mapped to `target.user.email_addresses` else mapped to `target.user.userid`.   
2022-08-11 |  Enhancement:  
\- Removed drop tag `TAG_MALFORMED_ENCODING`.  
\- Added `event_type` `GENERIC_EVENT`.   
2022-05-29 |  Enhancement - Modified the for loop for the field `riskEventTypes_v2` mapped to `additional.fields`.  
Mapped the field `level` to `security_result.severity_details`.  
Mapped the field `properties.result` to `security_result.action_details`.   
2022-04-20 |  Bug-fix - Parsed the logs with event `appDisplayName`: `NotApplicable`.  
\- Modified the for loop for the field `riskEventTypes`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
