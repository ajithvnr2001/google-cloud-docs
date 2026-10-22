---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsa-changelog/
title: Change log for CISCO_WSA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:46.542554+00:00
---

# Change log for CISCO_WSA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsa-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_WSA

Date | Changes  
---|---  
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `information`, `appname`, `facility`, `logtime`, `policy` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `ser_url` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `ser_msg` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ser_data` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha_value` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- Added a grok pattern on `transaction_disposition` to extract `ser_msg`, `ser_data`, `ser_url`.  
\- Modified the grok patterns in order to parse the logs and following UDM fields are now being mapped correctly:  
-`event.idm.read_only_udm.metadata.event_timestamp.nanos`  
-`event.idm.read_only_udm.metadata.event_timestamp.seconds`  
-`event.idm.read_only_udm.metadata.event_type`  
-`event.idm.read_only_udm.metadata.log_type`  
-`event.idm.read_only_udm.metadata.product_event_type`  
-`event.idm.read_only_udm.metadata.product_name`  
-`event.idm.read_only_udm.metadata.vendor_name`  
-`event.idm.read_only_udm.network.application_protocol`  
-`event.idm.read_only_udm.network.http.method`  
-`event.idm.read_only_udm.network.http.response_code`  
-`event.idm.read_only_udm.network.http.user_agent`  
-`event.idm.read_only_udm.network.session_id`  
-`event.idm.read_only_udm.principal.asset.ip`  
-`event.idm.read_only_udm.principal.ip`  
-`event.idm.read_only_udm.principal.user.userid`  
-`event.idm.read_only_udm.security_result.severity`  
-`event.idm.read_only_udm.target.asset.ip`  
-`event.idm.read_only_udm.target.ip`  
-`event.idm.read_only_udm.target.port`  
-`event.idm.read_only_udm.target.url`  
2025-11-23 |  Enhancement:  
\- Added support for new log formats by expanding the grok patterns to parse additional variations of CISCO WSA logs.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `tar_region` raw log field to `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.state`: Newly mapped `tar_state` raw log field to `event.idm.read_only_udm.target.location.state` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Newly mapped `tar_city` raw log field to `event.idm.read_only_udm.target.location.city` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `interaction_mode`, `proxy_session_id` raw log fields to `event.idm.read_only_udm.additional.fields` as key-value pairs.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `server_cert_organization`, `target_kerberos_realm`, `kerberos_kvno`, `kerberos_keytab`, `kerberos_enctype` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` as key-value pairs.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `sec_summary` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- Refined the mapping logic for the `app_proto` field to `event.idm.read_only_udm.network.application_protocol` to only map valid ApplicationProtocol enum values.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` for logs having principal user data.   
2025-11-13 |  Enhancement:  
\- Modified the conditional logic within the scanning_verdict loop to also skip processing when the value is equal to `Unknown`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `auth_mechanism` raw log field to `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_id` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `server_response` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threat_confidence`, `threat_attempts`, `auth_protocol`, `auth_status`, `threat_category`, `threat_severity` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `latency`, `first_server_byte`, `first_client_byte`, `response_header`, `client_body`, `first_response_byte`, `auth_module`, `auth_status_code`, `auth_error_component`, `auth_error_module`, `auth_error_description`, `auth_error_details` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-12 |  Enhancement:  
\- Added gsub to replace `\\r\\n` and `\\n` with "" in message field.  
\- event.idm.read_only_udm.additional.fields:Removed mapping of `application` from `event.idm.read_only_udm.additional.fields` UDM field because the `mime_type` in raw logs was wrongly getting mapped to `event.idm.read_only_udm.additional.fields` UDM field with a key as `application`.  
\- Modified the existing grok pattern to correctly parse `mime_type` field for the raw logs by removing `application` field from the grok pattern.  
\- Modified grok patterns to parse `session_id` field from raw logs.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.   
2025-07-21 |  Enhancement:  
\- Modified a grok pattern to parse `mime_type` from raw logs.  
\- event.idm.read_only_udm.target.file.mime_type : Newly mapped `mime_type` field with `event.idm.read_only_udm.target.file.mime_type` UDM field.   
2025-07-08 |  Enhancement:  
\- Added GROK pattern to support new format of Syslog logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cmf`, `dcf`, `err`, `case_name`, `total_bytes`, `request_size`, `transaction_disposition` and `application` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_sent` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `response_size` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referer_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname, event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `wsa_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname`, `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.   
2024-08-13 |  Enhancement:  
\- Modified the Grok pattern to parse CSV data.   
2024-07-29 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
