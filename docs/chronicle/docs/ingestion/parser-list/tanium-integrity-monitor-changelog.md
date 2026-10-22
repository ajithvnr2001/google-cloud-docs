---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-integrity-monitor-changelog/
title: Change log for TANIUM_INTEGRITY_MONITOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:03.956229+00:00
---

# Change log for TANIUM_INTEGRITY_MONITOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-integrity-monitor-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_INTEGRITY_MONITOR

Date | Changes  
---|---  
2025-10-28 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Computer_Name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `Process_Path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Event_Time`, `Hashed_At` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Event_Time`, `Hashed_At`, and `Watchlists` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `FILE_MODIFICATION` if `has_principal` is `true`, `has_file` is `true` and `message` contains `write`.  
\- Renamed from computer_name to Computer_Name.  
\- Renamed from process_path to Process_Path.  
\- Renamed from file_path to File_Path.  
\- Renamed from change_type to Change_Type.  
\- Renamed from hashed_at to Hashed_At.   
2022-10-12 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
