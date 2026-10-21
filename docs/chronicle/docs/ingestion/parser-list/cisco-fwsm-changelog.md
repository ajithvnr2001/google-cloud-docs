---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-fwsm-changelog/
title: Change log for CISCO_FWSM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:46:32.110719+00:00
---

# Change log for CISCO_FWSM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-fwsm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_FWSM

Date | Changes  
---|---  
2025-10-17 |  Enhancement:  
\- Added New GROK pattern for SYSLOG logs.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tls_version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `packet_size`, `threshold` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-04-17 |  Enhancement:  
\- Added a GROK pattern for SYSLOG log.  
\- Added a GROK pattern for field `decrip`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped src_fwuser raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped dst_fwuser raw log field with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped dst_mapped_interface raw log field with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped dst_mapped_port raw log field with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped dst_interface_name raw log field with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped src_interface_name raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped src_mapped_port raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.labels: Newly mapped src_mapped_interface raw log field with event.idm.read_only_udm.principal.labels UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped protocol raw log field with event.idm.read_only_udm.network.ip_protocol UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped session_id raw log field with event.idm.read_only_udm.network.session_id UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Newly mapped `icmp_code`, `icmp_code_laddr`, `icmp_code_xlated`, `icmp_type`, `icmp_seq_num`, `interface_name`, and `tcp_flags` raw log field with event.idm.read_only_udm.about.resource.attribute.labels UDM field.   
2023-05-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
