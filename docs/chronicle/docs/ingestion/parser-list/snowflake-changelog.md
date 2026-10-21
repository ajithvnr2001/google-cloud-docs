---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snowflake-changelog/
title: Change log for SNOWFLAKE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:36:23.021884+00:00
---

# Change log for SNOWFLAKE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snowflake-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SNOWFLAKE

Date | Changes  
---|---  
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.session_id`: Removed mapping of `SESSION_ID` raw log field from `event.idm.read_only_udm.network.http.session_id` UDM field as it is not a valid UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SESSION_ID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `QUERY_PARAMETERIZED_HASH` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `QUERY_TEXT` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-24 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `PIPE_RECEIVED_TIME` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `PIPE_CATALOG_NAME` and `PIPE_SCHEMA_NAME` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `LAST_LOAD_TIME` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `FILE_NAME` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `PIPE_NAME` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ERROR_LIMIT`,`BYTES_BILLED` and `ERROR_COUNT` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ROW_COUNT` and `ROW_PARSED` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `FILE_SIZE` raw log field with `event.idm.read_only_udm.target.file.`size` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TABLE_CATALOG_NAME`, `TABLE_CATALOG_ID`, `TABLE_ID`, `TABLE_SCHEMA_ID`, `TABLE_SCHEMA_NAME` and `STAGE_LOCATION` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `TABLE_NAME` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-04-15 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `column4` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `column6` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `APPLICATION` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `OS` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `OS_VERSION` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `PYTHON_VERSION` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `PYTHON_RUNTIME` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `PYTHON_COMPILER` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `OCSP_MODE` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `TRACING` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `column10` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- Added a Grok Pattern to handle new csv pattern logs when both json and csv filters are failing.   
2025-04-09 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `column2` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `column7` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column10` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `column17` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `column9` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column71` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column3` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column4` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `column6` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `column11` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `column8` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2025-03-05 |  Enhancement:  
\- Changed mapping of `START_TIME` from `security_result.detection_fields` to `metadata.event_timestamp`.   
2025-01-16 |  Enhancement:  
\- Added support for parsing arrays of JSON.   
2025-01-08 |  Enhancement:  
\- Mapped `CLIENT_IP` to `principal.ip`.  
\- Mapped `EVENT_ID`, `EVENT_TYPE`, `FIRST_AUTHENTICATION_FACTOR`, `IS_SUCCESS`, `REPORTED_CLIENT_TYPE`, and `REPORTED_CLIENT_VERSION` to `security_result.detection_fields`.  
\- Added `CSV` filter to parse new format logs.   
2024-08-12 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
