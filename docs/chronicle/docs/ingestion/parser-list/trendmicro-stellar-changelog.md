---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-stellar-changelog/
title: Change log for TRENDMICRO_STELLAR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:45:49.263870+00:00
---

# Change log for TRENDMICRO_STELLAR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-stellar-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_STELLAR

Date | Changes  
---|---  
2026-03-02 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `reason` (key: reason) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified a grok pattern to parse the `eventTime` raw log field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Modified date filter to support an additional timestamp format.   
2025-12-03 |  Enhancement:  
\- Added grok pattern to extract the integer value from `programSize` and handle potential trailing characters.  
\- Replaced carriage return and newline characters with spaces in the raw message.  
\- Removed spaces from the `serverIP` field.  
\- Refactored the assignment of `metadata.event_type` to use an intermediate variable, defaulting to `GENERIC_EVENT` if no other type is set.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `violatedPolicy` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `violatedPolicy` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alLastUpdateAt` raw log field to `event.idm.read_only_udm.additional.fields`.   
2025-10-01 |  Enhancement:  
\- Added grok patterns in order to parse the logs with variation.  
\- Corrected the over written values for `event.idm.read_only_udm.metadata.product_name` and `event.idm.read_only_udm.metadata.vendor_name` UDM fields.  
\- event.idm.read_only_udm.security_result.threat_id: Newly Mapped `threatAttackID` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `frameworkName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly Mapped `fileSize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `fileVersion` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `fileCreateTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `fileModificationTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `file_product` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `file_vendor` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly Mapped `lastModifierPath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `agentGrpPath` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `agentGrpName` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `agentRt` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly Mapped `agentGrpGuid` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly Mapped `legacyAgentSeverity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `agentIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `agentIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `rebootRequired` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly Mapped `threatName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly Mapped `fileName` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.   
2025-04-16 |  Enhancement:  
\- Added grok patterns in order to parse the logs with variation.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Updated `has_user` to `true` when `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.user` is present.   
2025-02-12 |  Enhancement:  
\- Added support to parse the unparsed logs.   
2025-01-23 |  Enhancement:  
Added a Grok pattern to parse the logs.  
\- Mapped `eventTime` to `metadata.event_timestamp`.  
\- Mapped `start` to `metadata.event_timestamp`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `event_id` to `metadata.product_log_id`.  
\- Mapped `security_result.action` for `event_id` in [`5888`,`8193`,`5377`,`8194`].  
\- Mapped `event_name` to `metadata.product_event_type`.  
\- Mapped `serverIP` to `intermediary.hostname`.  
\- Changed `metadata.event_type` for `event_id` in [`5888`,`4609`,`523`,`8197`,`8214`,`8209`,`8211`]   
2024-12-05 |  Enhancement:  
\- Mapped `sourceIP` to `principal.ip`and `principal.asset.ip`.  
\- Mapped `fileHashAllowed` to `target.file.sha256`.  
\- Mapped `programHash` to `target.file.sha256`.  
\- Mapped `certificate` to `network.tls.client.certificate.issuer`.  
\- Mapped `programSize` to `principal.process.file.size`.  
\- Mapped `programPath` to `principal.process.file.full_path`.  
\- Mapped `domain` to `principal.administrative_domain`  
2024-11-21 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
