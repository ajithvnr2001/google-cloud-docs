---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-firewall-changelog/
title: Change log for SOPHOS_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:30.135140+00:00
---

# Change log for SOPHOS_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOPHOS_FIREWALL

Date | Changes  
---|---  
2026-06-04 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip` log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `reported_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.ciaddr`: Newly mapped `reported_ip` raw log field with `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When `reported_ip` is not empty, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `lease_time` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern on message to extract `intermediary_ip` log field.   
2025-04-23 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `date_time` and `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field   
2024-08-26 |  Enhancement:  
\- Parsed logs for timezone=`WAT`.   
2023-11-20 |  Enhancement:  
\- Mapped `packets_sent` to `network.sent_packets`.  
\- Mapped `packets_received` to `network.received_packets`.  
\- Mapped `src_trans_ip` to `principal.nat_ip`.  
\- Mapped `src_trans_port` to `principal.nat_port`.  
\- Mapped `dst_trans_ip` to `target.nat_ip`.  
\- Mapped `dst_trans_port` to `target.nat_port`.  
\- Mapped `bytes_sent` to `network.sent_bytes`.  
\- Mapped `bytes_received` to `network.received_bytes`.  
\- Mapped `duration` to `network.session_duration`.  
\- Mapped `referer` to `network.http.referer_url`.  
\- Mapped `ipaddress` to `principal.ip` and `network.dhcp.ciaddr`.  
\- Mapped `client_physical_address` to `network.dhcp.chaddr`.  
\- Mapped `client_host_name` to `network.dhcp.client_hostname`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `http_status` to `network.http.response_code`.  
\- Mapped `app_name` to `principal.application`.  
\- Mapped `out_display_interface`, `web_policy_id`, `http_category`, `http_category_type`, `exceptions`, `con_id`,  
`used_quota`, `src_zone_type`, `src_zone`, `dst_zone_type`, `dst_zone`, `app_risk`, `app_category`, `nat_rule_name`,  
`gw_id_request`, `gw_name_request`, `app_filter_policy_id`, `app_technology`, `in_interface`, `out_interface`,  
`con_event`, `srczonetype`, `dstzonetype`, `connevent`, `connid`, `hb_health`, `category_type`,  
`activityname` to `security_result.detection_fields`.   
2023-11-10 |  Enhancement:  
\- Mapped `fw_rule_type` to `security_result.rule_type`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `device_serial_id` to `principal.asset.asset_id`.  
\- Mapped `log_type`, `log_component`, `log_subtype`, `log_version`, `nat_rule_id`, `ether_type`,  
`hb_status`, `app_resolved_by`, `app_is_cloud`, `qualifier`, `log_occurrence`, `in_display_interface` to `security_result.detection_fields`.   
2023-04-03 |  Enhancement:  
\- Modified mapping of `device_name` from `principal.hostname` to `intermediary.hostname`.  
\- Modified mapping of `device_id` from `principal.asset.asset_id` to `intermediary.asset.asset_id`.  
\- Modified mapping of `metadata.vendor_name` from `SOPHOS Ltd.` to `SOPHOS`.  
\- Mapped `sent_pkts` to `network.sent_packets`.  
\- Mapped `recv_pkts` to `network.received_packets`.  
\- Mapped `tran_src_ip` to `principal.nat_ip`.  
\- Mapped `tran_src_port` to `principal.nat_port`.  
\- Mapped `tran_dst_ip` to `target.nat_ip`.  
\- Mapped `tran_dst_port` to `target.nat_port`.   
2022-12-01 |  Enhancement - Parsed logs for timezone=`IST`.  
\- Mapped `application_category, application_risk and application_technology` to `security_result.detection_fields`.  
\- Mapped `fw_rule_name` to `security_result.rule_name`.  
\- Mapped `fw_rule_section` to `security_result.rule_set`.   
2022-08-18 |  Enhancement - Parsed logs for timezone=`CEST`.  
\- Reduced Generic Event percentage  
\- Mapped `user_name` to `event.idm.read_only_udm.principal.user.userid`  
\- Mapped `device_id` to `event.idm.read_only_udm.principal.asset.asset_id`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
