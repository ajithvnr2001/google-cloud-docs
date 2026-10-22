---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-amp-changelog/
title: Change log for CISCO_AMP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:52.514981+00:00
---

# Change log for CISCO_AMP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-amp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_AMP

Date | Changes  
---|---  
2025-10-06 |  Enhancement:  
\- event.idm.read_only_udm.security_result.last_discovered_time: Removed mapping of `column209` from `event.idm.read_only_udm.security_result.last_discovered_time` UDM field and mapped `column143` instead.   
2025-09-25 |  Enhancement:  
\- Added Grok, KV, and CSV filters to parse the new log format.  
\- event.idm.read_only_udm.observer.resource.attribute.labels: Newly mapped `SourceModuleName` raw log field to event.idm.read_only_udm.observer.resource.attribute.labels with key `product_name`.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `column61` raw log field to `event.idm.read_only_udm.principal.asset_id`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column62` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `column63` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.url: Newly mapped `column64` raw log field to `event.idm.read_only_udm.principal.url`.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `column65` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers`.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped IP and MAC addresses from the JSON array in `column67` raw log field to `event.idm.read_only_udm.principal.asset.attribute.labels`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column68` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.target.file.names: Newly mapped `column176` raw log field to `event.idm.read_only_udm.target.file.names`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `column177` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `column180` raw log field to `event.idm.read_only_udm.target.file.sha256`.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped a static value `AMP` to `event.idm.read_only_udm.metadata.product_name`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `app` raw log field to `event.idm.read_only_udm.intermediary.application`.  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped `pid` raw log field to `event.idm.read_only_udm.intermediary.process.pid`.  
\- Conditionally set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` based on the presence of user information.  
\- Mapped `column142` to `security_result.summary`.  
\- Mapped `column175` to `security_result.description`.  
\- Mapped `column71` to `security_result.threat_name`.  
\- Mapped `column206` to `security_result.attack_details.tactics`.  
\- Mapped `column207` to `security_result.attack_details.techniques`.  
\- Mapped `column208` to `security_result.first_discovered_time`.  
\- Mapped `column209` to `security_result.last_discovered_time`.   
2025-03-14 |  Enhancement:  
\- Mapped `Compressed_sha256` to `additional.fields`.  
\- Mapped `analysis_action`, `analysis_score`, `analysis_status`, `verdict_num`, and `verdict_from` to `security_result.detection_fields`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `file_name` to `target.file.names`.  
\- Mapped `file_type` to `target.file.mime_type`.  
\- Mapped `upload_reason` to `metadata.description`.   
2025-02-28 |  Enhancement:  
\- Added support for the new format of logs.  
\- Added a Grok pattern to the new format of logs.  
\- Mapped `active_connections`,`from`,`is_slow`,`instance_id`,`malwareverdict` and ,`verdict_str` to `additional.fields`.  
\- Mapped `Time` to `metadata.event_timestamp`.  
\- Mapped `file_extension` to `arget.resource.attribute.labels`.  
\- Mapped `filemime` to `target.file.mime_type`.  
\- Mapped `filename` to `target.file.full_path`.  
\- Mapped `host` to `principal.hostname` and `principal.assest.hostname`.  
\- Mapped `length_file` to `principal.resource.attribute.labels`.  
\- Mapped `sha256` to `target.file.sha256`.  
\- Mapped `uploadreason` to `security_result.description`.  
\- Mapped `log_id` to `metadata.product_log_id`.  
\- Mapped `ssl_bytes` to `network.sent_bytes`.  
\- Mapped `socket_bytes` to `network.received_bytes`.   
2024-12-18 |  Enhancement:  
\- Added a Grok pattern to support new JSON log format.   
2024-05-14 |  Enhancement:  
\- Mapped `event_type_id` to `metadata.product_log_id`.  
\- Mapped `detection_id` to `security_result.detection_fields`.  
\- Mapped `file.disposition`, `error.error_code`, and `error.description` to `security_result.description`.  
\- Mapped `file.file_name` to `target.file.names`.  
\- Mapped `file.parent.disposition`, `file.parent.file_name`, `file.parent.identity.md5`, `file.parent.identity.sha1`, and `file.parent.identity.sha256` to `target.resource.attribute.labels`.  
\- Mapped `file.identity.md5` to `target.file.md5`.  
\- Mapped `file.identity.sha1` to `target.file.sha1`.   
2024-02-23 |  Enhancement:  
\- Added support to parse logs if `event_type` is `Component Download Success`, `Scan Started`, `Scan Completed, No Detections`, `Product Update Started`, `Product is already installed.`, `Policy Update`, `Install Started`, `Product Update Failed`, `Uninstall`, `Endpoint IOC Definition Update Success`, `Endpoint IOC Scan Started`, `Policy Update Failure`, `Endpoint IOC Scan Failed`, `Major Fault Raised`, `Critical Fault Raised`, `Endpoint IOC Scan Detection Summary`, `Endpoint IOC Configuration Update Success`, `Scan Failed`, `Fault Cleared`, or `Install Failure`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
