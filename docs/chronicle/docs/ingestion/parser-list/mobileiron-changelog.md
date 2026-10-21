---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mobileiron-changelog/
title: Change log for MOBILEIRON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:11:36.768408+00:00
---

# Change log for MOBILEIRON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mobileiron-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MOBILEIRON

Date | Changes  
---|---  
2026-05-06 |  Enhancement  
\- Added a grok pattern to correctly parse the syslog format of the logs.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `common_client_id` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.software.name`: Newly mapped `common_client_name` raw log field with `event.idm.read_only_udm.principal.asset.software.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.software.version`: Newly mapped `common_client_version` raw log field with `event.idm.read_only_udm.principal.asset.software.version` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ios_ip_address`, `common_ip_address`, `ios_vpn_ip_address` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.creation_time`: Newly mapped `common_creation_date` raw log field with `event.idm.read_only_udm.principal.asset.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.principal.user.phone_numbers`: Newly mapped `common_current_phone_number`, `common_home_phone_number` raw log fields with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `common_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.manufacturer`: Newly mapped `common_manufacturer` raw log field with `event.idm.read_only_udm.principal.asset.hardware.manufacturer` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.serial_number`: Newly mapped `common_SerialNumber` raw log field with `event.idm.read_only_udm.principal.asset.hardware.serial_number` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.model`: Newly mapped `common_model` raw log field with `event.idm.read_only_udm.principal.asset.hardware.model` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `common_os_version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `common_uuid` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `common_wifi_mac_address`, `ios_BluetoothMAC` raw log fields with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.platform_patch_level`: Newly mapped `ios_BuildVersion` raw log field with `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `ios_iPhoneUDID` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_email_address`, `user_ldap_user_attributes_mail` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.first_name`: Newly mapped `user_first_name` raw log field with `event.idm.read_only_udm.principal.user.first_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.last_name`: Newly mapped `user_last_name` raw log field with `event.idm.read_only_udm.principal.user.last_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.last_login_time`: Newly mapped `user_last_admin_portal_login_time` raw log field with `event.idm.read_only_udm.principal.user.last_login_time` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `user_uuid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `user_ldap_user_object_sid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `user_ldap_user_attributes_memberOf`, `user_ldap_groups` raw log fields with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `common_client_build_date`, `common_compliant` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `common_data_protection_enabled`, `common_device_is_compromised` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `ios_DeviceName`, `ios_iPhoneVERSION`, `ios_iPhonePRODUCT`, `ios_ProductName` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `user_sam_account_name`, `user_ldap_attr_dn`, `user_ldap_dn`, `user_ldap_principal`, `user_ldap_upn`, `user_ldap_user_attributes_sAMAccountName`, `user_ldap_user_attributes_displayName`, `user_ldap_user_attributes_givenName`, `user_ldap_user_attributes_sn`, `user_ldap_user_attributes_userPrincipalName` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `common_apns_capable`, `common_background_status`, `common_battery_level`, `common_blocked`, `common_cellular_technology`, `common_device_admin_enabled`, `common_device_encrypted`, `common_lang_country_id`, `common_language`, `common_language_id`, `common_mutual_auth_enabled`, `common_locale`, `common_intune_compliance_azure_device_id`, `common_intune_compliance_azure_client_status_code`, `common_intune_compliance_azure_tenant_id`, `common_mdm_managed`, `common_miclient_last_connected_at`, `common_mdm_tos_accepted`, `common_model_name`, `common_modified_at`, `common_processor_architecture`, `common_quarantined_action`, `common_quarantined`, `common_registration_date`, `common_retired`, `common_roaming`, `common_sd_card_encrypted`, `common_security_state`, `common_status`, `common_storage_capacity`, `common_storage_free`, `common_catalog_ids`, `common_device_space_ids`, `common_device_space_path`, `common_device_space_name`, `common_mtd_status`, `common_mtd_anti_phishing_status`, `common_mtd_anti_phishing_vpn_status`, `common_ccm_migration_status`, `common_auth_only`, `common_EnhancedLoggingEnabled`, `ios_apnsToken`, `ios_osUpdateStatus`, `ios_data_protection`, `ios_DataRoamingEnabled`, `ios_PersonalHotspotEnabled`, `ios_forceEncryptedBackup`, `ios_HardwareEncryptionCaps`, `ios_iOSBackgroundStatus`, `ios_IsDeviceLocatorServiceEnabled`, `ios_IsDoNotDisturbInEffect`, `ios_iTunesStoreAccountIsActive`, `ios_IsDEPEnrolledDevice`, `ios_IsDEPDevice`, `ios_IsMDMServiceEnrolledDevice`, `ios_IsCloudBackupEnabled`, `ios_IsNetworkTethered`, `ios_IsActivationLockEnabled`, `ios_ActivationLockBypassCode`, `ios_it_policy_result`, `ios_PasscodeIsCompliant`, `ios_PasscodeIsCompliantWithProfiles`, `ios_PasscodePresent`, `ios_security_reason_code`, `ios_VoiceRoamingEnabled`, `ios_wakeup_status`, `ios_IsMDMLostModeEnabled`, `ios_IsMultiUser`, `ios_sim_countOfSims`, `ios_Supervised`, `ios_TimeZone`, `ios_apple_user_enrolled_device`, `ios_TrustedDevice`, `ios_ddm_enabled`, `ios_ddm_capabilities_available`, `common_owner`, `user_ldap_user_account_control_account_disabled`, `user_ldap_user_account_control_password_expired`, `user_ldap_user_account_control_locked_out`, `user_ldap_user_attributes_distinguishedName`, `user_ldap_user_attributes_objectSid`, `user_ldap_user_attributes_cn`, `user_ldap_user_attributes_userAccountControl` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: If `common_platform_name` and `common_platform` raw log fields contain `ios`, updated `event.idm.read_only_udm.principal.platform` to `MAC`.   
2026-04-24 |  Enhancement  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `BLOCK` with `event.idm.read_only_udm.security_result.action` UDM field if `resultStatus` has value `FAILURE`.   
2026-04-16 |  Enhancement  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actorId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actorName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actorUid` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `actorRoles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `resultStatus` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `resultStatus` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `actionType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `entityName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `entityId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `entityType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.user.group_identifiers`: Newly mapped `entityGroup` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `entityAuditId`, `details` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `entityDeleted`, `expiresAt`, `publishedAt`, `publisherId`, `tenantUuid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated to `NETWORK_CONNECTION`, `USER_UNCATEGORIZED`, `STATUS_UPDATE` and `USER_RESOURCE_ACCESS` based on required UDM fields.   
2026-03-16 |  Enhancement  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a grok pattern to correctly parse a SYSLOG format where the time field was previously being misidentified as part of the SystemType field. The time value is now correctly extracted due to the addition of the new grok pattern.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Mapped `time` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- Added a regex pattern to remove trailing periods from `kv_msg` and `kv_data`.  
\- Added a gsub function to remove commas from the `product` raw log field.   
2026-02-10 |  Enhancement  
\- Added grok patterns to correctly parse the SYSLOG format of logs.  
\- Added null check condition for `sr_action` field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for `date_time` raw log field to parse `event.idm.read_only_udm.metadata.event_timestamp` UDM field in correct format.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `command` raw log field to `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when `has_resource` is `true`.   
2025-12-05 |  Enhancement  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `host` from `event.idm.read_only_udm.principal.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `host` from `event.idm.read_only_udm.principal.asset.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `product`, `ip_in_bracket` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: The static value has been updated from `MOBILEIRON` to `Ivanti`.  
\- event.idm.read_only_udm.metadata.product_name: Changed mapping for event.idm.read_only_udm.metadata.product_name from `product` raw log field to `Endpoint Manager Mobile` static value.  
\- event.idm.read_only_udm.metadata.product_name: The static value has been updated from `MOBILEIRON` to `Endpoint Manager Mobile`.   
2025-11-10 |  Enhancement  
\- Added support for syslog format.  
\- Set metadata.event_type to NETWORK_CONNECTION when both principal and target IP addresses are present.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `app_name` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `procid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msgid` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_host` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url_1` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `session_user` raw log fields to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `response_size` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referrer` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `http_status` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `date_time` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `ip_1` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `time` raw log field to `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `t1`, `mem_percent`, `vsz`, `rss`, `stat`, `start`, `token_id`, `tag`, `safepoint_ns_1`, `safepoint_ns_2`, `ns_1`, `duration_ms`, `apache_error_code`, `log_year`, `module`, `error_code` and `attempts` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `run_user`, `systemd_user`, `type`, `safepoint_type` and `http_request` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped from the `loglevel` raw field, set to `INFORMATIONAL`, `ERROR`, or `MEDIUM` based on case-insensitive checks for `INFO`, `Error`, or `Warning` to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped from the `loglevel` raw field when loglevel does not match the conditions for security_result.severity to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `summary` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `program_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `user`, `nice`, `iowait`, `steal`, `idle` and `system` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2024-11-07 |  Enhancement  
\- Added support for syslog format.   
2023-02-02 |  Enhancement  
\- Update the existing mapping `security_result.summary` to `security_result.description` for `complianceViolationTypeToReason.BLACKLIST_APPS`.  
\- Mapped `complianceViolationTypeToReason.SA` to `security_result.summary`.   
2022-04-25 |  Enhancement - Modified event_type from `GENERIC_EVENT` to `USER_UNCATEGORIZED`  
\- Mapped `policyViolatedAt` to `metadata.event_timestamp`  
\- Mapped `platformType` to `principal.asset.platform_software.platform`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
