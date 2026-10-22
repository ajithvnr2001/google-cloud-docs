---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sam-changelog/
title: Change log for IBM_SAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:02.026632+00:00
---

# Change log for IBM_SAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_SAM

Date | Changes  
---|---  
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `GS_CREATE_HOLD_ZPLANT` and `syslog_version` raw log field with `event.idm.read_only_udm.additional.fields` UDM fields.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `authntype` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `component` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `rev` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `location` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `user_location` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `name_in_rgy` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action`, `auth`, `outcome`, `status`, `user_location_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `blade` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `component_rev`, `resource` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `instance` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-04-02 |  Enhancement:  
\- Added a new Grok pattern to parse a new syslog format.  
\- Added an `ip` null check before mapping it to `intermediary.ip`.  
\- Modified the null check condition for `src_ip` , `dst_ip` and `rcv_bytes`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol_value` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field if `ip_protocol_value` has value in `TCP` , `UDP` , `ICMP`.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method_value` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sha256_value` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Moved `description` from line `323` to `122` as many field mapping are done before description and hence few fields are not getting mapped so moved it to line `122` to parse all the grok fields.  
\- Added a `has_target` check before mapping `event_type` to `NETWORK_HTTP`.   
2024-11-19 |  Enhancement:  
\- Added a new Grok pattern to parse new format of syslog logs.   
2024-03-08 |  Enhancement:  
\- Added support for new pattern of syslog logs.  
\- Mapped `src_host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `user_name` to `principal.user.userid`.  
\- Mapped `src_application` to `principal.application`.  
\- Mapped `product_event_type` to `metadata.product_event_type`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `target_hostname` to `target.hostname`.  
\- Mapped `src_resource` to `principal.resource.name`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `file_name` to `principal.file.full_path`.  
\- Mapped `connection_type` to `additional.fields`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.   
2023-09-12 |  Enhancement:  
\- Added a Grok pattern to support new log format.   
2023-05-21 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
