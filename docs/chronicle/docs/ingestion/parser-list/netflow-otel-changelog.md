---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netflow-otel-changelog/
title: Change log for NETFLOW_OTEL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:05:36.064452+00:00
---

# Change log for NETFLOW_OTEL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netflow-otel-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETFLOW_OTEL

Date | Changes  
---|---  
2025-04-23 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `flow.io.bytes` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Mapped `flow.io.bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2025-04-11 |  Enhancement:  
\- Newly created parser.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `source.address` raw log field with `event.idm.read_only_udm.principal.ip` and `principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `source.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination.port` raw log field with `event.idm.read_only_udm.target.port` UDM field  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `network.transport` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `network.type` , `flow.io.bytes` , `flow.io.packets` , `flow.start` , `flow.time_received` and `flow.end` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `flow.sequence_num` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `flow.sampler_address` raw log field with `event.idm.read_only_udm.observer.ip` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `flow.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
