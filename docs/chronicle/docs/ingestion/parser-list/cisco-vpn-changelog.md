---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vpn-changelog/
title: Change log for CISCO_VPN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:10:05.441999+00:00
---

# Change log for CISCO_VPN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vpn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_VPN

Date | Changes  
---|---  
2025-03-13 |  Enhancement:  
\- Added a grok pattern to parse `userId` from the log.  
\- Added a grok pattern to parse `hostname` from the log.   
2025-01-30 |  Enhancement:  
\- Mapped `puser_id` to `principal.user.userid`.   
2024-12-18 |  Enhancement:  
\- Added support for new format of logs.   
2024-12-05 |  Enhancement:  
\- Added support to parse new format of unparsed SYSLOG logs.   
2024-11-07 |  Enhancement:  
\- Added support to parse new format of unparsed SYSLOG logs.   
2024-07-02 |  Enhancement:  
\- Added support to parse new format of unparsed logs.  
\- Changed `src_ip` mapping from `target.ip` to `principal.ip`.  
\- Changed `dst_ip` mapping from `principal.ip` to `target.ip`.   
2024-05-27 |  Enhancement:  
\- Added support to parse dropped logs that wer dropped due to UDM validation and a missing target field.   
2024-03-25 |  Enhancement:  
\- Added support to parse new format unparsed logs.   
2024-02-23 |  Enhancement:  
\- Parsed the logs with event IDs `733100`,`725011`,`737034`,`737006`,`106023`.  
\- Added `on_error` check for Grok patterns.   
2024-01-15 |  Enhancement:  
\- Added new Grok patterns for the support of new patterns of syslog logs.  
\- If `observer.ip` is a valid IP value, mapped `observer` to `observer.ip`.   
2022-08-19 |  Enhancement - Parsed The logs with event_id's :- `113012`,`113015`,`722033`,`722035`,`716058`,`716002`,`716038`,`722028`,`722032`,`722034`,`716001`,`716059`,`305012`,`106015`,  
`305011`,`302015`,`302016`,`725016`,`302020`,`302014`,`302013`,`302021`,`106006`,`110002`,`605005`,`605004`,`106001`,`734003`,`734001`,`725002`,`607001`,`725001`,`106012`,  
`725005`,`611101`,`611102`,`402119`,`737026`,`313009`,`725007`,`725003`,`109207`,`500003`,`500004`,`444100`,`444102`,`602303`,`602304`,`315011`,`602101`,`302004`.  
\- Updated the event_type from `GENERIC_EVENT` to `USER_UNCATEGORIZED` when event_id=`113014`.  
\- Updated the event_type from `GENERIC_EVENT` to `USER_LOGIN` when event_id=`113016`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
