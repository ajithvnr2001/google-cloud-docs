---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-event-export-changelog/
title: Change log for SYMANTEC_EVENT_EXPORT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:11.740668+00:00
---

# Change log for SYMANTEC_EVENT_EXPORT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-event-export-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_EVENT_EXPORT

Date | Changes  
---|---  
2026-09-28 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: Removed `BLOCK` mapping for `security_result.action` when `type_id` is `8020`, `1000`, `20`, `2` and `id` is `1` as none of the raw logs with these `type_id` and `id` values record security violations, threats, or failed events.  
\- `event.idm.read_only_udm.security_result.action`: Updated conditional logic to map `id` to `ALLOW` when `type_id` is `8001` or `8078` or `8000` or `8002` or `8003` or `8004` or `8005` or `8006` or `8007` or `8009` or `8016` or `8071` and `id` is `1`, `BLOCK` when `type_id` is `8001` or `8078` or `8000` or `8002` or `8003` or `8004` or `8005` or `8006` or `8007` or `8009` or `8016` or `8071` and `id` is `2`, and scoped `BLOCK` mapping when `type_id` is `8031` or `8040` or `8025` or `8027` or `8032` or `8033` or `8038` and `id` is `1` or `11`.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `customer_uid` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor.user.uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `actor.uid` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `platform_data.sep_hw_uid` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `process.user.uid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `process.uid` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `process.file.path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.size`: Newly mapped `process.file.size` raw log field with `event.idm.read_only_udm.target.process.file.size` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `process.file.sha2` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.platform_version`: Newly mapped `device_os_ver` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `policy.version` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `edr_enriched_data.category_id`, `edr_enriched_data.category_name`, `edr_enriched_data.rule_name`, `edr_enriched_data.rule_id`, `actor.session.is_admin`, `process.session.is_admin` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `org_unit_uid`, `device_group_name`, `actor.file.uid`, `trans_event_raw_length`, `process.file.signature_level_id`, `actor.file.signature_level_id`, `timezone`, `process.pid`, `actor.file.xattributes.sip`, `process.file.xattributes.sip`, `actor.file.xattributes.quarantine`, `process.file.xattributes.quarantine`, `seq_num`, `actor.start_time`, `process.start_time`, `actor.file.created`, `actor.file.modified`, `process.file.created`, `process.file.modified` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-06 |  Enhancement:  
\- Mapped first occurrence of ipv4 or ipv6 from `device_networks` to `intermediary.ip` and all the rest to `principal.asset.ip`.   
2025-02-24 |  Enhancement:  
\- Mapped first IP from `device_networks` to `intermediary.ip` and the rest to `principal.asset.ip`.   
2025-02-11 |  Enhancement:  
\- Mapped first IP from `device_networks` to `principal.asset.ip`.   
2025-01-16 |  Enhancement:  
\- If `id` is in [`1`, `11`], then mapped `security_result.action` to `BLOCK`. Otherwise, if `id` is in [`2`, `3`, `4`, `8`, `13`, `14`, `16`], then mapped `security_result.action` to `ALLOW`. Otherwise, if `id` is in [`5`, `6`, `7`, `15`], then mapped `security_result.action` to `ALLOW_WITH_MODIFICATION`. Otherwise, if `id` is `12`, then mapped `security_result.action` to `QUARANTINE`. Otherwise, if `id` is `0`, then mapped `security_result.action` to `UNKNOWN_ACTION`.   
2024-12-04 |  Enhancement:  
\- Mapped `cybox.path` to `target.file.full_path`.  
\- Mapped `cybox.size` to `target.file.size`.  
\- If `id` is `1` then mapped `security_result.action` to `BLOCK` else if `id` is `2` then mapped `security_result.action` to `ALLOW` else if `id` is in `[`3`,`4`,`5`,`6`,`7`]` then mapped `security_result.action` to `ALLOW_WITH_MODIFICATION` else if `id` is `12` then mapped `security_result.action` to `QUARANTINE`.  
\- Mapped `audit` to `additional.fields`.  
\- If `policy.rulename` has `File and Folder Access Attempts` then mapped `file.name` to `principal.file.names`.  
\- If `device_os_type_id` is `100` then mapped `principal.platform` to `WINDOWS`.  
\- If `device_os_type_id` is `200` then mapped `principal.platform` to `LINUX`.  
\- If `device_os_type_id` is `300` then mapped value `SOLARIS` to `additional.fields` .  
\- If `device_os_type_id` is `301` then mapped value `AIX` to `additional.fields`.  
\- If `device_os_type_id` is `302` then mapped value `HP-UX` to `additional.fields`.  
\- If `device_os_type_id` is `400` then mapped value `MACINTOSH` to `additional.fields`.  
\- If `device_os_type_id` is `500` then mapped `principal.platform` to `IOS`.  
\- If `device_os_type_id` is `501` then mapped `principal.platform` to `ANDROID`.  
\- If `device_os_type_id` is `502` then mapped value `WINDOWS MOBILE` to `additional.fields`.  
\- If `device_os_type_id` is `503` then mapped value `IPADOS` to `additional.fields`.  
\- If `device_os_type_id` is `1001` then mapped value `OTHER` to `additional.fields`.  
\- If `device_os_type_id` is `0` then mapped `principal.platform` to `UNKNOWN`.  
\- Modified the mapping of `product_uid` from `metadata.product_log_id` to `target.process.pid`.  
\- Modified the mapping of `process_id` from `target.process.pid` to `_metadata.product_log_id`.   
2024-11-21 |  Enhancement:  
\- Modified mappings of `severity_id`.   
2024-10-25 |  Enhancement:  
\- Mapped `connection.url.port` to `target.port`.  
\- Mapped `connection.url.host` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `connection.url.domain_name` to `target.administrative_domain`.  
\- Mapped `connection.url.text` to `target.url`.  
\- Mapped `connection.src_name` to `target.application`.  
\- Mapped `parent.file.md5` to `principal.process.parent_process.file.md5`.  
\- Mapped `parent.file.sha1` to `principal.process.parent_process.file.sha1`.  
\- Mapped `parent.file.sha256` to `principal.process.parent_process.file.sha256`.  
\- Mapped `parent.file.folder` to `principal.process.parent_process.file.full_path`.  
\- Mapped `parent.file.product_name`, `parent.file.company_name`, `parent.file.created`, `parent.file.normalized_path`, `parent.file.signature_company_name`, `parent.file.signature_value`, and `parent.file.xattributes.portal` to `principal.resource.attribute.labels`.  
\- Mapped `parent.file.signature_value_ids` to `additional.fields`.  
\- Mapped `parent.file.version` to `network.tls.version`.  
\- Mapped `parent.file.signature_issuer` to `network.tls.server.certificate.issuer`.   
2023-11-07 |  Enhancement:  
\- Added support for SYSLOG format logs.  
\- Added `not null` checks to `parent.cmd_line`, `parent.pid`, `actor.pid`, `actor.cmd_line`, `device_name`, `device_group`, `device_os_name`, `device_group`, `device_domain`, `device_uid` prior mapping to UDM.  
\- Mapped `device_name` to `principal.hostname`.  
\- Mapped `user_name` to `principal.user.user_display_name`.  
\- Mapped `actor.user.name` to `principal.user.user_display_name`.  
\- Mapped `actor.user.domain` to `principal.administrative_domain`.  
\- Mapped `actor.user.sid` to `principal.user.windows_sid`.  
\- Mapped `actor.file.size` to `principal.process.file.size`.  
\- Mapped `device_public_ip` to `principal.ip`.  
\- Mapped `device_networks.ipv6` to `intermediary.ip`.  
\- Mapped `user_email` to `principal.user.email_addresses`.   
2022-08-19 |  Enhancement - Reduced Generic Event percentage.  
\- Mapped `type_id` to event.idm.read_only_udm.metadata.event_type  
\- Parsed logs for type_id = 21   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
