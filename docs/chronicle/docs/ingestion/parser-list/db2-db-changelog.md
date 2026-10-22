---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/db2-db-changelog/
title: Change log for DB2_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:47.755400+00:00
---

# Change log for DB2_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/db2-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DB2_DB

Date | Changes  
---|---  
2026-07-29 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `poe` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: Newly mapped `usrPriv` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `intent` , `length`, and `CorrelationNumber` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `Object_Class_Code` from `event.idm.read_only_udm.target.resource.type` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.ancestors.name`: Newly mapped `Object_Class_Code` raw log field with `event.idm.read_only_udm.target.resource.ancestors.name` UDM field.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `SQL` to extract `resource_name`.   
2025-12-04 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `audit event` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event correlator` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `instance name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `archive path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `execution id`, `application id`, `authid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `event status`, `access attempted`, `access_approval_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `timestamp_1`, `process`, `object type`, `plugin name`, `auth type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added null conditional check for `usrName` field.   
2024-09-25 |  Enhancement:  
\- Mapped `System` and `Subsystem` to `additional.fields`.   
2024-09-19 |  Enhancement:  
\- Modified date block to parse timestamp correctly.   
2024-06-27 |  Enhancement:  
\- Modified date block to handle new pattern of timestamps.  
\- Added support for new pattern of timestamp.   
2024-06-04 |  Enhancement:  
\- Added a Grok pattern to extract resource_name from the `SQL` field and mapped it to `target.resource.name`.   
2024-02-26 |  Enhancement:  
\- Added support for new date formats.  
\- Aligned `principal.ip` and `principal.asset.ip` mapping.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mapping.  
\- Aligned `target.hostname` and `target.asset.hostname` mapping.   
2023-12-16 |  Enhancement  
\- Mapped `ConnectionType` to `principal.process.pid`.  
\- Mapped `plan` to `principal.resource.name`.  
\- Mapped `SSID` to `network.session_id`.  
\- Mapped `CorrelationUser` to `intermediary.user.userid`.  
\- Mapped `SQL` to `principal.process.command_line`.   
2023-10-30 |  Enhancement  
\- Parsed new format of JSON logs.  
\- Mapped the following additional fields:  
\- Mapped `AuthenticatedUser` to `principal.user.userid`.  
\- Mapped `SQL` to `target.resource.attribute.labels`.  
\- Parsed `date` and `time` field.   
2022-05-04 |  Bug-fix  
\- Added condition check for the presence of fields `objtyp` and `obj` before they get mapped.  
\- Parsed the logs failing during Validation API testing.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
