---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/informix-changelog/
title: Change log for INFORMIX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:31:43.770694+00:00
---

# Change log for INFORMIX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/informix-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for INFORMIX

Date | Changes  
---|---  
2026-07-28 |  Enhancement:  
\- Added support for `SYSLOG + CSV` format.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_timestamp` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `syslog_hostname` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `syslog_process` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `status_flag` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `remote_hostname` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `remote_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `service_name` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `database_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Added conditional logic to set `event.idm.read_only_udm.target.resource.resource_type` to `DATABASE` when `database_name` raw log field is present.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `session_status` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Added conditional logic to set `event.idm.read_only_udm.metadata.event_type` to `SYSTEM_AUDIT_LOG_UNCATEGORIZED` when `has_principal_user` is true, `NETWORK_CONNECTION` when both `has_target` and `has_principal` are true, `STATUS_UPDATE` when `has_principal` is true, or `GENERIC_EVENT` as fallback.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
