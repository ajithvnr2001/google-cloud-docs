---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ai-hunter-changelog/
title: Change log for AI_HUNTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:07:29.986834+00:00
---

# Change log for AI_HUNTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ai-hunter-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AI_HUNTER

Date | Changes  
---|---  
2026-06-25 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields for SYSLOG format of logs.  
\- Added support for JSON formatted fields within the SYSLOG logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sensor` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.severity` and `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `threat_level` raw log field with `event.idm.read_only_udm.security_result.severity` and `event.idm.read_only_udm.security_result.severity_details` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `is_new_threat` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when principal machine details and target machine details are present.   
2026-03-02 |  Enhancement:  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `api_msg` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.target.hostname`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
-`event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `source_module` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
-`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
-`event.idm.read_only_udm.metadata.event_type`: If `src_ip` is not null `has_principal` is `true` and updated the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UNCATEGORIZED`, else if `src_ip` is null `has_principal` is `false` and updated the value of `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.  
\- Modified the grok patterns in message and inner_message grok in order to parse the logs and following UDM fields are now being mapped correctly:  
-`event.idm.read_only_udm.metadata.description`  
-`event.idm.read_only_udm.metadata.event_timestamp.seconds`  
-`event.idm.read_only_udm.metadata.log_type`  
-`event.idm.read_only_udm.metadata.product_name`  
-`event.idm.read_only_udm.metadata.vendor_name`  
-`event.idm.read_only_udm.principal.ip`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
