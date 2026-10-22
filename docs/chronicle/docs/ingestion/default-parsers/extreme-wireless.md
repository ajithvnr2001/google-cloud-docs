---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless/
title: Collect Extreme Wireless logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:46.994209+00:00
---

# Collect Extreme Wireless logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Extreme Wireless logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Extreme Wireless logs to Google Security Operations using the Bindplane agent.

Extreme Networks wireless controllers generate syslog messages for client association and disassociation events, authentication, RADIUS interactions, and access point status changes. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Extreme Networks CloudIQ controller
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Extreme Networks CloudIQ



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
          chronicle/extreme_wireless:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: EXTREME_WIRELESS
            raw_log_field: body
        
        service:
          pipelines:
            logs/extreme_wireless_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/extreme_wireless
        




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
          chronicle/extreme_wireless:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: EXTREME_WIRELESS
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
             




## Configure syslog on Extreme Networks CloudIQ

  1. Sign in to the **CloudIQ** web UI.
  2. Go to **Configure > Common Objects > Management > Syslog Servers**.
  3. Click **+**.
  4. Provide the following configuration details: 
     * **Name** : Provide a unique name for the server.
     * **Severity** : Select **Info**.
     * Select an existing syslog IP address from the **Select** menu, or click **+**.
     * Enter the Bindplane agent IP address.
     * Enter the Bindplane agent port number.
     * Click **ADD**.
  5. Click **Save Syslog Server**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `security_result.detection_fields.key` | The value of the `action` field from the raw log is mapped to the `security_result.detection_fields.key`.  
`action` | `security_result.detection_fields.value` | The value of the `action` field from the raw log is mapped to the `security_result.detection_fields.value`.  
`BSSID` | `principal.resource.attribute.labels.key` | The string "BSSID" is assigned to the `principal.resource.attribute.labels.key`.  
`BSSID` | `principal.resource.attribute.labels.value` | The value of the `BSSID` field from the raw log is mapped to the `principal.resource.attribute.labels.value`.  
`collection_time.nanos` | `metadata.event_timestamp.nanos` | The value of `collection_time.nanos` from the raw log is mapped to `metadata.event_timestamp.nanos`.  
`collection_time.seconds` | `metadata.event_timestamp.seconds` | The value of `collection_time.seconds` from the raw log is mapped to `metadata.event_timestamp.seconds`.  
`collection_time.seconds` | `timestamp.seconds` | The value of `collection_time.seconds` from the raw log is mapped to `timestamp.seconds`.  
`collection_time.nanos` | `timestamp.nanos` | The value of `collection_time.nanos` from the raw log is mapped to `timestamp.nanos`.  
`data` | `security_result.description` | The value of the `data` field from the raw log, after undergoing several `gsub` transformations to remove unwanted characters and "N/A" values, is mapped to the `security_result.description` field.  
`description` | `security_result.description` | The value of the `description` field, extracted by the grok parser, is mapped to the `security_result.description` field.  
`first` | `security_result.detection_fields.key` | The string "first" is assigned to the `security_result.detection_fields.key`.  
`first` | `security_result.detection_fields.value` | The value of the `first` field from the raw log is mapped to the `security_result.detection_fields.value`.  
`hostname` | `principal.asset.hostname` | The value of the `hostname` field from the raw log is mapped to the `principal.asset.hostname` and `principal.hostname` fields.  
`hostname` | `principal.hostname` | The value of the `hostname` field from the raw log is mapped to the `principal.asset.hostname` and `principal.hostname` fields.  
`IP` | `principal.asset.ip` | The value of the `IP` field from the raw log is mapped to the `principal.asset.ip` and `principal.ip` fields.  
`IP` | `principal.ip` | The value of the `IP` field from the raw log is mapped to the `principal.asset.ip` and `principal.ip` fields.  
`MAC` | `principal.resource.attribute.labels.key` | The string "MAC" is assigned to the `principal.resource.attribute.labels.key`.  
`MAC` | `principal.resource.attribute.labels.value` | The value of the `MAC` field from the raw log is mapped to the `principal.resource.attribute.labels.value`.  
`medium` | `security_result.detection_fields.key` | The string "medium" is assigned to the `security_result.detection_fields.key`.  
`medium` | `security_result.detection_fields.value` | The value of the `medium` field from the raw log is mapped to the `security_result.detection_fields.value`. The `metadata.event_type` is determined by logic within the parser. If both `principal` and `target` machine IDs are present, it's set to `NETWORK_CONNECTION`. If either `principal` or `target` user IDs are present, it's set to `USER_UNCATEGORIZED`. If only the `principal` machine ID is present, it's set to `STATUS_UPDATE`. Otherwise, it defaults to `GENERIC_EVENT`. The string "EXTREME WIRELESS" is assigned to `metadata.product_name`.  
`prod_event_type` | `metadata.product_event_type` | The value of the `prod_event_type` field from the raw log is mapped to the `metadata.product_event_type` field.  
`port` | `principal.port` | The value of the `port` field from the raw log, converted to an integer, is mapped to the `principal.port` field.  
`problem_summary` | `security_result.summary` | The value of the `problem_summary` field from the raw log is mapped to the `security_result.summary` field.  
`SSID` | `principal.resource.attribute.labels.key` | The string "SSID" is assigned to the `principal.resource.attribute.labels.key`.  
`SSID` | `principal.resource.attribute.labels.value` | The value of the `SSID` field from the raw log is mapped to the `principal.resource.attribute.labels.value`.  
`station` | `principal.asset.hostname` | The value of the `station` field from the raw log is mapped to the `principal.asset.hostname` and `principal.hostname` fields.  
`station` | `principal.hostname` | The value of the `station` field from the raw log is mapped to the `principal.asset.hostname` and `principal.hostname` fields.  
`target_host` | `target.asset.hostname` | The value of the `target_host` field from the raw log is mapped to the `target.asset.hostname` and `target.hostname` fields.  
`target_host` | `target.hostname` | The value of the `target_host` field from the raw log is mapped to the `target.asset.hostname` and `target.hostname` fields.  
`target_ip` | `target.asset.ip` | The value of the `target_ip` field from the raw log is mapped to the `target.asset.ip` and `target.ip` fields.  
`target_ip` | `target.ip` | The value of the `target_ip` field from the raw log is mapped to the `target.asset.ip` and `target.ip` fields.  
`target_port` | `target.port` | The value of the `target_port` field from the raw log, converted to an integer, is mapped to the `target.port` field.  
`target_user` | `target.user.userid` | The value of the `target_user` field from the raw log is mapped to the `target.user.userid` field.  
`user-profile` | `security_result.detection_fields.key` | The string "user profile" is assigned to the `security_result.detection_fields.key`.  
`user-profile` | `security_result.detection_fields.value` | The value of the `user-profile` field from the raw log is mapped to the `security_result.detection_fields.value`.  
`username` | `principal.user.userid` | The value of the `username` field from the raw log is mapped to the `principal.user.userid` field. The string "EXTREME_WIRELESS" is assigned to `metadata.vendor_name`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-wireless-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
