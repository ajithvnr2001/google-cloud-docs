---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vormetric-changelog/
title: Change log for VORMETRIC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:22.352940+00:00
---

# Change log for VORMETRIC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vormetric-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VORMETRIC

Date | Changes  
---|---  
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `DIRECTORY`, `FILE` from `event.idm.read_only_udm.target.resource.type` UDM field as the UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Mapped `DIRECTORY`, `FILE` values with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- Updated grok patterns to add support for new format of `SYSLOG+JSON` logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `message` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `details.client_name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `account` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `service` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `requestId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `principal.iss` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain_id` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `details.grant_type`, `principal.acc`, `details.connection`, `details.client_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: When `success` field is true, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW and when `success` field is false, updated the value of `event.idm.read_only_udm.security_result.action` to BLOCK.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Mapped `Vormetric, Inc.` value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `Vormetric` value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When `event_type` is GENERIC_EVENT and principal machine data is present and principal or target user details are present and `details_grant_type` is client_credential, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGIN.   
2024-08-05 |  Enhancement:  
\- Modified the Grok pattern to parse the unparsed logs.  
\- Fixed the mapping of `event_type` to map to `USER_LOGIN` instead of `NETWORK_CONNECTION` when `desc` is in `admin` or `login` or `user`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
