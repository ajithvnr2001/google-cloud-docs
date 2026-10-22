---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-central-changelog/
title: Change log for SOPHOS_CENTRAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:54.676083+00:00
---

# Change log for SOPHOS_CENTRAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-central-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOPHOS_CENTRAL

Date | Changes  
---|---  
2026-02-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Removed mapping of `source` from `event.idm.read_only_udm.principal.application` UDM field.As it was not required.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Changed mapping for `event.idm.read_only_udm.principal.user.user_display_name`. It is now mapped from source if `source` is not empty, otherwise it is mapped from `Username`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `Username` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field. When `source` is not empty.  
\- Added `action` in overwrite   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Removed mapping of `source` from `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `source` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field. As it is more relevant mapping.  
\- `event.idm.read_only_udm.principal.cloud.availability_zone`: Removed mapping of `location` from `event.idm.read_only_udm.principal.cloud.availability_zone` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Mapped `location` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field. As it is more relevant mapping.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `source` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `location` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `file_path_1` raw log field(s) with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action_1` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.  
\- A new field udn_from_grok has been introduced to act as a flag, preventing the source field from being mapped to principal.user.user_display_name if it has already been processed by a specific grok pattern.   
2026-01-09 |  Enhancement:  
If user_id exists:  
\- event.idm.read_only_udm.principal.user.userid: Mapped user_id raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.application: Mapped source raw log field to event.idm.read_only_udm.principal.application UDM field.  
\- event.idm.read_only_udm.principal.cloud.availability_zone: Mapped location raw log field to event.idm.read_only_udm.principal.cloud.availability_zone UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Changed event type from USER_RESOURCE_ACCESS to USER_UNCATEGORIZED.  
If user_id does not exist:  
\- event.idm.read_only_udm.principal.user.userid: Mapped source raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.cloud.availability_zone: Removed mapping of location from event.idm.read_only_udm.principal.cloud.availability_zone UDM field,as it is more suitable for `event.idm.read_only_udm.principal.location` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Mapped location raw log field to event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Mapped location raw log field to event.idm.read_only_udm.principal.asset.hostname UDM field.   
2025-12-01 |  Enhancement:  
\- Modified grok pattern for event type `Event::Endpoint::DataLossPreventionAutomaticallyAllowed` to newly extract `Username`, `app`, and `act` and enhance parsing of `name` field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `created_at` and `datastream` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `Username` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.   
2025-07-30 |  Enhancement:  
\- Added initial declaration for `application` raw field to avoid parsing error.  
\- Added a null check for `target.process.file.full_path`.   
2025-01-30 |  Enhancement:  
\- Added support to parse unparsed JSON logs.   
2025-01-08 |  Enhancement:  
\- Added `url`, `action`, and `scan_name` in statedata to parse unparsed logs.  
\- Mapped `user_id` to `principal.user.userid`.   
2024-09-05 |  Enhancement:  
\- Added support to parse unparsed JSON logs.  
\- Mapped `location` to `principal.cloud.availability_zone`.   
2024-05-17 |  Enhancement:  
\- Mapped `data.core_remedy_items.items.0.descriptor` and `core_remedy_items.items.0.descriptor` to `target.process.file.full_path`.   
2024-05-14 |  Bug-Fix:  
\- Changed mapping of `target.user.userid` from `duid` to `suser`.  
\- Mapped `duid` to `security_result.detection_fields`.   
2022-12-27 |  Enhancement -  
\- Creating a new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
