---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ionix-changelog/
title: Change log for IONIX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:36:08.495902+00:00
---

# Change log for IONIX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ionix-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IONIX

Date | Changes  
---|---  
2025-10-22 |  Enhancement:  
\- `event.idm.entity.entity.asset.asset_id`: Newly mapped `data.asset` raw log field with `event.idm.entity.entity.asset.asset_id` UDM field.  
\- `event.idm.entity.entity.hostname`: Newly mapped `data.asset` raw log field with `event.idm.entity.entity.hostname` UDM field.  
\- `event.idm.entity.entity.asset.ip`: Newly mapped `ip` raw log field with `event.idm.entity.entity.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `data.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `data.date_compromised` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `data.endpoint_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `data.endpoint_os` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `data.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `data.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `data.related_asset` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `data.related_asset` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `data.malware_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.stealer_family`, `data.incident_id`, `data.date_added`, `data.password_strength`, `data.password_hash`, `data.endpoint_antivirus`, `data.endpoint_cidr` and `data.device_association` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name` is set to a constant value of `IONIX`.  
\- `event.idm.read_only_udm.metadata.vendor_name` is set to a constant value of `IONIX`.   
2023-09-28 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
