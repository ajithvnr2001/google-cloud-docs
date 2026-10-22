---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teradata-db-changelog/
title: Change log for TERADATA_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:33.623765+00:00
---

# Change log for TERADATA_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teradata-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TERADATA_DB

Date | Changes  
---|---  
2025-06-17 |  Enhancement:  
\- In this version some mappings were removed, as listed below, in order to introduce more accurate mappings for the relevant raw fields.  
\- Added new Grok pattern to parse raw log field.  
\- `event.idm.read_only_udm.principal.user.user_display_name` : Removed mapping of `profile_name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Mapped `profile_name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid` : Removed mapping of `proc_id` from `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.id` : Mapped `proc_id` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.user.userid` : Removed mapping of `user_id` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` : Mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp` : Newly mapped `collect_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `logon_date_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name` : Removed mapping of `user_name` from `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name` : Mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type` : Newly mapped `DATABASE` with `event.idm.read_only_udm.target.resource.resource_type` UDM field value when `default_database` raw log field is available.  
\- `event.idm.read_only_udm.target.resource.parent` : Newly mapped `logon_source` raw log field with `event.idm.read_only_udm.target.resource.parent` UDM field.  
\- `event.idm.read_only_udm.principal.application` : Removed mapping of `app_id` from `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id` : Mapped `app_id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` : Removed mapping of `client_id` from `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id` : Mapped `client_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code` : Newly mapped `error_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels` : Newly mapped `statement_type` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.groupid` : Newly mapped `statement_group` raw log field with `event.idm.read_only_udm.principal.user.groupid` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype` : Newly mapped `request_mode` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` : Newly mapped `tt_granularity` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `protocol`, `remote_hostname`, `logon_details`, `connection_id`, `port`, `cid`, and `jdbc_driver_info` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-21 |  Enhancement:  
\- Newly created parser.  
\- Mapped `ts` to `metadata.event_timestamp`.  
\- Mapped `profile_name` to `principal.user.user_display_name`.  
\- Mapped `app_id` to `principal.application`.  
\- Mapped `client_addr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `client_id` to `principal.user.userid`.  
\- Mapped `collect_timestamp` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `default_database` to `target.resource.name`.  
\- Mapped `error_code` to `security_result.detection_fields`.  
\- Mapped `error_text` to `security_result.summary`.  
\- Mapped `host_name` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `logon_date_time` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `logon_source` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `proc_id` to `principal.process.pid`.  
\- Mapped `query_text` to `target.process.command_line`.  
\- Mapped `request_mode` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `session_id` to `network.session_id`.  
\- Mapped `statement_group` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `statement_type` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `user_id` to `target.user.userid`.  
\- Mapped `user_name` to `target.user.user_display_name`.  
\- Set `metadata.vendor_name` to `TERADATA`.  
\- Set `metadata.product_name` to `TERADATA_DB`.  
\- Set `metadata.event_type` to `USER_RESOURCE_ACCESS`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on the presence of principal, principal user, and target resource.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
