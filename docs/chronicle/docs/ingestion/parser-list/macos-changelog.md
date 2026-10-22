---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/macos-changelog/
title: Change log for MACOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:41.989404+00:00
---

# Change log for MACOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/macos-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MACOS

Date | Changes  
---|---  
2026-07-09 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Changed mapping for keys within `backtrace.frames`. Previously, these keys were mapped directly. Now, they are mapped with an index suffix to reflect their position in the `backtrace.frames` array.  
\- Added support for additional timestamp formats in the date filter.   
2025-12-18 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `eventMessage` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `senderImagePath` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processImagePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userID` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `activityIdentifier`, `bootUUID`, `category`, `formatString`, `machTimestamp`, `messageType`, `parentActivityIdentifier`, `processImageUUID`, `senderImageUUID`, `senderProgramCounter`, `subsystem`, `threadID`, `traceID`, and fields from `backtrace.frames` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to USER_UNCATEGORIZED when a userID is present.   
2024-09-18 |  Enhancement:  
\- Added support to handle unparsed JSON logs.   
2022-05-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
