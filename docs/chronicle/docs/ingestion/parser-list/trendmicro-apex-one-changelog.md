---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-one-changelog/
title: Change log for TRENDMICRO_APEX_ONE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:32.051192+00:00
---

# Change log for TRENDMICRO_APEX_ONE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-one-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_APEX_ONE

Date | Changes  
---|---  
2026-04-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `TMCMdevicePlatform` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `filePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cnt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-01 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `ihost` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `ihost` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `deviceFacility` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `ApexCentralHost` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.observer.asset.hostname: Newly mapped `ApexCentralHost` raw log field with `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `cs2` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `cs2` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `suser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.   
2025-08-13 |  Enhancement:  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `fname` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- event.idm.read_only_udm.about.file.full_path: Removed mapping of `fname` from `event.idm.read_only_udm.about.file.full_path` UDM field. Added previously for the particular customer, now moved the same to conf file.   
2025-08-08 |  Enhancement:  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `fname` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.   
2025-08-05 |  Enhancement:  
\- Added a grok pattern to parse `intermediary.ip`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `intermediary.ip` and `intermediary.asset.ip`: Newly mapped `inter_ip` raw log field with `intermediary.ip` and `intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.   
2025-07-22 |  Enhancement:  
\- event.idm.read_only_udm.target.file.sha1: Newly mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- event.idm.read_only_udm.about.file.full_path: Removed mapping of `fileHash` from `event.idm.read_only_udm.about.file.full_path` UDM field. As it is more suitable to be mapped to `event.idm.read_only_udm.target.file.sha1`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `cs5` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field when `cs5Label` is `ActionResult`.   
2024-09-05 |  Enhancement:  
\- If `act` is `1` or `3` or `7` or `4`, then set `security_result.action` to `ALLOW`.  
\- If `act` is `2`, then set `security_result.action` to `BLOCK`.  
\- If `act` is `5` or `6`, then set `security_result.action` to `QUARANTINE`.  
\- If `act` is `8`, then set `security_result.action` to `ALLOW_WITH_MODIFICATION`.   
2024-07-30 |  Enhancement:  
\- Added support to handle JSON logs.   
2023-12-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
