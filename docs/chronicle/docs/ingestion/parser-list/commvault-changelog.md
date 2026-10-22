---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/commvault-changelog/
title: Change log for COMMVAULT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:39.502822+00:00
---

# Change log for COMMVAULT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/commvault-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for COMMVAULT

Date | Changes  
---|---  
2026-06-24 |  Enhancement:  
\- Added new grok patterns to parse different formats of the `Details` field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `Utctimestamp` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.permissions`: Newly mapped `permission1`, `permission2`, `permission3`, `permission4`, `permission5`, `permission6`, `permission7`, `permission8`, `permission9`, `permission10`, `permission11`, `permission12`, `permission13`, `permission14`, `permission15`, `permission16`, `permission17`, `permission18` raw log fields to `event.idm.read_only_udm.target.resource.attribute.permissions` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `role` raw log field to `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `role_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_name` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `new_guid` raw log field to `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `agent_type` raw log field to `event.idm.read_only_udm.target.resource.resource_type` (set to VIRTUAL_MACHINE when `agent_type` contains `Virtual Server`) UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `User` raw log field to `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `login_attempted_from`, `subclient_set`, `transport_mode`, `volume_restore_type`, `restore_deleted_items`, `to_time`, `restore_from_copy_precedence`, `is_from_browse_backup`, `restore_acls`, `source_item`, `user_password_user_name`, `server_logon_account_user_name`, `advanced_restore_options_old`, `advanced_restore_options_new`, `new_name`, `disks_new_name`, `disks_datastore`, `disks_name`, `destination_client_name` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `subclient`, `subclient_set` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `esx_host`, `login_name` raw log fields to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `schedules_old`, `schedules_new`, `schedule_type`, `operation_type`, `is_disk_browse`, `use_vcloud_login`, `disk_option`, `vcenter_esx`, `datastore` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category1`, `category2`, `category3`, `category4`, `category5`, `category6`, `category7`, `category8`, `category9`, `category10`, `category11`, `category12`, `category13`, `category14`, `category15`, `category16`, `category17`, `category18` raw log fields to `event.idm.read_only_udm.security_result.category_details` UDM field.   
2025-02-20 |  Enhancement:  
\- Added `gsub` to map `Occurrencetime` to `metadata.event_timestamp`.   
2025-01-22 |  Enhancement:  
\- Mapped `Commcellname` to `additional.fields`.  
\- Mapped `Operation` to `metadata.description`.  
\- Mapped `Companyname` to `principal.user.company_name`.  
\- Mapped `machine_name` to `principal.hostname`.  
\- Mapped `locale` to `additional.fields`.   
2024-10-08 |  Enhancement:  
\- Mapped `computer` to `principal.hostname` and `principal.asset.hostname`.   
2023-11-10 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
