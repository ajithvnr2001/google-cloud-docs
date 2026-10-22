---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-net-policy-server-changelog/
title: Change log for WINDOWS_NET_POLICY_SERVER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:06.674287+00:00
---

# Change log for WINDOWS_NET_POLICY_SERVER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-net-policy-server-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_NET_POLICY_SERVER

Date | Changes  
---|---  
2024-12-26 |  \- Added support for JSON logs.   
2024-12-05 |  \- Added a new Grok pattern to extract `src_ip` and mapped it to `principal.ip` and `principal.asset.ip`.   
2024-03-27 |  \- Added a check for `calling_station_id`, `device-mac` and `mac_address`.  
\- If `nas_port` is not in the range 1 and 65535, then mapped `nas_port` to `target.resource.attribute.labels`.   
2022-11-21 |  \- Mapped event_source to target.application  
\- added new grok pattern to parse the data  
\- Mapped called-station_Id/macaddress to target.mac  
\- Mapped calling-station-Id/macaddress to principal.mac   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
