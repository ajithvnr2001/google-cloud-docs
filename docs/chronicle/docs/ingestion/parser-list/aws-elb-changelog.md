---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-elb-changelog/
title: Change log for AWS_ELB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:43.993139+00:00
---

# Change log for AWS_ELB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-elb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_ELB

Date | Changes  
---|---  
2026-01-23 |  Enhancement:  
\- Added a grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `bucket_owner_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `bucket` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `signature`, `auth_type`, `auth_header`, `turn_around_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `object_size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `target_ip`, `target_hostname`, `dst_ip`, `hostname`, and `bucket` are empty, updated to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `client_ip` is not empty, updated to `NETWORK_HTTP`.  
\- `event.idm.read_only_udm.metadata.event_type`: Otherwise, updated to `USER_RESOURCE_ACCESS`.   
2025-02-19 |  Enhancement:  
\- Added support for new format of syslog logs.  
\- Mapped `sec_status` to `security_result.action`.  
\- Mapped `grp_identifiers` to `principal.user.group_identifiers`.  
\- Mapped `http_version` to `network.application_protocol_version`.  
\- Mapped `useragent` to `network.http.user_agent`.  
\- Mapped `severity_level` to `security_result.severity`.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `port` to `principal.port`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `int_host` to `intermediary.hostname`.  
\- Mapped `int_port` to `intermediary.port`.  
\- Mapped `tid` to `additional.fields`.  
\- Added a Grok pattern to parse `sent_bytes`.   
2024-11-12 |  Enhancement:  
\- Added support to parse new format of syslog logs.   
2024-03-22 |  Enhancement:  
\- Added new Grok pattern to support new pattern of JSON logs.  
\- Added support for CEF pattern logs.  
\- Mapped `dst_ip` to `target.ip`.  
\- Mapped `dst_port` to `target.port`.  
\- Mapped `sip` to `principal.ip`.  
\- Mapped `request_processing_time`, `target_processing_time`, `siteid`, `fileId`, and `response_processing_time` to `security_result.detection.fields`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.  
\- Aligned mappings for `target.hostname` and `target.asset.hostname`.  
\- Mapped `cipher` to `network.tls.cipher`.  
\- Mapped `version` to `network.tls.version`.  
\- Mapped `Customer` to `principal.user.user_display_name`.   
2022-05-27 |  Enhancement - Modified the value stored in metadata.product_name to `AWS Elastic Load Balancer`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
