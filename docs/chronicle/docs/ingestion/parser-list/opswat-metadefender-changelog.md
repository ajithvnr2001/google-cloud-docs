---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opswat-metadefender-changelog/
title: Change log for OPSWAT_METADEFENDER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:26.596607+00:00
---

# Change log for OPSWAT_METADEFENDER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opswat-metadefender-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPSWAT_METADEFENDER

Date | Changes  
---|---  
2025-10-07 |  Enhancement:  
\- event.idm.read_only_udm.security_result.summary: Newly mapped OMSverdict, OMSoverallResult raw log field with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped OMSrequestId raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped OMSsource, OMSclientAddress raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped OMSsource, OMSclientAddress raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped intermediary_ip_1, intermediary_ip_2 raw log field with event.idm.read_only_udm.intermediary.ip UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped OMSruleName raw log field with event.idm.read_only_udm.security_result.rule_name UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped OMSdata_id raw log field with event.idm.read_only_udm.target.resource.id UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped OMSparent_data_id raw log field with event.idm.read_only_udm.principal.resource.id UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped OMSfileName raw log field with event.idm.read_only_udm.target.file.full_path UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped OMSfileSize raw log field with event.idm.read_only_udm.target.file.size UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped OMSfileTypeDesc raw log field with event.idm.read_only_udm.target.file.mime_type UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped OMSroot_data_id raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped OMSfirstchunk_ts, OMSlastchunk_ts, OMSthreatFoundCount, OMSembeddedObjectsWithThreat, OMStotalResultCount, OMSengines-metadata, OMSis_sync_scan, OMSworkflow_id, OMStotalProcessingTime, OMSid, OMSicapMethod, OMSicapWorkflow, OMSscanDuration, OMSaction, OMSblocked raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped OMSaction and OMSblocked raw log field with event.idm.read_only_udm.security_result.action UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped OMSuser raw log field with event.idm.read_only_udm.principal.user.userid UDM field.   
2024-10-29 |  Enhancement:  
\- Mapped `IP address` to `principal.ip`.  
\- Mapped `Sender` to `network.email.from`.  
\- Mapped `Recipients` to `network.email.to`.  
\- Mapped `Subject` to `metadata.description`.  
\- Mapped `OMSreason` to `security_result.action_details`.  
\- Mapped `OMSemail_sender` to `network.email.from`.  
\- Mapped `OMSemail_recipients` to `network.email.to`.  
\- Mapped `OMSsha256sum` to `target.file.sha256`.   
2024-10-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
