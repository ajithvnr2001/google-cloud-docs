---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appian-cloud-changelog/
title: Change log for APPIAN_CLOUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:41.912049+00:00
---

# Change log for APPIAN_CLOUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appian-cloud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for APPIAN_CLOUD

Date | Changes  
---|---  
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_severity` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `email` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if it is not an email address, else map to `event.idm.read_only_udm.principal.user.email_addresses`.   
2025-05-06 |  \- event.idm.read_only_udm.target.resource.product_object_id: Newly Mapped `sessionID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` when the `application` is `Web API` to UDM field.   
2025-04-04 |  \- event.idm.read_only_udm.metadata.log_type: Newly Mapped `APPIAN_CLOUD` value with `event.idm.read_only_udm.metadata.log_type` UDM field .  
\- event.idm.read_only_udm.network.session_id: Newly Mapped `sessionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly Mapped `transactionId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.about.platform_version :Newly Mapped `versionDetails` raw log field with `event.idm.read_only_udm.security_result.about.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.application :Newly Mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.ip :Newly Mapped `IpAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.assest.ip :Newly Mapped `IpAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid :Newly Mapped `userId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields :Newly Mapped `rolesAllow` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields :Newly Mapped `userRole` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details :Newly Mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.resource.name :Newly Mapped `resourcename` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.process.command_line :Newly Mapped `commandline` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.additional.fields :Newly Mapped `devicetimestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses :Newly Mapped `email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.   
2025-02-12 |  \- Changed `metadata.vendor_name` mapping from `APPIAN_CLOUD` to `Appian`.  
\- Changed `metadata.product_name` mapping from `APPIAN_CLOUD` to `Cloud Platform`.   
2025-01-24 |  \- Added Grok patterns to parse the logs.  
\- Mapped `src_host` to `intermediary.hostname`.  
\- Mapped `sqlcmd` to `security_result.detection_fields`.  
\- Mapped `oid` to `target.resource.product_object_id`.  
\- Mapped `detail` to `security_result.severity_details`.  
\- Mapped `thread` to `additional.fields`.  
\- Mapped `document_name` to `target.files.names`.  
\- Mapped `hash` to `target.file.md5`.  
\- Mapped `src_ip1` to `target.ip` and `target.asset.ip`.  
\- Mapped `name` to `target.resource.resource_subtype`.  
\- Mapped `msg` and `reason` to `security_result.summary`.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `details` to `security_result.description` and `security_result.detection_fields`.  
\- Mapped `user` to `principal.user.product_object_id`.  
\- Mapped `action` to `target.resource.resource_subtype` and `target.resource.attribute.labels`.  
\- Mapped `original_value`, `setting_new_value`, `setting_old_value`, and `new_value` to `target.resource.attribute.labels`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `property` to `target.resource.name`.  
\- Mapped `modified_by_uuid` to `principal.user.product_object_id`.  
\- Mapped `modified_by_username` to `principal.user.userid`.  
\- Mapped `page_involved`, `site_involved`, and `page_group_involved` to `target.resource.attribute.labels`.  
\- Mapped `total_thread_count`, `daemon_thread_count`, used_heap_space`, `available_heap_space`, `tenured_generation_usage_after_collection`, `tenured_generation_used`, `tenured_generation_available`, `permanent_generation_used`, and `permanent_generation_available` to `additional.fields".  
\- Mapped `young_collection_count`, `young_cllection_time`, `tenured_collection_count`, `tenured_collection_time`, `cpu_core_count`, `total_system_memory`, `used_system_memory`, `total_swap_space`, `used_swap_space`, `load_average`, and `session_count` to `additional.fields`.  
\- Mapped `record_type_name` to `target.resource.name`.  
\- Mapped `record_identifier`, `record_type_url_stub`, `view`, `filters`, `environment`, and `site_url_stub` to `target.resource.attribute.labels`.  
\- Mapped `data_store`, `entity`, and `operation_type` to `additional.fields`.  
\- Mapped `action1` to `security_result.summary`.  
\- Mapped `user_uuid` to `target.user.product_object_id`.  
\- Mapped `operation_name`, `prepare_time`, `transform_time`, and `execute_time` to `additional.fields`.  
\- Mapped `operation_detail` to `security_result.summary`.  
\- Mapped `object` to `security_result.summary`.  
\- Mapped `host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `database` to `target.resource.name`.  
\- Mapped `retcode` to `additional.fields`.  
\- Mapped `connectionid` to `network.session.id`.  
\- Mapped `queryid` to `target.resource.product_object_id`.  
\- When `userid` is emailaddress, mapped these fields to `principal.user.userid`, and `principal.user.email_address`.  
\- Mapped `server_host` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `minimum_execution_time`, `execution_count`, `status_code_1xx_count`, `status_code_2xx_count`, `status_code_3xx_count`, `status_code_4xx_count`, `status_code_5xx_count`, `minimum_response_size`, `maximum_response_time`, `maximum_response_size`, `mean_execution_time`, and `maximum_response_size` to `security_result.detection_fields`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `act` to `security_result.action`.  
\- When `message` is `record-usage` or `sites-usage`, then `metadata.event_type` is `USER_RESOURCE_ACCESS`.  
\- When message is `admin-console-audit`, then `metadata.event_type` is `USER_RESOURCE_UPDATE_CONTENT`.  
\- When message is `delete`, then `metadata.event_type` is `USER_RESOURCE_DELETION`.   
2024-11-14 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
