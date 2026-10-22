---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tripwire-fim-changelog/
title: Change log for TRIPWIRE_FIM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:30.262281+00:00
---

# Change log for TRIPWIRE_FIM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tripwire-fim-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRIPWIRE_FIM

Date | Changes  
---|---  
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ElementId`, `NodeId`, `AssociatedObjects`, `VerId`, `query` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `asm_log_element` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `actionDetail` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- Added missing `on_error` label in the existing grok patterns to prevent errors.  
\- Added a `target_mid_present` flag wherever `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.hostname` is being mapped.  
\- Added `is_network_connection` flag when `category` in `System`, `Element Check` and event_type is `NETWORK_CONNECTION` to prevent log from failing when mandatory parameters are missing for `NETWORK_CONNECTION` event_type.  
\- `event.idm.read_only_udm.metadata.event_type`: If `is_network_connection` flag is `true`, `msg` does not match `shut down`, `principal_mid_present` flag is `true`, and `target_mid_present` flag is `true`, updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `is_network_connection` flag is `true`, `msg` does not match `shut down`, and either `principal_mid_present` flag is not `true` or `target_mid_present` flag is not `true`, updated to ``.  
\- Added new grok patterns to extract `actionDetail`, `asm_log_element`, and `query` from `desc` field.  
\- Added validation for `target_ip` to ensure it's a valid IP address before merging into `event.idm.read_only_udm.target.ip`.  
\- Added gsub to remove `'` from `rules` and `actionDetail` fields.  
\- Fields getting populated because of above mentioned changes are :  
\- event.idm.read_only_udm.additional.fields  
\- event.idm.read_only_udm.metadata.event_type  
\- event.idm.read_only_udm.metadata.event_timestamp.seconds  
\- event.idm.read_only_udm.metadata.log_type  
\- event.idm.read_only_udm.metadata.product_event_type  
\- event.idm.read_only_udm.metadata.product_log_id  
\- event.idm.read_only_udm.metadata.product_name  
\- event.idm.read_only_udm.metadata.vendor_name  
\- event.idm.read_only_udm.principal.asset.hostname  
\- event.idm.read_only_udm.principal.asset.ip  
\- event.idm.read_only_udm.principal.hostname  
\- event.idm.read_only_udm.principal.ip  
\- event.idm.read_only_udm.principal.user.userid  
\- event.idm.read_only_udm.security_result.action  
\- event.idm.read_only_udm.security_result.action_details  
\- event.idm.read_only_udm.security_result.description  
\- event.idm.read_only_udm.security_result.rule_name  
\- event.idm.read_only_udm.security_result.severity  
\- event.idm.read_only_udm.target.application  
\- event.idm.read_only_udm.target.asset.hostname  
\- event.idm.read_only_udm.target.asset.ip  
\- event.idm.read_only_udm.target.hostname  
\- event.idm.read_only_udm.target.ip  
\- event.idm.read_only_udm.security_result.detection_fields   
2026-02-06 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of TripwireEnterpriseElementId from event.idm.read_only_udm.target.resource.attribute.labels UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Mapped TripwireEnterpriseElementId raw log field to event.idm.read_only_udm.target.resource.product_object_id UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of TripwireEnterpriseElementName from event.idm.read_only_udm.target.resource.attribute.labels UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.file.names: Mapped TripwireEnterpriseElementName raw log field to event.idm.read_only_udm.target.file.names UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of TripwireEnterpriseNodeType from event.idm.read_only_udm.target.resource.attribute.labels UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.platform: Mapped TripwireEnterpriseNodeType raw log field to event.idm.read_only_udm.target.platform UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of TripwireEnterpriseRule from event.idm.read_only_udm.target.resource.attribute.labels UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.rule_name: Mapped TripwireEnterpriseRule raw log field to event.idm.read_only_udm.security_result.rule_name UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of TripwireEnterpriseRuleId from event.idm.read_only_udm.target.resource.attribute.labels UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.rule_id: Mapped TripwireEnterpriseRuleId raw log field to event.idm.read_only_udm.security_result.rule_id UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of TripwireEnterpriseRuleType from event.idm.read_only_udm.security_result.detection_fields UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.rule_type: Mapped TripwireEnterpriseRuleType raw log field to event.idm.read_only_udm.security_result.rule_type UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped TripwireEnterpriseVersionSha512 raw log field to event.idm.read_only_udm.target.file.sha256 UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped dtz raw log field to event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- Newly added support for the `TIMESTAMP_ISO8601` format logs and parsed the timestamp `TIMESTAMP_ISO8601` format of logs correctly to its respective UDM fields.  
\- Added on_error for the `start` and `datetime` timestamp raw log fields. This fixed parsing issues for logs with TIMESTAMP_ISO8601 timestamp, allowing the following UDM fields to be mapped correctly:  
\- event.idm.read_only_udm.metadata.product_log_id  
\- event.idm.read_only_udm.metadata.product_name  
\- event.idm.read_only_udm.metadata.product_version  
\- event.idm.read_only_udm.metadata.url_back_to_product  
\- event.idm.read_only_udm.metadata.vendor_name  
\- event.idm.read_only_udm.observer.asset.hostname  
\- event.idm.read_only_udm.observer.hostname  
\- event.idm.read_only_udm.observer.resource.attribute.labels  
\- event.idm.read_only_udm.principal.asset.hostname  
\- event.idm.read_only_udm.principal.asset.ip  
\- event.idm.read_only_udm.principal.hostname  
\- event.idm.read_only_udm.principal.ip  
\- event.idm.read_only_udm.principal.process.file.full_path  
\- event.idm.read_only_udm.principal.resource.attribute.labels  
\- event.idm.read_only_udm.principal.resource.product_object_id  
\- event.idm.read_only_udm.principal.user.userid  
\- event.idm.read_only_udm.security_result.action  
\- event.idm.read_only_udm.security_result.category_details  
\- event.idm.read_only_udm.security_result.description  
\- event.idm.read_only_udm.security_result.detection_fields  
\- event.idm.read_only_udm.security_result.rule_id  
\- event.idm.read_only_udm.security_result.rule_name  
\- event.idm.read_only_udm.security_result.rule_type  
\- event.idm.read_only_udm.security_result.severity  
\- event.idm.read_only_udm.security_result.summary  
\- event.idm.read_only_udm.target.application  
\- event.idm.read_only_udm.target.asset.hostname  
\- event.idm.read_only_udm.target.asset.ip  
\- event.idm.read_only_udm.target.file.full_path  
\- event.idm.read_only_udm.target.file.names  
\- event.idm.read_only_udm.target.file.sha1  
\- event.idm.read_only_udm.target.file.size  
\- event.idm.read_only_udm.target.hostname  
\- event.idm.read_only_udm.target.ip  
\- event.idm.read_only_udm.target.labels  
\- event.idm.read_only_udm.target.platform  
\- event.idm.read_only_udm.target.registry.registry_key  
\- event.idm.read_only_udm.target.registry.registry_value_data  
\- event.idm.read_only_udm.target.resource.attribute.labels  
\- event.idm.read_only_udm.target.resource.name  
\- event.idm.read_only_udm.target.resource.product_object_id  
\- event.idm.read_only_udm.target.user.userid   
2025-06-30 |  Enhancement:  
\- Added Grok patterns to parse the `msg` field from the raw logs.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseChangeType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseElementId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseElementName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseNodeType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseRule` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseRuleId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `TripwireEnterpriseRuleType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `TripwireEnterpriseSeverity` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `TripwireEnterpriseSeverityRange` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `TripwireEnterpriseUrl` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.target.file.sha1: Newly mapped `TripwireEnterpriseVersionSha1` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `deviceExternalId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `fsize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.   
2025-06-02 |  Enhancement:  
\- Modified the grok patterns in order to extract hostname.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `hstname` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field  
\- event.idm.read_only_udm.observer.asset.hostname: Newly mapped `hstname` raw log field with `event.idm.read_only_udm.observer.asset.hostname` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseIds` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseLogLevel` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `TripwireEnterpriseNodeId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.target.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.target.ip` UDM field  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.observer.resource.attribute.labels: Newly mapped `deviceFacility` raw log field with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `externalId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `shost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `shost` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field  
\- event.idm.read_only_udm.target.application: Newly mapped `application` raw log field with `event.idm.read_only_udm.target.application` UDM field  
\- event.idm.read_only_udm.target.labels: Newly mapped `processes` raw log field with `event.idm.read_only_udm.target.labels` UDM field   
2024-11-07 |  Bug-Fix:  
\- Initialized `cs4Label` to null.  
\- Set `additional_cs4.key` to `cs4` if `cs4Label` is null.  
\- Set `additional_cs4.value` to `cs4Label` if `cs4Label` is not null.   
2023-06-21 |  Enhancement:  
\- Added gsub to handle CEF format logs.   
2023-06-07 |  Enhancement:  
\- Added a Grok pattern to handle CEF formatted logs.   
2022-06-14 |  Bug-Fix: - Added a new grok to parse `HKEY_` type logs without space between regestry_key and value.  
\- Added validation check for target_hostname or target_ip prior to mapping of event_type to NETWORK_CONNECTION.  
\- Added null check for username prior to mapping to udm.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
