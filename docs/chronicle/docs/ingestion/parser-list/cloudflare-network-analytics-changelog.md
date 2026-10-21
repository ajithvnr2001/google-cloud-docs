---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-network-analytics-changelog/
title: Change log for CLOUDFLARE_NETWORK_ANALYTICS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:49.502631+00:00
---

# Change log for CLOUDFLARE_NETWORK_ANALYTICS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-network-analytics-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDFLARE_NETWORK_ANALYTICS

Date | Changes  
---|---  
2025-09-11 |  Enhancement:  
\- Replaced `sec_result` to `security_result` for mapping action.   
2025-08-26 |  Enhancement:  
\- event.idm.read_only_udm.network.ip_protocol: Newly Mapped IPProtocol raw log field to event.idm.read_only_udm.network.ip_protocol UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly Mapped Outcome raw log field to event.idm.read_only_udm.security_result.action UDM field.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `SourceASN` from event.idm.read_only_udm.additional.fields UDM field. (incorrect mapping)  
\- event.idm.read_only_udm.principal.network.asn: Mapped SourceASN raw log field to event.idm.read_only_udm.principal.network.asn UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `DestinationASN` from event.idm.read_only_udm.target.resource.attribute.labels UDM field. (incorrect mapping)  
\- event.idm.read_only_udm.target.network.asn: Mapped DestinationASN raw log field to event.idm.read_only_udm.target.network.asn UDM field.   
2025-02-10 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
