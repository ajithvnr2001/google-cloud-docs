---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extrahop-changelog/
title: Change log for EXTRAHOP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:10.937795+00:00
---

# Change log for EXTRAHOP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extrahop-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for EXTRAHOP

Date | Changes  
---|---  
2025-12-26 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `tar_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `extrahop_detail` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional check for message not containing `events` and used gsub to remove extra backslashes and quotes from the `KV` field.  
\- Added new grok patterns to parse new format of logs.   
2025-07-24 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jsonPayload.occurTime`, `rdp_record.desktopHeight`, `rdp_record.desktopWidth`, `rdp_record.keyboardLayout`, `rdp_record.requestedColorDepth`, `rdp_record.clientL2Bytes`, `rdp_record.serverL2Bytes` raw log field(s) `with event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alert_value` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Mapped `application_protocol` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Mapped `events.principal.asset_id` (index 0) raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Mapped `events.principal.asset_id` (index > 0) raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Mapped `events.target.asset_id` (index 0) raw log field to `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Mapped `events.target.asset_id` (index > 0) raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Mapped `events.target.hostname` (index 0) raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Mapped `events.target.hostname` (index > 0) raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Mapped `events.principal.hostname` (index 0) raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Mapped `events.principal.hostname` (index 0) raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Mapped `events.principal.hostname` (index > 0) raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Mapped `events.principal.user` (index > 0) raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Mapped `events.target.user` (index > 0) raw log field to `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- Added grok pattern for `events.vulnerability.description` to extract `application_protocol`, flow, and payload.  
\- Updated event.idm.read_only_udm.metadata.event_type logic to set to USER_UNCATEGORIZED if has_principal_user or has_target_user is true.  
\- Removed the redundant code for mapping `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.userid`.   
2025-07-16 |  Enhancement:  
\- Modified grok patterns to handle new fields from the `description` field.  
\- event.idm.read_only_udm.target.application: Newly mapped `target_app` raw log field to event.idm.read_only_udm.target.application.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `file_transfer_description` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `target_file` raw log field to event.idm.read_only_udm.target.file.full_path.  
\- event.idm.read_only_udm.target.registry.registry_key: Newly mapped `registry_path` raw log field to event.idm.read_only_udm.target.registry.registry_key.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `command_path` raw log field to event.idm.read_only_udm.target.process.command_line.  
\- Added support for event.idm.read_only_udm.metadata.event_type to USER_LOGIN when title is `Kerberos Wrong Password Errors`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to REGISTRY_MODIFICATION when title is `New Remote Registry Modification Attempt`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to PROCESS_LAUNCH when title is `Remote Service Launch`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to SCAN_NETWORK when title is `TCP SYN Scan`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to FILE_CREATION when title is `New SMB Executable File Transfer Activity`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to USER_LOGIN when title is `Microsoft 365 Risky User Activities: Unfamiliar Sign-In Properties`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to NETWORK_CONNECTION when title is `New Remote Access Software Activity`.  
\- Added support for event.idm.read_only_udm.metadata.event_type to USER_LOGIN when title is `LDAP Invalid Credentials Error`.   
2025-06-30 |  \- `event.idm.read_only_udm.target.asset.asset_id` and `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `jsonPayload.target.asset_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` and `event.idm.read_only_udm.target.resource.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.principal.asset.asset_id` and `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `jsonPayload.principal.asset_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` and `event.idm.read_only_udm.principal.resource.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `jsonPayload.target.ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `jsonPayload.principal.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `jsonPayload.target.mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `jsonPayload.principal.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields and `event.idm.read_only_udm.principal.resource.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` and `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `jsonPayload.target.hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields and `event.idm.read_only_udm.target.resource.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.target.user.userid` and `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `jsonPayload.target.user` raw log field with `event.idm.read_only_udm.target.user.userid` and `event.idm.read_only_udm.target.user.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `jsonPayload.principal.user` raw log field with `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.principal.user.attribute.labels` if it has array of values.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector`: Newly mapped `jsonPayload.vulnerability.cvss_vector` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector` UDM field.   
2025-06-16 |  \- `event.idm.read_only_udm.metadata.description`: Removed mapping of `events.vulnerability.description` raw log field from `event.idm.read_only_udm.metadata.description` to make uniform mapping and also events.metadata.description is already mapped to event.idm.read_only_udm.metadata.description.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `events.vulnerability.description` raw log field with `event.idm.read_only_udm.security_result.detection_fields`.  
\- Added Grok patterns to parse the field from the raw logs.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `suspicious_domain` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `rule_created`, `rule_update` and 'rule_provided_by` raw log field with `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.about.url`: Newly mapped `reference` raw log field with `event.idm.read_only_udm.security_result.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `sid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.   
2025-05-15 |  \- Added support for Missing Mapping of ExtraHop RevealX Webhook Schema as per the ExtraHop Team request.   
2025-05-09 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Added support to generate separate event for each victim, if multiple victims are present in the same log.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp, event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `start_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` and `event.idm.read_only_udm.security_result.first_discovered_time` UDM fields.  
\- event.idm.read_only_udm.security_result.last_updated_time: Newly mapped `update_time` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `end_time` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.risk_score: Newly mapped `risk_score` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `categories` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.asset.category: Newly mapped `participant.endpoint` raw log field with `event.idm.read_only_udm.principal.asset.category` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `participant.object_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `participant.object_value` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `participant.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `participant.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.target.asset.category: Newly mapped `participant.endpoint` raw log field with `event.idm.read_only_udm.target.asset.category` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.asset.product_object_id: Newly mapped `participant.object_id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `participant.object_value` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Newly mapped `participant.hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `participant.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.security_result.attack_details.tactics.id: Newly mapped `mitre_tactics.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.id` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics.name: Newly mapped `mitre_tactics.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.name` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques.id: Newly mapped `mitre_techniques.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.id` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques.name: Newly mapped `mitre_techniques.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `create_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `url` raw log field with `event.idm.read_only_udm.url_back_to_product` UDM field.   
2025-05-06 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.resource_subtype: Removed mapping of `resource.type` from `event.idm.read_only_udm.target.resource.resource_subtype`.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Mapped `resource.type` to `event.idm.read_only_udm.intermediary.resource.resource_subtype`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `resource.labels.method` from `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Mapped `resource.labels.method` to `event.idm.read_only_udm.intermediary.resource.attribute.labels`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `jsonPayload.intermediary.hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `jsonPayload.metadata.description` raw log field with `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `jsonPayload.metadata.product_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `jsonPayload.metadata.url_back_to_product` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product`.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `jsonPayload.principal.asset_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `jsonPayload.principal.ip` raw log field with `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `jsonPayload.principal.user` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score: Newly mapped `jsonPayload.vulnerability.cvss_base_score` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score`.  
\- event.idm.read_only_udm.security_result.about.asset.vulnerabilities.first_found: Newly mapped `jsonPayload.vulnerability.first_found` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.first_found`.  
\- event.idm.read_only_udm.security_result.about.asset.vulnerabilities.last_found: Newly mapped `jsonPayload.vulnerability.last_found` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.last_found`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `jsonPayload.vulnerability.description` raw log field with `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.security_result.about.asset.vulnerabilities.name: Newly mapped `jsonPayload.vulnerability.name` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.name`.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `jsonPayload.vulnerability.severity` raw log field with `event.idm.read_only_udm.security_result.severity`.   
2025-05-05 |  Enhancement:  
\- `event.idm.ready_only_udm.security_result.severity`: Modified the logic for mapping `sr_severity` raw log field with `event.idm.ready_only_udm.security_result.severity` UDM field when `severity` is equal to null and `risk_score` is not null.  
If `risk_score` >= 90 then mapped `security_result.severity` to `CRITICAL`.  
If `risk_score` >= 70 then mapped `security_result.severity` to `ERROR`.  
If `risk_score` >= 60 then mapped `security_result.severity` to `HIGH`.  
If `risk_score` >= 40 then mapped `security_result.severity` to `MEDIUM`.  
If `risk_score` >= 20 then mapped `security_result.severity` to `LOW`.  
else mapped `security_result.severity` to `INFORMATIONAL`.  
\- `event.idm.ready_only_udm.security_result.severity`: Modified the logic for mapping `sr_severity` raw log field with `event.idm.ready_only_udm.security_result.severity` UDM field when `alert_severity` is not equal to null.  
If `alert_severity` is `1` then mapped `security_result.severity` to `CRITICAL`.  
If `alert_severity` is `2` then mapped `security_result.severity` to `HIGH`.  
If `alert_severity` is `3` then mapped `security_result.severity` to `ERROR`.  
If `alert_severity` is `4` then mapped `security_result.severity` to `MEDIUM`.  
If `alert_severity` is `5` then mapped `security_result.severity` to `LOW`.  
If `alert_severity` is `6` or `7` then mapped `security_result.severity` to `INFORMATIONAL`.  
\- `event.idm.ready_only_udm.security_result.severity`: Modified the logic for mapping `sr_severity` raw log field with `event.idm.ready_only_udm.security_result.severity` UDM field when `events.vulnerability.severity` has `critical` and `high` values.  
If `events.vulnerability.severity` is `critical` then mapped `security_result.severity` to `CRITICAL`.  
If `events.vulnerability.severity` is `high` then mapped `security_result.severity` to `HIGH`.  
\- `event.idm.ready_only_udm.security_result.severity`: Modified the logic for mapping `sr_severity` raw log field with `event.idm.ready_only_udm.security_result.severity` UDM field when `cn2_risk_score` is not equal to null and `severity` is equal to null".  
If `cn2_risk_score` >= 90 then mapped `security_result.severity` to `CRITICAL`.  
If `cn2_risk_score` >= 70 then mapped `security_result.severity` to `ERROR`.  
If `cn2_risk_score` >= 60 then mapped `security_result.severity` to `HIGH`.  
If `cn2_risk_score` >= 40 then mapped `security_result.severity` to `MEDIUM`.  
If `cn2_risk_score` >= 20 then mapped `security_result.severity` to `LOW`.  
else mapped `security_result.severity` to `INFORMATIONAL`.   
2025-04-22 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp, event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `start_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` and `event.idm.read_only_udm.security_result.first_discovered_time` UDM fields.  
\- event.idm.read_only_udm.security_result.last_updated_time: Newly mapped `update_time` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `end_time` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.risk_score: Newly mapped `risk_score` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `categories` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.asset.category: Newly mapped `participant.endpoint` raw log field with `event.idm.read_only_udm.principal.asset.category` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `participant.object_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `participant.object_value` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `participant.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields if `participant.role` is `offender`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `participant.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if `participant.role` is `offender`.  
\- event.idm.read_only_udm.target.asset.category: Newly mapped `participant.endpoint` raw log field with `event.idm.read_only_udm.target.asset.category` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.asset.product_object_id: Newly mapped `participant.object_id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `participant.object_value` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Newly mapped `participant.hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields if `participant.role` is `victim`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `participant.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field if `participant.role` is `victim`.  
\- event.idm.read_only_udm.security_result.attack_details.tactics.id: Newly mapped `mitre_tactics.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.id` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics.name: Newly mapped `mitre_tactics.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.name` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques.id: Newly mapped `mitre_techniques.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.id` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques.name: Newly mapped `mitre_techniques.name` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `create_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `url` raw log field with `event.idm.read_only_udm.url_back_to_product` UDM field.   
2025-04-07 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-11 |  Enhancement:  
\- Mapped `jsonPayload.msg` to `metadata.description`.  
\- Mapped `jsonPayload.srcdata` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `jsonPayload.dstdata` to `target.ip` and `target.asset.ip`.  
\- Mapped `jsonPayload.dhost` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `jsonPayload.shost` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `insertId` to `additional.fields`.  
\- Mapped `jsonPayload.cn2` to `security_result.risk_score`.  
\- Mapped `jsonPayload.name` to `security_result.summary`.  
\- Mapped `jsonPayload.rt` to `metadata.event_timestamp`.  
\- Mapped `jsonPayload.start`, `jsonPayload.end` and `logName` to `additional.fields`.  
\- Mapped `resource.labels.method` and `resource.labels.service` to `target.resource.attribute.labels`.  
\- Mapped `jsonPayload.cat` and `jsonPayload.cs5` to `security_result.detection_fields`.   
2025-01-15 |  Enhancement:  
\- Mapped `dst` to `target.asset.ip` and `target.ip`.   
2025-01-09 |  Enhancement:  
\- Mapped `url` to `principal.url`.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `title`, `id`, `description_format`, `victims.name`, `victims.external`, `offenders.name`, `offenders.externaal`, `victim_primary.name`, victim_primary.external`, `offender_primary.name`, and `offender_primary.external` to `additional.fields".  
\- Mapped `dst.type` to `target.resource_type`.  
\- Mapped `dst.hostname` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `dst.ipaddr` to `target.ip` and `target.asset.ip`.  
\- Mapped `dst.role` to `target_resource.attribute.roles`.  
\- Mapped `dst.device.macaddr` to `target.mac`.  
\- Mapped `src.type` to `principal.resource_type`.  
\- Mapped `src.hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `src.ipaddr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `src.role` to `principal_resource.attribute.roles`.  
\- Mapped `src.device.macaddr` to `principal.mac`.  
\- Mapped `api.ip`, `api.status`, `api.id`, `api.start_time`, `api.mod_time`, `api.categories`, `api.update_time`, and `api.ticket_id` to `security_result.detection_fields`.  
\- Mapped `victims.ipaddr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `offenders.ipaddr` to `target.ip` and `target.asset.ip`.  
\- Mapped `victim_primary.ipaddr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `offender_primary.ipaddr` to `target.ip` and `target.asset.ip`.  
\- Mapped `api.participants.role`, `api.participants.object_id`, `api.participants.object_type`, and `api.participants.external` to `section_details.fields`.  
\- Mapped `risk_score` and `api.risk_score` to `security_result.risk_score`.  
\- Mapped `src.endpoint` and `src.device.oid` to `principal.resource.attribute.labels`.  
\- Mapped `dst.endpoint` and `dst.device.oid` to `target.resource.attribute.labels`.  
\- Mapped `dst.device.ipaddr` to `target.ip` and `target.asset.ip`.  
\- Mapped `src.device.ipaddr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `categories_array` and `categories_id` to `additional.fields`.   
2024-12-13 |  Enhancement:  
\- Mapped `src` to `principal.asset.ip`.  
\- Mapped `dst` to `target.asset.ip` and `target.ip`.  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `signature` to `security_result.summary` and `section_details.rule_name`.   
2024-11-26 |  Enhancement:  
\- If `events.vulnerability.severity` equals `medium`, then map `MEDIUM` to `security_result.severity`.  
\- Mapped `events.vulnerability.description` to `metadata.description`.   
2024-10-28 |  Enhancement:  
\- Added support to handle SYSLOG+JSON logs.   
2023-10-27 |  Enhancement:  
\- Added JSON block to parse uparsed JSON logs.  
\- Reduced the percentage of events with `metadata.event_type` set to `GENERIC_EVENT` to 0.   
2022-12-15 |  Enhancement:  
\- Mapped the field `macaddr` to `principal.mac`.  
\- Mapped the field `ipaddr` to `principal.ip`.  
\- Mapped the field `object_name` to `target.resource.name`.  
\- Mapped the field `object_type` to `target.resource.resource_type`.  
\- Mapped the field `object_id` to `target.resource.product_object_id`.  
\- Mapped the field `event_id` to `metadata.product_event_type`.  
\- Mapped the field `operation` to `metadata.product_event_type`.  
\- Mapped the field `user` to `principal.user.userid`.  
\- Mapped the field `facility` to `principal.resource.resource_subtype`.  
\- Mapped the field `src_ip` to `principal.ip`.  
\- Mapped the field `summary` to `security_result.summary`.  
\- Mapped the field `name` to `metadata.description`.  
\- Mapped the field `severity` to `security_result.severity_details`.  
\- Mapped the field `priority` to `security_result.severity` and `security_result.severity_details`.  
\- Mapped the field `alert_name` to `security_result.summary`.   
2022-06-30 |  Enhancement:  
\- Mapped `detectionID` to `security_result.rule_labels`.  
\- When `product_event_type` is equal to `Unsafe LDAP Authentication` Mapped `event_type` to `STATUS_UPDATE`.  
\- Mapped `prin_url` to `principal.url`.  
\- Mapped `desc` to `metadata.description`.   
2022-05-18 |  Enhancement - The newly ingested logs have been parsed and mapped to the following fields:  
`RDP Record.clientName` mapping changed to `principal.hostname` from `principal.user.userid`.  
`RDP Record.cookie` mapped to `principal.user.userid`.  
`eh_event` mapping changed to `network.application_protocol` from `metadata.product_event_type`.   
2022-05-10 |  Enhancement - The newly ingested logs have been parsed and mapped to the following fields:  
server_ip` mapped to `target.ip'.  
`RDP Record.proto` mapped to `network.ip_protocol`.  
`RDP Record.clientPort` mapped to `principal.port`.  
`RDP Record.clientName` mapped to `principal.user.userid`.  
`RDP Record.clientBytes` mapped to `network.sent_bytes`.  
`RDP Record.serverBytes` mapped to `network.received_bytes`.  
`RDP Record.clientBuild` mapped to `metadata.product_version`.  
`RDP Record.selectedProtocol` mapped to `security_result.description`.  
`eh_event` mapped to `metadata.product_event_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
