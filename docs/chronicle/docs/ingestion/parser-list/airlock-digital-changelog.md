---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airlock-digital-changelog/
title: Change log for AIRLOCK_DIGITAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:06:37.963297+00:00
---

# Change log for AIRLOCK_DIGITAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airlock-digital-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AIRLOCK_DIGITAL

Date | Changes  
---|---  
2026-07-17 |  \- Added grok pattern to parse new format of `description` raw log field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `datetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` and `event.idm.read_only_udm.extensions.auth.type`: Mapped `event.idm.read_only_udm.metadata.event_type` as `USER_LOGIN` and `event.idm.read_only_udm.extensions.auth.type` as `SSO` when `task` is `login` and `auth_type` is `SSO`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-11-07 |  \- Added support for JSON logs.   
2024-06-18 |  \- Added a Grok pattern to parse the unparsed SYSLOG logs.   
2023-02-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
