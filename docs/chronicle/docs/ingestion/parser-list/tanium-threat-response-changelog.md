---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-threat-response-changelog/
title: Change log for TANIUM_THREAT_RESPONSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:38:11.198993+00:00
---

# Change log for TANIUM_THREAT_RESPONSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-threat-response-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_THREAT_RESPONSE

Date | Changes  
---|---  
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `IntelName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.   
2026-04-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.parent_process.parent_process.parent_process.parent_process.parent_process.parent_process.file.md5`: Used correct variable name to map `match_parent_parent_parent_parent_parent_parent_parent_file_md5` with `event.idm.read_only_udm.target.process.parent_process.parent_process.parent_process.parent_process.parent_process.parent_process.file.md5` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Used correct label name to map `state.enabled` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `security_event_timestamp`, `security_event_type_identifier`, `relevant_actions_timestamp`, `MatchDetails.finding.type_id`, `MatchDetails.finding.artifact.artifact_hash`, `MatchDetails.finding.artifact.instance_hash`, `MatchDetails.finding.artifact.windows_defender_event.event.exploit_guard_blocked.id`, `MatchDetails.finding.artifact.windows_defender_event.timestamp_ms`, `EID` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `additional_fields_id`, `additional_fields_detection_time`, `impactScore`, `MatchDetails.finding.artifact.windows_defender_event.event.exploit_guard_blocked.detection_time`, `Intel_Source` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `relevant_actions_target_file_path` raw log field with event.idm.read_only_udm.target.file.full_path UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `MatchDetails_finding_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `Link` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `MatchDetails.finding.artifact.windows_defender_event.event.exploit_guard_blocked.process_name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `MatchDetails.finding.artifact.windows_defender_event.event.exploit_guard_blocked.user` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `MatchDetails.finding.artifact.windows_defender_event.event.exploit_guard_blocked.path` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-10-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application_name` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `application_vendor` raw log field(s) with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `application_version`, `count` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Changed mapping for `event.idm.read_only_udm.target.process.pid` from `MatchDetails.match.properties.pid` to `MatchDetails_pid` since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Changed mapping for `event.idm.read_only_udm.target.process.file.full_path` from `MatchDetails.match.properties.file.fullpath`, `MatchDetails.match.properties.fullpath` to `MatchDetails_file_fullpath`, `MatchDetails_fullpath` since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.file.md5`: Changed mapping for `event.idm.read_only_udm.target.process.file.md5` from `MatchDetails.match.properties.file.md5`, `MatchDetails.match.properties.md5` to `MatchDetails_file_md5`, `MatchDetails_md5` since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.file.sha1`: Changed mapping for `event.idm.read_only_udm.target.process.file.sha1` from `MatchDetails.match.properties.file.sha1`, `MatchDetails.match.properties.sha1` to `MatchDetails_file_sha1`, `MatchDetails_sha1` since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Changed mapping for `event.idm.read_only_udm.target.process.file.sha256` from `MatchDetails.match.properties.file.sha256`, `MatchDetails.match.properties.sha256` to `MatchDetails_file_sha256`, `MatchDetails_sha256` since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Changed mapping for this field and its parent processes from `MatchDetails.match.properties...ppid` fields to intermediate variables (`ppid`, `parent_ppid`, etc.) since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.parent_process.file.sha1`: Changed mapping for this field and its parent processes from `MatchDetails.match.properties...file.sha1` fields to intermediate variables (`parent_sha1`, `parent2_sha1`, etc.) since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.target.process.parent_process.file.sha256`: Changed mapping for this field and its parent processes from `MatchDetails.match.properties...file.sha256` fields to intermediate variables (`parent_sha256`, `parent2_sha256`, etc.) since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.security_result.about.process.command_line`: Changed mapping for this field and its parent processes from `MatchDetails.match.properties...args` fields to intermediate variables (`MatchDetails_args`, `MatchDetails_parent_args`, etc.) since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.security_result.about.process.file.full_path`: Changed mapping for this field and its parent processes from `MatchDetails.match.properties...name` fields to intermediate variables (`name`, `parent_name`, etc.) since the log is a nested json with varied structure.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Changed mapping for fields related to parent user and process start times from `MatchDetails.match.properties...` fields to intermediate variables (e.g., `parent_user`, `parent_start_time`, etc.) since the log is a nested json with varied structure.  
\- The logic for accessing nested `MatchDetails` fields has been refactored to first populate an intermediate local variable and then use that variable for UDM field mapping, preventing errors from halting filter execution.   
2025-08-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_id` raw log field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_address` raw log field(s).  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `creation_time` raw log field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped based on a conditional check of the `object_type_name` raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `AlertId`, `modifier_user_id`, `object_id`, `type`, `modification_time`, `object_name`, `last_modified_by`, `audit_row_id` raw log field(s).  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `evt_name` raw log field to `security_result.detection_fields`.  
\- `event.idm.read_only_udm.principal.port`: Changed mapping for event.idm.read_only_udm.principal.port from `MatchDetails.match.properties.local_port` to a temporary variable `MatchDetails_match_properties_local_port`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Changed mapping for event.idm.read_only_udm.network.ip_protocol from `MatchDetails.match.properties.protocol` to a temporary variable `match_properties_protocol`.  
\- `event.idm.read_only_udm.target.ip`: Changed mapping for event.idm.read_only_udm.target.ip from `MatchDetails.match.properties.remote_ip` to a temporary variable `match_properties_remote_ip`.  
\- `event.idm.read_only_udm.target.port`: Changed mapping for event.idm.read_only_udm.target.port from `MatchDetails.match.properties.remote_port` to a temporary variable `match_properties_remote_port`.  
\- For parent processes 4 through 7, mappings for the following UDM fields were updated to use temporary variables instead of direct deep-field access, to improve safety:  
\- `event.idm.read_only_udm.target.process.parent_process...product_specific_process_id`  
\- `event.idm.read_only_udm.target.process.parent_process...file.sha1`  
\- `event.idm.read_only_udm.target.process.parent_process...file.sha256`  
\- `event.idm.read_only_udm.security_result.about.process.parent_process...command_line`  
\- `event.idm.read_only_udm.security_result.about.process.parent_process...file.full_path`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- Renamed from `Alert Id` to `AlertId`.  
\- Added conditional checks for temporary variables populated from `MatchDetails` to safely access nested fields.  
\- Added `on_error` for all new `mutate` and `convert` blocks to handle potential parsing and conversion failures gracefully.  
\- `event.idm.read_only_udm.metadata.event_type`: If `object_type_name` matches `authentication`, updated to `USER_LOGIN`.  
\- Added JSON parsing for the `MatchDetails` field to flatten its structure.  
\- Added GROK parsing for the `details` field to extract `user_id`, `session_id`, and `ip_address`.  
\- Added a `gsub` filter to unescape quotes (`\\"`) in the raw log message.  
\- The `metadata.product_event_type` field is now dynamically populated using the `audit_type` and `type_name` fields.   
2025-02-06 |  Enhancement:  
\- Mapped `MITRE Techniques` to `security_result.attack_details.techniques`.  
\- Mapped `Impact Score` to `security_result.detection_fields`.   
2025-01-03 |  Enhancement:  
\- Converted file md5 values to lowercase.   
2024-11-28 |  Enhancement:  
\- Added support for unparsed `MatchDetails` field.   
2024-10-16 |  Enhancement:  
\- Mapped `MatchDetails.match.properties.parent.args` to `security_result.about.process.parent_process.command_line`.  
\- Mapped `MatchDetails.match.properties.parent.parent.args` to `security_result.about.process.parent_process.parent_process.command_line`.  
\- Mapped `MatchDetails.match.properties.parent.parent.parent.args` to `security_result.about.process.parent_process.parent_process.parent_process.command_line`.  
\- Mapped `MatchDetails.match.properties.parent.parent.parent.parent.args` to `security_result.about.process.parent_process.parent_process.parent_process.parent_process.command_line`.   
2023-07-28 |  Enhancement:  
\- Removed `MatchDetails.finding.system_info` from initialization.   
2023-07-13 |  Enhancement:  
\- Added a check for the SYSLOG+JSON format logs after identifying the JSON format failed.   
2023-03-13 |  Bug Fix:  
\- Resolved error by adding a conditional check before setting `is_alert` value to `true`.   
2022-11-14 |  Enhancement:  
\- Mapped `id` to `target.resource.attribute.labels`.  
\- Mapped `params` to `security_result.detection_fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
