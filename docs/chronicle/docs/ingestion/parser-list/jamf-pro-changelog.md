---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-pro-changelog/
title: Change log for JAMF_PRO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:57.385106+00:00
---

# Change log for JAMF_PRO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-pro-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JAMF_PRO

Date | Changes  
---|---  
2025-10-20 |  Enhancement:  
\- Newly added Grok pattern for `message` data field to parse the logs in proper manner.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `computer_meta.name`, `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `when_milliseconds` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `combined_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.description` : Newly mapped `event_message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `loglevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field and mapped as `MEDIUM` when it has value `WARN` and `INFORMATIONAL` when it has value `INFO` and `ERROR` when it has value `ERROR`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-10-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `webhook.eventTimestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `webhook.name`, `event_value.trigger`, `webhook.id`, `webhook.webhookEvent` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `event_value.computer.udid`, `event_value.udid` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `event_value.computer.deviceName`, `event_value.deviceName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `event_value.computer.model`, `event_value.model`, `event_value.userDirectoryID`, `event_value.computer.osBuild`, `event_value.osBuild`, `event_value.computer.jssID`, `event_value.jssID`, `event_value.computer.managementId`, `event_value.managementId`, `event_value.computer.serialNumber`, `event_value.serialNumber`, `event_value.userDirectoryID`, `event_value.computer.userDirectoryID`, raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `event_value.computer.macAddress`, `event_value.macAddress`, `event_value.computer.alternateMacAddress`, `event_value.alternateMacAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `event_value.computer.osVersion`, `event_value.osVersion` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `event_value.computer.username`, `event_value.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `event_value.computer.realName`, `event_value.realName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `event_value.computer.emailAddress`, `event_value.emailAddress` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.phone_numbers`: Newly mapped `event_value.computer.phone`, `event_value.phone` raw log field with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.principal.user.title`: Newly mapped `event_value.computer.position`, `event_value.position` raw log field with `event.idm.read_only_udm.principal.user.title` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `event_value.computer.ipAddress`, `event_value.ipAddress`, `event_value.computer.reportedIpV4Address`, `event_value.reportedIpV4Address`, `event_value.reportedIpV6Address`, `event_value.computer.reportedIpV6Address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_value.building`, `event_value.department`, `event_value.room` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-09-11 |  Enhancement:  
\- Added support to parse JSON logs.   
2024-06-21 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
