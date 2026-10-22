---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/darktrace-changelog/
title: Change log for DARKTRACE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:48.509736+00:00
---

# Change log for DARKTRACE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/darktrace-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DARKTRACE

Date | Changes  
---|---  
2026-09-02 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `model.tags`, `triggeredComponents.triggeredFilters.trigger.value` when `triggeredComponents.triggeredFilters.filterType` is `Model tags`, and `model.category` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `model.logic.data.cid`, `model.logic.data.weight`, `model.logic.targetScore`, `model.behaviour`, `model.compliance`, `model.actions.antigena.threshold`, `model.actions.antigena.duration`, and `model.actions.antigena.network_actions` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `model.logic.type` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `model.logic.version` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device.aghuuid`, `triggeredComponents.cbid`, `triggeredComponents.chid`, `device.aghasn`, `model.interval`, `model.sequenced`, `model.active`, `model.readOnly`, `model.modified`, `model.sharedEndpoints`, `model.version`, and `commentCount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `device.interfaces.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `device.interfaces.ips.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dest` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `device.aghcountry` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `creationTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-07-22 |  Enhancement:  
\- Added a grok pattern to parse new format of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `header`, `Relation between endpoints`, `Source of username`, `ASN`, `Connection count`, `Transport protocol`, `Application protocol`, `Time_start`, `Time_end`, `Endpoints include`, `rarity_start`, `rarity_end`, `Total uids`, `relatedUids`, `children`, `groupingIds`, `start`, `end`, `breachDevices_identifier`, `Time observed`, `Range of IP rarities`, `ip_addresses.hostname` and `JA3 client hashes` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `Uploaded` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `Downloaded` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Destination port`, `breachDevices.did` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `Username observed prior to activity`, `breachDevices.sid`, `breachDevices.hostname` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.ip`: Newly mapped `ip_addresses.ip` raw log field with `event.idm.read_only_udm.about.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Suspicious properties`, `mitreTactics`, `relatedBreaches.modelName`, `relatedBreaches.pbid`, `relatedBreaches.threatScore`, `relatedBreaches.timestamp`, `attackPhases`, `acknowledged`, `pinned`, `groupByActivity`, `userTriggered`, `externalTriggered`, `groupCategory` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `details.0.0.contents.0.values.0.hostname`, `breachDevices.hostname` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `details.0.0.contents.0.values.0.ip`, `breachDevices.ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `breachDevices.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- Added conditional check for category matching `(?i)Compliance` to set `_sec_result.severity` to `MEDIUM`.   
2025-12-02 |  Enhancement:  
\- Updated the condition for `MEDIUM_PRIORITY` from >= 0.5 and <= 0.79 to >= 0.5 and < 0.8.  
\- Updated the condition for `LOW_PRIORITY` from >= 0 and <= 0.49 to >= 0 and < 0.5.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `percentScore` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `device.credentials` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.   
2025-11-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `iris-event-type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `inhibitor` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `inhibitor` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `inhibitor` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `device.os` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.asset.type`: Newly mapped `device.typename` raw log field with `event.idm.read_only_udm.principal.asset.type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device.ossource`, `model.tags` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `inhibitor` is parsed successfully, updated to `NETWORK_CONNECTION`.  
\- The logic for handling `model.phid`, `model.throttle`, and `model.delay` has been updated to use temporary local variables before populating UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `codeid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action_family` is added to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `CREATE_NEEDSCONFIRMATION`, then set `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `inhibitor` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- The logic for processing `model.tags` has been refactored to simplify the loop.   
2025-10-14 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_pid`: Newly mapped `model.phid` raw log field to `event.idm.read_only_udm.principal.process.parent_pid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `device.ossource` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `model.throttle`, `device.os`,`device.tags`,`model.delay`,`model.tags`,`model.actions`,`model.activeTimes`,`mitreTechniquestactics.tactics`,`pbid` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-13 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `darktrace_host` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `device_hostname` field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.mac, event.idm.read_only_udm.principal.asset.mac: Newly mapped `device_mac` field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- event.idm.read_only_udm.principal.resource.attribute.labels : Newly mapped `device.vendor` field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `pbid`,`model.sequenced`,`model.active`,`model.created.by` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields : Newly mapped `model.priority`,`model.compliance` fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added gsub on `model_description` fields to remove `\\\n`.   
2025-08-10 |  Enhancement:  
\- Modified the logic to determine `event.idm.read_only_udm.security_result.priority` based on the `score` field.  
\- event.idm.read_only_udm.principal.process.parent_pid: Newly mapped `model.phid` raw log field to event.idm.read_only_udm.principal.process.parent_pid.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `model.logic.data.cid`, `model.logic.data.weight`, `model.logic.targetScore`, `model.actions.antigena.duration`, and `model.actions.antigena.threshold` raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `model.logic.type` raw log field to event.idm.read_only_udm.security_result.rule_type.  
\- event.idm.read_only_udm.security_result.rule_version: Newly mapped `model.logic.version` raw log field to event.idm.read_only_udm.security_result.rule_version.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `model.throttle`, `model.sharedEndpoints`, `model.actions`, `model.actions.antigena.confirm`, `model.behaviour`, and `model.version` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `model.actions.antigena.action` raw log field to event.idm.read_only_udm.security_result.action_details.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `model.modified` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `model.category` raw log field to event.idm.read_only_udm.security_result.category_details.   
2025-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `triggeredComponents.triggeredFilters.trigger.value`, `triggeredComponents.triggeredFilters.cfid`, `triggeredComponents.triggeredFilters.filterType`, `triggeredComponents.triggeredFilters.trigger.tag.tid`, `triggeredComponents.triggeredFilters.trigger.tag.thid`, `triggeredComponents.triggeredFilters.trigger.tag.restricted`, `triggeredComponents.triggeredFilters.trigger.tag.data.color`, `triggeredComponents.triggeredFilters.trigger.tag.data.auto`, `triggeredComponents.triggeredFilters.trigger.isReferenced` raw fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `triggeredComponents.triggeredFilters.trigger.value` raw field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `triggeredComponents.triggeredFilters.filterType` is `Destination IP`.   
2025-05-30 |  Enhancement:  
\- Added declaration for fields in grok overwrites and initial mapping.   
2025-05-20 |  Enhancement:  
\- Added grok pattern for new log format.  
\- Updated grok pattern for `dvc` raw field to parse IP correctly.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly Mapped `issue_code` raw field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly Mapped `tags` raw field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly Mapped `severity` raw field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly Mapped `mitrld` raw field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly Mapped `DevicemacAddress` raw field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `externalId` raw field from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly Mapped `externalId` raw field with `event.idm.read_only_udm.security_result.threat_id` UDM field.   
2025-05-19 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `host_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- Replaced `event.idm.read_only_udm.intermediary` with `intermediary`.   
2025-05-09 |  Enhancement:  
\- Added a gsub to replace `\r\n` with ` ` in `message` field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Removed mapping of `dvc` from `event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip` UDM field and mapped `dvc_ip` instead.  
\- Added a `on_error` check before mapping `dvc_ip` to `principal_ip` raw log field.  
\- Added a Grok pattern to extract `device_ip2_` from `device_ip2` raw log field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Removed mapping of `ip.ip` from `event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip` UDM field and mapped `device_ip2_` instead.  
\- Added a `on_error` check before mapping `device_ip2_` to `principal_ip` raw log field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques: Newly mapped `technique_data` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics: Newly mapped `tactics_data` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.   
2025-04-28 |  Enhancement:  
\- Added the Grok patterns to parse the new pattern of logs with SYSLOG format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` and `timestamp` fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Set `event.idm.read_only_udm.security_result.severity` UDM field to `INFORMATIONAL` if the value of `severity` field is 0, 1 or 2.  
\- Set `event.idm.read_only_udm.security_result.severity` UDM field to `LOW` if the value of `severity` field is 3 or 4.  
\- Set `event.idm.read_only_udm.security_result.severity` UDM field to `MEDIUM` if the value of `severity` field is 5 or 6.  
\- Set `event.idm.read_only_udm.security_result.severity` UDM field to `HIGH` if the value of `severity` field is 7 or 8 and set `event.idm.is_alert` and `event.idm.is_significant` UDM fields to `true`.  
\- Set `event.idm.read_only_udm.security_result.severity` UDM field to `CRITICAL` if the value of `severity` field is 9 or 10 and set `event.idm.is_alert` and `event.idm.is_significant` UDM fields to `true`.   
2025-04-22 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity: Newly mapped severity raw log field with event.idm.read_only_udm.security_result.severity UDM field.   
2025-04-08 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `model_uuid` raw field from `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Mapped `model_uuid` raw field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly Mapped `version` raw field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly Mapped `vendor` raw field to `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly Mapped `product` raw field to `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly Mapped `deviceExternalId` raw field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.labels` : Newly Mapped `cs3` raw field to `event.idm.read_only_udm.principal.labels` UDM field.  
\- Added a Grok pattern to support new `syslog` format.   
2025-03-12 |  Enhancement:  
\- When `model.created.userid` is present, then mapped `model.created.userid` to `principal.user.userid` and `model.uuid` to `principal.user.product_object_id`.  
\- Mapped `model.edited.userid` to `additional.fields` with key as `model.edited.by`.   
2025-01-16 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-11-21 |  Enhancement:  
\- Corrected spelling of `email_direciton_error` to `email_direction_error`.   
2024-10-30 |  Enhancement:  
\- Added a Grok pattern to parse the SYSLOG+JSON logs.   
2024-10-25 |  Enhancement:  
\- Mapped `direction` to `network.direction` for `INBOUND,` `OUTBOUND,` or `BROADCAST.` Otherwise, mapped it to `additional.fields`.   
2024-10-24 |  Enhancement:  
\- Added a new Grok pattern to parse new JSON logs.   
2024-10-08 |  Enhancement:  
\- changed the `event_type` from `USER_UNCATEGORIZED` to `EMAIL_UNCATEGORIZED` when `from` field is present.  
\- `from` mapped to `newtwork.email.from` & `principal.user.email_addresses`.  
\- `recipients` mapped to `newtwork.email.to` & `target.user.email_addresses`.  
\- changed `subject` mapping from `metadata.description` to `newtwork.email.subject`.  
\- changed `message_id` mapping from `additional.fields` to `newtwork.email.mail_id`.  
\- changed `uuid` mapping from `principal.user.userid` to `metadata.product_log_id`.   
2024-10-07 |  Enhancement:  
\- Mapped `filterType` under `triggeredFilters` to `additional.fields`.  
\- When `trigger.value` is having non IP value, then mapped `trigger.value` under `triggeredFilters` to `additional.fields`.   
2024-09-25 |  Enhancement:  
\- Mapped `description` to `metadata.description`.  
\- Mapped `score` field to `security_result.priority_details`.   
2024-09-19 |  Enhancement:  
\- Mapped all fields under `triggeredFilters` to `additional.fields`.   
2024-09-09 |  Enhancement:  
\- Mapped `uuid` to `principal.user.userid`.  
\- Mapped `from` to `principal.user.email_addresses`.  
\- Mapped `subject` to `metadata.description`.  
\- Mapped `anomaly_score`, `tags`, `link_hosts`, and `message_id` to `additional.fields`.  
\- Mapped `recipients` to `observer.user.email_addresses`.  
\- Mapped `attachment_sha1s` and `attachment_sha256s` to `security_result.detection_fields`.   
2024-08-29 |  Enhancement:  
\- Mapped `hostname` field to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `label` field to `security_result.attribute.label`.  
\- Mapped `ip_address` field to `principal.ip` and `principal.asset.ip`.  
\- Mapped `priority` field to `security_result.priority_details`.  
\- Mapped `priority_level` field to `security_result.priority`.  
\- Mapped `alert_name` field to `security_result.rule_name`.  
\- Mapped `message` field to `security_result.description`.  
\- Mapped `url` field to `security_result.url_back_to_product`.   
2024-08-06 |  Enhancement:  
\- When `filterType` is `Destination IP`, then mapped `triggeredFilter.trigger.value` to `target.ip`.  
\- When principal and target machine data is absent but user data is available then mapped `metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-04-05 |  Bug-Fix:  
\- Changed mapping for `model.name` and `model.now.name` from `principal.user.user_display_name` to `metadata.product_event_type`.  
\- When principal machine data and target machine data are present, then changed mapping for `metadata.event_type` from `GENERIC_EVENT` or `USER_UNCATEGORIZED` to `NETWORK_CONNECTION`, else mapping it to `USER_RESOURCE_ACCESS`.   
2023-12-20 |  Bug-Fix: Fixed the flaky results for the mapping `sec_result.about.resource.attribute.labels` where `key` is `details`.   
2023-11-20 |  Enhancement, Bug-Fix:  
\- Parsed subfields in the `message` field of the raw log.  
\- Mapped `uuid` to `principal.user.userid` and set `metadata.event_type` to `USER_UNCATEGORIZED` when `uuid` is present.  
\- Mapped `direction` to `network.direction`.  
\- Mapped `from` to `network.email.from`.  
\- Mapped `subject` to `network.email.subject`.  
\- Mapped `attachment_sha1s`, `attachment_sha256s`, `recipients`, `link_hosts`, `tags`, `actions`, `anomaly_score`, `message_id` to `security_result.detection_fields`.  
\- Mapped `url` to `security_result.url_back_to_product`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `hostname` to `principal.hostname`.  
\- Added `on_error` to a JSON block to parse unparsed set of JSON logs.  
\- Mapped `model.pid` to `principal.process.pid`.  
\- Mapped `model.uuid` to `principal.user.userid`.  
\- Mapped `model.name` to `principal.user.user_display_name`.  
\- Mapped `breachUrl` to `security_result.url_back_to_product`.  
\- Mapped `device.typelabel`, `device.sid`, `device.typename` to `principal.resource.attribute.labels`.  
\- Mapped `device.ip` to `principal.ip`.  
\- Mapped `device.ips.0.subnet` to `additional_fields`.  
\- Mapped `device.did` to `principal.asset.asset_id`.  
\- Mapped `device.customFields.DT-AUTO.macaddress` to `principal.mac`.  
\- Mapped `device.firstSeen` to `principal.asset.first_seen_time`.  
\- Mapped `device.device.lastSeen` to `principal.asset.last_seen_time`.  
\- Mapped `mitreTechniques` to `security_result.attack_details.techniques`.   
2023-09-26 |  Enhancement:  
\- Adjusted the parser to support nested JSON.  
\- Fixed the parser to handle special characters in the log.  
\- Mapped the fields of new log type.   
2023-08-29 |  Enhancement:  
\- Mapped `details` to `sec_result.about.resource.attribute.labels`.  
\- Mapped `principal_port_no` to `principal.port`.  
\- Mapped `ip_protocol` to `network.ip_protocol`.  
\- Mapped `location` to `principal.location.country_or_region`.  
\- Mapped `target_host` to `target.hostname`.  
\- Mapped `target_ip` to `target.ip`.  
\- Mapped `source_ip` to `principal.ip`.  
\- Mapped `source_port` to `principal.port`.  
\- Mapped `dest_ip` to `target.ip`.  
\- Mapped `dest_port` to `target.port`.  
\- Mapped `@host` to `principal.hostname`.  
\- Mapped `uid` to `principal.user.userid`.  
\- Mapped `note` to `principal.application`.  
\- Mapped `@type` to `sec_result.about.resource.attribute.labels`.  
\- Mapped `opcode` to `sec_result.about.resource.attribute.labels`.  
\- Mapped `trans_id` to `sec_result.about.resource.attribute.labels`.  
\- Mapped `query_class` to `sec_result.about.resource.attribute.labels`.   
2023-07-14 |  Enhancement:  
\- Mapped `dvchost` to `principal.hostname`.  
\- Mapped `deviceMacAddress` to `principal.mac`.  
\- Modified mapping of `dvc` to map to `principal.ip` only if it's a valid IP address.   
2023-03-24 |  Enhancement:  
\- Mapped `model.now.category` to `security_result.severity`.  
\- Mapped `model.now.message` to `security_result.description`.  
\- Mapped `model.now.description` to `metadata.description`.  
\- Mapped `model.now.uuid` to `principal.user.userid`.  
\- Mapped `model.now.pid` to `principal.process.pid`.  
\- Mapped `model.now.name` to `principal.user.user_display_name`.  
\- Mapped `score` to `security_result.priority`.  
\- Mapped `triggeredComponents.port` to `intermediary.port`.  
\- Mapped `triggeredComponents.ip` to `intermediary.ip`.  
\- Mapped `device.ip` to `principal.ip`.  
\- Mapped `device.macaddress` to `principal.mac`.  
\- Mapped `device.hostname` to `principal.hostname`.  
\- Mapped `model.then.logic.data.cid`, `model.now.logic.data.cid`, `model.now.tags` to `additional.fields`.  
\- Mapped `Mapped `model.then.description`, `model.then.uuid`, `model.then.name`, `model.then.pid` to `principal.resource.attribute.labels'.  
\- Modified `metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` wherver `principal.ip` or `principal.hostname` is present.   
2022-10-31 |  Enhancement:  
\- Mapped the field `time` to `metadata.event_timestamp`.  
\- Mapped the field `model.description` to `metadata.description`.  
\- Mapped the field `model.name` to `principal.user.user_display_name`.  
\- Mapped the field `model.pid` to `principal.process.pid`.  
\- Mapped the field `device.did` to `principal.asset.asset_id`.  
\- Mapped the field `device.objecttype` to `principal.asset.type`.  
\- Mapped the field `device.ips` to `principal.ip`.  
\- Mapped the field `device.firstSeen` to `principal.asset.first_seen_time`.  
\- Mapped the field `device.lastSeen` to `principal.asset.last_discover_time`.  
\- Mapped the fields `device.sid`, `device.typename` and `device.typelabel` to `principal.resource.attribute.labels`.  
\- Mapped the field `model.tags` and `model.logic.data` to `additional.fields`.  
\- Mapped the field `breachUrl` to `security_result.url_back_to_product`.  
\- Mapped the field `mitreTechniques` to `security_result.detection_fields`.  
\- Added conditional checks for `details.0.0.contents.2.values.0` mapped to `principal.port`.  
\- Dropped the logs having incorrect json format.   
2022-10-13 |  Added grok to parse new json type logs.  
Mapped `category` to `security_result.severity`.  
Mapped `title` to `security_result.summary`.  
Mapped `details.0.0.contents.1.values.0.hostname` to `principal.hostname`.  
Mapped `details.0.0.contents.1.values.0.ip` to `principal.ip`.  
Mapped `details.0.0.contents.2.values.0` to `principal.port`.  
Mapped `details.0.0.contents.4.values.0` to `principal.location.country_or_region`.  
Mapped `details.0.1.contents.0.values.0.hostname` to `target.hostname`.  
Mapped `details.0.1.contents.0.values.0.ip` to `target.ip`.  
Mapped `incidentEventUrl` to `principal.url`.  
Mapped `summary` to `metadata.description`.  
Mapped `model.uuid` to `principal.user.userid`.  
Mapped `relatedBreaches.0.modelName` to `security_result.description`.   
2022-04-22 |  Added support for issue code being non-numeric in CEF message   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
