---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/island-browser-changelog/
title: Change log for ISLAND_BROWSER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:43:28.729010+00:00
---

# Change log for ISLAND_BROWSER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/island-browser-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ISLAND_BROWSER

Date | Changes  
---|---  
2026-06-01 |  Enhancement:  
\- Added gsubs to parse the new format of logs.   
2026-05-14 |  Enhancement:  
\- Added gsubs to parse the failed JSON logs.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Newly mapped `details.application_parameters_details_list.parameters.parameter_value` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field where `parameter_name` is `project`.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `details.application_parameters_details_list.parameters.parameter_value` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field where `parameter_name` is `domain`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details.application_parameters_details_list.parameters.parameter_name`, `matchedDevicePosture.azure_ad`, `matchedDevicePosture.registry_keys` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `matchedDevicePosture.client_certificates` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `logMessage.userId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `logMessage.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `logMessage.userName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `logMessage.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` as `ALLOW` if `logMessage.verdict` is `Allowed`, as `BLOCK` if `logMessage.verdict` is `Blocked` else `UNKNOWN_ACTION`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `logMessage.verdict` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `logMessage.topLevelUrl` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `logMessage.sourceIp` and `logMessage.publicIp` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `logMessage.sourceIp` and `logMessage.publicIp` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `logMessage.saasApplicationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `logMessage.saasApplicationCategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `logMessage.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `logMessage.region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Conditionally mapped from `logMessage.details.application_parameters_details_list[*].parameters` where parameter_name is `project`.  
\- `event.idm.read_only_udm.target.administrative_domain`: Conditionally mapped from `logMessage.details.application_parameters_details_list[*].parameters` where parameter_name is `domain`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `logMessage.osUserName` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `logMessage.machineId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Conditionally mapped from `logMessage.osPlatform (`WINDOWS`, `MAC`, `LINUX`)`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `logMessage.saasApplicationId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `logMessage.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `logMessage.tenantId` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logMessage.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.creation_time`: Newly mapped `logMessage.createdDate` raw log field with `event.idm.read_only_udm.target.resource.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.last_update_time`: Newly mapped `logMessage.updatedDate` raw log field with `event.idm.read_only_udm.target.resource.attribute.last_update_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `logMessage.frameUrl`, `logMessage.urlWebCategories`, `logMessage.urlWebReputation`, `logMessage.countryCode`, `logMessage.origin`, `logMessage.tabId`, logMessage.details.application_parameters_details_list.application_id`, `logMessage.processedDate`, `logMessage.syslogConnectorId` and `logMessage.window_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `logMessage.details.navigation_details.is_fail_open_close_active`, `logMessage.details.navigation_details.is_iframe`, `logMessage.details.navigation_details.is_fail_open_close_active`, `logMessage.details.policy_version_details.application_access_policy_version`, `logMessage.details.policy_version_details.browser_access_policy_version`, `logMessage.details.policy_version_details.browser_policy_version`, `logMessage.details.policy_version_details.dlp_policy_version`, `logMessage.details.policy_version_details.pam_policy_version`, `logMessage.isIslandPrivateAccess`, `logMessage.compatibilityMode`, `logMessage.matchedDevicePosture.client_certificates.issuer`, `logMessage.matchedDevicePosture.client_certificates.subject`, `logMessage.matchedDevicePosture.client_certificates.thumbprint`, `logMessage.machineName`, `logMessage.deviceId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `logMessage.ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `logMessage.ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` as `USER_RESOURCE_ACCESS` if `has_principal_user` and `has_resource` are true.   
2025-12-08 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `Id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user_email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `auth_application` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `Client_sending_date` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `Client_event_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `User_name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Machine_name` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Machine_name` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `Country` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Public_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `Public_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Source_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `Source_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `Top_level_url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `Window_id` raw log field to `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `Saas_application_name` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly `mapped Machine_id` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.about.url: Newly mapped `Frame_url` raw log field to `event.idm.read_only_udm.about.url` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `Os_platform` raw log field to `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `Region` raw log field to `event.idm.read_only_udm.principal.location.state` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `Saas_application_id` raw log field to `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `Rule_id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `Rule_name` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.confidence_score: Newly mapped `Url_web_reputation` raw log field to `event.idm.read_only_udm.security_result.confidence_score` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `Saas_application_category` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `Verdict_reason` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Compatibility_mode`, `Processed_date`, `Country_code`, `Is_island_private_access`, `Url_web_categories`, `Origin`, `Matched_device_posture.Value`, `Matched_device_posture.Metadata`, `Details.Value`, and `Details.Metadata` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Tab_id`, `Signature`, and `Data_target` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `Device_id` and `Os_user_name` raw log fields to `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.   
2025-11-12 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `machine_id` raw log field to `event.idm.read_only_udm.principal.asset.asset_id`.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped `matched_device_posture.machine_model` raw log field to `event.idm.read_only_udm.principal.asset.platform_software.platform_version`.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `details.file_info_details.mime_type` raw log field to `event.idm.read_only_udm.target.file.mime_type`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `details.file_info_details.name` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `details.file_info_details.size_in_bytes` raw log field to `event.idm.read_only_udm.target.file.size`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `verdict_reason` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data_target`, `matched_device_posture.browser_version`, `matched_device_posture.chromium_version`, `matched_device_posture.crowd_strike_zta_info.agent_id`, `matched_device_posture.crowd_strike_zta_info.cid`, `matched_device_posture.crowd_strike_zta_info.score`, `matched_device_posture.gatekeeper_version`, `matched_device_posture.is_gatekeeper_enabled`, `matched_device_posture.os_version` and `matched_device_posture.system_integrity_protection` to `event.idm.read_only_udm.additional.fields`.   
2025-10-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `machineName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `osUserName` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `machineId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `saasApplicationId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.cpu_platform`: Newly mapped `matchedDevicePosture.architecture` raw log field with `event.idm.read_only_udm.principal.asset.hardware.cpu_platform` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `matchedDevicePosture.browser_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `matchedDevicePosture.os_code_name` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform_patch_level`: Newly mapped `matchedDevicePosture.os_version` raw log field with `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `matchedDevicePosture.device_type`, `matchedDevicePosture.disk_encryption`, `matchedDevicePosture.domain`, `matchedDevicePosture.is_default_browser`, `matchedDevicePosture.island_platform` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `matchedDevicePosture.machine_name`, `matchedDevicePosture.os_firewall_enabled`, `matchedDevicePosture.os_screen_lock_enabled`, `matchedDevicePosture.secure_boot`,`countryCode,details.ipa_details.ipa_forwarding_method`,`details.ipa_details.ipa_rule`,`details.navigation_details.is_fail_open_close_active`, `details.navigation_details.is_iframe`, `details.policy_version_details.application_access_policy_version`, `details.policy_version_details.browser_access_policy_version`, `details.policy_version_details.browser_policy_version`, `details.policy_version_details.dlp_policy_version`, `details.policy_version_details.pam_policy_version,windowId,compatibilityMode`,`createdDate`,`syslogConnectorId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `product.enabled`, `product.name`, and `product.signatures_are_up_to_date` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Added a conditional check to map to `event.idm.read_only_udm.metadata.event_type` `FILE_UNCATEGORIZED` if `has_file` and `has_principal_user` is true.   
2025-08-28 |  Enhancement:  
\- Added a gsub to parse proper value.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `art`, `application_access_policy_version`, `sourceDnsDomain`, `av`, `geid`, `policy_version_details.application_access_policy_version`, `policy_version_details.browser_access_policy_version`, `policy_version_details.browser_policy_version`, `policy_version_details.dlp_policy_version`, `policy_version_details.pam_policy_version`, `parent_frame_url` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `aid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `agentZoneURI` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `at` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `ahost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ahost` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `agt` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `agt` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `amac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `deviceZoneURI` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `catdt` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `deviceSeverity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `atz` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.metadata.description: Changed mapping logic for `event.idm.read_only_udm.metadata.description` from using `rename` to a `replace` mutate on the `msg` field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is true, updated to STATUS_UPDATE.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true or `principal_user_present` is true, updated to USER_UNCATEGORIZED.  
\- Added support for CEF formatted logs by including cef_extraction.include and cef_udm_mapping.include for non-JSON formatted messages.   
2025-04-09 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `machine_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `os_platform` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `os_user_name` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `top_level_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `client_event_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `country_code` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tenant_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `tab_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `signature` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `public_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `processed_date` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `matched_user_group` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `frame_url` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `url_web_categories` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `client_sending_date` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.anti_malware_product.name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.anti_malware_product.enabled` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.anti_malware_product.signatures_are_up_to_date` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.anti_malware_product.signatures_last_updated` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.client_certificates.issuer` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.client_certificates.subject` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `matched_device_posture.client_certificates.thumbprint` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.domain.name: Newly mapped `matched_device_posture.domain` raw log field with `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped `matched_device_posture.os_code_name` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Newly mapped `matched_device_posture.machine_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.disk_encryption` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `matched_device_posture.is_virtual_machine` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
-event.idm.read_only_udm.principal.file.full_path,event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `matched_device_posture.processes` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field, and `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `origin` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.confidence_score: Newly mapped `url_web_reputation` raw log field with `event.idm.read_only_udm.security_result.confidence_score` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `is_island_private_access` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `window_id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `compatibility_mode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `event.idm.read_only_udm.network_UNCATEGORIZED` if `has_event.idm.read_only_udm.network`, `has_ event.idm.read_only_udm.principal_user`, and `has_ event.idm.read_only_udm.target_hostname` are true; otherwise, set it to `USER_UNCATEGORIZED` if `has_ event.idm.read_only_udm.principal_user` is true.   
2024-05-20 |  Enhancement:  
\- Initialized `RuleName` to null.  
\- Mapped `userId` to `principal.user.userid`.  
\- Mapped `email` to `principal.user.email_addresses`.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `topLevelUrl` to `network.http.referral_url`.  
\- Mapped `ruleId` to `security_result.rule_id`.  
\- Mapped `ruleName` to `security_result.rule_name`.  
\- Mapped `Verdict` and `verdict` to `security_result.action_details`.  
\- Mapped `sourceIp` and `publicIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `verdictReason` to `security_result.description`.  
\- Mapped `tabId`, `urlWebReputation`, `updatedDate`, `processedDate`, `service`, `id`, `deviceId`, `frameUrl`, `urlWebCategories`, `isIslandPrivateAccess`, `tenantId`, `saasApplicationCategory`, `saasApplicationName`, `machineName`, `details.navigationDetails.isIframe`, `details.navigationDetails.is_iframe`, `navigation_details.is_iframe`, `matchedDevicePosture.domain`, `matchedDevicePosture.workgroup`, and `incognito` to `additional.fields`.   
2023-09-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
