---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-scaleft-changelog/
title: Change log for OKTA_SCALEFT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:30.186566+00:00
---

# Change log for OKTA_SCALEFT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-scaleft-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OKTA_SCALEFT

Date | Changes  
---|---  
2026-05-06 |  \- Added a grok pattern on `details.user_access_method` to extract `desc` and `asset_id`.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `asset_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `details.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `details.actor` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `details.client` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `details.username`, `details.server.server_accounts.username` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.project.name`: Newly mapped `details.project` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.project.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `details.server.server_accounts` raw log field with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.   
2025-08-18 |  Newly created parser:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `details.from_address`, `details.client_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `details.from_address`, `details.client_ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `details.type` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `details.actor.status`, `details.actor.user_type` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Newly mapped `details.session_type` raw log field(s) with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `details.actor.name`, `details.unix_user_name` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `details.actor.details.full_name` raw log field(s) with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.first_name: Newly mapped `details.actor.details.first_name` raw log field(s) with `event.idm.read_only_udm.principal.user.first_name` UDM field.  
\- event.idm.read_only_udm.principal.user.last_name: Newly mapped `details.actor.details.last_name` raw log field(s) with `event.idm.read_only_udm.principal.user.last_name` UDM field.  
\- event.idm.read_only_udm.principal.user.employee_id: Newly mapped `details.actor.id` raw log field(s) with `event.idm.read_only_udm.principal.user.employee_id` UDM field.  
\- event.idm.read_only_udm.principal.user.department: Newly mapped `details.actor.team_name` raw log field(s) with `event.idm.read_only_udm.principal.user.department` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `details.client.hostname` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `details.client.hostname` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `details.client.id` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `details.client.description` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `details.client.os` raw log field(s) with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `details_client_os` raw log field(s) with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `details.actor.details.email` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `details.team_id`, `details.project.id` raw log field(s) with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `details.team_name` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `details.client.state` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `details.target_server` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `details.via`, `details.trace_id` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `details_session_type`, `details.ssh_public_key` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped `details.actor.details.user_type` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `details.project.name` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `details.server.id`, `details.server.state`, `details.project.team`, `details.project.create_server_users`, `details.project.force_shared_ssh_users`, `details.project.forward_traffic`, `details.project.next_unix_gid`, `details.project.next_unix_uid`, `details.project.rdp_session_recording`, `details.project.require_preauth_for_creds`, `details.project.ssh_certificate_type`, `details.project.ssh_session_recording`, `serverhostname`, `alt_name`, `details.ssh_key_fingerprint` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.platform_version: Newly mapped `details.server.os`, `detailsserver.os` raw log field(s) with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- event.idm.read_only_udm.target.platform: Newly mapped `details.server.os_type`, `detailsserver.os_type` raw log field(s) with `event.idm.read_only_udm.target.platform` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `details_team_id` raw log field(s) with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `details.client.encrypted` raw log field(s) with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `details.client.user_name` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `serverhostname`, `alt_name` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `alt_name` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary`, `intermediary_value` raw log field(s) with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `detailsserver.sftd_version`, `details.server.sftd_version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.target.asset.attribute.labels: Newly mapped `detailsserver.state`, `detailsserver.managed`, `detailsserver.ssh_key_fingerprint` raw log field(s) with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `details.username` raw log field(s) with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `details.ssh_algorithm` raw log field(s) with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `OKTA_SCALEFT` static value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `OKTA_SCALEFT` static value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped `SSO` static value with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Added conditional check to set `event_type:  
\- If `has_principal_user` is `true` and `has_target_user` is `true`, updated to `USER_LOGIN`.  
\- If `has_principal_user` is `true` and `details_type` contains `login`, updated to `USER_LOGIN`.  
\- If `has_principal_user` is `true`, updated to `USER_UNCATEGORIZED`.  
\- If `has_principal` is `true`, updated to `STATUS_UPDATE`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
