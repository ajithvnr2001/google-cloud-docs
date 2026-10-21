---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin-sso-changelog/
title: Change log for ONELOGIN_SSO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:05:49.041365+00:00
---

# Change log for ONELOGIN_SSO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin-sso-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONELOGIN_SSO

Date | Changes  
---|---  
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `user_attributes.username`, `adc_id`, `adc_name`, `user_attributes.openid_name`, `user_attributes.samaccountname`, `user_attributes.member_of` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.group.product_object_id: Newly mapped `user_attributes.group_id` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- Applied gsub transformation to replace \\\" with ' in the message field.   
2024-05-27 |  Enhancement:  
\- Added `gsub` to parse dropped logs.  
\- Mapped `user_attributes.lastname` to `principal.user.last_name`.  
\- Mapped `user_attributes.firstname` to `principal.user.first_name`.  
\- Mapped `user_attributes.department` to `principal.user.department`.  
\- Mapped `user_attributes.title` to `principal.user.title`.  
\- Mapped `user_attributes.email` to `principal.user.email_addresses`.   
2024-05-21 |  Enhancement:  
\- Mapped `created_at` to `metadata.event_timestamp`.  
\- When `principal.user.userid` is not present for event 334, then mapped `metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2023-04-28 |  Enhancement - mapped the following raw logs elements to UDM elements:  
\- Removed characters from log if it contains "`\`, `\\n` or `\\` to correct the JSON log.  
\- Supported different format for datetime match.  
\- Mapped `id` to `metadata.product_object_id`.  
\- Mapped `account_id` to `additional.fields`.  
\- Mapped `assuming_acting_user_id` to `additional.fields`.  
\- Mapped `otp_device_id` to `additional.fields`.  
\- Mapped `directory_sync_run_id` to `additional.fields`.  
\- Mapped `resource_type_id` to `additional.fields`.  
\- Mapped `user_agent` to `network.http.parsed_user_agent`.  
\- Mapped `otp_device_id` to `principal.asset_id`.  
\- Mapped `actor_system` to `additional.fields`.  
\- Mapped `operation_name` to `additional.fields`.  
\- Mapped `resolution` to `additional.fields`.  
\- Mapped `client_id` to `additional.fields`.  
\- Mapped `risk_cookie_id` to `additional.fields`.  
\- Mapped `browser_fingerprint` to `additional.fields`.  
\- Mapped `event_type_ids` to `additional.fields`.  
\- Mapped `since` to `additional.fields`.  
\- Mapped `until` to `additional.fields`.  
\- Mapped `proxy_ip` to `intermediary.ip`.  
\- Mapped `error_description` to `additional.fields`.   
2022-05-18 |  Enhancement - map following raw logs elements to UDM elements:  
\- actor_user_id to event.idm.read_only_udm.principal.user.product_object_id  
\- user_id to event.idm.read_only_udm.target.user.product_object_id   
2022-03-23 |  Enhancement-map following raw logs elements to UDM elements  
\- user_agent to event.idm.read_only_udm.network.http.user_agent.  
\- uuid to event.idm.read_only_udm.metadata.product_log_id.  
\- group_id to event.idm.read_only_udm.target.group.product_object_id.  
\- group_name to event.idm.read_only_udm.target.group.group_display_name.  
\- policy_type to security_result.rule_type.  
\- policy_id to security_result.rule_id.  
\- policy_name to security_result.rule_name.  
\- authentication_factor_type to event.idm.read_only_udm.extensions.auth.auth_details.  
\- risk_reasons to security_result.description.  
\- risk_score to security_result.severity_details.  
Logic enhancements for the following app_id, app_name, directory_id, directory_name, privilege_id, privilege_name, role_name, role_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
