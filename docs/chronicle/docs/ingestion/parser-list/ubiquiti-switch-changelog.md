---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubiquiti-switch-changelog/
title: Change log for UBIQUITI_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:29.129585+00:00
---

# Change log for UBIQUITI_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubiquiti-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UBIQUITI_SWITCH

Date | Changes  
---|---  
2026-08-17 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `op`, `message_type` , `ip_assign_type` , `wpa_auth_delta` , `assoc_delta` , `auth_delta` , `event_id` , `auth_ts` , `auth_utc` , `sta_dc_reason` , `auth_rssi` , `auth_algo` raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- Modified a grok pattern to parse the raw log fields.   
2026-05-20 |  Enhancement:  
\- Modified a grok pattern to parse the fields correctly.  
\- Added a grok pattern on `UNIFIutcTime` to extract year.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `UNIFIsite` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `UNIFIcategory` and `UNIFIutcTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-06 |  Enhancement:  
\- `event.idm.read_only_udm.target.application: Newly mapped `tar_app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description: Newly mapped `desc`, `msg`, DESCR` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version: Newly mapped `prod_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `UNIFIclientAlias` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname: Newly mapped `UNIFIclientHostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname: Newly mapped `UNIFIclientHostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip: Newly mapped `UNIFIclientIp`, `src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip: Newly mapped `UNIFIclientIp`, `src_ip` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.mac: Newly mapped `UNIFIclientMac`, `src_mac` raw log fields with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.target.hostname: Newly mapped `UNIFIconnectedToDeviceName` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname: Newly mapped `UNIFIconnectedToDeviceName` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip: Newly mapped `UNIFIconnectedToDeviceIp`, `dst_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip: Newly mapped `UNIFIconnectedToDeviceIp`, `dst_ip` raw log fields with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.mac: Newly mapped `UNIFIconnectedToDeviceMac`, `dst_mac` raw log fields with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.target.asset.mac: Newly mapped `UNIFIconnectedToDeviceMac` raw log field with `event.idm.read_only_udm.target.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.port: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol: Newly mapped `PROTO` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.summary: Newly mapped `summary` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details: Newly mapped `sev_details` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped `max_rssi`, `min_rssi`, `RxPath`, `UNIFIlastConnectedToDeviceName`, `UNIFIlastConnectedToDeviceIp`, `UNIFIlastConnectedToDeviceMac`, `UNIFIlastConnectedToDeviceModel`, `UNIFIlastConnectedToDeviceVersion`, `UNIFIwifiName`, `UNIFIwifiChannel`, `UNIFIwifiChannelWidth`, `UNIFIWiFiRssi`, `UNIFIlastConnectedToWiFiChannel`, `UNIFIlastConnectedToWiFiChannelWidth`, `UNIFIlastConnectedToWiFiRssi`, `LEN`, `TTL`, `TOS`, `ID`, `PREC`, `SEQ`, `ACK`, `WINDOW`, `URGP`, `MARK` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped UNIFIwifiBand` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if UNIFIwifiBand is not empty or `na`.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped UNIFIlastConnectedToWiFiBand` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if UNIFIlastConnectedToWiFiBand is not empty or `na`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `UNIFIconnectedToDeviceModel`, `UNIFIconnectedToDeviceVersion` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- If principal_present is `true` and target_present is `true`, updated to NETWORK_HTTP and Else if has_user is `true`, updated to USER_UNCATEGORIZED.  
\- Added new Grok patterns to support new pattern of logs.  
\- Added a KV filter to parse kv_data.  
\- Added support for ISO8601 timestamp format for the timestamp field.   
2023-11-21 |  Enhancement:  
\- Added support for new pattern of SYSLOGS.  
\- Added null check for `SRC`, `DST`, `SPT` before mapping to UDM fields.  
\- Added new GROK patterns to extract `mac`, `principal_ip` from `description`.  
\- Added `principal_present` check before setting `metadata.event_type` to `STATUS_SHUTDOWN`, `STATUS_STARTUP`.  
\- Mapped `source_port` to `principal.port`.  
\- Mapped `query_1` to `target.administrative_domain`.  
\- Mapped `query_server_1` to `target.ip`.  
\- Mapped `satisfaction_now`, `anomalies`, `event_type`, `assoc_status`, `radio` to `security_result.detection_fields`.  
\- Mapped `mac`, `sta`, `bssid` to `principal.mac`.  
\- Mapped `principal_ip` to `principal.ip`.  
\- Mapped `asset_id` to `observer.asset.product_object_id`.  
\- Mapped `asset_version` to `observer.asset.software.version`.  
\- Mapped `application` to `observer.application`.  
\- Mapped `process_id` to `observer.process.pid`.  
\- Mapped `vap` to `metadata.ingestion_labels`.   
2022-08-26 |  Added Mapping for unparsed log.  
SRC mapped to principal.ip.  
DST mapped to target.ip.  
SPT mapped to target.port.  
SPT mapped to principal.port.  
PROTO mapped to network.ip_protocol.  
TTL mapped to additional.fields.  
ID mapped to additional.fields.  
IN mapped to additional.fields.  
MAC mapped to principal.mac.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
