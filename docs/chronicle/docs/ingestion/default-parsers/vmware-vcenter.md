---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter/
title: Collect VMware vCenter logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:03.265191+00:00
---

# Collect VMware vCenter logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware vCenter logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VMware vCenter logs to Google Security Operations using the Bindplane agent.

VMware vCenter is a server management platform that generates JSON and syslog messages for virtual machine operations, host management, authentication, and configuration changes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the VMware vCenter server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the VMware vCenter Server Management web UI



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/vmware_vcenter:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VMWARE_VCENTER
            raw_log_field: body
        
        service:
          pipelines:
            logs/vmware_vcenter_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vmware_vcenter
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/vmware_vcenter:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VMWARE_VCENTER
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure syslog in VMware vCenter

  1. Sign in to the **vCenter Server Management** web UI.
  2. Go to **Syslog > Forwarding Configuration**.
  3. Click **Configure** to create a new forwarding configuration.
  4. Provide the following configuration details: 
     * **Server address** : Enter the Bindplane agent IP address.
     * **Protocol** : Select **UDP**.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
  5. Click **Save**.
  6. Click **Send Test Message** to verify the configuration.



## UDM mapping table

The following table lists the log-to-UDM field mappings for VMware vCenter logs:

Log field | UDM mapping  
---|---  
`Access Mask` | `principal.process.access_mask`  
`Account Domain` | `principal.administrative_domain`  
`Account Name` | `target.user.userid`  
`AccessControlRuleAction` | `security_result.action`  
`AccessControlRuleName` | `security_result.rule_name`  
`ACPolicy` | `security_result.rule_labels`  
`admin` | `principal.resource.attribute.labels`  
`agent.hostname` | `principal.hostname`,  
`principal.asset.hostname`  
`agent.type` | `observer.application`  
`agent.version` | `intermediary.platform_version`  
`alarm_target` | `about.resource.name`  
`api_call_method` | `metadata.product_event_type`  
`app` | `principal.application`  
`ApplicationProtocol` | `network.application_protocol`  
`appname` | `principal.application`  
`auth_date_time` | `metadata.collected_timestamp`  
`auth_user` | `target.user.userid`  
`Authentication Package` | `security_result.about.resource.name`  
`basedn_group_iden` | `target.user.group_identifiers`  
`bytes_received` | `network.received_bytes`  
`bytes_sent` | `network.sent_bytes`  
`Client` | `target.user.attribute.labels`  
`Client Address` | `principal.ip`  
`Client Port` | `principal.port`  
`client_ip` | `principal.ip`,  
`principal.asset.ip`  
`client_port` | `principal.port`  
`ClientVersion` | `target.platform_version`  
`cmd` | `target.process.command_line`  
`ConnectionID` | `security_result.about.labels`  
`cor_id` | `metadata.product_log_id`  
`data_center` | `target.location.name`  
`datacenter` | `target.location.name`  
`desc` | `metadata.description`  
`description_data` | `metadata.description`  
`dest_ip` | `target.ip`,  
`target.asset.ip`  
`dest_port` | `target.port`  
`DeviceUUID` | `metadata.product_log_id`  
`domain` | `principal.administrative_domain`  
`dstip` | `target.ip`,  
`target.asset.ip`  
`EgressZone` | `target.location.name`  
`error_code` | `security_result.detection_fields`  
`error_message` | `security_result.summary`  
`event_name` | `metadata.product_event_type`  
`eventid` | `metadata.product_event_type`  
`EventPriority` | `security_result.severity`,  
`security_result.severity_details`  
`@fields.company_name` | `principal.user.company_name`  
`@fields.facility` | `principal.resource.resource_subtype`  
`@fields.host` | `principal.hostname`,  
`principal.asset.hostname`  
`@fields.privatecloud_id` | `principal.resource_ancestors.product_object_id`  
`@fields.privatecloud_name` | `principal.resource_ancestors.name`  
`@fields.procid` | `principal.process.pid`  
`@fields.region_id` | `principal.location.country_or_region`  
`file_path` | `target.process.file.full_path`  
`file_type` | `network.http.response_headers`  
`FirstPacketSecond` | `security_result.about.labels`  
`f_path` | `target.file.full_path`  
`function` | `security_result.detection_fields`  
`hmethod` | `network.http.method`  
`host.architecture` | `principal.asset.hardware`  
`host.id` | `observer.asset_id`  
`host.ip` | `principal.ip`,  
`principal.asset.ip`  
`host.mac` | `principal.mac`  
`host.os.kernel` | `principal.platform_patch_level`  
`host.os.platform` | `target.platform`  
`host.os.version` | `principal.platform_version`  
`host_ip` | `principal.ip`,  
`principal.asset.ip`  
`http_method` | `network.http.method`  
`HTTPResponse` | `network.http.response_code`  
`http_version` | `network.tls.version_protocol`  
`i_ip` | `intermediary.ip`,  
`intermediary.asset.ip`  
`i_port` | `intermediary.port`  
`IngressZone` | `principal.location.name`  
`InitiatorBytes` | `network.sent_bytes`  
`InitiatorPackets` | `network.sent_packets`  
`insertId` | `metadata.product_log_id`  
`InstanceId` | `target.asset_id`  
`inter_host_name` | `intermediary.hostname`  
`inter_ip` | `intermediary.ip`  
`inter_port` | `target.port`  
`intermediary_ip` | `intermediary.ip`  
`intermediary_port` | `intermediary.port`  
`ip` | `target.ip`,  
`target.asset.ip`  
`ips` | `principal.ip`,  
`principal.asset.ip`  
`jsonPayload.appname` | `security_result.detection_fields`  
`jsonPayload.facility` | `security_result.detection_fields`  
`jsonPayload.hostname` | `principal.hostname`,  
`principal.asset.hostname`  
`jsonPayload.message` | `security_result.detection_fields`  
`jsonPayload.priority` | `security_result.detection_fields`  
`jsonPayload.version` | `security_result.detection_fields`  
`kv_msg1.cipher` | `network.tls.cipher`  
`kv_msg1.ctladdr` | `intermediary.user.attribute.labels`  
`kv_msg1.daemon` | `security_result.about.labels`  
`kv_msg1.from` | `network.email.from`  
`kv_msg1.get_error` | `intermediary.user.attribute.labels`  
`kv_msg1.msgid` | `network.email.mail_id`  
`kv_msg1.proto` | `security_result.about.labels`  
`kv_msg1.size` | `network.sent_bytes`  
`kv_msg1.stat` | `security_result.summary`  
`kv_msg1.to` | `network.email.to`  
`kv_msg1.verify` | `security_result.description`,  
`security_result.action`  
`kv_msg1.version` | `network.tls.version`  
`labels.log_type` | `metadata.product_event_type`  
`labels.net.host.ip` | `principal.ip`,  
`principal.asset.ip`  
`labels.net.host.port` | `principal.port`  
`labels.net.peer.ip` | `intermediary.ip`,  
`intermediary.asset.ip`,  
`target.ip`,  
`target.asset.ip`  
`labels.net.peer.port` | `intermediary.port`,  
`target.port`  
`labels.net.transport` | `network.ip_protocol`  
`level` | `security_result.severity`,  
`security_result.severity_details`  
`level_name` | `security_result.severity`,  
`security_result.severity_details`  
`local_address_1` | `observer.ip`  
`local_address_2` | `observer.ip`  
`local_port_1` | `observer.port`  
`log.file.path` | `target.process.file.full_path`  
`log.source.address` | `intermediary.ip`,  
`intermediary.port`  
`log.syslog.severity.name` | `security_result.severity_details`  
`log_id` | `metadata.product_log_id`  
`log_level` | `security_result.severity`,  
`security_result.severity_details`  
`logName` | `security_result.category_details`  
`Logon Account` | `principal.user.userid`  
`logstash.irm_site` | `target.location.name`  
`logstash.process.host` | `additional.fields`  
`mail_from` | `network.email.from`  
`mail_to` | `network.email.to`  
`msg` | `metadata.description`  
`name` | `about.group.group_display_name`  
`namespace` | `principal.namespace`  
`NAPPolicy` | `security_result.rule_labels`  
`o_ip` | `observer.ip`,  
`observer.asset.ip`  
`o_port` | `observer.port`  
`obj_h` | `additional.fields`  
`obj_p` | `additional.fields`  
`p_ip` | `principal.ip`,  
`principal.asset.ip`  
`p_log_id` | `metadata.product_log_id`  
`p_port` | `principal.port`  
`p_user_id` | `principal.user.userid`  
`p_vm_name` | `target.resource.name`  
`parsable_message` | `metadata.description`  
`pid` | `target.process.pid`  
`port` | `intermediary.port`  
`ppid` | `principal.process.pid`  
`prin_app` | `principal.application`  
`prin_domain` | `principal.administrative_domain`  
`prin_name` | `principal.resource.attribute.labels`  
`prin_pid` | `principal.process.pid`  
`principal_email` | `principal.user.email_addresses`  
`principal_ip1` | `principal.ip`,  
`principal.asset.ip`  
`principal_ip2` | `principal.ip`,  
`principal.asset.ip`  
`principal_port` | `principal.port`  
`priority` | `security_result.severity`,  
`security_result.severity_details`  
`process` | `principal.application`  
`process_id` | `principal.process.pid`  
`product_event_type` | `metadata.product_event_type`  
`program` | `principal.application`  
`Protocol` | `network.ip_protocol`  
`providername` | `principal.application`  
`r_bytes` | `network.received_bytes`  
`r_name` | `principal.resource.name`  
`ReferencedHost` | `target.hostname`,  
`target.asset.hostname`  
`Relative Target Name` | `target.file.full_path`  
`relay` | `intermediary.hostname`,  
`intermediary.ip`  
`request_path` | `target.url`  
`resource.labels.project_id` | `src.resource_ancestors.product_object_id`  
`resource.type` | `src.user.attribute.labels`  
`resource_name` | `target.resource.name`  
`ResponderBytes` | `network.received_bytes`  
`ResponderPackets` | `network.received_packets`  
`response_code` | `network.http.response_code`  
`response_details` | `target.resource.attribute.labels`  
`role` | `target.user.attribute.roles`  
`s_bytes` | `network.sent_bytes`  
`sec_desc` | `security_result.description`  
`Security ID` | `target.user.windows_sid`  
`security_result_action_detail` | `security_result.action_details`  
`server_name` | `target.hostname`,  
`target.asset.hostname`  
`session_id` | `network.session_id`  
`severity` | `security_result.severity`,  
`security_result.severity_details`  
`severity_data` | `security_result.severity`,  
`security_result.severity_details`  
`Share Name` | `target.resource.name`  
`sid` | `about.group.windows_sid`  
`Source Network Address` | `principal.ip`  
`Source Port` | `principal.port`  
`source_port` | `principal.port`  
`src_ip` | `principal.ip`  
`srcip` | `principal.ip`,  
`principal.asset.ip`  
`ssh_proto` | `network.application_protocol`  
`summary` | `security_result.summary`  
`syslog_host` | `target.hostname`,  
`target.asset.hostname`  
`t_ip` | `target.ip`,  
`target.asset.ip`  
`t_port` | `target.port`  
`t_url` | `target.url`  
`tags` | `additional.fields`  
`principal_app` | `principal.application`  
`target_domain` | `target.administrative_domain`  
`target_host` | `target.hostname`,  
`target.asset.hostname`  
`target_ip1` | `target.ip`,  
`target.asset.ip`  
`target_ip2` | `target.ip`,  
`target.asset.ip`  
`target_port` | `target.port`  
`target_userid` | `target.user.userid`  
`temp_host` | `intermediary.hostname`  
`tgt_domain` | `target.administrative_domain`  
`tgt_user` | `target.user.userid`  
`thread_id` | `principal.resource.attribute.labels`  
`tls_cipher` | `network.tls.cipher`  
`type` | `metadata.product_event_type`  
`upn_name` | `intermediary.url`  
`upstream_ip` | `target.ip`,  
`target.asset.ip`  
`upstream_port` | `target.port`  
`URL` | `target.url`  
`User` | `security_result.summary`  
`user` | `target.user.userid`,  
`principal.user.userid`  
`User ID` | `target.user.userid`  
`user_id` | `principal.user.userid`  
`UserAgent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`username` | `principal.user.userid`  
`usrName` | `target.user.userid`  
`vc_event_obj_id` | `target.asset.asset_id`  
`vc_event_severity` | `security_result.severity`,  
`security_result.severity_details`  
`vc_username` | `target.user.userid`  
`ver_proto` | `network.tls.version`  
`version` | `metadata.product_version`  
`@version` | `principal.platform_version`  
`vpxd_some_id` | `additional.fields`  
`LEEF_version` | `additional.fields`  
`ICMPType` | `additional.fields`  
`ICMPCode` | `additional.fields`  
`IngressInterface` | `additional.fields`  
`EgressInterface` | `additional.fields`  
`WebApplication` | `additional.fields`  
`DNSQuery` | `additional.fields`  
`DNSRecordType` | `additional.fields`  
`DNSResponseType` | `additional.fields`  
`DNS_TTL` | `additional.fields`  
`ApplicationProtocol` | `additional.fields`  
`service.type` | `additional.fields`  
`log.syslog.facility.code` | `additional.fields`  
`log.syslog.facility.name` | `additional.fields`  
`log.syslog.severity.code` | `additional.fields`  
`log.syslog.priority` | `additional.fields`  
`host.os.name` | `additional.fields`  
`host.os.build` | `additional.fields`  
`labels.plugin_id` | `additional.fields`  
`opID` | `additional.fields`  
`sub` | `additional.fields`  
`api_invocations` | `additional.fields`  
`vc_event_cat_0` | `additional.fields`  
`vc_event_cat_1` | `additional.fields`  
`vc_event_chain_id` | `additional.fields`  
`vc_event_obj_name` | `additional.fields`  
`vc_event_obj_type` | `additional.fields`  
`p_log_id_repeat` | `additional.fields`  
`sys_priority` | `additional.fields`  
`facility` | `additional.fields`  
`originator` | `additional.fields`  
`originator_id` | `additional.fields`  
`subsystem` | `additional.fields`  
`request_timestamp` | `additional.fields`  
`response_flags` | `additional.fields`  
`duration_total_ms` | `additional.fields`  
`duration_upstream_connect_ms` | `additional.fields`  
`duration_response_tx_ms` | `additional.fields`  
`local_port_2` | `additional.fields`  
`proc_id` | `additional.fields`  
`eventid_label` | `additional.fields`  
`Logger_Name` | `additional.fields`  
`subcomponent` | `additional.fields`  
`op_id` | `additional.fields`  
`vcenter_uuid_1` | `additional.fields`  
`vcenter_uuid_2` | `additional.fields`  
`object_lookup_method` | `additional.fields`  
`conn_id` | `additional.fields`  
`performed_action` | `additional.fields`  
`login_time` | `additional.fields`  
`open_connections` | `additional.fields`  
`total_connections` | `additional.fields`  
`channel_id` | `additional.fields`  
`line_number` | `additional.fields`  
`vc_event_desc` | `additional.fields`  
`uid` | `additional.fields`  
`euid` | `additional.fields`  
`ruser` | `additional.fields`  
`tty` | `additional.fields`  
`tenant` | `additional.fields`  
`duration_ms` | `additional.fields`  
`provider` | `additional.fields`  
`provider_type` | `additional.fields`  
`response_flag` | `additional.fields`  
`http_path` | `additional.fields`  
`unknown_metric_1` | `additional.fields`  
`unknown_metric_2` | `additional.fields`  
`sequence_id` | `additional.fields`  
`syslog_facility_code` | `additional.fields`  
`syslog_severity_code` | `additional.fields`  
`syslog_severity` | `additional.fields`  
`syslog_pri` | `additional.fields`  
`syslog_facility` | `additional.fields`  
`logstash.collect.timestamp` | `additional.fields`  
`logstash.ingest.timestamp` | `additional.fields`  
`logstash.process.timestamp` | `additional.fields`  
`logstash.irm_site` | `additional.fields`  
`logstash.irm_environment` | `additional.fields`  
`logstash.irm_region` | `additional.fields`  
`agent.id` | `additional.fields`  
`agent.ephemeral_id` | `additional.fields`  
`ecs.version` | `additional.fields`  
`input.type` | `additional.fields`  
  
## UDM mapping delta reference

On September 15, 2026, Google SecOps released a new version of the VMware vCenter parser, which includes changes to the mapping of VMware vCenter log fields to UDM fields.

### Log-field mapping delta

The following table lists the mapping delta for VMware vCenter log-to-UDM fields exposed prior to September 15, 2026 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping | Reason for change  
---|---|---|---  
`appname` | `target.application` | `principal.application` | This is considered the tool initiating the action by the user, making it the principal application originating the event rather than the destination being acted upon.  
`auth_user` | `principal.user.userid` | `target.user.userid` | This is a user login event for which the user is being acted upon.  
`logstash.process.host` | `target.hostname` | `additional.fields` | This field is added by the Logstash pipeline. It indicates the hostname of the server where the Logstash process is running, which is part of the log collection infrastructure. This host is not the source of the event itself, but rather an intermediary processing the log.  
`username` | `target.user.userid` | `principal.user.userid` | This userid belongs to the src of event and not the target.  
`domain` | `target.administrative_domain` | `principal.administrative_domain` | This domain belongs to the src of event and not the target.  
`resource.labels.project_id` | `src.cloud.project.id` | `src.resource_ancestors.product_object_id` | Previous field deprecated.  
`target_app` | `target.application` | `principal.application` | The log specifically describes an internal Single Sign-On.  
`process` | `additional.fields` | `principal.application` | Better suited.  
`app` | `target.application` | `principal.application` | The log specifically describes an internal Single Sign-On.  
`@fields.privatecloud_id` | `principal.cloud.project.id` | `principal.resource_ancestors.product_object_id` | Previous field deprecated.  
`@fields.privatecloud_name` | `principal.cloud.project.name` | `principal.resource_ancestors.name` | Previous field deprecated.  
`@fields.facility` | `principal.resource.type` | `principal.resource.resource_subtype` | Previous field deprecated.  
`Client` | `target.labels` | `target.user.attribute.labels` | Previous field deprecated.  
`kv_msg1.ctladdr` | `intermediary.labels` | `intermediary.user.attribute.labels` | Previous field deprecated.  
`kv_msg1.get_error` | `intermediary.labels` | `intermediary.user.attribute.labels` | Previous field deprecated.  
`resource.type` | `src.labels` | `src.user.attribute.labels` | Previous field deprecated.  
`admin` | `principal.user.attribute.labels` | `principal.resource.attribute.labels` | Previous field deprecated.  
`role` | `target.user.role_name` | `target.user.attribute.roles` | Previous field deprecated.  
`syslog_host` | Unmapped | `target.hostname` | Newly added field mapping.  
`log.source.address` | Unmapped | `intermediary.ip`,  
`intermediary.port` | Newly added field mapping.  
`agent.type` | Unmapped | `observer.application` | Newly added field mapping.  
`agent.version` | Unmapped | `intermediary.platform_version` | Newly added field mapping.  
`pid` | Unmapped | `target.process.pid` | Newly added field mapping.  
`temp_host` | Unmapped | `intermediary.hostname` | Newly added field mapping.  
`port` | Unmapped | `intermediary.port` | Newly added field mapping.  
`inter_hostname` | Unmapped | `intermediary.hostname` | Newly added field mapping.  
`tgt_user` | Unmapped | `target.user.userid` | Newly added field mapping.  
`tgt_domain` | Unmapped | `target.administrative_domain` | Newly added field mapping.  
`alarm_target` | Unmapped | `about.resource.name` | Newly added field mapping.  
`prin_app` | Unmapped | `principal.application` | Newly added field mapping.  
`dest_ip` | Unmapped | `target.ip` | Newly added field mapping.  
`dest_port` | Unmapped | `target.port` | Newly added field mapping.  
`error_message` | Unmapped | `security_result.summary` | Newly added field mapping.  
`error_code` | Unmapped | `security_result.detection_fields` | Newly added field mapping.  
`function` | Unmapped | `security_result.detection_fields` | Newly added field mapping.  
`thread_id` | Unmapped | `principal.resource.attribute.labels` | Newly added field mapping.  
`obj_p` | Unmapped | `additional.fields` | Newly added field mapping.  
`obj_h` | Unmapped | `additional.fields` | Newly added field mapping.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vcenter-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
