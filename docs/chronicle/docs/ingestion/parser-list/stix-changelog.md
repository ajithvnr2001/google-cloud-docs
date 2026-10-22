---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stix-changelog/
title: Change log for STIX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:09.599696+00:00
---

# Change log for STIX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stix-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for STIX

Date | Changes  
---|---  
2026-09-11 |  Enhancement:  
\- `event.idm.entity.entity.url`: Newly mapped `object_value` (when `object_type` matches `url`), `object_x_misp_value` (when `object_x_misp_type` is `url`), and `object.x_misp_attributes.value` (when `object.x_misp_attributes.type` is `url`) raw log fields to `event.idm.entity.entity.url`.  
\- `event.idm.entity.metadata.creation_timestamp`: Newly mapped `object_created` raw log field to `event.idm.entity.metadata.creation_timestamp` when `start_time_present` is not `true` and `index` is greater than `0`.  
\- `event.idm.entity.metadata.interval.start_time`: Newly mapped `object_created` and `object_valid_from` raw log fields to `event.idm.entity.metadata.interval.start_time` when `start_time_present` is not `true` and `index` is greater than `0`.  
\- `event.idm.entity.entity.resource.attribute.labels`: Newly mapped `object.x_misp_attributes.type`, `object.x_misp_attributes.value`, `object.x_misp_attributes.uuid`, `object.x_misp_attributes.category`, `object.x_misp_attributes.object_relation`, `object.observed_data_refs`, `object.where_sighted_refs`, `object.sighting_of_ref`, `object.country`, `object.x_misp_name`, `object.x_misp_meta_category`, `object.issuer`, `object.subject`, `object.x_misp_text`, `object.serial_number`, `object.validity_not_after`, `object.validity_not_before`, `object.first_observed`, `object.last_observed`, `object.number_observed`, `next`, and `more` raw log fields to `event.idm.entity.entity.resource.attribute.labels`.   
2026-09-01 |  Enhancement:  
\- `event.idm.entity.resource.name`: Newly mapped `mutex_name` raw log field with `event.idm.entity.resource.name` UDM field  
\- `event.idm.metadata.entity_type`: If `created`, `valid_from` or `timestamp` is not empty, updated the value of `event.idm.metadata.entity_type` to IP_ADDRESS.  
\- `event.idm.metadata.entity_type`: If `created`, `valid_from` or `timestamp` is not empty, updated the value of `event.idm.metadata.entity_type` to URL.  
\- `event.idm.metadata.entity_type`: If `pattern` matches mutex:name, updated the value of `event.idm.metadata.entity_type` to MUTEX.  
\- `event.idm.entity.resource.resource_type`: If `pattern` matches mutex:name, updated the value of `event.idm.entity.resource.resource_type` to MUTEX.  
\- `event.idm.metadata.threat.category`: If `threat_detail` is empty and `entity_type` is IP_ADDRESS, URL or MUTEX, updated the value of `event.idm.metadata.threat.category` to NETWORK_SUSPICIOUS.   
2026-07-31 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.entity.entity.resource.attribute.labels`: Newly mapped `object.x_misp_type`, `object.x_misp_value` and `object.x_misp_category` raw log fields with `event.idm.read_only_udm.entity.resource.attribute.labels` UDM field.   
2026-07-09 |  Enhancement:  
\- `event.idm.entity.entity.resource.attribute.labels`: Newly mapped `extensions.extension-definition--6fa2481c-990d-4b26-a56f-333dddf87d34.extension_type`, `extensions.extension-definition--fc03abfc-3c69-4d9b-8a3b-eaf468e6aa26.extension_type` raw log fields with `event.idm.entity.entity.resource.attribute.labels` UDM field.   
2026-07-02 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.entity.entity.metadata.interval.start_time`: Removed mapping of `created` raw log field from `event.idm.entity.entity.metadata.interval.start_time` UDM field when `valid_from` is present as it is more accurate mapping.  
\- `event.idm.entity.entity.metadata.interval.start_time`: Mapped `created` raw log field with `event.idm.entity.entity.metadata.interval.start_time` UDM field when `valid_from` is not present.   
2026-06-26 |  Enhancement:  
-`event.idm.entity.entity.resource.type`: Removed mapping of `type` from `event.idm.entity.entity.resource.type ` UDM field since `event.idm.entity.entity.resource.type` UDM field is deprecated.  
-`event.idm.entity.entity.resource.resource_type`: Mapped `type` raw log field with `event.idm.entity.entity.resource.resource_type` UDM field.  
-`event.idm.entity.entity.resource.attribute.labels`: Newly mapped `object.source_ref`, `object.target_ref`, `object.type`, `object.value`, `object.id`, `object.pattern_type`, `object.name`, `object.spec_version`, `object.created`, `object.modified`, `object.valid_from`, `object.relationship_type`, `object.identity_class`, `object_created_by_ref`, `object.is_family`, `object.infrastructure_types`, `object.first_seen`, `object.resource_level`, `object.primary_motivation`, `object.aliases`, `object.threat_actor_types`, `object.roles`, `object.sophistication`, `object.published`, `object.contact_information`, `object.sectors`, `object.labels`, `object.report_types`, `object.object_refs`, `object.external_references.source_name`, `object.external_references.external_id`, `object.kill_chain_phases.phase_name`, `object.kill_chain_phases.kill_chain_name`, `external_references.source_name`, `external_references.external_id` , `type`, and `kill_chain_phases.phase_name` raw log fields with `event.idm.entity.entity.resource.attribute.labels` UDM field.  
-`event.idm.entity.entity.ip`: Newly mapped `object.value` and `object.pattern` raw log fields with `event.idm.entity.entity.ip` UDM field.  
-`event.idm.entity.entity.resource.name`: Newly mapped `object.name` raw log field with `event.idm.entity.entity.resource.name` UDM field.  
-`event.idm.entity.metadata.description`: Newly mapped `object.description` raw log field with `event.idm.entity.metadata.description` UDM field.  
-`event.idm.entity.metadata.creation_timestamp`: Newly mapped `object.created` raw log field with `event.idm.entity.metadata.creation_timestamp` UDM field.  
-`event.idm.entity.metadata.interval.start_time`: Newly mapped `object.created` and `object.valid_from` raw log fields with `event.idm.entity.metadata.interval.start_time` UDM field.  
-`event.idm.entity.entity.asset.system_last_update_time`: Newly mapped `object.modified` raw log field with `event.idm.entity.entity.asset.system_last_update_time` UDM field.  
-`event.idm.entity.threat.detection_fields`: Newly mapped `object.indicator_types` and `object.malware_types` raw log fields with `event.idm.entity.threat.detection_fields` UDM field.  
-`event.idm.entity.entity.hostname`: Newly mapped `object.external_references.source_name` and `external_references.source_name` raw log fields with `event.idm.entity.entity.hostname` UDM field.  
-`event.idm.entity.entity.user.userid`: Newly mapped `object.external_references.external_id` and `external_references.external_id` raw log fields with `event.idm.entity.entity.user.userid` UDM field.   
2026-04-17 |  Enhancement:  
\- `event.idm.entity.entity.hostname`: Newly mapped `dom` raw log field with `event.idm.entity.entity.hostname` UDM field when the pattern indicates a domain URL.  
\- `event.idm.entity.entity.url`: Newly mapped `name` raw log field with `event.idm.entity.entity.url` UDM field when `title` indicates a phishing URL and `name` contains URL data.  
\- `event.idm.entity.metadata.entity_type`: Updated the value to `DOMAIN_NAME` when the pattern indicates a domain URL, and to `URL` when `title` indicates a phishing URL and `name` contains URL data.  
\- `event.idm.entity.metadata.threat.category`: Updated the value of `event.idm.entity.metadata.threat.category` to PHISHING when `title` indicates phishing related data.  
\- `event.idm.entity.metadata.threat.confidence_details`: Updated the value of `event.idm.entity.metadata.threat.confidence_details` to `high_confidence from title` when `title` indicates a high confidence phishing URL, watchlist IP, or imminent threat IP.  
\- `event.idm.entity.metadata.threat.severity`: Updated the value of `event.idm.entity.metadata.threat.severity` to HIGH when `title` indicates a high confidence phishing URL, watchlist IP, or imminent threat IP.   
2026-02-20 |  Enhancement:  
\- `event.idm.entity.metadata.threat.severity`: Set the value of `event.idm.entity.metadata.threat.severity` to `MEDIUM` or `HIGH` when `x_severity` is `medium` or `high` respectively. If `x_severity` is neither `medium` nor `high`, the value is instead mapped to `event.idm.entity.metadata.threat.severity_details`.  
\- `event.idm.entity.entity.resource.attribute.labels`: Newly mapped `valid_from` (key: `valid_from`), `valid_until` (key: `valid_until`), and `pattern_version` (key: `pattern_version`) raw log fields with `event.idm.entity.entity.resource.attribute.labels` UDM field.   
2025-11-24 |  Enhancement:  
\- event.idm.entity.entity.asset.attribute.labels: Removed mapping of `labels` raw log field to `event.idm.entity.entity.asset.attribute.labels` UDM field as it is a duplicate mapping.  
\- event.idm.entity.entity.resource.attribute.labels: Removed mapping of `object_marking_refs` raw log field to `event.idm.entity.entity.resource.attribute.labels` UDM field as it is a duplicate mapping.  
\- event.idm.entity.entity.metadata.collected_timestamp: Removed mapping of `modified` raw log field from `event.idm.entity.metadata.collected_timestamp` UDM field inorder to introduce a more accurate mapping.  
\- event.idm.entity.entity.asset.system_last_update_time: Newly mapped `modified` raw log field to `event.idm.entity.entity.asset.system_last_update_time` UDM field.  
\- event.idm.entity.metadata.creation_timestamp: Newly mapped `created` raw log field to `event.idm.entity.metadata.creation_timestamp` UDM field.  
\- event.idm.entity.metadata.collected_timestamp : Newly mapped `timestamp` raw log field to `event.idm.entity.metadata.collected_timestamp` UDM field.  
\- event.idm.entity.entity.resource.attribute.labels: Newly mapped `pattern_type`, `lang` raw log fields to `event.idm.entity.entity.resource.attribute.labels` UDM field.   
2025-10-16 |  Enhancement:  
\- Modified JSON parsing logic to include `gsub` replacements to fix common issues in malformed JSON messages before re-attempting parsing.  
\- event.idm.entity.entity.asset.attribute.labels: Newly mapped `entrie.logText.labels` raw log field to `event.idm.entity.entity.asset.attribute.labels` UDM field.  
\- event.idm.entity.entity.asset.product_object_id: Newly mapped `entrie.logText.created_by_ref` raw log field to `event.idm.entity.entity.asset.product_object_id` UDM field.  
\- event.idm.entity.entity.asset.system_last_update_time: Newly mapped `entrie.logText.modified` raw log field to `event.idm.entity.entity.asset.system_last_update_time` UDM field.  
\- event.idm.entity.entity.hostname: Newly mapped `entrie.logText.pattern` raw log field to `event.idm.entity.entity.hostname` UDM field.  
\- event.idm.entity.entity.hostname: Newly mapped `pattern` raw log field to `event.idm.entity.entity.hostname` UDM field.  
\- event.idm.entity.entity.resource.attribute.labels: Newly mapped `entrie.logText.object_marking_refs` raw log field to `event.idm.entity.entity.resource.attribute.labels` UDM field.  
\- event.idm.entity.entity.resource.attribute.labels: Newly mapped `entrie.logText.x_ncsc_govt_nz_category` raw log field to `event.idm.entity.entity.resource.attribute.labels` UDM field.  
\- event.idm.entity.entity.resource.name: Newly mapped `entrie.logText.name` raw log field to `event.idm.entity.entity.resource.name` UDM field.  
\- event.idm.entity.entity.resource.type: Newly mapped `entrie.logText.type` raw log field to `event.idm.entity.entity.resource.type` UDM field.  
\- event.idm.entity.entity.user.userid: Newly mapped `customerId` raw log field to `event.idm.entity.entity.user.userid` UDM field.  
\- event.idm.entity.metadata.collected_timestamp: Newly mapped `entrie.logText.timestamp` raw log field to `event.idm.entity.metadata.collected_timestamp` UDM field.  
\- event.idm.entity.metadata.creation_timestamp: Newly mapped `entrie.logText.created` raw log field to `event.idm.entity.metadata.creation_timestamp` UDM field.  
\- event.idm.entity.metadata.description: Newly mapped `entrie.logText.title` raw log field to `event.idm.entity.metadata.description` UDM field.  
\- event.idm.entity.metadata.interval.end_time: Newly mapped `entrie.logText.valid_until` raw log field to `event.idm.entity.metadata.interval.end_time` UDM field.  
\- event.idm.entity.metadata.interval.start_time: Newly mapped `entrie.logText.valid_from` raw log field to `event.idm.entity.metadata.interval.start_time` UDM field.  
\- event.idm.entity.metadata.product_entity_id: Newly mapped `entrie.logText.id` raw log field to `event.idm.entity.metadata.product_entity_id` UDM field.   
2025-08-25 |  Enhancement:  
\- event.idm.entity.entity.url: Newly mapped `observable.object.properties.value.value` with `event.idm.entity.entity.url` when `observable.object.properties.type` is `URL`.  
\- event.idm.entity.entity.ip: Newly mapped `observable.object.properties.address_value.value` with `event.idm.entity.entity.ip` when `observable.object.properties.category` is `ipv4-addr`.  
\- event.idm.entity.entity.file: Newly mapped `observable.object.properties.hashes` with `event.idm.entity.entity.file` for `MD5`, `SHA1`, and `SHA256` types.  
\- event.idm.entity.metadata.product_version: Newly mapped `version` raw log field with event.idm.entity.entity.metadata.product_version UDM field.  
\- event.idm.entity.metadata.description: Newly mapped `description` raw log field with event.idm.entity.metadata.description UDM field.  
\- event.idm.entity.metadata.product_entity_id: Newly mapped `id` raw log field with event.idm.entity.metadata.product_entity_id UDM field.  
\- event.idm.entity.threat.detection_fields: Newly mapped `observable.keywords` raw log field with event.idm.entity.threat.detection_fields UDM field.  
\- event.idm.entity.entity.asset.attribute.labels: Newly mapped `observable.object.properties.value.condition`, `handling.controlled_structure`, `handling.marking_structures.color`, `related_indicators.related_indicators`, `related_indicators.scope`, `indicator_types`, `valid_time_positions` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM field.  
\- event.idm.entity.entity.asset.asset_id: Newly mapped `item.indicator.idref` raw log field with event.idm.entity.entity.asset.asset_id UDM field.   
2025-04-04 |  Enhancement:  
\- FQDN: Added support for the event `FQDN` and relevant corresponding raw log fields.  
\- event.idm.entity.metadata.threat.detection_fields: Newly mapped `observable.object.properties.custom_properties` raw log field with `event.idm.entity.metadata.threat.detection_fields` UDM field.  
\- event.idm.entity.entity.resource.attribute.labels: Newly mapped `observable.indicator_types` to `event.idm.entityentity.resource.attribute.labels` UDM field.  
\- event.ioc.domain_and_ports.domain: Newly mapped `observable.object.properties.value` raw log field with `event.ioc.domain_and_ports.domain` UDM field, when `observable.object.properties.name` is `FQDN`.   
2025-03-06 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-11-07 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.   
2024-10-15 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- Removed duplicate code.  
\- Renamed field `extension-definition--322b8f77-262a-4cb8-a915-1e441e00329b` to `mitre-extension-definition` and mapped `mitre-extension-definition.extension_type` to `entity.resource.attribute.labels.value`.  
\- Renamed field `extension-definition--f93e2c80-4231-4f9a-af8b-95c9bd566a82` to `sco-extension-definition` and mapped `sco-extension-definition.extension_type` to `entity.resource.attribute.labels.value`.   
2024-09-25 |  Enhancement:  
\- Mapped `x_ctix_confidence_score` to `threat_detail.confidence_score`.   
2024-09-20 |  Enhancement:  
\- Added drop statement to drop unsupported logs.  
\- Mapped `modified` to `timestamp`.  
\- Mapped `valid_from` to `entity_event.metadata.interval.start_time`.  
\- Added support for logs with the `pattern` value `hostname:value`.  
\- If the `entity_type` field is not equal to `File,` then map the `valid_until` field to the value of `entity_event.metadata.interval.end_time.`  
2024-09-19 |  Enhancement:  
\- Added new Grok patterns to parse the field `pattern`.  
\- Mapped `valid_until` to `metadata.interval.end_time`.   
2024-09-18 |  Enhancement:  
\- Added support for logs with the `pattern` value `ipv4:addr`.  
\- Added support for logs with the `main_observable_type` value `Hostname`.  
\- Mapped `confidence` to `threat_detail.confidence_score`.  
\- When `main_observable_type` is `StixFile`, then mapped `name` to `entity.entity.file.full_path`.   
2024-03-06 |  Enhancement:  
\- Added support for logs with the `type` value `indicator`.   
2024-02-07 |  Enhancement:  
\- Added support for entity field mappings for new set of ingested logs.  
\- Mapped `description` to `threat_detail.description`.  
\- Mapped `external_references.0.source_name` to `entity_event.entity.hostname`.  
\- Mapped fields present in nested JSON field `extensions.extension-definition` to `threat_detail.detection_fields`.   
2023-11-08 |  Enhancement:  
\- Added support for entity field mappings for new set of ingested logs.  
\- Mapped `entity_type` to `IP_ADDRESS` and `entity_event.entity.ip` to `ip` for `pattern` = `ipv4-addr`.  
\- Mapped `entity_type` to `USER` and `entity_event.entity.user.email_addresses` to `mail` for `pattern` = `email-addr`.  
\- Mapped `entity_type` to `FILE` and `entity_event.entity.file.sha256` to `sha256val`,`entity_event.entity.file.md5` to `MD5_val` and `entity_event.entity.file.sha1` to `sha1_val` for `pattern` = `file:hashes`.  
\- Mapped `entity_type` to `DOMAIN_NAME` and `entity_event.entity.hostname` to `dom` for `pattern` = `domain-name`.  
\- Mapped `entity_type` to `URL` and `entity_event.entity.url` to `url_val` for `pattern` = `url:value`.   
2023-03-24 |  Enhancement: Added support for entity field mappings.   
2022-12-12 |  Bug Fix - Mapped timestamp to `metadata.event_timestamp`.  
\- Added Grok patterns to identify the type of log.  
\- Added type specific blocks like `md5`, `sha1`, `sha256`, `domain-name`, `mal_file_name` etc.   
2022-12-03 |  Bug Fix - Parsed unparsed logs:  
\- Added Grok patterns to identify the type of log.  
\- Added type specific blocks like `mal_md5`, `mal_url` etc.  
\- Parsed `SHA-512` as `security_result.detection_fields` due to large size.   
2022-11-27 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
