---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-eyeinspect/
title: Collect Forescout eyeInspect logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:27.950068+00:00
---

# Collect Forescout eyeInspect logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-eyeinspect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forescout eyeInspect logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forescout eyeInspect logs to Google Security Operations using the Bindplane agent.

Forescout eyeInspect is an OT/ICS network monitoring platform that provides deep packet inspection of industrial protocols, asset discovery, and threat detection in operational technology environments. It generates alerts and audit logs for industrial network events in CEF format.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Forescout eyeInspect Command Center
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Forescout eyeInspect Command Center with administrator permissions



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/forescout_eyeinspect:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: FORESCOUT_EYEINSPECT
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/eyeinspect_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/forescout_eyeinspect
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `forescout_eyeinspect`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `FORESCOUT_EYEINSPECT`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `eyeinspect_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/forescout_eyeinspect:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORESCOUT_EYEINSPECT
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure Forescout eyeInspect syslog forwarding

  1. Sign in to the **Forescout eyeInspect Command Center** web console.
  2. Go to the **Alert Forwarding** configuration section.
  3. Click **Add** to create a new alert forwarding destination.
  4. Provide the following configuration details: 
     * **Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **TCP** (recommended) or **UDP**.
     * **Format** : Select **CEF** (Common Event Format).
     * **Severity** : Select **Informational** or lower to capture all events, including alerts and audit logs.
  5. Click **Save**.
  6. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** The Chronicle parser expects CEF-formatted Forescout eyeInspect logs. LEEF and JSON formats are also supported. Ensure the selected format matches what the Chronicle parser supports for your log type.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`message` | `about` | Mapped: `CEF:` → `about`  
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`message` | `about.ip` | Mapped: `CEF:` → `ips`  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`message` | `about.mac` | Mapped: `CEF:` → `mac_address`, `CEF:` → `dvcmac`  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`message` | `about.nat_ip` | Mapped: `CEF:` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`message` | `about.resource.attribute.permissions` | Mapped: `CEF:` → `permissions`  
`permissions` | `about.resource.attribute.permissions` | Merged  
`Assigned_hosts_label` | `additional.fields` | Merged  
`Available_memory_label` | `additional.fields` | Merged  
`Available_swap_label` | `additional.fields` | Merged  
`Connected_clients_label` | `additional.fields` | Merged  
`EM_connection_status_label` | `additional.fields` | Merged  
`Engine_status_label` | `additional.fields` | Merged  
`Installed_Plugins_label` | `additional.fields` | Merged  
`Used_memory_label` | `additional.fields` | Merged  
`Used_swap_label` | `additional.fields` | Merged  
`additional_cfp1` | `additional.fields` | Merged  
`additional_cfp2` | `additional.fields` | Merged  
`additional_cfp3` | `additional.fields` | Merged  
`additional_cfp4` | `additional.fields` | Merged  
`additional_cn1` | `additional.fields` | Merged  
`additional_cn2` | `additional.fields` | Merged  
`additional_cn3` | `additional.fields` | Merged  
`additional_cs1` | `additional.fields` | Merged  
`additional_cs2` | `additional.fields` | Merged  
`additional_cs3` | `additional.fields` | Merged  
`additional_cs4` | `additional.fields` | Merged  
`additional_cs5` | `additional.fields` | Merged  
`additional_cs6` | `additional.fields` | Merged  
`additional_cs7` | `additional.fields` | Merged  
`additional_devicePayloadId` | `additional.fields` | Merged  
`additional_eventId` | `additional.fields` | Merged  
`additional_flexString1` | `additional.fields` | Merged  
`additional_fname` | `additional.fields` | Merged  
`application_status_label` | `additional.fields` | Merged  
`cnt_label` | `additional.fields` | Merged  
`cpu_usage_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`event_type` | `additional.fields` | Mapped values (11 total, e.g. `System statistics` → `cpu_usage_label`, `System statistics` →...  
`message` | `additional.fields` | Mapped values (32 total, e.g. `CEF:` → `additional_eventId`, `CEF:` → `additional_devicePayl...  
`type_label` | `additional.fields` | Merged  
`act` | `extensions.auth.type` | Mapped: `(?i)LOGIN` → `MACHINE`  
`app_protocol` | `extensions.auth.type` | Mapped: `CounterACT` → `AUTHTYPE_UNSPECIFIED`  
`kv_data` | `extensions.auth.type` | Mapped: `Log: Login` → `AUTHTYPE_UNSPECIFIED`, `logged out` → `AUTHTYPE_UNSPECIFIED`  
`message` | `extensions.auth.type` | Mapped: `CEF:` → `MACHINE`, `CEF:` → `AUTHTYPE_UNSPECIFIED`  
`message` | `intermediary` | Mapped: `CEF:` → `intermediary`  
`iporhost` | `intermediary.asset.hostname` | Directly mapped  
`middle_ip` | `intermediary.asset.ip` | Merged  
`deviceDnsDomain` | `intermediary.hostname` | Directly mapped  
`iporhost` | `intermediary.hostname` | Directly mapped  
`middle_ip` | `intermediary.ip` | Merged  
`pid` | `intermediary.process.pid` | Directly mapped  
`desc` | `metadata.description` | Directly mapped  
`event_type` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ts_syslog` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`act` | `metadata.event_type` | Mapped: `(?i)LOGIN` → `USER_LOGIN`  
`app_protocol` | `metadata.event_type` | Mapped: `CounterACT` → `USER_LOGIN`, `CounterACT` → `USER_LOGOUT`, `CounterACT` → `GENERIC_E...  
`app_protocol_output` | `metadata.event_type` | Mapped: `SSH` → `STATUS_UPDATE`  
`data` | `metadata.event_type` | Mapped: `Target:` → `NETWORK_CONNECTION`  
`et_lower` | `metadata.event_type` | Mapped: `nac policy log` → `SCAN_HOST`, `port bite` → `SCAN_NETWORK`, `block event` → `NETWO...  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`has_target` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`kv_data` | `metadata.event_type` | Mapped: `Log: Login` → `USER_LOGIN`, `logged out` → `USER_LOGOUT`, `RADIUS Authentication re...  
`message` | `metadata.event_type` | Mapped values (12 total, e.g. `CEF:` → `USER_LOGIN`, `CEF:` → `USER_RESOURCE_ACCESS`, `CEF:`...  
`meta_event_type` | `metadata.event_type` | Mapped: `GENERIC_EVENT` → `NETWORK_CONNECTION`, `GENERIC_EVENT` → `STATUS_UPDATE`, `GENERIC_...  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`engineName` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`eventtype` | `metadata.product_event_type` | Directly mapped  
`alertId` | `metadata.product_log_id` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `CEF:` → `FORESCOUT EYEINSPECT`  
`product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`message` | `metadata.vendor_name` | Mapped: `CEF:` → `FORESCOUT`  
`vendor_name` | `metadata.vendor_name` | Directly mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:` → `INBOUND`, `CEF:` → `OUTBOUND`  
`answers` | `network.dns.answers` | Merged  
`app` | `network.dns.answers` | Mapped: `DNS` → `answers`  
`message` | `network.dns.answers` | Mapped: `CEF:` → `answers`  
`app` | `network.dns.questions` | Mapped: `DNS` → `questions`  
`message` | `network.dns.questions` | Mapped: `CEF:` → `questions`  
`questions` | `network.dns.questions` | Merged  
`mail_from` | `network.email.from` | Directly mapped  
`et_lower` | `network.email.subject` | Mapped: `mail (anomaly/infection) (attempt/sender/server/amount/attachment/receipeint)` → `m...  
`mail_subject` | `network.email.subject` | Merged  
`message` | `network.email.subject` | Mapped: `CEF:` → `mail_subject`  
`et_lower` | `network.email.to` | Mapped: `mail (anomaly/infection) (attempt/sender/server/amount/attachment/receipeint)` → `m...  
`mail_to` | `network.email.to` | Merged  
`message` | `network.email.to` | Mapped: `CEF:` → `mail_to`  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`l4Proto` | `network.ip_protocol` | Directly mapped  
`protocol` | `network.ip_protocol` | Directly mapped  
`protocol1` | `network.ip_protocol` | Directly mapped  
`downDataLength` | `network.received_bytes` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`message` | `network.received_bytes` | Mapped: `CEF:` → `uinteger`  
`message` | `network.sent_bytes` | Mapped: `CEF:` → `uinteger`  
`out` | `network.sent_bytes` | Renamed/mapped  
`upDataLength` | `network.sent_bytes` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`sensorName` | `observer.hostname` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`Host` | `principal.asset.hostname` | Directly mapped  
`Hostname` | `principal.asset.hostname` | Directly mapped  
`Source` | `principal.asset.hostname` | Directly mapped  
`srcHostName` | `principal.asset.hostname` | Directly mapped  
`app_protocol` | `principal.asset.ip` | Mapped: `CounterACT` → `source_ip`  
`app_protocol_output` | `principal.asset.ip` | Mapped: `SSH` → `source_ip`  
`et_lower` | `principal.asset.ip` | Mapped: `block event` → `host_ip`, `(?i)Property change detected` → `source_ip`  
`host_ip` | `principal.asset.ip` | Merged  
`kv_data` | `principal.asset.ip` | Mapped: `Log: Login` → `source_ip`, `logged out` → `source_ip`  
`message` | `principal.asset.ip` | Mapped: `CEF:` → `srcIp`, `CEF:` → `source_ip`, `CEF:` → `host_ip`, `CEF:` → `src_ip`  
`source_ip` | `principal.asset.ip` | Merged  
`srcIp` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`message` | `principal.asset.mac` | Mapped: `CEF:` → `srcMac`  
`srcMac` | `principal.asset.mac` | Merged  
`pcapSha1` | `principal.file.sha1` | Directly mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`Host` | `principal.hostname` | Directly mapped  
`Hostname` | `principal.hostname` | Directly mapped  
`Source` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`srcHostName` | `principal.hostname` | Directly mapped  
`app_protocol` | `principal.ip` | Mapped: `CounterACT` → `source_ip`  
`app_protocol_output` | `principal.ip` | Mapped: `SSH` → `source_ip`  
`et_lower` | `principal.ip` | Mapped: `block event` → `host_ip`, `(?i)Property change detected` → `source_ip`  
`host_ip` | `principal.ip` | Merged  
`kv_data` | `principal.ip` | Mapped: `Log: Login` → `source_ip`, `logged out` → `source_ip`  
`message` | `principal.ip` | Mapped values (6 total, e.g. `CEF:` → `principal_ip`, `CEF:` → `shost`, `CEF:` → `srcIp`)  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`source_ip` | `principal.ip` | Merged  
`srcIp` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`MAC` | `principal.mac` | Merged  
`et_lower` | `principal.mac` | Mapped: `(?i)Property change detected` → `MAC`  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:` → `mac`, `CEF:` → `srcMac`, `CEF:` → `MAC`, `CEF:` → `src_mac`  
`srcMac` | `principal.mac` | Merged  
`src_mac` | `principal.mac` | Merged  
`message` | `principal.nat_ip` | Mapped: `CEF:` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`source_port` | `principal.port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`srcPort` | `principal.port` | Directly mapped  
`src_port` | `principal.port` | Directly mapped  
`command` | `principal.process.command_line` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`resource` | `principal.resource.name` | Directly mapped  
`message` | `principal.user.attribute.roles` | Mapped: `CEF:` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`User` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`user_name` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`app_protocol` | `security_result` | Mapped: `CounterACT` → `sec_result`  
`data` | `security_result` | Mapped: `Target:` → `sec_result`  
`kv_data` | `security_result` | Mapped: `Log: Login` → `sec_result`, `logged out` → `sec_result`, `RADIUS Authentication res...  
`message` | `security_result` | Mapped: `CEF:` → `security_result`, `CEF:` → `sec_result`  
`sec_result` | `security_result` | Merged  
`message` | `security_result.about.resource.attribute.labels` | Mapped: `CEF:` → `res_label`  
`res_label` | `security_result.about.resource.attribute.labels` | Merged  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`action_status` | `security_result.action` | Mapped: `"success", "successful"` → `sec_action`  
`app_protocol` | `security_result.action` | Mapped: `CounterACT` → `sec_action`  
`et_lower` | `security_result.action` | Mapped: `block event` → `security_result_action`  
`kv_data` | `security_result.action` | Mapped: `Log: Login` → `sec_action`  
`message` | `security_result.action` | Mapped: `CEF:` → `_action`, `CEF:` → `sec_action`, `CEF:` → `security_result_action`  
`sec_action` | `security_result.action` | Merged  
`security_result_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.alert_state` | Mapped: `alert` → `ALERTING`  
`message` | `security_result.alert_state` | Mapped: `CEF:` → `ALERTING`, `CEF:` → `NOT_ALERTING`  
`message` | `security_result.attack_details.tactics` | Mapped: `CEF:` → `tactics`  
`tactics` | `security_result.attack_details.tactics` | Merged  
`message` | `security_result.attack_details.techniques` | Mapped: `CEF:` → `techniques`  
`techniques` | `security_result.attack_details.techniques` | Merged  
`alertCategory` | `security_result.category_details` | Merged  
`cat` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF:` → `cat`, `CEF:` → `alertCategory`  
`Category` | `security_result.description` | Directly mapped  
`Reason` | `security_result.description` | Directly mapped  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`act` | `security_result.description` | Directly mapped  
`description` | `security_result.description` | Directly mapped  
`details` | `security_result.description` | Directly mapped  
`et_lower` | `security_result.description` | Directly mapped  
`event_type` | `security_result.description` | Directly mapped  
`kv_data` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`policy_details` | `security_result.description` | Directly mapped  
`rnmsg` | `security_result.description` | Directly mapped  
`dstMacVendor_label` | `security_result.detection_fields` | Merged  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`l2Proto_label` | `security_result.detection_fields` | Merged  
`l3Proto_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (13 total, e.g. `CEF:` → `operation_label`, `CEF:` → `operasjon_label`, `CEF:`...  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`protocol_label` | `security_result.detection_fields` | Merged  
`protocol_type` | `security_result.detection_fields` | Mapped: `IP` → `protocol_label`  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`srcMacVendor_label` | `security_result.detection_fields` | Merged  
`status_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`Rule` | `security_result.rule_id` | Directly mapped  
`alert_id` | `security_result.rule_id` | Directly mapped  
`device_event_class_id` | `security_result.rule_id` | Directly mapped  
`typeId` | `security_result.rule_id` | Directly mapped  
`Match` | `security_result.rule_name` | Directly mapped  
`et_lower` | `security_result.rule_name` | Mapped: `block event` → `Virtual Firewall blocking`  
`is_fw_blocking` | `security_result.rule_name` | Mapped: `true` → `Virtual Firewall blocking`  
`message` | `security_result.rule_name` | Mapped: `CEF:` → `Virtual Firewall blocking`  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`name` | `security_result.rule_name` | Directly mapped  
`message` | `security_result.severity` | Mapped values (6 total, e.g. `CEF:` → `LOW`, `CEF:` → `MEDIUM`, `CEF:` → `HIGH`)  
`severity` | `security_result.severity` | Mapped values (13 total, e.g. `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM",...  
`severity` | `security_result.severity_details` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`event_name` | `security_result.summary` | Directly mapped  
`event_type` | `security_result.summary` | Directly mapped  
`log_description` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`threat` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF:` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`Destination` | `target.asset.hostname` | Directly mapped  
`Target` | `target.asset.hostname` | Directly mapped  
`computer_name` | `target.asset.hostname` | Directly mapped  
`dstHostName` | `target.asset.hostname` | Directly mapped  
`Destination` | `target.asset.ip` | Merged  
`app_protocol` | `target.asset.ip` | Mapped: `CounterACT` → `target_ip`, `CounterACT` → `Destination`  
`data` | `target.asset.ip` | Mapped: `Target:` → `Destination`  
`dest_ip` | `target.asset.ip` | Merged  
`destination_ip` | `target.asset.ip` | Merged  
`dstIp` | `target.asset.ip` | Merged  
`et_lower` | `target.asset.ip` | Mapped: `port bite` → `destination_ip`, `block event` → `target_ip`  
`kv_data` | `target.asset.ip` | Mapped: `Log: Login` → `target_ip`  
`message` | `target.asset.ip` | Mapped values (5 total, e.g. `CEF:` → `dstIp`, `CEF:` → `target_ip`, `CEF:` → `Destination`)  
`target_ip` | `target.asset.ip` | Merged  
`dstMac` | `target.asset.mac` | Merged  
`message` | `target.asset.mac` | Mapped: `CEF:` → `dstMac`  
`Destination` | `target.hostname` | Directly mapped  
`Target` | `target.hostname` | Directly mapped  
`computer_name` | `target.hostname` | Directly mapped  
`dstHostName` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`Destination` | `target.ip` | Merged  
`IPv6_Address` | `target.ip` | Merged  
`app_protocol` | `target.ip` | Mapped: `CounterACT` → `target_ip`, `CounterACT` → `Destination`  
`data` | `target.ip` | Mapped: `Target:` → `Destination`  
`dest_ip` | `target.ip` | Merged  
`destination_ip` | `target.ip` | Merged  
`dstIp` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`et_lower` | `target.ip` | Mapped: `port bite` → `destination_ip`, `block event` → `target_ip`  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`kv_data` | `target.ip` | Mapped: `Log: Login` → `target_ip`  
`message` | `target.ip` | Mapped values (7 total, e.g. `CEF:` → `dst_ip`, `CEF:` → `IPv6_Address`, `CEF:` → `dstIp`)  
`target_ip` | `target.ip` | Merged  
`dest_mac` | `target.mac` | Merged  
`dstMac` | `target.mac` | Merged  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF:` → `mac_address`, `CEF:` → `dstMac`, `CEF:` → `dest_mac`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF:` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dest_port` | `target.port` | Directly mapped  
`dpt` | `target.port` | Renamed/mapped  
`dstPort` | `target.port` | Directly mapped  
`port` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`message` | `target.resource.attribute.labels` | Mapped: `CEF:` → `resource_Type_label`  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF:` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
`username` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `FORESCOUT EYEINSPECT`  
N/A | `metadata.vendor_name` | Constant: `FORESCOUT`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.alert_state` | Constant: `ALERTING`  
N/A | `security_result.rule_name` | Constant: `Virtual Firewall blocking`  
N/A | `security_result.severity` | Constant: `LOW`  
`app_protocol_src` | `network.application_protocol` | Mapped from changelog  
`Category" and "policy_details` | `security_result.description` | Mapped from changelog  
`CPU_usage", "Available_memory", "Used_memory", "Available_swap", "Used_swap` | `additional.fields` | Mapped from changelog  
`application_status", "Connected_clients", "EM_connection_status", "Assigned_hosts", "Engine_status", "Installed_Plugins` | `additional.fields` | Mapped from changelog  
`alart_id` | `security_result.rule_id` | Mapped from changelog  
`protocol2` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forescout-eyeinspect-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
