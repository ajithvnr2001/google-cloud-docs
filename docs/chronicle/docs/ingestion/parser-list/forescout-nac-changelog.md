---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-nac-changelog/
title: Change log for FORESCOUT_NAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:03:23.832319+00:00
---

# Change log for FORESCOUT_NAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-nac-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORESCOUT_NAC

Date | Changes  
---|---  
2026-03-27 |  Enhancement:  
\- Added support for new format of `Json` logs.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the mapping of `event.idm.read_only_udm.metadata.event_type` with `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.priority_details`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `appname` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `proc_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- Added a Grok pattern on json message field to parse user_name, session_id, log_description, and details fields.  
\- Added a Grok pattern to parse the `resource_name` field from `log_description` field.   
2025-10-13 |  Enhancement:  
\- Added a new grok pattern to `header_data` to parse the fields like `pid`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Source_1` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `Source_1` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Source_1` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Source_1` raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.target.ip: Newly mapped `Target_1` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `Target_1` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `Target_1` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `Target_1` raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac_addr` raw log field to event.idm.read_only_udm.principal.mac.   
2024-11-07 |  Enhancement:  
\- Mapped `cat` to `security_result.alert_state`.  
\- Mapped `eventtype` to `security_result.category_details`.  
\- Mapped `device_event_class_id` to `security_result.rule_id` and `event_name` to `security_result.summary`.   
2024-11-05 |  Bug-fix:  
\- Added support for new format of SYSLOG logs.   
2024-04-22 |  Bug-fix:  
\- Removed drop condition to parse unparsed logs.   
2024-02-05 |  Enhancement:  
\- Mapped `eventtype` to `additional.fields`.   
2024-01-29 |  Bug-Fix:  
\- Added new Grok patterns to parse CEF logs.  
\- Added condition to avoid conversion failure for `principal.port`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `action` to `security_result.action_details`.  
\- Mapped `resource` to `principal.resource.name`.  
\- Mapped `command` to `principal.process.command_line`.  
\- Mapped `version` to `metadata.product_version`.  
\- Added Grok patterns to parse the missing field values in description.  
\- Mapped `source_ip` to `principal.asset.ip`.  
\- Mapped `target_ip` to `target.asset.ip`.  
\- Mapped `computer_name` to `target.asset.hostname`.  
\- Mapped `destination` to `target.asset.hostname`.  
\- Mapped `Target` to `target.asset.hostname`.  
\- Mapped `Hostname` to `principal.asset.hostname`.  
\- Mapped `Source` to `principal.asset.hostname`.  
\- Mapped `middle_ip` to `intermediary.asset.ip`.  
\- Mapped `iporhost` to `intermediary.asset.hostname`.  
\- Mapped `Host` to `principal.asset.hostname`.   
2023-12-21 |  Bug-Fix:  
\- Added new Grok patterns for unparsed SYSLOG logs.  
\- Mapped `CPU usage`, `Available memory`, `Used memory`, `Available swap`, `Used swap`, `Application status`, `Connected Clients`, `EM connection status`, `Assigned hosts`, `Engine status` and `Installed plugins` to `additional.fields`.  
\- Added condition to check if message contains `CEF:` to parse `CEF` logs.   
2023-05-31 |  Enhancement:  
\- Enhanced parser to reduce `GENERIC_EVENT` and set the `metadata.event_type` to a more appropriate value.   
2022-10-07 |  Enhancement:  
\- Enhanced the parser to support CEF format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
