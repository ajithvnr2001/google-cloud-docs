---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-smartdefense-changelog/
title: Change log for CHECKPOINT_SMARTDEFENSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:57.638676+00:00
---

# Change log for CHECKPOINT_SMARTDEFENSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-smartdefense-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHECKPOINT_SMARTDEFENSE

Date | Changes  
---|---  
2026-04-01 |  \- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `ifdir` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when principal and target data is present, `STATUS_UPDATE` when only principal data is present, and `GENERIC_EVENT` otherwise.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `vendor_name` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip`, `origin` log fields with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_hostname` log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `principal_pid` log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `smartdefense_profile`, `layer_uuid`, `layer_name`, `precise_error`, `suppressed_logs`, `flags`, `originsicname`, `sequencenum`, `time`, `version`, `description_url`, `log_id`, `performance_impact`, `reject_id_kid`, `received_bytes`, `sent_bytes`, `ser_agent_kid`, `packet_info`, `ProductFamily`, `malware_rule_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `tags`, `policy_name`, `__policy_id_tag.product`, `db_tag`, `mgmt`, `date`, `ifname`, `policy`, `policy_time`, `protection_id`, `protection_type`, `rule`, `sub_policy_name`, `sub_policy_uid` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `loguid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `attack` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `attack_info`, `Attack Info` raw log fields with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.last_updated_time`: Newly mapped `lastupdatetime` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `protection_name`, `reason` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `proxy_src_ip` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `received_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `resource` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `rule_uid`, `reject_id` raw log fields with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `s_port`, `sport_svc` raw log fields with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `service`, `svc` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `service_id` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `web_client_type` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `web_client_type` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- Added a Grok pattern to parse the new format SYSLOG + KV logs. Due to this change, the following fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.security_result.confidence_details`  
2024-07-02 |  Created a new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
