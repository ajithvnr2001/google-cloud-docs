---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-identity-cloud-changelog/
title: Change log for FORGEROCK_IDENTITY_CLOUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:59:06.484760+00:00
---

# Change log for FORGEROCK_IDENTITY_CLOUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-identity-cloud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORGEROCK_IDENTITY_CLOUD

Date | Changes  
---|---  
2026-03-30 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source_cloud`, `type`, `entry_info_nodeExtraLogging_auditInfo_Timestamp`, `entry_info_nodeOutcome`, `entry_info_authLevel` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `entry_info_nodeExtraLogging_auditInfo_clientId` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `entry_info_nodeExtraLogging_auditInfo_EventName`, `entry_info_nodeExtraLogging_auditInfo_FlowType`, `entry_info_displayName`, `entry_info_nodeType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `entry_info_nodeExtraLogging_auditInfo_Status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `entry_info_nodeExtraLogging_auditInfo_TransactionId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `entry_info_nodeId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `entry_info_treeName` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `tenant_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `USER_LOGIN` to `event.idm.read_only_udm.metadata.event_type` to when `payload.eventName` is `AM-NODE-LOGIN-COMPLETED` and contains principal data.  
\- The updated raw log now allows the fields to parse properly and the following fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.resource.attribute.labels`  
\- `event.idm.read_only_udm.target.resource.name`  
2025-08-06 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `payload.realm` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `payload.source` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `payload.level` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `payload.timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-22 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `payload.client.ip` and `payload.http.request.headers.x-forwarded-for` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `payload.client.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.http.request.method`: Newly mapped `payload.http.request.method` raw log field with `event.idm.read_only_udm.network.http.request.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `payload.http.request.path` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.topic`, `payload.http.request.headers.accept-api-version`, `payload.http.request.secure`, `payload.request.detail`, `payload.response`, `payload.request`, `payload.trackingIds`, `payload.objectId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `payload.http.request.headers.user-agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `payload.http.request.headers.host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `payload.http.request.headers.x-forwarded-proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `payload.response.statusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `payload.operation` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when `has_network_http` is `true` and `has_principal` is `true`.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_principal_user` is `true`.   
2024-03-11 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
