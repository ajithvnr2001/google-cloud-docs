---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-alerts-changelog/
title: Change log for CS_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:38.708959+00:00
---

# Change log for CS_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CS_ALERTS

Date | Changes  
---|---  
2026-10-06 |  \- security_result.about.user.product_object_id: Removed mapping of `assigned_to_uuid` from `security_result.about.user.product_object_id` UDM field for better mapping accuracy.  
\- additional.fields[assigned_to_uuid]: Newly mapped `assigned_to_uuid` raw log field with `additional.fields[assigned_to_uuid]` UDM field.  
\- security_result.about.user.user_display_name: Removed mapping of `assigned_to_name` from `security_result.about.user.user_display_name` UDM field for better mapping accuracy.  
\- additional.fields[assigned_to_name]: Newly mapped `assigned_to_name` raw log field with `additional.fields[assigned_to_name]` UDM field.   
2026-09-01 |  \- security_result.about.user.userid: Removed mapping of `assigned_to_uid` from `security_result.about.user.userid` UDM field for better mapping accuracy.  
\- additional.fields[assigned_to_uid]: Newly mapped `assigned_to_uid` raw log field with `additional.fields[assigned_to_uid]` UDM field.   
2026-02-18 |  \- principal.user.userid: Removed mapping of `user_id` from `principal.user.userid` UDM field if `user_id` value is in valid SID format.  
\- principal.user.windows_sid: Newly mapped `user_id` raw log field with `principal.user.windows_sid` UDM field if `user_id` value is in valid SID format.   
2026-01-20 |  \- `security_result.action`: Included all the possible values of `pattern_disposition` raw log field to populate `security_result.action` UDM field.  
\- `security_result.action`: Removed mapping of `pattern_disposition_details` from `security_result.action` UDM field.   
2026-01-12 |  \- `security_result.rule_name`: Newly mapped `mitre_attack.technique` raw log field with `security_result.rule_name` UDM field where `technique` field is not present but the `mitre_attack` array object is available.  
\- `security_result.rule_id`: Newly mapped `mitre_attack.technique_id` raw log field with `security_result.rule_id` UDM field where `technique_id` field is not present but the `mitre_attack` array object is available.  
\- `security_result.category`: Newly set `security_result.category` UDM based on the `mitre_attack.technique` raw log field values.  
\- The event mapping will be updated to provide more accurate classification for events where the `technique` field is not present but the newly inroduced `mitre_attack` array object is available. Events that were previously mapped as `SCAN_UNCATEGORIZED` may now be mapped to a more precise event_type based on the `technique` in the first mitre_attack object.  
\- Additionally, the following field mappings will be updated based on the revised event mapping. For events previously mapped as `SCAN_UNCATEGORIZED` that are now mapped to `SCAN_FILE`, the mappings will change as follows:  
The fields under `target.process.file.*` will be removed and instead mapped to `target.file.*`.   
2026-01-06 |  Updated the field mapping for the epp product to accurately map `incident.score`, `severity`, and `severity_name` fields.  
\- If both `severity` and `incident.score` raw fields are present, `severity` will be prioritized and mapped to the `security_result.severity_details` UDM field, while `incident.score` will be mapped to the `security_result.risk_score` UDM field.  
\- If only the `incident.score` raw field is present, it will be mapped to `security_result.severity_details` UDM fields.   
2025-12-31 |  \- Handled the parser edge cases for the field mapping logic.   
2025-11-14 |  \- security_result.severity: Updated the logic for mapping the `security_result.severity` UDM field based on the `incident.score` value when that field is available in the raw log.  
\- Below is the revised logic for populating the UDM field security_result.severity, based on the value ranges of the raw log field incident.score:  
\- 80-100: CRITICAL  
\- 60-79: HIGH  
\- 40-59: MEDIUM  
\- 20-39: LOW  
\- 0-19: INFORMATIONAL   
2025-10-28 |  \- additional.fields[is_closed] : Newly mapped `is_closed` raw log field with `additional.fields[is_closed]` UDM field.  
\- security_result.detection_fields[lead_id] : Newly mapped `lead_id` raw log field with `security_result.detection_fields[lead_id]` UDM field.  
\- security_result.detection_fields[lead_type] : Newly mapped `lead_type` raw log field with `security_result.detection_fields[lead_type]` UDM field.  
\- security_result.confidence_score : Newly mapped `score` raw log field with `security_result.confidence_score` UDM field.  
\- security_result.detection_fields[signal_start_timestamp] : Newly mapped `signal_start_timestamp` raw log field enum value with `security_result.detection_fields[signal_start_timestamp]` UDM field.  
\- security_result.detection_fields[signal_end_timestamp] : Newly mapped `signal_end_timestamp` raw log field enum value with `security_result.detection_fields[signal_end_timestamp]` UDM field.  
\- security_result.detection_fields[signal_updated_timestamp] : Newly mapped `signal_updated_timestamp` raw log field enum value with `security_result.detection_fields[signal_updated_timestamp]` UDM field.  
\- Enhance the parser to parse the mitre_attack field.   
2025-10-27 |  \- Added support for new product alerts: `automated-lead-context`, `automated-lead`, `thirdparty`.  
\- Below mappings are updated to map more fields more accurately:  
\- target.process.command_line: Removed mapping of `cmdline` from `target.process.command_line` UDM field and mapped `reconstructed_command_line` instead.  
\- security_result.detection_fields[cmdline]: Newly mapped `cmdline` raw log field with `security_result.detection_fields[cmdline]` UDM field in case of `reconstructed_command_line` field is not empty.  
\- security_result.about.hostname: Removed mapping of `host_names` first index value from `security_result.about.hostname` UDM field for thirdparty product alerts.  
\- principal.hostname: Newly mapped `host_names` first index value with `principal.hostname` UDM field for thirdparty product alerts.   
2025-10-10 |  \- security_result.detection_fields[anomalous_ticket_content_classification] : Newly mapped `anomalous_ticket_content_classification` raw log field enum value with `security_result.detection_fields[anomalous_ticket_content_classification] ` UDM field.  
\- security_result.detection_fields[isp_classification] : Newly mapped `isp_classification` raw log field enum value with `security_result.detection_fields[isp_classification] ` UDM field.  
\- security_result.detection_fields[ldap_search_query_attack] : Newly mapped `ldap_search_query_attack` raw log field enum value with `security_result.detection_fields[ldap_search_query_attack] ` UDM field.  
\- security_result.detection_fields[model_anomaly_indicators] : Newly mapped `model_anomaly_indicators` raw log field enum value with `security_result.detection_fields[model_anomaly_indicators] ` UDM field.  
\- security_result.detection_fields[protocol_anomaly_classification] : Newly mapped `protocol_anomaly_classification` raw log field enum value with `security_result.detection_fields[protocol_anomaly_classification] ` UDM field.  
\- security_result.detection_fields[rpc_op_classification] : Newly mapped `rpc_op_classification` raw log field enum value with `security_result.detection_fields[rpc_op_classification] ` UDM field.  
\- security_result.detection_fields[suspicious_machine_account_alteration_type] : Newly mapped `suspicious_machine_account_alteration_type` raw log field enum value with `security_result.detection_fields[suspicious_machine_account_alteration_type] ` UDM field.   
2025-09-29 |  Updated field mapping for `incident.score`, `severity` and `severity_name` to map more accurately.  
\- security_result.severity_details: Removed mapping of `severity` from `security_result.severity_details` UDM field and mapped `incident.score` field instead.  
\- security_result.severity: Removed mapping of `severity_name` from `security_result.severity` UDM field and mapped `incident.score` field ranges 0-10 instead.  
\- security_result.detection_fields[score]: Removed mapping of `incident.score` from `security_result.detection_fields[score]` UDM field and mapped `severity` instead. It will be mapped only when `incident.score` is available in the log.   
2025-09-19 |  \- This is a new Premium version for the CS_ALERTS parser.  
\- For the configuration details along with the list mapping which were changed in comparison to the existing default parser, please check the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr#udm-mapping-delta-cs-alerts   
2025-08-26 |  Changing existing mappings in order to introduce more accurate mappings for `target.process.command_line`, `target.file.full_path` and `target.file.sha256` for the epp product and ofp type.  
\- target.process.command_line: Removed mapping of `cmdline` from `target.process.command_line` UDM field when `macros.cmdline` raw log field is not empty.  
\- security_result.detection_fields[cmdline]: Mapped `cmdline` raw log field with `security_result.detection_fields[cmdline]` UDM field when `macros.cmdline` raw log field is not empty.  
\- target.process.command_line: Newly mapped `macros.cmdline` raw log field with `target.process.command_line` UDM field.  
\- target.file.full_path: Removed mapping of `filepath` from `target.file.full_path` UDM field when `macros.ioc_description` raw log field is not empty.  
\- security_result.detection_fields[filepath]: Mapped `filepath` raw log field with `security_result.detection_fields[filepath]` UDM field when `macros.ioc_description` raw log field is not empty.  
\- target.file.full_path: Newly mapped `macros.ioc_description` raw log field with `target.file.full_path` UDM field.  
\- target.file.sha256: Removed mapping of `sha256` from `target.file.sha256` UDM field when `macros.ioc_value` raw log field is not empty and `macros.ioc_type` is equal to `hash_sha256`.  
\- security_result.detection_fields[sha256]: Mapped `sha256` raw log field with `security_result.detection_fields[sha256]` UDM field when `macros.ioc_value` raw log field is not empty and `macros.ioc_type` is equal to `hash_sha256`.  
\- target.file.sha256: Newly mapped `macros.ioc_value` raw log field with `target.file.sha256` UDM field when `macros.ioc_type` is equal to `hash_sha256`.  
\- security_result.detection_fields[macros_display_name]: Newly mapped `macros.display_name` raw log field with `security_result.detection_fields[macros_display_name]` UDM field.  
\- security_result.detection_fields[macros_ioc_source]: Newly mapped `macros.ioc_source` raw log field with `security_result.detection_fields[macros_ioc_source]` UDM field.  
\- security_result.detection_fields[macros_md5]: Newly mapped `macros.md5` raw log field with `security_result.detection_fields[macros_md5]` UDM field when `macros.md5` raw log field is not equal to `N/A`.  
\- security_result.detection_fields[macros_sha256]: Newly mapped `macros.sha256` raw log field with `security_result.detection_fields[macros_sha256]` UDM field.  
\- security_result.detection_fields[macros_type]: Newly mapped `macros.type` raw log field with `security_result.detection_fields[macros_type]` UDM field.  
\- security_result.detection_fields: Newly mapped `macros.ioc_type` raw log field with `security_result.detection_fields.key` UDM field and `macros.ioc_value` raw log field with `security_result.detection_fields.value` UDM field.   
2025-08-14 |  Changing existing mappings in order to introduce more accurate mappings for `security_result.rule_id` and `security_result.rule_name` for the CWPP, MOBILE, and OVERWATCH products.  
\- security_result.rule_id: Removed mapping of `technique_id` from `security_result.rule_id` UDM field and mapped `pattern_id` instead for `CWPP`, `MOBILE` and `OVERWATCH` product.  
\- security_result.rule_name: Removed mapping of `technique` from `security_result.rule_name` UDM field and mapped `name` instead for `CWPP`, `MOBILE`, and `OVERWATCH` product.  
\- security_result.detection_fields[pattern_id]: Removed mapping of `pattern_id` from `security_result.detection_fields[pattern_id]` UDM field for `CWPP`, `MOBILE` and `OVERWATCH` product.  
\- security_result.detection_fields[name]: Removed mapping of `name` from `security_result.detection_fields[name]` UDM field for `CWPP`, `MOBILE` and `OVERWATCH` product.  
\- security_result.detection_fields[xdr_rule_id]: Removed mapping of `xdr_rule_id` from `security_result.detection_fields[xdr_rule_id]` UDM field for `XDR` product.   
2025-08-08 |  Changing existing mappings in order to introduce more accurate mappings for `security_result.rule_id` and `security_result.rule_name` for the XDR, IDP, NGSIEM, and EPP products.  
\- security_result.rule_id: Removed mapping of `technique_id` from `security_result.rule_id` UDM field and mapped `xdr_rule_id` instead for `XDR` product.  
\- security_result.rule_id: Removed mapping of `technique_id` from `security_result.rule_id` UDM field and mapped `correlation_rule_id` instead for `NGSIEM` product.  
\- security_result.rule_id: Removed mapping of `technique_id` from `security_result.rule_id` UDM field and mapped `pattern_id` instead for `IDP` product.  
\- security_result.rule_id: Removed mapping of `technique_id` from `security_result.rule_id` UDM field and mapped `rule_instance_id` if not empty otherwise mapped `pattern_id` field instead for `EPP` product.  
\- security_result.rule_name: Removed mapping of `technique` from `security_result.rule_name` UDM field and mapped `name` instead for `EPP`, `NGSIEM`, `XDR` and `IDP` product.  
\- security_result.detection_fields[pattern_id]: Removed mapping of `pattern_id` from `security_result.detection_fields[pattern_id]` UDM field for `IDP` product.  
\- security_result.detection_fields[pattern_id]: Removed mapping of `pattern_id` from `security_result.detection_fields[pattern_id]` UDM field for `epp` product when `rule_instance_id` field is not present.  
\- security_result.detection_fields[name]: Removed mapping of `name` from `security_result.detection_fields[name]` UDM field for `EPP`, `NGSIEM`, `XDR` and `IDP` product.   
2025-06-27 |  \- Enhance the parser to parse the host_type raw field.   
2025-05-20 |  \- metadata.product_event_type: Newly mapped `product` raw log field with `metadata.product_event_type` UDM field   
2025-05-08 |  \- Newly created CS_ALERTS parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
