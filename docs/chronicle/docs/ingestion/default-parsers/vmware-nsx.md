---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-nsx/
title: Collect VMware Networking and Security Virtualization (NSX) Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:06.151856+00:00
---

# Collect VMware Networking and Security Virtualization (NSX) Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-nsx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware Networking and Security Virtualization (NSX) Manager logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VMware NSX Manager logs to Google Security Operations using the Bindplane agent.

VMware NSX is a network virtualization and security platform that generates syslog messages for firewall events, distributed firewall rules, routing changes, audit logs, and controller events. The parser extracts fields using grok patterns, key-value parsing, and JSON parsing, and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the VMware NSX environment
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to VMware NSX



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
            chronicle/vmware_nsx:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VMWARE_NSX
                raw_log_field: body
        
        service:
            pipelines:
                logs/vmware_nsx_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/vmware_nsx
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Syslog configuration for NSX Edge

  1. Sign in to the **vSphere Web Client**.
  2. Go to **Networking & Security > NSX Edges**.
  3. Select the specific **NSX Edge** instance you want to configure.
  4. Go to **Syslog Settings** : 
     * For NSX 6.4.4 and later: **Manage > Settings > Appliance Settings > Settings > Change Syslog Configuration**.
     * For NSX 6.4.3 and earlier: **Manage > Settings > Configuration > Details > Change**.
  5. Configure the syslog server details: 
     * **Server** : Enter the IP address or hostname of the syslog server (Bindplane).
     * **Protocol** : Select **UDP** or **TCP** (depending on your Bindplane configuration).
     * **Port** : Enter the port number (depending on your Bindplane configuration).
  6. Click **OK** to save the settings.



## Syslog configuration for NSX Manager

  1. Sign in to the NSX Manager web interface with administrator credentials (`https://<NSX-Manager-IP>` or `https://<NSX-Manager-Hostname>`).
  2. Go to **Manage Appliance Settings > General**.
  3. Click **Edit** to configure the syslog server settings.
  4. Enter the syslog server details: 
     * **Server** : Enter the IP address or hostname of the syslog server (Bindplane).
     * **Protocol** : Select **UDP** or **TCP** (depending on your Bindplane configuration).
     * **Port** : Enter the port number (depending on your Bindplane configuration).
  5. Click **OK** to save the settings.



## Syslog configuration for NSX Controller

  1. Sign in to the **vSphere Web Client**.
  2. Go to **Networking & Security > Installation and Upgrade > Management > NSX Controller Nodes**.
  3. Select the **NSX Manager** that manages the controller nodes.
  4. Click **Common Controller Attributes Edit**.
  5. In the **Syslog Servers** dialog, click **Add** : 
     * Enter the syslog server name or IP address.
     * Select the **UDP** protocol (depending on your Bindplane configuration).
     * Set the **Log Level** (for example, `INFO`).
  6. Click **OK** to save the settings.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`DST` | `event.idm.read_only_udm.target.ip` | The destination IP address is extracted from the `DST` field in the raw log.  
`ID` | `event.idm.read_only_udm.metadata.product_log_id` | The product log ID is extracted from the `ID` field in the raw log.  
`MAC` | `event.idm.read_only_udm.principal.mac` | The MAC address is extracted from the `MAC` field in the raw log.  
`ModuleName` | `event.idm.read_only_udm.metadata.product_event_type` | The product event type is extracted from the `ModuleName` field in the raw log.  
`Operation` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The operation is extracted from the `Operation` field in the raw log and added as a label with key "Operation".  
`PROTO` | `event.idm.read_only_udm.network.ip_protocol` | The IP protocol is extracted from the `PROTO` field in the raw log.  
`RES` | `event.idm.read_only_udm.target.resource.name` | The target resource name is extracted from the `RES` field in the raw log.  
`SRC` | `event.idm.read_only_udm.principal.ip` | The source IP address is extracted from the `SRC` field in the raw log.  
`SPT` | `event.idm.read_only_udm.principal.port` | The source port is extracted from the `SPT` field in the raw log.  
`UserName` | `event.idm.read_only_udm.principal.user.userid` | The user ID is extracted from the `UserName` field in the raw log.  
`app_type` | `event.idm.read_only_udm.principal.application` | The principal application is extracted from the `app_type` field in the raw log.  
`application` | `event.idm.read_only_udm.target.application` | The target application is extracted from the `application` field in the raw log.  
`audit` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The audit value is extracted from the `audit` field in the raw log and added as a label with key "audit".  
`cancelTimeUTC` | `event.idm.read_only_udm.principal.resource.attribute.last_update_time` | The last update time is derived from the `cancelTimeUTC` field in the raw log.  
`client` | `event.idm.read_only_udm.principal.ip` or `event.idm.read_only_udm.principal.administrative_domain` | If the `client` field is an IP address, it's mapped to principal IP. Otherwise, it's mapped to principal administrative domain.  
`comp` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The component value is extracted from the `comp` field in the raw log and added as a label with key "Comp".  
`datetime` | `event.idm.read_only_udm.metadata.event_timestamp` | The event timestamp is extracted from the `datetime` field in the raw log.  
`description` | `event.idm.read_only_udm.metadata.description` | The description is extracted from the `description` field in the raw log.  
`details` | `event.idm.read_only_udm.principal.resource.attribute.labels` | The details are extracted from the `details` field in the raw log and added as labels.  
`direction` | `event.idm.read_only_udm.network.direction` | If the `direction` field is "OUT", it's mapped to "OUTBOUND".  
`dst_ip` | `event.idm.read_only_udm.target.ip` | The destination IP address is extracted from the `dst_ip` field in the raw log.  
`DPT` | `event.idm.read_only_udm.target.port` | The destination port is extracted from the `DPT` field in the raw log.  
`errorCode` | `event.idm.read_only_udm.security_result.detection_fields` | The error code is extracted from the `errorCode` field in the raw log and added as a detection field.  
`eventType` | `event.idm.read_only_udm.metadata.product_event_type` | The product event type is extracted from the `eventType` field in the raw log.  
`filepath` | `event.idm.read_only_udm.principal.process.file.full_path` | The file path is extracted from the `filepath` field in the raw log.  
`hostname` | `event.idm.read_only_udm.principal.ip` | The hostname is extracted from the `hostname` field in the raw log and, if it's an IP address, mapped to principal IP.  
`kv_data` | Various UDM fields | The key-value pairs in `kv_data` are mapped to various UDM fields based on their keys.  
`kv_data1` | Various UDM fields | The key-value pairs in `kv_data1` are mapped to various UDM fields based on their keys.  
`kv_data2` | Various UDM fields | The key-value pairs in `kv_data2` are mapped to various UDM fields based on their keys.  
`kv_data3` | Various UDM fields | The key-value pairs in `kv_data3` are mapped to various UDM fields based on their keys.  
`kv_data4` | Various UDM fields | The key-value pairs in `kv_data4` are mapped to various UDM fields based on their keys.  
`level` | `event.idm.read_only_udm.security_result.severity` | If the `level` field is "INFO", it's mapped to "INFORMATIONAL". If it's "ERROR", it's mapped to "ERROR".  
`managedExternally` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The managedExternally value is extracted from the `managedExternally` field in the raw log and added as a label with key "managedExternally".  
`message` | Various UDM fields | The message field is parsed to extract various UDM fields.  
`message_data` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The message data is extracted from the `message_data` field in the raw log and added as a label with key "message".  
`network_status` | `event.idm.read_only_udm.additional.fields` | The network status is extracted from the `network_status` field in the raw log and added as an additional field with key "Network_Connection_Status".  
`new_value` | Various `event.idm.read_only_udm.target` fields | The new value is extracted from the `new_value` field in the raw log and used to populate various target fields.  
`node` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The node value is extracted from the `node` field in the raw log and added as a label with key "node".  
`old_value` | Various UDM fields | The old value is extracted from the `old_value` field in the raw log and used to populate various UDM fields.  
`payload` | Various UDM fields | The payload is extracted from the `payload` field in the raw log and used to populate various UDM fields.  
`pid` | `event.idm.read_only_udm.target.process.pid` | The process ID is extracted from the `pid` field in the raw log.  
`reqId` | `event.idm.read_only_udm.metadata.product_log_id` | The product log ID is extracted from the `reqId` field in the raw log.  
`resourceId` | `event.idm.read_only_udm.principal.resource.product_object_id` | The product object ID is extracted from the `resourceId` field in the raw log.  
`s2comp` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The s2comp value is extracted from the `s2comp` field in the raw log and added as a label with key "s2comp".  
`ses` | `event.idm.read_only_udm.network.session_id` | The session ID is extracted from the `ses` field in the raw log.  
`src_host` | `event.idm.read_only_udm.principal.hostname` | The principal hostname is extracted from the `src_host` field in the raw log.  
`src_ip` | `event.idm.read_only_udm.principal.ip` | The source IP address is extracted from the `src_ip` field in the raw log.  
`src_ip1` | `event.idm.read_only_udm.principal.ip` | The source IP address is extracted from the `src_ip1` field in the raw log.  
`src_port` | `event.idm.read_only_udm.principal.port` | The source port is extracted from the `src_port` field in the raw log.  
`startTimeUTC` | `event.idm.read_only_udm.principal.resource.attribute.creation_time` | The creation time is derived from the `startTimeUTC` field in the raw log.  
`subcomp` | `event.idm.read_only_udm.network.application_protocol` or `event.idm.read_only_udm.principal.resource.attribute.labels.value` | If the `subcomp` field is "http", it's mapped to "HTTP". Otherwise, it's added as a label with key "Sub Comp".  
`tname` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The tname value is extracted from the `tname` field in the raw log and added as a label with key "tname".  
`type` | `event.idm.read_only_udm.metadata.product_event_type` | The product event type is extracted from the `type` field in the raw log.  
`uid` | `event.idm.read_only_udm.principal.user.userid` | The user ID is extracted from the `uid` field in the raw log.  
`update` | `event.idm.read_only_udm.principal.resource.attribute.labels.value` | The update value is extracted from the `update` field in the raw log and added as a label with key "update".  
`user` | `event.idm.read_only_udm.principal.user.user_display_name` | The user display name is extracted from the `user` field in the raw log.  
`vmw_cluster` | `event.idm.read_only_udm.target.resource.name` | The target resource name is extracted from the `vmw_cluster` field in the raw log.  
`vmw_datacenter` | `event.idm.read_only_udm.target.resource.attribute.labels.value` | The vmw_datacenter value is extracted from the `vmw_datacenter` field in the raw log and added as a label with key "vmw_datacenter".  
`vmw_host` | `event.idm.read_only_udm.target.hostname` or `event.idm.read_only_udm.target.ip` | If the `vmw_host` field is a hostname, it's mapped to target hostname. Otherwise, if it's an IP address, it's mapped to target IP.  
`vmw_object_id` | `event.idm.read_only_udm.target.resource.product_object_id` | The product object ID is extracted from the `vmw_object_id` field in the raw log.  
`vmw_product` | `event.idm.read_only_udm.target.application` | The target application is extracted from the `vmw_product` field in the raw log.  
`vmw_vcenter` | `event.idm.read_only_udm.target.cloud.availability_zone` | The availability zone is extracted from the `vmw_vcenter` field in the raw log.  
`vmw_vcenter_id` | `event.idm.read_only_udm.target.resource.attribute.labels.value` | The vmw_vcenter_id value is extracted from the `vmw_vcenter_id` field in the raw log and added as a label with key "vmw_vcenter_id".  
`vmw_vr_ops_appname` | `event.idm.read_only_udm.intermediary.application` | The intermediary application is extracted from the `vmw_vr_ops_appname` field in the raw log.  
`vmw_vr_ops_clustername` | `event.idm.read_only_udm.intermediary.resource.name` | The intermediary resource name is extracted from the `vmw_vr_ops_clustername` field in the raw log.  
`vmw_vr_ops_clusterrole` | `event.idm.read_only_udm.intermediary.resource.attribute.roles.name` | The intermediary resource role name is extracted from the `vmw_vr_ops_clusterrole` field in the raw log.  
`vmw_vr_ops_hostname` | `event.idm.read_only_udm.intermediary.hostname` | The intermediary hostname is extracted from the `vmw_vr_ops_hostname` field in the raw log.  
`vmw_vr_ops_id` | `event.idm.read_only_udm.intermediary.resource.product_object_id` | The intermediary product object ID is extracted from the `vmw_vr_ops_id` field in the raw log.  
`vmw_vr_ops_logtype` | `event.idm.read_only_udm.intermediary.resource.attribute.labels.value` | The vmw_vr_ops_logtype value is extracted from the `vmw_vr_ops_logtype` field in the raw log and added as a label with key "vmw_vr_ops_logtype".  
`vmw_vr_ops_nodename` | `event.idm.read_only_udm.intermediary.resource.attribute.labels.value` | The vmw_vr_ops_nodename value is extracted from the `vmw_vr_ops_nodename` field in the raw log and added as a label with key "vmw_vr_ops_nodename". Determined by a series of conditional statements based on the values of other fields. Possible values are USER_LOGIN, NETWORK_CONNECTION, STATUS_UPDATE, and GENERIC_EVENT. Hardcoded to "VMWARE_NSX". Hardcoded to "VMWARE_NSX". Hardcoded to "VMWARE_NSX". Set to "AUTHTYPE_UNSPECIFIED" if `Operation` is "LOGIN" and `target_details` is not empty, or if the `message` contains "authentication failure" and `application` is not empty. Set to "SSH" if `PROTO` is "ssh2", or set to "HTTP" if `subcomp` is "http". Determined by a series of conditional statements based on the values of other fields. Possible values are ALLOW and BLOCK. Set to "VIRTUAL_MACHINE" if `vmw_cluster` is not empty.  
`Resource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`zone_action` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`product_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`sent_pkt` | `event.idm.read_only_udm.network.sent_packets` | Mapped from changelog  
`received_pkt` | `event.idm.read_only_udm.network.received_packets` | Mapped from changelog  
`sent_byte` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`received_byte` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`msg1` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`ip_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_protocol_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_protocol_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`interface_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tcp_flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_zone_value` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`sec_desc` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`Originated_Ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`Originated_Ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`event_source` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`Resource_Name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`Universal_Object` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`Code` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`Event_Message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`Above_supported_instances` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Above_threshold_instances` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Below_threshold_instances` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`supported_compact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`supported_quadlarge` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`supported_large` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`supported_xlarge` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action` | `security_result.action_details` | Mapped from changelog  
`rule_id` | `security_result.rule_id` | Mapped from changelog  
`network.direction` | `INBOUND` | Mapped from changelog  
`security_result.action_details` | `ALLOW` | Mapped from changelog  
`security_result.action_details` | `BLOCK` | Mapped from changelog  
`metadata.event_type` | `NETWORK_CONNECTION` | Mapped from changelog  
`unique_id` | `principal.resource.product_object_id` | Mapped from changelog  
`resource_type` | `principal.resource.sub_type` | Mapped from changelog  
`_create_user","_last_modified_user` | `principal.user.email_addresses` | Mapped from changelog  
`action` | `security_result.action` | Mapped from changelog  
`display_name` | `principal.resource.name` | Mapped from changelog  
`_last_modified_time` | `principal.resource.attribute.last_update_time` | Mapped from changelog  
`_create_time` | `principal.resource.attribute.creation_time` | Mapped from changelog  
`parent_path` | `principal.resource.parent` | Mapped from changelog  
`id` | `principal.resource.id` | Mapped from changelog  
`resource_type` | `target.resource.sub_type` | Mapped from changelog  
`unique_id` | `target.resource.product_object_id` | Mapped from changelog  
`path` | `target.process.file.full_path` | Mapped from changelog  
`id` | `target.resource.id` | Mapped from changelog  
`vmw_host` | `target_details.hostname or target_details.ip` | Mapped from changelog  
`vmw_vr_ops_clusterrole` | `intermediary.resource.attribute.labels.roles.name` | Mapped from changelog  
`vmw_host","vmw_product","vmw_vcenter","vmw_cluster","vmw_vr_ops_id","vmw_object_id","vmw_datacenter","vmw_vcenter_id","vmw_vr_ops_logtype","vmw_vr_ops_appname","vmw_vr_ops_hostname","vmw_vr_ops_nodename","vmw_vr_ops_clustername","vmw_vr_ops_clusterrole","managedExternally","update","filepath","eventType","resourceId` | `principal.resource.attribute.labels` | Mapped from changelog  
`tname", "s2comp", "node` | `principal.resource.attribute.labels` | Mapped from changelog  
`exe` | `target.process.file.full_path` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-nsx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
