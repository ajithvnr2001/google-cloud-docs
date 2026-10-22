---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000/
title: Collect HPE BladeSystem c7000 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:40.481914+00:00
---

# Collect HPE BladeSystem c7000 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HPE BladeSystem c7000 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HPE BladeSystem c7000 logs to Google Security Operations using the Bindplane agent.

HPE BladeSystem c7000 is a blade server enclosure that generates syslog messages for hardware events, component status changes, configuration changes, and system alerts. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the HPE BladeSystem c7000
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the HPE BladeSystem Onboard Administrator or StorageGRID Manager



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
          chronicle/hpe_bladesystem_c7000:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: HPE_BLADESYSTEM_C7000
            raw_log_field: body
        
        service:
          pipelines:
            logs/hpe_bladesystem_c7000_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/hpe_bladesystem_c7000
        




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
          chronicle/hpe_bladesystem_c7000:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HPE_BLADESYSTEM_C7000
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
             




## Configure syslog directly in HPE BladeSystem

  1. Sign in to the **BladeSystem** UI.
  2. Go to **Configuration > System Log**.
  3. Click the **Log Options** tab.
  4. Select the **Enable remote system logging** checkbox.
  5. Provide the following configuration details: 
     * **Syslog Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default port is `514`).
     * **Protocol** : The protocol is always **UDP**.
  6. Click **Test Remote Log** and verify logs are received.
  7. Click **Apply** to save.



## Configure syslog in StorageGRID Software

You can configure both the audit message levels within StorageGRID and set up external syslog servers for forwarding these messages.

### Configure StorageGRID audit message levels

  1. Sign in to the **GRID Manager** web UI.
  2. Go to **Configuration > Monitoring > Audit and syslog server**.
  3. For each category of audit message, select the **Normal** audit level from the list.
  4. Click **Save**.



### Configure StorageGRID external syslog server

  1. From the **Audit and syslog server** page, click **Configure external syslog server**.
  2. Provide the following configuration details: 
     * Enter the Bindplane agent IP address.
     * Enter the Bindplane agent port number (default port is `514`).
     * Select the **UDP** or **TCP** protocol, depending on your Bindplane agent configuration.
  3. Click **Continue**.



### Configure syslog events

  1. From the **Manage syslog content** step of the wizard, select each type of audit information you want to send to the external syslog server: 
     * Send audit logs
     * Send security events
     * Send application logs
     * Send access logs
  2. For **Severity** , select **Passthrough** or **7** (Informational).
  3. For **Facility** , select **Passthrough**.
  4. Click **Continue**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`command` | `principal.process.command_line` | Directly mapped from the raw log field "command".  
`component` | `metadata.product_event_type` | Directly mapped from the raw log field "component".  
`component_name` | `additional.fields[0].value.string_value` | Directly mapped from the raw log field "component_name".  
`description` | `security_result.description` | Directly mapped from the raw log field "description" after optional grok parsing.  
`description` | `security_result.detection_fields[0].value` | Extracted from the "description" field using a grok pattern. Represents the current state.  
`description` | `security_result.detection_fields[1].value` | Extracted from the "description" field using a grok pattern. Represents the previous state.  
`description` | `security_result.detection_fields[2].value` | Extracted from the "description" field using a grok pattern. Represents the cause of the state change.  
`event_timestamp` | `metadata.event_timestamp` | Directly mapped from the raw log field "event_timestamp" after date parsing.  
`hostname` | `principal.hostname` | Directly mapped from the raw log field "hostname".  
`hostname` | `principal.asset.hostname` | Copied from the mapped "principal.hostname" field.  
`internal_code` | `additional.fields[1].value.string_value` | Directly mapped from the raw log field "internal_code".  
`priority_id` | `additional.fields[2].value.string_value` | Directly mapped from the raw log field "priority_id".  
| `additional.fields[0].key` | Static value: "Component Name".  
| `additional.fields[1].key` | Static value: "Internal Code".  
| `additional.fields[2].key` | Static value: "Priority Id".  
| `metadata.event_type` | Set to "STATUS_UPDATE" if "principal.hostname" is successfully extracted, otherwise set to "GENERIC_EVENT".  
| `metadata.vendor_name` | Static value: "HP".  
| `metadata.product_name` | Static value: "HPE BladeSystem c7000".  
| `metadata.log_type` | Static value: "HPE_BLADESYSTEM_C7000".  
| `security_result.severity` | Mapped from the "severity" field based on the following logic:- "Critical" -> "CRITICAL"- "Major" -> "HIGH"- "Warning" -> "MEDIUM"- "Info", "Minor" -> "LOW"- Default -> "UNKNOWN_SEVERITY"  
| `security_result.detection_fields[0].key` | Static value: "Current State".  
| `security_result.detection_fields[1].key` | Static value: "Previous State".  
| `security_result.detection_fields[2].key` | Static value: "Cause".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hpe-bladesystem-c7000-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
