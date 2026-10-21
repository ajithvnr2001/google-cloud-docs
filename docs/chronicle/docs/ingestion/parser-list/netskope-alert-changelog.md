---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-changelog/
title: Change log for NETSKOPE_ALERT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:36:09.817777+00:00
---

# Change log for NETSKOPE_ALERT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETSKOPE_ALERT

Date | Changes  
---|---  
2024-08-14 |  Enhancement:  
\- Added support for new log format.   
2024-06-04 |  Enhancement:  
\- Mapped `matched_username` to `principal.user.email_addresses`.  
\- When `action` is `bypass` or `alert`, then mapped `action` to `security_result.action_details` and set `security_result.action` to `QUARANTINE`.  
\- When `alert_type` is `DLP`, then mapped `dlp_rule_severity` to `security_result.severity`.   
2024-02-19 |  Enhancement:  
\- Changed the mapping of `client_bytes` from `network.received_bytes` to `network.sent_bytes`.  
\- Changed the mapping of `server_bytes` from `network.sent_bytes` to `network.received_bytes`.   
2024-02-08 |  Enhancement:  
\- Mapped `useragent` and `user_agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.   
2023-11-10 |  Enhancement:  
\- Added Grok pattern, to check whether `srcip` is a valid IP pattern.  
\- Mapped `instance_id` to `principal.hostname`.  
\- Mapped `traffic_type` to `security_result.detection_fields`.  
\- Mapped `app_activity` to `additional.fields`.  
\- Mapped `count` to `additional.fields`.  
\- Mapped `site` to `additional.fields`.  
\- Mapped `device` to `principal.resource.resource_sub_type`.  
\- Mapped `type` to `security_result.detection_fields`.  
\- Changed the mapping of `hostname` using `replace` instead of `rename`.  
\- Changed `cci` mapping from `additional.fields` to `security_result.detection_fields`.  
\- Changed `ccl` mapping from `additional.fields` to `security_result.confidence_details`.  
\- Populated `security_result.confidence` according to the value in `ccl`.   
2023-07-14 |  Bug-Fix -  
\- Extracted value for `browser_session_id`,`app_session_id` using Grok pattern before mapping.  
\- Added condition check to validate email before mapping the field `to_user`.   
2023-07-06 |  Enhancement -  
\- Modified Grok pattern to identify whether `dsthost` is an IP address or not.  
If `dsthost` is an IP address, then mapped to `target.ip`, else mapped to `target.hostname`.   
2023-06-06 |  Enhancement -  
\- Mapped `domain` to `target.hostname`.  
\- Mapped `app_session_id` to `target.resource.attribute.labels`.  
\- Mapped `malware_severity` to `security_result.severity`.  
\- Mapped `malware_type` to `security_result.detection_fields`.  
\- Mapped `threat_match_field` to `security_result.detection_fields`.  
\- Mapped `ja3` to `network.tls.client.ja3`.  
\- Mapped `ja3s` to `network.tls.server.ja3s`.  
\- Mapped `cci`, `ccl` to `additional.fields`.  
\- Mapped `access_method` to `extensions.auth.auth_details`.  
\- Mapped `browser_version` to `network.http.parsed_user_agent.browser_version`.  
\- Mapped `dlp_profile` to `security_result.rule_type`.  
\- Mapped `dlp_rule` to `security_result.rule_name`.  
\- Mapped `netskope_pop` to `observer.hostname`.  
\- Mapped `page` to `network.http.referral_url`.  
\- Mapped `to_user` to `target.user.email_addresses`.  
\- Mapped `to_user_category` to `target.resource.attribute.labels`.   
2023-03-23 |  Enhancement -  
\- Mapped `security_result.alert_state` to `ALERTING` if `alert` is equal to `yes`.  
\- Mapped `security_result.alert_state` to `NOT_ALERTING` if `alert` is equal to `no`.  
\- Mapped `security_result.alert_state` to `UNSPECIFIED` if `alert` is null.   
2022-07-23 |  Enhancement:  
\- Removed unnecessary mapping for `metadata.description`.   
2022-07-01 |  Enhancement:  
\- The field `os` mapped to `principal.platform`.  
\- The field `dsthost` mapped to `target.ip` if `dsthost` is an IP, else mapped to `target.hostname`.  
\- The field `dstport` mapped to `target.port`.  
\- The field `srcport` mapped to `principal.port`.  
\- The field `user` mapped to `principal.user.email_addresses`, if `user` is a valid email address.  
\- The field `src_latitude` mapped to `principal.location.region_latitude`.  
\- The field `src_longitude` mapped to `principal.location.region_longitude`.  
\- The field `ip_protocol` mapped to `network.ip_protocol`.  
\- The field `client_bytes` mapped to `network.received_bytes`.  
\- The field `server_bytes` mapped to `network.sent_bytes`.  
\- The field `browser_session_id` mapped to `network.session_id`.  
\- The field `network_session_id` mapped to `network.session_id`.  
\- The field `appcategory` mapped to `security_result.category_details`.  
\- The field `publisher_cn` mapped to `additional.fields[n]`.  
\- The field `publisher_name` mapped to `additional.fields[n]`.  
\- The field `tunnel_id` mapped to `additional.fields[n]`.  
\- The field `tunnel_type` mapped to `additional.fields[n]`.  
\- Changed mapping for the field `shared_with` from `intermediary.user.email_addresses` to `network.email.to`.  
\- Changed mapping for the field `network.email.to` from `principal.user.email_addresses` to `network.email.from`.  
\- Added conditional checks for field `_severity`, `shared_with`, `from_user`, `protocol`.  
\- Modified `metadata.event_type` for the following cases:  
\- `GENERIC_EVENT` to `NETWORK_HTTP` where `principal.ip or principal.hostname` and `target.ip or target.hostname` are not null.  
\- `GENERIC_EVENT` to `STATUS_UPDATE` where `principal.ip or principal.hostname` is not null.  
\- `GENERIC_EVENT` to `USER_UNCATEGORIZED` where `principal.user.userid` is not null.   
2022-06-17 |  Bug-Fix:  
\- Added conditinal check for `md5` == `not available`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
