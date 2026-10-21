---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-resource-logs-changelog/
title: Change log for AZURE_RESOURCE_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:55:25.207604+00:00
---

# Change log for AZURE_RESOURCE_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-resource-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_RESOURCE_LOGS

Date | Changes  
---|---  
2026-07-27 |  Enhancement:  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Removed mapping of `properties.location.geoCoordinates.latitude` from `event.idm.read_only_udm.principal.location.region_latitude` UDM field as it is a deprecated field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Mapped `properties.location.geoCoordinates.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Removed mapping of `properties.location.geoCoordinates.longitude` from `event.idm.read_only_udm.principal.location.region_longitude` UDM field as it is a deprecated field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Mapped `properties.location.geoCoordinates.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.cloud.environment`: Removed mapping of `MICROSOFT_AZURE` value from `event.idm.read_only_udm.target.cloud.environment` UDM field as it is a deprecated field.  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.environment`: Mapped `MICROSOFT_AZURE` value to `event.idm.read_only_udm.target.asset.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `properties.appDisplayName` raw log field with `event.idm.read_only_udm.target.application` UDM field  
\- `event.idm.read_only_udm.network.asn`: Newly mapped `properties.autonomousSystemNumber` raw log field with `event.idm.read_only_udm.network.asn` UDM field  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.ipAddressFromResourceProvider`, `properties.globalSecureAccessIpAddress` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `identity` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `durationMs` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.status.additionalDetails` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.security_result.severity`: Updated the value of `event.idm.read_only_udm.security_result.severity` based on `level` raw log field.  
\- `event.idm.read_only_udm.security_result.action`: When `resultType` is 0, updated the `event.idm.read_only_udm.security_result.action` value to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `resourceId`, `authenticationMethod`, `authenticationStepRequirement`, `authenticationStepResultDetail`, `succeeded`,`authenticationStepDateTime`, `authenticationMethodDetail`, `RequestSequence`, `StatusSequence` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `operationVersion`, `properties.tokenIssuerName`, `properties.homeTenantName`, `properties.alternateSignInName`, `properties.signInIdentifier`, `properties.federatedCredentialId`, `properties.servicePrincipalCredentialThumbprint`, `properties.appServicePrincipalId`, `properties.clientSessionId`, `properties.appOwnerTenantId`, `properties.sourceAppClientId`, `properties.redirectUrl`, `properties.privateLinkDetails`, `properties.authenticationContextClassReferences`, `properties.authenticationRequirementPolicies`, `properties.sessionLifetimePolicies`, `properties.conditionalAccessAudiences`, `properties.isInteractive`, `properties.clientCredentialType`, `properties.authenticationProtocol`, `properties.signInTokenProtectionStatus`, `properties.tokenProtectionStatusDetails.signInSessionStatus`, `properties.tokenProtectionStatusDetails.signInSessionStatusCode`, `properties.incomingTokenType`, `properties.processingTimeInMilliseconds`, `properties.agent.agentType`, `properties.agent.agentSubjectType`, `properties.resourceTenantId`, `properties.homeTenantId`, `properties.resourceOwnerTenantId`, `properties.uniqueTokenIdentifier`, `properties.flaggedForReview`, `properties.isTenantRestricted`, `properties.isThroughGlobalSecureAccess`, `properties.originalTransferMethod`, `properties.resourceServicePrincipalId`, `signInEventTypes` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-12 |  Enhancement:  
\- Mapped `properties.log` to `security_result.detection_fields`.  
\- Mapped `properties.roleInstance` to `target.resource.attribute.labels`.  
\- Mapped `properties.message` to `metadata.description`.  
\- Mapped `properties.hostVersion` , `properties.functionInvocationId` , `properties.hostInstanceId` , `properties.levelId` , `properties.eventId` , and `properties.eventName` to additional.fields.   
2025-01-06 |  Enhancement:  
\- Mapped `ipAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `Region` to `principal.location.country_or_region`.  
\- Mapped `Environment`, `TaskName`, `ActivityId`, `subscriptionId`, and `namespaceName` to `security_result.detection_fields`.   
2024-10-29 |  Enhancement:  
\- If `resource_type` is `MANAGEDCLUSTERS`, then set `target.resource.type` to `CLUSTER`.  
\- If `resource_type` is `MANAGEDINSTANCES`, then set `target.resource.type` to `VIRTUAL_MACHINE`.  
\- If `resource_type` is `DATABASEACCOUNTS`, then set `target.resource.type` to `DATABASE`.   
2024-10-17 |  Enhancement:  
\- Mapped `count`, `total`, `minimum`, `ApiName`, `Authentication`, `ScaleUnit`, `pod`, and `containerID` to `security_result.detection_fields`.  
\- Mapped `Region` to `principal.location.name`.  
\- Mapped `processId` to `principal.process.pid`.  
\- Mapped `action` to `security_result.action_details`.   
2024-08-29 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-07-24 |  Enhancement:  
\- Mapped `Role.DisplayName`, `Role.TemplateId` to `security_result.detection_fields`.  
\- Initialized `authenticationStepResultDetail` to parse unparsed logs.   
2024-05-10 |  Bug-Fix:  
\- Changed mapping of `conditionalAccessStatus` from `security_result.about.labels` to `security_result.about.resource.attribute.labels`.   
2024-03-13 |  Enhancement:  
\- Mapped additional fields for `AADNonInteractiveUserSignInLogs`, `AADManagedIdentitySignInLogs`, `AADProvisioningLogs`, and `AADServicePrincipalSignInLogs`.  
\- Mapped `properties.correlationId` to `security_result.detection_fields`.   
2023-12-11 |  Enhancement:  
\- Mapped `properties.requestId`, `properties.riskEventType`, `properties.tokenIssuerType` and `properties.keyIds` to `target.resource.attribute.labels`.  
\- Mapped `properties.detectionTimingType` to `additional.fields`.  
\- Mapped `properties.appliedConditionalAccessPolicies` to `about.labels`.  
\- Mapped `properties.authenticationProcessingDetails` to `security_result.detection_fields`.  
\- Mapped `properties.additionalInfo.userAgent` to `network.http.user_agent`.  
\- Mapped `properties.additionalInfo.alertUrl` to `target.url`.   
2023-10-04 |  Bug-Fix:  
\- When the JSON filter fails, added `on_error` for the JSON filter and dropped the log with tag `TAG_MALFORMED_MESSAGE`.  
\- When there is no error in `CONVERT` filter which converts to integer for `properties.ScStatus`,`properties.statusCode`,`statusCode`,`record.properties.ScStatus`, and `record.properties.statusCode`, then mapped to `network.http.response_code`.  
\- Added a condition for `responseStatus.code` and `record.responseStatus.code`. When `on_error` for `CONVERT` is not true, then mapped to `network.http.response_code`.   
2023-09-04 |  Enhancement:  
-Mapped the following fields under `properties.additionalDetails`:  
\- Mapped value as `metadata.product_deployment_id` where key is `TenantId`.  
\- Mapped value as `security_result.rule_id` where key is `PolicyId`.  
\- Mapped value as `network.http.user_agent` where key is `Client`.  
\- Mapped value as `principal.user.email_addresses` where key is `LocalAccountUsername`.  
\- Mapped value as `principal.administrative_domain` where key is `DomainName`.  
\- Mapped `properties.targetResources.userPrincipalName` to `target.user.email_addresses`.  
\- Mapped `properties.initiatedBy.app.appId` to `target.resource.attribute.labels`.   
2023-08-04 |  Enhancement:  
\- Mapped `properties.initiatedBy.user.userPrincipalName` to `principal.user.userid`.   
2023-07-10 |  Enhancement:  
\- Initialized `UnderlayClass`,`record.UnderlayClass`,`UnderlayName`,`record.UnderlayName` fields and checked for null.   
2022-11-18 |  Enhancement:  
\- `security_result.action` is BLOCK by default added condition to avoid that only if `properties.succeeded` is `false`,`statusText` is `fail/false`,`resultType` is `fail/failed` then security_result.action is `BLOCK`.   
2022-11-11 |  Bug-Fix - Added null check for `properties.log.annotations.authorization`.  
\- Added on_error statement for `properties.log.annotations.authorization.k8s.io/decision`, `properties.log.annotations.authorization.k8s.io/reason`.   
2022-10-20 |  Bug-fix  
\- Added a condition when resultType is `success` security_results.action should be ALLOW instead of BLOCK by default.  
\- Mapped event_type to `USER_LOGIN` and extensions.auth.type to `AUTH_UNSPECIFIED` when operationName is `Sign-in Activity`.  
\- Mapped `callerIpAddress` to `principal.ip` when `properties.ipAddress` is empty.  
\- Mapped eventy_type to `USER_RESOURCE_ACCESS` when `callerIpAddress` is not empty and `target.resource` is not empty.   
2022-10-03 |  Enhancement - Mapped following fields :  
\- Mapped `statusCode` to `network.http.response_code`.  
\- Mapped `correlationId` to `security_result.detection_fields`.  
\- Mapped `properties.userAgentHeader` to `network.http.user_agent`.  
\- Mapped `properties.accountName` to `principal.user.userid`.  
\- Mapped `properties.objectKey` to `target.resource.attribute.labels`.  
\- Mapped `properties.clientRequestId` to `target.resource.attribute.labels`.  
\- Mapped `properties.responseMd5` to `target.resource.attribute.labels`.  
\- Mapped `properties.tlsVersion` to `network.tls.version`.  
\- Mapped `uri` to `network.http.referral_url`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `resourceType` to `target.resource.type`.  
\- Mapped `statusText` to `security_result.summary`.   
2022-08-11 |  Bug-fix  
\- Remapped `properties.deviceDetail.displayName` to `principal.asset.hardware.model`.   
2022-07-18 |  Enhancement - Mapped following fields :  
\- mapped `properties.activity` to `metadata.description`.  
\- mapped `properties.riskType` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.riskLevelDuringSignIn` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.riskLevelAggregated` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.originalRequestId` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `Level`,`tenantId` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.conditionalAccessStatus` to `security_result.about.labels`.  
\- mapped `properties.userType` to `target.user.attribute.labels`.  
\- mapped `properties.provisioningSteps.0.details.city` to `principal.location.city`.  
\- mapped `properties.provisioningSteps.0.details.country` to `principal.location.country_or_region`.  
\- mapped `properties.sourceSystem.Id` to `principal.resource.product_object_id`.  
\- mapped `properties.sourceIdentity.details.id` to `principal.user.product_object_id`.  
\- mapped `properties.sourceSystem.Name` to `principal.resource.name`.  
\- mapped `properties.accountEnabled`,`properties.isProcessing`,`properties.isGuest`,`properties.isDeleted` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.authenticationRequirement`, `properties.status.errorCode`, `properties.statusInfo.Status` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.sourceIdentity.details.odatatype`, `properties.provisioningSteps.0.details.appRoleAssignments` to `principal.user.attribute.labels`.  
\- mapped `properties.sourceIdentity.details.UserPrincipalName`, `properties.ServicePrincipalId` to `principal.user.userid`.  
\- mapped `properties.source`,`correlationId`, `properties.activityDateTime`, `properties.detectedDateTime`,`properties.lastUpdatedDateTime` to `security_result.detection_fields`.  
\- mapped `properties.sourceIdentity.details.DisplayName`, `properties.ServicePrincipalDisplayName`, `properties.servicePrincipalName` to `principal.user.user_display_name`.  
\- mapped `properties.servicePrincipalType`, `properties.servicePrincipalCredentialKeyId` to `principal.resource.attribute.labels`.  
\- mapped `properties.deviceDetail.isCompliant`, `properties.deviceDetail.isManaged` to `principal.asset.attribute.labels`.   
2022-06-26 |  Parsed logs having `category` value as `UserRiskEvents` , `RiskyUsers` , `RiskyServicePrincipals` , `ServicePrincipalSignInLogs` , `NonInteractiveUserSignInLogs` , `ProvisioningLogs` , `ADFSSignInLogs`.  
\- mapped `properties.ipAddress` to `principal.ip`.  
\- mapped `properties.id` to `metadata.product_log_id`.  
\- mapped `properties.displayName` to `target.application`.  
\- mapped `properties.location.city` to `principal.location.city`.  
\- mapped `properties.location.state` to `principal.location.state`.  
\- mapped `properties.userDisplayName` to `target.user.user_display_name`.  
\- mapped `properties.userId` to `target.user.product_object_id`.  
\- mapped `properties.appId` to `target.resource.attribute.labels`.  
\- mapped `properties.resourceDisplayName` to `target.resource.name`.  
\- mapped `properties.resourceId` to `target.resource.product_object_id`.  
\- mapped `properties.deviceDetail.operatingSystem` to `principal.platform_version`.  
\- mapped `properties.deviceDetail.browser` to `network.http.user_agent`.  
\- mapped `properties.deviceDetail.deviceId` to `principal.asset.asset_id`.  
\- mapped `properties.deviceDetail.displayName` to `principal.asset.hostname`.  
\- mapped `properties.sourceIdentity.details.id` to `principal.user.product_object_id`.  
\- mapped `properties.location.countryOrRegion` to `principal.location.country_or_region`.  
\- mapped `properties.location.geoCoordinates.latitude` to `principal.location.region_latitude`.  
\- mapped `properties.location.geoCoordinates.longitude` to `principal.location.region_longitude`.  
\- mapped `properties.sourceIdentity.details.DisplayName` to `principal.user.user_display_name`.  
\- mapped `properties.authenticationDetails.0.authenticationMethodDetail` to `security_result.about.labels`.  
\- mapped `properties.riskLevel`, `properties.riskState`, `properties.riskDetail` to `event.idm.read_only_udm.additional.fields`.  
\- If value of `properties.authenticationDetails.0.authenticationMethod` is `Password`, then mapped `extensions.auth.mechanism` to `USERNAME_PASSWORD`.  
\- If value of `properties.userPrincipalName` is in email format then mapped it to `target.user.userid` and `target.user.email_addresses` , else mapped it only to `target.user.userid`.  
\- If value of `properties.sourceIdentity.details.UserPrincipalName` is in email format then mapped it to `principal.user.userid` and `principal.user.email_addresses` , else mapped it only to `principal.user.userid`.  
For category `NonInteractiveUserSignInLogs` :  
\- mapped `properties.deviceDetail.trustType` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `properties.clientAppUsed` to `principal.application`.  
For category `UserRiskEvents` :  
\- If value of `properties.additionalInfo.Key` is `userAgent`, then mapped `properties.additionalInfo.Value` to `network.http.user_agent`.   
2022-05-31 |  Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
