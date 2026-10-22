---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arista-switch-changelog/
title: Change log for ARISTA_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:40.088136+00:00
---

# Change log for ARISTA_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arista-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARISTA_SWITCH

Date | Changes  
---|---  
2025-12-16 |  Enhancement:  
\- Added a Grok pattern to parse the new pattern of SYSLOG format logs.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `Message_Code` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `config_file` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `service` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `tty` raw log field to `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `authz_action` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.namespace: Newly mapped `vrf_name` raw log field to `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.network.asn: Newly mapped `neighbor_as` raw log field to `event.idm.read_only_udm.network.asn` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `neighbor_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `neighbor_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `task_id`, `bgp_error_code`, `bgp_error_subcode`, `radius_method_list`, `start_time`, `timezone` and `elapsed_time` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-15 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vlan_id` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Enhanced date parsing for `event.idm.read_only_udm.metadata.event_timestamp` to add support for `MMM d HH:mm:ss` and `MMM dd HH:mm:ss` date formats.  
\- Updated syslog grok patterns to parse the raw log field `timestamp` using both `SYSLOGTIMESTAMP` and `TIMESTAMP_ISO8601` patterns.   
2024-06-07 |  Enhancement:  
\- Added a Grok pattern to parse the new pattern of SYSLOG format logs.  
\- Mapped `principal_mac` to `principal.mac`.  
\- Mapped `principal_port` to `principal.port`.   
2024-03-17 |  Enhancement:  
\- Added a Grok pattern to parse SYSLOG format logs.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `proto` to `network.application_protocol`.  
\- Mapped `prin_ip` to `principal.ip`.   
2022-08-03 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
