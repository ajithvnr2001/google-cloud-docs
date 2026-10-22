---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch/
title: Collect Brocade switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:25.570107+00:00
---

# Collect Brocade switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Brocade switch logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Brocade switch logs to Google Security Operations using the Bindplane agent.

Brocade switches (Fibre Channel SAN switches) generate syslog messages for fabric events, zone changes, login/logout activity, and system events. The parser normalizes fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Brocade switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Brocade switch using SSH or Telnet



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
          chronicle/brocade_switch:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BROCADE_SWITCH
            raw_log_field: body
        
        service:
          pipelines:
            logs/brocade_switch_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/brocade_switch
        




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
          chronicle/brocade_switch:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BROCADE_SWITCH
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog export from a Brocade switch

  1. Connect to the Brocade switch using SSH or Telnet with the appropriate credentials.
  2. Run the following command to specify the **IP** address and **Port** of the syslog server (Bindplane):
         
         syslogadmin --set -ip <BINDPLANE_IP> -port 514
         

  3. Run the following command to display the configured syslog servers:
         
         syslogadmin --show -ip
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application` | `additional.fields[].key`: "application"  
`additional.fields[].value.string_value`: | Value extracted from the `application@1588` field in the raw log when the KV_DATA field exists.  
`class` | `additional.fields[].key`: "class"  
`additional.fields[].value.string_value`: | Value extracted from the `class@1588` field in the raw log when the KV_DATA field exists.  
`domain` | `principal.administrative_domain` | Value extracted from the grok pattern matching the `domain` field.  
`Event` | `additional.fields[].key`: "event_category"  
`additional.fields[].value.string_value`: | Value extracted from the `arg0@1588` field in the raw log when the KV_DATA field exists.  
`event_id` | `metadata.product_log_id` | Value extracted from the grok pattern matching the `event_id` field.  
`event_type` | `metadata.product_event_type` | Value extracted from the grok pattern matching the `event_type` field.  
`flags` | `additional.fields[].key`: "flags"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `flags` field.  
`Info` | `metadata.description` | Value extracted from the `Info` field, parsed using grok.  
`interface` | `app_protocol_src` | Value extracted from the `interface@1588` field in the raw log when the KV_DATA field exists. Used to derive `network.application_protocol`.  
`ip` | `principal.ip` | Value extracted from the `ip` field, parsed using grok. Merged into `principal.ip` if it's not the same as the IP extracted from the `Info` field.  
`Info`, `IP Addr` | `principal.ip` | Value extracted from the `IP Addr` field within the `Info` field, parsed using grok.  
`log` | `additional.fields[].key`: "log"  
`additional.fields[].value.string_value`: | Value extracted from the `log@1588` field in the raw log when the KV_DATA field exists.  
`msg` | `metadata.description` | Value extracted from the `msg` field, parsed using grok.  
`msgid` | `additional.fields[].key`: "msgid"  
`additional.fields[].value.string_value`: | Value extracted from the `msgid@1588` field in the raw log when the KV_DATA field exists.  
`prin_host` | `principal.hostname`  
`principal.asset.hostname` | Value extracted from the grok pattern matching the `prin_host` field.  
`product_version` | `metadata.product_version` | Value extracted from the grok pattern matching the `product_version` field.  
`repeat_count` | `additional.fields[].key`: "repeat_count"  
`additional.fields[].value.string_value`: | Value extracted from the `msg` field, parsed using grok.  
`role`, `user_role` | `principal.user.attribute.roles[].name` | Value extracted from the `role@1588` or `user_role` field. If the value is "admin", it's replaced with "Admin".  
`sequence_number` | `additional.fields[].key`: "sequence_number"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `sequence_number` field.  
`severity` | `security_result.severity` | Value extracted from the `severity` field, parsed using grok. Mapped to UDM severity values (INFORMATIONAL, ERROR, CRITICAL, MEDIUM).  
`Status` | `security_result.summary` | Value extracted from the `Status` field.  
`switch_name` | `additional.fields[].key`: "switch_name"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `switch_name` field.  
`target_application` | `target.application` | Value extracted from the grok pattern matching the `target_application` field.  
`time` | `additional.fields[].key`: "time"  
`additional.fields[].value.string_value`: | Value extracted from the `time` field within the `kv_data3` field.  
`timestamp` | `metadata.event_timestamp.seconds` | Value extracted from the `timestamp` field, parsed using the date filter.  
`user` | `principal.user.userid`  
`principal.user.user_display_name` | Value extracted from the `user` or `user@1588` field, parsed using grok. Copied from `principal.hostname`. Copied from `principal.ip`. Copied from `metadata.product_event_type` or set to "STATUS_UPDATE" based on conditions. Copied from the log's `create_time.nanos`. Determined by parser logic based on the values of `has_principal`, `has_target`, `has_userid`, and `event_type`. Can be "SYSTEM_AUDIT_LOG_UNCATEGORIZED", "STATUS_UPDATE", or "GENERIC_EVENT". Hardcoded to "BROCADE_SWITCH". Hardcoded to "BROCADE". Hardcoded to "BROCADE_SWITCH". Derived from the `interface` field or set to "SSH" if the `interface` field contains "SSH".  
`CLI` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`prin_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/brocade-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
