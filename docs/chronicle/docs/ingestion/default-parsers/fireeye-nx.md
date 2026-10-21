---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx/
title: Collect Trellix Network Security (formerly FireEye NX) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:34:02.673555+00:00
---

# Collect Trellix Network Security (formerly FireEye NX) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Network Security (formerly FireEye NX) logs

**Parser Version:** 34.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how you can ingest Trellix Network Security (formerly known as FireEye NX) logs to Google Security Operations using the Bindplane.

Trellix Network Security is a network threat protection solution that detects and blocks advanced, targeted, and other evasive attacks hiding in web traffic. It uses a combination of signature-based and signatureless analysis engines—including Multi-Vector Virtual Execution (MVX)—to identify and stop zero-day exploits, malware callbacks, and other advanced threats in real time.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A host running Windows Server 2016 or later, or a Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and the Trellix NX appliance.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Trellix Network Security (NX) management console or Central Management System (CMS) appliance.



## Get Google SecOps ingestion authentication file

  1. Sign in to the **Google SecOps** console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**. 
  4. Save the file securely on the system where the Bindplane agent will be installed.



## Get Google SecOps customer ID

  1. Sign in to the **Google SecOps** console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with **root** or **sudo** privileges.
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

  * **Linux** : `/opt/observiq-otel-collector/config.yaml`
  * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
        udplog:
           listen_address: "0.0.0.0:514"
        
        exporters:
        chronicle/fireeye_nx:
           compression: gzip
           creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
           customer_id: '<CUSTOMER_ID>'
           endpoint: malachiteingestion-pa.googleapis.com
           log_type: FIREEYE_NX
           raw_log_field: body
           ingestion_labels:
        
        service:
        pipelines:
           logs/fireeye_nx_to_chronicle:
              receivers:
              - udplog
              exporters:
              - chronicle/fireeye_nx
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration** : 
    * `listen_address`: IP address and port to listen on. 
      * `0.0.0.0` to listen on all interfaces.
      * Port `514` is standard (requires root). Use `1514` or higher for non-root users.
  * **Exporter configuration** : 
    * `creds_file_path`: Full path to the ingestion authentication file.
    * `<CUSTOMER_ID>`: Your Customer ID from the Google SecOps console.
    * `endpoint`: Regional endpoint URL (e.g., `malachiteingestion-pa.googleapis.com`). See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list.



### Save the configuration file

After editing, save the file: * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`. * **Windows** : Click **File** > **Save**.

## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure syslog forwarding on Trellix Network Security

  1. Sign in to the **Trellix Network Security** console with an administrator account.
  2. Go to **Settings > Notifications**.
  3. Click the **rsyslog** tab.
  4. Select the **Event type** checkbox to enable rsyslog notifications.
  5. In the **Rsyslog Settings** area, provide the following configuration details:

     * **Default format** : Select **JSON** and set the level of detail to **Extended**. This combination is commonly referred to as `json-extended`. The Extended option is only applicable for JSON, XML, and Text formats.
**Note:** Use `json-extended` rather than CEF. CEF output doesn't include enough detail to triage alerts in Google SecOps. The "Extended" level of detail provides the most complete alert context, including static-analysis, data-theft details, and all files and objects modified during analysis.
  6. In the **Rsyslog Server Listing** section:

     * Enter a descriptive name for the new entry (for example, `Google SecOps-Bindplane`).
     * Click **Add Rsyslog Server**.
  7. For the newly added server, provide the following configuration details:

     * **Enabled** : Select the checkbox to enable the server.
     * **IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Protocol** : Select **TCP**. Confirm the Bindplane agent uses the `tcplog` receiver and that the port number matches.

**Note:** The `json-extended` format produces larger events than CEF, and UDP can truncate or drop large syslog messages. Consequently, TCP is required for reliable delivery. 
     * **Event Types** : Select the event types to forward or select **All** for comprehensive logging.

  8. Click **Update** to save the configuration.

**Note:** In a Trellix Network Security deployment with a Central Management System (CMS), event notifications are configured on the CMS appliance, not on individual sensors. For more information, see the [Trellix Network Security System Administration Guide](https://docs.trellix.com/bundle/nx_11.x_sag/).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`alert.dst.ip` | `target.ip`, `target.asset.ip` | Direct mapping.  
`alert.dst.mac` | `target.mac`, `target.asset.mac` | Direct mapping.  
`alert.dst.port` | `target.port` | Direct mapping.  
`alert.name` | `metadata.product_event_type` | Direct mapping.  
`alert.occurred` | `metadata.event_timestamp` | Direct mapping.  
`alert.src.ip` | `principal.ip`, `principal.asset.ip` | Direct mapping.  
`alert.src.port` | `principal.port` | Direct mapping.  
`log_id` | `metadata.product_log_id` | Direct mapping.  
`response_code` | `network.http.response_code` | Direct mapping.  
`user_id` | `principal.user.userid` | Direct mapping.  
N/A | `metadata.event_type` | Set based on presence of IP, hostname, or user ID (e.g., `SCAN_UNCATEGORIZED`, `STATUS_UPDATE`).  
N/A | `metadata.log_type` | Set to `FIREEYE_NX`.  
N/A | `metadata.vendor_name` | Set to `FireEye`.  
N/A | `security_result.action` | **ALLOW** if "notified", **BLOCK** if "blocked".  
N/A | `is_alert` | Set to `true`.  
`filePath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`fileType` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`fsize` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`fileHash` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`fileHash` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`fname` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`flexString1` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`device_vendor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entry.data.product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_source.alert_product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dvchost` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`dvcmac` | `event.idm.read_only_udm.intermediary.mac` and `event.idm.read_only_udm.intermediary.asset.mac` | Mapped from changelog  
`rawmsg.dcerpc.response_stub_data_len` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`rawmsg.dcerpc.request_stub_data_len` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`rawmsg.dcerpc.interface.uuid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`rawmsg.dcerpc.interface.version` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`rawmsg.dcerpc.interface.minor-version` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`rawmsg.dcerpc.request_stub_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dcerpc_request_stub_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.dcerpc.response_stub_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dcerpc_response_stub_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.dcerpc.opnum` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dcerpc_opnum` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`rawmsg.event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`rawmsg.src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`rawmsg.src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`rawmsg.src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`rawmsg.dest_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`rawmsg.dest_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`rawmsg.dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`rawmsg.proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`rawmsg.dns.id` | `event.idm.read_only_udm.network.dns.id` | Mapped from changelog  
`rawmsg.dns.rrname` | `event.idm.read_only_udm.network.dns.questions.name` | Mapped from changelog  
`rawmsg.dns.rrtype` | `event.idm.read_only_udm.network.dns.questions.type` | Mapped from changelog  
`rawmsg.dns.tx_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_tx_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.dns.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.flow_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flow_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.iface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`iface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rawmsg.session_key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`session_key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`meta_oml` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn2Label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn4Label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`link` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`meta_sip4` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`deviceid` | `event.idm.read_only_udm.target.asset_id` | Mapped from changelog  
`deviceid` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`meta_cbname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`meta_cbname` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`entry.data.alert.explanation.malware-detected.malware.stype` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`malware_stype` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`product` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`alert.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`alert.vlan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.ips-detected.action-taken` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.explanation.ips-detected.signature-name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.interface.interface` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.interface.label` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.src.port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`alert.src.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`alert.src.mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`alert.dst.ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`event_item.dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`alert.dst.port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`alert.dst.mac` | `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` | Mapped from changelog  
`alert.signature_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`alert.id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`alert.name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`alert.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`appliance` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`alert.occurred` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`appliance-id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.class` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.sequence` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.src_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.dst_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.details.geo_org` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_item.details.ratio` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.src.vlan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.root-infection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.ack` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.uuid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`alert.protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`alert.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`alert.alert-url` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`alert.category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`event_item.src_ip` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`event_item.details.dest_ip_resolved` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`event_item.details.duration_seconds` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`event_item.details.inbound_mb` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`event_item.details.outbound_mb` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`event_item.name` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`event_type` | `event.idm.read_only_udm.metadata.event_type` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`dstip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`file_hash` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`file_sha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`file_name` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`size` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`srcports` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`file_type` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`file_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dstports` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`src_mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`dst_mac` | `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` | Mapped from changelog  
`process` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`db_action` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`tid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`db_pool` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`db_handler` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`db_details` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`log_message` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`command_line` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`request_uri` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`http_referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`http_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`http_host'` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`request_length` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`http_version` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`binary_path` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`resource_path` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`'target_user'` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`'log_message'` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`'incoming_peer_name'` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`'incoming_session_id' and 'session_id'` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`'client'` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`'group_id'` | `event.idm.read_only_udm.principal.group_product_object_id` | Mapped from changelog  
`'target_pid'` | `event.idm.read_only_udm.target.process.pid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
