---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-btp-changelog/
title: Change log for SAP_BTP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:08:22.657758+00:00
---

# Change log for SAP_BTP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-btp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_BTP

Date | Changes  
---|---  
2026-09-03 |  \- `event.idm.read_only_udm.principal.user.user_display_name`: Conditionally mapped `user` to `event.idm.read_only_udm.principal.user.user_display_name` UDM field only when user is present.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field only when user is not present.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `json_message_identityProvider` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `json_message.success`, `json_message.attributes.successful` raw log fields with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `json_message_data` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `status`, `object_id_json_message` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `json_message_data_subject_id`, `json_message_object_id_name` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `json_message_data_subject_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `json_message_data_subject_role` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- When `crud_type` is `DELETE`, updated the value to `USER_RESOURCE_DELETION`.  
\- When `category` or `json_message_category` is `audit.data-modification` and user is present, updated the value to `USER_RESOURCE_UPDATE_CONTENT`.  
\- When `category` or `json_message_category` is `audit.data-access` and user and target resource are present, updated the value to `USER_RESOURCE_ACCESS`.  
\- When principal machine data is present, updated the value to `STATUS_UPDATE`.  
\- When user is present, updated the value to `USER_UNCATEGORIZED`.   
2024-07-19 |  -Mapped `uuid`,`data`,`attributes`,`id`,`customDetails` to `security_result.detection_fields`.   
2024-02-22 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
