---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mist-changelog/
title: Change log for JUNIPER_MIST \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:38.987542+00:00
---

# Change log for JUNIPER_MIST  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mist-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUNIPER_MIST

Date | Changes  
---|---  
2026-05-20 |  Enhancement:  
\- Added support for JSON format logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `adminName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `admin_mail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message_data` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `org_id` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.group.product_object_id`: Newly mapped `site_id` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `site_name` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `sdkinvite_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.mac`, `event.idm.read_only_udm.target.asset.mac`: Newly mapped `device_mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM field when the value is a valid mac address.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `device_mac` field to event.idm.read_only_udm.target.resource.attribute.labels UDM field when the value is not a valid mac address.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `template_id` and `after_json.device_type` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`, `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: if principal user data is present then set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `map_id`, `after_json.map_id` and `before_json.map_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Added a Grok pattern on `event.idm.read_only_udm.metadata.description` to extract `role1` and `role2`.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `role1` and `role2` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `after_json.download_strategy`, `after_json.reboot_strategy`, `after_json.start_time`, `after_json.reboot_time`, `after_json.max_failure_percentage`, `after_json.device_ids`, `after_json.site_ids`, `after_json.rules.match_model`, `after_json.versions.firmware_type`, `after_json.versions.version`, `after_json.versions.force`, `before_json.x`, `after_json.x`, `before_json.y`, `after_json.y`, `before_json.x_m`, `after_json.x_m`, `before_json.y_m`, `after_json.y_m`, `after_json.heightSet`, `after_json.role`, `after_json.connected`, `after_json.locating`, `after_json.orientation`, `after_json.height`, `before_json.adopted`, `after_json.adopted`, `before_json.name`, `after_json.name`, and `after_json.notes`, `device_mac_1`, `site_id_1`, `site_name_1` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `invite_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.   
2025-03-13 |  Enhancement:  
\- Added a Grok pattern on `log_event.admin_name` to extract `user_name` and `user_id`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `user_name` to `principal.user.user_display_name`.  
\- Added a Grok pattern on `log_event.message` to extract `target_user_id`.  
\- Mapped `target_user_id` to `target.user.userid`.  
\- When `message` contains `Update Invite`, then set `metadata.event_type` to `USER_CREATION`.  
\- When `message` contains `Accessed/Invoked`, then set `metadata.event_type` to `USER_LOGIN`.   
2024-11-14 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-07-08 |  Enhancement:  
\- Mapped `event.ssids` and `event.bssids` to `principal.resource.attribute.labels`.   
2024-06-04 |  Enhancement:  
\- Mapped `event.admin_name` to `principal.administrative_domain`.  
\- Mapped `event.src_ip`, `event.client_ip`, and `event.ip` to `principal.ip`.  
\- Mapped `event.device_name` and `event.client_hostname` to `principal.hostname`.  
\- Mapped `event.device_type`, `event.mxedge_name`, `event.ssid`, and `event.mxedge_id` to `principal.resource.attribute.labels`.  
\- Mapped `event.mac` to `principal.mac`.  
\- Mapped `event.user_agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `event.message` to `metadata.description`.  
\- Mapped `event.client_username` to `principal.user.user_display_name`.  
\- Mapped `event.ap_name` to `principal.application`.   
2024-05-03 |  Enhancement:  
\- Mapped `site_id` to `src.asset.asset_id`.  
\- Mapped `site_name` to `src.asset.location.name`.  
\- Mapped `group` to `src.user.group_identifiers`.  
\- Mapped `hostnames` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `org_id` to `principal.asset_id`.  
\- Mapped `id` to `principal.asset.asset_id`.  
\- If `has_principal` is `true` and `has_target` is `false`, then set `metadata.event_type` to `USER_UNCATEGORIZED`, else set `metadata.event_type` to `GENERIC_EVENT`.   
2023-02-24 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
