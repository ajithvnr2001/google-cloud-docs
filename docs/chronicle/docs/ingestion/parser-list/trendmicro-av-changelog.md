---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-av-changelog/
title: Change log for TRENDMICRO_AV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:33.524089+00:00
---

# Change log for TRENDMICRO_AV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-av-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_AV

Date | Changes  
---|---  
2023-05-21 |  Enhancement:  
\- Mapped `Received`,`Generated` to `about.labels`.   
2023-05-09 |  Enhancement - For logs with CEF format, mapped syslog timestamp to `metadata.event_timestamp`.   
2023-02-03 |  Enhancement  
\- Mapped `metadata.event_type` to `SCAN_UNCATEGORIZED` if log type is `LogSpyware`,`LogPredictiveMachineLearning`.  
\- Mapped `Device_name`,`Enhetsnavn` to `principal.hostname`.  
\- Mapped `Domain`,`Domene` to `principal.administrative_domain`.  
\- Mapped `Group_name`,`Gruppenavn` to `principal.group.group_display_name`.  
\- Mapped `Mottatt` to `metadata.collected_timestamp`.  
\- Mapped `Generert`,`Generated` to `metadata.event_timestamp`.  
\- Mapped `Subject`,`Emne`,`Path` to `about.process.command_line`.  
\- Mapped `Type`,`Scan_Type` to `security_result.description`.  
\- Mapped `User`,`Bruker` to `target.user.userid`.  
\- Mapped `CustomerName` to `target.user.user_display_name`.  
\- Mapped `File_name`,`Object`,`Objekt`,`Infected_Resource` to `target.process.file.full_path`.  
\- Mapped `Action_Taken` to `security_result.action_details`.  
\- Mapped `Spyware`,`Virus_Malware_Name`,`Unknown_Threat` to `security_result.threat_name`.   
2022-05-30 |  Added support for CEF format logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
