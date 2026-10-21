---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bloxone-changelog/
title: Change log for BLOXONE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:20:14.400418+00:00
---

# Change log for BLOXONE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bloxone-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BLOXONE

Date | Changes  
---|---  
2025-01-07 |  Enhancement:  
\- Added a new Grok pattern to parse unparsed logs.  
\- Mapped `intermediaryhost` to `intermediary.hostname`.   
2024-12-02 |  Enhancement:  
\- If `raw.app` is a valid application_protocol value, it is mapped to `network.application_protocol`.   
2024-06-18 |  Enhancement:  
\- Added support to handle CEF logs.   
2024-01-18 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Mapped `network` to `principal.hostname`, and `principal.asset.hostname`.  
\- Mapped `device` to `principal.ip`, and `principal.asset.ip`.  
\- Mapped `rip` to `target.ip`, and `target.asset.ip`.  
\- Mapped `mac_address` to `principal.mac`.  
\- Mapped `country` to `principal.location.name`.  
\- Mapped `os_version` to `principal.platform_version`.  
\- Mapped `app_name` to `principal.application`.  
\- Mapped `user` to `principal.user.user_display_name`.  
\- Mapped `feed_type` to `principal.resource.attribute.labels`.  
\- Mapped `feed_name` to `principal.resource.name`, and `principal.resource.resource_subtype`.  
\- Mapped `policy_action` to `security_result.action_details`.  
\- Mapped `endpoint_groups`, `user_groups`, `dns_view`, `dhcp_fingerprint`, `policy_name`, `tclass`, `tproperty`, `threat_indicator`, `category`, and `rcode` to `security_result.detection_fields`.  
\- Mapped `app_category` to `security_result.category_details`.  
\- Mapped `confidence` to `security_result.confidence`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `qname` to `questions.name`.  
\- Mapped `rdata` to `dns.answers`.   
2023-03-07 |  Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
