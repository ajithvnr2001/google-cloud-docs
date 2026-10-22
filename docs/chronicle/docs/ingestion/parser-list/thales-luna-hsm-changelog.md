---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-luna-hsm-changelog/
title: Change log for THALES_LUNA_HSM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:34.120923+00:00
---

# Change log for THALES_LUNA_HSM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thales-luna-hsm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THALES_LUNA_HSM

Date | Changes  
---|---  
2025-09-12 |  Enhancement:  
\- Added new grok patterns to handle new format of syslogs  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field to `event.idm.read_only_udm.principal.port`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Mapped `event.idm.read_only_udm.network.ip_protocol` UDM field to `UDP` when `desc` has `UDP` in the string.   
2024-11-28 |  Enhancement:  
\- Mapped `user_id` to `target.user.userid`.   
2024-10-24 |  Enhancement:  
\- Mapped `user_id` to `target.user.userid`.   
2022-12-02 |  Enhancement:  
\- Added grok to parse logs containing `cni-podman1`, `IPv6` and `Code`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `group_id` from `target.user.groupid` to `target.user.group_identifiers`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
