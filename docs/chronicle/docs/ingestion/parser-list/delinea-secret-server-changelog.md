---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-secret-server-changelog/
title: Change log for DELINEA_SECRET_SERVER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:54:50.148027+00:00
---

# Change log for DELINEA_SECRET_SERVER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-secret-server-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DELINEA_SECRET_SERVER

Date | Changes  
---|---  
2025-12-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `suid`, `cs4Label`, `user_data` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EventClassId`, `item_Id`, `Details`, `Event`, `Action_data`, `item_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `num` from `event.idm.read_only_udm.metadata.product_log_id` UDM field since raw log `num` field represents logseverity value.  
\- `event.idm.read_only_udm.security_result.severity_details`: Mapped `num` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `num` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field based on the value in `num` raw log field.   
2025-11-11 |  Enhancement:  
\- Updated timestamp parsing to use the `EventDateTime` field when available, falling back to `rt`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `Level` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Service.Type` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ProcessedTime`, `Redelivered`, `RelayEvenIfExpired`, `_ucid`, `ForceCompress`, `Version`, `CorrelationId`, `Source.Host.Network.AddressType` and `TenantSecondaryId` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-04-23 |  Enhancement:  
\- Added a Grok pattern to support new format of syslog logs.   
2025-02-25 |  Enhancement:  
\- Mapped `source_host_network_ipaddress` to `principal.ip`.  
\- Mapped `target_host_name` to `target_host_name`.  
\- Mapped `machineTimeZone` to `additional.fields`.  
\- Mapped `machineName` to `additional.fields`.  
\- Mapped `product` to `additional.fields`.  
\- Mapped `schemaVersion` to `additional.fields`.  
\- Mapped `byUserEmailAddress` to `principal.user.email_addresses`.  
\- Mapped `byUserDisplayName` to `principal.user.email_addresses` if `byUserEmailAddress` is not equal to null else `byUserDisplayName` to `additional.fields`.   
2025-01-29 |  Enhancement:  
\- Added support for a new JSON log format.   
2024-09-05 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
