---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-datapower-changelog/
title: Change log for IBM_DATAPOWER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:54.012497+00:00
---

# Change log for IBM_DATAPOWER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-datapower-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_DATAPOWER

Date | Changes  
---|---  
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `mem`, `http_response`, `request_duration`, `response_duration`, `request_timestamp` , `response_timestamp`, `event_type_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip` log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.url`: Newly mapped `req.5` raw log field with `event.idm.read_only_udm.intermediary.url` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `ver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `req.4` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: When `httpmethod` is `PO`, updated the value of `event.idm.read_only_udm.network.http.method` to `POST`.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `res.4` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `req.2.1` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `req.2.0` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `idg` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `req.1` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `dom` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_Ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `rte` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `req.6` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Added a Grok pattern to parse raw log fields from a SYSLOG+JSON format.  
\- Added a grok pattern on `url` to extract `intermediary_ip`.  
\- The updated grok pattern now allows the fields to parse properly and the following fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.network.application_protocol`  
\- `event.idm.read_only_udm.network.direction`  
\- `event.idm.read_only_udm.network.session_id`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.target.application`  
2026-01-22 |  Enhancement:  
\- Updated the grok pattern to parse `responcecode` from the summary, which impacts the mapping to `event.idm.read_only_udm.network.http.response_code`.  
\- Updated the grok patterns to parse `trans_type` raw log field.  
\- Added the grok pattern to parse `target_url` from the `target_url`, which impacts the mapping to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `transaction_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `errorMessage` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `errorCode`, `errorSuggestion` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-05 |  Enhancement:  
\- Added new grok patterns to support additional log message formats.   
2025-12-25 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_label`, `event_type_id` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `trans_type` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `attributes.chronicle_ingestion_label.agent` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `attributes.chronicle_ingestion_label.ucname` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `attributes.chronicle_namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `attributes.log.record.uid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.parent`: Newly mapped `resource_attributes.cloud.resource_id` raw log field with `event.idm.read_only_udm.principal.cloud.project.parent` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.id`: Newly mapped `resource_attributes.gcp.label.project_id` raw log field with `event.idm.read_only_udm.principal.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.name`: Newly mapped `resource_attributes.gcp.project` raw log field with `event.idm.read_only_udm.principal.cloud.project.name` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.resource_subtype`: Newly mapped `resource_attributes.gcp.resource_type` raw log field with `event.idm.read_only_udm.principal.cloud.project.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_application` field with `event.idm.read_only_udm.target.application` UDM field.   
2025-12-04 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `prin_ip` (from log.source.address) raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `prin_port` (from log.source.address) raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `agent.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `agent.type` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `agent.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `agent.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `agent.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `responcecode` (from summary) raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `prin_user_id` (from summary) raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `useragent` (from summary) raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `useragent` (from summary) raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` (from summary) raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ecs.version`, `fields.fb_bu`, `fields.fb_collector`, `fields.fb_sourcename`, `agent.ephemeral_id`, `sftp_poller`, `mpgw`, `gtid`, `version`, `host.name`, `input.type`, `tags` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If summary contains `logged in` AND has_target is `true`, updated to USER_LOGIN.  
\- event.idm.read_only_udm.metadata.event_type: If summary contains `failed to log in` AND has_target is `true`, updated to USER_LOGIN.  
\- event.idm.read_only_udm.metadata.event_type: If has_target is `true` AND has_principal is `true`, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.event_type: Condition for STATUS_UPDATE changed from specific field checks to if has_principal is `true`.   
2025-06-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp`.   
2024-06-18 |  Enhancement:  
\- Added new Grok patterns to parse the new type of unparsed logs.  
\- Mapped `target_host` to `target.hostname`.  
\- Mapped `prin_ip` to `principal.ip`.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.   
2023-11-09 |  Enhancement:  
\- Added new Grok patterns to parse the new type of unparsed logs.  
\- Added new Grok patterns to parse `summary` from the log.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Changed the mapping of `user_id` from `principal.user.userid` to `target.user.userid`.  
\- For successful login events, `event_type` is mapped to `USER_LOGIN` and `security_result.action` to `ALLOW`.  
\- For failed login events, `event_type` is mapped to `USER_LOGIN` and `security_result.action` to `BLOCK`.   
2023-10-18 |  Enhancement:  
\- Added a Grok pattern to parse the unparsed failed user login logs.  
\- Added a Grok pattern to parse the fields `ip` and `user_id` from the logs.  
\- Mapped `user_id` to `principal.user.userid`.  
\- If a log contains the value `failed to log in` in the description:  
Set `metadata.event_type` to `USER_UNCATEGORIZED`.  
Set `extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.   
2022-12-26 |  Enhancement:  
\- Added GROK pattern to parse the unparsed SYSLOG logs.  
\- If log contains the Logged out and Logged fields, then `metadata.event_type`  
is set to either `USER_LOGOUT` or `USER_LOGIN`.   
2022-06-30 |  Enhancement:  
\- Added a Grok pattern for retrieving `src_ip`.   
2022-06-10 |  Enhancement - The newly ingested SYSLOG format logs have been handled and parsed..  
\- If Log contains any response code value such as 200, 201,203 are mapped to `network.http.response_code`.  
\- If Log contains application protocols such as HTTP, FTP etc, are mapped to `network.application_protocol`.  
\- If Target IP and Principal Hostname are not null then metadata.event_type mapped to `NETWORK_UNCATEGORIZED`.  
\- If Source Ip and Principal Hostname are not null then metadata.event_type mapped to `STATUS_UPDATE`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
