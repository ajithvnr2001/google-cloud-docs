---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/terraform-enterprise/
title: Collect Terraform Enterprise logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:10.127733+00:00
---

# Collect Terraform Enterprise logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/terraform-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Terraform Enterprise logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Terraform Enterprise logs to Google Security Operations using Google Cloud Storage V2.

Terraform Enterprise (TFE) is a self-hosted infrastructure as code platform that generates application logs containing audit events for workspace operations, policy checks, state changes, and user activity. Audit events are embedded within the TFE application logs and marked with the `[Audit Log]` tag. Because TFE stores these logs locally on the application server, you must export them to a Google Cloud Storage (GCS) bucket and then configure a Google SecOps feed to ingest them.

**Note:** The Audit Trails API is only available for HCP Terraform (Cloud), not for self-hosted Terraform Enterprise. This guide covers TFE application log collection from the self-hosted server.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Administrative access to the Terraform Enterprise server (SSH or console access)
  * Access to TFE application logs on the server file system (typically at `/var/log/terraform-enterprise/` or accessible via `replicatedctl app logs`)



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `terraform-enterprise-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Configure automated export of TFE application logs to GCS

Terraform Enterprise embeds audit log entries within its application logs. Audit events are marked with the `[Audit Log]` string and can be filtered from the application log output. Choose one of the following approaches to automate the export.

### Option 1: TFE log forwarding with Fluent Bit to GCS (recommended)

Terraform Enterprise supports external log forwarding using a built-in Fluent Bit-based mechanism. You can configure TFE to forward application logs to a GCS bucket.

  1. Access the TFE administration console.
  2. Go to **Settings > Logging**.
  3. Enable **External Logging**.
  4. Configure the Fluent Bit output to use the GCS plugin:
         
         [OUTPUT]
             Name                       gcs
             Match                      *
             Bucket                     terraform-enterprise-logs
             Object_key_format          audit-logs/tfe_logs_%Y%m%d_%H%M%S.json
             Content_Type               application/json
         

**Note:** Replace `terraform-enterprise-logs` with your GCS bucket name. The TFE server must have a service account or credentials with **Storage Object Admin** role on the bucket.
  5. Save the configuration and restart the TFE services if prompted.

**Note:** Consult the [Terraform Enterprise log forwarding documentation](https://developer.hashicorp.com/terraform/enterprise/admin/infrastructure/logging) for the full list of supported configuration options and authentication methods.



### Option 2: Compute Engine VM with cron (for direct log collection)

If the TFE server runs on Google Compute Engine or has network connectivity to GCP, configure a cron job on the TFE server to export filtered audit logs to GCS.

  1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) on the TFE server.
  2. Create a service account for the export:

     1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
     2. Click **Create Service Account**.
     3. Provide the following configuration details: 
        * **Service account name** : Enter `tfe-log-export-sa`
        * **Service account description** : Enter `Service account for TFE log export to GCS`
     4. Click **Create and Continue**.
     5. Add the **Storage Object Admin** role.
     6. Click **Done**.
     7. Download a JSON key for the service account and copy it to the TFE server.
  3. Create an export script on the TFE server (`/opt/tfe-export/export_logs.sh`):
         
         #!/usr/bin/env bash
         set -euo pipefail
         
         BUCKET="terraform-enterprise-logs"
         PREFIX="audit-logs"
         LOG_DIR="/var/log/terraform-enterprise"
         EXPORT_DIR="/tmp/tfe-export"
         TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
         
         mkdir -p "$EXPORT_DIR"
         
         # Filter audit log entries from TFE application logs
         grep '\[Audit Log\]' "$LOG_DIR"/*.log > "$EXPORT_DIR/tfe_audit_${TIMESTAMP}.json" 2>/dev/null || true
         
         if [ -s "$EXPORT_DIR/tfe_audit_${TIMESTAMP}.json" ]; then
             gcloud storage cp "$EXPORT_DIR/tfe_audit_${TIMESTAMP}.json" \
                 "gs://${BUCKET}/${PREFIX}/"
             echo "Uploaded tfe_audit_${TIMESTAMP}.json to gs://${BUCKET}/${PREFIX}/"
         else
             echo "No audit log entries found."
         fi
         
         rm -rf "$EXPORT_DIR"
         

**Note:** Replace `terraform-enterprise-logs` with your bucket name. Adjust the `LOG_DIR` path to match your TFE installation. For Docker-based TFE installations, logs may be accessible via `docker logs terraform-enterprise` or `replicatedctl app logs`.
  4. Make the script executable and schedule it with cron:
         
         chmod +x /opt/tfe-export/export_logs.sh
         (crontab -l ; echo "0 * * * * /opt/tfe-export/export_logs.sh >> /var/log/tfe-export.log 2>&1") | crontab -
         




### Option 3: Storage Transfer Service (for file-based log collection)

If TFE logs are written to a file system accessible via a Storage Transfer Agent, use Storage Transfer Service to move them to GCS.

  1. In the **GCP Console** , go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **POSIX filesystem** as the source.
  4. Follow the instructions to install the [Storage Transfer Agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) on the TFE server or a machine with access to the TFE log directory.
  5. Configure the transfer job:

Setting | Value  
---|---  
**Source directory** | Path to TFE log directory (for example, `/var/log/terraform-enterprise/`)  
**Destination bucket** | `terraform-enterprise-logs`  
**Destination path** | `audit-logs/`  
**Schedule** | Set a recurring schedule (for example, every hour)  
  6. Click **Create**.




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Terraform Enterprise Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Terraform Enterprise Audit** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `terraform-enterprise-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure the Google SecOps feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Terraform Enterprise Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Terraform Enterprise Audit** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://terraform-enterprise-logs/audit-logs/
           

       * Replace `terraform-enterprise-logs` with your GCS bucket name.
       * Replace `audit-logs` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action_label` | `additional.fields` | Merged  
`allow_config_generation_label` | `additional.fields` | Merged  
`allow_empty_apply_label` | `additional.fields` | Merged  
`auto_apply_label` | `additional.fields` | Merged  
`can_apply_label` | `additional.fields` | Merged  
`can_cancel_label` | `additional.fields` | Merged  
`can_comment_label` | `additional.fields` | Merged  
`can_discard_label` | `additional.fields` | Merged  
`can_force_cancel_label` | `additional.fields` | Merged  
`can_force_execute_label` | `additional.fields` | Merged  
`can_override_policy_check_label` | `additional.fields` | Merged  
`comments_label` | `additional.fields` | Merged  
`cost_estimated_at_label` | `additional.fields` | Merged  
`cost_estimating_at_label` | `additional.fields` | Merged  
`dd_span_id_label` | `additional.fields` | Merged  
`dd_trace_id_label` | `additional.fields` | Merged  
`has_changes_label` | `additional.fields` | Merged  
`is_cancelable_label` | `additional.fields` | Merged  
`is_confirmable_label` | `additional.fields` | Merged  
`is_destroy_label` | `additional.fields` | Merged  
`is_discardable_label` | `additional.fields` | Merged  
`is_force_cancelable_label` | `additional.fields` | Merged  
`jsonPayload_auth_source_label` | `additional.fields` | Merged  
`jsonPayload_db_label` | `additional.fields` | Merged  
`jsonPayload_dd_env_label` | `additional.fields` | Merged  
`jsonPayload_dd_service_label` | `additional.fields` | Merged  
`jsonPayload_dd_span_id_label` | `additional.fields` | Merged  
`jsonPayload_dd_trace_id_label` | `additional.fields` | Merged  
`jsonPayload_dd_version_label` | `additional.fields` | Merged  
`jsonPayload_ddsource_label` | `additional.fields` | Merged  
`jsonPayload_duration_label` | `additional.fields` | Merged  
`jsonPayload_format_label` | `additional.fields` | Merged  
`jsonPayload_node_id_label` | `additional.fields` | Merged  
`jsonPayload_selinux_context_label` | `additional.fields` | Merged  
`jsonPayload_systemd_cgroup_label` | `additional.fields` | Merged  
`jsonPayload_systemd_slice_label` | `additional.fields` | Merged  
`jsonPayload_view_label` | `additional.fields` | Merged  
`json_image_name_label` | `additional.fields` | Merged  
`json_syslog_identifier_label` | `additional.fields` | Merged  
`json_transport_label` | `additional.fields` | Merged  
`json_uid_label` | `additional.fields` | Merged  
`msg_label` | `additional.fields` | Merged  
`plan_only_label` | `additional.fields` | Merged  
`plan_queueable_at_label` | `additional.fields` | Merged  
`plan_queued_at_label` | `additional.fields` | Merged  
`planned_and_finished_at_label` | `additional.fields` | Merged  
`planned_at_label` | `additional.fields` | Merged  
`planning_at_label` | `additional.fields` | Merged  
`policychecks_label` | `additional.fields` | Merged  
`post_plan_completed_at_label` | `additional.fields` | Merged  
`post_plan_running_at_label` | `additional.fields` | Merged  
`queuing_at_label` | `additional.fields` | Merged  
`refresh_label` | `additional.fields` | Merged  
`refresh_only_label` | `additional.fields` | Merged  
`resource_label` | `additional.fields` | Merged  
`runevents_label` | `additional.fields` | Merged  
`save_plan_label` | `additional.fields` | Merged  
`source_label` | `additional.fields` | Merged  
`source_realtime_timestamp_label` | `additional.fields` | Merged  
`taskstages_label` | `additional.fields` | Merged  
`trigger_reason_label` | `additional.fields` | Merged  
`updated_at_label` | `additional.fields` | Merged  
`uuid_label` | `additional.fields` | Merged  
`data.attributes.created-at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`receiveTimestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`time_stamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`time_zone` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSSSSS+Z.Z`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`, `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`, `true` → `USER_UNCATEGORIZED`  
`type` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`insertId` | `metadata.product_log_id` | Directly mapped  
`data.attributes.terraform-version` | `metadata.product_version` | Directly mapped  
`vault_version` | `metadata.product_version` | Directly mapped  
`logName` | `metadata.url_back_to_product` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`status` | `network.http.response_code` | Renamed/mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`request_id` | `network.session_id` | Directly mapped  
`jsonPayload.machine_id` | `principal.asset.asset_id` | Directly mapped  
`dd_service` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`actor_ip` | `principal.asset.ip` | Merged  
`sha` | `principal.file.sha1` | Directly mapped  
`dd_service` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`jsonPayload.hostname` | `principal.hostname` | Directly mapped  
`src_host` | `principal.hostname` | Directly mapped  
`actor_ip` | `principal.ip` | Merged  
`remote_ip` | `principal.ip` | Merged  
`port` | `principal.port` | Renamed/mapped  
`src_port` | `principal.port` | Renamed/mapped  
`jsonPayload.cap_effective` | `principal.process.access_mask` | Renamed/mapped  
`jsonPayload.cmdline` | `principal.process.command_line` | Directly mapped  
`jsonPayload.exe` | `principal.process.file.full_path` | Directly mapped  
`jsonPayload.comm` | `principal.process.file.names` | Merged  
`jsonPayload.pid` | `principal.process.pid` | Directly mapped  
`jsonPayload_container_tag_label` | `principal.resource.attribute.labels` | Merged  
`jsonPayload.container_id_full` | `principal.resource.product_object_id` | Directly mapped  
`resource_id` | `principal.resource.product_object_id` | Directly mapped  
`resource.type` | `principal.resource.resource_subtype` | Directly mapped  
`auth_impersonator_id_label` | `principal.user.attribute.labels` | Merged  
`client_token_accessor_label` | `principal.user.attribute.labels` | Merged  
`client_token_label` | `principal.user.attribute.labels` | Merged  
`mount_accessor_label` | `principal.user.attribute.labels` | Merged  
`mount_point_label` | `principal.user.attribute.labels` | Merged  
`namespace_id_label` | `principal.user.attribute.labels` | Merged  
`organization_id_label` | `principal.user.attribute.labels` | Merged  
`request_id_label` | `principal.user.attribute.labels` | Merged  
`write_timestamp_label` | `principal.user.attribute.labels` | Merged  
`role` | `principal.user.attribute.roles` | Merged  
`organization` | `principal.user.department` | Merged  
`jsonPayload.gid` | `principal.user.group_identifiers` | Merged  
`auth.entity_id` | `principal.user.product_object_id` | Directly mapped  
`auth.display_name` | `principal.user.user_display_name` | Directly mapped  
`actor` | `principal.user.userid` | Directly mapped  
`auth.accessor_id` | `principal.user.userid` | Directly mapped  
`auth.entity_id` | `principal.user.userid` | Directly mapped  
`request.client_id` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`record.resource.action` | `security_result.action_details` | Directly mapped  
`request.operation` | `security_result.action_details` | Directly mapped  
`data.attributes.status` | `security_result.category_details` | Merged  
`apply_detection_field_id` | `security_result.detection_fields` | Merged  
`apply_detection_field_related` | `security_result.detection_fields` | Merged  
`auth_accessor_label` | `security_result.detection_fields` | Merged  
`auth_client_token_label` | `security_result.detection_fields` | Merged  
`auth_metadata_role_label` | `security_result.detection_fields` | Merged  
`auth_policy_results_allowed_label` | `security_result.detection_fields` | Merged  
`auth_token_type_label` | `security_result.detection_fields` | Merged  
`comments_related_label` | `security_result.detection_fields` | Merged  
`configuration_version_detection_field_id` | `security_result.detection_fields` | Merged  
`configuration_version_detection_field_related` | `security_result.detection_fields` | Merged  
`cost_estimate_detection_field_id` | `security_result.detection_fields` | Merged  
`cost_estimate_detection_field_related` | `security_result.detection_fields` | Merged  
`data_id_label` | `security_result.detection_fields` | Merged  
`data_links_self_label` | `security_result.detection_fields` | Merged  
`detection_fields_organization_id` | `security_result.detection_fields` | Merged  
`id_label` | `security_result.detection_fields` | Merged  
`plan_detection_field_id` | `security_result.detection_fields` | Merged  
`plan_detection_field_related` | `security_result.detection_fields` | Merged  
`policy_checks_related_label` | `security_result.detection_fields` | Merged  
`run_events_related_label` | `security_result.detection_fields` | Merged  
`task_stages_related_label` | `security_result.detection_fields` | Merged  
`token_ttl_label` | `security_result.detection_fields` | Merged  
`workspace_detection_field_id` | `security_result.detection_fields` | Merged  
`jsonPayload.priority` | `security_result.priority_details` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`  
`severity_detail` | `security_result.severity` | Mapped: `(?i)Info` → `INFORMATIONAL`, `(?i)Error` → `ERROR`, `(?i)Warning` → `MEDIUM`  
`request.remote_address` | `target.asset.ip` | Merged  
`target_ip` | `target.asset.ip` | Merged  
`request.remote_address` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`labels_namespace` | `target.namespace` | Directly mapped  
`request.remote_port` | `target.port` | Renamed/mapped  
`labels_location` | `target.resource.attribute.cloud.availability_zone` | Directly mapped  
`region` | `target.resource.attribute.cloud.availability_zone` | Directly mapped  
`provider` | `target.resource.attribute.cloud.environment` | Mapped: `aws` → `AMAZON_WEB_SERVICES`  
`cluster_size_label` | `target.resource.attribute.labels` | Merged  
`cluster_tier_label` | `target.resource.attribute.labels` | Merged  
`hcp_product_label` | `target.resource.attribute.labels` | Merged  
`image_tag_label` | `target.resource.attribute.labels` | Merged  
`instance-id_label` | `target.resource.attribute.labels` | Merged  
`organization_id_label` | `target.resource.attribute.labels` | Merged  
`cluster_id` | `target.resource.name` | Directly mapped  
`jsonPayload.container_name` | `target.resource.name` | Directly mapped  
`name` | `target.resource.name` | Directly mapped  
`record.resource.id` | `target.resource.name` | Directly mapped  
`project_id` | `target.resource.product_object_id` | Directly mapped  
`resource.meta.project_id` | `target.resource.product_object_id` | Directly mapped  
`record.resource.type` | `target.resource.resource_subtype` | Directly mapped  
`target_resource_ancestors` | `target.resource_ancestors` | Merged  
`path` | `target.url` | Directly mapped  
`request.path` | `target.url` | Directly mapped  
`mount_accessor_label` | `target.user.attribute.labels` | Merged  
`mount_class_label` | `target.user.attribute.labels` | Merged  
`mount_point_label` | `target.user.attribute.labels` | Merged  
`mount_running_plugin_version_label` | `target.user.attribute.labels` | Merged  
`mount_type_label` | `target.user.attribute.labels` | Merged  
`replication_cluster_label` | `target.user.attribute.labels` | Merged  
N/A | `metadata.event_type` | Constant: `USER_RESOURCE_ACCESS`  
N/A | `metadata.product_name` | Constant: `TERRAFORM_ENTERPRISE`  
N/A | `metadata.vendor_name` | Constant: `TERRAFORM_ENTERPRISE`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.attribute.cloud.environment` | Constant: `AMAZON_WEB_SERVICES`  
`data.attributes.created-at` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`data.attributes.status` | `event.idm.read_only_udm.security_result.0.category_details` | Mapped from changelog  
`data.attributes.actions.is-cancelable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.actions.is-confirmable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.actions.is-discardable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.actions.is-force-cancelable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.allow-config-generation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.allow-empty-apply` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.auto-apply` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.has-changes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.is-destroy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-apply` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-cancel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-comment` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-discard` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-force-cancel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-force-execute` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.permissions.can-override-policy-check` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.plan-only` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.refresh` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.refresh-only` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.save-plan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.cost-estimated-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.cost-estimating-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.plan-queueable-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.plan-queued-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.planned-and-finished-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.planned-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.planning-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.post-plan-completed-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.post-plan-running-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.status-timestamps.queuing-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.trigger-reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.attributes.updated-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.relationships.run-events.data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.relationships.task-stages.data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.relationships.policy-checks.data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.relationships.comments.data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.relationships.workspace.data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.workspace.data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.apply.data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.apply.data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.apply.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.configuration-version.data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.configuration-version.data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.configuration-version.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.cost-estimate.data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.cost-estimate.data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.cost-estimate.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.plan.data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.plan.data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.plan.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.run-events.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.task-stages.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.policy-checks.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.relationships.comments.links.related` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.links.self` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`jsonPayload.source_realtime_timestamp` | `additional.fields` | Mapped from changelog  
`jsonPayload.container_tag` | `principal.resource.attribute.labels` | Mapped from changelog  
`jsonPayload.uid` | `additional.fields` | Mapped from changelog  
`jsonPayload.transport` | `additional.fields` | Mapped from changelog  
`jsonPayload.syslog_identifier` | `additional.fields` | Mapped from changelog  
`jsonPayload.image_name` | `additional.fields` | Mapped from changelog  
`jsonPayload.image_name` | `target.ip` | Mapped from changelog  
`jsonPayload.image_name` | `target.resource.name` | Mapped from changelog  
`dd.trace_id` | `additional.fields` | Mapped from changelog  
`dd.span_id` | `additional.fields` | Mapped from changelog  
`dd.env` | `additional.fields` | Mapped from changelog  
`dd.service` | `additional.fields` | Mapped from changelog  
`dd.version` | `additional.fields` | Mapped from changelog  
`jsonPayload.systemd_cgroup` | `additional.fields` | Mapped from changelog  
`jsonPayload.systemd_slice` | `additional.fields` | Mapped from changelog  
`jsonPayload.selinux_context` | `additional.fields` | Mapped from changelog  
`resource.labels.location` | `target.resource.attribute.cloud.availability_zone` | Mapped from changelog  
`resource.labels.project_id` | `target.resource_ancestors.product_object_id` | Mapped from changelog  
`resource.labels.namespace` | `target.namespace` | Mapped from changelog  
`resource.labels.node_id` | `additional.fields` | Mapped from changelog  
`receiveTimestamp` | `metadata.collected_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/terraform-enterprise-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
