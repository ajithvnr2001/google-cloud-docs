---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-storage-audit-changelog/
title: Change log for AZURE_STORAGE_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:55.347986+00:00
---

# Change log for AZURE_STORAGE_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-storage-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_STORAGE_AUDIT

Date | Changes  
---|---  
2026-07-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `properties.accountName` from `event.idm.read_only_udm.principal.user.userid` UDM field since it is the storage account whose requests are being logged and the service receiving the request.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `properties.accountName` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Removed mapping of `storageAccounts` from `event.idm.read_only_udm.intermediary.hostname` UDM field as this a storage account name.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `storageAccounts` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Removed mapping of `uri` from `event.idm.read_only_udm.network.http.referral_url` UDM field since this is a request target url.  
\- `event.idm.read_only_udm.target.url`: Mapped `uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.src.user.userid`: Removed mapping of `identity.requester.upn` from `event.idm.read_only_udm.src.user.userid` UDM field since this is the principal user name of the requester.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `identity.requester.upn` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.src.user.product_object_id`: Removed mapping of `identity.requester.objectId` from `event.idm.read_only_udm.src.user.product_object_id` UDM field since this is the object id of the principal user requester.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Mapped `identity.requester.objectId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Removed mapping of `identity.autorization.principals.id` from `event.idm.read_only_udm.principal.user.product_object_id` UDM field since this is security principal id and the actual object id of the principal user requester.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `identity.autorization.principals.id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `identity.requester.appId`, `identity.requester.tenantId`,`identity.requester.tokenIssuer` and `identity.requester.audience` raw log fields from `event.idm.read_only_udm.additional.fields` UDM field as it represents the details of the requester.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `identity.requester.appId`, `identity.requester.tenantId`, `identity.requester.tokenIssuer` and `identity.requester.audience` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `properties.objectKey` raw log field from `event.idm.read_only_udm.additional.fields` UDM field as it contains the name of the resource being accessed.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `properties.objectKey` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `properties.requestBodySize` from `event.idm.read_only_udm.additional.fields` UDM field since the value represents the size of the sent bytes.  
\- `event.idm.read_only_udm.network.sent_bytes`: Mapped `properties.requestBodySize` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.additional.fields`: Removed mapping of `properties.responseBodySize` from `event.idm.read_only_udm.additional.fields` UDM field since the value represents the size of the received bytes.  
\- `event.idm.read_only_udm.network.received_bytes`: Mapped `properties.responseBodySize` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.cloud.environment`: Removed mapping of `MICROSOFT_AZURE` from `event.idm.read_only_udm.target.cloud.environment` UDM field since this UDM field is a deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.environment`: Mapped `MICROSOFT_AZURE` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.contentLengthHeader` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource_group`, `storageAccounts`, `subscriptions`, `provider`, `subresource_type`, `subresource_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operationName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field when `Type` raw log field is not present.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `MACHINE` to `event.idm.read_only_udm.extensions.auth.type` UDM field when `identity.type` is `SAS`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `statusCode` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_WRITTEN` when `operationName` consists of the keywords `Put`, `Insert`, `Update`, `Merge`, `Append` or `Set` are present and principal userid details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_DELETION` when `operationName` consists of the keywords `Delete` is present and principal userid details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT` when `operationName` consists of `Lease` or `category` is `StorageWrite` and principal userid details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when `operationName` consists of the keywords `Get`, `List`, `Query` or `Peek` are present and principal user details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when principal and target machine details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when the above conditions are not met.   
2026-05-05 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.resource.name`: Newly mapped `identity.delegatedResource.resourceId` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.product_object_id`: Newly mapped `identity.delegatedResource.objectId` raw log field with `event.idm.read_only_udm.intermediary.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.administrative_domain`: Newly mapped `identity.delegatedResource.tenantId` raw log field with `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `principalData.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_duration`: Newly mapped `durationMs` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `identity.requester.audience`, `properties.metricResponseType`, `properties.lastModifiedTime`, `properties.serverLatencyMs`, `identity.authorization.auth.denyAssignmentId`, `identity.authorization.auth.type`, `identity.authorization.auth.result`, `identity.authorization.auth.reason` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-28 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `properties.primaryIPv4Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.primaryIPv4Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dest_IP` extracted from `properties.conditions.destinationIP` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dest_IP` extracted from `properties.conditions.destinationIP` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dest_port` extracted from `properties.conditions.destinationIP` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `properties.ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `properties.direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `properties.type` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `properties.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `properties.macAddress` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.network.session_duration`: Newly mapped `properties.duration` raw log field with `event.idm.read_only_udm.network.session_duration` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `AccountName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `UserAgentHeader` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `UserAgentHeader` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `TlsVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `systemId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ServerLatencyMs`, `clientRequestId`, `ContentLengthHeader`, `objectKey`, `requestBodySize`, `requestHeaderSize`, `responseBodySize`, `serviceType` , `sourceSystem`, `itemId`, `timeReceived`, `responseHeaderSize`, `aadTenantId`, `aadClientId`, `queryText`, `responseDurationMs`, `statsWorkspaceCount`, `statsRegionCount`, `isBillable` and `NodeType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AuthenticationType`, `AuthenticationHash` and `priority` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TenantId`, `SubscriptionId`, `Internal_WorkspaceResourceId`,`destinationPortRange` and `requestTarget`raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `vnetResourceGuid` raw log field with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `sourcePortRange` and `AssetIdentity` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `resourceId` from `event.idm.read_only_udm.target.resource.id` UDM field since it is a deprecated field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added `MetricResponseType` to the conditional checks for `security_action` and `security_result.summary`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.aadObjectId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `properties.responseCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `properties.workspaceRegion` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.   
2025-06-04 |  \- Added a grok pattern to fetch `inter_host` from `resource_id`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-05-16 |  \- Added `parse_app_protocol.include` file to add support for `event.idm.read_only_udm.network.application_protocol` UDM field-  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.operationCount` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.requestHeaderSize` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.responseHeaderSize` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.requestBodySize` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.responseBodySize` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.smbSessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbTreeConnectID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbPersistentHandleID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbVolatileHandleID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbCreditsConsumed` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbMessageID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbCommandMajor` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.smbCommandDetail` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.smbFileId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `loggingSourceName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `loggingSourceName` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `loggingSourceName` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2024-12-12 |  \- Mapped `identity.tokenHash`, `identity.type`, `identity.requester.appId`, `identity.requester.tenantId`, `identity.requester.tokenIssuer`, `properties.sourceAccessTier`, `principal.type`, `auth.action`, `auth.roleAssignmentId`, and `auth.roleDefinitionId` to `additional.fields`.  
\- Mapped `identity.requester.upn` to `src.user.userid`.  
\- Mapped `identity.requester.objectId` to `src.user.product_object_id`.   
2024-12-06 |  \- Mapped `smbCommandMinor` to `security_result.action_details`.   
2024-07-31 |  \- Initialized `statusText` and `correlationId` to null.   
2024-04-08 |  \- Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
