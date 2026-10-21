---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nutanix-prism/
title: Collect Nutanix Prism Central logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:42:55.479880+00:00
---

# Collect Nutanix Prism Central logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nutanix-prism/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nutanix Prism Central logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Nutanix Prism Central logs to Google Security Operations using Bindplane. Nutanix Prism Central is a centralized management platform for Nutanix hyperconverged infrastructure clusters. It provides a unified view for monitoring, managing, and automating operations across multiple Nutanix clusters, including VM lifecycle management, capacity planning, and security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Nutanix Prism Central web console with administrator or Prism Admin role.



## Get Google SecOps ingestion authentication file

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/nutanix_prism:
                 compression: gzip
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 customer_id: '<CUSTOMER_ID>'
                 endpoint: malachiteingestion-pa.googleapis.com
                 log_type: NUTANIX_PRISM
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/nutanix_prism_to_chronicle:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/nutanix_prism
         



  * Replace the **port** and **IP address** as required in your infrastructure.
  * Replace **`<CUSTOMER_ID>`** with the actual customer ID.
  * Update **`/path/to/ingestion-authentication-file.json`** to the path where the authentication file was saved.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure syslog forwarding on Nutanix Prism Central

### Configure remote syslog server

  1. Sign in to the **Nutanix Prism Central** web console.
  2. Click the **gear icon** (Settings) in the top-right corner.
  3. In the **Settings** panel, scroll down and select **Syslog Server** under the **Monitoring and Logging** section.
  4. Click **\+ Configure Syslog Server**.
  5. In the **Server Name** field, enter a descriptive name (for example, `Bindplane-SecOps`).
  6. In the **IP Address** field, enter the IP address of the Bindplane agent host.
  7. In the **Port** field, enter `514` (or your configured port).
  8. In the **Transport Protocol** dropdown, select **UDP**.
  9. Click **Save**.



### Configure log modules

  1. After adding the syslog server, click on the server entry `Bindplane-SecOps`.
  2. Click **\+ Add Module** to configure which log types to forward.
  3. Add the following modules according to your requirements: 
     * **AUDIT** : Captures user authentication events, configuration changes, and API activity.
     * **API_AUDIT** : Captures all REST API calls to Prism Central.
     * **FLOW** : Captures network microsegmentation flow logs (if Flow is enabled).
     * **MICROSEG** : Captures microsegmentation policy events.
  4. For each module: 
     1. Select the **Module** from the dropdown.
     2. Set the **Log Level** to **INFO** or your desired level (recommended: **INFO** for comprehensive logging).
     3. Click **Save**.



### Configure syslog on individual Prism Element clusters (optional)

If you also need logs from individual Prism Element clusters:

  1. Sign in to the **Prism Element** web console for the specific cluster.
  2. Click the **gear icon** (Settings).
  3. Go to **Syslog Server** under the **Monitoring and Logging** section.
  4. Click **\+ Configure Syslog Server**.
  5. Enter the same Bindplane agent details: 
     * **Server Name** : Enter `Bindplane-SecOps`.
     * **IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Transport Protocol** : Select **UDP**.
  6. Click **Save**.
  7. Add modules (**AUDIT** , **HARDWARE** , **STORAGE** , **HYPERVISOR**) as needed.



For more information, see [Nutanix Prism Central syslog documentation](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide:mul-syslog-server-pc-c.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`audit_log` | `about` | Mapped: `true` → `about`  
`audit_log` | `about.labels` | Mapped values (5 total, e.g. `true` → `labels_syscall`, `true` → `labels_data`, `true` → `la...  
`labels_arch` | `about.labels` | Merged  
`labels_data` | `about.labels` | Merged  
`labels_devmajor` | `about.labels` | Merged  
`labels_devminor` | `about.labels` | Merged  
`labels_syscall` | `about.labels` | Merged  
`audit_log` | `additional.fields` | Mapped: `false` → `originating_id`, `false` → `sessionId_label`, `false` → `source_file_label`  
`creation_time_usecs_label` | `additional.fields` | Merged  
`curr_range_idx_label` | `additional.fields` | Merged  
`deserialization_in_progress_label` | `additional.fields` | Merged  
`done_callback_set_label` | `additional.fields` | Merged  
`is_arena_enabled_label` | `additional.fields` | Merged  
`last_rpc_time_usecs_label` | `additional.fields` | Merged  
`line_number_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped: `pam_unix` → `pam_module_label`, `pam_unix` → `pam_submodule_label`  
`num_rpcs_before_stateful_scans_got_enabled_label` | `additional.fields` | Merged  
`nutanix_scan_keys_label` | `additional.fields` | Merged  
`originating_id` | `additional.fields` | Merged  
`pam_module_label` | `additional.fields` | Merged  
`pam_submodule_label` | `additional.fields` | Merged  
`prefetch_error_label` | `additional.fields` | Merged  
`prefetch_hits_label` | `additional.fields` | Merged  
`prefetch_in_progress_label` | `additional.fields` | Merged  
`prefetch_stopped_label` | `additional.fields` | Merged  
`processed_data_size_label` | `additional.fields` | Merged  
`sessionId_label` | `additional.fields` | Merged  
`source_file_label` | `additional.fields` | Merged  
`thread_name_label` | `additional.fields` | Merged  
`total_data_read_bytes_label` | `additional.fields` | Merged  
`total_deserialization_time_usecs_label` | `additional.fields` | Merged  
`total_rows_read_label` | `additional.fields` | Merged  
`total_rpc_time_usecs_label` | `additional.fields` | Merged  
`total_rpcs_done_label` | `additional.fields` | Merged  
`total_scan_time_label` | `additional.fields` | Merged  
`unprocessed_data_size_label` | `additional.fields` | Merged  
`use_chakrdb_backend_label` | `additional.fields` | Merged  
`vblocks_label` | `additional.fields` | Merged  
`vdisk_id_label` | `additional.fields` | Merged  
`audit_log` | `extensions.auth.type` | Mapped: `false` → `AUTHTYPE_UNSPECIFIED`, `true` → `MACHINE`, `true` → `AUTHTYPE_UNSPECIFIED`  
`audit_log_type` | `extensions.auth.type` | Mapped values (6 total, e.g. `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHAN...  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`audit_log` | `intermediary` | Mapped: `false` → `intermediary`, `false` → `logstash1`, `true` → `intermediary`  
`logstash1` | `intermediary` | Merged  
`dvc` | `intermediary.hostname` | Renamed/mapped  
`header_host` | `intermediary.hostname` | Directly mapped  
`logstash.ingest.host` | `intermediary.hostname` | Directly mapped  
`defaultMsg` | `metadata.description` | Mapped when `audit_log` == `false`  
`description` | `metadata.description` | Mapped when `api_call_message` != ``  
`msg2` | `metadata.description` | Directly mapped  
`logstash.collect.timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS`  
`logstash.ingest.timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS`  
`logstash.process.timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS`  
`metadata_ingested_timestamp` | `metadata.event_timestamp` | Parsed as `UNIX`  
`timestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`audit_log` | `metadata.event_type` | Mapped values (30 total, e.g. `false` → `GENERIC_EVENT`, `false` → `USER_LOGIN`, `false` → `...  
`audit_log_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `STATUS_UPDATE`, `true` → `GENERIC_EVENT`  
`has_principal_id` | `metadata.event_type` | Mapped: `false` → `GENERIC_EVENT`, `true` → `SETTING_MODIFICATION`, `true` → `PROCESS_LAUNCH`  
`http_method` | `metadata.event_type` | Mapped: `GET` → `USER_RESOURCE_ACCESS`, `POST` → `RESOURCE_CREATION`, `"PATCH","UPDATE"` → `...  
`audit_log_type` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`operation` | `metadata.product_event_type` | Mapped when `api_call_message` != ``  
`operationType` | `metadata.product_event_type` | Mapped when `audit_log` == `false`  
`pam_message` | `metadata.product_event_type` | Mapped when `message` =~ `pam_unix`  
`program` | `metadata.product_event_type` | Mapped when `audit_log` == `false`  
`entity_uuid` | `metadata.product_log_id` | Mapped when `audit_log` == `false`  
`uuid` | `metadata.product_log_id` | Mapped when `audit_log` == `false`  
`audit_log` | `metadata.product_name` | Mapped: `true` → `Nutanix_Prism`  
`api_version` | `metadata.product_version` | Mapped when `audit_log` == `false`  
`audit_log` | `metadata.vendor_name` | Mapped: `true` → `Nutanix_Prism`  
`audit_log` | `network.application_protocol` | Mapped: `true` → `SSH`  
`audit_log_type` | `network.application_protocol` | Mapped: `CRYPTO_SESSION` → `SSH`  
`audit_log` | `network.direction` | Mapped: `true` → `OUTBOUND`, `true` → `INBOUND`  
`audit_log_type` | `network.direction` | Mapped: `CRYPTO_SESSION` → `OUTBOUND`, `CRYPTO_SESSION` → `INBOUND`  
`direction` | `network.direction` | Mapped: `from-client` → `OUTBOUND`, `from-server` → `INBOUND`  
`http_method` | `network.http.method` | Mapped when `audit_log` == `false`  
`audit_log` | `network.ip_protocol` | Mapped values (6 total, e.g. `false` → `UDP`, `false` → `TCP`, `true` → `IP6IN4`)  
`audit_log_type` | `network.ip_protocol` | Mapped: `CRYPTO_SESSION` → `TCP`  
`audit_log` | `network.sent_bytes` | Mapped: `true` → `uinteger`  
`audit_log_type` | `network.sent_bytes` | Mapped: `CRYPTO_SESSION` → `uinteger`  
`ksize` | `network.sent_bytes` | Directly mapped  
`ses` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`cipher` | `network.tls.cipher` | Directly mapped  
`pfs` | `network.tls.curve` | Directly mapped  
`agent.type` | `observer.application` | Mapped when `audit_log` == `false`  
`agent.id` | `observer.asset_id` | Mapped when `audit_log` == `false`  
`agent.type` | `observer.asset_id` | Mapped when `audit_log` == `false`  
`audit_log` | `observer.ip` | Mapped: `false` → `collect_ip`  
`collect_ip` | `observer.ip` | Merged  
`agent.version` | `observer.platform_version` | Mapped when `audit_log` == `false`  
`application` | `principal.application` | Mapped when `application` != ``  
`comm` | `principal.application` | Directly mapped  
`terminal` | `principal.application` | Directly mapped  
`audit_log` | `principal.asset.attribute.labels` | Mapped: `true` → `token_new`  
`token_new` | `principal.asset.attribute.labels` | Merged  
`audit_log` | `principal.asset.hardware` | Mapped: `false` → `hardware`  
`hardware` | `principal.asset.hardware` | Merged  
`hostname` | `principal.asset.hostname` | Mapped when `hostname` != ``  
`principal_hostname` | `principal.asset.hostname` | Directly mapped  
`syslog_host` | `principal.asset.hostname` | Mapped when `audit_log` == `false`  
`audit_log` | `principal.asset.ip` | Mapped: `false` → `clientIp`, `false` → `src_ip`, `false` → `ip`  
`clientIp` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`replica_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`host.id` | `principal.asset_id` | Mapped when `audit_log` == `false`  
`target.group` | `principal.group` | Renamed/mapped  
`audit_log` | `principal.group.attribute.labels` | Mapped: `true` → `labels_inode_gid`  
`labels_inode_gid` | `principal.group.attribute.labels` | Merged  
`hostname` | `principal.hostname` | Directly mapped  
`principal_asset_hostname` | `principal.hostname` | Directly mapped  
`syslog_host` | `principal.hostname` | Mapped when `audit_log` == `false`  
`addr` | `principal.ip` | Merged  
`audit_log` | `principal.ip` | Mapped values (6 total, e.g. `false` → `clientIp`, `false` → `src_ip`, `false` → `ip`)  
`audit_log_type` | `principal.ip` | Mapped: `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHANGE", "USER_START", "U...  
`clientIp` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`laddr` | `principal.ip` | Merged  
`replica_ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`audit_log` | `principal.labels` | Mapped: `false` → `irmsite`, `false` → `irmregion`, `false` → `irmenvironment`, `false` → `c...  
`clienttype` | `principal.labels` | Merged  
`irmenvironment` | `principal.labels` | Merged  
`irmregion` | `principal.labels` | Merged  
`irmsite` | `principal.labels` | Merged  
`audit_log` | `principal.mac` | Mapped: `false` → `mac`, `true` → `formatted_mac_addr`  
`formatted_mac_addr` | `principal.mac` | Merged  
`mac` | `principal.mac` | Merged  
`audit_log` | `principal.platform` | Mapped values (5 total, e.g. `false` → `LINUX`, `false` → `WINDOWS`, `false` → `MAC`)  
`host.os.kernel` | `principal.platform_patch_level` | Mapped when `audit_log` == `false`  
`host.os.version` | `principal.platform_version` | Mapped when `audit_log` == `false`  
`rport` | `principal.port` | Directly mapped  
`src_port` | `principal.port` | Mapped when `audit_log` == `false`  
`cgroup` | `principal.process.file.full_path` | Directly mapped  
`process_name` | `principal.process.file.names` | Merged  
`target.process.parent_process.pid` | `principal.process.parent_process.pid` | Renamed/mapped  
`princ_pid` | `principal.process.pid` | Mapped when `audit_log` == `false`  
`process_id` | `principal.process.pid` | Mapped when `process_id` != ``  
`spid` | `principal.process.pid` | Directly mapped  
`target.process.pid` | `principal.process.pid` | Renamed/mapped  
`target.user` | `principal.user` | Renamed/mapped  
`audit_log` | `principal.user.attribute.labels` | Mapped: `true` → `labels_inode_uid`  
`labels_inode_uid` | `principal.user.attribute.labels` | Merged  
`acct` | `principal.user.user_display_name` | Directly mapped  
`userName` | `principal.user.user_display_name` | Mapped when `audit_log` == `false`  
`user_id` | `principal.user.user_display_name` | Mapped when `audit_log` == `false`  
`pam_principal_uid` | `principal.user.userid` | Mapped when `message` =~ `pam_unix`  
`suid` | `principal.user.userid` | Directly mapped  
`uid` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Mapped when `audit_log` == `false`  
`audit_log` | `security_result` | Mapped: `false` → `security_result`, `true` → `security_result`  
`audit_log` | `security_result.about.labels` | Mapped: `true` → `labels_list`  
`labels_list` | `security_result.about.labels` | Merged  
`action` | `security_result.action` | Merged  
`audit_log` | `security_result.action` | Mapped: `true` → `security_action`, `true` → `action`  
`audit_log_type` | `security_result.action` | Mapped: `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHANGE", "USER_START", "U...  
`res` | `security_result.action` | Mapped: `success` → `security_action`  
`security_action` | `security_result.action` | Merged  
`res` | `security_result.action_details` | Directly mapped  
`alertuid` | `security_result.detection_fields` | Merged  
`audit_log` | `security_result.detection_fields` | Mapped values (7 total, e.g. `false` → `entity_type`, `false` → `entity_name`, `false` → `en...  
`detection_fields_key` | `security_result.detection_fields` | Merged  
`entity_name` | `security_result.detection_fields` | Merged  
`entity_type` | `security_result.detection_fields` | Merged  
`entity_uuid` | `security_result.detection_fields` | Merged  
`labels_saddr` | `security_result.detection_fields` | Merged  
`labels_sig` | `security_result.detection_fields` | Merged  
`audit_log` | `security_result.severity` | Mapped values (5 total, e.g. `false` → `CRITICAL`, `false` → `ERROR`, `false` → `HIGH`)  
`log_level` | `security_result.severity` | Mapped: `"EMERGENCY","ALERT","CRITICAL"` → `CRITICAL`, `WARNING` → `HIGH`, `NOTICE` → `MEDIU...  
`audit_log` | `security_result.summary` | Mapped: `true` → `systemcall was successful`, `true` → `systemcall was failed`  
`op` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Directly mapped  
`res` | `security_result.summary` | Directly mapped  
`success` | `security_result.summary` | Mapped: `(?i)yes` → `systemcall was successful`, `(?i)no` → `systemcall was failed`  
`summary` | `security_result.summary` | Directly mapped  
`name` | `src.file.full_path` | Directly mapped  
`src` | `src.ip` | Renamed/mapped  
`terminal` | `target.application` | Directly mapped  
`audit_log` | `target.asset.attribute.labels` | Mapped: `true` → `token_new`  
`token_new` | `target.asset.attribute.labels` | Merged  
`audit_log` | `target.asset.attribute.permissions` | Mapped: `true` → `permissions`  
`permissions` | `target.asset.attribute.permissions` | Merged  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`audit_log` | `target.asset.ip` | Mapped: `false` → `ip`  
`ip` | `target.asset.ip` | Merged  
`full_path` | `target.file.full_path` | Directly mapped  
`name` | `target.file.full_path` | Directly mapped  
`path` | `target.file.full_path` | Directly mapped  
`filetype` | `target.file.mime_type` | Directly mapped  
`audit_log` | `target.group` | Mapped: `true` → `principal.group`  
`audit_log_type` | `target.group` | Mapped values (8 total, e.g. `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHAN...  
`audit_log` | `target.group.attribute.labels` | Mapped values (12 total, e.g. `true` → `labels_new_gid`, `true` → `labels_NEW_GID`, `true` →...  
`labels_EGID` | `target.group.attribute.labels` | Merged  
`labels_FSGID` | `target.group.attribute.labels` | Merged  
`labels_NEW_GID` | `target.group.attribute.labels` | Merged  
`labels_OBJ_GID` | `target.group.attribute.labels` | Merged  
`labels_OGID` | `target.group.attribute.labels` | Merged  
`labels_SGID` | `target.group.attribute.labels` | Merged  
`labels_egid` | `target.group.attribute.labels` | Merged  
`labels_fsgid` | `target.group.attribute.labels` | Merged  
`labels_new_gid` | `target.group.attribute.labels` | Merged  
`labels_obj_gid` | `target.group.attribute.labels` | Merged  
`labels_ogid` | `target.group.attribute.labels` | Merged  
`labels_sgid` | `target.group.attribute.labels` | Merged  
`group_display_name` | `target.group.group_display_name` | Directly mapped  
`id` | `target.group.product_object_id` | Directly mapped  
`product_object_id` | `target.group.product_object_id` | Directly mapped  
`hostname` | `target.hostname` | Directly mapped  
`target_asset_hostname` | `target.hostname` | Directly mapped  
`addr` | `target.ip` | Merged  
`audit_log` | `target.ip` | Mapped: `false` → `ip`, `true` → `addr`  
`audit_log_type` | `target.ip` | Mapped: `CRYPTO_SESSION` → `addr`  
`ip` | `target.ip` | Merged  
`audit_log` | `target.labels` | Mapped: `true` → `labels_ter`, `true` → `labels_tty`, `true` → `labels_exit`, `true` → `labe...  
`labels_exit` | `target.labels` | Merged  
`labels_subj` | `target.labels` | Merged  
`labels_ter` | `target.labels` | Merged  
`labels_tty` | `target.labels` | Merged  
`audit_log` | `target.mac` | Mapped: `false` → `mac`  
`mac` | `target.mac` | Merged  
`lport` | `target.port` | Directly mapped  
`args` | `target.process.command_line` | Directly mapped  
`command_line` | `target.process.command_line` | Directly mapped  
`ocomm` | `target.process.command_line` | Directly mapped  
`exe` | `target.process.file.full_path` | Directly mapped  
`audit_log` | `target.process.parent_process.pid` | Mapped: `true` → `principal.process.parent_process.pid`  
`audit_log_type` | `target.process.parent_process.pid` | Mapped: `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHANGE", "USER_START", "U...  
`ppid` | `target.process.parent_process.pid` | Directly mapped  
`audit_log` | `target.process.pid` | Mapped: `true` → `principal.process.pid`  
`audit_log_type` | `target.process.pid` | Mapped: `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHANGE", "USER_START", "U...  
`opid` | `target.process.pid` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`audit_log` | `target.resource.attribute.labels` | Mapped: `true` → `labels_mem`, `true` → `labels_vcpu`, `true` → `labels_olh`, `true` → `labe...  
`block_number_label` | `target.resource.attribute.labels` | Merged  
`labels_mem` | `target.resource.attribute.labels` | Merged  
`labels_olh` | `target.resource.attribute.labels` | Merged  
`labels_oll` | `target.resource.attribute.labels` | Merged  
`labels_vcpu` | `target.resource.attribute.labels` | Merged  
`partition_id_label` | `target.resource.attribute.labels` | Merged  
`snapshot_chain_id_label` | `target.resource.attribute.labels` | Merged  
`transaction_id_label` | `target.resource.attribute.labels` | Merged  
`admin_permission_1` | `target.resource.attribute.permissions` | Merged  
`admin_permission_2` | `target.resource.attribute.permissions` | Merged  
`admin_permission_3` | `target.resource.attribute.permissions` | Merged  
`audit_log` | `target.resource.attribute.permissions` | Mapped values (9 total, e.g. `true` → `admin_permission_1`, `true` → `admin_permission_2`, `...  
`group_permission_1` | `target.resource.attribute.permissions` | Merged  
`group_permission_2` | `target.resource.attribute.permissions` | Merged  
`group_permission_3` | `target.resource.attribute.permissions` | Merged  
`others_permission_1` | `target.resource.attribute.permissions` | Merged  
`others_permission_2` | `target.resource.attribute.permissions` | Merged  
`others_permission_3` | `target.resource.attribute.permissions` | Merged  
`exe` | `target.resource.name` | Directly mapped  
`new-disk` | `target.resource.name` | Directly mapped  
`obj` | `target.resource.name` | Directly mapped  
`params.vm_name` | `target.resource.name` | Mapped when `audit_log` == `false`  
`vm` | `target.resource.name` | Directly mapped  
`inode` | `target.resource.product_object_id` | Directly mapped  
`audit_log` | `target.resource.resource_type` | Mapped: `true` → `SETTING`  
`audit_log_type` | `target.resource.resource_type` | Mapped: `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHANGE", "USER_START", "U...  
`rest_endpoint` | `target.url` | Mapped when `audit_log` == `false`  
`audit_log` | `target.user` | Mapped: `true` → `principal.user`  
`audit_log_type` | `target.user` | Mapped values (8 total, e.g. `"SYSCALL", "LOGIN", "USER_LOGIN", "USER_ACCT", "USER_ROLE_CHAN...  
`audit_log` | `target.user.attribute.labels` | Mapped values (15 total, e.g. `true` → `labels_auid`, `true` → `labels_AUID`, `true` → `labe...  
`labels_AUID` | `target.user.attribute.labels` | Merged  
`labels_EUID` | `target.user.attribute.labels` | Merged  
`labels_FSUID` | `target.user.attribute.labels` | Merged  
`labels_OAUID` | `target.user.attribute.labels` | Merged  
`labels_OUID` | `target.user.attribute.labels` | Merged  
`labels_SUID` | `target.user.attribute.labels` | Merged  
`labels_auid` | `target.user.attribute.labels` | Merged  
`labels_euid` | `target.user.attribute.labels` | Merged  
`labels_fsuid` | `target.user.attribute.labels` | Merged  
`labels_id` | `target.user.attribute.labels` | Merged  
`labels_oauid` | `target.user.attribute.labels` | Merged  
`labels_obj_uid` | `target.user.attribute.labels` | Merged  
`labels_ouid` | `target.user.attribute.labels` | Merged  
`labels_sauid` | `target.user.attribute.labels` | Merged  
`labels_suid` | `target.user.attribute.labels` | Merged  
`audit_log` | `target.user.attribute.roles` | Mapped: `true` → `obj_role`, `true` → `subj_role`  
`obj_role` | `target.user.attribute.roles` | Merged  
`subj_role` | `target.user.attribute.roles` | Merged  
`obj_user` | `target.user.user_display_name` | Directly mapped  
`user_display_name` | `target.user.user_display_name` | Directly mapped  
`id` | `target.user.userid` | Directly mapped  
`pam_target_user` | `target.user.userid` | Mapped when `message` =~ `pam_unix`  
`uid` | `target.user.userid` | Directly mapped  
`userid` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `Nutanix_Prism`  
N/A | `metadata.vendor_name` | Constant: `Nutanix_Prism`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `network.direction` | Constant: `OUTBOUND`  
N/A | `network.ip_protocol` | Constant: `IP6IN4`  
N/A | `principal.platform` | Constant: `LINUX`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
N/A | `security_result.summary` | Constant: `systemcall was successful`  
N/A | `target.group` | Constant: `principal.group`  
N/A | `target.process.parent_process.pid` | Constant: `principal.process.parent_process.pid`  
N/A | `target.process.pid` | Constant: `principal.process.pid`  
N/A | `target.resource.resource_type` | Constant: `SETTING`  
N/A | `target.user` | Constant: `principal.user`  
`header_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`thread_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`line_number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vdisk_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pam_module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pam_submodule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`snapshot_chain_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`partition_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`block_number` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`transaction_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`replica_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`pam_target_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`pam_principal_uid` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`pam_message` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`princ_pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`affectedEntityList" and "alertUid` | `security_result.detection_fields` | Mapped from changelog  
`clientIp" and "params.requested_ip_address` | `principal.ip` | Mapped from changelog  
`originatingClusterUuid" and "sessionId` | `additional.fields` | Mapped from changelog  
`params.mac_address` | `principal.mac` | Mapped from changelog  
`logstash.ingest.host` | `intermediary[0].hostname` | Mapped from changelog  
`logstash.collect.host` | `observer.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nutanix-prism-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
