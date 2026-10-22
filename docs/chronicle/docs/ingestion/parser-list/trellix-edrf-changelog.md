---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-edrf-changelog/
title: Change log for TRELLIX_EDRF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:32.940521+00:00
---

# Change log for TRELLIX_EDRF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-edrf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRELLIX_EDRF

Date | Changes  
---|---  
2026-05-21 |  \- Added support for JSON format.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `item.systemUniqueID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `item.maGuid` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `item.host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `item.hxId`, `item.hxUrl`, `item.parentTraceId`, `item.contextTraceId`, `item.it`, `item.integrity`, `item.procFileAttrs.lastModificationDate`, `item.procFileAttrs.creationDate`, `item.procFileAttrs.fileType`, `item.procFileAttrs.fsattrs`, `item.procFileAttrs.embedFileVersion`, `item.procFileAttrs.embedProductName`, `item.procFileAttrs.embedProductVersion`, `item.procFileAttrs.embedVendorName`, `item.procFileAttrs.subsystem`, `item.network.accessType`, and `item.parentsTraceId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `item.rv` raw log field with `event.idm.read_only_udm.metadata.product_version UDM field`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `item.traceId` raw log field with `event.idm.read_only_udm.metadata.product_log_id UDM field`.  
\- `event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `item.time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp UDM field`.  
\- `event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `item.pSha2` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `item.pFullName` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line: Newly mapped `item.cmdLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names: Newly mapped `item.processName`, `item.procFileAttrs.name`, and `item.procFileAttrs.embedFilename` raw log fields with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain: Newly mapped `item.user.domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.user.userid: Newly mapped `item.user.name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid: Newly mapped `item.user.id` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.md5: Newly mapped `item.procFileAttrs.md5` raw log field with `event.idm.read_only_udm.target.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha1: Newly mapped `item.procFileAttrs.sha1` raw log field with `event.idm.read_only_udm.target.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256: Newly mapped `item.procFileAttrs.sha256` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.process.file.size: Newly mapped `item.procFileAttrs.size` raw log field with `event.idm.read_only_udm.target.process.file.size` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path: Newly mapped `item.procFileAttrs.path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields: Newly mapped `item.procFileAttrs.reputation.reputation`, `item.procFileAttrs.reputation.productId`, `item.procFileAttrs.reputation.vtpPrivileges`, and `item.tdmRuleIds` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cert.type`, `cert.issuerName`, `cert.publicKeyHash`, `cert.subject`, `cert.validNotAfter`, `cert.sha1`, `cert.validNotBefore`, and `dnsName` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Newly mapped `item.registry.regKeyName` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `item.network.direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `item.network.dstIp` raw log field with `event.idm.read_only_udm.target.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `item.network.srcIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `item.network.dstPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `item.network.srcPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `item.network.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `item.uniqueRuleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions: Newly mapped `item.dns.name`, `item.dns.type`, and `item.dns.class` raw log fields with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: If eventType is `Process Created`, updated the value of `event.idm.read_only_udm.target.process.pid`.  
\- `event.idm.read_only_udm.principal.process.pid`: If eventType is `NOT Process Created`, updated the value of `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.principal.process.pid`: If eventType is `Process Created`, updated the value of `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: If eventType is NOT `Process Created`, updated the value of `event.idm.read_only_udm.principal.process.parent_process.pid`.  
\- `event.idm.read_only_udm.network.application_protocol`: If `item.network.protocol` is HTTPS, updated the value of `event.idm.read_only_udm.network.application_protocol` to HTTPS`.  
\- `event.idm.read_only_udm.network.ip_protocol`: If `item.network.protocol` is HTTPS, updated the value of `event.idm.read_only_udm.network.ip_protocol` to TCP`.  
\- `event.idm.read_only_udm.network.application_protocol: If `item.network.protocol` is HTTP, updated the value of event.idm.read_only_udm.network.application_protocol` to HTTP`.  
\- `event.idm.read_only_udm.network.ip_protocol`: If `item.network.protocol` is HTTP, updated the value of `event.idm.read_only_udm.network.ip_protocol` to TCP`.  
\- `event.idm.read_only_udm.metadata.event_type`: If eventType is DNS Query, updated the value of `event.idm.read_only_udm.metadata.event_type` to NETWORK_DNS.  
\- `event.idm.read_only_udm.network.application_protocol`: If eventType is DNS Query, updated the value of `event.idm.read_only_udm.network.application_protocol` to DNS.  
\- `event.idm.read_only_udm.metadata.event_type`: If eventType is Network Accessed and target IP is not empty and not `0`, updated the value of `event.idm.read_only_udm.metadata.event_type` to NETWORK_CONNECTION.  
\- `event.idm.read_only_udm.metadata.event_type`: If eventType is Process Created, updated the value of `event.idm.read_only_udm.metadata.event_type` to PROCESS_OPEN.  
\- `event.idm.read_only_udm.metadata.event_type`: If eventType is RegKey Read, updated the value of `event.idm.read_only_udm.metadata.event_type` to REGISTRY_UNCATEGORIZED.  
\- `event.idm.read_only_udm.metadata.event_type`: If eventType is not DNS Query, Network Accessed, Process Created, or RegKey Read and host_value is present, updated the value of `event.idm.read_only_udm.metadata.event_type` to STATUS_UPDATE.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to GENERIC_EVENT.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
