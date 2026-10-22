---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-web-protection-changelog/
title: Change log for MCAFEE_WEB_PROTECTION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:38.897280+00:00
---

# Change log for MCAFEE_WEB_PROTECTION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-web-protection-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_WEB_PROTECTION

Date | Changes  
---|---  
2025-04-16 |  Enhancement:  
\- Added grok pattern to parse the new format of logs.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `userID` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `url` raw log field with event.idm.read_only_udm.principal.url" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `virus` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Location` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `lastRule` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `applicationType` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Requested_timestamp` raw log field with event.idm.read_only_udm.metadata.event_timestamp" UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Ssl_scanned` raw log field with event.idm.read_only_udm.additional.fields" UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `av_scanned_up` raw log field with event.idm.read_only_udm.additional.fields" UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `av_scanned_down` raw log field with event.idm.read_only_udm.additional.fields" UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rbi` raw log field with event.idm.read_only_udm.additional.fields" UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `dlp` raw log field with event.idm.read_only_udm.additional.fields" UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `Filename` raw log field with event.idm.read_only_udm.principal.file.full_path" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Mw_probabililty` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Discarded_host` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `Ssl_client_prot` raw log field with event.idm.read_only_udm.principal.resource.attribute.labels" UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `Ssl_server_prot` raw log field with event.idm.read_only_udm.principal.resource.attribute.labels" UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `domain_fronting_url` raw log field with event.idm.read_only_udm.security_result.detection_fields" UDM field.   
2024-12-19 |  Enhancement-  
\- Added Grok patterns to parse the unparsed logs.  
\- Mapped `country` to `principal.location.country_or_region`.  
\- Mapped `intermediary_ip1` to `intermediary.ip`.  
\- Mapped `intermediary_ip2` to `intermediary.ip`.  
\- Mapped `intermediary_port` to `intermediary.port`.   
2022-09-22 |  Enhancement-  
\- Updated the parser as per newly ingested logs having different names and fields.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
