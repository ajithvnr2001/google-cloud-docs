---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-defend-changelog/
title: Change log for ELASTIC_DEFEND \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:10:05.670092+00:00
---

# Change log for ELASTIC_DEFEND  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-defend-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ELASTIC_DEFEND

Date | Changes  
---|---  
2026-03-02 |  \- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `_source.host.hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `_source.process.pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `_source.process.command_line` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `_source.process.name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `_source.process.parent.executable` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `_source.process.Ext.token.integrity_level_name`, `_source.process.Ext.code_signature`, `_source.process.Ext.ancestry`, `_source.process.Ext.protection`, `_source.process.Ext.authentication_id` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_source.winlog.event_data.PrivilegeList` with label `Privilege List`, `_source.event.ingested` with label `Ingested`, `_source.event.provider` with label `Provider` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `_source.user.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `_source.event.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `_source.host.domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `_source.event.sequence` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true` and `has_target_user` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- `event.idm.read_only_udm.extensions.auth.type`: If `has_principal` is `true` and `has_target_user` is `true`, then set `event.idm.read_only_udm.extensions.auth.type` to `MACHINE`.   
2025-08-08 |  \- `event.idm.read_only_udm.security_result.description`: Newly mapped `_source.kibana.alert.rule.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `_source.kibana.alert.rule.rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `_source.kibana.alert.rule.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `_source.kibana.alert.rule.parameters.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `_source.kibana.alert.rule.parameters.threat.tactic.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `_source.kibana.alert.rule.parameters.threat.technique.techniques.id` raw log field with`event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.   
2025-07-31 |  \- We added regex pattern for `_source.user.id` UDM field to map `principal.user.windows_sid`.  
-`event.idm.read_only_udm.target.process.command_line`: Removed mapping of `_source.process.name` from `target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `_source.process.command_line` raw log field with `target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `_source.process.name` raw log field with `target.process.file.names` UDM field.   
2025-06-03 |  \- `event.idm.read_only_udm.target.file.sha256` : Removed mapping of `_source.file.Ext.malware_signature.primary.signature.hash.sha256` raw log field from `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- Updated label name from `all_names` to `malware_signature_all_names` in `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-05-15 |  \- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `_source.group.name` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Removed mapping of `_source.process.name` raw log field from `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Mapped `_source.process.name` raw log field to `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Removed mapping of `_source.process.executable` raw log field from `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `_source.user.name` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Removed mapping of `source.process.parent.executable` raw log field from `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Mapped `source.process.parent.executable` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.ruleset`: Newly mapped `_source.rule.rule_set` raw log field to `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_source.group.id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name': Newly mapped `_source.rule.name` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_set': Newly mapped `_source.rule.ruleset` raw log field to `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id': Newly mapped `_source.rule.id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name': Newly mapped `_source.file.Ext.malware_signature.primary.signature.name` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id': Newly mapped `_source.file.Ext.malware_signature.primary.signature.id` raw log field to `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256': Newly mapped `_source.file.Ext.malware_signature.primary.signature.hash.sha256` raw log field to `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields': Newly mapped `_source.file.Ext.malware_signature.all_names` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields': Newly mapped `_source.file.Ext.malware_signature.identifier` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields': Newly mapped `_source.user.id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid': Newly mapped `_source.process.entity_id` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid': Newly mapped `_source.process.pid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.   
2025-03-04 |  \- Newly Parser Created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
