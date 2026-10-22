---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-cmdb-changelog/
title: Change log for SERVICENOW_CMDB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:40.809416+00:00
---

# Change log for SERVICENOW_CMDB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-cmdb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SERVICENOW_CMDB

Date | Changes  
---|---  
2026-08-07 |  Enhancement:  
\- `event.idm.relations.entity.asset.attribute.labels`: Removed mapping of `sys_domain`, `asset_display_value`, `model_id.link`, `device_type`, `discovery_proto_id`, `discovery_proto_type`, `can_switch`, `can_route`, `can_hub`, `can_partitionvlans`, `ports`, `u_internet_internal`, `u_type_physical_virtual`, `u_bau_project`, `u_end_security_vulnerability_eol`, `u_exclude_from_sam`, `comments`, `sys_domain.link`, `cpu_count`, `environment`, `virtual`, `subcategory` from `event.idm.relations.entity.asset.attribute.labels` UDM fields since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.attribute.labels`: Mapped `sys_domain`, `asset_display_value`, `model_id.link`, `device_type`, `discovery_proto_id`, `discovery_proto_type`, `can_switch`, `can_route`, `can_hub`, `can_partitionvlans`, `ports`, `u_internet_internal`, `u_type_physical_virtual`, `u_bau_project`, `u_end_security_vulnerability_eol`, `u_exclude_from_sam`, `comments`, `sys_domain.link`, `cpu_count`, `environment`, `virtual`, `subcategory` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM fields.  
\- `event.idm.relations.entity.labels`: Removed mapping of `sys_domain_path`, `sys_mod_count`, `location`, `location.link`, `attestation_status`, `monitor`, `operational_status`, `skip_sync`, `install_status` from `event.idm.relations.entity.labels` UDM fields since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.attribute.labels`: Mapped `sys_domain_path`, `sys_mod_count`, `location`, `location.link`, `attestation_status`, `monitor`, `operational_status`, `skip_sync`, `install_status` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM fields.  
\- `event.idm.relations.entity.asset.first_discover_time`: Removed mapping of `first_discovered` from `event.idm.relations.entity.asset.first_discover_time` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.first_discover_time`: Mapped `first_discovered` raw log field with `event.idm.entity.entity.asset.first_discover_time` UDM field.  
\- `event.idm.relations.entity.asset.last_discover_time`: Removed mapping of `last_discovered` from `event.idm.relations.entity.asset.last_discover_time` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.last_discover_time`: Mapped `last_discovered` raw log field with `event.idm.entity.entity.asset.last_discover_time` UDM field.  
\- `event.idm.relations.entity.asset.system_last_update_time`: Removed mapping of `sys_updated_on` from `event.idm.relations.entity.asset.system_last_update_time` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.system_last_update_time`: Mapped `sys_updated_on` raw log field with `event.idm.entity.entity.asset.system_last_update_time` UDM field.  
\- `event.idm.relations.entity.asset.category`: Removed mapping of `category` from `event.idm.relations.entity.asset.category` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.category`: Mapped `category` raw log field with `event.idm.entity.entity.asset.category` UDM field.  
\- `event.idm.relations.entity.asset.product_object_id`: Removed mapping of `sys_id` from `event.idm.relations.entity.asset.product_object_id` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.product_object_id`: Mapped `sys_id` raw log field with `event.idm.entity.entity.asset.product_object_id` UDM field.  
\- `event.idm.relations.entity.asset.hostname`: Removed mapping of `name`, `client_name`, `host_name` from `event.idm.relations.entity.asset.hostname` UDM fields since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.hostname`: Mapped `name`, `client_name`, `host_name` raw log fields with `event.idm.entity.entity.asset.hostname` UDM fields.  
\- `event.idm.relations.entity.asset.ip`: Removed mapping of `ip_address` from `event.idm.relations.entity.asset.ip` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.ip`: Mapped `ip_address` raw log field with `event.idm.entity.entity.asset.ip` UDM field.  
\- `event.idm.relations.entity.asset.hardware`: Removed mapping of `hardware` from `event.idm.relations.entity.asset.hardware` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.hardware`: Mapped `hardware` raw log field with `event.idm.entity.entity.asset.hardware` UDM field.  
\- `event.idm.relations.entity.asset.platform_software.platform_version`: Removed mapping of `firmware_version` from `event.idm.relations.entity.asset.platform_software.platform_version` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.platform_software.platform_version`: Mapped `firmware_version` raw log field with `event.idm.entity.entity.asset.platform_software.platform_version` UDM field.  
\- `event.idm.relations.entity.asset.asset_id`: Removed mapping of `asset_tag` from `event.idm.relations.entity.asset.asset_id` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.asset_id`: Mapped `asset_tag` raw log field with `event.idm.entity.entity.asset.asset_id` UDM field.  
\- `event.idm.relations.entity.asset.software`: Removed mapping of `discovery_source` from `event.idm.relations.entity.asset.software` UDM field since the asset details represent the primary entity for IP Switch logs rather than a relational entity.  
\- `event.idm.entity.entity.asset.software`: Mapped `discovery_source` raw log field with `event.idm.entity.entity.asset.software` UDM field.  
\- `event.idm.entity.entity.user.userid`: Removed mapping of `sys_updated_by` from `event.idm.entity.entity.user.userid` UDM field since the user details represent a relational entity for IP Switch logs rather than the primary entity.  
\- `event.idm.relations.entity.user.userid`: Mapped `sys_updated_by` raw log field with `event.idm.relations.entity.user.userid` UDM field.  
\- `event.idm.entity.entity.user.product_object_id`: Removed mapping of `sys_id` from `event.idm.entity.entity.user.product_object_id` UDM field since the user details represent a relational entity for IP Switch logs rather than the primary entity.  
\- `event.idm.relations.entity.user.product_object_id`: Mapped `sys_id` raw log field with `event.idm.relations.entity.user.product_object_id` UDM field.  
\- `event.idm.entity.entity.asset_id`: Mapped `asset` raw log field with `event.idm.entity.entity.asset_id` UDM field.  
\- `event.idm.entity.metadata.entity_type`: Set the value of `event.idm.entity.metadata.entity_type` to ASSET when `sys_class_name` is IP Switch.   
2026-07-23 |  Enhancement:  
\- `event.idm.entity.relations.entity.user.username`: Removed mapping of `host_name` from `event.idm.entity.relations.entity.user.username` UDM field since `host_name` represents `ASSET` entity and not `USER` entity.  
\- `event.idm.entity.relations.entity.asset.hostname`: Mapped `host_name` raw log field with `event.idm.entity.relations.entity.asset.hostname` UDM field.  
\- `event.idm.entity.relations.entity.user.user_display_name`: Newly mapped `owned_by.display_value` raw log field with `event.idm.entity.relations.entity.user.user_display_name` UDM field.  
\- `event.idm.entity.relations.entity.asset.hardware.model`: Newly mapped `model_id.display_value` raw log field with `event.idm.entity.relations.entity.asset.hardware.model` UDM field.  
\- `event.idm.entity.relations.entity.asset.platform_software.platform_version`: Newly mapped `firmware_version` raw log field with `event.idm.entity.relations.entity.asset.platform_software.platform_version` UDM field.  
\- `event.idm.entity.relations.entity.asset.attribute.labels`: Newly mapped `support_group.display_value`, `support_group.link`, `asset.display_value`, `model_id.link`, `device_type`, `discovery_proto_id`, `discovery_proto_type`, `can_switch`, `can_route`, `can_hub`, `can_partitionvlans`, `ports`, `u_internet_internal`, `u_type_physical_virtual`, `u_bau_project`, `u_end_security_vulnerability_eol`, `u_exclude_from_sam`, `comments`, `subcategory`, `firmware_version` raw log fields with `event.idm.entity.relations.entity.asset.attribute.labels` UDM field.  
\- `event.idm.entity.relations.entity_type`: When `host_name` is not empty, updated the value of `event.idm.entity.relations.entity_type` to ASSET.  
\- Added support for new date format to the date match pattern for `first_discovered`, `last_discovered`, `sys_updated_on`, and `sys_created_on` raw log fields.   
2026-06-24 |  Enhancement:  
\- `event.idm.entity.entity.asset.attribute.labels`: Newly mapped `dr_backup_name` ,`dv_u_device_role` ,`u_decomissioned` ,`warranty_expiration` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM field.  
\- `event.idm.entity.metadata.entity_type`: Added support for `event.idm.entity.metadata.entity_type` to be mapped to `ASSET` when both hostname and entity details are present for additional `sys_class_name` raw log field values.   
2026-06-05 |  Enhancement:  
\- `event.idm.entity.metadata.creation_timestamp`: Newly mapped `sys_created_on` raw log field with `event.idm.entity.metadata.creation_timestamp` UDM field.  
\- `event.idm.entity.relations.entity.asset.asset_id`: Newly mapped `asset` raw log field with `event.idm.entity.relations.entity.asset.asset_id` UDM field.  
\- `event.idm.entity.relations.entity.asset.first_seen_time`: Newly mapped `install_date` raw log field with `event.idm.entity.relations.entity.asset.first_seen_time` UDM field.  
\- `event.idm.entity.entity.asset.attribute.labels`: Newly mapped `chassis_type`, `vendor.value`, `vendor.link`, `os_address_width`, `invoice_number`, `assigned`, `os_domain`, `can_print`, `cd_rom`, `unverified`, `asset.value`, `owned_by.link`, `assigned_to.link`, `managed_by.link`, `asset.link`, `hardware_substatus`, `hardware_status`, `sys_domain.value`, `processor_name.value`, `processor_name.link`, `cpu_core_thread`, `cpu_manufacturer.value`, `cpu_manufacturer.link`, `department.value`, `default_gateway`, `po_number`, `internet_facing`, `sys_class_path`, `u_technical_hold`, `cost_cc`, `order_date`, `attested`, `fault_count`, `sys_created_by` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM field.  
\- `event.idm.entity.relations.entity.asset.attribute.labels`: Newly mapped `dv_operational_status`, `u_glp`, `u_gmp`, `manufacturer_company_name`, `u_other_gxp`, `u_gcp`, `managed_by_group_name`, `managed_by_User_Name`, `cpu_count`, `environment`, `owned_by_User_Name`, `region, `site`, `support_group_name`, `u_backup_method`, `u_backup_required`, `virtual` raw log fields with `event.idm.entity.relations.entity.asset.attribute.labels` UDM field.  
\- `event.idm.entity.relations.entity.asset.hostname`: Removed mapping of `host_name`, `name`, `client_name` from `event.idm.entity.relations.entity.asset.hostname` UDM field to change the entity type from USER to ASSET.  
\- `event.idm.entity.entity.asset.hostname`: Mapped `host_name`, `name`, `client_name` raw log field to `event.idm.entity.entity.asset.hostname` UDM field.  
\- `event.idm.entity.relations.entity.asset.ip`: Removed mapping of `ip_address` from `event.idm.entity.relations.entity.asset.ip` UDM field to change the entity type from USER to ASSET.  
\- `event.idm.entity.entity.asset.ip`: Mapped `ip_address` raw log field to `event.idm.entity.entity.asset.ip` UDM field.  
\- `event.idm.entity.relations.entity.asset.hostname`: Removed mapping of `host_name` from `event.idm.entity.relations.entity.asset.hostname` UDM field to change the entity type from USER to ASSET.  
\- `event.idm.entity.relations.entity.user.username`: Mapped `host_name` raw log field to `event.idm.entity.relations.entity.user.username` UDM field.  
\- `event.idm.entity.relations.entity.asset.hardware.model`: Changed mapping for `event.idm.entity.relations.entity.asset.hardware.model` from `model_id.value` to `dv_model_id` UDM field.  
\- Updated `subcategory` check to include `Computer` for mapping to `LAPTOP`.  
\- `event.idm.read_only_udm.entity.user.userid`: Newly mapped `sys_id` raw log field with `event.idm.read_only_udm.entity.user.userid` UDM field when `userid` field is not present.   
2025-03-27 |  Enhancement:  
\- `event.idm.entity.entity.user.userid`: Newly mapped `owned_by.value` raw log field with `entity.user.userid` UDM field.  
\- `event.idm.entity.entity.user.product_object_id`: Newly mapped `owned_by.value` raw log field with `entity.user.product_object_id` UDM field.  
\- `event.idm.entity.entity.user.userid`: Newly mapped `assigned_to.value` raw log field with `entity.user.product_object_id` UDM field.  
\- `event.idm.entity.entity.user.product_object_id`: Newly mapped `assigned_to.value` raw log field with `entity.user.product_object_id` UDM field.  
\- When `owned_by.value` or `assigned_to.value` is available, then mapped `event.idm.entity.entity.metadata.entity_type` to `USER`.  
\- When category is `End User Asset`, `Hardware`, `Physical Server`, `Printer`, `Workstation` or `Storage` then mapped `event.idm.entity.relation.entity_type` as `ASSET`.  
\- When `manufacturer` data is available then mapped `event.idm.entity.relation.entity_type` as `ASSET`.  
\- Dropped the events when `event.idm.entity.metadata.entity_type` and `event.idm.read_only_udm.metadata.event_type` are not present.   
2025-03-10 |  Enhancement:  
\- Changed mappings of fields from `event.idm.entity.entity` to `event.idm.entity.relations`.  
\- Changed mappings of fields from `event.idm.entity.relations` to `event.idm.entity.entity`.  
\- Changed `metadata.entity_type` from `ASSET` to `USER`.   
2025-01-30 |  Enhancement:  
\- Mapped `calendar_integration`, `u_ldap_source`, `u_show_popup`, `source`, `building`, `web_service_access_only`, `notification`, `enable_multifactor_authn`, `sso_source`, `sys_domain.display_value`, `sys_domain.link`, `u_itil_license_type`, and `u_assets_validated` to `entity.entity.asset.attribute.labels`  
\- Mapped `last_login_time` to `entity.relation.entity.user.last_login_time`.  
\- Mapped `x_bmgr_support_ent_bomgar_username`, `vip`, `zip`, `time_format`, `active`, `gender`, `failed_attempts`, `federated_id`, `internal_integration_user`, `u_business_line`, `department.link`, `introduction`, `preferred_language`, `manager.link`, `photo`, `avatar`, `time_zone`, `schedule`, and `correlation_id` to `entity.relation.entity.user.attribute.labels`.  
\- Mapped `street` to `entity.relation.entity.user.personal_address.name`.  
\- Mapped `department.display_value` to `entity.relation.entity.user.department`.  
\- Mapped `u_office` to `entity.relation.entity.user.company_name`.  
\- Mapped `title` to `entity.relation.entity.user.title`.  
\- Mapped `first_name` to `entity.relation.entity.user.first_name`.  
\- Mapped `last_name` to `entity.relation.entity.user.last_name`.  
\- Mapped `middle_name` to `entity.relation.entity.user.middle_name`.  
\- Mapped `manager.display_value` to `entity.relation.entity.user.managers.user_display_name`.  
\- Mapped `sys_domain_path`, `transaction_log`, `cost_center`, `sys_mod_count`, and `sys_tags` to `entity.entity.labels`.  
\- Mapped `employee_number`, `phone`, `home_phone`, and `mobile_phone` to `entity.relation.entity.user.phone_numbers`.  
\- Mapped `city` to `entity.relation.entity.user.personal_address.city`.  
\- Mapped `state` to `entity.relation.entity.user.personal_address.state`.   
2025-01-16 |  Enhancement:  
\- Mapped `country` to `entity.location.country_or_region`.  
\- Mapped `u_site_code` to `entity.location.city`.  
\- Mapped `u_region` to `entity_labels`.  
\- Mapped `location.display_value` to `entity.labels`.  
\- Mapped `location.link` to `entity.labels`.  
\- Mapped `email` to `_relation.entity.user.email_addresses`.   
2024-10-16 |  Enhancement:  
\- Mapped `sys_id` to `entity.asset.product_object_id`.   
2024-07-02 |  Enhancement:  
\- Mapped `u_sima_bs_activation_date`, `attestation_status`, `u_oracle_asm_lun_size`, `u_app_resource_jndi_name`, `is_encrypted`, `monitor`, `operational_status`, `u_updated_ci`, `u_cluster_node`, `firewall_status`, `skip_sync`, `u_excluded`, `u_data_classification`, `u_sla_report`, `u_restriction`, `u_rack_slot`, `u_account_aztech_oe.link`, `u_account_aztech_oedisplay_value`, `u_organisational_entity.link`, `u_organisational_entity.display_value`, `assignment_group.link`, `assignment_group.display_value`, `cost_center.link`, `cost_center.display_value`, `u_service_instance`, `u_local_oe_cost_center`, `managed_by`, `u_mode_of_operation`, `install_status`, and `u_provider_tag` to `entity.labels`.  
\- Mapped `u_build_user` to `entity.user.email_addresses`.   
2024-01-23 |  Bug-Fix-  
\- Changed the entire mapping for logs which are of `ASSET` type.  
\- Mapped `metadata.entity_type` to `ASSET` and `relations.entity_type` to `USER`.  
\- Changed mapping of `label_ci_link` from `entity.entity.user.attribute.labels` to `relation.entity.user.attribute.labels`.  
\- Changed mapping of `label_value` from `entity.entity.user.attribute.labels` to `relation.entity.user.attribute.labels`.  
\- Changed mapping of `label_sys_class_name` from `entity.entity.user.attribute.labels` to `relation.entity.user.attribute.labels`.  
\- Changed mapping of `first_discovered` from `asset_entity.asset.last_discover_time` to `entity.entity.asset.last_discover_time`.  
\- Changed mapping of `last_discovered` from `asset_entity.asset.first_discover_time` to `entity.entity.asset.first_discover_time`.  
\- Changed mapping of `sys_updated_on` from `asset_entity.asset.system_last_update_time` to `entity.entity.asset.system_last_update_time`".  
\- Changed mapping of `category` from `asset_entity.asset.category` to `entity.entity.asset.category`.  
\- Changed mapping of `u_sub_status` from `asset_entity.asset.deployment_status` to "entity.entity.asset.deployment_status.  
\- Changed mapping of `subcategory` from `asset_entity.asset.type` to `entity.entity.asset.type`.  
\- Changed mapping of `name` from `asset_entity.asset.hostname` to `entity.entity.asset.hostname`.  
\- Changed mapping of `_lan1` and `_lan2` and `_ip` from `asset_entity.asset.ip` to `entity.entity.asset.ip`.  
\- Changed mapping of `_mac` from `asset_entity.asset.mac` to `entity.entity.asset.mac`.  
\- Changed mapping of `dns_domain` from `asset_entity.asset.network_domain` to `entity.entity.asset.network_domain`.  
\- Changed mapping of `os` from `asset_entity.asset.platform_software.platform` to `entity.entity.asset.platform_software.platform`.  
\- Changed mapping of `os_version` and `os_service_pack` from `asset_entity.asset.platform_software.platform_patch_level` to `entity.entity.asset.platform_software.platform_patch_level`.  
\- Changed mapping of `asset_tag` from `asset_entity.asset.asset_id` to `entity.entity.asset.asset_id`.  
\- Changed mapping of `WMI_Asset_ID` from `asset_entity.asset.asset_id` to `entity.entity.asset.asset_id`.  
\- Changed mapping of `_asset_software` and `software` from `asset_entity.asset.software` to `entity.entity.asset.software`.  
\- Changed mapping of `client_name` from `asset_entity.asset.hostname` to `entity.entity.asset.hostname`.  
\- Changed mapping of `client_id` from `entity.entity.user.userid` to `relation.entity.user.userid`.  
\- Changed mapping of `ips` from `asset_entity.asset.ip` to `entity.entity.asset.ip`.  
\- Changed mapping of `hardware` from `asset_entity.asset.hardware` to `entity.entity.asset.hardware`.  
\- Changed mapping of `DNS_Name` from `asset_entity.asset.network_domain` to `entity.entity.asset.network_domain`.  
\- Changed mapping of `sys_id` from `entity.entity.user.product_object_id` to `relation.entity.user.product_object_id`.  
\- Changed mapping of `WMI_Service_Tag` from `entity.entity.user.product_object_id` to `relation.entity.user.product_object_id`.  
\- Changed mapping of `u_owner_name_computer` from `entity.entity.user.user_display_name` to `relation.entity.user.user_display_name`.  
\- Changed mapping of `roles` from `entity.entity.user.attribute.roles` to `relation.entity.user.attribute.roles`.   
2023-05-31 |  Enhancement-  
\- Removed unwanted declarations.  
\- Wrote merge blocks separately to avoid conflict.   
2023-05-22 |  Enhancement-Added mappings for the following fields-  
\- Mapped `number` to `security_result.detection_fields`.  
\- Mapped `cmdb_ci` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `host_name` to `event.idm.entity.entity.asset.hostname`.  
\- Mapped `short_description` to `security_result.description`.  
\- Mapped `description` to `security_result.action_details`.  
\- Mapped `sys_class_name` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `u_aam_category` to `security_result.category_details`.  
\- Mapped `u_aam_subcategory` to `security_result.detection_fields`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `user_role` from `entity.user.role_name` to `entity.user.attribute.roles`.   
2022-06-10 |  Enhancement- The newly ingested logs have been parsed and mapped to the following fields:  
\- `WMI_Service_Tag` mapped to `entity.user.product_object_id`.  
\- `User_Name` mapped to `entity.user.user_display_name`.  
\- `user_role` mapped to `entity.user.role_name`.  
\- `OperatingSystemRole` mapped to `entity.asset.type`.  
\- `MAC_Addresses` mapped to `entity.asset.mac`.  
\- `OS` mapped to `entity.asset.platform_software.platform`.  
\- `WMI_Asset_ID` mapped to `entity.asset.asset_id`.  
\- `WindowsOperatingSystem` mapped to `entity.asset.software`.  
\- `SerialNumber` mapped to `entity.asset.product_object_id`.  
\- `client_name` mapped to `entity.asset.hostnam`.  
\- `client_id` mapped to `entity.user.userid`.  
\- `CIDR_Subnet_String` mapped to `entity.asset.ip`.  
\- `Computer_Serial_Number` mapped to `entity.asset.hardware.serial_number`.  
\- `Computer_Serial_Number` mapped to `entity.asset.hardware.manufacturer`.  
\- `Computer_Serial_Number` mapped to `entity.asset.hardware.model`.  
\- `DNS_Name` mapped to `entity.asset.network_domain`.   
2022-04-13 |  Enhancement-Parsed the CEF format logs having different message format.  
Mapped the following additional fields: `event`, `event_ts`, `instance`, `userid`, `source_ip`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
