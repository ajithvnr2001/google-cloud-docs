---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hadoop-changelog/
title: Change log for HADOOP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:05.250807+00:00
---

# Change log for HADOOP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hadoop-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HADOOP

Date | Changes  
---|---  
2026-02-23 |  Enhancement  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `collection_time_details` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.asset.network_domain`: Newly mapped `principal_network_domain` raw log field to `event.idm.read_only_udm.principal.asset.network_domain` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp_details` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Added null and empty conditional check before mapping `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` as null is not a valid hostname.  
\- `event.idm.read_only_udm.metadata.new_event`: Updated the `event.idm.read_only_udm.metadata.new_event` from `NETWORK_CONNECTION` to `STATUS_UPDATE` when no target device details are found.  
\- `event.idm.read_only_udm.metadata.description`: Added a grok pattern to correctly extract raw log fields and map them to the appropriate UDM fields; previously, these were being incorrectly parsed into the `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Added a grok pattern to correctly extract raw log fields and map them to the appropriate UDM field; previously, these were being incorrectly parsed into the `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- Added a new grok pattern for the raw log field `ugi` to extract principal_network_domain.  
\- Added a new grok pattern to handle the new format of syslog+kv logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.process.command_line`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.src.file.full_path  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.observer.ip`  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.principal.user.userid`  
2023-06-05 |  Enhancement - Added new Grok pattern to parse new syslog format logs.  
\- Changed `event_type` from `GENERIC_EVENT` to `NETWORK_CONNECTION` when both `principal` and `target` fields are present, otherwise set it to `STATUS_UPDATE`.  
\- Mapped `ugi` to `target.ip`.  
\- Mapped `tip` to `target.hostname`.  
\- Mapped `cmd` to `principal.process.command_line`.  
\- Mapped the `hostname` and IP address already mapped to `observer.hostname and observer.ip` to `principal.hostname` and `principal.ip` as well to meet validation requirements.   
2022-05-25 |  Mapped IP to observer.ip.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
