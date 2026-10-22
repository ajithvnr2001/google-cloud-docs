---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-firewall-changelog/
title: Change log for PAN_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:50.445890+00:00
---

# Change log for PAN_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_FIREWALL

Date | Changes  
---|---  
2026-10-07 |  \- Enhanced the parser to handle the parsing of the Strata Logging Service new log format and added the support of the DNS event type of Strata Logging Service.   
2026-09-25 |  \- security_result.action: Newly mapped `Action` raw log field with `security_result.action` UDM field.   
2026-08-07 |  \- target.url_metadata.last_http_response_headers.fields: Newly mapped `HTTP Headers` raw log field with `target.url_metadata.last_http_response_headers.fields` UDM field.   
2026-06-17 |  Updated the parser to remove the duplicate and redundant field mappings for TRAFFIC events.  
\- target.hostname: Removed mapping of `device_name` from the target.hostname UDM field.  
\- target.hostname: Removed mapping of `dvchost` from `target.hostname` UDM field.  
\- target.hostname: Removed mapping of `DeviceName` from `target.hostname` UDM field.  
\- target.asset.hostname: Removed mapping of `device_name` from `target.asset.hostname` UDM field.  
\- target.asset.hostname: Removed mapping of `dvchost` from `target.asset.hostname` UDM field.  
\- target.asset.hostname: Removed mapping of `DeviceName` from `target.asset.hostname` UDM field.   
2026-06-05 |  Enhanced the parser to optimize and improve performance.   
2026-04-21 |  Enhanced the parser to update the existing field mappings and added new field mappings for the events TRAFFIC, THREAT and CORRELATION.  
\- intermediary.hostname: Newly mapped `Device Name` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.hostname: Newly mapped `dvchost` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.hostname: Newly mapped `DeviceName` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.asset.hostname: Newly mapped `Device Name` raw log field with `intermediary.asset.hostname` UDM field.  
\- intermediary.asset.hostname: Newly mapped `dvchost` raw log field with `intermediary.asset.hostname` UDM field.  
\- intermediary.asset.hostname: Newly mapped `DeviceName` raw log field with `intermediary.asset.hostname` UDM field.  
\- target.hostname: Newly mapped `Device Name` raw log field with `target.hostname` UDM field.  
\- target.hostname: Newly mapped `dvchost` raw log field with `target.hostname` UDM field.  
\- target.hostname: Newly mapped `DeviceName` raw log field with `target.hostname` UDM field.  
\- target.asset.hostname: Newly mapped `Device Name` raw log field with `target.asset.hostname` UDM field.  
\- target.asset.hostname: Newly mapped `dvchost` raw log field with `target.asset.hostname` UDM field.  
\- target.asset.hostname: Newly mapped `DeviceName` raw log field with `target.asset.hostname` UDM field.  
\- target.user.userid: Removed mapping of `PanOSUserBySource` from `target.user.userid` UDM field.  
\- target.user.userid: If `duser` raw log field is empty then mapped `PanOSUserBySource` raw log field with `target.user.userid` UDM field.Else `duser` raw log field is not empty then mapped `PanOSUserBySource` raw log field with `additional.fields`.   
2026-04-17 |  \- additional.fields: Newly mapped `Syslog Priority Value` raw log field with `additional.fields` UDM field.   
2026-03-25 |  Handled the edge case for the Miscellaneous raw log field.   
2026-03-19 |  Updated the event_type mapping in the parser for the `GLOBALPROTECT` log type.  
\- metadata.event_type: Updated the `metadata.event_type` to `USER_LOGIN` where logtype value is `GLOBALPROTECT` and event_id raw log field value is `auth` or `login` and stage raw log field value is `login`.  
\- metadata.event_type: Updated the `metadata.event_type` to `USER_LOGOUT` where logtype value is `GLOBALPROTECT` and event_id raw log field value is `logout` and stage raw log field value is `logout`.   
2026-02-27 |  Enhanced the parser to handle the parsing of the UDM field `target.user.userid`.   
2026-02-20 |  Added new field mappings for the events SYSTEM, CONFIG, HIPMATCH and IPTAG.  
\- intermediary.hostname: Newly mapped `dvchost` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.asset.hostname: Newly mapped `dvchost` raw log field with `intermediary.asset.hostname` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `PanOSVsysName` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- target.hostname: Newly mapped `dvchost` raw log field with `target.hostname` UDM field.  
\- target.asset.hostname: Newly mapped `dvchost` raw log field with `target.asset.hostname` UDM field.  
\- target.asset.attribute.labels: Newly mapped `PanOSVsysName` raw log field with `target.asset.attribute.labels` UDM field.   
2025-12-30 |  Added the field mapping for the field of the `SYSTEM`,`CONFIG`,`HIPMATCH` and `IPTAG` event type.  
\- intermediary.asset.hardware.serial_number: Newly mapped `Serial Number` raw log field with `intermediary.asset.hardware.serial_number` UDM field.  
\- intermediary.asset.hardware.serial_number: Newly mapped `deviceExternalId` raw log field with `intermediary.asset.hardware.serial_number` UDM field.  
\- intermediary.asset.hardware.serial_number: Newly mapped `SerialNumber` raw log field with `intermediary.asset.hardware.serial_number` UDM field.  
\- intermediary.hostname: Newly mapped `Device Name` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.hostname: Newly mapped `dvchost` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.hostname: Newly mapped `DeviceName` raw log field with `intermediary.hostname` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `Virtual System` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `PanOSVsysName` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `vSrcName` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `Virtual System (vsys)` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `cs3` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.asset.attribute.labels: Newly mapped `VirtualSystem` raw log field with `intermediary.asset.attribute.labels` UDM field.  
\- intermediary.resource.product_object_id: Newly mapped `Virtual System ID` raw log field with `intermediary.resource.product_object_id` UDM field.  
\- intermediary.resource.product_object_id: Newly mapped `cn2` raw log field with `intermediary.resource.product_object_id` UDM field.  
\- intermediary.resource.product_object_id: Newly mapped `VirtualSystemID` raw log field with `intermediary.resource.product_object_id` UDM field.   
2025-12-24 |  Updated the field mapping for the field of the `System` event type.  
\- observer.asset.hostname: Removed mapping of `LogSourceName` from `observer.asset.hostname` UDM field.  
\- target.resource.attribute.labels[`log_source_name`]: Mapped `LogSourceName` raw log field with `target.resource.attribute.labels[`log_source_name`]` UDM field.   
2025-12-15 |  Updated and added the field mapping for the fields of the `audit` event type.  
\- Added the Grok pattern to extract `Serial Number` from the `message` field.  
\- metadata.product_event_type: Newly mapped `Subtype` raw log field with `metadata.product_event_type` UDM field.  
\- metadata.description: Newly mapped `Description` raw log field with `metadata.description` UDM field.  
\- additional.fields: Newly mapped `Status` raw log field with `additional.fields` UDM field.  
\- principal.process.command_line: Removed mapping of `CLI Command` from `principal.process.command_line` UDM field, as this field is present in the product documentation but not in the log, which appears to be a product documentation gap.  
\- security_result.severity: Removed mapping of `Severity` from `security_result.severity` UDM field, as this field is present in the product documentation but not in the log, which appears to be a product documentation gap.   
2025-11-19 |  \- Update the mapping of fields and event type and added support of SCTP and AUDIT event types.  
\- Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-firewall#udm_mapping_delta   
2025-11-04 |  \- Added support for Strata Logging Service JSON format as part of parser refresher.   
2025-07-25 |  \- Enhanced the parser to parse the full description of the event into `metadata.description` UDM field.   
2025-06-23 |  \- `intermediary.asset.hardware.serial_number`: Removed mapping of `Serial Number (Column 103)` from `intermediary.asset.hardware.serial_number` UDM field and mapped `Serial Number(Column 3)` instead for CSV log format.   
2025-06-13 |  \- Added support for a log format in which CSV logs are wrapped in JSON with escaped characters.   
2025-06-06 |  Enhancement:  
\- Modified the mappings from `event.idm.read_only_udm.principal.labels` to `event.idm.read_only_udm.principal.resource.attribute.labels` since `event.idm.read_only_udm.principal.labels` is deprecated.  
\- Modified the mappings from `event.idm.read_only_udm.target.labels` to `event.idm.read_only_udm.target.resource.attribute.labels` since `event.idm.read_only_udm.target.labels` is deprecated.   
2025-04-28 |  \- `security_result.severity_details`: Newly mapped `severity` raw log field with `security_result.severity_details` UDM field for CEF format.  
\- `GTP`: Added support for the event `GTP` and relevant corresponding raw log fields.   
2025-02-14 |  \- Modified the Grok pattern to validate the `network.email.to` and `network.email.from` UDM fields.   
2025-01-27 |  \- Updated the parser to handle event type validation errors.   
2025-01-24 |  \- Fixed a typo in the parser configuration file for `target.asset.product_object_id`.   
2025-01-07 |  \- Modified the Grok for LEEF formatted logs to parse with for product name `PAN-OS SyslogIntegration`.   
2025-01-06 |  Enhancement:  
\- Handled error validation for the `target.url` field.   
2024-10-09 |  Enhancement:  
\- Added the mapping of `High Resolution Timestamp` for the auth subtype logs of SYSTEM.   
2024-09-09 |  Enhancement:  
\- Added Grok pattern in `security_result_threat_id` to parse the unparsed data.  
\- Mapped `malware_family` to `security_result.detection_fields`.  
\- Mapped `suspicious_dns_name` to `network.dns.questions`.   
2024-08-22 |  \- Modified grok pattern to extract values from `description` field with lowercase and special characters.   
2024-06-11 |  \- Modified the Grok pattern to extract `device_version` from the `message` field.  
\- Mapped `device_version` to `metadata.product_version`.   
2024-06-05 |  \- Updated the mapping condition for the `security_result.action` for the TRAFFIC logs.  
\- Updated the Grok pattern to extract the IP address from the `description` field.   
2024-05-22 |  \- Added mapping for the `product_version` in the CEF formatted logs.   
2024-05-16 |  \- Updated the Grok pattern to extract the userid `msg` field.  
\- Added mapping of `app` raw log field to `target.application` for the TRAFFIC logs.  
\- Added support for audit event logs.   
2024-04-17 |  \- Updated the `metadata.event_type` to `USER_LOGIN` where logtype value is `System` and message describes `Logged In` activity.   
2024-03-28 |  \- Added new time format in date filter.   
2024-03-13 |  \- Handle mapping of `characteristic_of_app` with `security_result.summary`.   
2024-02-19 |  \- Prioritized the `High Resolution Timestamp` raw field for the mapping of `metadata.event_timesatamp`.   
2024-02-14 |  \- Updated the Grok pattern to extract the correct userid and IP address from `msg` field.  
\- Updated the Grok pattern to extract URL and hostname from `misc` field.   
2024-01-31 |  \- Extracted domain and userid from `Source User` field.  
\- Updated the typo for `PanOSTimeGeneratedHighResolution` field for the logs of type `GLOBALPROTECT`.   
2024-01-17 |  Updated the typo for `PanOSTimeGeneratedHighResolution` field.  
Extracted `domain` and `userid` from `Source User` for `TRAFFIC` log type.  
Updated the Grok pattern to extract URL and hostname from `misc` field.  
Updated the Grok pattern to extract the correct user ID and IP address from `msg` field.   
2024-01-03 |  Updated the `metadata.event_type` to `USER_LOGIN` where logtype value is `System` and subtype value is `auth`.  
Supported new field names for the CEF format logs for `DECRYPTION`, `GLOBALPROTECT` and `AUTHENTICATION` log type.  
Extracted all possible values from the `msg` field and mapped accordingly.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.  
Added additional mapping by extracting values from `msg` field.  
Added mappings of the raw log fields which were mapped to the deprecated field `noun.labels`.   
2023-09-20 |  Updated the mapping of `msg` field to `metadata.description` field for LEEF log format.   
2023-09-06 |  Changed regular expression pattern to map all authentication events to `USER_LOGIN`.   
2023-06-28 |  Updated the parser to include `security_result.severity` field.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-02 |  \- Changed the mapping of the `network.sent_bytes` and `network.received_bytes` fields.   
2023-03-29 |  \- `security_result.action` field is set to `BLOCK` when the value of raw log field `act/action` is `drop-packet`.   
2023-03-15 |  \- Handled rename failure error for `GLOBALPROTECT` type logs in CEF format.   
2023-03-01 |  \- Added mapping of field bytes sent and bytes received to `about.labels` if the field value is 0.   
2023-02-15 |  \- Extracted numerical `threat_id` from `security_result.threat_name` and mapped it to `security_result.threat_id`.   
2023-02-01 |  \- Added mapping of `Application` field to `target.application` for `THREAT` type logs in CSV format.   
2022-12-09 |  \- Handled unnecessary double quotes.   
2022-11-16 |  \- Added gsub filters to handle unnecessary double quotes.  
\- Changed mapping of `misc` value for THREAT type logs. Now, in case of subtype `spyware` and `vulnerability`, value in misc variable will be mapped with `target.url` and `target.file.full_path` both. Also, restored `target.hostname` mapping for subtype `url' .  
\- Added validation check for network.session_duration.seconds   
2022-11-04 |  \- Modified mapping of `misc` field for subtype `spyware`, `misc` field value is mapped with `target.file.full_path`.   
2022-10-04 |  \- Added condition to parse newly injested csv format logs.   
2022-09-28 |  Promoted PAN_FIREWALL parser to default.  
For the field mapping differences, see [ https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/pan-firewall-map-changes>field mapping changes](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code)  
2022-03-28 |  Enhancement-Added mappings for certain fields when log is of type TRAFFIC/THREAT.  
\- Sequence Number to event.idm.read_only_udm.metadata.product_log_id.  
\- Session End Reason to event.idm.read_only_udm.security_result.summary.  
\- Session ID to event.idm.read_only_udm.network.session_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
