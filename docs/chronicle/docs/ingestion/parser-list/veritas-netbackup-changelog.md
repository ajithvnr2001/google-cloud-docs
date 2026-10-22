---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veritas-netbackup-changelog/
title: Change log for VERITAS_NETBACKUP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:30.760875+00:00
---

# Change log for VERITAS_NETBACKUP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veritas-netbackup-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VERITAS_NETBACKUP

Date | Changes  
---|---  
2026-02-06 |  Enhancement:  
\- `event.idm.read_only_udm.observer.hostname`: Removed mapping of `obs_hostname` from `event.idm.read_only_udm.observer.hostname` UDM field in order to introduce more appropriate UDM mapping.  
\- Renamed the field `obs_hostname` in the grok to `intermediary_hostname` to better represent the field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `intermediary_hostname` to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.user.userid`: Removed mapping of `app_user` from `event.idm.read_only_udm.observer.user.userid` UDM field in order to introduce more appropriate UDM mapping.  
\- `event.idm.read_only_udm.intermediary.user.userid`: Mapped `app_user` to `event.idm.read_only_udm.intermediary.user.userid` UDM field.   
2026-01-15 |  Enhancement:  
\- Enhanced the grok pattern to parse the new pattern with RFC5424 syslog headers.  
\- The parsing logic was updated to support RFC5424 and ISO8601 timestamp formats for the ts field.   
2025-10-23 |  Enhancement:  
\- Enhanced the grok pattern for event_datetime to extract the date along with the timezone.   
2025-10-01 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `ts` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field and mapped `event_datetime` instead if `event_datetime` is present.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `event_ts` and `event_action` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-08 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped originator_host, host_type, product, p_uuid, schedule, response_time_ms, reason raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped accessed_from raw log field(s) with event.idm.read_only_udm.principal.application UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped p_hostname raw log field(s) with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped p_hostname raw log field(s) with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped p_ip raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped p_ip raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped p_port raw log field(s) with event.idm.read_only_udm.principal.port UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped process_name raw log field(s) with event.idm.read_only_udm.principal.process.file.names UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped user_id raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped login_host raw log field(s) with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped login_host raw log field(s) with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped d_ip raw log field(s) with event.idm.read_only_udm.target.ip UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped d_ip raw log field(s) with event.idm.read_only_udm.target.asset.ip UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped d_port raw log field(s) with event.idm.read_only_udm.target.port UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped target_user raw log field(s) with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped obs_hostname raw log field(s) with event.idm.read_only_udm.observer.hostname UDM field.  
\- event.idm.read_only_udm.observer.user.userid: Newly mapped app_user raw log field(s) with event.idm.read_only_udm.observer.user.userid UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped exit_code raw log field(s) with event.idm.read_only_udm.security_result.action UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped auth_status raw log field(s) with event.idm.read_only_udm.security_result.action_details UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped operation raw log field(s) with event.idm.read_only_udm.security_result.description UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped policy_name raw log field(s) with event.idm.read_only_udm.security_result.rule_name UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped event_category raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped details raw log field(s) with event.idm.read_only_udm.metadata.description UDM field.  
\- Renamed from target to event.idm.read_only_udm.target.  
\- Renamed from observer to event.idm.read_only_udm.observer.  
\- event.idm.read_only_udm.metadata.event_type: If event_category contains `LOGIN` and target_user is present, updated to USER_LOGIN.  
\- event.idm.read_only_udm.metadata.event_type: If event_action is `ACCESS`, updated to USER_RESOURCE_ACCESS.  
\- New grok patterns were introduced to parse two new Veritas NetBackup log formats.  
\- Additional grok logic was added to parse values from the details and summary fields.   
2024-01-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
