---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-run-changelog/
title: Change log for GCP_RUN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:15:03.215883+00:00
---

# Change log for GCP_RUN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-run-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_RUN

Date | Changes  
---|---  
2026-08-14 |  Enhancement -  
\- Added support for new format of JSON logs.  
\- Added a Grok pattern to parse the raw log fields  
\- `event.idm.read_only_udm.target.url`: Newly mapped `event_data.subject` raw log field with `event.idm.read_only_udm.target.url` UDM field  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `event_data.data.resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field  
\- `security_result.summary`: Newly mapped `eventType` raw log field with `security_result.summary` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_data.data.protoPayload.methodName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_data.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_data.data.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `event_data.data.protoPayload.resourceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field  
\- `event.idm.read_only_udm.target.application`: Newly mapped `event_data.data.protoPayload.serviceName` raw log field with `event.idm.read_only_udm.target.application` UDM field  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `event_data.source` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `event_data.specversion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `event_data.time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `event_data.data.logName` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `event_data.data.protoPayload.authenticationInfo.principalEmail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field  
\- `security_result.description`: Newly mapped `event_data.data.protoPayload.metadata.tableDeletion.reason` raw log field with `security_result.description` UDM field  
\- `event.idm.read_only_udm.principal.ip`/`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `event_data.data.protoPayload.requestMetadata.callerIp` raw log field with `event.idm.read_only_udm.principal.ip`/`event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `event_data.data.protoPayload.requestMetadata.callerSuppliedUserAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `event_data.data.protoPayload.requestMetadata.callerSuppliedUserAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_data.datacontenttype`, `event_data.dataschema`, `event_data.data.insertId`, `event_data.data.type`, `event_data.data.protoPayload.metadata.type`, `event_data.data.resource.labels.dataset_id`, `event_data.data.resource.labels.project_id`, `event_data.data.protoPayload.authorizationInfo.0.granted`, `event_data.data.protoPayload.authorizationInfo.0.permission` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_DELETION` when `event_data.data.protoPayload.methodName` is `DeleteTable` and user data is present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to 'USER_UNCATEGORIZED` when user data is present.  
\- Else, set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2024-01-22 |  Enhancement -  
\- Added mapping for logs where logName is `projects/1234/logs/run.googleapis.com%2Fstderr`, `projects/1234/logs/run.googleapis.com%2Fstdout`, `projects/1234/logs/run.googleapis.com%2Frequests` and `projects/1234/logs/run.googleapis.com%2Fvarlog%2Fsystem`.  
\- Mapped `httpRequest.latency` to `target.resource.attribute.labels`.  
\- Mapped `resource.labels.configuration_name` to `target.resource.attribute.labels`.  
\- Mapped `resource.labels.revision_name` to `target.resource.attribute.labels`.  
\- Mapped `resource.labels.service_name` to `target.resource.attribute.labels`.  
\- Mapped `httpRequest.protocol` to `network.application_protocol`.  
\- Mapped `httpRequest.requestMethod` to `network.http.method`.  
\- Mapped `httpRequest.requestSize` to `network.sent_bytes`.  
\- Mapped `httpRequest.requestUrl` to `target.url`.  
\- Mapped `httpRequest.responseSize` to `network.received_bytes`.  
\- Mapped `httpRequest.remoteIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `httpRequest.serverIp` to target.ip` and `target.asset.ip".  
\- Mapped `httpRequest.status` to `network.http.response_code`.  
\- Mapped `httpRequest.userAgent` to `network.http.user_agent`.  
\- Mapped `logName` to `metadata.product_event_type`.  
\- Mapped `textPayload` to `additional.fields`.  
\- Mapped `labels.run.googleapis.com_execution_name` to `additional.fields`.  
\- Mapped `labels.run.googleapis.com_task_attempt` to `additional.fields`.  
\- Mapped `labels.run.googleapis.com_task_index` to `additional.fields`.  
\- Mapped `labels.instanceId` to `additional.fields`.  
\- Mapped `resource.labels.job_name` to `additional.fields`.   
2023-04-13 |  Enhancement -  
\- Set `target.resource.attribute.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.  
\- Set `target.resource.name` to the full resource name value.   
2022-07-13 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
