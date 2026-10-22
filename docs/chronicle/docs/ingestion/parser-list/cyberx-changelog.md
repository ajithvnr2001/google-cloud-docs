---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberx-changelog/
title: Change log for CYBERX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:49.478970+00:00
---

# Change log for CYBERX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERX

Date | Changes  
---|---  
2025-04-14 |  Enhancement:  
\- Added Gsub to replace `\\n` with ` ` on `message` to parse the logs.  
\- Added Grok pattern to extract `intermediary_hostname` from the log.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- Added conditional check before mapping `cs1` and `cs1Label` to `event.idm.read_only_udm.additional.fields` in include file `cef_udm_mapping.include`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `UUID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- Added conditional check before mapping `externalID_value` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field in include file `cef_udm_mapping.include`.   
2025-01-23 |  Enhancement:  
\- Added a Grok pattern to parse the new format of logs.  
\- Mapped `product_version_x` to `metadata.product_version`.  
\- Mapped `pro_event_type` to `metadata.product_event_type`.  
\- Mapped `title` to `security_result.description`.  
\- Mapped `msg` to `metadata.description`.  
\- Added a Grok pattern to parse `client_ip`.  
\- Mapped `client_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `type` to `security_result.detection_fields`.  
\- Mapped date format `MMM dd yyyy HH:mm:ss` to `metadata.event_timestamp`.  
\- Mapped `src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `dst_ip` to `target.ip`.  
\- Mapped `src_mac` to `principal.mac`.  
\- Mapped `cat` to `security_result.detection_fields`.   
2025-01-08 |  Enhancement:  
\- Mapped `timestamp` and `ts` to `metadata.event_timestamp`.  
\- Mapped `type` to `security_result.detection_fields`.   
2024-06-25 |  Enhancement:  
\- Added support for the CEF format of syslog logs.  
\- Added support for new pattern of XML logs.   
2024-05-15 |  Enhancement:  
\- Modified KV pattern to handle new pattern of SYSLOGS.  
\- Mapped `source_ip2` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `destination_ip2` to `target.ip` and `target.asset.ip`.  
\- Mapped `Severity` to `security_result.severity_details`.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.   
2023-12-06 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
