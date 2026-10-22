---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-dlp-changelog/
title: Change log for SYMANTEC_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:06.742285+00:00
---

# Change log for SYMANTEC_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_DLP

Date | Changes  
---|---  
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `incident_snap` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- Modified grok patterns to handle `Severity` format variations.  
\- Refactored parser logic for `recipient` and `sender` email addresses to support `from=` prefix and enforce length constraints.   
2025-08-21 |  Enhancement:  
\- Renamed from `policy_rule` field to `subject` in the grok pattern because it maps to a `subject` field, not a `rule_name` field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `policy_rule` from `event.idm.read_only_udm.security_result.rule_name` UDM field.  
event.idm.read_only_udm.network.email.subject: Mapped `subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If the event_type is `SCAN_NETWORK`, updated to `EMAIL_TRANSACTION`.   
2025-07-22 |  Enhancement:  
\- Added a grok pattern to parse the log.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `policies` raw log field to event.idm.read_only_udm.security_result.rule_id.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule` raw log field to event.idm.read_only_udm.security_result.rule_name.  
\- event.idm.read_only_udm.security_result.rule_name: Removed mapping of `asunto` raw log field from event.idm.read_only_udm.security_result.rule_name as asunto represents the email subject, not the rule name.  
\- event.idm.read_only_udm.network.email.subject: Mapped `asunto` raw log field to event.idm.read_only_udm.network.email.subject.   
2025-07-10 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added a separate date filter for timestamp which do not have year and updated `rebase` to `true`.  
\- Added a grok pattern for `dhost` and `temp_dhost` to validate the hostname.  
\- Added `N/A` with null check for `fname` before mapping it with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `cnt` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `resolution` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url : Added a check to ensure if `dhost` is a URL before mapping it with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field when it contains email .  
\- Added a grok pattern for `dhost` to extract hostname from URL.   
2025-06-05 |  Enhancement:  
\- Added Grok to handle the `occurredOn` field properly.   
2025-05-15 |  Enhancement:  
\- Added support to handle the `occurredOn` field properly.  
\- event.idm.read_only_udm.security_result.verdict.response_count : Newly Mapped `Total Count` raw log field to `event.idm.read_only_udm.security_result.verdict.response_count` UDM field.   
2025-02-04 |  Enhancement:  
\- Added support for SYSLOG logs.   
2025-01-08 |  Enhancement:  
\- Mapped `ATTACHMENT_FILENAME` to `principal.file.full_path`.  
\- When `DATAOWNER_NAME` is present, then mapped `DATAOWNER_NAME` to `principal.user.userid`.  
\- When `DATAOWNER_NAME` is not present, then mapped `ENDPOINT_USERNAME` to `principal.user.userid`.   
2024-12-27 |  Enhancement:  
\- Added support to parse the new log format.   
2024-12-04 |  Enhancement:  
\- Added support to parse the new log format.   
2024-11-11 |  Enhancement:  
\- Added support to parse the new log format.   
2024-09-05 |  Enhancement:  
\- Added support to parse the new log format.   
2024-06-17 |  Enhancement:  
\- Added support to parse the new format of field `recipients`.   
2024-06-14 |  Enhancement:  
\- Added support for CEF Logs.   
2024-05-16 |  Enhancement:  
\- Mapped `dlp_type` to `security_result.detection_fields`.   
2024-04-26 |  Bug-Fix:  
\- Mapped `recipients` to `target.user.email_addresses`.   
2024-03-10 |  Enhancement:  
\- Added new Grok patterns to parse logs of new SYSLOG formats.  
\- Mapped `server` to `target.application`.  
\- Mapped `url` to `target.url`.  
\- Mapped `dataowner_mail` to `principal.user.email_addresses`.  
\- Mapped `reported_on` and `monitor_name` to `additional.fields`.  
\- Mapped `sender` to `network.email.from`.  
\- Mapped `subject` to `network.email.subject`.   
2024-02-20 |  Enhancement:  
\- Mapped `blocked` to `security_result.action_details` and `security_result.action`.   
2024-01-12 |  Enhancement:  
\- Mapped `incident_id` and `DLP_EP_Incident_ID` to `security_result.detection_fields`.  
\- Added a Grok pattern to parse logs of new SYSLOG formats.  
\- Mapped `location` to `principal.resource.attribute.labels`.  
\- Mapped `target_type` to `target.resource.attribute.labels`.   
2023-12-06 |  Enhancement:  
\- Added a Grok pattern to parse logs of new formats.  
\- Mapped `application` to `principal.application`.  
\- Mapped `application_name` to `target.application`.  
\- Mapped `policy_name` to `security_result.detection_fields`.   
2023-09-02 |  Enhancement:  
\- Added support to parse failing logs and mapped the fields accordingly.   
2023-08-17 |  Enhancement:  
\- Mapped `Occurred on` to `principal.labels`.  
\- When `act` is `Modified`, set `security_result.action` to `ALLOW_WITH_MODIFICATION`.  
\- Mapped `status` to `principal.labels`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
