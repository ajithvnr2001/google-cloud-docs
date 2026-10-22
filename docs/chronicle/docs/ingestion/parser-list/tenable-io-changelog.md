---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-io-changelog/
title: Change log for TENABLE_IO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:33.985170+00:00
---

# Change log for TENABLE_IO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-io-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TENABLE_IO

Date | Changes  
---|---  
2026-08-05 |  Enhancement:  
\- Modified the parser logic to extract `event.idm.read_only_udm.network.ip_protocol` from `port.protocol`, ensuring it only accepts valid enum values.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `port.protocol` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `ip_protocol_out` when the protocol is unknown.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `plugin.cpe` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `asset.operating_system` raw log field to `event.idm.read_only_udm.principal.asset.attribute.labels`.   
2026-01-19 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `metadata.event_timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `metadata.product_name` raw log field to `event.idm.read_only_udm.metadata.product_name`.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `metadata.vendor_name` raw log field to `event.idm.read_only_udm.metadata.vendor_name`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `metadata.event_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `security_result.description` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target.asset.hostname` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target.asset.hostname` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target.asset.ip` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target.asset.ip` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `target.asset.asset_id` raw log field to `event.idm.read_only_udm.target.asset.asset_id`.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `target.asset_id` raw log field to `event.idm.read_only_udm.target.asset.asset_id`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `target.resource.name` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- Added logic to populate `event.idm.read_only_udm.security_result.severity` based on the values of the `security_result.category` raw field.  
\- Added gsub to change string `security_result` to `sec_res` to avoid error.   
2026-01-13 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version`,`update.plugin.patch_publication_date`,`update.plugin.solution`,`update.plugin.vpr.drivers.threat_sources_last28`,`update.resurfaced_date`,`update.last_fixed`,`update.asset.operating_system`,`update.plugin.cve`,`update.plugin.bid`,`count_updated`,`count_deleted` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.entity.entity.asset.vulnerabilities.cve_id`: Newly mapped `update.plugin.cve` raw log field to `event.idm.entity.entity.asset.vulnerabilities.cve_id`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `update.plugin.see_also`,`update.plugin.cvss_vector.access_vector`,`update.asset.netbios_name`,`update.plugin.cvss3_vector.user_interaction`,`update.plugin.cvss3_vector.privileges_required`,`update.plugin.cvss3_vector.raw`,`update.plugin.cvss3_vector.integrity_impact`,`update.plugin.cvss3_vector.confidentiality_impact`,`update.plugin.cvss3_vector.availability_impact`,`update.plugin.cvss3_vector.authentication`,`update.plugin.cvss3_vector.access_vector`,`update.plugin.cvss3_vector.access_complexity`,`update.plugin.cvss_base_score`,`update.plugin.cvss_vector.raw`,`update.plugin.cvss_vector.integrity_impact`,`update.plugin.cvss_vector.confidentiality_impact`,`update.plugin.cvss_vector.availability_impact`,`update.plugin.cvss_vector.authentication`,`update.plugin.cvss_vector.access_complexity`,`update.plugin.stig_severity`,`update.plugin.vuln_publication_date`,`update.plugin.xrefs.id`,`update.plugin.xrefs.type`,`update.plugin.vpr.updated`,`update.plugin.vpr.drivers.product_coverage`,`update.plugin.vpr.drivers.threat_recency.upper_bound`,`update.plugin.vpr.drivers.threat_recency.lower_bound`,`update.plugin.vpr.drivers.threat_intensity_last28`,`update.plugin.vpr.drivers.cvss_impact_score_predicted`,`update.plugin.vpr.drivers.exploit_code_maturity`,`update.plugin.vpr.drivers.age_of_vuln.lower_bound`,`update.plugin.vpr.drivers.age_of_vuln.upper_bound`,`update.plugin.vpr.score`,`update.plugin.vpr_v2.malware_observations_recency`,`update.plugin.vpr_v2.malware_observations_intensity_last30`,`update.plugin.vpr_v2.in_the_news_recency`,`update.plugin.vpr_v2.in_the_news_intensity_last30`,`update.plugin.vpr_v2.on_cisa_kev`,`update.plugin.vpr_v2.exploit_code_maturity`,`update.plugin.vpr_v2.cve_id`,`update.plugin.vpr_v2.exploit_probability`,`update.plugin.vpr_v2.vpr_severity`,`update.plugin.vpr_v2.vpr_percentile`,`update.plugin.vpr_v2.score` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `update.plugin.cpe` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.   
2025-12-29 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.last_record_timestamp`,`payload.first_record_timestamp`,`payload.num_deletes`,`payload.num_updates`,`payload.version`,`payload_type`,`portData.protocol`,`open_ports.first_seen`,`open_ports.last_seen`,`networkinterface.name`,`source.last_seen`,`source.first_seen`,`source.name`,`update.plugin.exploit_framework_exploithub`,`update.plugin.exploit_framework_metasploit`,`update.plugin.exploited_by_malware`,`update.plugin.exploited_by_nessus`,`update.plugin.family`,`update.plugin.has_patch`,`update.plugin.id`,`update.plugin.in_the_news`,`update.plugin.name`,`update.plugin.modification_date`,`update.plugin.publication_date`,`update.plugin.synopsis`,`update.plugin.type`,`update.plugin.unsupported_by_vendor`,`update.plugin.version`,`update.plugin.has_workaround`,`update.first_found`,`update.last_found`,`update.indexed`,`update.state`,`update.source`,`update.has_agent`,`update.has_plugin_results`,`update.created_at`,`update.updated_at`,`update.first_seen`,`update.last_seen`,`update.network_id`,`update.acr_score`,`update.exposure_score`,`update.port.protocol`,`update.plugin.exploit_framework_d2_elliot`,`update.plugin.exploit_framework_core`,`update.plugin.exploit_framework_canvas`,`update.plugin.exploit_available`,`update.plugin.description`,`update.plugin.checks_for_malware`,`update.plugin.checks_for_default_account`,`update.output`,`update.asset.tracked`,`update.asset.fqdn`,`update.asset.network_id` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `update.asset.last_scan_target` raw log field to `event.idm.read_only_udm.target.attribute.labels`.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` and `event.idm.entity.entity.asset.ip`: Newly mapped `update.asset.ipv4`,`update.ipv4s` raw log field to `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip` and `event.idm.entity.entity.asset.ip`.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `update.scan.target`,`update.asset.last_scan_target`,`update.last_scan_target` raw log field to `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `update.last_schedule_id`,`update.last_scan_id`,`update.last_licensed_scan_date`,`update.last_scan_time`,`update.first_scan_time`,`update.severity_modification_type`,`update.severity_default_id`,`update.severity_id`,`update.severity`,`update.scan.uuid`,`update.scan.started_at`,`update.finding_id` and `update.plugin.risk_factor`,`update.scan.schedule_uuid` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `update.asset.uuid`,`update.asset.hostname` raw log field to `event.idm.read_only_udm.principal.asset.attribute.labels`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `open_ports.port`,`update.port.port`,`update.port.service` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.entity.entity.asset.product_object_id`, `event.idm.entity.entity.asset.asset_id`,`event.idm.read_only_udm.principal.asset.asset_id` : Newly mapped `payload_id` raw log field to `event.idm.entity.entity.asset.product_object_id`,`event.idm.entity.entity.asset.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- Added a conditional check before mapping `ASSET` to `event.idm.read_only_udm.metadata.entity_type`, if `has_entity_asset` is `true`.  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `payload.path` raw log field to `event.idm.read_only_udm.about.file.full_path`.  
\- `event.idm.read_only_udm.about.file.md5`: Newly mapped `payload.md5` raw log field to `event.idm.read_only_udm.about.file.md5`.   
2025-11-27 |  Enhancement:  
\- event.idm.read_only_udm.target.port: Newly mapped `port.port` raw log field to `event.idm.read_only_udm.target.port`.  
\- Enhanced parsing to handle the case where `scan.target` is `127.0.0.1`. When this occurs, `asset.ipv4` is mapped to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`. A label with key `loopback_address` and value `127.0.0.1` is also added to `event.idm.read_only_udm.additional.fields`.  
\- Modified the conditional logic to ensure the standard `scan.target` IP parsing does not run when `scan.target` is `127.0.0.1`.   
2025-10-29 |  Enhancement-  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `finding_id` and `plugin.version` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `last_fixed`, `plugin.unsupported_by_vendor`, `resurfaced_date` and `time_taken_to_fix` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Refactored parser logic for `scan.target` and `asset.last_scan_target`: Added logic to parse as an IP and map to `event.idm.read_only_udm.target.ip`, falling back to `event.idm.read_only_udm.target.hostname` if not an IP.   
2025-02-18 |  Enhancement-  
\- Added support to parse the unparsed fields.   
2025-01-08 |  Enhancement-  
\- Added UDM events support for the parser.   
2023-01-02 |  Enhancement-  
\- Mapped the field `ipv4s` to `event.idm.entity.entity.asset.ip`.  
\- Mapped the field `mac_addresses` to `event.idm.entity.entity.asset.mac`.  
\- Mapped the field `hostnames` to `event.idm.entity.entity.asset.hostname`.  
\- Mapped the field `id` to `event.idm.entity.entity.asset.product_object_id`.  
\- Mapped the field `fqdns` to `event.idm.entity.entity.asset.network_domain`.  
\- Mapped the field `netbios_names` to `event.idm.entity.entity.asset.network_domain`.  
\- Mapped the field `first_scan_time` to `vulnerabilities.scan_start_time`.  
\- Mapped the field `last_scan_time` to `vulnerabilities.scan_end_time`.  
\- Mapped the field `first_seen` to `vulnerabilities.first_found`.  
\- Mapped the field `last_seen` to `vulnerabilities.last_found`.  
\- Mapped the field `operating_systems.0` to `event.idm.entity.entity.asset.platform_software.platform_version`.  
\- Mapped the field `ssh_fingerprints.0` to `event.idm.entity.entity.asset.attribute.labels`.  
\- Mapped the field `system_types.0` to `event.idm.entity.entity.asset.attribute.labels`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
