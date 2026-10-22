---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-audit-changelog/
title: Change log for WORKDAY_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:51.481700+00:00
---

# Change log for WORKDAY_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKDAY_AUDIT

Date | Changes  
---|---  
2026-02-02 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Tenant` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Entry_Moment` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Action` raw log field to `event.idm.read_only_udm.security_result.action`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `Action` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_ID` parsed from `Changed_Made_By` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` parsed from `Changed_Made_By` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_ID` parsed from `Changed_Made_On` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `user_name` parsed from `Changed_Made_On` raw log field to `event.idm.read_only_udm.target.user.user_display_name`.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `Changed_Made_By` field is present.   
2025-12-17 |  Enhancement:  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `AuthenticationChannel` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field which was previously mapped to deprecated field `about.labels` and is now mapped to `additional.fields` since that is a more appropriate field.  
\- Added conditional check for `AuthFailMessage`.   
2025-11-20 |  Enhancement:  
\- event.idm.read_only_udm.target.application: Newly mapped `Worker` raw log field to `event.idm.read_only_udm.target.application`.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `target_name` raw log field to `event.idm.read_only_udm.target.user.user_display_name`.  
\- event.idm.read_only_udm.about.labels: Removed mapping of `AuthenticationChannel` from `event.idm.read_only_udm.about.labels` as the `about.labels` UDM field is deprecated.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Newly mapped `AuthenticationChannel` raw log field to `event.idm.read_only_udm.about.resource.attribute.labels`.  
\- Updated mapping for `event.idm.read_only_udm.security_result.action_details` from the static string `IsDeviceManaged` to the value of the `IsDeviceManaged` raw log field.   
2025-07-28 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `sessionid` raw log field with `event.idm.read_only_udm.network.session_id`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip`.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `status_code` raw log field with `event.idm.read_only_udm.network.http.response_code`.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if src_ip is not empty.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if primaryName is not empty.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `context`, `devicetype`, `browser`, `authmethod` raw log fields with `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp`.   
2025-01-30 |  Enhancement:  
\- `about_*` fields are changed to avoid duplicate fields.  
\- Removed the field `ClassOfInstance` field from `column8`.  
\- Mapped `column11` to `SecurityGroupModified`.  
\- Mapped `SecurityGroupModified` to `security_result.about.group.group_display_name`.  
\- Removed the field `ChangedRelationship` from `target.user.attributes.roles.name`.  
\- Removed the field `target.resource.attribute.labels.key/value` from `InstancesRemoved`.   
2024-11-06 |  Enhancement:  
\- Mapped `ClassOfInstance` to `metadata.description`.  
\- Mapped `ChangedRelationship` to `target.user.attribute.roles.name`.  
\- Mapped `InstancesRemoved` to `target.resource.attribute.labels`.   
2024-10-04 |  Enhancement:  
\- Modified the Grok patterns to parse the fields correctly.   
2023-12-08 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
