---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/admanager-plus-changelog/
title: Change log for ADMANAGER_PLUS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:56.710743+00:00
---

# Change log for ADMANAGER_PLUS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/admanager-plus-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ADMANAGER_PLUS

Date | Changes  
---|---  
2026-04-24 |  Enhancement  
\- `event.idm.read_only_udm.metadata.product_event_type`: Removed mapping of `TechnicianName` from `event.idm.read_only_udm.metadata.product_event_type` UDM field, as `TechnicianName` more accurately represents the user performing the action, who is often an administrator, rather than the type of event.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `Object_Name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field. This change allows `Object_Name` to be conditionally mapped to the target user, as it often represents the object or user being acted upon.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `TechnicianName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field, as this field identifies the administrator initiating the event.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Mapped `Object_Name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field, as `Object_Name` typically contains the name of the entity being affected.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority`, `syslog_version` and `product_app_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field to capture additional syslog metadata.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Mapped `User_Name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field when `Object_Name` is empty.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `User_Name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when `Object_Name` is not empty.  
\- Added a Grok pattern to parse new format of SYSLOG + KV logs.   
2025-05-02 |  Enhancement  
\- `event.idm.ready_only_udm.principal.user.personal_address.name`: Newly mapped `streetAddress` raw log field with `event.idm.ready_only_udm.principal.user.personal_address.name` UDM field.  
\- `event.idm.ready_only_udm.principal.user.office_address.name`: Newly mapped `physicalDeliveryOfficeName` raw log field with `event.idm.ready_only_udm.principal.user.office_address.name` UDM field.  
\- `event.idm.ready_only_udm.principal.user.attribute.labels`: Newly mapped `postalCode`, `countryCode` raw log field with `event.idm.ready_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.ready_only_udm.principal.user.company_name`: Newly mapped `company` raw log field with `event.idm.ready_only_udm.principal.user.company_name` UDM field.  
\- `event.idm.ready_only_udm.principal.user.department`: Newly mapped `department` raw log field with `event.idm.ready_only_udm.principal.user.department` UDM field.  
\- `event.idm.ready_only_udm.security_result.detection_fields`: Newly mapped `accountExpires`, `ou_label_1`, `ou_label_2`, `ou_label_3`, `dc_label_1`, `dc_label_2`, `cn_label_1`, `cn_label_2`, `primary_dc_label_1`, `primary_dc_label_2`, `manager_cn_value1` manager_ou_value1`, `manager_ou_value2`, `manager_ou_value3`, `manager_dc_value1` and `manager_dc_value2` raw log field with `event.idm.ready_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.ready_only_udm.principal.user.first_name`: Newly mapped `givenName` raw log field with `event.idm.ready_only_udm.user.first_name` UDM field.  
\- `event.idm.ready_only_udm.additional.fields`: Newly mapped `sn`, `st`, `l` raw log field with `event.idm.ready_only_udm.additional.fields` UDM field.   
2025-04-09 |  Enhancement  
\- Modified the Grok pattern to parse the unparsed logs.  
\- event.idm.ready_only_udm.principal.url: Newly mapped `wWWHomePage` raw log field with `event.idm.ready_only_udm.principal.url` UDM field.  
\- event.idm.ready_only_udm.principal.user.phone_numbers: Newly mapped `homePhone` raw log field with `event.idm.ready_only_udm.principal.user.phone_numbers` UDM field.  
\- event.idm.ready_only_udm.principal.location.city: Newly mapped `co` raw log field with `event.idm.ready_only_udm.principal.location.city` UDM field.   
2025-03-19 |  Enhancement  
\- Added gsub support for month names to parse the unparsed logs.   
2025-02-17 |  Enhancement  
\- Newly created parser for ADMANAGER_PLUS.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
