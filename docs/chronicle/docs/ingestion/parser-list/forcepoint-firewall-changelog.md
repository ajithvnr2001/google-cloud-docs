---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-firewall-changelog/
title: Change log for FORCEPOINT_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:45.882399+00:00
---

# Change log for FORCEPOINT_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORCEPOINT_FIREWALL

Date | Changes  
---|---  
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `NodeId` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field when `Facility` is `Management`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `CompId` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2026-02-03 |  Enhancement:  
\- The logic for populating event.idm.read_only_udm.intermediary.ip was updated. The raw field `NodeId` will now be mapped to `event.idm.read_only_udm.intermediary.ip` instead of `principal.ip` when the raw field `Facility` is Anti-Malware.  
\- event.idm.read_only_udm.principal.ip: Modified the mapping logic for the `NodeId` raw log field. When the `Facility` raw log field is `Anti-Malware`, `NodeId` is now exclusively mapped to `event.idm.read_only_udm.intermediary.ip`. This removes the previous conditional mapping of `NodeId` to `event.idm.read_only_udm.principal.ip` which occurred for `Anti-Malware` logs only when `Src` and `Dst` raw fields were empty. This change was made to more accurately reflect the role of the device identified by `NodeId` as an intermediary when the facility is `Anti-Malware`, in order to introduce a more accurate mapping for the raw log field.  
\- The condition for setting event.idm.read_only_udm.metadata.event_type to STATUS_UPDATE was updated to also check that principal_values is not empty.   
2025-11-12 |  Enhancement:  
\- event.idm.read_only_udm.security_result.rule_id: Removed mapping of `EventId` from `event.idm.read_only_udm.security_result.rule_id` as `RuleId` is more suitable for this field.  
\- event.idm.read_only_udm.security_result.rule_id: Mapped `RuleId` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- event.idm.read_only_udm.security_result.rule_name: Mapped `EventId` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- event.idm.read_only_udm.security_result.rule_labels: Removed mapping of `RuleId` from `event.idm.read_only_udm.security_result.rule_labels` to eliminate redundant mapping.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `IcmpId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-06 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname: Removed mapping of `CompId` from `event.idm.read_only_udm.target.hostname` because it was more suitable as an `intermediary` field.  
\- event.idm.read_only_udm.intermediary.hostname: Mapped `CompId` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `SrcVlan`, `Srcif`, `Rtt`, `NatRuleId`, `ReceptionTime`, `SenderType` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.rule_labels: Newly mapped `RuleId` raw log field to `event.idm.read_only_udm.security_result.rule_labels`.   
2025-02-11 |  Enhancement:  
\- Changed `inter_hostname` mapping from `principal.hostname` and `principal.asset.hostname` to `intermediary.hostname` and `intermediary.asset.hostname`.  
\- Modified the Grok pattern to parse IP address to `intermediary.ip`.   
2025-01-23 |  Enhancement:  
\- Modified the Grok pattern to parse the unparsed logs.   
2024-12-04 |  Enhancement:  
\- Modified `eventid` mapping from `metadata.product_log_id` to `security_result.rule_id`.  
\- Modified `log_id` mapping from `additional_fields` to `metadata.product_log_id`.   
2024-11-13 |  Enhancement:  
\- Mapped `eventid` to `metadata.product_log_id`.  
\- Moved `log_id` mapping from `metadata.product_log_id` to `additional_fields`.   
2023-02-16 |  Bug Fix  
\- Fixed the error when the target field is not set while generating event type `NETWORK_CONNECTION`.  
\- Modified the code to handle addition errors found in testing.   
2022-10-06 |  Enhancement - Added condition to Map `NodeId` to `principal.ip` when `Src` and `Dst` is empty.   
2022-06-27 |  Enhancement - Following fields were added  
Mapped `Action` to `security_result.action_details`.  
Mapped `AccElapsed` to `network.session_duration.seconds`.  
Mapped `Type` to `security_result.severity_details`.  
Mapped security_result.severity as `LOW` for `Type` having value `Notification`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
