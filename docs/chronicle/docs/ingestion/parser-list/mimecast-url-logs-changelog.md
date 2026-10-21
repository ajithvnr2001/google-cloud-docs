---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-url-logs-changelog/
title: Change log for MIMECAST_URL_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:46:40.895962+00:00
---

# Change log for MIMECAST_URL_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-url-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MIMECAST_URL_LOGS

Date | Changes  
---|---  
2026-07-13 |  Enhancement:  
\- Added support to parse multi event logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.mimecastEventType`, `record.emailPartsDescription`, `userAwarenessAction`, `actions`, `emailPartsDescription`, `mimecastEventType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Added a gsub for existing mapping of `userEmailAddress` to parse `event.idm.read_only_udm.network.email.to` UDM field correctly.  
\- `event.idm.read_only_udm.network.email.from`: Added a gsub for existing mapping of `fromUserEmailAddress` to parse `event.idm.read_only_udm.network.email.from` UDM field correctly.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `route` and `record.route` raw log fields with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `record.userEmailAddress` and `record.fromUserEmailAddress` are present, updated the value of `event.idm.read_only_udm.metadata.event_type` to `EMAIL_TRANSACTION` else updated the value of `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2025-01-16 |  Enhancement:  
\- Added support for unparsed logs.   
2024-09-23 |  Enhancement:  
\- When `action` is block then mapped `security_result.action` to `BLOCK`.  
\- When `action` is warn then mapped action to `security_result.action_details`.   
2024-06-12 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
