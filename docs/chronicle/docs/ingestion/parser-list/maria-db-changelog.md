---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/maria-db-changelog/
title: Change log for MARIA_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:58:41.512795+00:00
---

# Change log for MARIA_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/maria-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MARIA_DB

Date | Changes  
---|---  
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `column2` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, mapped to more appropriate field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `column2` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields. Added a conditional check to map `column4` to `event.idm.read_only_udm.principal.hostname` if it is not an IP address.   
2026-02-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `type_val`, `name_val`, `command_val`, `database`, `connection_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `status_message` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_year`, `time_val` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `program` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `server_uid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `user_auth_status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `db_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `db_version` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `managed_by` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Set the value of `event.idm.read_only_udm.security_result.severity` UDM field to `MEDIUM` when `log_level` is `warning` and to `INFORMATIONAL` when `log_level` is `note`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Added new date formats to support for the `event.idm.read_only_udm.metadata.event_timestamp`.  
\- Added the grok patterns to ensure inappropriate values are no longer being mapped to `event.idm.read_only_udm.metadata.product_event_type`, `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`, `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.metadata.event_timestamp.nanos` UDM fields. Additionally, this is allowing the `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields to be mapped correctly.   
2024-12-03 |  \- Added `gsub` to remove special characters from the CSV format logs.   
2024-11-08 |  \- Added support for the CSV format logs.   
2024-07-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
