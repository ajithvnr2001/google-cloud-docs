---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/misp-ioc-changelog/
title: Change log for MISP_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:41:21.846906+00:00
---

# Change log for MISP_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/misp-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MISP_IOC

Date | Changes  
---|---  
2026-07-16 |  Enhancement:  
\- `event.idm.entity.entity.file.names`: Newly mapped `Attribute.Event.value` raw log fields with `event.idm.entity.entity.file.names` UDM field when `log_type` is `email-attachment`.   
2026-07-02 |  Enhancement:  
\- `event.idm.entity.metadata.threat.description`: Newly mapped `Attribute.Event.info` raw log field with `event.idm.entity.metadata.threat.description` UDM field.  
\- `event.idm.entity.metadata.threat.detection_fields`: Newly mapped `Attribute.Event.ThreatLevel.name`, `Attribute.Event.ThreatLevel.id`, `Attribute.Event.Orgc.uuid`, `Attribute.Event.Orgc.name`, `Attribute.Event.Org.uuid`, `Attribute.Event.Org.name`, `Attribute.Event.publish_timestamp`, `Attribute.Event.timestamp`, `Attribute.Event.date`, `Attribute.Event.analysis`, `Attribute.Event.threat_level_id`, `Attribute.Event.user_id`, `Attribute.Event.orgc_id`, `Attribute.Event.org_id`, `Attribute.type`, and `log_source` raw log fields with `event.idm.entity.metadata.threat.detection_fields` UDM field.  
\- `event.idm.entity.entity.asset.product_object_id`: Newly mapped `Attribute.Event.uuid` raw log field with `event.idm.entity.entity.asset.product_object_id` UDM field.  
\- `event.idm.entity.metadata.entity_type`: Added conditional logic to set the field to `USER` when user email details are present and the raw log field `log_type` is `email`.   
2026-06-22 |  Enhancement:  
\- `event.idm.entity.entity.user.email_addresses`: Newly mapped `value` raw log field with `event.idm.entity.entity.user.email_addresses` UDM field when `type` is `threat-actor`.  
\- `event.idm.entity.entity.hostname`: Newly mapped `host` raw log field with `event.idm.entity.entity.hostname` UDM field when `type` is `hostname|port` or `hostname`.  
\- `event.idm.entity.entity.port`: Newly mapped `port` raw log field with `event.idm.entity.entity.port` UDM field when `type` is `hostname|port`.  
\- `event.idm.entity.metadata.entity_type`: Newly set `event.idm.entity.metadata.entity_type` to `DOMAIN_NAME` when `type` is `hostname|port`.   
2026-01-22 |  Enhancement:  
\- Added a new support to parse the new format of logs.  
\- event.idm.read_only_udm.entity.metadata.collected_timestamp: Newly mapped from `column19` raw log field with event.idm.read_only_udm.entity.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.entity.additional.fields: Newly mapped from `attributes.log_file_name` raw log field with event.idm.read_only_udm.entity.additional.fields UDM field.  
\- event.idm.read_only_udm.entity.additional.fields: Newly mapped from `attributes.log_type` raw log field with event.idm.read_only_udm.entity.additional.fields UDM field.  
\- event.idm.read_only_udm.entity.entity.labels: Newly mapped `column2`, `column7`, `column11`, `column12`, `column14`, `column16`, `column17`, `column18` raw log fields with event.idm.read_only_udm.entity.entity.labels UDM field.   
2026-01-07 |  Enhancement:  
\- event.idm.entity.entity.labels: Newly mapped `column9`, `column11`, `column12`, `column13` raw log field(s) with `event.idm.read_only_udm.entity.labels` UDM field. These are conditionally mapped to labels including `actor_name`, `country`, `misp_galaxy_tag`, `tlp`, and `vulnerability`.  
\- event.idm.entity.metadata.threat.threat_feed_name: Newly mapped the value to `MISP` when the `event_source_org` field is not available.  
\- event.idm.entity.metadata.interval.start_time: Converted type to UNIX timestamp. If `ts1` is empty, non-numeric, or zero, it is set to 1 before conversion.  
\- Added conditional logic to handle multiple CSV formats based on the content of column11 and column12.  
\- Added a conditional check for ts1 to determine whether to use it or @timestamp for date parsing.  
\- event.idm.entity.entity.labels: The `intelligence_source` field is now conditionally mapped from either `column11` or `column15` depending on the log format.   
2025-12-24 |  Enhancement:  
\- `event.idm.entity.metadata.threat.detection_fields`: Newly mapped `name`, `comment`,`Attribute.last_seen`,`first_seen`, `Org.id`, `Org.uuid`, `Org.local`, `Orgc.id`, `Orgc.uuid`, `Orgc.local`, `Attribute.distribution`, `Attribute.interval_start`, `Attribute.interval_end`, `Attribute.sharing_group_id`, `Attribute.disable_correlation`, `Attribute.object_id`, `Attribute.object_relation`, `log.id`, `log.event_id`, `log.distribution`, `interval_start`, `interval_end`, `template_uuid`, `meta-category`, `log.sharing_group_id`, `log.disable_correlation`, `log.object_id`, `log.object_relation`, `Tag` raw log field(s) with `event.idm.entity.metadata.threat.detection_fields` UDM field.  
\- Added conditional check for `log_type` to handle `x509-fingerprint-sha256` to set `event.idm.entity.metadata.entity_type` to `FILE` and map `Attribute.value` to `event.idm.entity.entity.file.sha256` UDM field.  
\- `event.idm.entity.entity.hostname`: Newly mapped `Attribute.value` raw log field(s) with `event.idm.entity.entity.hostname` UDM field when log_type is `target-org`.  
\- `event.idm.entity.metadata.entity_type`: Set the `event.idm.entity.metadata.entity_type` to `DOMAIN_NAME` when `log_type` is `target-org`.  
\- Added conditional check for `log_type` to handle [`link`,`URL embedded in the email`] to set `event.idm.entity.metadata.entity_type` to `URL` and map `Attribute.value` to `event.idm.entity.entity.url` UDM field.  
\- `event.idm.entity.entity.hostname`: Newly mapped `Orgc.name` raw log field(s) with `event.idm.entity.entity.hostname` UDM field when log_type is `text`.  
\- `event.idm.entity.metadata.entity_type`: Set the `event.idm.entity.metadata.entity_type` to `DOMAIN_NAME` when `log_type` is `text`.  
\- Removed `text` from the log_type list for which events are dropped and added a conditional check for `log_type` to handle `text` to set `event.idm.entity.metadata.entity_type` to `DOMAIN_NAME` and map `Orgc.name` to `event.idm.entity.entity.hostname` UDM field.  
\- Added conditional check for `log_type` to handle `email-dst` to set `event.idm.entity.metadata.entity_type` to `USER` and map `Attribute.value` to `event.idm.entity.entity.user.email_addresses` UDM field.  
\- Converted `Attribute.id` ,`Attribute.event_id`, `log.id`,`log.event_id`, `Attribute.timestamp`,`log.timestamp` to string before its mapping.  
\- Removed `==` and used `=~` operator for logtype `sha256` to handle logs where `type` contains `sha256`.  
\- Added a null conditional check for `log.comment` field before mapping it to `event.idm.entity.metadata.threat.detection_fields` to prevent populating null values.   
2025-10-06 |  Enhancement:  
\- event.idm.entity.entity.port: Newly mapped `port` field with `event.idm.entity.entity.port` UDM field.  
\- event.idm.entity.entity.labels: Newly mapped `column2` , `column10` , `column15` , `column22` , `column20` field with `event.idm.entity.entity.labels` UDM field.   
2025-06-26 |  Enhancement:  
\- Merged the output only when the `event.idm.entity.metadata.entity_type` is set.  
\- event.idm.entity.metadata.product_entity_id: Newly mapped `log.uuid` raw log field with `event.idm.entity.metadata.product_entity_id` UDM field.  
\- event.idm.entity.metadata.description: Newly mapped `Event.info` raw log field with `event.idm.entity.metadata.description` UDM field.  
\- event.idm.entity.metadata.interval.start_time: Newly mapped `entity_first_seen` raw log field with `event.idm.entity.metadata.interval.start_time` UDM field.  
\- event.idm.entity.metadata.threat.category_details: Newly mapped `log.category` raw log field with `event.idm.entity.metadata.threat.category_details` UDM field.  
\- event.idm.entity.metadata.threat.summary: Newly mapped `log.comment` raw log field with `event.idm.entity.metadata.threat.summary` UDM field.  
\- event.idm.entity.entity.labels: Newly mapped `Event.threat_level_id` and `event_creator_email` raw log fields with `event.idm.entity.entity.labels` UDM field.  
\- event.idm.entity.entity.file.full_path:  
Newly mapped `log.comment` raw log field with `event.idm.entity.entity.file.full_path` UDM field, if the type is md5, sha1, sha256, attachment or email-attachment and `log.comment` is not Artifacts dropped.  
Newly mapped log.value raw log field with `event.idm.entity.entity.file.full_path` UDM field, if the type is filename.  
Newly mapped file_name raw log field with `event.idm.entity.entity.file.full_path` UDM field, if the type is filename|sha256.  
\- event.idm.entity.entity.file.sha256:  
Newly mapped `log.value` raw log field with `event.idm.entity.entity.file.sha256` UDM field, if the type is sha256.  
Newly mapped `file_sha256` raw log field with `event.idm.entity.entity.file.sha256` UDM field, if the type is filename|sha256.  
\- event.idm.entity.entity.file.sha1: Newly mapped `log.value` raw log field with `event.idm.entity.entity.file.sha1` UDM field, if the type is sha1.  
\- event.idm.entity.entity.file.md5: Newly mapped `log.value` raw log field with `event.idm.entity.entity.file.md5` UDM field, if the type is md5.  
\- event.idm.entity.entity.hostname:  
Newly mapped `log.value` raw log field with `event.idm.entity.entity.hostname` UDM field, if the type is domain or hostname.  
\- Mapped `Attribute.value` to `event.idm.entity.entity.hostname`, when log.type is hostname.  
\- event.idm.entity.entity.ip: Newly mapped `ip` raw log field with `event.idm.entity.entity.ip` UDM field, if the type is ip-dst|port, ip-dst or ip-src.  
\- event.idm.entity.entity.port: Newly mapped `port` raw log field with `event.idm.entity.entity.port` UDM field, if the type is ip-dst|port.  
\- event.idm.entity.entity.resource.name: Newly mapped `log.value` raw log field with `event.idm.entity.entity.resource.name` UDM field, if the type is mutex.  
\- event.idm.entity.entity.registry.registry_key: Newly mapped `log.value` raw log field with `event.idm.entity.entity.registry.registry_key` UDM field, if the type is regkey.  
\- event.idm.entity.entity.user.email_addresses: Newly mapped `log.value` raw log field with `event.idm.entity.entity.user.email_addresses` UDM field, if the type is threat-actor, email-src, email or email-subject.  
\- event.idm.entity.entity.user.user_display_name: Newly mapped `log.uuid` raw log field with `event.idm.entity.entity.user.user_display_name` UDM field, if the type is email or `email-subject`.  
\- event.idm.entity.entity.url: Newly mapped `log.value` raw log field with `event.idm.entity.entity.url` UDM field, if the `type` is `uri`, `url`, `URL` embedded in the email or link.  
\- event.idm.entity.metadata.entity_type: Set the `event.idm.entity.metadata.entity_type` based on the `log.type` field.  
\- event.idm.entity.metadata.threat.detection_fields: Newly mapped `log.id`, `log.event_id`, `log.to_ids`, `log.timestamp`, `log.comment`, `log.deleted`, `log.first_seen`, `Org.name`, `Feed.publish`, `published` and `Event.Tag` raw log fields with `event.idm.entity.metadata.threat.detection_fields` UDM field.   
2025-04-10 |  Enhancement:  
\- Merged the output only when the `event.idm.entity.metadata.entity_type` is set.  
\- `syslog+json`: Added support for `syslog+json` format.  
\- event.idm.entity.metadata.entity_timestamp: Newly mapped `timestamp` raw log field with `event.idm.entity.metadata.entity_timestamp` UDM field.  
\- event.idm.entity.metadata.interval.start_time: Newly mapped `first_seen` raw log field with "event.idm.entity.metadata.interval.start_time` UDM field.  
\- event.idm.entity.metadata.interval.end_time: Newly mapped `last_seen` raw log field with "event.idm.entity.metadata.interval.end_time` UDM field.  
\- event.idm.entity.entity.file.sha1: Newly mapped `indicator` raw log field with `event.idm.entity.entity.file.sha1` UDM field, if the `type` is `sha1`.  
\- event.idm.entity.entity.file.md5: Newly mapped `indicator` raw log field with `event.idm.entity.entity.file.md5` UDM field, if the `type` is `md5`.  
\- event.idm.entity.entity.file.sha256: Newly mapped `indicator` raw log field with `event.idm.entity.entity.file.sha256` UDM field, if the `type` is `sha256`.  
\- event.idm.entity.entity.hostname: Newly mapped `indicator` raw log field with `event.idm.entity.entity.hostname` UDM field, if the `type` is `domain`.  
\- event.idm.entity.entity.ip: Newly mapped `indicator` raw log field with `event.idm.entity.entity.ip` UDM field, if the `type` is `IPv4`.  
\- event.idm.entity.entity.url: Newly mapped `indicator` raw log field with `event.idm.entity.entity.url` UDM field, if the `type` is `url`.  
\- event.idm.entity.metadata.threat.confidence_score: Newly mapped `confidence` raw log field with `event.idm.entity.metadata.threat.confidence_score` UDM field.  
\- event.idm.entity.metadata.threat.summary: Newly mapped `stix_package_title` raw log field with `event.idm.entity.metadata.threat.summary` UDM field.  
\- event.idm.entity.metadata.threat.category_details: Newly mapped `type` raw log field with `event.idm.entity.metadata.threat.category_details` UDM field.  
\- Set the `event.idm.entity.metadata.entity_type` to `USER` only when `event.idm.entity.entity.user.email_addresses` is present.   
2025-03-20 |  Enhancement:  
\- Added gsub to parse array format of logs.  
\- Mapped `confidence` to `threat_.confidence_details`.  
\- Mapped `value` to `entity.entity.url` when `type` is `url`.  
\- Mapped `value` to `entity.entity.hostname` when `type` is `domain` or `domiain`.  
\- Mapped `value` to `entity.entity.ip` when `type` is `ip`.  
\- Mapped `value` to `entity.entity.file.sha256` when `type` is `sha256`.  
\- Mapped `value` to `entity.entity.file.md5` when `type` is `md5`.  
\- Mapped `value` to `entity.entity.file.sha1` when `type` is `hash`.  
\- Set `entity.metadata.entity_type` based on the `type` field.  
\- Added `on_error` to `log.comment` mapping to handle the error when `log.comment` is not present in the log.   
2025-01-29 |  Enhancement:  
\- Added support to parse new format of JSON unparsed logs.   
2024-11-20 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-09-05 |  Enhancement:  
\- Added support to parse unparsed logs.   
2023-09-26 |  Enhancement:  
\- Mapped `published`, `Feed.publish`, `Org.name`, `Attribute.id`, `Attribute.event_id`, `Attribute.to_ids`, `Attribute.timestamp`, `Attribute.comment`, `Attribute.deleted`, `Attribute.first_seen`, all `tag.names` to `threat.detection_fields`.   
2023-08-17 |  Bug-Fix :  
\- Added a condition to perform a `gsub` operation, that removes extra back-slash, only when log is not JSON.   
2023-07-20 |  Bug-Fix :  
\- Changed `metadata.entity_type` to `MUTEX` when log is of type mutex.   
2023-07-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
