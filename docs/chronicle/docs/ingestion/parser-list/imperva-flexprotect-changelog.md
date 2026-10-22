---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-flexprotect-changelog/
title: Change log for IMPERVA_FLEXPROTECT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:15.411877+00:00
---

# Change log for IMPERVA_FLEXPROTECT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-flexprotect-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_FLEXPROTECT

Date | Changes  
---|---  
2023-08-28 |  Enhancement:  
\- Mapped `qstr` to `security_results.detection_fields`.   
2023-07-10 |  Parsed and mapped additional fields.  
\- Mapped `fileId` to `network.session_id`  
\- Mapped `siteid` to `security_results.detection_fields`.  
\- Mapped `suid` to `principal.user.userid`.  
\- Mapped `device_facility` to `principal.location.city`.  
\- Mapped `ccode` to `principal.location.country_or_region`.  
\- Mapped `cicode` to `principal.location.city`.  
\- Mapped `Customer` to `principal.user.user_display_name`.  
\- Mapped `start` to `security_result.detection_fields.event_start_time`.  
\- Mapped `cn1` to `network.http.response_code`.  
\- Mapped `sip` to `target.ip`.  
\- Mapped `spt` to `target.port`.  
\- Mapped `cpt` to `principal.port`.  
\- Mapped `ver` to `tls.version`.  
\- Mapped `cs8Label` to `additional_cs8.key`.  
\- Mapped `cs8` to `additional_cs8.value.string_value`.  
\- Mapped `cs9Label` to `additional_cs9.key`.  
\- Mapped `cs9` to `additional_cs9.value.string_value`.  
\- Mapped `end` to `security_result.detection_fields.event_end_time`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
