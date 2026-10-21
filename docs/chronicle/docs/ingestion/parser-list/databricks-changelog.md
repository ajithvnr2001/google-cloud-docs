---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/databricks-changelog/
title: Change log for DATABRICKS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:39:57.600213+00:00
---

# Change log for DATABRICKS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/databricks-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DATABRICKS

Date | Changes  
---|---  
2026-03-17 |  Newly created parser:  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_time`,`time`,`timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resourceId` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `operationVersion`, `version`, `jsonPayload.version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id`, `properties.logId`, `insertId` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `properties.sourceIPAddress`, `sourceIPAddress`, `jsonPayload.sourceIPAddress`,`source_ip_address` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_identity.email`, `identity.email`, `userIdentity.email`, `jsonPayload.userIdentity.email` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_identity.email`, `identity.email`, `userIdentity.email`, `jsonPayload.userIdentity.email`, `grantor` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action_name`,`properties.actionName`, `actionName`, `jsonPayload.actionName` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `service_name`, `properties.serviceName`, `serviceName`, `jsonPayload.serviceName` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response_code`, `response.status_code`, `p_response.statusCode`, `response.statusCode`, `jsonPayload.response.statusCode` raw log field(s) with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `properties.userAgent`, `userAgent`, `jsonPayload.userAgent` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `properties.sessionId`, `sessionId` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Host` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource.labels.function_name`, `object_name` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `resource.labels.region` raw log field(s) with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource.type`, `object_type` raw log field(s) with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `privilege_type` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `p_response.errorMessage` raw log field(s) with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `grantee` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `request_params.path` raw log field(s) with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped key-value pairs from `request_params`, `jsonPayload.request_params`, `identity_metadata` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped key-value pairs from `resource.labels` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `account_id`, `workspace_id`, `category`, `workspaceId`, `accountId`, `jsonPayload_accountId`, `jsonPayload_workspaceId`, `catalog_name`, `schema_name` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `response.result`, `audit_level`, `auditLevel`, `request_params.authenticationMethod`, `jsonPayload.auditLevel`, `jsonPayload.request_params.authenticationMethod` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `user_identity.subject_name`, `identity.subjectName` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_date`, `request_id`, `operationName`, `properties.requestId`, `requestId`, `jsonPayload.logName`, `jsonPayload.requestId`, `jsonPayload.timestamp`, `logName` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `DATABRICKS` raw log field(s) with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `DATABRICKS` raw log field(s) with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: The event_type is updated to `USER_RESOURCE_ACCESS`, `FILE_READ`, `FILE_MODIFICATION`, `USER_RESOURCE_CREATION`, `USER_RESOURCE_UPDATE_PERMISSIONS`, `USER_UNCATEGORIZED`, or `STATUS_UPDATE` based on the presence of necessary principal and target data, defaulting to GENERIC_EVENT if those details are missing.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
