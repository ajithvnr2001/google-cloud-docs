---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-remote-access-changelog/
title: Change log for BEYONDTRUST_REMOTE_ACCESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:32.601992+00:00
---

# Change log for BEYONDTRUST_REMOTE_ACCESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-remote-access-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BEYONDTRUST_REMOTE_ACCESS

Date | Changes  
---|---  
2025-12-04 |  Enhancement -  
\- `event.idm.read_only_udm.metadata.product_event_type`: Removed mapping of `product_event_type` raw log field from `event.idm.read_only_udm.metadata.product_event_type` UDM field since it was a valid `hostname` and in order to introduce a more accurate mapping we had removed the mappings of this raw log field `product_event_type` from its following UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `product_event_type` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field in order to map it to the appropriate UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `old_support:permissions:screen_sharing:annotations`, `old_support:prompting:command_shell`, `old_support:prompting:default`, `old_support:prompting:deploy_callback_button`, `old_support:prompting:elevate`, `old_support:prompting:file_transfer`, `old_support:prompting:registry`, `old_support:prompting:request_pin_unpin`, `old_support:prompting:screen_sharing:full_access`, `old_support:prompting:system_info`, `old_support:prompting:timeout`, `old_support:session:termination_behavior`, `stem_info_actions`, `old_support:prompting:screen_sharing`, `old_support:session:termination_behavior_rep_override` raw log fields with `event.idm.read_only_udm.additional.fields`.   
2025-11-14 |  Enhancement -  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped ack_button, code_name, new_authorization:allowed_approvers, old_authorization:allowed_approvers, old_authorization:allowed_to, old_authorization:approver_name, old_authorization:approver_teams, old_authorization:approvers, old_authorization:email_addresses, old_authorization:enabled, old_authorization:locale_code, old_authorization:max_duration, old_code_name, old_description, old_display_name, old_id, old_notification:email_addresses, old_notification:locale_code, old_support:permissions:command_shell, old_support:permissions:command_shell_commands, old_support:permissions:command_shell_is_whitelist, old_support:permissions:elevation, old_support:permissions:file_transfers:cust, old_support:permissions:file_transfers:download, old_support:permissions:file_transfers:rep, old_support:permissions:file_transfers:upload, old_support:permissions:registry_access, old_support:permissions:request_pin_unpin, old_support:permissions:screen_sharing, old_support:permissions:screen_sharing:application_restriction, old_support:permissions:screen_sharing:application_sharing, old_support:permissions:screen_sharing:clipboard_direction, old_support:permissions:screen_sharing:privacy_mode, old_support:permissions:screen_sharing:show_screen, support:permissions:allow_pinned_clients, support:permissions:allow_users, support:permissions:canned_scripts, support:permissions:chat, support:permissions:chat:push_url, support:permissions:chat:send_file, support:permissions:command_shell, support:permissions:command_shell_commands, support:permissions:command_shell_is_whitelist, support:permissions:deploy_callback_button, support:permissions:elevation, support:permissions:file_transfers:cust, support:permissions:file_transfers:download, support:permissions:file_transfers:rep, support:permissions:registry_access, support:permissions:request_pin_unpin, support:permissions:screen_sharing, support:permissions:screen_sharing:allow_elevated_tools, support:permissions:screen_sharing:annotations, support:permissions:screen_sharing:application_restriction, support:permissions:screen_sharing:application_sharing, support:permissions:screen_sharing:automatic_privacy_screen_request, support:permissions:screen_sharing:clipboard_direction, support:permissions:screen_sharing:privacy_mode, support:permissions:screen_sharing:show_screen, support:permissions:system_info, support:permissions:system_info:actions, support:prompting:default, support:prompting:deploy_callback_button, support:prompting:elevate raw log fields to the `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_hostname` raw log field to event.idm.read_only_udm.intermediary.asset.hostname UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestampvalue` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added conditional mapping for target, status, eventName raw log fields.  
\- Added new grok pattern for `message` data field to parse the logs in correct manner.   
2025-11-09 |  Enhancement -  
\- `event.idm.read_only_udm.extensions.auth.type`: Conditional mapping applied: Only mapped to `SSO` if `target` == `web/login` AND `who` =~ `using saml`, else if `target` == `rep_client` mapped to `MACHINE`, else mapped to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `category` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `nvps.auditid` raw log field to event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `nvps.ipaddress` raw log field to event.idm.read_only_udm.principal.ip UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `nvps.ipaddress` raw log field to event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `nvps.appuserid` raw log field to event.idm.read_only_udm.target.user.product_object_id UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `eventdate` raw log field to event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `agentid` raw log field to event.idm.read_only_udm.observer.application UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `nvps.systemname` raw log field to event.idm.read_only_udm.target.application UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `intermediary_ip` raw log field to event.idm.read_only_udm.intermediary.ip UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip` raw log field to event.idm.read_only_udm.intermediary.asset.ip UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `nvps.username` raw log field to event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nvps.authenticationtype`, `nvps.eventseverity`, `nvps.createdate`, `formatVersion`, `eventid`, `eventsubject`, `eventtype`, `nvps.subjectdescription`, `nvps.actiontype` raw log field(s) to event.idm.read_only_udm.additional.fields UDM field.   
2025-10-10 |  Enhancement -  
\- Added new grok pattern for the `message` data field to parse the logs in correct manner and to parse the dropped logs.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `eventName` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_LOGIN` if `eventName` contains `token` value in it.  
\- Added a grok pattern on `site` data field to extract `pra_hostname` , `appliance` data fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appliance`, `appliance_identifier` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.   
2022-09-30 |  Enhancement -  
\- Wrote grok to parse unparse syslogs".  
\- Mapped `device_vendor` to `additional.fields`.  
\- Mapped `event_name` to `additional.fields`.  
\- Mapped `device_product` to `additional.fields`.  
\- Mapped `externalKeyLabel` to `additional.fields`.  
\- Mapped `dstPriv` to `additional.fields`.  
\- Mapped `filePath` to `target.file.full_path`.  
\- Mapped `fsize` to `target.file.size`.   
2022-07-14 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
