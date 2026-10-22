---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-audit-changelog/
title: Change log for TRELLIX_HX_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:34.060154+00:00
---

# Change log for TRELLIX_HX_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRELLIX_HX_AUDIT

Date | Changes  
---|---  
2026-10-07 |  Enhancement:  
\- Added support for PersistenceItem audits.  
\- Mapped additional linkage, service, and digital signature metadata for PersistenceItem records.   
2026-10-06 |  \- Extend the TRELLIX_HX_AUDIT parser to support TaskItem items.   
2026-09-30 |  Enhancement:  
\- Added support for `PortItem` audit events.   
2026-09-24 |  Enhancement:  
\- Added support for RegistryItem audits.   
2026-09-21 |  Enhancement:  
\- Added support for ProcessItem audits.   
2026-09-11 |  Enhancement:  
\- Extended the parser to support `FileItem` audit events.   
2026-09-10 |  Enhancement:  
\- Added support for EventLogItem audits.   
2026-08-23 |  Enhancement:  
\- Mapped `network.ip_protocol` of `IPV6-ICMP` to `ICMP6`.  
\- Fixed registry events that have a value type of `REG_INVALID_TYPE`.  
\- Fixed process events that do not have parent process information.  
\- Fixed file write events that do not have parent process information.  
\- Skip file write events that have no filename.  
\- Fixed XPath typo `ipv4NetworkEventt` to `ipv4NetworkEvent` to correctly map  
localIPs for IPv4 network events.   
2026-08-05 |  \- Updated the parser `Product`, `Category`, `Supported Format`, `Reference` details.   
2026-02-20 |  Enhancement:  
\- Mapped `applianceId` itemList attribute to `metadata.product_deployment_id`.   
2026-02-18 |  Enhancement:  
\- Mapped target.process.file to target.file for PROCESS_MODULE_LOAD events.   
2025-11-14 |  Enhancement:  
\- Fixed bug where values of the `Registry value base64` label from one event  
in a list of XML audits may bleed into another.  
\- Added mappings to `network` from same values used in `target.network`.  
\- Removed dropping of events from loops.   
2025-09-18 |  Enhancement:  
\- Added mapping to `target.registry.registry_value_type` for registry audits.  
\- Added mapping to `target.hostname` for dnsLookupEvent audits.  
\- Fixed parsing of `principal.process.parent_process.pid`.  
\- Fixed parsing of `Writes`, `Number of Bytes Seen Written`, `Lowest File Offset Seen`  
`Closed`, and `Open Duration` target labels for FILE_MODIFICATION events.  
\- Fixed parsing of `process.file.full_path`.   
2025-07-21 |  Enhancement:  
\- Added mapping to `target.process.parent_process` to `processEvent` events.   
2025-07-19 |  Enhancement:  
\- Correctly map target.port for urlMonitorEvent events.  
\- Remove hostname from target.url for urlMonitorEvent events. The hostname  
is already present in target.hostname and may give the impression that the URL  
is fully qualified.   
2025-05-06 |  Populate target.labels `Device Path` for imageLoadEvent events.   
2025-02-10 |  Newly created parser. `ipv4NetworkEvent` mapped.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
