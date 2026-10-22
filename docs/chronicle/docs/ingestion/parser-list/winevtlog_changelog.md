---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog_changelog/
title: Change log for WINEVTLOG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:52.127035+00:00
---

# Change log for WINEVTLOG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINEVTLOG 

Date | Changes | 2022-04-27 | Promoted Gold Parser from test to new global default.   
  
---|---  
2022-04-22 |  1) Added EventID 1202 (Provider name: SceCli) and Event ID 102 (Provider Name: Microsoft-Windows-TaskScheduler).   
  
2022-04-21 |  1) For every event mapped Message field for Microsoft-Windows-Security-Auditing.   
2) For EventID 5137 mapped ObjectClass, ObjectDN.   
3) For EventID 5136 mapped AttributeValue.   
4) For EventID 4769 mapped TicketOptions, TicketEncryptionType.   
5) For EventID 4662 mapped ObjectType   
6) For EventID 4625 mapped FailureReason   
7) For EventID 4742 mapped SubjectLogonId   
8) Mapped Computer as intermediary.hostname.   
  
2022-03-30 |  1) Added mapping of `Channel` field for all the Event IDs.   
2) For EventID `5861` and SourceName `Microsoft-Windows-WMI-Activity`, changed mapping of `Channel` field from `security_result.summary` to `about.labels.key/value`.   
3) Added mapping of Task field for Event ID 4702.   
4) Extracted Event Description from Message field for Event ID 4767.   
5) Added gsub to handle "·" present in Message field for Event ID 4719.   
6) Added mapping of DSName and DSType field for Event ID 5137 & 5141\.   
7) Added mapping of ObjectClass field for Event ID 5141.   
8) Added mapping of OriginalVolume(Data_9), ShadowDeviceName(Data_8) and ProcessName(Data_3) field for Event ID 8222.   
9) Added mapping of OriginalVolume(Data_8) and ShadowDeviceName(Data_7) field for Event ID 8223.   
  
2022-03-29 |  1) Added mapping of TargetLogonId field for Event ID 4624.   
2) Added mapping of ServiceSid field for Event ID 4769.   
3) Added mapping of NewObjectDN and OldObjectDN fields for Event ID 5139.   
4) Added mapping of DnsHostName field for Event ID 4741.   
5) Added mapping for SubjectLogonId field.   
6 )Mapped actual hostname from FQDN name in Event ID 4768.   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
