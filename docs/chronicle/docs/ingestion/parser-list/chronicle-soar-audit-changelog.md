---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chronicle-soar-audit-changelog/
title: Change log for CHRONICLE_SOAR_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:54:31.850623+00:00
---

# Change log for CHRONICLE_SOAR_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chronicle-soar-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHRONICLE_SOAR_AUDIT

Date | Changes  
---|---  
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the conditional logic to set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` only when there are user details and resource details in the raw log.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.type`, `jsonPayload.endTime`, `jsonPayload.startTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `jsonPayload.connection.clientIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `jsonPayload.connection.clientPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `jsonPayload.connection.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `jsonPayload.connection.serverPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `jsonPayload.connection.serverIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` only when principal and target have machine details.   
2026-03-05 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `insertId` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `textPayload` raw log field(s) with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity_details` UDM field if `severity` is not enumerated value.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `receiveTimestamp` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `resource.type` raw log field(s) with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `labels.action_name` raw log field(s) with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `labels.instance_name` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `resource.labels.container_name` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.namespace: Newly mapped `resource.labels.namespace_name` raw log field(s) with `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `resource.labels.location` raw log field(s) with `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.labels` raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field when key not in `container_name`, `namespace_name` and `location`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field when key not in `action_name` and `instance_name`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `logName` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: The conditional logic to set event_type to `USER_RESOURCE_ACCESS` and `STATUS_UNCATEGORIZED` is updated.   
2025-05-29 |  \- event.idm.read_only_udm.target.user.userid: Removed mapping of `user` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ContactEmails` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ContactName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ContactPhone` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2023-10-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
