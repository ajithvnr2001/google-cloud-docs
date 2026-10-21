---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tableau-changelog/
title: Change log for TABLEAU \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:14:56.909395+00:00
---

# Change log for TABLEAU  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tableau-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TABLEAU

Date | Changes  
---|---  
2026-08-25 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `eventProcessedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `eventVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `eventCategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actorUserId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.role_name`: Newly mapped `licensingRoleName` raw log field with `event.idm.read_only_udm.principal.user.role_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `viewLuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `repositoryUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `ownerName` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `systemAdminLevel`, `siteRoleId`, `initiatingUserLuid`, `initiatingUserId`, `actorUserLuid` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field when key1 is equal to `systemAdminLevel`, `siteRoleId`, `initiatingUserLuid`, `initiatingUserId`, `actorUserLuid`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `index`, `firstPublishedAt`, `fields`, `revision`, `sheetId`, `caption`, `siteName`, `siteLuid`, `workbookLuid`, `workbookName`, `ownerLuid`, `title`, `sheetType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-02-09 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
`event.idm.read_only_udm.principal.user.userid`: Newly mapped `temp_user`, `user_name` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
`event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `temp_domain` raw log field(s) with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
`event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `temp_role` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
`event.idm.read_only_udm.additional.fields`: Newly mapped `source_info` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
`event.idm.read_only_udm.principal.application`: Newly mapped `user_application` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
`event.idm.read_only_udm.target.url`: Newly mapped `temp_http_uri`, `temp_api_call` raw log field(s) with `event.idm.read_only_udm.target.url` UDM field.  
`event.idm.read_only_udm.target.resource.name`: Newly mapped `temp_site_id`, `java_method` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
`event.idm.read_only_udm.target.resource.type`: Newly mapped `java_class` raw log field(s) with `event.idm.read_only_udm.target.resource.type` UDM field.  
`event.idm.read_only_udm.network.http.method`: Newly mapped `temp_http_method` raw log field(s) with `event.idm.read_only_udm.network.http.method` UDM field.  
`event.idm.read_only_udm.network.http.response_code`: Newly mapped `temp_http_status` raw log field(s) with `event.idm.read_only_udm.network.http.response_code` UDM field.   
2026-01-09 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `TimeGenerated` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `_TimeReceived` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_IsBillable` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_BilledSize` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_Internal_WorkspaceResourceId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_ItemId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TenantId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_SubscriptionId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `_ResourceId` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `FilePath` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `temp_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `temp_logger_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `temp_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `temp_thread_name` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `temp_log_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-12-17 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `appname` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id2` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `id1` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.observer.process.command_line`: Newly mapped `logger` raw log field with `event.idm.read_only_udm.observer.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `loglevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `site_id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `script_type` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `id3`, `thread` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `function_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2024-12-19 |  Enhancement:  
\- Mapped `Content` to `metadata.description`.  
\- Mapped `http_version` to `network.application_protocol_version`.   
2024-07-09 |  Enhancement:  
\- Added a Grok pattern to identify full_path filled values.  
\- Added if condition to check null or not.   
2024-06-03 |  \- Reviewer-suggested.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
