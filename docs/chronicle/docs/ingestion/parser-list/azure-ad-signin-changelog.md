---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-signin-changelog/
title: Change log for AZURE_AD_SIGNIN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:57.368065+00:00
---

# Change log for AZURE_AD_SIGNIN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-signin-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_AD_SIGNIN

Date | Changes  
---|---  
2026-09-15 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `resultSignature` from `event.idm.read_only_udm.additional.fields` since it represents action details and `event.idm.read_only_udm.security_result.action_details` is a more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action`: Mapped `resultSignature` raw log field to `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ConditionalAccessAudiences`, `Agent.agentSubjectType`, `_IsBillable`, `_BilledSize` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `DeviceDetail.isCompliant`, `DeviceDetail.isManaged` raw log fields to `event.idm.read_only_udm.principal.asset.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `StatusSequence`, `RequestSequence` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.rule_labels`: Newly mapped `apc.Result`, `apc.result` raw log fields to `event.idm.read_only_udm.security_result.rule_labels`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `ServicePrincipalName`, `servicePrincipalName`, `properties.servicePrincipalName` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels`.   
2026-09-02 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `resourceDisplayName` from `event.idm.read_only_udm.security_result.detection_fields` UDM field because `resourceDisplayName` identifies standard metadata about the target asset, not a security alert or detection.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `resourceDisplayName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `AuthenticationRequirement` from `event.idm.read_only_udm.additional.fields` UDM field because `AuthenticationRequirement` identifies specific authentication mechanism metadata, not a generic vendor-specific fallback.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Mapped `AuthenticationRequirement` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `processingTimeInMilliseconds`, `source`, `cribl_breaker`, `status.failureReason`, `signInTokenProtectionStatus`, `conditionalAccessAudiences`, `_time`, `originalRequestId`, `agent.agentType`, `agent.agentSubjectType`, `authenticationContextClassReferences.id`, `authenticationContextClassReferences.detail`, `tokenProtectionStatusDetails.signInSessionStatusCode`, `tokenProtectionStatusDetails.signInSessionStatus` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `homeTenantId`, `signInEventTypes`, `flaggedForReview`, `appOwnerTenantId`, `isTenantRestricted`, `isThroughGlobalSecureAccess`, `networkLocationDetails.networkType`, `networkLocationDetails.networkNames`, `uniqueTokenIdentifier`, `resourceTenantId`, `resourceOwnerTenantId`, `autonomousSystemNumber` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `status.additionalDetails` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `servicePrincipalId`, `resourceServicePrincipalId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `deviceDetail.displayName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `userType` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `deviceDetail.operatingSystem` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Added fallback logic to set to `IOS` if `deviceDetail.operatingSystem` matches `ios`.   
2026-08-17 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.resultType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `time` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field since `time` represents the collection timestamp, not the event occurrence time.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Retained `properties.createdDateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field, as it was previously overwritten by `time`.   
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `properties.userId` from `event.idm.read_only_udm.target.user.userid` UDM field since `properties.userId` represents the product object id of the user.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Mapped `properties.userId` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Removed mapping of `properties.appDisplayName` from `event.idm.read_only_udm.principal.application` UDM field since `properties.appDisplayName` represents the application name of the target resource.  
\- `event.idm.read_only_udm.target.application`: Mapped `properties.appDisplayName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.application`: Removed mapping of `resourceDisplayName` from `event.idm.read_only_udm.target.application` UDM field since `properties.resourceDisplayName` represents the resource display name of the target resource.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `resourceDisplayName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `clientAppUsed` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.application`: Mapped `clientAppUsed` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `deviceDetail.deviceId` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id`: Mapped `deviceDetail.deviceId` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `deviceDetail.isCompliant` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `deviceDetail.isCompliant` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `deviceDetail.isManaged` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `deviceDetail.isManaged` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `deviceDetail.trustType` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `deviceDetail.trustType` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `properties.deviceDetail.browser` from `event.idm.read_only_udm.security_result.detection_fields` UDM field in order to introduce more specific mapping.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `properties.deviceDetail.browser` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `DeviceDetail.displayName` from `event.idm.read_only_udm.security_result.detection_fields` UDM field since `DeviceDetail.displayName` consists of hostname details.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `properties.deviceDetail.displayName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `properties.appId` from `event.idm.read_only_udm.security_result.detection_fields` UDM field since `properties.appId` consists of application id of the target resource.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `properties.appId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.email_address`: Newly mapped `properties.userPrincipalName` raw log field with `event.idm.read_only_udm.target.user.email_address` UDM field, if `properties.userPrincipalName` is an email address.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `properties.userPrincipalName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field, if `properties.userPrincipalName` is not an email address.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `properties.location.countryOrRegion` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `ip_address_from_resource_provider` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `properties.redirectUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `properties.homeTenantName` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.deviceDetail.operatingSystem`, `properties.originalTransferMethod`, `properties.authenticationProtocol` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `properties.federatedCredentialId`, `properties.servicePrincipalCredentialKeyId`, `properties.servicePrincipalCredentialThumbprint`, `properties.sourceAppClientId`, `properties.appServicePrincipalId`, `properties.signInIdentifier`, `properties.alternateSignInName`, `properties.riskLevelDuringSignIn`, `properties.riskEventTypes`, `properties.riskEventTypes_v2`, `properties.authenticationRequirementPolicies`, `properties.sessionLifetimePolicies`, `properties.authenticationStrengths` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- Added a grok pattern on `properties.ipAddressFromResourceProvider` to extract `ip_address_from_resource_provider`.  
\- Newly added JSON filter to parse `DeviceDetail` raw log field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_labels`: Newly mapped `properties.appliedConditionalAccessPolicies.conditionsSatisfied`, `properties.appliedConditionalAccessPolicies.conditionsNotSatisfied` raw log field with `event.idm.read_only_udm.security_result.rule_labels`.  
\- Added a conditional check before mapping existing `properties.appliedConditionalAccessPolicies.displayName`, `properties.appliedConditionalAccessPolicies.id`, `properties.appliedConditionalAccessPolicies.result`, `properties.appliedConditionalAccessPolicies.enforcedGrantControls`, `properties.appliedConditionalAccessPolicies.enforcedSessionControls` for these raw log fields. Updated and corrected mappings for these raw log fields to parse these raw log fields in correct manner.   
2026-01-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `TimeGenerated` raw log field(s) from `event.idm.read_only_udm.metadata.event_timestamp` UDM field to avoid if/else-if logic conflicts with `CreatedDateTime`, ensuring both fields are captured independently when `TimeGenerated` is remapped to `metadata.collected_timestamp`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `TimeGenerated` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Added prefix `DeviceDetail_` to the keys for `AuthenticationProcessingDetails` raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Updated the logic for `AuthenticationContextClassReferences` to parse as a JSON array instead of a single string, ensuring each key-value pair is individually extracted and searchable.   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `authenticationRequirement`, `RiskEventTypes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-19 |  Enhancement:  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `Status.errorCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `Status.failureReason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `cribl.cribl_data.cribl_enrichment.topic_name`, `cribl.cribl_data.cribl_enrichment.cribl_source`, `AlternateSignInName`, `SignInIdentifier`, `DeviceDetail.deviceId`, `DeviceDetail.trustType`, `TokenIssuerName`, `AADTenantId`, `authdetail.authenticationMethod`, `authdetail.authenticationMethodDetail`, `authdetail.authenticationStepDateTime`, `authdetail.authenticationStepRequirement`, `authdetail.authenticationStepResultDetail`, `networklocation.networkType`, `networklocation.networkNames` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `authdetail.succeeded` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `authdetail.succeeded` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- Renamed raw field `ClientAppUsed` to `clientAppUsed` before JSON parsing to parse the field correctly.  
\- Removed PII data from the log file.   
2025-12-10 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Agent.agentType`, `AuthenticationContextClassReferences`, `AuthenticationProtocol`, `AuthenticationRequirement`, `ClientCredentialType`, `TimeGenerated`, `AuthenticationProcessingDetails` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `IsInteractive`, `DeviceDetail.displayName`, `OperationVersion`, `AppOwnerTenantId`, `CrossTenantAccessType`, `IsTenantRestricted`, `IsThroughGlobalSecureAccess`, `Type`, `_TimeReceived`, `AuthenticationRequirementPolicies` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.timestamp`: Newly mapped `CreatedDateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-01 |  Enhancement:  
\- Replaced values of new raw log field names to their corresponding old raw log field names to map data to UDM fields using existing mappings as follows:  
\-- `RiskDetail` -> `riskDetail`  
\-- `RiskLevelAggregated` -> `riskLevelAggregated`  
\-- `RiskLevelDuringSignIn` -> `riskLevelDuringSignIn`  
\-- `RiskState` -> `riskState`  
\-- `ResourceDisplayName` -> `resourceDisplayName`  
\-- `ResourceId` -> `resourceId`  
\-- `ResultSignature` -> `resultSignature`  
\- Added a condition check to process the `ConditionalAccessPolicies` raw log field only when it contains a string value it can enter into mappings of `ConditionalAccessPolicies` raw log field mapping to prevent parsing errors.  
\- Newly added for loop for `ConditionalAccessPolicies` , `apc.enforcedSessionControls` , and `apc.enforcedGrantControls` raw log field to parse its respective fields.  
\- `event.idm.read_only_udm.security_result.rule_name` : Newly mapped `apc.displayName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id` : Newly mapped `apc.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_labels` : Newly mapped `apc.Result`, `apc.conditionsSatisfied`, `apc.conditionsNotSatisfied` , `apc.enforcedGrantControls` , and `apc.enforcedSessionControls` raw log field with `event.idm.read_only_udm.security_result.rule_labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `SourceSystem`, `SessionLifetimePolicies`, `SessionId`, `ResourceTenantId`, `ResourceOwnerTenantId`, `TokenProtectionStatusDetails.signInSessionStatusCode`, `TokenProtectionStatusDetails.signInSessionStatus`, `DeviceDetail.browser`, `DeviceDetail.operatingSystem` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Newly mapped `ResourceServicePrincipalId` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `ResourceIdentity` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `Resource`, `ProcessingTimeInMilliseconds`, `OriginalTransferMethod`, `OriginalRequestId`, `Status.additionalDetails`, `RiskEventTypes_V2`, `IncomingTokenType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.city` : Newly mapped `LocationDetails.city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region` : Newly mapped `LocationDetails.countryOrRegion` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.state` : Newly mapped `LocationDetails.state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude` : Newly mapped `LocationDetails.geoCoordinates.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude` : Newly mapped `LocationDetails.geoCoordinates.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.   
2024-10-17 |  Enhancement:  
\- Mapped `userDisplayName` to `principal.user.user_display_name`.  
\- Mapped `userPrincipalName` to `principal.user.email_addresses`.  
\- Mapped `appDisplayName` to `principal.application`.  
\- Mapped `ipAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `userId` to `principal.user.userid`.  
\- Mapped `resourceDisplayName` to `target.application`.  
\- Mapped `status.errorCode` to `network.http.response_code`.  
\- Mapped `failureReason` to `security_result.summary`.  
\- Mapped `deviceDetail.operatingSystem` to `principal.platform`.  
\- Mapped `appId`, `clientAppUsed`, `conditionalAccessStatus`, `deviceDetail.deviceId`, `deviceDetail.deviceName`, `deviceDetail.browser`, `deviceDetail.isCompliant`, `deviceDetail.isManaged`, and `deviceDetail.trustType` to `security_result.detection_fields`.  
\- Mapped `location.city` to `principal.location.city`.  
\- Mapped `location.state` to `principal.location.state`.  
\- Mapped `location.countryOrRegion` to `principal.location.country_or_region`.  
\- Mapped `location.geoCoordinates.latitude` to `principal.location.region_coordinates.latitude`.  
\- Mapped `location.geoCoordinates.longitude` to `principal.location.region_coordinates.longitude`.   
2024-07-18 |  Enhancement:  
\- Added support for JSON logs containing array of logs.   
2024-05-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
