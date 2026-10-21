---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-firewall-changelog/
title: Change log for BARRACUDA_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:33.531142+00:00
---

# Change log for BARRACUDA_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BARRACUDA_FIREWALL

Date | Changes  
---|---  
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `barracuda_info` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- Added a grok pattern to parse `event_desc` and extract the fields.  
\- Added conditional check for `event.idm.read_only_udm.network.application_protocol` to map to `event.idm.read_only_udm.network.application_protocol` for values `ssh`, `rdp`, `dns`.  
\- Added conditional check to ensure `url_cat` is not empty before merging it into `event.idm.read_only_udm.security_result.category_details`.   
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Removed mapping of `event_time` from `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field. because `ingested_timestamp` are not populated from raw logs. It is the GMT timestamp when the event was ingested (received) by Google Security Operations.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `load1`, `load2`, `load3` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `application_protocol` matches `(?i)http` and `ip_protocol` does not match `(?i)icmp`, updated to `NETWORK_HTTP`, otherwise updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.   
2025-11-13 |  Enhancement:  
\- Modified the grok pattern to parse intermediary.hostname correctly.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `Duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Count` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `event_desc` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Setting `event.idm.read_only_udm.network.ip_protocol` UDM field with UDP when `ip_protocol` raw log field value is udp.   
2025-05-09 |  Enhancement:  
\- event.idm.read_only_udm.security_result.summary: Newly mapped info raw log field with event.idm.read_only_udm.security_result.summary UDM field.   
2025-04-22 |  Enhancement:  
\- Added support to map correct date in `ingested_timestamp` UDM field.  
\- Added support to parse logs which have `product_event_type` as `IL_Barracuda_NG_FW`.   
2024-09-05 |  Enhancement:  
\- Modified a Grok pattern to handle unparsed logs.   
2024-05-17 |  Enhancement:  
\- Added `on_error` for a Grok filter.  
\- Added IP address check for `target_ip` before merging with `target.ip`.   
2024-04-12 |  Enhancement:  
\- Modified date pattern to consider `event_time` value that includes timezone.   
2024-03-22 |  Enhancement:  
\- Added new Grok to parse logs with timestamp of ISO8601 format.   
2022-07-08 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
