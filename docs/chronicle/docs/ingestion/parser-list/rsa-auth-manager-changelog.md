---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-auth-manager-changelog/
title: Change log for RSA_AUTH_MANAGER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:18:54.830881+00:00
---

# Change log for RSA_AUTH_MANAGER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-auth-manager-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RSA_AUTH_MANAGER

Date | Changes  
---|---  
2026-06-17 |  Enhancement:  
\- Added a new grok pattern to parse the new `SYSLOG` and `SYSLOG+KV` format logs.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `PWD` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `USER` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `COMMAND` raw log field to `event.idm.read_only_udm.target.process.command_line`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column15` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Added support for the events `PROCESS_LAUNCH`, `USER_UNCATEGORIZED` and `NETWORK_CONNECTION` and relevant corresponding raw log fields.   
2026-05-21 |  \- event.idm.read_only_udm.security_result.description: Newly mapped `auth_module` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `auth_service` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `auth_action` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `uid` raw log field to `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `priority` and `program` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-29 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_log_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `principal_product_object_id` raw log field to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Conditionally mapped from the `custom_last_name` raw log field. If `custom_last_name` contains only `^[a-zA-Z]*$` and is not empty, it is mapped to `event.idm.read_only_udm.principal.user.user_display_name`. Otherwise, `custom_last_name` is not empty, its value is mapped to `event.idm.read_only_udm.additional.fields` under the key `custom_last_name`.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `Type` raw log field to `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `tar_product_object_id` raw log field to `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `path` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logger_class`, `event_code` and `application_session_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `correlation_id` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `principal_hostname` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `principal_security_domain_guid` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `username_1` raw log field to `event.idm.read_only_udm.target.user.attribute.labels` UDM field.   
2024-03-13 |  Enhancement:  
\- Modified the Grok pattern to parse the data in the header of the log.   
2022-08-09 |  Enhancement-Removed the dropped condition, handled and parsed the logs with appropriate GROK pattern.   
2022-06-13 |  Enhancement-Removed drop condition for logs with event_name = ACCESS_DIRECTORY.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
