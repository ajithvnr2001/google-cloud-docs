---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-alerts-changelog/
title: Change log for TRELLIX_HX_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:20:27.418424+00:00
---

# Change log for TRELLIX_HX_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRELLIX_HX_ALERTS

Date | Changes  
---|---  
2026-09-03 |  Enhancement:  
\- Added support for alerts ingested via webhook.  
\- Mapped hostname, IP address, and MAC address from webhook alerts to  
`principal.hostname`, `principal.ip`, `principal.mac`, and corresponding  
`principal.asset` fields.   
2026-09-02 |  Enhancement:  
\- Mapped the alert `source` to `additional.fields[`source`]`.   
2026-08-18 |  Enhancement:  
\- Added support for `AMSI` source events.   
2026-08-13 |  Enhancement:  
\- Added support for `MAL` source events.  
\- Mapped infected file details to `security_result.about.file`.  
\- Added mappings for processing detections loop.   
2025-11-14 |  Enhancement:  
\- Added mappings to `network` from same values used in `target.network`.   
2025-09-18 |  Enhancement:  
\- Added mapping to `target.registry.registry_value_type` for registry events.  
\- Added mapping to `target.hostname` for dnsLookupEvent events.   
2025-07-21 |  Enhancement:  
\- Added mapping to `target.process.parent_process` to `processEvent` events.   
2025-07-19 |  Enhancement:  
\- Correctly map target.port for urlMonitorEvent events.  
\- Remove hostname from target.url for urlMonitorEvent events. The hostname  
is already present in target.hostname and may give the impression that the URL  
is fully qualified.   
2025-05-06 |  Populate target.labels `Device Path` for imageLoadEvent events.   
2025-05-01 |  Populate target.labels `Registry value base64` for regKeyEvent events.  
In target.registry.registry_value_data, use regKeyEvent/value if regKeyEvent/text is not set.   
2025-03-31 |  Fix unparsed logs when event_values.__parentProcess is not set.   
2025-03-26 |  Add fallback mappings to multi_indicator for IOC security results when indicator field is not preset.   
2025-02-26 |  Mappings for regKeyEvent IOC event type.   
2025-02-20 |  Initial mappings for TRELLIX_HX_ALERTS logtype.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
