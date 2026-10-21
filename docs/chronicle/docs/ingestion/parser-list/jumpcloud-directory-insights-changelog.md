---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jumpcloud-directory-insights-changelog/
title: Change log for JUMPCLOUD_DIRECTORY_INSIGHTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:47:11.189509+00:00
---

# Change log for JUMPCLOUD_DIRECTORY_INSIGHTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jumpcloud-directory-insights-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUMPCLOUD_DIRECTORY_INSIGHTS

Date | Changes  
---|---  
2026-06-26 |  Enhancement:  
-`event.idm.read_only_udm.target.resource.type`: Removed mapping of `connection_to_type`,`type` from `event.idm.read_only_udm.target.resource.type` UDM field since `event.idm.read_only_udm.target.resource.type` UDM field is deprecated.  
-`event.idm.read_only_udm.target.resource.resource_subtype`: Mapped `connection_to_type`,`type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
-`event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `data.jc_initiated_by_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
-`event.idm.read_only_udm.metadata.description`: Newly mapped `data_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
-`event.idm.read_only_udm.principal.network.asn`: Newly mapped `data_asn_number` raw log field with `event.idm.read_only_udm.principal.network.asn` UDM field.  
-`event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `data.resource.app_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
-`event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `data.jc_initiated_by_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
-`event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `resource_system_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `data_asn_network`, `data.windows_meta_elevated`, `data.system_timestamp`, `data.repeat_count`, `data.is_out_of_bound`, `data.app_management_source`, `data.timestamp_source`, `data_to`, `data_from`, `data_state`, `asn_organization`, `process_name`,`message_timestamp` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.id`: Removed mapping of `data.system.id` and `data.resource.id` from `event.idm.read_only_udm.principal.resource.id` UDM field as the UDM field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `data.system.id` and `data.resource.id` raw log fields with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- Added null conditional checks.  
\- Added drop condition for invalid logs.  
\- Added grok filter to check for valid ip address.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.server_timestamp`, `data.timestamp_source`, `data.is_out_of_bound` and `data.jc_application_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `data.resource.type` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.@version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `data.application.version` is not null.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.system.id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `data.resource.id` is not null.   
2026-01-27 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `data.alert_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `data.alert_title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `data.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `data.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.priority: Newly mapped `data.priority` raw log field with `event.idm.read_only_udm.security_result.priority` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `data.rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `data.event_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `data.di_event.event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `data.di_event.initiated_by.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `data.di_event.initiated_by.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `data.di_event.client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data.di_event.association.action_source`, `data.di_event.initiated_by.id`, `data.di_event.useragent.name`, `data.di_event.association.connection.from.object_id`, `data.di_event.association.op`, `data.di_event.id`, `data.in_console_alert`, `data.di_event.tags`, `data.di_event.useragent.os_name`, `data.di_event.useragent.device`, `data.di_event.useragent.version`, `data.di_event.auth_method`, `data.previous_alert_status`, `data.resolution_condition`, `data.source_id`, `data.source_type`, `data.updated_at`, `data.violation_condition`, `data.di_event.association.connection.from.type`, `data.di_event.association.connection.to.type`, `data.di_event.file_input_timestamp`, `data.di_event.geoip.continent_code`, `data.di_event.geoip.region_code`, `data.di_event.geoip.timezone`, `data.di_event.initiated_by.type`, `data.di_event.useragent.major`, `data.di_event.useragent.minor`, `data.di_event.useragent.os`, `data.di_event.useragent.os_full`, `data.di_event.useragent.patch` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `data.di_event.association.connection.from.name` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.about.user.userid: Newly mapped `data.di_event.association.connection.to.name` raw log field with `event.idm.read_only_udm.about.user.userid` UDM field.  
\- event.idm.read_only_udm.about.user.product_object_id: Newly mapped `data.di_event.association.connection.to.object_id` raw log field with `event.idm.read_only_udm.about.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `data.di_event.success` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `data.di_event.service` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `data.di_event.geoip.country_code` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.user.company_name: Newly mapped `data.organization_name` raw log field with `event.idm.read_only_udm.principal.user.company_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `data.di_event.@version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `data.source_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `data.di_event.initiated_by.source` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `data.source_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.location.region_latitude: Newly mapped `data.di_event.geoip.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_longitude: Newly mapped `data.di_event.geoip.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `data.di_event.geoip.region_name` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data.di_event.organization` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true` and `event_description` is `membership is updated`, `updated to `GROUP_MODIFICATION`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true`, `updated to `USER_UNCATEGORIZED`.  
\- Added gsub to replace `@timestamp` with `timestamp` in the message field.   
2025-10-14 |  Enhancement:  
\- event.idm.read_only_udm.metadata.vendor_name: Changed mapping for `event.idm.read_only_udm.metadata.vendor_name` from `JUMPCLOUD_DIRECTORY_INSIGHTS` to `Jump Cloud`.  
\- event.idm.read_only_udm.metadata.product_name: Changed mapping for `event.idm.read_only_udm.metadata.product_name` from `JUMPCLOUD_DIRECTORY_INSIGHTS` to `Directory Platform`.   
2025-09-25 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped data.system.host_name raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped data.initiated_by.type raw log field to event.idm.read_only_udm.target.resource.type.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped data.geoip.timezone raw log field to event.idm.read_only_udm.principal.location.name.  
\- event.idm.read_only_udm.target.location.name: Newly mapped data.auth_context.jumpcloud_protect_device.geoip.timezone raw log field to event.idm.read_only_udm.target.location.name.  
\- event.idm.read_only_udm.target.location.state: Newly mapped data.auth_context.jumpcloud_protect_device.geoip.region_name raw log field to event.idm.read_only_udm.target.location.state.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped data.auth_context.jumpcloud_protect_device.geoip.country_code raw log field to event.idm.read_only_udm.target.location.country_or_region.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped data.auth_context.jumpcloud_protect_device.app_version raw log field to event.idm.read_only_udm.principal.asset.platform_software.platform_version.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `data.system.display_name` raw log field to event.idm.read_only_udm.principal.user.user_display_name  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped data.auth_context.jumpcloud_protect_device.os raw log field to event.idm.read_only_udm.principal.asset.platform_software.platform.  
\- event.idm.read_only_udm.target.ip: Newly mapped data.auth_context.jumpcloud_protect_device.ip raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped data.auth_context.jumpcloud_protect_device.ip raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.platform_version: Newly mapped data.auth_context.jumpcloud_protect_device.os_version raw log field to event.idm.read_only_udm.target.platform_version.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped data.service raw log field to event.idm.read_only_udm.target.resource.name.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped data.auth_context.jumpcloud_protect_device.username raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `dc_1` and `dc_2` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `uid` raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped data.outer.username raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.security_result.description: Newly mapped data.operation_type raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Newly mapped `data.eap_type` and `data.mech` raw log field to event.idm.read_only_udm.extensions.auth.auth_details.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of data.event_type from event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped data.event_type raw log field to event.idm.read_only_udm.metadata.product_event_type.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `start_tls`, `tls_established`, `error_code`, `operation_number`, `outer.eap_type`, `auth_meta.user_password_enabled`, `auth_meta.device_cert_enabled`, `auth_meta.user_cert_enabled`, `auth_meta.auth_idp`, `auth_meta.userid_type`, `data.error_message`, `data.auth_context.jumpcloud_protect_device.model`, `data.auth_context.auth_methods.jumpcloud_protect.success`, `data.useragent`, `data.mfa`, `data.mfa_meta.type`, `data.provider`, `data.initiated_by.id`, `data.auth_method`, `ou` and `o` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `data.username`, `connection_id`, `data.geoip.continent_code` and `data.auth_context.jumpcloud_protect_device.user_id` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `data.auth_context.jumpcloud_protect_device.geoip.region_code`, `data.auth_context.jumpcloud_protect_device.geoip.continent_code`, `auth_context.jumpcloud_protect_device.geoip.latitude`, `auth_context.jumpcloud_protect_device.geoip.longitude` and `data.auth_context.jumpcloud_protect_device.id` raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped `auth_type` raw log field to event.idm.read_only_udm.principal.resource.type.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `nas_mfa_state` raw log field to event.idm.read_only_udm.security_result.summary.  
\- Enhanced USER_LOGIN event detection to include ldap_bind, radius_auth_attempt, and user_login_attempt event types. Prioritized data.auth_context.auth_methods.password.success for determining security_result.action when available.   
2025-01-30 |  Enhancement:  
\- Mapped `association_op`, `action_source`, and `sso_token_success` to `additional.fields`.  
\- Mapped `connection_from_name` to `principal.resource.name`.  
\- Mapped `connection_from_type` to `principal.resource.resource_type`.  
\- Mapped `connection_from_object_id` to `principal.resource.product_object_id`.  
\- Mapped `connection_to_name` to `target.resource.name`.  
\- Mapped `connection_to_type` to `target.resource.resource_type`.  
\- Mapped `connection_to_object_id` to `target.resource.product_object_id`.   
2024-05-20 |  Enhancement:  
\- Added `gsub` to parse the unparsed invalid JSON logs.  
\- When `data.initiated_by.username` is present, then set `metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-01-10 |  Bug-Fix:  
\- Removed `gsub` to parse the logs which contain the `false` keyword.   
2023-11-21 |  Enhancement:  
\- Added `gsub` to remove the unwanted characters from the logs.   
2023-10-31 |  Enhancement:  
\- Added a gsub function to parse dropped logs.   
2023-10-16 |  Enhancement:  
\- Handled unparsed JSON logs.   
2023-04-11 |  Enhancement:  
\- Handled unparsed JSON logs.   
2023-02-20 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
