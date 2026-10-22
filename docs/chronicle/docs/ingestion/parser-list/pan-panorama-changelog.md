---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-panorama-changelog/
title: Change log for PAN_PANORAMA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:50.784968+00:00
---

# Change log for PAN_PANORAMA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-panorama-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_PANORAMA

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- Added support for new format of JSON + CSV logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added fallback logic to populate `event_ts` from `column7`, `column22`, or `column2` when `column1` lacks a syslog header.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column108`, `column103`, `column125`, `column7`, `column22` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `column112`, `column116` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `column109` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2026-06-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `config_ver`, `pan_category_or_id`, `action_flags`, `auth_profile`, `vsys_data`, `server_profile`, `idp_entity_id`, `sys_ver`, `Time_Generated`, `Generate_Time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when the logs contain login-related data.   
2026-04-21 |  Enhancement:  
\- Added support for the new format of the event `HIPMATCH`, `THREAT` logs and relevant corresponding raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pan_generated_timestamp`, `column19`, `high_timestamp`, `log_format_version`, `config_version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column8` raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column13`, `column14` raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hardware.model: Newly mapped `column25` raw log field with event.idm.read_only_udm.intermediary.asset.hardware.model UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `column28` raw log field with event.idm.read_only_udm.principal.asset.asset_id UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `column10` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `relay_hostname` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is true and `has_user` is true, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `network`, `pan`, `firewall`, `action`, `technology` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `principal_ip` and `target_ip` are not empty, updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `rules`, `testdata`, `log_forwarding_profile` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-05 |  Enhancement:  
\- Modified grok pattern to parse the `security_result_threat_name` field. The text portion is now mapped to `event.idm.read_only_udm.security_result.threat_name`, and the numeric portion within parentheses is mapped to `event.idm.read_only_udm.security_result.threat_id`. If the pattern doesn't match, the original `security_result_threat_name` value is mapped to `event.idm.read_only_udm.security_result.threat_name`.  
\- Updated the mapping logic for `event.idm.read_only_udm.network.direction` to include support for `client to server` and `server to client` as values for determining `OUTBOUND` and `INBOUND` directions, respectively.   
2026-01-26 |  Enhancement:  
\- Reverted back the changes in `pan_firewall_udm_mapping.include` file to avoid conflicts with the other parser.  
\- Created a new include file `pan_panorama_firewall_udm_mapping.include`.   
2026-01-16 |  Enhancement:  
\- Updated the parsing logic from customer-specific to generic.   
2026-01-08 |  Enhancement:  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `security_result_threat_name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Dynamic_DNS`, raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.network.ip_subnet_range: Newly mapped `principal_location_country_or_region` raw log field with `event.idm.read_only_udm.principal.network.ip_subnet_range` UDM field.  
\- event.idm.read_only_udm.target.network.ip_subnet_range: Newly mapped `target_location_country_or_region` raw log field with `event.idm.read_only_udm.target.network.ip_subnet_range` UDM field.  
\- Removed null values from `event.idm.read_only_udm.target.user.product_object_id`, `event.idm.read_only_udm.principal.user.product_object_id`, `event.idm.read_only_udm.network.http.method`, `event.idm.read_only_udm.network.http.referral_url`, `event.idm.read_only_udm.target.product_object_id` UDM fieldss.   
2025-12-24 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_hostname_1` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- Removed leading/trailing backslashes.  
\- Added a new Grok pattern to extract `target_hostname_1` from event_description.  
\- Added `monitoring` and `dhcp` in the conditional check.   
2025-10-31 |  Enhancement:  
\- Added conditional parsing logic to handle a different CSV column layout for logs where the firewall_name starts with `Panorama`. The field mappings listed below are specific to this condition.  
\- Added support for an additional syslog timestamp format.  
\- Dropped logs containing the string `futureuse1`.  
\- Removed trailing `.0` from fields derived from `column36`, `column46`, and `column47`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column9` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column9` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `column10` raw log field to `event.idm.read_only_udm.target.ip`.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `column10` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `column11` raw log field to `event.idm.read_only_udm.principal.nat_ip`.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `column12` raw log field to `event.idm.read_only_udm.target.nat_ip`.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `column13` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column14` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `column15` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- event.idm.read_only_udm.target.application: Newly mapped `column16` raw log field to `event.idm.read_only_udm.target.application`.  
\- event.idm.read_only_udm.additional.fields[`vsys`]: Newly mapped `column17` raw log field to `event.idm.read_only_udm.additional.fields[`vsys`]`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels[`from`]: Newly mapped `column18` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels[`from`]`.  
\- event.idm.read_only_udm.target.resource.attribute.labels[`to`]: Newly mapped `column19` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels[`to`]`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels[`inbound_if`]: Newly mapped `column20` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels[`inbound_if`]`.  
\- event.idm.read_only_udm.target.resource.attribute.labels[`outbound_if`]: Newly mapped `column21` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels[`outbound_if`]`.  
\- event.idm.read_only_udm.additional.fields[`logset`]: Newly mapped `column22` raw log field to `event.idm.read_only_udm.additional.fields[`logset`]`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `column24` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- event.idm.read_only_udm.additional.fields[`repeatcnt`]: Newly mapped `column25` raw log field to `event.idm.read_only_udm.additional.fields[`repeatcnt`]`.  
\- event.idm.read_only_udm.principal.port: Newly mapped `column26` raw log field to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.target.port: Newly mapped `column27` raw log field to `event.idm.read_only_udm.target.port`.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `column28` raw log field to `event.idm.read_only_udm.principal.nat_port`.  
\- event.idm.read_only_udm.target.nat_port: Newly mapped `column29` raw log field to `event.idm.read_only_udm.target.nat_port`.  
\- event.idm.read_only_udm.additional.fields[`flags`]: Newly mapped `column30` raw log field to `event.idm.read_only_udm.additional.fields[`flags`]`.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `column31` raw log field to `event.idm.read_only_udm.network.ip_protocol`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `column32` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `column34` raw log field to `event.idm.read_only_udm.network.sent_bytes`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `column35` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `column39` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `column41` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.additional.fields[`actionflags`]: Newly mapped `column42` raw log field to `event.idm.read_only_udm.additional.fields[`actionflags`]`.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `column43` raw log field to `event.idm.read_only_udm.principal.location.country_or_region`.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `column44` raw log field to `event.idm.read_only_udm.target.location.country_or_region`.  
\- event.idm.read_only_udm.network.sent_packets: Newly mapped `column46` raw log field to `event.idm.read_only_udm.network.sent_packets`.  
\- event.idm.read_only_udm.network.received_packets: Newly mapped `column47` raw log field to `event.idm.read_only_udm.network.received_packets`.  
\- event.idm.read_only_udm.additional.fields[`dg_hier_level_1`]: Newly mapped `column49` raw log field to `event.idm.read_only_udm.additional.fields[`dg_hier_level_1`]`.  
\- event.idm.read_only_udm.additional.fields[`dg_hier_level_2`]: Newly mapped `column50` raw log field to `event.idm.read_only_udm.additional.fields[`dg_hier_level_2`]`.  
\- event.idm.read_only_udm.additional.fields[`dg_hier_level_3`]: Newly mapped `column51` raw log field to `event.idm.read_only_udm.additional.fields[`dg_hier_level_3`]`.  
\- event.idm.read_only_udm.additional.fields[`dg_hier_level_4`]: Newly mapped `column52` raw log field to `event.idm.read_only_udm.additional.fields[`dg_hier_level_4`]`.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `column53` raw log field to `event.idm.read_only_udm.principal.resource.name`.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `column56` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `column57` raw log field to `event.idm.read_only_udm.target.user.product_object_id`.  
\- event.idm.read_only_udm.additional.fields[`tunnel_id`]: Newly mapped `column58` raw log field to `event.idm.read_only_udm.additional.fields[`tunnel_id`]`.  
\- event.idm.read_only_udm.additional.fields[`monitortag`]: Newly mapped `column59` raw log field to `event.idm.read_only_udm.additional.fields[`monitortag`]`.  
\- event.idm.read_only_udm.network.parent_session_id: Newly mapped `column60` raw log field to `event.idm.read_only_udm.network.parent_session_id`.  
\- event.idm.read_only_udm.additional.fields[`tunnel`]: Newly mapped `column62` raw log field to `event.idm.read_only_udm.additional.fields[`tunnel`]`.  
\- event.idm.read_only_udm.additional.fields[`assoc_id`]: Newly mapped `column63` raw log field to `event.idm.read_only_udm.additional.fields[`assoc_id`]`.  
\- event.idm.read_only_udm.additional.fields[`chunks`]: Newly mapped `column64` raw log field to `event.idm.read_only_udm.additional.fields[`chunks`]`.  
\- event.idm.read_only_udm.additional.fields[`chunks_sent`]: Newly mapped `column65` raw log field to `event.idm.read_only_udm.additional.fields[`chunks_sent`]`.  
\- event.idm.read_only_udm.additional.fields[`chunks_received`]: Newly mapped `column66` raw log field to `event.idm.read_only_udm.additional.fields[`chunks_received`]`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `column67` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- event.idm.read_only_udm.additional.fields[`http2_connection`]: Newly mapped `column68` raw log field to `event.idm.read_only_udm.additional.fields[`http2_connection`]`.  
\- event.idm.read_only_udm.principal.asset.category: Newly mapped `column78` raw log field to `event.idm.read_only_udm.principal.asset.category`.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `column82` raw log field to `event.idm.read_only_udm.principal.asset.platform_software.platform`.  
\- event.idm.read_only_udm.principal.asset.software_version: Newly mapped `column83` raw log field to `event.idm.read_only_udm.principal.asset.software_version`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `column84` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `column85` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- event.idm.read_only_udm.target.asset.category: Newly mapped `column86` raw log field to `event.idm.read_only_udm.target.asset.category`.  
\- event.idm.read_only_udm.target.asset.platform_software.platform: Newly mapped `column90` raw log field to `event.idm.read_only_udm.target.asset.platform_software.platform`.  
\- event.idm.read_only_udm.target.asset.software_version: Newly mapped `column91` raw log field to `event.idm.read_only_udm.target.asset.software_version`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `column92` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- event.idm.read_only_udm.target.mac: Newly mapped `column93` raw log field to `event.idm.read_only_udm.target.mac`.  
\- event.idm.read_only_udm.additional.fields[`container_id`]: Newly mapped `column94` raw log field to `event.idm.read_only_udm.additional.fields[`container_id`]`.  
\- event.idm.read_only_udm.additional.fields[`pod_namespace`]: Newly mapped `column95` raw log field to `event.idm.read_only_udm.additional.fields[`pod_namespace`]`.  
\- event.idm.read_only_udm.additional.fields[`pod_name`]: Newly mapped `column96` raw log field to `event.idm.read_only_udm.additional.fields[`pod_name`]`.  
\- event.idm.read_only_udm.principal.asset.hardware.serial_number: Newly mapped `column100` raw log field to `event.idm.read_only_udm.principal.asset.hardware.serial_number`.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `column101` raw log field to `event.idm.read_only_udm.principal.group.group_display_name`.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `column102` raw log field to `event.idm.read_only_udm.target.group.group_display_name`.  
\- event.idm.read_only_udm.additional.fields[`session_owner`]: Newly mapped `column103` raw log field to `event.idm.read_only_udm.additional.fields[`session_owner`]`.  
\- event.idm.read_only_udm.additional.fields[`nsdsai_sst`]: Newly mapped `column105` raw log field to `event.idm.read_only_udm.additional.fields[`nsdsai_sst`]`.  
\- event.idm.read_only_udm.additional.fields[`nsdsai_sd`]: Newly mapped `column106` raw log field to `event.idm.read_only_udm.additional.fields[`nsdsai_sd`]`.  
\- event.idm.read_only_udm.additional.fields[`subcategory_of_app`]: Newly mapped `column107` raw log field to `event.idm.read_only_udm.additional.fields[`subcategory_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`category_of_app`]: Newly mapped `column108` raw log field to `event.idm.read_only_udm.additional.fields[`category_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`technology_of_app`]: Newly mapped `column109` raw log field to `event.idm.read_only_udm.additional.fields[`technology_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`risk_of_app`]: Newly mapped `column110` raw log field to `event.idm.read_only_udm.additional.fields[`risk_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`characteristic_of_app`]: Newly mapped `column111` raw log field to `event.idm.read_only_udm.additional.fields[`characteristic_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`container_of_app`]: Newly mapped `column112` raw log field to `event.idm.read_only_udm.additional.fields[`container_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`is_saas_of_app`]: Newly mapped `column113` raw log field to `event.idm.read_only_udm.additional.fields[`is_saas_of_app`]`.  
\- event.idm.read_only_udm.additional.fields[`sanctioned_state_of_app`]: Newly mapped `column114` raw log field to `event.idm.read_only_udm.additional.fields[`sanctioned_state_of_app`]`.  
\- event.idm.read_only_udm.metadata.timestamp: Newly mapped `column3` raw log field to `event.idm.read_only_udm.metadata.timestamp`.   
2025-07-18 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `column53` to `principal.hostname` and `principal.asset.hostname` UDM fields when `type` is `TRAFFIC`.   
2025-06-06 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `column53` from `principal.hostname` UDM field when `type` is `TRAFFIC`.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `column53` from `principal.asset.hostname` UDM field when `type` is `TRAFFIC`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Mapped `column53` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when `type` is `TRAFFIC`.  
\- Modified the mappings from `event.idm.read_only_udm.principal.labels` to `event.idm.read_only_udm.principal.resource.attribute.labels` since `event.idm.read_only_udm.principal.labels` is deprecated.  
\- Modified the mappings from `event.idm.read_only_udm.target.labels` to `event.idm.read_only_udm.target.resource.attribute.labels` since `event.idm.read_only_udm.target.labels` is deprecated.   
2025-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `misc_data` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- Added a Grok pattern to parse the `misc_data` values.   
2025-04-03 |  Enhancement:  
\- Added support to parse `event_ts` with date format `MMM d HH:mm:ss` by writing a grok pattern to fetch year from the log.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_ts_1` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-18 |  Enhancement:  
\- Added a Grok pattern to parse `from_ip` to `principal.ip` and `principal.asset.ip` for different log formats.   
2025-03-12 |  Enhancement:  
\- Added a Grok pattern to parse `event_ts` and `firewall_name`.  
\- Mapped `event_ts` to `metadata.event_timestamp`.   
2025-02-27 |  Enhancement:  
\- Added a Grok pattern to parse `from_ip` to `principal.ip` and `principal.asset.ip`.   
2025-01-30 |  Enhancement:  
\- Added a new Grok pattern for `user_description`.  
\- Mapped `user_description` to `security_result.description`.   
2025-01-20 |  Enhancement:  
\- Modified mapping for `firewall_name` from `principal.hostname` to `intermediary.hostname`.  
\- Mapped `column53` to `principal.hostname` and `principal.asset.hostname`.   
2024-12-11 |  Enhancement:  
\- Added support for CSV logs where `type` is equal to `SYSTEM`.   
2024-12-10 |  Enhancement:  
\- Mapped `firewall_name` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `column15` to `security_result.summary`.   
2024-09-10 |  Enhancement:  
\- Removed duplicate mapping for `security_result.detection_fields`.  
\- Modified field value for `metadata.product_event_type`.   
2024-09-02 |  Enhancement:  
\- Mapped `sub_type` to `additional.fields`.   
2024-07-19 |  Enhancement:  
\- Implemented parsing for `Threat` subtype and modified existing parsers to accurately populate the corresponding UDM field.  
\- Added support for CSV logs where `type` is equal to `CONFIG`.   
2024-07-10 |  Enhancement:  
\- Added support for `USERID` CSV logs.   
2024-07-09 |  Enhancement:  
\- When `type` is `SYSTEM` then mapped `sub_type` to `security_result.detection_fields`.   
2024-06-15 |  Enhancement:  
\- When `target_port` is not empty, then mapped `target_port` to `target.port`.   
2024-01-25 |  Enhancement:  
\- Mapped `characterstic_of_app` to `security_result.summary`.  
\- Mapped `pkts_received` to `network.received_packets`.  
\- Mapped `pkts_sent` to `network.sent_bytes`.  
\- Mapped `md5hash` to `principal.file.md5`.  
\- Mapped `sha256hash` to `principal.file.sha256`.  
\- Mapped `sha1hash` to `principal.file.sha1`.  
\- Mapped `about_file_mime_type` to `principal.file.mime_type`.  
\- Mapped `principal_ip` to `principal.asset.ip`.  
\- Mapped `principal_ip1` to `principal.asset.ip`.  
\- Mapped `principal_ip2` to `principal.asset.ip`.  
\- Mapped `principal_ip3` to `principal.asset.ip`.  
\- Mapped `principal_hostname` to `principal.asset.hostname`.  
\- Mapped `target_ip` to `target.asset.ip`.  
\- Mapped `target_ip1` to `target.asset.ip`.  
\- Mapped `target_hostname` to `target.asset.hostname`.  
\- Mapped `intermediary_hostname` to "`intermediary.asset.hostname`.  
\- Mapped `category_of_app` to `security_result.category_details`.  
\- Mapped `subcategory_of_app1` to `security_result.category_details`.  
\- Mapped `subcategory_of_app` to `security_result.category_details`.   
2023-08-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
