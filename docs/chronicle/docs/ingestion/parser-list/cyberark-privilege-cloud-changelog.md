---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-privilege-cloud-changelog/
title: Change log for CYBERARK_PRIVILEGE_CLOUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:32.971110+00:00
---

# Change log for CYBERARK_PRIVILEGE_CLOUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-privilege-cloud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERARK_PRIVILEGE_CLOUD

Date | Changes  
---|---  
2025-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `suser` raw log field to `event.idm.read_only_udm.principal.user.userid` when `Issuer` is empty.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `cs1` raw log field to `event.idm.read_only_udm.target.user.userid` when `cs1Label` is `Affected User Name` and `duser` is empty.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `cs4` raw log field to `event.idm.read_only_udm.target.resource.name` when `cs4Label` is `Database`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `app` and `fname` from `event.idm.read_only_udm.additional.fields`, These fields are now mapped to their appropriate udm fields.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `fname` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- `event.idm.read_only_udm.target.application`: Mapped `app` raw log field to `event.idm.read_only_udm.target.application`.  
\- Added support for the event `FILE_OPEN` when `act` is `Open File` and `target.file.full_path` and principal fields are present.  
\- Added support for the event `FILE_READ` when `act` is `Retrieve File` and `target.file.full_path` and principal fields are present.  
\- Mapped `event.idm.read_only_udm.target.resource.resource_type` to the static value `DATABASE` when `cs4Label` is `Database`.  
\- Initialized additional CEF label fields (`cs1Label`, `cs3Label`, `cs4Label`, `cs5Label`, `cn1Label`, `cn2Label`) for use in conditional logic.   
2025-09-10 |  Enhancement:  
\- Added Grok support for SYSLOG + KV format.  
\- Refactored parser logic to support logs containing multiple events in a single log entry.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ExtraDetails`, `LogonDomain` and `TicketID` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `Location` raw log field to event.idm.read_only_udm.principal.location.name.  
\- event.idm.read_only_udm.principal.port: Newly mapped `Port` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `Category` raw log field to event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ProductTag` raw log field to event.idm.read_only_udm.security_result.detection_fields.   
2025-08-18 |  Enhancement:  
\- Updated the conditional logic for assigning USER_UNCATEGORIZED to the event_type field.   
2025-06-20 |  Enhancement:  
\- Newly added new grok pattern to parse `host` raw field correctly.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `app`, `Otherinfo`,and `Otherinfo` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `AffectedUserName` ,`RequestId`, `SafeName`,and `Database` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-11-13 |  Enhancement:  
\- Changed mapping of the syslog header `hostname` from `principal.hostname` to `intermediary.hostname`.   
2024-10-30 |  Enhancement:  
\- Mapped `hostn` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `MessageID`, `Version`, `Safe`, `PolicyID`, `DeviceType`, and `Address` to `additional.fields`.  
\- Mapped `GatewayStation` to `target.ip`.  
\- Mapped `UserName` to `principal.user.user_display_name`.  
\- Mapped `Station` to `principal.ip`.  
\- Mapped `Message` to `security_result.summary`.  
\- Mapped `Issuer` to `principal.user.userid`.  
\- Mapped `Station` to `principal.ip`.  
\- Mapped `File` to `principal.file.full_path`.  
\- Mapped `Severity` to `security_result.severity`.  
\- Mapped `CPMStatus` to `security_result.action`.   
2024-08-21 |  Enhancement:  
\- Mapped `host` to `principal.hostname` and `principal.asset.hostname`.   
2024-03-17 |  Enhancement:  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `device_event_class_id` and `event_name` to `metadata.product_event_type`.  
\- Mapped `msg` to `metadata.description`.  
\- If `shost` is IP then mapped `shost` to `principal.ip` else mapped it to `principal.hostname`.  
\- If `dvc` to `principal.hostname`.  
\- Mapped `dhost` to `target.hostname`.  
\- Mapped `duser` to `target.user.user_display_name`.  
\- Mapped `suser` to `principal.user.user_display_name`.  
\- Mapped `act` to `security_result.action_details`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `cn1`, `cn1Label`, `cn2`, `cn2Label`, `cs1`, `cs1Label`, `cs2`, `cs2Label`, `cs3`, `cs3Label`, `cs4`, `cs4Label`, `cs5`, `cs5Label`, and `fname` to `additional.fields`.   
2023-11-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
