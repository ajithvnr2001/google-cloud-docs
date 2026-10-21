---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-support-portal-changelog/
title: Change log for BROADCOM_SUPPORT_PORTAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:04:34.822478+00:00
---

# Change log for BROADCOM_SUPPORT_PORTAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-support-portal-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BROADCOM_SUPPORT_PORTAL

Date | Changes  
---|---  
2025-03-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `module`, `socket_details`, `fd`, `family`, `type`, `level`, `log_data`, `timestamp_details`, `session_duration`, `correlationId`, `className` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `request_url_details` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_userId_details` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `target_url_details`, `url_details` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `principal_application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method_details` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `application_protocol_details` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `application_protocol_data` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response_code_details` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `received_bytes_details` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sent_byte_details` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent_details` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `user_agent_details` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `principal_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_log_id_details` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application_details` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal machine data fields are present and target machine data fields are present then event_type is updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `principal user details are present then event_type is updated to `USER_UNCATEGORIZED`.  
\- Added a gsub to remove `\r\n`, `\n`, and `\\u001b` from `message`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Updated mapping for `event.idm.read_only_udm.principal.resource.attribute.labels` from `event1.idm.read_only_udm.principal.resource.attribute.labels` to `principal.resource.attribute.labels` UDM field.  
\- Added grok patterns to parse the log data.   
2025-01-29 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
