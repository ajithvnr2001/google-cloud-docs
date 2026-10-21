---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-sql-context/
title: Collect Cloud SQL context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:27.650856+00:00
---

# Collect Cloud SQL context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-sql-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloud SQL context logs

This document describes how fields of Cloud SQL context logs map to Google Security Operations Unified Data Model (UDM) fields.

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `GCP_SQL_CONTEXT` ingestion label.

For information about other context parsers that Google SecOps supports, see [Google SecOps context parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers).

## Supported Cloud SQL log formats

The Cloud SQL parser supports logs in JSON format.

## Supported Cloud SQL sample logs

  * JSON:
        
        {
          "name": "//cloudsql.googleapis.com/projects/cloudsql-experiment-target/instances/target-exfil-mysql/backupRuns/1684933200000",
          "assetType": "dummy.googleapis.com/BackupRun",
          "resource": {
            "version": "v1beta4",
            "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/sqladmin/v1beta4/rest",
            "discoveryName": "BackupRun",
            "parent": "//cloudsql.googleapis.com/projects/cloudsql-experiment-target/instances/target-exfil-mysql",
            "data": {
              "backupKind": "SNAPSHOT",
              "endTime": "2023-05-24T13:14:54.196Z",
              "enqueuedTime": "2023-05-24T13:13:32.856Z",
              "id": "1684933200000",
              "instance": "target-exfil-mysql",
              "kind": "sql#backupRun",
              "location": "us",
              "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/cloudsql-experiment-target/instances/target-exfil-mysql/backupRuns/1684933200000",
              "startTime": "2023-05-24T13:13:32.913Z",
              "status": "SUCCESSFUL",
              "type": "AUTOMATED",
              "windowStartTime": "2023-05-24T13:00:00Z"
            }
          },
          "ancestors": [
            "projects/687904117202",
            "organizations/299419016487"
          ]
        }
        




## Field mapping reference

This section explains how the Google SecOps parser maps fields of Cloud SQL context logs to Google SecOps Unified Data Model (UDM) fields. 

Log field | UDM mapping | Logic  
---|---|---  
`ancestors` | `relations.entity.resource_ancestors.name` | If the `resource.parent` log field value is not matched with the value of `ancestors` log field, then the `ancestors` log field is mapped to the `relations.entity.resource_ancestors.name` UDM field.  
`assetType` | `entity.resource.resource_subtype` |   
`name` | `entity.resource.name` |   
`resource.data.availableMaintenanceVersions` | `entity.resource.attribute.labels[available_maintenance_versions]` |   
`resource.data.backendType` | `entity.resource.attribute.labels[backend_type]` |   
`resource.data.backupKind` | `entity.resource.attribute.labels[backup_kind]` |   
`resource.data.connectionName` | `entity.resource.attribute.labels[connection_name]` |   
`resource.data.createTime` | `entity.resource.attribute.creation_time` |   
`resource.data.currentDiskSize` | `entity.resource.attribute.labels[current_disk_size]` |   
`resource.data.databaseInstalledVersion` | `entity.resource.attribute.labels[database_installed_version]` |   
`resource.data.databaseVersion` | `entity.resource.attribute.labels[database_version]` |   
`resource.data.description` | `metadata.description` |   
`resource.data.diskEncryptionConfiguration.kind` | `entity.resource.attribute.labels[disk_encryption_configuration_kind]` |   
`resource.data.diskEncryptionConfiguration.kmsKeyName` | `entity.resource.attribute.labels[disk_encryption_configuration_kms_key_name]` |   
`resource.data.diskEncryptionStatus.kind` | `entity.resource.attribute.labels[disk_encryption_status_kind]` |   
`resource.data.diskEncryptionStatus.kmsKeyVersionName` | `entity.resource.attribute.labels[disk_encryption_configuration_kms_key_version_name` |   
`resource.data.endTime` | `entity.resource.attribute.labels[end_time]` |   
`resource.data.enqueuedTime` | `metadata.creation_timestamp` |   
`resource.data.error.code` | `entity.resource.attribute.labels[error_code]` |   
`resource.data.error.kind` | `entity.resource.attribute.labels[error_kind]` |   
`resource.data.error.message` | `entity.resource.attribute.labels[error_message]` |   
`resource.data.etag` | `entity.resource.attribute.labels[etag]` |   
`resource.data.failoverReplica.available` | `entity.resource.attribute.labels[failover_replica_available]` |   
`resource.data.failoverReplica.name` | `entity.resource.attribute.labels[failover_replica_name]` |   
`resource.data.gceZone` | `entity.resource.attribute.cloud.availability_zone` |   
`resource.data.id` | `metadata.product_entity_id` |   
`resource.data.instance` | `entity.resource.attribute.labels[instance]` |   
`resource.data.instanceType` | `entity.resource.attribute.labels[instance_type]` |   
`resource.data.ipAddresses.ipAddress` | `entity.ip` |   
`resource.data.ipAddresses.timeToRetire` | `entity.labels[ip_addresses_time_to_retire]` |   
`resource.data.ipAddresses.type` | `entity.labels[ip_addresses_type]` |   
`resource.data.ipv6Address` | `entity.ip` |   
`resource.data.kind` | `entity.resource.attribute.labels[kind]` |   
`resource.data.location` | `entity.location.name` |   
`resource.data.maintenanceVersion` | `entity.resource.attribute.labels[maintenance_version]` |   
`resource.data.masterInstanceName` | `entity.resource.attribute.labels[master_instance_name]` |   
`resource.data.maxDiskSize` | `entity.resource.attribute.labels[max_disk_size]` |   
`resource.data.name` | `entity.resource.attribute.labels[resource_name]` |   
`resource.data.onPremisesConfiguration.caCertificate` | `entity.resource.attribute.labels[on_pem_conf_ca_certificate]` |   
`resource.data.onPremisesConfiguration.clientCertificate` | `entity.resource.attribute.labels[on_pem_conf_client_certificate]` |   
`resource.data.onPremisesConfiguration.clientKey` | `entity.resource.attribute.labels[on_pem_conf_client_key]` |   
`resource.data.onPremisesConfiguration.dumpFilePath` | `entity.resource.attribute.labels[on_pem_conf_dump_file_path]` |   
`resource.data.onPremisesConfiguration.hostPort` | `entity.resource.attribute.labels[on_pem_conf_host_port]` |   
`resource.data.onPremisesConfiguration.kind` | `entity.resource.attribute.labels[on_pem_conf_kind]` |   
`resource.data.onPremisesConfiguration.password` | `entity.resource.attribute.labels[on_pem_conf_password]` |   
`resource.data.onPremisesConfiguration.sourceInstance.name` | `relations.entity.resource.name` |   
`resource.data.onPremisesConfiguration.sourceInstance.project` | `relations.entity.resource.product_object_id` |   
`resource.data.onPremisesConfiguration.sourceInstance.region` | `relations.entity.location.country_or_region` |   
`resource.data.onPremisesConfiguration.username` | `entity.resource.attribute.labels[on_pem_conf_username]` |   
`resource.data.outOfDiskReport.sqlMinRecommendedIncreaseSizeGb` | `entity.resource.attribute.labels[out_of_disk_report_sql_min_recommended_increase_size_gb]` |   
`resource.data.outOfDiskReport.sqlOutOfDiskState` | `entity.resource.attribute.labels[out_of_disk_report_sql_out_of_disk_state]` |   
`resource.data.project` | `entity.resource.product_object_id` |   
`resource.data.region` | `entity.location.country_or_region` |   
`resource.data.replicaConfiguration.failoverTarget` | `entity.resource.attribute.labels[replica_conf_fail_over_target]` |   
`resource.data.replicaConfiguration.kind` | `entity.resource.attribute.labels[replica_conf_kind]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.caCertificate` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_ca_certificate]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.clientCertificate` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_client_certificate]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.clientKey` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_client_key]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.connectRetryInterval` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_connect_retry_interval]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.dumpFilePath` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_dump_file_path]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.kind` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_kind]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.masterHeartbeatPeriod` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_master_heart_beat_period]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.password` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_password]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.sslCipher` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_ssl_cipher]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.username` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_username]` |   
`resource.data.replicaConfiguration.mysqlReplicaConfiguration.verifyServerCertificate` | `entity.resource.attribute.labels[replica_conf_my_sql_replica_conf_verify_server_certificate]` |   
`resource.data.replicaNames` | `entity.resource.attribute.labels[replica_names]` |   
`resource.data.rootPassword` | `entity.resource.attribute.labels[root_password]` |   
`resource.data.satisfiesPzs` | `entity.resource.attribute.labels[satisfies_pzs]` |   
`resource.data.scheduledMaintenance.canDefer` | `entity.resource.attribute.labels[schedule_maintenance_can_defer]` |   
`resource.data.scheduledMaintenance.canReschedule` | `entity.resource.attribute.labels[schedule_maintenance_can_reschedule]` |   
`resource.data.scheduledMaintenance.scheduleDeadlineTime` | `entity.resource.attribute.labels[schedule_maintenance_deadline_time]` |   
`resource.data.scheduledMaintenance.startTime` | `entity.resource.attribute.labels[schedule_maintenance_start_time]` |   
`resource.data.secondaryGceZone` | `entity.resource.attribute.labels[secondary_gce_zone]` |   
`resource.data.selfLink` | `entity.url` |   
`resource.data.serverCaCert.cert` | `entity.resource.attribute.labels[server_ca_cert_cert]` |   
`resource.data.serverCaCert.certSerialNumber` | `entity.network.tls.server.certificate.serial` |   
`resource.data.serverCaCert.commonName` | `entity.network.tls.server.certificate.subject` |   
`resource.data.serverCaCert.createTime` | `entity.network.tls.server.certificate.not_before` |   
`resource.data.serverCaCert.expirationTime` | `entity.network.tls.server.certificate.not_after` |   
`resource.data.serverCaCert.instance` | `entity.resource.attribute.labels[server_ca_cert_instance]` |   
`resource.data.serverCaCert.kind` | `entity.resource.attribute.labels[server_ca_cert_kind]` |   
`resource.data.serverCaCert.selfLink` | `entity.resource.attribute.labels[server_ca_cert_self_link]` |   
`resource.data.serverCaCert.sha1Fingerprint` | `entity.network.tls.server.certificate.sha1` |   
`resource.data.serviceAccountEmailAddress` | `entity.user.email_addresses` |   
`resource.data.settings.activationPolicy` | `entity.resource.attribute.labels[settings_activation_policy]` |   
`resource.data.settings.activeDirectoryConfig.domain` | `entity.resource.attribute.labels[settings_active_directory_config_domain]` |   
`resource.data.settings.activeDirectoryConfig.kind` | `entity.resource.attribute.labels[settings_active_directory_config_kind]` |   
`resource.data.settings.authorizedGaeApplications` | `entity.resource.attribute.labels[settings_authorized_gae_applications]` |   
`resource.data.settings.availabilityType` | `entity.resource.attribute.labels[settings_availability_type]` |   
`resource.data.settings.backupConfiguration.backupRetentionSettings.retainedBackups` | `entity.resource.attribute.labels[settings_backup_conf_backup_retention_settings_retained_backups]` |   
`resource.data.settings.backupConfiguration.backupRetentionSettings.retentionUnit` | `entity.resource.attribute.labels[settings_backup_conf_backup_retention_settings_retention_unit]` |   
`resource.data.settings.backupConfiguration.binaryLogEnabled` | `entity.resource.attribute.labels[settings_backup_conf_binary_log_enabled]` |   
`resource.data.settings.backupConfiguration.enabled` | `entity.resource.attribute.labels[settings_backup_conf_enabled]` |   
`resource.data.settings.backupConfiguration.kind` | `entity.resource.attribute.labels[settings_backup_conf_kind]` |   
`resource.data.settings.backupConfiguration.location` | `entity.resource.attribute.labels[settings_backup_conf_location]` |   
`resource.data.settings.backupConfiguration.pointInTimeRecoveryEnabled` | `entity.resource.attribute.labels[settings_backup_conf_point_in_time_recovery_enabled]` |   
`resource.data.settings.backupConfiguration.replicationLogArchivingEnabled` | `entity.resource.attribute.labels[settings_backup_conf_replication_log_archiving_enabled]` |   
`resource.data.settings.backupConfiguration.startTime` | `entity.resource.attribute.labels[settings_backup_conf_start_time]` |   
`resource.data.settings.backupConfiguration.transactionLogRetentionDays` | `entity.resource.attribute.labels[settings_backup_conf_transaction_log_retention_days]` |   
`resource.data.settings.collation` | `entity.resource.attribute.labels[settings_collation]` |   
`resource.data.settings.connectorEnforcement` | `entity.resource.attribute.labels[settings_connector_enforcement]` |   
`resource.data.settings.crashSafeReplicationEnabled` | `entity.resource.attribute.labels[settings_crash_safe_replication_enabled]` |   
`resource.data.settings.databaseFlags.name` | `entity.resource.attribute.labels[settings_database_flags_name]` |   
`resource.data.settings.databaseFlags.value` | `entity.resource.attribute.labels[settings_database_flags_value]` |   
`resource.data.settings.databaseReplicationEnabled` | `entity.resource.attribute.labels[settings_database_replication_enabled]` |   
`resource.data.settings.dataDiskSizeGb` | `entity.resource.attribute.labels[settings_data_disk_size_gb]` |   
`resource.data.settings.dataDiskType` | `entity.resource.attribute.labels[settings_data_disk_type]` |   
`resource.data.settings.deletionProtectionEnabled` | `entity.resource.attribute.labels[settings_deletion_protection_enabled]` |   
`resource.data.settings.denyMaintenancePeriods.endDate` | `entity.resource.attribute.labels[settings_deny_maintenance_periods_end_date]` |   
`resource.data.settings.denyMaintenancePeriods.startDate` | `entity.resource.attribute.labels[settings_deny_maintenance_periods_start_date]` |   
`resource.data.settings.denyMaintenancePeriods.time` | `entity.resource.attribute.labels[settings_deny_maintenance_periods_time]` |   
`resource.data.settings.insightsConfig.queryInsightsEnabled` | `entity.resource.attribute.labels[settings_insights_config_query_insights_enabled]` |   
`resource.data.settings.insightsConfig.queryPlansPerMinute` | `entity.resource.attribute.labels[settings_insights_config_query_plans_per_minute]` |   
`resource.data.settings.insightsConfig.queryStringLength` | `entity.resource.attribute.labels[settings_insights_config_query_string_length]` |   
`resource.data.settings.insightsConfig.recordApplicationTags` | `entity.resource.attribute.labels[settings_insights_config_record_application_tags]` |   
`resource.data.settings.insightsConfig.recordClientAddress` | `entity.resource.attribute.labels[settings_insights_config_record_client_address]` |   
`resource.data.settings.ipConfiguration.allocatedIpRange` | `entity.resource.attribute.labels[settings_ip_configuration_allocated_ip_range]` |   
`resource.data.settings.ipConfiguration.authorizedNetworks.expirationTime` | `entity.resource.attribute.labels[settings_ip_configuration_authorized_networks_expiration_time]` |   
`resource.data.settings.ipConfiguration.authorizedNetworks.kind` | `entity.resource.attribute.labels[settings_ip_configuration_authorized_networks_kind]` |   
`resource.data.settings.ipConfiguration.authorizedNetworks.name` | `entity.resource.attribute.labels[settings_ip_configuration_authorized_networks_name]` |   
`resource.data.settings.ipConfiguration.authorizedNetworks.value` | `entity.resource.attribute.labels[settings_ip_configuration_authorized_networks_value]` |   
`resource.data.settings.ipConfiguration.ipv4Enabled` | `entity.resource.attribute.labels[settings_ip_configuration_ipv4_enabled]` |   
`resource.data.settings.ipConfiguration.privateNetwork` | `entity.resource.attribute.labels[settings_ip_configuration_private_network]` |   
`resource.data.settings.ipConfiguration.requireSsl` | `entity.resource.attribute.labels[settings_ip_configuration_require_ssl]` |   
`resource.data.settings.kind` | `entity.resource.attribute.labels[settings_kind]` |   
`resource.data.settings.locationPreference.followGaeApplication` | `entity.resource.attribute.labels[settings_location_preference_follow_gae_application]` |   
`resource.data.settings.locationPreference.kind` | `entity.resource.attribute.labels[settings_location_preference_kind]` |   
`resource.data.settings.locationPreference.secondaryZone` | `entity.resource.attribute.labels[settings_location_preference_secondary_zone]` |   
`resource.data.settings.locationPreference.zone` | `entity.resource.attribute.labels[settings_location_preference_zone]` |   
`resource.data.settings.maintenanceWindow.day` | `entity.resource.attribute.labels[settings_maintenance_window_day]` |   
`resource.data.settings.maintenanceWindow.hour` | `entity.resource.attribute.labels[settings_maintenance_window_hour]` |   
`resource.data.settings.maintenanceWindow.kind` | `entity.resource.attribute.labels[settings_maintenance_window_kind]` |   
`resource.data.settings.maintenanceWindow.updateTrack` | `entity.resource.attribute.labels[settings_maintenance_window_update_track]` |   
`resource.data.settings.passwordValidationPolicy.complexity` | `entity.resource.attribute.labels[settings_password_validation_policy_complexity]` |   
`resource.data.settings.passwordValidationPolicy.disallowUsernameSubstring` | `entity.resource.attribute.labels[settings_password_validation_policy_disallow_username_substring]` |   
`resource.data.settings.passwordValidationPolicy.enablePasswordPolicy` | `entity.resource.attribute.labels[settings_password_validation_policy_enable_password_policy]` |   
`resource.data.settings.passwordValidationPolicy.minLength` | `entity.resource.attribute.labels[settings_password_validation_policy_min_length]` |   
`resource.data.settings.passwordValidationPolicy.passwordChangeInterval` | `entity.resource.attribute.labels[settings_password_validation_policy_password_change_interval]` |   
`resource.data.settings.passwordValidationPolicy.reuseInterval` | `entity.resource.attribute.labels[settings_password_validation_policy_reuse_interval]` |   
`resource.data.settings.pricingPlan` | `entity.resource.attribute.labels[settings_pricing_plan]` |   
`resource.data.settings.replicationType` | `entity.resource.attribute.labels[settings_replication_type]` |   
`resource.data.settings.settingsVersion` | `entity.resource.attribute.labels[settings_version]` |   
`resource.data.settings.sqlServerAuditConfig.bucket` | `entity.resource.attribute.labels[settings_sql_server_audit_config_bucket]` |   
`resource.data.settings.sqlServerAuditConfig.kind` | `entity.resource.attribute.labels[settings_sql_server_audit_config_kind]` |   
`resource.data.settings.sqlServerAuditConfig.retentionInterval` | `entity.resource.attribute.labels[settings_sql_server_audit_config_retention_interval]` |   
`resource.data.settings.sqlServerAuditConfig.uploadInterval` | `entity.resource.attribute.labels[settings_sql_server_audit_config_upload_interval]` |   
`resource.data.settings.storageAutoResize` | `entity.resource.attribute.labels[storage_auto_resize]` |   
`resource.data.settings.storageAutoResizeLimit` | `entity.resource.attribute.labels[storage_auto_resize_limit]` |   
`resource.data.settings.tier` | `entity.resource.attribute.labels[tier]` |   
`resource.data.settings.timeZone` | `entity.resource.attribute.labels[time_zone]` |   
`resource.data.settings.userLabels` | `entity.resource.attribute.labels[user_labels]` |   
`resource.data.startTime` | `entity.resource.attribute.labels[start_time]` |   
`resource.data.state` | `entity.resource.attribute.labels[state]` |   
`resource.data.status` | `entity.resource.attribute.labels[status]` |   
`resource.data.suspensionReason` | `entity.resource.attribute.labels[suspension_reason]` |   
`resource.data.timeZone` | `entity.resource.attribute.labels[time_zone]` |   
`resource.data.type` | `entity.resource.attribute.labels[type]` |   
`resource.data.windowStartTime` | `entity.resource.attribute.labels[window_start_time]` |   
`resource.discoveryDocumentUri` | `entity.resource.attribute.labels[discovery_document]` |   
`resource.discoveryName` | `entity.resource.attribute.labels[discovery_name]` |   
`resource.parent, ancestors[]` | `relations.entity.resource.name` | If the `resource.parent` log field value is empty, then the `ancestors.0` log field is mapped to the `relations.entity.resource.name` UDM field.  
`resource.version` | `metadata.product_version` |   
`` | `entity.resource.resource_type` | The `entity.resource.resource_type` UDM field is set to `DATABASE`.  
`` | `metadata.entity_type` | If the `assetType` log field value matches the regular expression pattern `(BackupRun or instances)`, then the `metadata.entity_type` UDM field is set to `RESOURCE`.  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `GCP SQL`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Google Cloud Platform`.  
`` | `relations.entity_type` | If the `resource.data.onPremisesConfiguration.sourceInstance.name` log field value is _not_ empty, then the `relations.entity_type` UDM field is set to `RESOURCE`.  
`` | `relations.relationship` | If the `resource.data.onPremisesConfiguration.sourceInstance.name`,`resource.data.onPremisesConfiguration.sourceInstance.region`, or `resource.data.onPremisesConfiguration.sourceInstance.project` value is _not_ empty, then the `relations.entity.relationship` UDM field is set to `MEMBER`.  
  
If the `ancestor` log field value matches the regular expression pattern `organizations` or the `ancestor` log field value matches the regular expression pattern `folders`, then the `relations.relationship` UDM field is set to `MEMBER`.  
`` | `relations.entity.resource_ancestors.resource_subtype` | If the `ancestors` log field value matches the regular expression pattern `organizations`, then the `relations.entity.resource_ancestors.resource_subtype` UDM field is set to `organizations`.  
  
Else, if the `ancestors` log field value matches the regular expression pattern `folders`, then the `relations.entity.resource_ancestors.resource_subtype` UDM field is set to `folders`.  
`` | `relations.entity.resource_ancestors.resource_type` | The `relations.entity.resource_ancestors.resource_type` UDM field is set to `CLOUD_ORGANIZATION`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
