---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-forticlient-changelog/
title: Change log for FORTINET_FORTICLIENT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:58:32.543654+00:00
---

# Change log for FORTINET_FORTICLIENT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-forticlient-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FORTICLIENT

Date | Changes  
---|---  
2026-07-07 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `devid` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce a more accurate mapping.  
\- `event.idm.read_only_udm.observer.asset_id`: Mapped `devid` raw log field with `event.idm.read_only_udm.observer.asset_id` UDM field  
\- `event.idm.read_only_udm.principal.resource.name`: Removed mapping of `devname` from `event.idm.read_only_udm.principal.resource.name` UDM field as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.principal.resource.type`: Removed mapping of `devname` from `event.idm.read_only_udm.principal.resource.type` UDM field as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Mapped `devname` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `tunnelip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `remip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `logdesc` and `msg` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `craction`, `crlevel`, `crscore` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `tunnelid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appid`, `applist`, `incidentserialno`, `tunneltype`, `nextstat` and `apprisk` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Added support for parsing `direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.   
2026-06-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for parsing timezone offset from `ts` raw log field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `srcintf`, `srcintfrole` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dstintf`, `dstintfrole` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `srccountry` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dstcountry` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `policyid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `policytype` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policyname` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `group` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `sentpkt` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `rcvdpkt` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Mapped `appcat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action` and `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` and `event.idm.read_only_udm.security_result.action_details` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `authserver` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vd`, `poluuid`, `trandisp`, `service` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when principal machine details and target machine details present else setting it to `STATUS_UPDATE` when principal machine details are present.   
2025-01-13 |  Enhancement:  
\- Added support for mapping `service` to `network.application_protocol`.   
2023-12-29 |  Enhancement:  
\- Changed mapping of `SubjectUserName` from `principal.user.userid` to `additional.fields`.  
\- Changed mapping of `uid` from `principal.user.userid` to `principal.user.product_object_id`.  
\- If `uid` is not present, mapped `fctuid` to `principal.user.product_object_id`.  
\- Mapped `user` to `principal.user.userid` on the top of its mapping to `principal.user.user_display_name`.   
2023-11-30 |  Enhancement:  
\- Added a Grok pattern to parse the new logType.  
\- Added a Grok pattern to parse the new XML part.  
\- If `devname` is not null, set `principal.resource.type` to `DEVICE`.  
\- Mapped `devname` to `principal.resource.name`.  
\- Mapped `itime` to `additional.fields`.  
\- Mapped `fctsn` to `additional.fields`.  
\- Mapped `logver` to `additional.fields`.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `subtype` to `principal.resource.resource_subtype`.  
\- Mapped `eventtype` to `metadata.product_event_type`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `pcdomain` to `principal.administrative_domain`.  
\- Mapped `site` `additional.fields`.  
\- Mapped `fctver` `additional.fields`.  
\- Mapped `sessionid` to `network.session_id`.  
\- Mapped `srcname` to `principal.resource.attribute.labels`.  
\- Mapped `srcproduct` to `principal.application`.  
\- Mapped `srcport` `principal.port`.  
\- Mapped `direction` to `network.direction`.  
\- Mapped `dstip` to `target.ip`.  
\- Mapped `remotename` to `target.hostname`.  
\- Mapped `dstport` to `target.port`.  
\- Mapped `proto` to `network.ip_protocol`  
\- Mapped `rcvdbyte` to `network.received_bytes`.  
\- Mapped `sentbyte` to `network.sent_bytes`.  
\- Mapped `utmaction` to `security_result.description`.  
\- Mapped `sec_action` to `security_result.action`.  
\- Mapped `utmevent` to `security_result.category_details`.  
\- Mapped `threat` to `security_result.threat_name`.  
\- Mapped `service` to `network.application_protocol`.  
\- Mapped `url` to `principal.url`.  
\- Mapped `userinitiated` to `security_result.detection_fields`.  
\- Mapped `browsetime` to `additional.fields`.  
\- Mapped `date` and time` to `metadata.event_timestamp".  
\- Mapped `timestamp` to `metadata.collected_timestamp`.  
\- Mapped `client_ip` to `principal.ip`.  
\- Mapped `source_ver` to `principal.platform_version`.  
\- Mapped `source_type` to `principal.resource.attribute.labels`.  
\- Mapped `type` to `principal.resource.attribute.labels`.  
\- Mapped `event_id` to `additional.fields`.  
\- Mapped `ThreadID` to `additional.fields`.  
\- Mapped `SubjectLogonId` to `additional.fields`.  
\- Mapped `fctuid` to `principal.user.product_object_id`.  
\- Mapped `source_ver` to `principal.platform_version`.  
\- Mapped `ProviderGuid` to `principal.resource.product_object_id`.  
\- Mapped `ProcessId` to `principal.process.pid`.  
\- Mapped `SubjectUserSid` to `principal.user.windows_sid`.  
\- Mapped `SubjectUserName` to `principal.user.userid`.   
2023-10-27 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
