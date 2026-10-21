---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vsphere-changelog/
title: Change log for VMWARE_VSPHERE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:39:11.003294+00:00
---

# Change log for VMWARE_VSPHERE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vsphere-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_VSPHERE

Date | Changes  
---|---  
2026-06-03 |  \- Fixed a typo in the mapping value, changing `NETWOK_CONNECTION` to the correct spelling `NETWORK_CONNECTION`.   
2026-05-13 |  \- Added a grok pattern on `message` data field to parse raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `api_invocations` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column2`, `login time`, `syslog_priority`, `user_level` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-15 |  \- Added support for new format of SYSLOG + CSV logs.  
\- event.idm.read_only_udm.network.session_id : Newly Mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id ` UDM Field.  
\- event.idm.read_only_udm.metadata.product_log_id : Newly Mapped `uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.principal.hostname : Newly Mapped `Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM Field.  
\- event.idm.read_only_udm.principal.asset.hostname : Newly Mapped `Hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM Field.  
\- event.idm.read_only_udm.metadata.description : Newly Mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mappeed `activityType` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Originator` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `sub` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `opID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `progress` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `cls_simple_activity` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `certVerificationStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `itemType` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `vpxd` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `securityCompliance` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `logtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly Mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM Field.  
\- event.idm.read_only_udm.metadata.description: Newly Mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM Field.   
2024-10-29 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
