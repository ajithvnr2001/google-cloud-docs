---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyolo-ot-changelog/
title: Change log for CYOLO_OT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:48.735023+00:00
---

# Change log for CYOLO_OT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyolo-ot-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYOLO_OT

Date | Changes  
---|---  
2025-12-22 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`,`event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `inter_host` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cyolosubjectname` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `cyolocountrycode` raw log field(s) with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `cyolosubjectid` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field(s) with `event.idm.read_only_udm.target.ip`and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `cyoloobjname` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `cyoloobjid` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `cyolosessionid` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`,`event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `cyolouagent` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `cyoloauthid` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `cyoloauthname` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `cyolosubjectkind` raw log field(s) with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `cyoloobjkind` raw log field(s) with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `prod_type` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cyoloauthkind`, `cyolokind`, `cyoloresult` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cyolodstid` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cef_version`, `Signature_id`, `cef_severity`, `start`, `act`, `cyolotransid`, `cyolocredentialsorigin`, `cyolocredentialsid`, `cyolocredentialsname` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Assigned the values of certain fields to a third variable and used it as conditional check to prevent future errors.  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for `USER_LOGOUT` event type, if `message` =~ `user disconnected` and `has_user` == `true` and `has_target` == `true`, updated to USER_LOGOUT.  
\- Modified the grok pattern to parse raw log correctly.  
\- Removed unnecessary gsub blocks and used single gsub to split the field in `kv_data` and `kv_data1`.  
\- Added a conditional check before mapping `duration_str` field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-10-14 |  Enhancement:  
\- Added support for new log format.  
\- `event.idm.read_only_udm.security_result.outcome`: Newly mapped `result` to `event.idm.read_only_udm.security_result.outcome` and `event.idm.read_only_udm.security_result.action`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `credentials_origin`, `credentials_id`, and `credentials_name` to `event.idm.read_only_udm.principal.user.attribute.labels`.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `asset_id` to `event.idm.read_only_udm.target.asset.asset_id`.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly Mapped `asset_name` to `event.idm.read_only_udm.target.asset.product_object_id`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `remote_address` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `remote_address` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `country_code` raw log field(s) with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `destination_host` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `destination_host` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination_port` raw log field(s) with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `subject_name` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `subject_id` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `object_name` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `object_id` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `duration_str` (from `message`), `subject_kind`, `authority_kind`, `log_level`, `object_kind` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `client` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `client` raw log field(s) with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `authority_id` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `authority_name` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped fields from the `rules` array raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `hostname` raw log field(s) with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.resource.product_object_id`: Newly mapped `node_id` raw log field(s) with `event.idm.read_only_udm.observer.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `site_id`, `log_source`, `site_name`, `container_id`, `transaction_id`, `event_id` raw log field(s) with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `kind` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped hardcoded value `MACHINE` with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped hardcoded value `RDP` with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- Renamed from `observer` to `event.idm.read_only_udm.observer`.  
\- Renamed from `network` to `event.idm.read_only_udm.network`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `message` contains `user disconnected` and `has_user` is `true`, updated to `USER_LOGOUT`.  
\- Added a new grok pattern to support parsing for a new JSON-based log format in addition to the existing key-value format.   
2025-02-21 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
