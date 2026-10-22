---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup/
title: Collect Cohesity DataProtect (formerly Veritas NetBackup) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:26.470336+00:00
---

# Collect Cohesity DataProtect (formerly Veritas NetBackup) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cohesity DataProtect (formerly Veritas NetBackup) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cohesity DataProtect (formerly Veritas NetBackup) logs to Google Security Operations using Bindplane.

Cohesity DataProtect (formerly Veritas NetBackup, acquired by Cohesity in December 2024) is an enterprise-grade data protection and backup solution designed to safeguard data across physical, virtual, and cloud environments. It provides centralized management for backup, recovery, and disaster recovery operations, supporting a wide range of platforms, applications, and storage targets to ensure data resilience at scale.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with systemd.
  * Network connectivity between Bindplane agent and Cohesity DataProtect (formerly Veritas NetBackup).
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the NetBackup Administration Console or NetBackup Appliance Shell.
  * NetBackup version 7.7 or later (for syslog forwarding support).



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
          chronicle/netbackup:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: chronicle.googleapis.com
            log_type: VERITAS_NETBACKUP
            raw_log_field: body
            ingestion_labels:
              env: production
              source: netbackup
        
        service:
          pipelines:
            logs/netbackup_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/netbackup
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0:514` to listen on all interfaces on port 514. If port 514 requires root privileges on Linux, use `0.0.0.0:1514` and configure NetBackup to send to port 1514.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID from the previous step (for example, `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6`)
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be exactly `VERITAS_NETBACKUP`
    * `ingestion_labels`: Optional labels for filtering and organization



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/netbackup:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VERITAS_NETBACKUP
            raw_log_field: body
            ingestion_labels:
              env: production
              source: netbackup
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



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
         




## Configure Cohesity DataProtect (formerly Veritas NetBackup) syslog forwarding

NetBackup supports two methods for configuring syslog forwarding: through the `bp.conf` configuration file on the NetBackup primary server, or through the NetBackup Appliance Shell for appliance-based deployments.

### Option A: Configure syslog via bp.conf (NetBackup primary server)

  1. Sign in to the **NetBackup primary server** as an administrator.

  2. Open the `bp.conf` configuration file:

     * **Linux:**
    
    sudo vi /usr/openv/netbackup/bp.conf
    

     * **Windows:**
    
    C:\Program Files\Veritas\NetBackup\bp.conf
    

  3. Add the following entries to the `bp.conf` file:
         
         SYSLOG_SERVER = <BINDPLANE_AGENT_IP>
         SYSLOG_PORT = 514
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
**Note:** The `SYSLOG_SERVER` parameter specifies the destination syslog server, and `SYSLOG_PORT` sets the UDP port. The default port is 514 if `SYSLOG_PORT` is not specified.
  4. Save and close the file.

  5. Restart the NetBackup services to apply the changes:

     * **Linux:**
    
    sudo /usr/openv/netbackup/bin/bp.kill_all
    sudo /usr/openv/netbackup/bin/bp.start_all
    

     * **Windows:**
    
    "C:\Program Files\Veritas\NetBackup\bin\bpdown.exe" -f
    "C:\Program Files\Veritas\NetBackup\bin\bpup.exe" -f
    




### Option B: Configure syslog via NetBackup Appliance Shell

  1. Sign in to the **NetBackup Appliance Shell** via SSH or the web-based console.

  2. Navigate to **Settings > Syslog**.

  3. Run the following command to configure syslog forwarding:
         
         Settings > Syslog > Set <BINDPLANE_AGENT_IP> 514 UDP
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  4. Confirm the configuration by running:
         
         Settings > Syslog > Show
         

  5. Verify that the syslog server IP, port, and protocol are correctly displayed.




### Verify syslog forwarding

After configuring syslog forwarding, verify that logs are being sent by checking the Bindplane agent host:

  * **Linux:**
        
        sudo tcpdump -i any port 514 -A
        

  * **Windows:**




Use Wireshark or Microsoft Message Analyzer to capture traffic on port 514.

### Notes on NetBackup syslog behavior

  * NetBackup sends operational event logs, job status notifications, and system alerts via syslog. The log messages include backup job status, media events, device errors, and administrative actions.

  * Syslog messages are sent via UDP by default. NetBackup does not natively support TCP syslog forwarding through the `bp.conf` method.

  * The Google SecOps VERITAS_NETBACKUP parser handles both key-value pair and JSON-formatted syslog messages from NetBackup.

  * Ensure the NetBackup primary server system time is synchronized with NTP and configured to UTC for accurate log timestamps.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`data` | `additional.fields[0].value.string_value` | The date and time from the raw log message, extracted using grok and formatted as "MM/DD/YY HH:MM:SS".  
`data` | `metadata.description` | The description part of the message extracted using grok. Example: "(OdbcStatement::ExecDirect:962)::Error".  
`data` | `metadata.product_event_type` | The product event type extracted using grok. Example: "Error::83".  
`data` | `principal.asset.hostname` | The hostname extracted from the syslog message using grok.  
`data` | `principal.file.full_path` | The pem file path extracted from the JSON data in the log.  
`data` | `principal.hostname` | The hostname extracted from the syslog message using grok.  
`data` | `security_result.detection_fields[0].key` | The key "SqlState" is added if the `SqlState` field is present in the raw log after the grok parsing.  
`data` | `security_result.detection_fields[0].value` | The value of SqlState extracted from the raw log message using grok and kv.  
`data` | `security_result.detection_fields[1].key` | The key "NativeError" is added if the `NativeError` field is present in the raw log after the grok parsing.  
`data` | `security_result.detection_fields[1].value` | The value of NativeError extracted from the raw log message using grok and kv.  
`data` | `security_result.detection_fields[2].key` | The key "sev" is added if the `sev` field is present in the raw log after the grok parsing.  
`data` | `security_result.detection_fields[2].value` | The value of `sev` extracted from the JSON data in the log.  
`data` | `security_result.severity` | Set to "LOW" if the `sev` field (extracted from JSON) is "normal".  
`data` | `security_result.summary` | The error message or summary extracted from the raw log message using grok.  
`data` | `additional.fields[1].value.string_value` | The value of `thread` extracted from the JSON data in the log.  
`data` | `additional.fields[2].value.string_value` | The value of `m` extracted from the JSON data in the log.  
`data` | `additional.fields[3].value.string_value` | The value of `fn` extracted from the JSON data in the log.  
`collection_time` | `metadata.event_timestamp` | The timestamp from the `collection_time` field in the raw log. Set to "STATUS_UPDATE" if a principal hostname is present, otherwise "GENERIC_EVENT".  
`collection_time` | `timestamp` | The timestamp from the `collection_time` field in the raw log.  
`product_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`event_ts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veritas-netbackup-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
