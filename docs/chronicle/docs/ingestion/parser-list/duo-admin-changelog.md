---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-admin-changelog/
title: Change log for DUO_ADMIN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:13.724583+00:00
---

# Change log for DUO_ADMIN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/duo-admin-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DUO_ADMIN

Date | Changes  
---|---  
2026-06-24 |  Enhancement:  
\- Added a Grok pattern on `description.device` to differentiate between phone numbers and hostnames.  
\- `event.idm.read_only_udm.target.user.phone_numbers`: Removed mapping of `description.device` raw log field from `event.idm.read_only_udm.target.user.phone_numbers` UDM field when it does not matches a phone number pattern.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `description.device` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields when it does not match a phone number pattern.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `description.saml_idp`, `description.deleted_actcode`, `description.regen_mobile` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `description.notes` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine data and user data are present updated `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.   
2026-05-15 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `description.role` from `event.idm.read_only_udm.additional.fields` UDM field. As it is suitable to be mapped with `event.idm.read_only_udm.target.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles.name`: When `action` is related to login, Mapped `description.role` raw log field with `event.idm.read_only_udm.target.user.attribute.roles.name` UDM field  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: When `action` is not related to login, Mapped `description.role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `description.status` from `event.idm.read_only_udm.additional.fields` UDM field. As this is suitable to be mapped with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Mapped `description.status` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.target.user.phone_numbers`: Newly mapped `description.phone` raw log field with `event.idm.read_only_udm.target.user.phone_numbers` UDM field  
\- Added a grok pattern on `username` to extract `resource_name` and `app`.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `app` raw log field with `event.idm.read_only_udm.principal.application` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `description.is_temporary_password`, `description.hardtoken`, `description.restricted_by_admin_units` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-01-02 |  Enhancement:  
\- Mapped `description.webauthnkey` and `description.credential_name` to `additional.fields`.  
\- Mapped `description.owner_type` to `principal.user.role_name`.  
\- Mapped `description.owner_name` to `principal.user.user_display_name`.  
\- Mapped `description.owner_id` to `principal.user.attribute.labels`.   
2024-12-23 |  Enhancement:  
\- Added a Grok pattern to extract `trust-monitor` event from `triage_event_uri` and mapped it to `metadata.product_event_type`.  
\- Changed the mapping of `surfaced_auth.access_device.browser` from `target.resource.attribute.labels` to `principal.resource.attribute.labels`.  
\- Changed the mapping of `surfaced_auth.access_device.browser_version` from `target.resource.attribute.labels` to `principal.resource.attribute.labels`.   
2024-12-05 |  Enhancement:  
\- Mapped `triage_event_uri` to `metadata.url_back_to_product`.   
2024-10-23 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-08-27 |  Enhancement:  
\- Mapped `description.count`, `description.valid_secs`, `description.remaining_uses`, `description.bypass`, `description.bypass_code_ids.0`, `description.user_id`, `description.directory`, and `description.users` to `additional.fields`.   
2024-08-08 |  Enhancement:  
\- Mapped `description.os_version` to `principal.platform_version`.  
\- Mapped `description.lastname` to `principal.user.last_name`.  
\- Mapped `description.firstname` to `principal.user.first_name`.  
\- Mapped `description.name` to `principal.user.user_display_name`.  
\- Mapped `description.email` to `principal.user.email_addresses`.  
\- Mapped `description.phones.phone1.pname` to `principal.user.user_display_name`.  
\- Mapped `description.phones.phone1.number` to `target.user.phone_numbers`.  
\- Mapped `description.uname` to `target.user.email_addresses` or `target.user.userid` based on its format.  
\- Mapped `description.country_code`, `description.manufacturer`, `description.model`, `description.biometrics_status`, `description.tampered_status`, `description.passcode_status`, `description.phones.phone1.type`, `description.phones.phone1.extension`, `description.phones.phone1.notes`, `description.phones.phone1.predelay`, `description.phones.phone1.postdelay`, `object`, `actionlabel`, `description.role`, `description.subaccount_role`, `description.administrative_units`, `description.Users_added`, `description.Users_modified`, `description.Users_removed`, `description.Users_seen`, and `description.status` to `additional.fields`.   
2023-03-10 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
