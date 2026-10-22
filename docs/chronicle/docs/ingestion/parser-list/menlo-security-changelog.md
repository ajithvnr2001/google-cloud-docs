---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/menlo-security-changelog/
title: Change log for MENLO_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:37.852942+00:00
---

# Change log for MENLO_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/menlo-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MENLO_SECURITY

Date | Changes  
---|---  
2025-07-29 |  Enhancement:  
\- event.idm.read_only_udm.metadata.log_type: Newly mapped `log_type` raw log field to `event.idm.read_only_udm.metadata.log_type`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userid` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.ip`.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `user`-agent raw log field to `event.idm.read_only_udm.network.http.user_agent`.  
\- event.idm.read_only_udm.security_result.about.url: Newly mapped `url` raw log field to `event.idm.read_only_udm.security_result.about.url`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `categories` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `protocol` raw log field to `event.idm.read_only_udm.network.application_protocol`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `pe_reason` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `x-client-ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `customer_name` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.security_result.confidence_details: Newly mapped `risk_score` raw log field to `event.idm.read_only_udm.security_result.confidence_details`.  
\- Modified the parser to handle JSON format with key `event` into `event_data` to avoid conflict.  
\- Added logic to handle multiple destination IPs in `dst` field.  
\- Added logic to map `customer_name` to `intermediary.ip` or `intermediary.hostname` according to the value.   
2025-06-26 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Modified date filter to add support for new format of event_timestamp.  
\- event.idm.read_only_udm.principal.location.country_or_region : Newly mapped `region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.location.name : Newly mapped `region_name` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.group.product_object_id : Newly mapped `groups` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `content-type` and `product` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type : Newly mapped `mimeType` raw log fields with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Added support for `xff_ip` raw log field to map ip(s) in case of multiple ip addresses.  
\- event.idm.read_only_udm.security_result.detection_fields: All the fields were not parsing before which are parsing now.  
\- Added grok check for `top_url` to check whether it is a valid url or not.   
2025-03-19 |  Enhancement:  
\- Added support to map `categories` to `security_result.category_details` when it is in form of an array.  
\- Added Grok patterns to check for valid ips.  
\- Added condition checks before setting `metadata.event_type`.  
\- Added a condition check before mapping `sha256` to `target.file.sha256`.   
2023-08-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
