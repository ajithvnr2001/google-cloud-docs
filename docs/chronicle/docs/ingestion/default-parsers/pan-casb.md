---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-casb/
title: Collect Palo Alto Prisma Access CASB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:53.925462+00:00
---

# Collect Palo Alto Prisma Access CASB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Prisma Access CASB logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Palo Alto Prisma Access CASB logs to Google Security Operations using the Bindplane agent.

Palo Alto Networks SaaS Security (also known as Next-Generation CASB) is a cloud-delivered Cloud Access Security Broker integrated with Prisma Access. It provides visibility and control over sanctioned and unsanctioned SaaS applications, detects data policy violations, monitors user activity, and remediates risks across cloud services. Data Security, part of SaaS Security, generates logs for incidents, policy violations, remediation activities, activity monitoring, admin audit events, and behavior threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Palo Alto Networks SaaS Security service
  * If running behind a proxy, make sure firewall ports are open per the Bindplane agent requirements
  * Palo Alto Networks SaaS Security (Data Security) license, CASB-X license, or CASB-PA license
  * Administrative access to Strata Cloud Manager with permissions to configure SaaS Security settings
  * A valid TLS certificate on the syslog server (Data Security requires TLS for syslog connections)



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

## Get a Google SecOps customer ID

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
          tcplog:
            listen_address: "0.0.0.0:6514"
            tls:
              cert_file: '/opt/observiq-otel-collector/server.crt'
              key_file: '/opt/observiq-otel-collector/server.key'
        
        exporters:
          chronicle/pan_casb:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: PAN_CASB
            raw_log_field: body
            ingestion_labels:
              vendor: palo_alto_networks
              product: saas_security_casb
        
        service:
          pipelines:
            logs/pan_casb_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/pan_casb
        

**Note:** Data Security requires TLS for syslog connections. You must configure TLS on the Bindplane agent receiver with a valid certificate. If you use a self-signed certificate, set the TLS option to `peer-verify(optional-untrusted)` on the syslog server side.



### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: Set to `0.0.0.0:6514` to listen on all interfaces on port 6514 (standard syslog-over-TLS port).
    * `cert_file`: Path to the TLS certificate file for the Bindplane agent.
    * `key_file`: Path to the TLS private key file for the Bindplane agent.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Google SecOps customer ID.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be exactly `PAN_CASB`
    * `ingestion_labels`: Optional labels to categorize logs



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/pan_casb:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PAN_CASB
            raw_log_field: body
            ingestion_labels:
              vendor: palo_alto_networks
              product: saas_security_casb
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

### Linux

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           




### Windows

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
             




## Configure Palo Alto Networks SaaS Security syslog forwarding

To forward SaaS Security Data Security logs to the Bindplane agent, configure a syslog receiver in Strata Cloud Manager.

### Prepare a TLS certificate on the Bindplane agent host

Data Security requires TLS-encrypted syslog connections. Before configuring the syslog receiver, prepare the TLS certificate on the Bindplane agent host:

  1. Self-sign or obtain a TLS certificate for the Bindplane agent host.
  2. Place the certificate and private key files on the Bindplane agent host (for example, `/opt/observiq-otel-collector/server.crt` and `/opt/observiq-otel-collector/server.key`).
  3. Ensure the Bindplane agent configuration references these files in the `tls` section of the receiver.



### Configure syslog receiver in Strata Cloud Manager

  1. [Log in to](https://stratacloudmanager.paloaltonetworks.com/manage/saas-security/dashboard/sanctioned-apps) **Strata Cloud Manager**.
  2. Go to **Configuration > SaaS Security > Settings > Directory & External Services > External Services**.
  3. Click **Add Syslog/API Client**.
  4. Select **Syslog Receiver** to create a syslog server profile.
  5. In the **Name** field, enter a descriptive name for the profile (for example, `Chronicle-Bindplane`).
  6. Provide the following configuration details: 
     * **Server IP** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `6514`.
     * **Facility** : Select a syslog standard value (for example, **LOG_USER**) to calculate the priority (PRI) field. Values can be **LOG_USER** or **LOG_LOCAL0** through **LOG_LOCAL7**.
     * **Message format** : Select **IETF**.
  7. Click **Save** to save the syslog receiver configuration.

**Note:** Data Security supports only one syslog receiver at a time. If you already have a syslog receiver configured, you must remove it before adding a new one. TCP is required as the reliable transport. The IETF message format is recommended for TCP and TLS connections.



### Verify syslog forwarding

After saving the syslog receiver configuration, Data Security will begin forwarding the following log types to the Bindplane agent:

  * Incidents log
  * Policy Violation log
  * Remediation log
  * Activity Monitoring log
  * Admin Audit log
  * Behavior Threats log

**Note:** Logs are forwarded in comma-separated value (CSV) format. It may take a few minutes for logs to appear in Google SecOps after configuration.



For more information, see [Configure Syslog Monitoring on Data Security](https://docs.paloaltonetworks.com/saas-security/data-security/syslog-and-api-integration/configure-syslog-monitoring) and [Syslog Integration on Data Security](https://docs.paloaltonetworks.com/saas-security/data-security/syslog-and-api-integration/syslog-integration).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Captive_Portal_label` | `additional.fields` | Merged  
`ConfigVersion_label` | `additional.fields` | Merged  
`InboundInterface_label` | `additional.fields` | Merged  
`LogSetting_label` | `additional.fields` | Merged  
`OutboundInterface_label` | `additional.fields` | Merged  
`ProfileToken_label` | `additional.fields` | Merged  
`SessionEndReason_label` | `additional.fields` | Merged  
`SessionStartTime_label` | `additional.fields` | Merged  
`SubType_label` | `additional.fields` | Merged  
`Subtype_label` | `additional.fields` | Merged  
`Tunnel_label` | `additional.fields` | Merged  
`URLCategory_label` | `additional.fields` | Merged  
`action_label` | `additional.fields` | Merged  
`application_label` | `additional.fields` | Merged  
`application_risk_label` | `additional.fields` | Merged  
`application_technology` | `additional.fields` | Merged  
`auth_method` | `additional.fields` | Merged  
`bytes_label` | `additional.fields` | Merged  
`connection_error` | `additional.fields` | Merged  
`connection_error_id` | `additional.fields` | Merged  
`content_version` | `additional.fields` | Merged  
`count_of_repeats` | `additional.fields` | Merged  
`device_sn` | `additional.fields` | Merged  
`direction_of_attack` | `additional.fields` | Merged  
`event_id_value` | `additional.fields` | Merged  
`file_name` | `additional.fields` | Merged  
`http2_connection` | `additional.fields` | Merged  
`imsi` | `additional.fields` | Merged  
`inbound_interface` | `additional.fields` | Merged  
`log_setting` | `additional.fields` | Merged  
`log_subtype` | `additional.fields` | Merged  
`logtype` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (12 total, e.g. `LEEF:` → `application_risk_label`, `LEEF:` → `bytes_label`, `...  
`outbound_interface` | `additional.fields` | Merged  
`packet_id` | `additional.fields` | Merged  
`parent_session_id` | `additional.fields` | Merged  
`partial_hash` | `additional.fields` | Merged  
`repeat_count` | `additional.fields` | Merged  
`sequence_no` | `additional.fields` | Merged  
`session_id` | `additional.fields` | Merged  
`subtype` | `additional.fields` | Merged  
`time_generated_high_resolution` | `additional.fields` | Merged  
`totalPackets_label` | `additional.fields` | Merged  
`tunnel` | `additional.fields` | Merged  
`url_category` | `additional.fields` | Merged  
`urlcategorylist` | `additional.fields` | Merged  
`virtual_location` | `additional.fields` | Merged  
`virtual_system` | `additional.fields` | Merged  
`virtual_system_id` | `additional.fields` | Merged  
`vs_label` | `additional.fields` | Merged  
`column3` | `extensions.auth.type` | Mapped: `USERID` → `PHYSICAL`  
`column4` | `extensions.auth.type` | Mapped: `login` → `PHYSICAL`  
`column10` | `intermediary.hostname` | Directly mapped  
`column16` | `intermediary.hostname` | Directly mapped  
`event_data.EventDescription` | `metadata.description` | Directly mapped  
`hostname` | `metadata.description` | Directly mapped  
`msg.policyName` | `metadata.description` | Directly mapped  
`policyName` | `metadata.description` | Directly mapped  
`TimeReceived` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_data.EventTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSZ`  
`event_data.TimeGenerated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSZ`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`message` | `metadata.event_type` | Mapped: `LEEF:` → `GENERIC_EVENT`  
`ActionSource` | `metadata.product_event_type` | Directly mapped  
`LogType` | `metadata.product_event_type` | Directly mapped  
`SubType` | `metadata.product_event_type` | Directly mapped  
`Subtype` | `metadata.product_event_type` | Directly mapped  
`column3` | `metadata.product_event_type` | Directly mapped  
`event_data.EventName` | `metadata.product_event_type` | Directly mapped  
`msg.reason` | `metadata.product_event_type` | Directly mapped  
`reason` | `metadata.product_event_type` | Directly mapped  
`SequenceNo` | `metadata.product_log_id` | Directly mapped  
`alertId` | `metadata.product_log_id` | Directly mapped  
`msg.alertId` | `metadata.product_log_id` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `LEEF:` → `CASB`  
`column5` | `metadata.product_version` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`event_data.GlobalProtectClientVersion` | `metadata.product_version` | Directly mapped  
`callbackUrl` | `metadata.url_back_to_product` | Directly mapped  
`msg.callbackUrl` | `metadata.url_back_to_product` | Directly mapped  
`VendorName` | `metadata.vendor_name` | Directly mapped  
`message` | `metadata.vendor_name` | Mapped: `LEEF:` → `Palo Alto Networks`  
`column3` | `network.application_protocol` | Mapped: `THREAT` → `TCP`  
`has_principal` | `network.application_protocol` | Mapped: `true` → `TCP`  
`proto` | `network.application_protocol` | Directly mapped  
`Protocol` | `network.ip_protocol` | Directly mapped  
`column27` | `network.ip_protocol` | Mapped: `tcp` → `TCP`  
`column3` | `network.ip_protocol` | Mapped: `TRAFFIC` → `TCP`, `THREAT` → `TCP`  
`event_data.Protocol` | `network.ip_protocol` | Directly mapped  
`proto` | `network.ip_protocol` | Directly mapped  
`message` | `network.received_bytes` | Mapped: `LEEF:` → `uinteger`  
`srcBytes` | `network.received_bytes` | Directly mapped  
`srcPackets` | `network.received_packets` | Directly mapped  
`dstBytes` | `network.sent_bytes` | Directly mapped  
`message` | `network.sent_bytes` | Mapped: `LEEF:` → `uinteger`  
`dstPackets` | `network.sent_packets` | Directly mapped  
`SessionDuration` | `network.session_duration.seconds` | Renamed/mapped  
`SessionID` | `network.session_id` | Directly mapped  
`column21` | `network.session_id` | Mapped when `column3` == `THREAT`  
`event_data.SessionID` | `network.session_id` | Directly mapped  
`SourceUserDomain` | `principal.administrative_domain` | Directly mapped  
`DeviceSN` | `principal.asset.asset_id` | Directly mapped  
`DeviceName` | `principal.asset.hostname` | Directly mapped  
`event_data.DeviceName` | `principal.asset.hostname` | Directly mapped  
`SourceAddress` | `principal.asset.ip` | Merged  
`column3` | `principal.asset.ip` | Mapped: `USERID` → `ip`, `TRAFFIC` → `ip`, `THREAT` → `ip`  
`event_data.PublicIPv4` | `principal.asset.ip` | Merged  
`event_data.SourceAddress` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`column3` | `principal.asset.nat_ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`ip` | `principal.asset.nat_ip` | Merged  
`FileType` | `principal.file.mime_type` | Directly mapped  
`FileName` | `principal.file.names` | Merged  
`DeviceName` | `principal.hostname` | Directly mapped  
`event_data.DeviceName` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`SourceAddress` | `principal.ip` | Merged  
`column3` | `principal.ip` | Mapped: `USERID` → `ip`, `TRAFFIC` → `ip`, `THREAT` → `ip`  
`event_data.PublicIPv4` | `principal.ip` | Merged  
`event_data.SourceAddress` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `LEEF:` → `ip`, `LEEF:` → `src`  
`src` | `principal.ip` | Merged  
`SourceLocation` | `principal.location.country_or_region` | Directly mapped  
`column35` | `principal.location.country_or_region` | Directly mapped  
`event_data.SourceRegion` | `principal.location.country_or_region` | Directly mapped  
`FromZone` | `principal.location.name` | Directly mapped  
`event_data.FromZone` | `principal.location.name` | Directly mapped  
`event_data.HostID` | `principal.mac` | Merged  
`NATSource` | `principal.nat_ip` | Merged  
`column3` | `principal.nat_ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`event_data.NATSource` | `principal.nat_ip` | Merged  
`ip` | `principal.nat_ip` | Merged  
`NATSourcePort` | `principal.nat_port` | Directly mapped  
`column25` | `principal.nat_port` | Directly mapped  
`event_data.NATSourcePort` | `principal.nat_port` | Directly mapped  
`EndpointOSType` | `principal.platform` | Directly mapped  
`event_data.EndpointOSVersion` | `principal.platform_version` | Directly mapped  
`SourcePort` | `principal.port` | Directly mapped  
`column13` | `principal.port` | Directly mapped  
`column23` | `principal.port` | Directly mapped  
`event_data.SourcePort` | `principal.port` | Directly mapped  
`srcPort` | `principal.port` | Directly mapped  
`application_Subcategory` | `principal.resource.attribute.labels` | Merged  
`application_category` | `principal.resource.attribute.labels` | Merged  
`cloudhostname` | `principal.resource.attribute.labels` | Merged  
`cortexdatalaketenantid` | `principal.resource.attribute.labels` | Merged  
`flowtype` | `principal.resource.attribute.labels` | Merged  
`inboundinterfacedetailstype` | `principal.resource.attribute.labels` | Merged  
`log_source_id` | `principal.resource.attribute.labels` | Merged  
`log_source_name` | `principal.resource.attribute.labels` | Merged  
`log_type` | `principal.resource.attribute.labels` | Merged  
`logsource` | `principal.resource.attribute.labels` | Merged  
`outboundinterfacedetailstype` | `principal.resource.attribute.labels` | Merged  
`panorama_sn` | `principal.resource.attribute.labels` | Merged  
`platform_type` | `principal.resource.attribute.labels` | Merged  
`source_label` | `principal.resource.attribute.labels` | Merged  
`source_location` | `principal.resource.attribute.labels` | Merged  
`column4` | `principal.resource.type` | Directly mapped  
`column2` | `principal.user.product_object_id` | Directly mapped  
`SourceUser` | `principal.user.userid` | Directly mapped  
`SourceUserName` | `principal.user.userid` | Directly mapped  
`column12` | `principal.user.userid` | Directly mapped  
`usrName` | `principal.user.userid` | Directly mapped  
`message` | `security_result` | Mapped: `LEEF:` → `security_result`  
`sec_result` | `security_result` | Merged  
`action` | `security_result.action` | Merged  
`action_value` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`column3` | `security_result.category_details` | Mapped: `THREAT` → `column94`, `THREAT` → `column97`, `THREAT` → `column98`  
`column94` | `security_result.category_details` | Merged  
`column97` | `security_result.category_details` | Merged  
`column98` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `LEEF:` → `cat`  
`msg.policyDescription` | `security_result.description` | Directly mapped  
`policyDescription` | `security_result.description` | Directly mapped  
`DGHierarchyLevel1_label` | `security_result.detection_fields` | Merged  
`DGHierarchyLevel2_label` | `security_result.detection_fields` | Merged  
`DGHierarchyLevel3_label` | `security_result.detection_fields` | Merged  
`DGHierarchyLevel4_label` | `security_result.detection_fields` | Merged  
`action_label` | `security_result.detection_fields` | Merged  
`alert_status` | `security_result.detection_fields` | Merged  
`eventstatus_label` | `security_result.detection_fields` | Merged  
`policy_id` | `security_result.detection_fields` | Merged  
`policy_recommendation` | `security_result.detection_fields` | Merged  
`policy_type` | `security_result.detection_fields` | Merged  
`portal_label` | `security_result.detection_fields` | Merged  
`stage_label` | `security_result.detection_fields` | Merged  
`threat_category` | `security_result.detection_fields` | Merged  
`RuleUUID` | `security_result.rule_id` | Directly mapped  
`alertRuleId` | `security_result.rule_id` | Directly mapped  
`column61` | `security_result.rule_id` | Directly mapped  
`event_data.RuleUUID` | `security_result.rule_id` | Directly mapped  
`msg.alertRuleId` | `security_result.rule_id` | Directly mapped  
`Rule` | `security_result.rule_name` | Directly mapped  
`alertRuleName` | `security_result.rule_name` | Directly mapped  
`column11` | `security_result.rule_name` | Directly mapped  
`event_data.Rule` | `security_result.rule_name` | Directly mapped  
`msg.alertRuleName` | `security_result.rule_name` | Directly mapped  
`Severity` | `security_result.severity` | Directly mapped  
`column3` | `security_result.severity` | Mapped: `THREAT` → `INFORMATIONAL`  
`column31` | `security_result.severity` | Mapped: `Informational` → `INFORMATIONAL`  
`msg.severity` | `security_result.severity` | Directly mapped  
`severity` | `security_result.severity` | Directly mapped  
`ThreatNameFirewall` | `security_result.threat_name` | Directly mapped  
`Application` | `target.application` | Directly mapped  
`TunneledApplication` | `target.application` | Directly mapped  
`column13` | `target.asset.hostname` | Directly mapped  
`DestinationAddress` | `target.asset.ip` | Merged  
`column3` | `target.asset.ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`dest_ip` | `target.asset.ip` | Merged  
`event_data.DestinationAddress` | `target.asset.ip` | Merged  
`ip` | `target.asset.ip` | Merged  
`column3` | `target.asset.nat_ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`ip` | `target.asset.nat_ip` | Merged  
`accountId` | `target.hostname` | Directly mapped  
`column13` | `target.hostname` | Directly mapped  
`msg.accountId` | `target.hostname` | Directly mapped  
`DestinationAddress` | `target.ip` | Merged  
`column3` | `target.ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`dest_ip` | `target.ip` | Merged  
`dst` | `target.ip` | Merged  
`event_data.DestinationAddress` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`message` | `target.ip` | Mapped: `LEEF:` → `dst`  
`network_ip` | `target.ip` | Merged  
`DestinationLocation` | `target.location.country_or_region` | Directly mapped  
`Location` | `target.location.country_or_region` | Directly mapped  
`event_data.DestinationLocation` | `target.location.country_or_region` | Directly mapped  
`msg.resourceRegionId` | `target.location.country_or_region` | Directly mapped  
`resourceRegionId` | `target.location.country_or_region` | Directly mapped  
`ToZone` | `target.location.name` | Directly mapped  
`event_data.ToZone` | `target.location.name` | Directly mapped  
`network_mac` | `target.mac` | Merged  
`NATDestination` | `target.nat_ip` | Merged  
`column3` | `target.nat_ip` | Mapped: `TRAFFIC` → `ip`, `THREAT` → `ip`  
`event_data.NATDestination` | `target.nat_ip` | Merged  
`ip` | `target.nat_ip` | Merged  
`NATDestinationPort` | `target.nat_port` | Directly mapped  
`column26` | `target.nat_port` | Directly mapped  
`event_data.NATDestinationPort` | `target.nat_port` | Directly mapped  
`DestinationPort` | `target.port` | Directly mapped  
`column24` | `target.port` | Directly mapped  
`dstPort` | `target.port` | Directly mapped  
`event_data.DestinationPort` | `target.port` | Directly mapped  
`cloudType` | `target.resource.attribute.cloud.environment` | Mapped: `gcp` → `GOOGLE_CLOUD_PLATFORM`, `aws` → `AMAZON_WEB_SERVICES`, `azure` → `MICROSOFT...  
`accountName` | `target.resource.attribute.cloud.project.id` | Directly mapped  
`msg.accountName` | `target.resource.attribute.cloud.project.id` | Directly mapped  
`networkInterfaceId` | `target.resource.attribute.labels` | Merged  
`privateDnsName` | `target.resource.attribute.labels` | Merged  
`publicDnsName` | `target.resource.attribute.labels` | Merged  
`resource_type_label` | `target.resource.attribute.labels` | Merged  
`subnetId` | `target.resource.attribute.labels` | Merged  
`tag_label` | `target.resource.attribute.labels` | Merged  
`vpcId` | `target.resource.attribute.labels` | Merged  
`msg.resourceName` | `target.resource.name` | Directly mapped  
`resourceName` | `target.resource.name` | Directly mapped  
`msg.resourceId` | `target.resource.product_object_id` | Directly mapped  
`resourceId` | `target.resource.product_object_id` | Directly mapped  
`URL` | `target.url` | Directly mapped  
`URLDomain` | `target.url` | Directly mapped  
`column29` | `target.url` | Directly mapped  
`resource.data.securityGroups.0.groupId` | `target.user.group_identifiers` | Merged  
`resource.data.securityGroups.0.groupName` | `target.user.group_identifiers` | Merged  
`DestinationUser` | `target.user.user_display_name` | Directly mapped  
`DestinationUser` | `target.user.userid` | Directly mapped  
`column9` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_RESOURCE_ACCESS`  
N/A | `metadata.product_name` | Constant: `CASB`  
N/A | `metadata.vendor_name` | Constant: `Palo Alto Networks`  
N/A | `network.application_protocol` | Constant: `TCP`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.attribute.cloud.environment` | Constant: `GOOGLE_CLOUD_PLATFORM`  
`column6` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column10` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column21` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column24` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column27` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column31` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column32` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column33` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column34` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column35` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column36` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column37` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column38` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column39` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column41` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column42` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column43` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column44` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`column8` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`column30` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.network.tls.next_protocol` | Mapped from changelog  
`column46` | `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` | Mapped from changelog  
`column45` | `event.idm.read_only_udm.observer.resource.name` | Mapped from changelog  
`column47` | `event.idm.read_only_udm.observer.resource.product_object_id` | Mapped from changelog  
`column19` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`column20` | `event.idm.read_only_udm.principal.asset.hardware.serial_number` | Mapped from changelog  
`column14` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`column15` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column17` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column18` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`column22` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`column23` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`column25` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`column26` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`column40` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`column29` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`VirtualSystemID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationTechnology` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LogType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`Subtype` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`Subtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_value` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`ThreatNameFirewall` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`SessionID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`DeviceName` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`DeviceName` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`Location` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`TunneledApplication` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`URLDomain` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`SourceUserName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column35` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`column61` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`column94` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column97` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column98` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column21` | `event.idm.read_only_udm.event1.idm.read_only_udm.network.session_id` | Mapped from changelog  
`ThreatCategory` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SubType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`FileName` | `event.idm.read_only_udm.principal.file.names` | Mapped from changelog  
`FileType` | `event.idm.read_only_udm.principal.file.mime_type` | Mapped from changelog  
`LogType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HTTP2Connection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LogSetting` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`InboundInterface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OutboundInterface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Application` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VirtualLocation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CaptivePortal` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`URLCategoryList` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SessionID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RepeatCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ConfigVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`URLCategory` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DirectionOfAttack` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SequenceNo` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PacketID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DestinationAddress` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VirtualSystemName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IMSI` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ParentSessionID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Tunnel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationRisk` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ContentVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TimeGeneratedHighResolution` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplicationCategory` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`ApplicationSubcategory` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`LogType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`SourceLocation` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`CloudHostname` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`CortexDataLakeTenantID` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`FlowType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`InboundInterfaceDetailsType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`LogSource` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`OutboundInterfaceDetailsType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`PanoramaSN` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`PlatformType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Action` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DGHierarchyLevel1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DGHierarchyLevel2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DGHierarchyLevel3` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DGHierarchyLevel4` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`RuleUUID` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`Rule` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`Protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`ToZone` | `event.idm.read_only_udm.target.location.name` | Mapped from changelog  
`SourceAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SourceAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`DestinationAddress` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`DestinationAddress` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`NATSource` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`NATDestination` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`SourceUser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`DestinationUser` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`SourcePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`DestinationPort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`NATSourcePort` | `event.idm.read_only_udm.principal.nat_port` | Mapped from changelog  
`NATDestinationPort` | `event.idm.read_only_udm.target.nat_port` | Mapped from changelog  
`URL` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`DeviceSN` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`FromZone` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`DestinationLocation` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`X-Forwarded-For` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SourceUserDomain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`VendorName` | `event.idm.read_only_udm.metadata.vendor_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-casb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
