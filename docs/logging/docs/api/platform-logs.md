---
url: https://docs.cloud.google.com/logging/docs/api/platform-logs/
title: Google Cloud platform logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:11.838774+00:00
---

# Google Cloud platform logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/platform-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Google Cloud platform logs Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud platform logs in Cloud Logging let you debug and troubleshoot issues, monitor resources, and understand the Google Cloud services that you use. Logging receives, indexes, and stores these service-specific log entries so that you can view, query, and manage them.

## Overview

The Google Cloud platform logs visible to you in Logging depend on which [Google Cloud services](https://cloud.google.com/terms/services) and resources you use in your Google Cloud project or organization.

When using this document, note the following:

  * Not all Google Cloud services implement platform logs. For an expanding (non-exhaustive) list of the services that implement platform logs, see the following Index of Google Cloud platform logs.
  * Each Google Cloud service that implements platform logs manages its own configuration. Refer to [service-specific documentation](https://docs.cloud.google.com/docs) to determine whether the service enables platform logs by default and how to enable or disable platform logs.



## Index of Google Cloud platform logs

Following are tables of some of the Google Cloud platform logs supported by Cloud Logging. To understand the data contained in the tables, see Log entry structure on this page.

**Note:** This index is actively being expanded to include more Google Cloud platform logs. This index isn't an exhaustive list of all the Google Cloud platform logs available in Cloud Logging. For a list of Google Cloud services with monitored resources in Cloud Logging, see [Monitored resources and services](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

### Abuse Event

Logging API service name: `abuseevent.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
abuseevent.googleapis.com%2Fabuse_events | abuseevent.googleapis.com/Location | [type.googleapis.com/google.cloud.abuseevent.logging.v1.AbuseEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/abuseevent/logging/v1/abuse_event.proto) | abuseevent.googleapis.com/service_account  
abuseevent.googleapis.com/vm_resource | CRITICAL  
NOTICE  
ALERT  
  
### AlloyDB

Logging API service name: `alloydb.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
alloydb.googleapis.com%2Fpostgres.log | alloydb.googleapis.com/Instance | The PostgreSQL database logs. | CONSUMER_PROJECT  
CONSUMER_PROJECT_NUMBER  
NODE_ID  
SOURCE  
DATABASE_VERSION | INFO  
WARNING  
ERROR  
ALERT  
NOTICE  
alloydb.googleapis.com%2Fjournald | alloydb.googleapis.com/Instance | Container logs for dataplane agents. | CONSUMER_PROJECT  
CONSUMER_PROJECT_NUMBER  
CONTAINER_ID  
CONTAINER_ID_FULL  
CONTAINER_LOG_ORDINAL  
CONTAINER_NAME  
CONTAINER_TAG  
IMAGE_NAME  
NODE_ID  
DATABASE_VERSION  
SYSLOG_FACILITY  
SYSLOG_IDENTIFIER  
SYSLOG_TIMESTAMP  
_BOOT_ID  
_CAP_EFFECTIVE  
_CMDLINE  
_COMM  
_EXE  
_GID  
_HOSTNAME  
_MACHINE_ID  
_PID  
_RUNTIME_SCOPE  
_SOURCE_REALTIME_TIMESTAMP  
_STREAM_ID  
_SYSTEMD_CGROUP  
_SYSTEMD_INVOCATION_ID  
_SYSTEMD_SLICE  
_SYSTEMD_UNIT  
_TRANSPORT  
 _UID  
_ _MONOTONIC _TIMESTAMP  
_ _REALTIME_TIMESTAMP  
CONTAINER_LOG _EPOCH  
_ _SEQNUM  
_ _SEQNUM_ID  
CODE_LINE  
CODE_FILE  
JOB_ID  
TID  
CODE_FUNCTION  
SYSLOG_RAW  
INVOCATION_ID  
UNIT | ERROR  
INFO  
WARNING  
NOTICE  
ALERT  
alloydb.googleapis.com%2Fpostgresinternal | alloydb.googleapis.com/Instance | The internal dogfish logs. | CONSUMER_PROJECT  
CONSUMER_PROJECT_NUMBER  
LOG_TYPE  
NODE_ID  
DATABASE_VERSION | DEFAULT  
INFO  
WARNING  
ERROR  
alloydb.googleapis.com%2Finstance_agent | saas_instance | Logs for instance agent running on AlloyDB VM. | N/A | INFO  
WARNING  
ERROR  
EMERGENCY  
alloydb.googleapis.com%2Fpostgres_upgrade | alloydb.googleapis.com/Instance | It contains log output by pg_upgrade during database major version upgrade. | OPERATION_NAME  
FILE_NAME  
LOG_TYPE | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
alloydb.googleapis.com%2Fpostgres_upgrade_internal | alloydb.googleapis.com/Instance | The internal pg_upgrade logs during database major version upgrade. | OPERATION_NAME  
FILE_NAME  
LOG_TYPE | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
alloydb.googleapis.com%2Freplication | alloydb.googleapis.com/Instance | Logs for the replication workflow. | OPERATION_STAGE  
SOURCE_ID  
TARGET_ID  
OPERATION_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Application Integration

Logging API service name: `integrations.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
integrations.googleapis.com%2Fexecution_info | integrations.googleapis.com/IntegrationVersion | [type.googleapis.com/google.cloud.integrations.v1alpha.ExecutionInfo](https://github.com/googleapis/googleapis/blob/master/google/cloud/integrations/v1alpha/log_entries.proto) | N/A | INFO  
WARNING  
ERROR  
  
### Artifact Registry

Logging API service name: `artifactregistry.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
artifactregistry.googleapis.com%2Frequests | artifactregistry.googleapis.com/Project | [type.googleapis.com/google.devtools.artifactregistry.logging.v1.RequestLog](https://github.com/googleapis/googleapis/blob/master/google/devtools/artifactregistry/logging/v1/request_log.proto) | artifactregistry.googleapis.com/method_name  
artifactregistry.googleapis.com/resource_name  
artifactregistry.googleapis.com/resource_location  
artifactregistry.googleapis.com/trace_id | INFO  
ERROR  
artifactregistry.googleapis.com%2Frequests | artifactregistry.googleapis.com/Repository | [type.googleapis.com/google.devtools.artifactregistry.logging.v1.RequestLog](https://github.com/googleapis/googleapis/blob/master/google/devtools/artifactregistry/logging/v1/request_log.proto) | artifactregistry.googleapis.com/method_name  
artifactregistry.googleapis.com/resource_name  
artifactregistry.googleapis.com/resource_location  
artifactregistry.googleapis.com/trace_id  
artifactregistry.googleapis.com/repository_format  
artifactregistry.googleapis.com/repository_mode | INFO  
ERROR  
  
### Assured Workloads

Logging API service name: `assuredworkloads.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
assuredworkloads.googleapis.com%2Fregulatory_intercept_ack | folder | [type.googleapis.com/google.cloud.assuredworkloads.regulatoryintercept.logging.v1.RegulatoryInterceptAckLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/assuredworkloads/regulatoryintercept/logging/v1/regulatory_intercept_ack_log_entry.proto) | N/A | INFO  
assuredworkloads.googleapis.com%2Fregulatory_intercept_ack | project | [type.googleapis.com/google.cloud.assuredworkloads.regulatoryintercept.logging.v1.RegulatoryInterceptAckLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/assuredworkloads/regulatoryintercept/logging/v1/regulatory_intercept_ack_log_entry.proto) | N/A | INFO  
  
### Backup for GKE

Logging API service name: `gkebackup.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
gkebackup.googleapis.com%2Fbackup_change | gkebackup.googleapis.com/BackupPlan | [type.googleapis.com/google.cloud.gkebackup.logging.v1.BackupChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | backup_id | INFO  
ERROR  
gkebackup.googleapis.com%2Fbackup_plan_change | gkebackup.googleapis.com/BackupPlan | [type.googleapis.com/google.cloud.gkebackup.logging.v1.BackupPlanChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | backup_plan_id | INFO  
ERROR  
gkebackup.googleapis.com%2Frestore_change | gkebackup.googleapis.com/RestorePlan | [type.googleapis.com/google.cloud.gkebackup.logging.v1.RestoreChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | restore_id | INFO  
ERROR  
gkebackup.googleapis.com%2Frestore_plan_change | gkebackup.googleapis.com/RestorePlan | [type.googleapis.com/google.cloud.gkebackup.logging.v1.RestorePlanChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | restore_plan_id | INFO  
ERROR  
gkebackup.googleapis.com%2Fbackup_channel_change | gkebackup.googleapis.com/BackupChannel | [type.googleapis.com/google.cloud.gkebackup.logging.v1.BackupChannelChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | backup_channel_id | INFO  
ERROR  
gkebackup.googleapis.com%2Frestore_channel_change | gkebackup.googleapis.com/RestoreChannel | [type.googleapis.com/google.cloud.gkebackup.logging.v1.RestoreChannelChange](https://github.com/googleapis/googleapis/blob/master/google/cloud/gkebackup/logging/v1/logging.proto) | restore_channel_id | INFO  
ERROR  
gkebackup.googleapis.com%2Fbfg_backup_plan_jobs | gkebackup.googleapis.com/BackupPlan | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupPlanJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
gkebackup.googleapis.com%2Fbfg_backup_restore_jobs | gkebackup.googleapis.com/Project | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupRestoreJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
gkebackup.googleapis.com%2Fclh | global | CLH logs | N/A | ERROR  
INFO  
WARNING  
DEFAULT  
  
### BigQuery Data Transfer API

Logging API service name: `bigquerydatatransfer.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
bigquerydatatransfer.googleapis.com%2Ftransfer_config | bigquery_dts_config | Debug logs for BigQuery Data Transfer runs. Describes the current status of the transfer run. | run_id | DEFAULT  
INFO  
WARNING  
ERROR  
  
### CbTestDuckService

Logging API service name: `cbtestduckservice.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cbtestduckservice.googleapis.com%2Factivity_history | cbtestduckservice.googleapis.com/Book | Test payload for CB Test Duck Service | N/A | INFO  
DEBUG  
ERROR  
  
### Certificate Manager

Logging API service name: `certificatemanager.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
certificatemanager.googleapis.com%2Fcertificates_expiry | certificatemanager.googleapis.com/Project | [type.googleapis.com/google.cloud.certificatemanager.logging.v1.CertificatesExpiry](https://github.com/googleapis/googleapis/blob/master/google/cloud/certificatemanager/logging/v1/logs.proto) | N/A | WARNING  
  
### Chat

Logging API service name: `chat.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
chat.googleapis.com%2Ferrors | chat.googleapis.com/Project | [type.googleapis.com/google.chat.logging.v1.ChatAppLogEntry](https://github.com/googleapis/googleapis/blob/master/google/chat/logging/v1/chat_app_log_entry.proto) | N/A | ERROR  
  
### Cloud Backup and DR

Logging API service name: `backupdr.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
backupdr.googleapis.com%2Fbackup_recovery_appliance_events | backupdr.googleapis.com/BackupRecoveryAppliance | [type.googleapis.com/google.cloud.backupdr.logging.v1.Event](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/eventlog.proto) | N/A | ERROR  
WARNING  
INFO  
backupdr.googleapis.com%2Fgcb_backup_recovery_jobs | backupdr.googleapis.com/ManagementConsole | [type.googleapis.com/google.cloud.backupdr.logging.v1.BackupRecoveryJobReportLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/reportlog.proto) | N/A | INFO  
backupdr.googleapis.com%2Fgcb_daily_schedule_compliance | backupdr.googleapis.com/ManagementConsole | [type.googleapis.com/google.cloud.backupdr.logging.v1.DailyScheduleComplianceReportLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/reportlog.proto) | N/A | INFO  
backupdr.googleapis.com%2Fgcb_protected_resource | backupdr.googleapis.com/ManagementConsole | [type.googleapis.com/google.cloud.backupdr.logging.v1.ProtectedResourceReportLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/reportlog.proto) | N/A | INFO  
backupdr.googleapis.com%2Fbdr_backup_restore_jobs | backupdr.googleapis.com/BackupDRProject | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupRestoreJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
backupdr.googleapis.com%2Fbdr_backup_plan_jobs | backupdr.googleapis.com/BackupPlan | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupPlanJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
backupdr.googleapis.com%2Fbdr_auto_protection_policy_jobs | backupdr.googleapis.com/AutoProtectionPolicy | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRAutoProtectionPolicyJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
backupdr.googleapis.com%2Fbdr_auto_protection_policy_binding_jobs | backupdr.googleapis.com/AutoProtectionPolicyBinding | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRAutoProtectionPolicyBindingJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
backupdr.googleapis.com%2Fbdr_auto_protection_policy_binding_jobs | backupdr.googleapis.com/BackupDRProject | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRAutoProtectionPolicyBindingJobLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
ERROR  
backupdr.googleapis.com%2Fbdr_protected_resource | backupdr.googleapis.com/BackupPlan | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRProtectedResourceLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
backupdr.googleapis.com%2Fbdr_backup_vault_details | backupdr.googleapis.com/BackupVault | [type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupVaultDetailsLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/backupdr/logging/v1/bdr_log.proto) | N/A | INFO  
  
### Cloud Database Migration Service

Logging API service name: `datamigration.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
datamigration.googleapis.com%2Fmigration_job_event | datamigration.googleapis.com/MigrationJob | [type.googleapis.com/google.cloud.clouddms.logging.v1.MigrationJobEventLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/clouddms/logging/v1/clouddms_platform_logs.proto) | N/A | INFO  
NOTICE  
ERROR  
datamigration.googleapis.com%2Fconnection_profile_event | datamigration.googleapis.com/ConnectionProfile | [type.googleapis.com/google.cloud.clouddms.logging.v1.ConnectionProfileEventLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/clouddms/logging/v1/clouddms_platform_logs.proto) | N/A | INFO  
NOTICE  
ERROR  
datamigration.googleapis.com%2Fprivate_connection_event | datamigration.googleapis.com/PrivateConnection | [type.googleapis.com/google.cloud.clouddms.logging.v1.PrivateConnectionEventLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/clouddms/logging/v1/clouddms_platform_logs.proto) | N/A | INFO  
NOTICE  
ERROR  
  
### Cloud Datastream

Logging API service name: `datastream.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
datastream.googleapis.com%2Fstream_activity | datastream.googleapis.com/Stream | [type.googleapis.com/google.cloud.datastream.logging.v1.StreamActivityLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/datastream/logging/v1/datastream_logs.proto) | N/A | ERROR  
INFO  
WARNING  
  
### Cloud Deploy

Logging API service name: `clouddeploy.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
clouddeploy.googleapis.com%2Frelease_render | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.ReleaseRenderEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/release_render_payload.proto) | N/A | INFO  
clouddeploy.googleapis.com%2Frollout_notification | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.RolloutNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/rollout_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Frollout_update | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.RolloutUpdateEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/rollout_update_payload.proto) | N/A | INFO  
clouddeploy.googleapis.com%2Fdeliverypipeline_notification | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.DeliveryPipelineNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/deliverypipeline_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Fdeploypolicy_evaluation | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.DeployPolicyEvaluationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/deploypolicy_evaluation_payload.proto) | N/A | INFO  
WARNING  
ERROR  
clouddeploy.googleapis.com%2Fdeploypolicy_notification | clouddeploy.googleapis.com/DeployPolicy | [type.googleapis.com/google.cloud.deploy.v1.DeployPolicyNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/deploypolicy_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Fcustomtargettype_notification | clouddeploy.googleapis.com/CustomTargetType | [type.googleapis.com/google.cloud.deploy.v1.CustomTargetTypeNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/customtargettype_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Ftarget_notification | clouddeploy.googleapis.com/Target | [type.googleapis.com/google.cloud.deploy.v1.TargetNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/target_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Frelease_notification | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.ReleaseNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/release_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Fjobrun_notification | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.JobRunNotificationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/jobrun_notification_payload.proto) | N/A | ERROR  
clouddeploy.googleapis.com%2Fautomation | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.AutomationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/automation_payload.proto) | N/A | ERROR  
NOTICE  
clouddeploy.googleapis.com%2Fautomationrun | clouddeploy.googleapis.com/DeliveryPipeline | [type.googleapis.com/google.cloud.deploy.v1.AutomationRunEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/deploy/v1/automationrun_payload.proto) | N/A | ERROR  
NOTICE  
  
### Cloud Functions

Logging API service name: `cloudfunctions.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cloudfunctions.googleapis.com%2Fcloud-functions | cloud_function | Cloud Functions writes logs to this stream that indicate the start and end of execution, as well as the stdout and stderr from those executions. | execution_id  
instance_id  
infrastructure  
runtime_version | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Cloud IDS

Logging API service name: `ids.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
ids.googleapis.com%2Fthreat | ids.googleapis.com/Endpoint | Threat logs from the Cloud IDS endpoint. | N/A | DEFAULT  
ids.googleapis.com%2Finstance_agent | saas_instance | Logs for instance agent running on Cloud IDS VM. | N/A | ERROR  
INFO  
WARNING  
ids.googleapis.com%2Ftraffic | ids.googleapis.com/Endpoint | Traffic logs from the Cloud IDS endpoint. | N/A | DEFAULT  
  
### Cloud Load Balancing

Logging API service name: `loadbalancing.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
loadbalancing.googleapis.com%2Frequests | internal_http_lb_rule | [type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/loadbalancing/type/load_balancer_log_entry.proto) | N/A | INFO  
WARNING  
ERROR  
loadbalancing.googleapis.com%2Fexternal_regional_requests | http_external_regional_lb_rule | [type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/loadbalancing/type/load_balancer_log_entry.proto) | N/A | INFO  
WARNING  
ERROR  
  
### Cloud Locations

Logging API service name: `cloud.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cloud.googleapis.com%2Fipsec_events | vpn_gateway | VPN Tunnel logs from the VPN Gateway instance | tunnel_id | DEBUG  
NOTICE  
  
### Cloud Monitoring API

Logging API service name: `monitoring.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
monitoring.googleapis.com%2Fuptime_checks | uptime_url | uptime_url uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | gae_app | gae_app uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | gce_instance | gce_instance uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | aws_ec2_instance | aws_ec2_instance uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | aws_elb_load_balancer | aws_elb_load_balancer uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | k8s_service | k8s_service uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | servicedirectory_service | servicedirectory_service uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
monitoring.googleapis.com%2Fuptime_checks | cloud_run_revision | cloud_run_revision uptime check logs. | check_id  
checker_location  
execution_id  
uptime_result_type  
service_directory_endpoint | ERROR  
INFO  
NOTICE  
  
### Cloud OS Config

Logging API service name: `osconfig.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
osconfig.googleapis.com%2Fpatch_job | cloud_osconfig_patch_job | [type.googleapis.com/google.cloud.osconfig.logging.PatchJobCompletedLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/osconfig/logging/patch_job_log.proto) | osconfig.googleapis.com/patch_job | INFO  
ERROR  
  
### Cloud Run

Logging API service name: `run.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
run.googleapis.com%2Fstdout | cloud_run_revision | Cloud Run stdout logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stdout from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
goog-managed-by  
goog-cloudfunctions-runtime  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstderr | cloud_run_revision | Cloud Run stderr logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stderr from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
goog-managed-by  
goog-cloudfunctions-runtime  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Frequests | cloud_run_revision | Cloud Run request logs. Each request served by a Cloud Run service should have a corresponding request log entry. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
goog-managed-by  
goog-cloudfunctions-runtime | DEFAULT  
INFO  
WARNING  
ERROR  
run.googleapis.com%2F/dev/log | cloud_run_revision | Cloud Run syslogs. These are syslog-structured logs written to /dev/log in the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
goog-managed-by  
goog-cloudfunctions-runtime  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/var/log | cloud_run_revision | Cloud Run /var/log logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to /var/log/** from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
goog-managed-by  
goog-cloudfunctions-runtime  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstdout | cloud_run_job | Cloud Run stdout logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stdout from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
run.googleapis.com/execution_name  
run.googleapis.com/task_index  
run.googleapis.com/task_attempt  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstderr | cloud_run_job | Cloud Run stderr logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stderr from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
run.googleapis.com/execution_name  
run.googleapis.com/task_index  
run.googleapis.com/task_attempt  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/dev/log | cloud_run_job | Cloud Run syslogs. These are syslog-structured logs written to /dev/log in the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
run.googleapis.com/execution_name  
run.googleapis.com/task_index  
run.googleapis.com/task_attempt  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/var/log | cloud_run_job | Cloud Run /var/log logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to /var/log/** from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
run.googleapis.com/execution_name  
run.googleapis.com/task_index  
run.googleapis.com/task_attempt  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstdout | cloud_run_worker_pool | Cloud Run stdout logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stdout from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstderr | cloud_run_worker_pool | Cloud Run stderr logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stderr from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/dev/log | cloud_run_worker_pool | Cloud Run syslogs. These are syslog-structured logs written to /dev/log in the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/var/log | cloud_run_worker_pool | Cloud Run /var/log logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to /var/log/** from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstdout | cloud_run_instance | Cloud Run stdout logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stdout from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Fstderr | cloud_run_instance | Cloud Run stderr logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to stderr from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2Frequests | cloud_run_instance | Cloud Run request logs. Each request served by a Cloud Run service should have a corresponding request log entry. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id | DEFAULT  
INFO  
WARNING  
ERROR  
run.googleapis.com%2F/dev/log | cloud_run_instance | Cloud Run syslogs. These are syslog-structured logs written to /dev/log in the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
run.googleapis.com%2F/var/log | cloud_run_instance | Cloud Run /var/log logs. Each entry contains a line (or multiple lines, if they match a known multi-line exception format like a stack trace) written to /var/log/** from the user container. | instanceId  
managed-by  
commit-sha  
gcb-trigger-id  
gcb-build-id  
container_name | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Cloud SQL

Logging API service name: `cloudsql.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cloudsql.googleapis.com%2Fmysql.err | cloudsql_database | The error log contains a record and diagnostic messages such as errors, warnings, and notes that occur during server startup, shutdown, and while the server is running. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fmysql-slow.log | cloudsql_database | The slow query log consists of SQL statements that take more than `long_query_time` seconds to execute. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fmysql-general.log | cloudsql_database | The general query log records when clients connect or disconnect, and it logs each SQL statement received from clients. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Freplication-setup.log | cloudsql_database | They are related to external server replication setup. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Freplication-status.log | cloudsql_database | They are related to external server replication status monitoring. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
SOURCE_ID  
PROJECT_NUMBER | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Factive_directory.log | cloudsql_database | It logs Active Directory related events for SQL Server instances. | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fxevents.log | cloudsql_database | It logs Extended Events related events for SQL Server instances. | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2FPolybase_Dms_movement.log | cloudsql_database | It logs DMS movement events for PolyBase enabled SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2FPolybase_Dms_errors.log | cloudsql_database | It logs DMS error events for PolyBase enabled SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2FPolybase_DWEngine_errors.log | cloudsql_database | It logs DWEngine error events for PolyBase enabled SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2FPolybase_DWEngine_movement.log | cloudsql_database | It logs DWEngine movement events for PolyBase enabled SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2FPolybase_DWEngine_server.log | cloudsql_database | It logs DWEngine server events for PolyBase enabled SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fmysql-upgrade.log | cloudsql_database | Used to contain mysql_upgrade logs. Now deprecated. | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fpostgres.log | cloudsql_database | It contains the database server's log output from the Cloud SQL instance. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fpostgres-audit.log | cloudsql_database | It contains the audit log entries from the pgAudit extension in the Cloud SQL instance. | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fsqlserver.err | cloudsql_database | These logs are from the SQL Server errorlog on the Cloud SQL instance. | CONTAINER_ID  
CONTAINER_ID_FULL  
CONTAINER_NAME  
CONTAINER_TAG  
CONTAINER_PARTIAL_ID  
CONTAINER_PARTIAL_LAST  
CONTAINER_PARTIAL_MESSAGE  
CONTAINER_PARTIAL_ORDINAL  
IMAGE_NAME  
INSTANCE_ID  
INSTANCE_UID  
LOG_BUCKET_NUM  
SYSLOG_IDENTIFIER  
_BOOT_ID  
_CAP_EFFECTIVE  
_CMDLINE  
_COMM  
_EXE  
_GID  
_HOSTNAME  
_MACHINE_ID  
_PID  
PROJECT_NUMBER  
_SOURCE_REALTIME_TIMESTAMP  
_SYSTEMD_CGROUP  
_SYSTEMD_INVOCATION_ID  
_SYSTEMD_SLICE  
_SYSTEMD_UNIT  
_TRANSPORT  
 _UID  
_ _MONOTONIC _TIMESTAMP  
_ _REALTIME_TIMESTAMP  
USERSPACE_USEC  
SYSLOG_TIMESTAMP  
SOURCE_ID  
_RUNTIME_SCOPE  
CONTAINER_LOG_ORDINAL  
CONTAINER_LOG _EPOCH  
_ _SEQNUM _ID  
_ _SEQNUM | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fsqlagent.out | cloudsql_database | These logs are from sqlagent.out on the Cloud SQL instance. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fentraid.log | cloudsql_database | It logs Entra ID related events for SQL Server instances. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Foperationdetails.log | cloudsql_database | These logs show details of long running operations such as Import SQL for SQL Server instances. | INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fpostgres-upgrade.log | cloudsql_database | It contains log output by pg_upgrade during database major version upgrade. | FILE_NAME  
INSTANCE_UID  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID  
EVENT_TIME | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fevent.log | cloudsql_database | It logs structured database environment events such as out of memory. | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fmysql-performance-capture.log | cloudsql_database | It contains log output of mysql performance capture logs. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID  
EVENT_TIME  
FILE_NAME | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
cloudsql.googleapis.com%2Fimage-audit.log | cloudsql_database | It contains runtime container and OS image digests for supply-chain certification verification. | INSTANCE_UID  
IS_EXTERNAL_SERVER_REPLICA  
LOG_BUCKET_NUM  
PROJECT_NUMBER  
SOURCE_ID  
imageId  
imageType  
imageClass  
imageCode  
releaseVersion | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Cloud Setup

Logging API service name: `cloudsetup.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cloudsetup.googleapis.com%2Fcomplete_deployment | api | [type.googleapis.com/google.cloud.cloudsetup.logging.v1.CompleteDeploymentEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/cloudsetup/logging/v1/complete_deployment.proto) | activity_type_name | DEFAULT  
  
### Cloud Storage

Logging API service name: `storage.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
storage.googleapis.com%2Frelocate_bucket_errors | gcs_bucket | [type.googleapis.com/google.storage.platformlogs.v1.RelocateBucketError](https://github.com/googleapis/googleapis/blob/master/google/storage/platformlogs/v1/relocate_bucket_error.proto) | N/A | ERROR  
  
### Cloud VPN

Logging API service name: `vpn.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
vpn.googleapis.com%2Fipsec_events | vpn_gateway | VPN Tunnel logs from the VPN Gateway instance | tunnel_id | DEBUG  
NOTICE  
  
### Cloud Workstations

Logging API service name: `workstations.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
workstations.googleapis.com%2Fdisk_assignments | workstations.googleapis.com/Workstation | Disk assignment logs | disk | NOTICE  
workstations.googleapis.com%2Fvm_assignments | workstations.googleapis.com/Workstation | VM assignment logs | external_ip  
instance_id  
internal_ip  
instance_name | NOTICE  
workstations.googleapis.com%2Fworkstation_shutdowns | workstations.googleapis.com/Workstation | Workstation shutdown logs | external_ip  
instance_id  
internal_ip  
instance_name  
shutdown_reason | NOTICE  
  
### Compute Engine

Logging API service name: `compute.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
compute.googleapis.com%2Fgce_disaster_recovery | gce_instance | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgce_disaster_recovery | gce_disk | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgce_disaster_recovery | gce_snapshot | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgce_disaster_recovery | gce_instance_template | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgce_disaster_recovery | gce_instance_group_manager | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgce_disaster_recovery | gce_resevered_address | [type.googleapis.com/google.compute.logging.dr.v1.DisasterRecoveryEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/dr/v1/disaster_recovery_event.proto) | N/A | N/A  
compute.googleapis.com%2Fgdnsusage | gce_instance | [type.googleapis.com/google.compute.logging.gdnsusage.v1.GdnsVmUsagePlatformLog](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/gdnsusage/v1/gdns_vm_usage.proto) | resource_name | DEBUG  
compute.googleapis.com%2Fvm_extension_policies | gce_instance | [type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent](https://github.com/googleapis/googleapis/blob/master/google/compute/logging/agentcontrolplane/v1/logs.proto) | N/A | INFO  
DEBUG  
ERROR  
WARNING  
  
### Container Security API

Logging API service name: `containersecurity.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
containersecurity.googleapis.com%2Ffinding | k8s_cluster | type.googleapis.com/cloud.kubernetes.security.containersecurity_logging.Finding | N/A | INFO  
  
### Dataform

Logging API service name: `dataform.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
dataform.googleapis.com%2Fworkflow_invocation_completion | dataform.googleapis.com/Repository | [type.googleapis.com/google.cloud.dataform.logging.v1.WorkflowInvocationCompletionLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataform/logging/v1/logging.proto) | N/A | INFO  
WARNING  
ERROR  
dataform.googleapis.com%2Factas_dry_run_result | dataform.googleapis.com/Repository | [type.googleapis.com/google.cloud.dataform.logging.v1.ActAsDryRunResultLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataform/logging/v1/logging.proto) | N/A | INFO  
WARNING  
  
### Datapipelines API

Logging API service name: `datapipelines.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
datapipelines.googleapis.com%2Frequests | datapipelines.googleapis.com/Location | [type.googleapis.com/google.cloud.datapipelines.logging.v1.RequestLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/datapipelines/logging/v1/logging.proto) | N/A | DEFAULT  
datapipelines.googleapis.com%2Frequests | datapipelines.googleapis.com/Pipeline | [type.googleapis.com/google.cloud.datapipelines.logging.v1.RequestLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/datapipelines/logging/v1/logging.proto) | N/A | DEFAULT  
  
### Dataproc

Logging API service name: `dataproc.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
dataproc.googleapis.com%2Fautoscaler | cloud_dataproc_cluster | [type.googleapis.com/google.cloud.dataproc.logging.AutoscalerLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/autoscaler_log.proto) | N/A | INFO  
WARNING  
ERROR  
CRITICAL  
dataproc.googleapis.com%2Fautoscaler | cloud_dataproc_batch | [type.googleapis.com/google.cloud.dataproc.logging.AutoscalerLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/autoscaler_log.proto) | N/A | INFO  
WARNING  
ERROR  
CRITICAL  
dataproc.googleapis.com%2Fautoscaler | cloud_dataproc_session | [type.googleapis.com/google.cloud.dataproc.logging.AutoscalerLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/autoscaler_log.proto) | N/A | INFO  
WARNING  
ERROR  
CRITICAL  
dataproc.googleapis.com%2Freconciler | cloud_dataproc_session | [type.googleapis.com/google.cloud.dataproc.logging.ReconciliationLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/reconciler_log.proto) | N/A | INFO  
dataproc.googleapis.com%2Freconciler | cloud_dataproc_cluster | [type.googleapis.com/google.cloud.dataproc.logging.ReconciliationClusterHealLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/reconciler_log.proto) | N/A | INFO  
dataproc.googleapis.com%2Fcluster_reconciler | cloud_dataproc_cluster | [type.googleapis.com/google.cloud.dataproc.logging.ReconciliationClusterHealLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/reconciler_log.proto), [type.googleapis.com/google.cloud.dataproc.logging.ReconciliationClusterTtlLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/reconciler_log.proto), [type.googleapis.com/google.cloud.dataproc.logging.ReconciliationClusterStopTtlLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/dataproc/logging/reconciler_log.proto) | N/A | INFO  
  
### Dataproc Metastore

Logging API service name: `metastore.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
metastore.googleapis.com%2Fbackground | metastore.googleapis.com/Service | Dataproc Metastore background logs. | logger | DEFAULT  
ERROR  
INFO  
WARNING  
metastore.googleapis.com%2Fsystem | metastore.googleapis.com/Service | Service system logs. | method  
service_region | DEFAULT  
ERROR  
INFO  
WARNING  
metastore.googleapis.com%2Frequests | metastore.googleapis.com/Service | Service request logs. | method  
service_region | DEFAULT  
INFO  
metastore.googleapis.com%2Fscheduled_backup | metastore.googleapis.com/Service | [type.googleapis.com/google.cloud.metastore.logging.v1.ScheduledBackupLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/metastore/logging/v1/scheduled_backups_log.proto) | N/A | DEFAULT  
INFO  
WARNING  
ERROR  
  
### Developer Connect

Logging API service name: `developerconnect.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
developerconnect.googleapis.com%2Fsdlc_deployment | k8s_cluster | type.googleapis.com/cloud.hosted.developerconnect.sdlc.logging.DeploymentEvent | developerconnect.googleapis.com/insights_config_id  
developerconnect.googleapis.com/insights_config_deployment_id | INFO  
  
### Event Threat Detection

Logging API service name: `threatdetection.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
threatdetection.googleapis.com%2Fdetection | threat_detector | Event Threat Detection finding. | N/A | NOTICE  
WARNING  
ALERT  
CRITICAL  
ERROR  
  
### Eventarc

Logging API service name: `eventarc.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
eventarc.googleapis.com%2Fenrollment_activity | eventarc.googleapis.com/Enrollment | [type.googleapis.com/google.cloud.eventarc.logging.v1.EnrollmentActivity](https://github.com/googleapis/googleapis/blob/master/google/cloud/eventarc/logging/v1/enrollment_activity.proto) | N/A | INFO  
ERROR  
eventarc.googleapis.com%2Fmessage_bus_activity | eventarc.googleapis.com/MessageBus | [type.googleapis.com/google.cloud.eventarc.logging.v1.MessageBusActivity](https://github.com/googleapis/googleapis/blob/master/google/cloud/eventarc/logging/v1/message_bus_activity.proto) | N/A | INFO  
ERROR  
eventarc.googleapis.com%2Fpipeline_activity | eventarc.googleapis.com/Pipeline | [type.googleapis.com/google.cloud.eventarc.logging.v1.PipelineActivity](https://github.com/googleapis/googleapis/blob/master/google/cloud/eventarc/logging/v1/pipeline_activity.proto) | N/A | INFO  
ERROR  
eventarc.googleapis.com%2Fgoogle_api_source_activity | eventarc.googleapis.com/GoogleApiSource | [type.googleapis.com/google.cloud.eventarc.logging.v1.GoogleApiSourceActivity](https://github.com/googleapis/googleapis/blob/master/google/cloud/eventarc/logging/v1/google_api_source_activity.proto) | N/A | INFO  
ERROR  
  
### Fault Testing

Logging API service name: `faulttesting.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
faulttesting.googleapis.com%2Fexperiment_events | faulttesting.googleapis.com/Experiment | [type.googleapis.com/google.cloud.faulttesting.v1alpha.FaultTestingLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/faulttesting/v1alpha/logging.proto) | N/A | INFO  
DEBUG  
ERROR  
  
### Firestore

Logging API service name: `firestore.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
firestore.googleapis.com%2Fundeliverable_first_gen_event | firestore.googleapis.com/Database | [type.googleapis.com/google.firestore.v1beta1.UndeliverableFirstGenEvent](https://github.com/googleapis/googleapis/blob/master/google/firestore/v1beta1/undeliverable_first_gen_event.proto) | firestore.googleapis.com/environment | ERROR  
  
### Firestore/Datastore

Logging API service name: `datastore.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
datastore.googleapis.com%2Fmigration_state | datastore_database | [type.googleapis.com/google.datastore.admin.v1.MigrationStateEvent](https://github.com/googleapis/googleapis/blob/master/google/datastore/admin/v1/migration.proto) | N/A | NOTICE  
datastore.googleapis.com%2Fmigration_progress | datastore_database | [type.googleapis.com/google.datastore.admin.v1.MigrationProgressEvent](https://github.com/googleapis/googleapis/blob/master/google/datastore/admin/v1/migration.proto) | N/A | INFO  
  
### GKE On-prem (Anthos)

Logging API service name: `anthos.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
anthos.googleapis.com%2Fseesaw_engine | anthos_l4lb | These logs are from seesaw_engine on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
anthos.googleapis.com%2Fseesaw_ha | anthos_l4lb | These logs are from seesaw_ha on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
anthos.googleapis.com%2Fseesaw_healthcheck | anthos_l4lb | These logs are from seesaw_healthcheck on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
anthos.googleapis.com%2Fseesaw_ncc | anthos_l4lb | These logs are from seesaw_ncc on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
anthos.googleapis.com%2Fseesaw_ecu | anthos_l4lb | These logs are from seesaw_ecu on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
anthos.googleapis.com%2Fseesaw_config | anthos_l4lb | These logs are from seesaw_config on the Seesaw VM instances running in GKE OnPrem. | N/A | N/A  
  
### Google Analytics Data API

Logging API service name: `analyticsdata.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
analyticsdata.googleapis.com%2Ffresh_bigquery_export_status | analyticsdata.googleapis.com/FreshBigQueryExport | [type.googleapis.com/google.analytics.cloud.ExportStatusLog](https://github.com/googleapis/googleapis/blob/master/google/analytics/cloud/bigquery_export_platform_log.proto) | N/A | DEFAULT  
INFO  
WARNING  
analyticsdata.googleapis.com%2Fbigquery_daily_export_status | analyticsdata.googleapis.com/BigQueryDailyExport | [type.googleapis.com/google.analytics.cloud.ExportStatusLog](https://github.com/googleapis/googleapis/blob/master/google/analytics/cloud/bigquery_export_platform_log.proto) | N/A | DEFAULT  
INFO  
WARNING  
  
### Google Binary Authorization API

Logging API service name: `binaryauthorization.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
binaryauthorization.googleapis.com%2Fcontinuous_validation | k8s_cluster | v1beta1: [type.googleapis.com/google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/binaryauthorization/v1beta1/continuous_validation_logging.proto) | N/A | WARNING  
  
### Google Health API

Logging API service name: `health.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
health.googleapis.com%2Fwebhook_notification | health.googleapis.com/Subscriber | [type.googleapis.com/google.devicesandservices.health.v4.WebhookNotificationCloudLog](https://github.com/googleapis/googleapis/blob/master/google/devicesandservices/health/v4/webhook_notification_cloud_log.proto) | N/A | DEFAULT  
INFO  
WARNING  
ERROR  
  
### Google Maps Platform - Mobility Billing

Logging API service name: `mobilitybilling.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
mobilitybilling.googleapis.com%2Fexternal_cloud_logs | mobilitybilling.googleapis.com/Project | [type.googleapis.com/google.maps.mobilitybilling.logs.v1.ReportBillableEventLog](https://github.com/googleapis/googleapis/blob/master/google/maps/mobilitybilling/logs/v1/mobility_billing_cloud_logging.proto) | environment | DEFAULT  
ERROR  
  
### Google Workspace Add-ons

Logging API service name: `gsuiteaddons.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
gsuiteaddons.googleapis.com%2Ferrors | g_suite_add_ons | [type.googleapis.com/google.cloud.gsuiteaddons.logging.v1.GSuiteAddOnsLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/gsuiteaddons/logging/v1/g_suite_add_ons_log_entry.proto) | N/A | ERROR  
  
### Identity Toolkit

Logging API service name: `identitytoolkit.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
identitytoolkit.googleapis.com%2Frequests | identitytoolkit_project | [type.googleapis.com/google.cloud.identitytoolkit.logging.RequestLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/identitytoolkit/logging/request_log.proto) | N/A | INFO  
ERROR  
identitytoolkit.googleapis.com%2Frequests | identitytoolkit_tenant | [type.googleapis.com/google.cloud.identitytoolkit.logging.RequestLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/identitytoolkit/logging/request_log.proto) | N/A | INFO  
ERROR  
  
### Immersive Stream for XR

Logging API service name: `stream.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
stream.googleapis.com%2Fsession_event | stream.googleapis.com/StreamInstance | [type.googleapis.com/google.cloud.stream.logging.v1.SessionEventLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/stream/logging/v1/logging.proto) | N/A | INFO  
ERROR  
  
### Key Management Service

Logging API service name: `cloudkms.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
cloudkms.googleapis.com%2Fcryptokey_events | cloudkms_cryptokey | [type.googleapis.com/google.cloud.kms.logging.v1.CryptoKeyEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/kms/logging/v1/logs.proto) | N/A | INFO  
ERROR  
cloudkms.googleapis.com%2Fcryptokeyversion_events | cloudkms_cryptokeyversion | [type.googleapis.com/google.cloud.kms.logging.v1.CryptoKeyVersionEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/kms/logging/v1/logs.proto) | N/A | INFO  
ERROR  
  
### Live Stream API

Logging API service name: `livestream.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
livestream.googleapis.com%2Fchannel_activities | livestream.googleapis.com/Channel | [type.googleapis.com/google.cloud.video.livestream.logging.v1.ChannelActivity](https://github.com/googleapis/googleapis/blob/master/google/cloud/video/livestream/logging/v1/logs.proto) | N/A | INFO  
DEBUG  
ERROR  
  
### Local Rides and Deliveries API

Logging API service name: `fleetengine.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
fleetengine.googleapis.com%2Fupdate_vehicle_attributes | fleetengine.googleapis.com/Fleet | type.googleapis.com/maps.fleetengine.v1.UpdateVehicleAttributesLog | environment  
vehicle_id | DEFAULT  
ERROR  
  
### Logging API

Logging API service name: `logging.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
logging.googleapis.com%2Fsink_error | logging_sink | A report of an error encountered while trying to export data to a configured log sink. | activity_type_name  
destination  
error_code  
error_detail  
log_entity_id  
log_filter  
sink_id | ERROR  
logging.googleapis.com%2Fmetric_throttled | metric | Informs customer that a metric associated with Logs-based metrics is being throttled. | activity_type_name  
dropped_labels  
label_cardinalities  
limit_type  
metric_name  
user_cardinality | WARNING  
  
### Memorystore

Logging API service name: `memorystore.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
memorystore.googleapis.com%2Flog_stream | memorystore.googleapis.com/Instance | [type.googleapis.com/google.logging.v2.LogEntry](https://github.com/googleapis/googleapis/blob/master/google/logging/v2/log_entry.proto) | CONSUMER_PROJECT  
INSTANCE_ID | INFO  
WARNING  
ERROR  
memorystore.googleapis.com%2Fclh | generic_task | Log stream for clh | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
memorystore.googleapis.com%2Fagents | saas_instance | Log stream for agents | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
memorystore.googleapis.com%2Finstance_agent | saas_instance | Log stream for instance_agent | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Network Analyzer

Logging API service name: `networkanalyzer.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
networkanalyzer.googleapis.com%2Fanalyzer_reports | networking.googleapis.com/Location | [type.googleapis.com/google.cloud.networkanalyzer.logging.v1.Report](https://github.com/googleapis/googleapis/blob/master/google/cloud/networkanalyzer/logging/v1/analyzer_log.proto) | N/A | DEFAULT  
  
### Network Services API

Logging API service name: `networkservices.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
networkservices.googleapis.com%2Fmesh_events | mesh | A simple JSON payload containing a single 'description' field with event details. | N/A | ERROR  
INFO  
  
### Partner Data Ingestion

Logging API service name: `partnerdataingestion.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
partnerdataingestion.googleapis.com%2Fingest_details | consumed_api | [type.googleapis.com/google.search.partnerdataingestion.logging.v1.IngestDetailsLog](https://github.com/googleapis/googleapis/blob/master/google/search/partnerdataingestion/logging/v1/platformlog.proto) | N/A | INFO  
  
### Pub/Sub

Logging API service name: `pubsub.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
pubsub.googleapis.com%2Fingestion_failures | pubsub_topic | [type.googleapis.com/google.pubsub.v1.IngestionFailureEvent](https://github.com/googleapis/googleapis/blob/master/google/pubsub/v1/pubsub.proto) | N/A | WARNING  
  
### Recommender API

Logging API service name: `recommender.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
recommender.googleapis.com%2Factions | recommender | v1: [type.googleapis.com/google.cloud.recommender.logging.v1.ActionLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/recommender/logging/v1/action_log.proto)  
v1beta1: [type.googleapis.com/google.cloud.recommender.logging.v1beta1.ActionLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/recommender/logging/v1beta1/action_log.proto) | N/A | INFO  
recommender.googleapis.com%2Factions | recommender_insight_type | v1: [type.googleapis.com/google.cloud.recommender.logging.v1.InsightActionLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/recommender/logging/v1/action_log.proto)  
v1beta1: [type.googleapis.com/google.cloud.recommender.logging.v1beta1.InsightActionLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/recommender/logging/v1beta1/action_log.proto) | N/A | INFO  
  
### SaaS Lifecycle Management

Logging API service name: `saasmanagement.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
saasmanagement.googleapis.com%2Fterraform_internal | saasmanagement.googleapis.com/Instance | [type.googleapis.com/google.cloud.saasaccelerator.management.logs.v1.InstanceEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto) | resource_project_number | DEBUG  
ERROR  
INFO  
  
### SaaS Runtime

Logging API service name: `saasservicemgmt.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
saasservicemgmt.googleapis.com%2Fdeployment_events | saasservicemgmt.googleapis.com/Unit | [type.googleapis.com/google.cloud.saasplatform.saasservicemgmt.logging.v1.UnitOperationLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/saasplatform/saasservicemgmt/logging/v1/unit_operation_log.proto) | unit_kind_id  
saas_id  
rollout_id  
tenant_id  
release_id  
saassvcmgmt_correlation_id | INFO  
DEBUG  
ERROR  
saasservicemgmt.googleapis.com%2Frollout_events | saasservicemgmt.googleapis.com/Rollout | [type.googleapis.com/google.cloud.saasplatform.saasservicemgmt.logging.v1.RolloutLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/saasplatform/saasservicemgmt/logging/v1/rollout_log.proto) | unit_kind_id  
saas_id  
release_id | INFO  
DEBUG  
ERROR  
  
### Secret Manager API

Logging API service name: `secretmanager.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
secretmanager.googleapis.com%2Fsecret_event | secretmanager.googleapis.com/Secret | [type.googleapis.com/google.cloud.secretmanager.logging.v1.SecretEvent](https://github.com/googleapis/googleapis/blob/master/google/cloud/secretmanager/logging/v1/secret_event.proto) | N/A | DEFAULT  
DEBUG  
INFO  
NOTICE  
WARNING  
ERROR  
CRITICAL  
ALERT  
EMERGENCY  
  
### Sensitive Actions Service

Logging API service name: `sensitiveaction.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
sensitiveaction.googleapis.com%2Faction | sensitiveaction.googleapis.com/Location | [type.googleapis.com/google.cloud.sensitiveaction.logging.v1.SensitiveAction](https://github.com/googleapis/googleapis/blob/master/google/cloud/sensitiveaction/logging/v1/sensitive_action_payload.proto) | N/A | NOTICE  
  
### Serial Console

Logging API service name: `serialconsole.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
serialconsole.googleapis.com%2Fserial_port_1_output | gce_instance | A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes them useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues. | compute.googleapis.com/resource_name  
is_text_escaped | INFO  
DEBUG  
serialconsole.googleapis.com%2Fserial_port_2_output | gce_instance | A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes them useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues. | compute.googleapis.com/resource_name  
is_text_escaped | INFO  
DEBUG  
serialconsole.googleapis.com%2Fserial_port_3_output | gce_instance | A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes them useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues. | compute.googleapis.com/resource_name  
is_text_escaped | INFO  
DEBUG  
serialconsole.googleapis.com%2Fserial_port_4_output | gce_instance | A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes them useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues. | compute.googleapis.com/resource_name  
is_text_escaped | INFO  
DEBUG  
serialconsole.googleapis.com%2Fserial_port_debug_output | gce_instance | A virtual machine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes them useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues. | compute.googleapis.com/resource_name  
is_text_escaped | INFO  
DEBUG  
  
### Storage Transfer

Logging API service name: `storagetransfer.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
storagetransfer.googleapis.com%2Ftransfer_activity | storage_transfer_job | [type.googleapis.com/google.storagetransfer.logging.TransferActivityLog](https://github.com/googleapis/googleapis/blob/master/google/storagetransfer/logging/transfer_activity_log.proto) | namespace  
log_type  
feed_id | INFO  
WARNING  
ERROR  
  
### Traffic Director

Logging API service name: `trafficdirector.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
trafficdirector.googleapis.com%2Fevents | gce_network | [type.googleapis.com/google.networking.trafficdirector.type.TrafficDirectorLogEntry](https://github.com/googleapis/googleapis/blob/master/google/networking/trafficdirector/type/traffic_director_log_entry.proto) | N/A | ERROR  
INFO  
WARNING  
trafficdirector.googleapis.com%2Fevents | gateway_scope | [type.googleapis.com/google.networking.trafficdirector.type.TrafficDirectorLogEntry](https://github.com/googleapis/googleapis/blob/master/google/networking/trafficdirector/type/traffic_director_log_entry.proto) | N/A | ERROR  
INFO  
trafficdirector.googleapis.com%2Fevents | mesh | [type.googleapis.com/google.networking.trafficdirector.type.TrafficDirectorLogEntry](https://github.com/googleapis/googleapis/blob/master/google/networking/trafficdirector/type/traffic_director_log_entry.proto) | N/A | ERROR  
INFO  
  
### Vertex AI API

Logging API service name: `aiplatform.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
aiplatform.googleapis.com%2Fpipeline_job_events | aiplatform.googleapis.com/PipelineJob | [type.googleapis.com/google.cloud.aiplatform.logging.PipelineJobLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/aiplatform/logging/pipeline_job.proto) | network  
pipeline_name  
pipeline_type  
service_account  
template_metadata_version  
template_uri  
vertex-ai-pipelines-run-billing-id  
vertex_pipeline_system_label_propagate_labels | ERROR  
INFO  
aiplatform.googleapis.com%2Fpipeline_job_task_events | aiplatform.googleapis.com/PipelineJob | [type.googleapis.com/google.cloud.aiplatform.logging.PipelineJobTaskLogEntry](https://github.com/googleapis/googleapis/blob/master/google/cloud/aiplatform/logging/pipeline_job.proto) | custom_job_id  
network  
pipeline_name  
schedule_name  
service_account  
template_metadata_version  
template_uri  
vertex-ai-pipelines-run-billing-id  
vertex_pipeline_system_label_propagate_labels | ERROR  
INFO  
  
### Web Security Scanner API

Logging API service name: `websecurityscanner.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
websecurityscanner.googleapis.com%2Fscan_activity | security_scanner_scan_config | [type.googleapis.com/google.cloud.websecurityscanner.v1.ScanRunLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/websecurityscanner/v1/scan_run_log.proto) | N/A | ERROR  
WARNING  
INFO  
  
### Workflows

Logging API service name: `workflows.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
workflows.googleapis.com%2Fengine_call | workflows.googleapis.com/Workflow | [type.googleapis.com/google.cloud.workflows.type.EngineCallLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/workflows/type/engine_call.proto) | workflows.googleapis.com/execution_id  
workflows.googleapis.com/revision_id | DEBUG  
workflows.googleapis.com%2Fexecutions_system | workflows.googleapis.com/Workflow | [type.googleapis.com/google.cloud.workflows.type.ExecutionsSystemLog](https://github.com/googleapis/googleapis/blob/master/google/cloud/workflows/type/executions_system.proto) | workflows.googleapis.com/execution_id  
workflows.googleapis.com/revision_id | INFO  
ERROR  
  
### reCAPTCHA Enterprise

Logging API service name: `recaptchaenterprise.googleapis.com`

Log ID | Monitored resource | Payload | Labels | Severities  
---|---|---|---|---  
recaptchaenterprise.googleapis.com%2Fassessment | recaptchaenterprise.googleapis.com/Key | [type.googleapis.com/google.cloud.recaptchaenterprise.v1.Assessment](https://github.com/googleapis/googleapis/blob/master/google/cloud/recaptchaenterprise/v1/recaptchaenterprise.proto) | N/A | DEFAULT  
ERROR  
recaptchaenterprise.googleapis.com%2Fannotation | recaptchaenterprise.googleapis.com/Key | [type.googleapis.com/google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest](https://github.com/googleapis/googleapis/blob/master/google/cloud/recaptchaenterprise/v1/recaptchaenterprise.proto) | N/A | DEFAULT  
ERROR  
  
## Understand and manage platform logs

The following sections provide basic information about using and managing platform logs in Cloud Logging.

### Log entry structure

Cloud Logging represents logs using a single data type, `LogEntry`, which defines certain common data for all log entries as well as the payloads that Google Cloud services can include. For detailed information about the contents of log entries, see the Logging API reference for the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) type.

The index of platform logs highlights the following characteristics of log entries:

  * **Log ID** : The URL-encoded identifier within `logName`. For example, if the broader log name is `organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity`, then the log ID is `cloudresourcemanager.googleapis.com%2Factivity`.

Note that if the log ID string in a log entry's `logName` field is prefixed by `serviceName.googleapis.com`, it is a Google Cloud platform log entry.

  * **Monitored resource** : The resource from which the log entry originated. This consists of a resource type from the [Monitored resource list](https://docs.cloud.google.com/logging/docs/api/v2/resource-list) and additional label values that identify a specific instance.

  * **Payload** : The log entry payload, which can be represented as `textPayload` or `jsonPayload`.




### View logs

There are several ways to view your platform log entries:

  * To read log entries using the Google Cloud console, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * To read log entries through the Logging API, see the [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.
  * To read log entries using the Google Cloud CLI, see [Reading log entries](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#reading_log_entries).



### Route logs

You can control how your log entries are routed and stored. The Log Router checks each log entry against existing rules to determine which log entries to discard, which log entries to store in Cloud Logging, and which log entries to include in exports to other destinations.

For details, see [Routing and storage overview: Log Router](https://docs.cloud.google.com/logging/docs/routing/overview#log-router).

### Logs retention

Log entries are stored in Logging buckets for a specified length of time and are then deleted. For more information, see [Logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
