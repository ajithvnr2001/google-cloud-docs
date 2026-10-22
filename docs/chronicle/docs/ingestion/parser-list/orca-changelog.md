---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/orca-changelog/
title: Change log for ORCA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:25.165026+00:00
---

# Change log for ORCA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/orca-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ORCA

Date | Changes  
---|---  
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `data.asset_name` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields, as it contains principal hostname related data.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `data.asset_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `data.alert_labels` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `data.alert_labels` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.findings.evidences.events` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-24 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.findings.cve.fixable`, `data.findings.cve.exploitable`, `data.findings.cve.cvss_source_link`, `data.findings.cve.cvss_source`, `data.remediation_cli`, `data.findings.anomaly_context.past_baseline_values`, `data.findings.anomaly_context.anomaly_values`, `data.findings.anomaly_context.anomaly_in_field`, `data.findings.Path`, `data.findings.ConsoleUrlLink`, `data.asset_tags.created_at`, `data.asset_tags.iam_user_name`, `data.asset_tags.environment_id`, `data.custom_tags.360_brand_guardian`, `data.custom_tags.appgate_orca_contact`, `data.findings.SSHConfigurationFiles.Path`, `data.findings.SSHConfigurationFiles.id`, `data.findings.SSHConfigurationFiles.name`, `data.findings.SSHConfigurationFiles.type`, `data.findings.Roles.name`, `data.findings.Roles.RoleType`, `data.findings.Roles.id`, `data.findings.Roles.type`, `data.asset_regions`, `data.asset_vpcs`, `data.findings.Arn`, `data.findings.Exposure`, `data.findings.HasMalwareWithHighConfidence`, `data.findings.InstanceProfile.Arn`, `data.findings.InstanceProfile.id`, `data.findings.InstanceProfile.name`, `data.findings.InstanceProfile.type`, `data.findings.InstanceProfile.InstanceProfileId`, `data.findings.InstanceProfile.Roles.Arn`, `data.findings.InstanceProfile.Roles.EffectivePermissionsPolicy.id`, `data.findings.InstanceProfile.Roles.EffectivePermissionsPolicy.name`, `data.findings.InstanceProfile.Roles.EffectivePermissionsPolicy.type`, `data.findings.InstanceProfile.Roles.LastActiveTime`, `data.findings.InstanceProfile.Roles.PermissionUsage`, `data.findings.LinuxOsPasswords.MaskedPassword`, `data.findings.LinuxOsPasswords.id`, `data.findings.LinuxOsPasswords.name`, `data.findings.LinuxOsPasswords.type`, `data.findings.InstanceProfile.Roles.RoleId`, `data.findings.InstanceProfile.Roles.asset_unique_id`, `data.findings.InstanceProfile.Roles.Policies.IsPermissive`, `data.findings.InstanceProfile.Roles.Policies.PermissiveActions`, `data.findings.InstanceProfile.Roles.Policies.PolicyBody`, `data.findings.InstanceProfile.Roles.Policies.PolicyId`, `data.findings.InstanceProfile.Roles.Policies.asset_unique_id`, `data.findings.InstanceProfile.Roles.Policies.id`, `data.findings.InstanceProfile.Roles.Policies.name`, `data.findings.InstanceProfile.Roles.Policies.type`, `data.findings.Content.asset_unique_id`, `data.findings.Content.id`, `data.findings.Content.name`, `data.findings.Content.type`, `data.findings.IsDir`, `data.findings.SensitiveData.ExtraData.CommandWithParameters`, `data.findings.SensitiveData.ExtraData.MaskedPassword`, `data.findings.SensitiveData.ExtraData.Username`, `data.findings.SensitiveData.id`, `data.findings.SensitiveData.name`, `data.findings.SensitiveData.type`, `data.asset_tags.L1_AREA`, `data.asset_tags.L8_TEAM`, `data.asset_tags.L3_CLIENT`, `data.asset_tags.L5_PRODUCT`, `data.asset_tags.L6_ENVIRONMENT`, `data.asset_tags.L7_FUNCTIONALITY`, `data.asset_tags.aws_ec2launchtemplate_id`, `data.asset_tags.aws_autoscaling_groupName`, `data.asset_tags.Tenable`, `data.asset_tags.DTP-TOOLS`, `data.asset_tags.Description`, `data.asset_tags.DTP-DEVOPS`, `data.asset_tags.business_area`, `data.asset_tags.technical_role`, `data.asset_tags.backup_schedule`, `data.asset_tags.business_region`, `data.asset_tags.business_client`, `data.asset_tags.business_project`, `data.asset_tags.technical_origin`, `data.asset_tags.business_customer`, `data.asset_tags.compliance_origin`, `data.asset_tags.technical_cluster`, `data.asset_tags.technical_managed`, `data.asset_tags.technical_product`, `data.asset_tags.accountowner_owner`, `data.asset_tags.data_classification`, `data.asset_tags.IT-DarkTrace-Mirror`, `data.asset_tags.technical_provision`, `data.asset_tags.disasterrecovery_rpo`, `data.asset_tags.disasterrecovery_rto`, `data.asset_tags.operations_environment`, `data.findings.LinuxOsPasswords.Username`, `data.findings.LinuxOsPasswords.Status`, `data.related_compliances`, `data.auto_remediation_actions` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.findings.cve.packages.package_name`, `data.findings.cve.packages.patched_version`, `data.findings.cve.packages.installed_version`, `data.findings.anomaly_context.unix_timestamp_anomaly_hour`, `data.findings.WindowsOsPasswords` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `data.resource_group_name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.asset.first_seen_time`: Newly mapped `data.findings.cve.first_seen` raw log field with `event.idm.read_only_udm.target.asset.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cve_id`: Newly mapped `data.findings.cve.cve_id` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cve_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.severity_details`: Newly mapped `data.findings.cve.cvss_severity` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector`: Newly mapped `data.findings.cve.cvss_vector` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector` UDM field.  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score`: Newly mapped `data.findings.cve.cvss_score` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `data.asset_tags.who` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `data.asset_tags.service` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.asset.creation_time`: Newly mapped `data.asset_tags.date_created` raw log field with `event.idm.read_only_udm.target.asset.creation_time` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `data.asset_tags.iam_role_name` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `data.asset_tags.created_by` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.   
2026-03-05 |  Enhancement:  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.account_id`, `data.status`, `data.type`, `data.orca_score`, `data.last_updated` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.category_details`: Newly mapped `data.alert_category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
-`event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `data.last_seen` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
-`event.idm.read_only_udm.principal.resource_ancestors`: Newly mapped `data.account_name` raw log field with `event.idm.read_only_udm.principal.resource_ancestors` UDM field.  
-`event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `data.asset_tags.Environment` , `data.asset_tags.Application` , `data.asset_tags.bp-snapshot-policy` , `data.asset_tags.aws:cloudformation:stack-name` , `data.asset_tags.aws:cloudformation:stack-id` , `data.asset_tags.aws:cloudformation:logical-id` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `data.asset_regions`, `data.asset_labels` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
-`event.idm.read_only_udm.security_result.rule_name`: Newly mapped `data.rule_type` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
-`event.idm.read_only_udm.security_result.description`: Newly mapped `data.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
-`event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `data.asset_category` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
-`event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `data.alert_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
-`event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `data.alert_ui_link` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `data.asset_type`, `data.asset_name`, `data.asset_state`, `data.cve_list`, `data.asset_unique_id`, `data.cloud_provider_id`, `data.alert_labels`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.security_result.summary`: Newly mapped `data.details` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-02-06 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `remediation_console` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `findings.Vpc.id`, `findings.Vpc.name`, `meta.is_migrated`,`findings.Vpc.asset_unique_id`, `findings.Vpc.type`, `findings.ip`, `findings.name`, `findings.type`, `findings.version`, `account_id`, `last_updated`, `findings.id`, `findings.fixable`, `findings.top_cves.cve_id`, `findings.top_cves.fixable`, `findings.top_cves.cvss_score`, `findings.top_cves.first_seen`, `findings.top_cves.cvss_source`, `findings.top_cves.cvss_vector`, `findings.top_cves.exploitable`, `findings.top_cves.cvss_source_link`, `findings.total_cves`, `findings.exploitable`, `findings.count_by_cvss_severity.MEDIUM`, `findings.count_by_cvss_severity.CRITICAL`, `orca_score` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auto_remediation_actions` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `alert_category` raw log field(s) with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `findings.GroupId` raw log field(s) with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `findings.Region` raw log field(s) with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.about.ip`: Newly mapped `findings.SgIpPermissions.IpRanges` raw log field(s) with `event.idm.read_only_udm.security_result.about.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `alert_id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `alert_ui_link` raw log field(s) with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.   
2025-10-17 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data.Source`, `data.RuleSource` ,`data.CveExploitAvailable` ,`data.CveFixAvailable`, `data.MaxCvssScore`, `data.Recommendation.value`, `data.AlertSource`, `data.AlertId` and `data.Findings.id` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.Labels`, `data.CveIds`, `data.Inventory.asset_unique_id` and `data.Score` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `data.Inventory.name` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id` : Newly mapped `data.RuleId` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name` : Newly mapped `data.RuleType` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.   
2025-10-14 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `name` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `last_seen` raw log field to `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `data.RiskFindings.value.Email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `data.RiskFindings.value.AzureUserId` raw log field to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.name`: Newly mapped `data.AssetData.value.account_name` raw log field to `event.idm.read_only_udm.principal.cloud.project.name` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.environment`: Conditionally mapped `data.AssetData.value.cloud_provider` raw log field to `event.idm.read_only_udm.principal.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.id`: Newly mapped `data.AssetData.value.cloud_vendor_id` raw log field to `event.idm.read_only_udm.principal.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `data.RiskFindings.value.ConsoleUrlLink` raw log field to `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `data.AssetData.value.asset_category`, elements from `data.AssetData.value.asset_vpcs`, elements from `data.AssetData.value.asset_regions`, elements from `data.AssetData.value.asset_tags_info_list`, elements from `data.AssetData.value.custom_tags_info_list`, `data.AssetData.value.cluster_type`, elements from `data.AssetData.value.asset_labels`, and `data.AssetData.value.resource_group_name` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `data.Details.value` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `data.RuleId.value` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Conditionally mapped `data.RiskLevel.value` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `data.Severity.value` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `data.RuleType.value` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped based on parsing elements from `data.MitreTechniques.value` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped based on parsing elements from `data.MitreTechniques.value` raw log field to `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.RiskFindings.value.CreationTime` (key: `creation_time`), `data.RiskFindings.value.LastActiveTime` (key: `last_active_time`), `data.CreatedAt.value` (key: `data_created_at`), `data.CommentsCount.value` (key: `comments_count`), `data.LastSeen.value` (key: `last_seen`), `data.LastUpdated.value` (key: `last_updated`), `data.AssetData.value.vm_id` (key: `asset_data_vm_id`), `data.RiskLevelTime.value` (key: `risk_level_time`), `data.last_sync.value` (key: `last_sync_time`), `data.AssetData.value.cluster_name` (key: `cluster_name`), elements from `data.Labels.value` (key: `Data Value Label List`), `data.RemediationCli.value` elements (key: `remediation_cli_list`), `data.RemediationConsole.value` elements (key: `remediation_console_list`), and `data.StatusTime.value` (key: `orca_status_time`) raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.RiskFindings.value.AccountEnabled` (key: `risk_findings_account_enabled`), `data.IsLive.value` (key: `is_live`), `data.OrcaScore.value` (key: `orca_score`), `data.Status.value` (key: `orca_status`), elements from `data.RelatedCompliances.value` (keys: `related_compliances_*`), `data.RiskFindings.value.id` (key: `risk_finding_id`), `data.RiskFindings.value.version` (key: `risk_findings_version`), `data.Score.value` (key: `orca_raw_score`), elements from `data.ScoreVector.value.AlertBaseScore.Features` (keys: `AlertBaseScore_*`), elements from `data.ScoreVector.value.AssetContextScore.Features` (keys: `AssetContextScore_*`), `data.Title.value` (key: `alert_title`), and `data.RuleSource.value` (key: `data_rule_source`) raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-08-13 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped the `Details.User_Name` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped from the `URI` field extracted from the XML in TaskContent (within raw_event.EventData.Data) to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `raw_event.EventData.Data` to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Details.Scheduled_Task_Name` and `Details.Task_Execution_Count` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `TaskContent`, `Date`, `Author`, `Source`, `Description`, `SecurityDescriptor`, `boot_trigger_enabled`, `boot_trigger_delay`, `boot_trigger_repetition_interval`, `use_unified_scheduling_engine`, `multiple_instances_policy`, `disallow_start_if_on_batteries`, `execution_time_limit`, `stop_if_going_on_batteries`, `allow_start_on_demand`, `start_when_available`, `enabled`, `hidden`, and `run_only_if_idle` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-29 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `data.LastUpdated` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `data.Category` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `data.RuleSource` raw log field to `event.idm.read_only_udm.metadata.product_name`.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `data.Inventory.id` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id`.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `data.Inventory.type` raw log field to `event.idm.read_only_udm.principal.resource.resource_subtype`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `data.Hostname` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `data.Hostname` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `data.Severity` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `data.Severity` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `customerName` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary` raw log field to `event.idm.read_only_udm.intermediary`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data.AlertType`, `data.RiskLevel`, `data.CreatedAt`, `data.LastSeen`, `data.ClosedTime`, `data.StatusTime` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.   
2025-06-30 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields`: Newly Mapped `related_compliances`, `Event Viewer File`, and `data.remediation_console` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques and event.idm.read_only_udm.security_result.attack_details.tactics: Newly Mapped `data.mitre_technique` and `data.mitre_techniques` with `event.idm.read_only_udm.security_result.attack_details.techniques` and `event.idm.read_only_udm.security_result.attack_details.tactics` UDM fields.   
2025-02-28 |  Enhancement:  
\- Mapped `ACCOUNT`, `EVENT_CATEGORY`, `subject.srcEvent.recipientAccountAlias`, `DERIVED_FIELDS.SOURCE`, `subject.srcEvent.event.userIdentity.accessKeyId`, `subject.srcEvent.event.userIdentity.arn`, `subject.srcEvent.event.errorCode`, `subject.srcEvent.event.errorMessage`, `subject.srcEvent.event.eventID`, `subject.srcEvent.event.eventSource`, `subject.srcEvent.event.userIdentity.sessionContext.attributes.mfaAuthenticated`, `subject.srcEvent.username`, `subject.startTime`, `subject.srcEvent.eventName`, `DERIVED_FIELDS.CATEGORY`, `DERIVED_FIELDS.SUBCATEGORY`, `subject.dstEvent.gbm_version`, `subject.dstEvent.is_visible`, `subject.dstEvent.severity`, `subject.dstEvent.recipientAccountAlias`, `subject.srcEvent.api`, `subject.srcEvent.calltype`, `subject.srcEvent.gbm_version`, `subject.srcEvent.is_visible`, `subject.srcEvent.severity` to `additional.fields`.  
\- Mapped `SUMMARY` to `metadata.description`.  
\- Mapped `EVENT_TYPE` to `metadata.product_event_type`.  
\- Mapped `EVENT_ID` to `metadata.product_log_id`.  
\- Mapped `LINK` to `metadata.url_back_to_product`.  
\- Mapped `subject.srcEvent.event.userAgent`, `subject.srcEvent.source` to `network.http.user_agent`.  
\- Mapped `subject.srcEvent.recipientAccountId` to `principal.user.groupid`.  
\- Mapped `subject.srcEvent.principalId` to `principal.user.userid`.  
\- Mapped `subject.srcEvent.event.awsRegion` to `security_result.about.asset.attribute.cloud.availability_zone`.  
\- Mapped `subject.srcEvent.event.eventCategory` to `security_result.about.asset.category`.  
\- Mapped `EVENT_NAME` to `security_result.category` (ACL_VIOLATION or AUTH_VIOLATION based on event name)  
\- Mapped `EVENT_NAME` to `security_result.summary`.  
\- Mapped `subject.srcType` to `src.resource.resource_subtype`.  
\- Mapped `subject.srcEvent.event.userIdentity.sessionContext.attributes.creationDate` to `metadata.event_timestamp`.  
\- Mapped `subject.srcEvent.accountcaller` to `principal.resource.product_object_id`.  
\- Mapped `subject.dstEvent.region` to `target.asset.location.name`.  
\- Mapped `subject.dstEvent.accountcaller` to `target.resource.product_object_id`.  
\- Mapped `subject.dstType` to `target.resource.resource_subtype`.  
\- Mapped `subject.dstEvent.service` to `target.url`.  
\- Mapped `subject.dstEvent.username` to `target.user.userid`.   
2025-02-06 |  Enhancement: Added support for a new JSON log format.   
2025-01-07 |  Newly created parser for ORCA.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
