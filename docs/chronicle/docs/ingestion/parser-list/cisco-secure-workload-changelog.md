---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-workload-changelog/
title: Change log for CISCO_SECURE_WORKLOAD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:10:58.633371+00:00
---

# Change log for CISCO_SECURE_WORKLOAD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-workload-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_SECURE_WORKLOAD

Date | Changes  
---|---  
2026-05-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Details.user_dst_app_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Details.user_dst_environment`, `Details.ConsumerThreatCategories`, `Details.ProviderThreatCategories` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `Details.user_dst_location` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.domain.first_seen_time`: Newly mapped `time_range.0` raw log field with `event.idm.read_only_udm.principal.domain.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.principal.domain.last_seen_time`: Newly mapped `time_range.1` raw log field with `event.idm.read_only_udm.principal.domain.last_seen_time` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostkey` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `hostvalue` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alertsubType` , `Details.user_dst_ownership`, `Details.user_dst_network_zone`, `key_id_collection_count`, `summarized_alerts`, `host_name_count`, `scope_id`, `hostkey` and `hostvalue` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-14 |  Enhancement:  
\- Added support for KV and SYSLOG format.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Details.SourceAddress` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `Details.SourcePort` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Details.DestinationAddress` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `Details.DestinationPort` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Details.Protocol` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Details.status` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.role_name`: Newly mapped `Details.user_src_role` raw log field to `event.idm.read_only_udm.principal.user.role_name` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `Details.user_src_location` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Details.user_src_app_name` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Details.ProviderScopes`, `Details.ConsumerScopes`, `Details.IsProviderMalicious`, `Details.IsConsumerMalicious`, `Details.user_src_network_zone`, `Details.user_src_environment`, `Details.user_src_ownership`, `vrf_id`, `scope_name`, `individual_alert`, `summary_alert_freq`, `alert_grain` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2024-12-02 |  Newly created parser.   
2024-11-11 |  Enhancement:  
\- Added a new Grok pattern to parse logs in the new SYSLOG+JSON format.  
\- Replaced `key_id`,`tenat_id` and `event_time` with `keyId`,`tenantId` and `eventTime`.  
\- Mapped `connection` and `event_name` to `additional.fields`.  
\- Mapped `pid` to `principal.process.pid`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
