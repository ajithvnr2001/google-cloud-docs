---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-firewall/
title: Collect Juniper SRX Series Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:32:54.489862+00:00
---

# Collect Juniper SRX Series Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Juniper SRX Series Firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Juniper SRX Series Firewall logs to Google Security Operations using Bindplane.

Juniper SRX Series firewalls are high-performance network security devices that provide next-generation firewall (NGFW) capabilities, including stateful inspection, intrusion detection and prevention (IDP), application security, and VPN. SRX firewalls generate syslog messages for traffic, security, system, and session events that can be forwarded to external SIEM platforms for centralized security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and the Juniper SRX firewall.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Juniper SRX firewall (root or super-user level access via J-Web or CLI).



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/juniper_firewall:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: chronicle.googleapis.com
            log_type: JUNIPER_FIREWALL
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/juniper_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/juniper_firewall
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Port `514` is the standard syslog port (requires root privileges on Linux). Use `1514` for non-root deployments.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Google SecOps customer ID.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`).



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/juniper_firewall:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: JUNIPER_FIREWALL
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
    * **Windows** : Click **File > Save**.



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
         




## Configure Juniper SRX syslog forwarding

Configure the Juniper SRX firewall to forward syslog messages to the Bindplane agent.

### Using J-Web interface

  1. Sign in to the **Juniper SRX** J-Web interface.
  2. Go to **Configure > System Properties > Syslog**.
  3. Click **Add** under the **Host** section to add a new syslog server.
  4. Provide the following configuration details: 
     * **Host name** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Log prefix** : Optional prefix for log messages.
     * **Facility** : Select the facility and severity levels to forward: 
       * **any** : Select severity level **info** or higher.
  5. In the **Source address** field, enter the SRX management interface IP (optional but recommended for consistent source identification).
  6. Click **OK** to save.
  7. Click **Commit** to apply the configuration.



### Using Junos CLI

  1. Connect to the Juniper SRX via SSH or console.
  2. Enter configuration mode:
         
         configure
         

  3. Configure the syslog host:
         
         set system syslog host BINDPLANE_IP any info
         set system syslog host BINDPLANE_IP port 514
         set system syslog host BINDPLANE_IP source-address SRX_MGMT_IP
         set system syslog host BINDPLANE_IP structured-data
         

Replace:

     * `BINDPLANE_IP`: IP address of the Bindplane agent host.
     * `SRX_MGMT_IP`: Management IP address of the SRX firewall.
  4. Configure security log streaming (for traffic and session logs):
         
         set security log mode stream
         set security log source-address SRX_MGMT_IP
         set security log stream chronicle-stream host BINDPLANE_IP
         set security log stream chronicle-stream port 514
         set security log stream chronicle-stream transport protocol udp
         set security log stream chronicle-stream format sd-syslog
         set security log stream chronicle-stream severity info
         set security log stream chronicle-stream category all
         

Replace:

     * `BINDPLANE_IP`: IP address of the Bindplane agent host.
     * `SRX_MGMT_IP`: Management IP address of the SRX firewall.
  5. Commit the configuration:
         
         commit
         

  6. Verify the syslog configuration:
         
         show system syslog
         show security log
         




### Configure specific log categories

  * To forward specific log types, configure individual facilities:
        
        set system syslog host BINDPLANE_IP firewall any
        set system syslog host BINDPLANE_IP authorization info
        set system syslog host BINDPLANE_IP daemon info
        set system syslog host BINDPLANE_IP kernel info
        set system syslog host BINDPLANE_IP interactive-commands info
        




Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.

### Verify syslog forwarding

  1. On the SRX, run the following command to view active syslog destinations:
         
         show system syslog
         

  2. Generate test traffic through the firewall and verify logs appear in the Bindplane agent logs.




For more information, see the [Juniper SRX Series documentation](https://www.juniper.net/documentation/product/us/en/srx-series/).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`source-address` | `event.idm.read_only_udm.principal.ip` | Value taken from `source-address`.  
`source-port` | `event.idm.read_only_udm.principal.port` | Value taken from `source-port` and converted to integer.  
`destination-address` | `event.idm.read_only_udm.target.ip` | Value taken from `destination-address`.  
`destination-port` | `event.idm.read_only_udm.target.port` | Value taken from `destination-port` and converted to integer.  
`protocol-id` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from protocol number to name (6=TCP, 17=UDP, 1=ICMP).  
`policy-name` | `event.idm.read_only_udm.security_result.rule_name` | Value taken from `policy-name`.  
`source-zone-name` | `event.idm.read_only_udm.additional.fields` | Value taken from `source-zone-name` and added with key `source-zone-name`.  
`destination-zone-name` | `event.idm.read_only_udm.additional.fields` | Value taken from `destination-zone-name` and added with key `destination-zone-name`.  
`service-name` | `event.idm.read_only_udm.target.application` | Value taken from `service-name`.  
`application` | `event.idm.read_only_udm.target.application` | Value taken from `application` (if `service-name` is not present).  
`nat-source-address` | `event.idm.read_only_udm.principal.nat_ip` | Value taken from `nat-source-address`.  
`nat-source-port` | `event.idm.read_only_udm.principal.nat_port` | Value taken from `nat-source-port` and converted to integer.  
`nat-destination-address` | `event.idm.read_only_udm.target.nat_ip` | Value taken from `nat-destination-address`.  
`nat-destination-port` | `event.idm.read_only_udm.target.nat_port` | Value taken from `nat-destination-port` and converted to integer.  
`bytes-from-client` | `event.idm.read_only_udm.network.sent_bytes` | Value taken from `bytes-from-client` and converted to unsigned integer.  
`bytes-from-server` | `event.idm.read_only_udm.network.received_bytes` | Value taken from `bytes-from-server` and converted to unsigned integer.  
`packets-from-client` | `event.idm.read_only_udm.additional.fields` | Value taken from `packets-from-client` and added with key `packets-from-client`.  
`packets-from-server` | `event.idm.read_only_udm.additional.fields` | Value taken from `packets-from-server` and added with key `packets-from-server`.  
`elapsed-time` | `event.idm.read_only_udm.additional.fields` | Value taken from `elapsed-time` and added with key `elapsed-time`.  
`username` | `event.idm.read_only_udm.principal.user.userid` | Value taken from `username`.  
`reason` | `event.idm.read_only_udm.security_result.description` | Value taken from `reason`.  
`action` | `event.idm.read_only_udm.security_result.action` | If `action` is `accept` or `permit`, set to `ALLOW`. If `action` is `deny`, `drop`, `reject`, or `close`, set to `BLOCK`.  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Value taken from syslog hostname field.  
`attack-name` | `event.idm.read_only_udm.security_result.threat_name` | Value taken from `attack-name` (IDP events).  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from severity string: `info` to `INFORMATIONAL`, `warning` to `MEDIUM`, `error` or `major` to `ERROR`, `critical` to `CRITICAL`.  
| `event.idm.read_only_udm.metadata.vendor_name` | Set to `Juniper Networks`.  
| `event.idm.read_only_udm.metadata.product_name` | Set to `SRX Series Firewall`.  
`source-zone` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`destination-zone` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`REASON` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`PROFILE` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.intermediary.process.pid` | Mapped from changelog  
`ppid` | `event.idm.read_only_udm.intermediary.process.product_specific_process_id` | Mapped from changelog  
`CATEGORY` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`URL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`src_value_zone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destinationzone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NESTED-APPLICATION` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocol_value` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`SESSIONID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`application_value` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`src_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`src_mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`nat_src_address` | `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip` | Mapped from changelog  
`nat_src_value_port` | `event.idm.read_only_udm.principal.nat_port` | Mapped from changelog  
`src_value_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`roles_names` | `event.idm.read_only_udm.principal.user.attribute.roles.name` | Mapped from changelog  
`interface` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`eth_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`direction` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`packet_info` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`packets_info` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`src_rule_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`src_rule_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`srv_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`srcpolicyname` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`dest_address` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dst_mac` | `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` | Mapped from changelog  
`nat_dest_address` | `event.idm.read_only_udm.target.nat_ip` and `event.idm.read_only_udm.target.asset.nat_ip` | Mapped from changelog  
`nat_dest_port` | `event.idm.read_only_udm.target.nat_port` | Mapped from changelog  
`dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`target_user_name` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`user_value` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`RTLOG` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`RT` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`WEBFILTER` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`SNMPD` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`FLOW` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`DH` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`PKID` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`BGP` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`SNMP` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`RPD` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`JTASK` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`KMD` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`APPIDD` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`IFINFO` | `event.idm.ready_only_udm.metadata.product_event_type` | Mapped from changelog  
`sec_desc` | `security_result.description` | Mapped from changelog  
`processid` | `target.process.id` | Mapped from changelog  
`TSr" and "TSi` | `additional.fields` | Mapped from changelog  
`fw` | `intermediary.ip` | Mapped from changelog  
`msg1` | `security_result.summary` | Mapped from changelog  
`desc` | `metadata.description` | Mapped from changelog  
`local_ip` | `principal.ip` | Mapped from changelog  
`remote_ip` | `target.ip` | Mapped from changelog  
`app` | `principal.application` | Mapped from changelog  
`pid` | `principal.process.pid` | Mapped from changelog  
`event_title` | `metadata.product_event_type` | Mapped from changelog  
`event_message` | `metadata.description` | Mapped from changelog  
`Local-ip` | `principal.ip` | Mapped from changelog  
`Gateway_Name", "vpn", "tunnel_id", "tunnel_if", "Local_IKE_ID", "Remote_IKE_ID", "AAA_username", "VR_id", "Traffic_selector", "Traffic_selector_Remote_ID", "Traffic_selector_local_ID", "SA_Type", "Reason", "threshold", "time-period", and "error-message_data` | `observer.resource.attribute.labels` | Mapped from changelog  
`target_ip` | `target.ip` | Mapped from changelog  
`principal_host` | `principal.hostname` | Mapped from changelog  
`user_id` | `target.user.userid` | Mapped from changelog  
`file_path` | `target.file.full_path` | Mapped from changelog  
`pid_2` | `target.process.pid` | Mapped from changelog  
`server_ip` | `target.ip` | Mapped from changelog  
`event_time` | `metadata.event_timestamp` | Mapped from changelog  
`ACTION` | `security_result.action_details` | Mapped from changelog  
`SESSION_ID` | `network.session_id` | Mapped from changelog  
`APPLICATION` | `principal.application` | Mapped from changelog  
`pingCtlOwnerIndex", "pingCtlTestName", "usp_lsys_max_num_rpd", "usp_lsys_max_num", "urlcategory_risk", "application_sub_category", "source-zone", "destination-zone", "NESTED-APPLICATION", "CATEGORY", "REASON", "PROFILE", "source_rule", "retrans_timer" and "arp_unicast_mode` | `additional.fields` | Mapped from changelog  
`time` | `metadata.event_timestamp` | Mapped from changelog  
`ident` | `target.application` | Mapped from changelog  
`pid` | `target.process.pid` | Mapped from changelog  
`internal-protocol` | `network.ip_protocol` | Mapped from changelog  
`state` | `security_result.detection_fields` | Mapped from changelog  
`internal-ip` | `principal.ip` | Mapped from changelog  
`reflexive-ip` | `target.ip` | Mapped from changelog  
`internal-port` | `principle.port` | Mapped from changelog  
`reflexive-port` | `target.port` | Mapped from changelog  
`local-address` | `principal.ip` | Mapped from changelog  
`remote-address` | `target.ip` | Mapped from changelog  
`dns-server-address` | `principal.ip` | Mapped from changelog  
`domain-name` | `principal.administrative_domain` | Mapped from changelog  
`argument1` | `network.direction` | Mapped from changelog  
`test-owner` | `additional.fields` | Mapped from changelog  
`local-initiator` | `additional.fields` | Mapped from changelog  
`test-name` | `additional.fields` | Mapped from changelog  
`SPI` | `additional.fields` | Mapped from changelog  
`AUX-SPI` | `additional.fields` | Mapped from changelog  
`Type` | `additional.fields` | Mapped from changelog  
`error-message` | `security_result.summary` | Mapped from changelog  
`rcvd` | `network.received_bytes` | Mapped from changelog  
`rule-name` | `security_result.rule_id` | Mapped from changelog  
`rulebase-name` | `security_result.detection_fields` | Mapped from changelog  
`export-id` | `security_result.detection_fields` | Mapped from changelog  
`repeat-count` | `security_result.detection_fields` | Mapped from changelog  
`packet-log-id` | `security_result.detection_fields` | Mapped from changelog  
`alert` | `is_alert` | Mapped from changelog  
`outbound-packets` | `network.sent_packets` | Mapped from changelog  
`inbound-packets` | `network.received_packets` | Mapped from changelog  
`outbound-bytes` | `network.sent_bytes` | Mapped from changelog  
`inbound-bytes` | `network.received_bytes` | Mapped from changelog  
`application-characteristics` | `security_result.summary` | Mapped from changelog  
`application-risk` | `security_result.severity_details` | Mapped from changelog  
`application-category` | `security_result.detection_fields` | Mapped from changelog  
`application-sub-category` | `security_result.detection_fields` | Mapped from changelog  
`dst-nat-rule-name` | `security_result.detection_fields` | Mapped from changelog  
`dst-nat-rule-type` | `security_result.detection_fields` | Mapped from changelog  
`src-nat-rule-name` | `security_result.detection_fields` | Mapped from changelog  
`src-nat-rule-type` | `security_result.detection_fields` | Mapped from changelog  
`encrypted` | `security_result.detection_fields` | Mapped from changelog  
`nested-application` | `security_result.detection_fields` | Mapped from changelog  
`packet-incoming-interface` | `security_result.detection_fields` | Mapped from changelog  
`session-id-32` | `network.session_id` | Mapped from changelog  
`packets-from-client` | `network.sent_packets` | Mapped from changelog  
`packets-from-server` | `network.received_packets` | Mapped from changelog  
`elapsed-time` | `network.session_duration.seconds` | Mapped from changelog  
`source-destination-address` | `principal.nat_ip` | Mapped from changelog  
`source-destination-port` | `principal.nat_port` | Mapped from changelog  
`msg_data` | `security_result.description` | Mapped from changelog  
`threat-severity` | `security_result.severity` | Mapped from changelog  
`app_name` | `target.application` | Mapped from changelog  
`command` | `target.process.command_line` | Mapped from changelog  
`action` | `security_result.action_details` | Mapped from changelog  
`sec_description` | `security_result.description` | Mapped from changelog  
`application-name` | `network.application_protocol` | Mapped from changelog  
`subtype` | `metadata.product_event_type` | Mapped from changelog  
`source-interface-name` | `security_result.detection_fields` | Mapped from changelog  
`destination-interface-name` | `security_result.detection_fields` | Mapped from changelog  
`source-zone-name` | `security_result.detection_fields` | Mapped from changelog  
`destination-zone-name` | `security_result.detection_fields` | Mapped from changelog  
`service-name` | `security_result.detection_fields` | Mapped from changelog  
`application-name` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
