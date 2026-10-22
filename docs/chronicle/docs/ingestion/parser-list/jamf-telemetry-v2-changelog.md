---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-telemetry-v2-changelog/
title: Change log for JAMF_TELEMETRY_V2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:41.669517+00:00
---

# Change log for JAMF_TELEMETRY_V2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-telemetry-v2-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JAMF_TELEMETRY_V2

Date | Changes  
---|---  
2025-11-19 |  1) Update Field Mapping - change the UDM field  
\- For Event Type 9:  
\- `udm.target.process.pgid`: Removed mapping of `event.exec.target.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.target.process.pgid`: Mapped `event.exec.target.group_id` to `udm.target.process.pgid`.  
\- For Event Type 125:  
\- `udm.target.process.pgid`: Removed mapping of `event.btm_launch_item_remove.app.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.target.process.pgid`: Mapped `event.btm_launch_item_remove.app.group_id` to `udm.target.process.pgid`.  
\- For Event Type 126:  
\- `udm.principal.process.pgid`: Removed mapping of `event.profile_add.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.profile_add.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 127:  
\- `udm.principal.process.pgid`: Removed mapping of `event.profile_remove.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.profile_remove.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 132:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_group_add.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_group_add.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 133:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_group_remove.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_group_remove.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 134:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_group_set.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_group_set.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 135:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_modify_password.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_modify_password.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 136:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_disable_user.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_disable_user.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 137:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_enable_user.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_enable_user.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 138:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_attribute_value_add.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_attribute_value_add.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 139:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_attribute_value_remove.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_attribute_value_remove.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 140:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_attribute_set.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_attribute_set.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 141:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_create_user.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_create_user.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 142:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_create_group.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_create_group.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 143:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_delete_user.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_delete_user.instigator.group_id` to `udm.principal.process.pgid`.  
\- For Event Type 144:  
\- `udm.principal.process.pgid`: Removed mapping of `event.od_delete_group.instigator.group_id` from `event1.idm.read_only_udm.additional.fields`.  
\- `udm.principal.process.pgid`: Mapped `event.od_delete_group.instigator.group_id` to `udm.principal.process.pgid`.  
2) Additional Events Parsing  
\- Added support for the events `9010`, `19010`, `10147`, `147`, `10084`, `84`, `10083`, `83`.   
2025-05-08 |  Newly created JAMF_TELEMETRY_V2 Gold parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
