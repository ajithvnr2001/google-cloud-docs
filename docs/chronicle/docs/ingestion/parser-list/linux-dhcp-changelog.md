---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-dhcp-changelog/
title: Change log for LINUX_DHCP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:16.473792+00:00
---

# Change log for LINUX_DHCP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-dhcp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LINUX_DHCP

Date | Changes  
---|---  
2024-09-05 |  Enhancement-  
Added a new Grok pattern to parse new types of unparsed logs of format SYSLOG.   
2023-11-10 |  Enhancement-  
Added a new Grok pattern to parse new type of unparsed logs of format SYSLOG.   
2022-09-05 |  Enhancement-  
Migrated the custom parsers into default parser.   
2022-08-19 |  Fix-  
\- Added a new grok for the logs with timestamp of ISO8601 format.  
\- Mapped sc_summary to `security_result.summary`.  
\- Mapped chaddr1 to `principal.mac`.   
2022-08-04 |  Enhancement  
-Parsed logs of type `dhcpd` which were not handled earlier.  
-Added check for ciaddr,chaddr.  
-Mapped `src_ip` to `principal.ip`.  
-Mapped `metadata.event_type` to `STATUS_UPDATE` where type includes `RELEASE` and ciaddr is null.  
-Mapped `metadata.event_type` to `STATUS_UPDATE` where `metadata.event_type` to `GENERIC_EVENT` and `src_ip` is not null.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
