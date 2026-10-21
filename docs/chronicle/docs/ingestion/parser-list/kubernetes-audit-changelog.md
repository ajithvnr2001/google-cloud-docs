---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-changelog/
title: Change log for KUBERNETES_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:08:30.435932+00:00
---

# Change log for KUBERNETES_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KUBERNETES_AUDIT

Date | Changes  
---|---  
2026-03-30 |  Enhancement:  
\- Added support for KV and Grok format for logs where the message field is not a JSON object.  
\- `event.idm.read_only_udm.metadata.product_log_id`:Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`:Newly mapped `time`,`line_number` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`:Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname: Newly mapped `stsendpoint`,`target_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `prin_application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `arn`, `accountid`, `accesskeyid` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`:Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.user.group_identifiers`: Newly mapped `groups` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `userid`, `uid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `username` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `path` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: If `path` contains authenticate and target user details are present, updated the value of `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`, when path contains `authenticate` and target user details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`, when target device details are present and principal device details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`, when principal device details are present.  
\- `event.idm.read_only_udm.metadata.event_type`:Newly set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`, when principal machine data, target machine data and user details are absent.   
2025-02-19 |  Enhancement:  
\- Added support for a new format of JSON logs.   
2025-01-24 |  Enhancement:  
\- Added `on_error` when mapping `annotations.authorization.k8s.io/reason` to `security_result.description`.  
\- Mapped `objectRef.name` to `additional.fields`.  
\- Mapped `objectRef.namespace` to `additional.fields`.  
\- Mapped `objectRef.resource` to `additional.fields`.  
\- Mapped `objectRef.apiVersion` to `additional.fields`.  
\- Mapped `responseObject.metadata.annotations.volume.kubernetes.io/selected-node` to `additional.fields`.  
\- Mapped `responseObject.metadata.annotations.volume.kubernetes.io/storage-provisioner` to `additional.fields`.  
\- Mapped `responseObject.metadata.annotations.control-plane.alpha.kubernetes.io/leader` to `additional.fields`.  
\- Mapped `holderIdentity` to `additional.fields`.  
\- Mapped `leaseDurationSeconds` to `additional.fields`.  
\- Mapped `acquireTime` to `additional.fields`.  
\- Mapped `renewTime` to `additional.fields`.  
\- Mapped `leaderTransitions` to `additional.fields`.  
\- Mapped `labels.os.type` to `_principal.platform`.  
\- Mapped `responseObject.metadata.managedFields` to `additional.fields`.  
\- Mapped `responseObject.status.images` to `additional.fields`.   
2024-12-03 |  Enhancement:  
\- Added support to parse new format of JSON logs.   
2023-08-21 |  Enhancement:  
\- Parsed new format JSON logs.  
\- Based on `verb`, identified the specific `event_types`.  
\- Mapped following additional fields :  
\- `kind` to `metadata.product_event_type`.  
\- `apiVersion` to `metadata.product_version`.  
\- `auditID` to `metadata.product_log_id`.  
\- `stage` to `metadata.description`.  
\- `requestURI` to `target.url`.  
\- `userAgent` to `network.http.user_agent`.  
\- `verb` to `network.http.method`.  
\- `responseStatus.code` to `network.http.response_code`.  
\- `user.username` to `principal.user.user_display_name`.  
\- `user.uid` to `principal.user.userid`.  
\- `user.groups` to `principal.user.group_identifiers`.  
\- `sourceIPs` to `principal.ip`.  
\- `objectRef.resource` to `target.resource.resource_subtyp`.  
\- `annotations.authorization.k8s.io/decision` to `security_result.action`.  
\- `annotations.authorization.k8s.io/reason` to `security_result.description`.  
\- `stageTimestamp` to `metadata.collected_timestamp`.   
2022-07-14 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
