---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-directory-changelog/
title: Change log for PING_DIRECTORY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:42.575784+00:00
---

# Change log for PING_DIRECTORY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-directory-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PING_DIRECTORY

Date | Changes  
---|---  
2026-07-31 |  \- Added grok pattern for new format of SYSLOG+JSON logs.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_host` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `jsonPayload.fromAddress` raw log field with `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `jsonPayload.toAddress` raw log field with `event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `jsonPayload.fromPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `jsonPayload.toPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `jsonPayload.protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `product_name`, `jsonPayload.startupID`, `jsonPayload.product`, `syslog_priority`, `syslog_tag`, `jsonPayload.protocol`, `jsonPayload.clientConnectionPolicy` fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-24 |  \- `event.idm.read_only_udm.security_result.action`: If `jsonPayload.resultCodeName` is `Success`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `jsonPayload.baseDN` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `jsonPayload.connectionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `jsonPayload.instanceName` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `jsonPayload.instanceName` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `jsonPayload.logType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `jsonPayload.requesterIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `jsonPayload.requesterIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.labels.instance_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `resource.labels.project_id` raw log field with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.availability_zone`: Newly mapped `resource.labels.zone` raw log field with `event.idm.read_only_udm.target.cloud.availability_zone` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `jsonPayload.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `jsonPayload.filter` (key: `filter`) raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.requestedAttributes` (key: `requestedAttributes`), `jsonPayload.preAuthorizationUsedPrivileges` (key: `preAuthorizationUsedPrivileges`), `jsonPayload.requestControlOIDs` (key: `requestControlOIDs`), `jsonPayload.usedPrivileges` (key: `jsonPayload_usedPrivileges`), `interServerRequestControls.componentName` (key: `InterServerRequestControlsComponentName`), `interServerRequestControls.operationPurpose` (key: `InterServerRequestControlsOperationPurpose`), `jsonPayload.dereferenceAliases` (key: `jsonPayload_dereferenceAliases`), `jsonPayload.entriesReturned` (key: `entriesReturned`), `jsonPayload.isIndexed` (key: `jsonPayload_isIndexed`), `jsonPayload.messageID` (key: `jsonPayload_messageID`), `jsonPayload.messageType` (key: `jsonPayload_messageType`), `jsonPayload.operationID` (key: `jsonPayload_operationID`), `jsonPayload.processingTimeMillis` (key: `jsonPayload_processingTimeMillis`), `jsonPayload.requestedSizeLimit` (key: `jsonPayload_requestedSizeLimit`), `jsonPayload.requestedTimeLimitSeconds` (key: `jsonPayload_requestedTimeLimitSeconds`), `jsonPayload.scope` (key: `jsonPayload_scope`), `jsonPayload.scopeName` (key: `jsonPayload_scopeName`), `jsonPayload.threadID` (key: `jsonPayload_threadID`), `jsonPayload.typesOnly` (key: `jsonPayload_typesOnly`), `jsonPayload.uncachedDataAccessed` (key: `jsonPayload_uncachedDataAccessed`), `jsonPayload.usingAdminSessionWorkerThread` (key: `jsonPayload_usingAdminSessionWorkerThread`), `jsonPayload.workQueueWaitTimeMillis` (key: `jsonPayload_workQueueWaitTimeMillis`), `jsonPayload.resultCode` (key: `jsonPayload_resultCode`), `logName` (key: `logName`), `labels.agent.googleapis.com/log_file_path` (key: `labels_agent_googleapis_com_log_file_path`), `labels.compute.googleapis.com/resource_name` (key: `labels_compute_googleapis_com_resource_name`), `jsonPayload.operationType` (key: `jsonPayload_operationType`), `jsonPayload.requesterDN` (key: `jsonPayload_requesterDN`), `receiveTimestamp` (key: `receiveTimestamp`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-31 |  \- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `prin_host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field as the host running the directory server `prin_host` is the target of requests coming from client `requesterIP`.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Mapped `prin_host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field as the host running the directory server `prin_host` is the target of requests coming from client `requesterIP`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `prod_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- The grok pattern for message was updated to extract `prod_event_type` and handle variations in key-value data starting with either `requesterIP=` or `product=.`.   
2025-03-05 |  \- Mapped `product_event` to `metadata.product_event_type`.  
\- Mapped `administrativeOperation` to `metadata.description`.  
\- Mapped `fromAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `toAddress` to `target.ip` and `target.asset.ip`.  
\- Added support to parse new types of logs.   
2024-11-19 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
