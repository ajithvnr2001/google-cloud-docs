---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fidelis-network-changelog/
title: Change log for FIDELIS_NETWORK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:34:07.737604+00:00
---

# Change log for FIDELIS_NETWORK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fidelis-network-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIDELIS_NETWORK

Date | Changes  
---|---  
2025-08-07 |  Enhancement:  
\- Added support to map the `rt` field into `event.idm.read_only_udm.metadata.event_timestamp.seconds`.  
\- Added support to `duser` field to get parse properly.  
\- event.idm.read_only_udm.metadata.description: Newly Mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `suser` from `event.idm.read_only_udm.target.user.userid` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.user.userid: Mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field   
2025-07-22 |  Enhancement:  
\- Added a Grok pattern to handle new pattern of CEF logs.  
\- Used `parse_app_protocol` include while mapping `proto` to `network.application_protocol`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `proto` is not a valid `event.idm.read_only_udm.network.application_protocol` value.   
2025-03-03 |  Enhancement:  
\- Added support to handle CEF logs.   
2024-10-09 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-06-04 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `alert_type` to `security_result.detection_fields`.   
2023-09-04 |  Enhancement -  
\- Mapped `event1.sld` to `principal.hostname`.  
\- Mapped `event1.sni` to `target.hostname`.  
\- Mapped `event1.src_ip6` to `principal.ip`.  
\- Mapped `event1.dst_ip6` to `target.ip`.  
\- Mapped `event1.sport` to `principal.port`.  
\- Mapped `event1.dport` to `target.port`.  
\- Mapped `event1.cipher` to `network.tls.cipher`.  
\- Mapped `event1.tproto` to `network.ip_protocol`.  
\- Mapped `event1.client_asset_name` to `principal.application`.  
\- Mapped `event1.direction` to `network.direction`.  
\- Mapped `event1.rel_sesid` to `network.session_id`.  
\- Mapped `event1.tls_ciphersuite` to `network.tls.cipher`.  
\- Mapped `event1.ja3sdigest` to `network.tls.server.ja3s`.  
\- Mapped `event1.ja3digest` to `network.tls.client.ja3`.  
\- Mapped `event1.srvcerthash` to `target.file.sha1`.  
\- Mapped `event1.sha256` to `target.file.sha256`.  
\- Mapped `event1.md5` to `target.file.md5`.  
\- Mapped `event1.filetype` to `target.file.mime_type`.  
\- Mapped `event1.filesize` to `target.file.size`.  
\- Mapped `event1.certificate_issuer_name` to `network.tls.client.certificate.issuer`.  
\- Mapped `event1.certificate_subject_name` to `network.tls.client.certificate.subject`.  
\- Mapped `event1.certificate_start_date` to `network.tls.client.certificate.not_before`.  
\- Mapped `event1.certificate_end_date` to `network.tls.client.certificate.not_after`.  
\- Mapped `event1.client_packet_count` to `network.sent_bytes`.  
\- Mapped `event1.server_packet_count` to `network.received_bytes`.  
\- Mapped `event1.session_size` to `network.session_duration.seconds`.  
\- Mapped `event1.server_asset_subnet` to `read_only_udm.additional.fields`.  
\- Mapped `event1.client_asset_subnet` to `read_only_udm.additional.fields`.  
\- Mapped `event1.sha1hash` to `read_only_udm.additional.fields`.  
\- Mapped `event1.type` to `read_only_udm.additional.fields`.  
\- Mapped `event1.histbuf` to `read_only_udm.additional.fields`.  
\- Mapped `event1.sen_name` to `read_only_udm.additional.fields`.  
\- Mapped `event1.certificate_subject_altname` to `read_only_udm.additional.fields`.  
\- Mapped `event1.certificate_key_usage` to `read_only_udm.additional.fields`.  
\- Mapped `event1.certificate_key_length` to `read_only_udm.additional.fields`.  
\- Mapped `event1.certificate_extended_key_usage` to `read_only_udm.additional.fields`.  
\- Mapped `event1.version` to `network.tls.version`.   
2023-05-19 |  Enhancement -  
\- Mapped `exe_richsignaturehash`, `exe_richsignaturepvhash`, `alert_threat_score` to `security_result.detection_fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
