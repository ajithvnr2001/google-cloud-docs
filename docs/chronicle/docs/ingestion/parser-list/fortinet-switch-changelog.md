---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-switch-changelog/
title: Change log for FORTINET_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:40:30.523560+00:00
---

# Change log for FORTINET_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_SWITCH

Date | Changes  
---|---  
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `duration`, `interface`, `total`, `used` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-05 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields` : Removed mapping of `subtype` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents the event being performed.  
\- `event.idm.read_only_udm.metadata.product_event_type` : Mapped `subtype` with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type` : Removed mapping of `event` from `event.idm.read_only_udm.metadata.product_event_type` UDM field as this represents the description about the event.  
\- `event.idm.read_only_udm.security_result.summary` : Mapped `event` with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `switch.interface`, `oldstate` , `newstate` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vlan` , `status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-13 |  Enhancement:  
\- Added support for timezone in the `timestamp`  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cpu`, `memory`, `sn`, `concurrent_session`, `profile`, `total_session`, `ui` and `average` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dstip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` : Updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when principal machine data and target machine data is present and `action` is `login`.  
\- `event.idm.read_only_udm.metadata.event_type` : Updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when principal machine data and target machine data is present and `action` is `logout`.   
2024-11-11 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
