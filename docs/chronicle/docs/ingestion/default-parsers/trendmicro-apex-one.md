---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-one/
title: Collect Trend Micro Apex One logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:28:14.591983+00:00
---

# Collect Trend Micro Apex One logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Apex One logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Apex One logs to Google Security Operations using the Bindplane agent.

Trend Micro Apex One is an endpoint security platform that generates CEF-formatted syslog messages for malware detections, intrusion prevention events, suspicious file activity, web reputation verdicts, and device control events. The parser extracts fields from CEF-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Trend Micro Apex Central server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator access to the Apex Central console



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
          chronicle/trendmicro_apex_one:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TRENDMICRO_APEX_ONE
            raw_log_field: body
        
        service:
          pipelines:
            logs/trendmicro_apex_one_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/trendmicro_apex_one
        




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
          chronicle/trendmicro_apex_one:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TRENDMICRO_APEX_ONE
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
             




## Configure syslog forwarding in Trend Micro Apex One

  1. Sign in to the **Apex Central** console using administrator credentials.
  2. Go to **Administration > Settings > Syslog Settings**.
  3. Check the box labeled **Enable syslog forwarding**.
  4. Configure **Syslog Server Details** : 
     * **Server Address** : Enter the Bindplane agent IP address or FQDN.
     * **Port** : Enter the Bindplane agent port number (for example, `514` for `UDP`).
     * **Protocol** : Select **UDP** as the transmission protocol.
  5. Optional: **Configure Proxy Settings** — Check **Use a SOCKS proxy server** (ensure proxy settings are configured under **Administration > Settings > Proxy Settings**).
  6. **Log Format** : Select **CEF**.
  7. **Frequency** : Define how often logs are forwarded to the Syslog server.
  8. **Log Type** : Select **Security logs** and **Product information**.
  9. Click **Test Connection** to ensure Apex Central can communicate with the Syslog server.
  10. Click **Save** to apply the settings.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`act` | `security_result.action_details` | Directly mapped from the `act` field.  
`ApexCentralHost` | `about.asset.asset_id` | Used as part of the asset_id generation logic. The value "Trend Micro.Apex Central:" is prepended to the `deviceExternalId` field.  
`app` | `target.port` | Directly mapped from the `app` field.  
`cat` | `security_result.category_details` | Directly mapped from the `cat` field.  
`cn1` | `additional.fields[4].value.string_value` | Directly mapped from the `cn1` field. Key is derived from `cn1Label`.  
`cn1Label` | `additional.fields[4].key` | Directly mapped from the `cn1Label` field.  
`cn2` | `additional.fields[6].value.string_value` | Directly mapped from the `cn2` field. Key is derived from `cn2Label`.  
`cn2Label` | `additional.fields[6].key` | Directly mapped from the `cn2Label` field.  
`cn3` | `additional.fields[2].value.string_value` | Directly mapped from the `cn3` field. Key is derived from `cn3Label`.  
`cn3Label` | `additional.fields[2].key` | Directly mapped from the `cn3Label` field.  
`cs1` | `additional.fields[0].value.string_value` | Directly mapped from the `cs1` field. Key is derived from `cs1Label`.  
`cs1Label` | `additional.fields[0].key` | Directly mapped from the `cs1Label` field.  
`cs2` | `additional.fields[1].value.string_value` | Directly mapped from the `cs2` field. Key is derived from `cs2Label`.  
`cs2Label` | `additional.fields[1].key` | Directly mapped from the `cs2Label` field.  
`cs3` | `additional.fields[5].value.string_value` | Directly mapped from the `cs3` field. Key is derived from `cs3Label`.  
`cs3Label` | `additional.fields[5].key` | Directly mapped from the `cs3Label` field.  
`cs4` | `additional.fields[0].value.string_value` | Directly mapped from the `cs4` field. Key is derived from `cs4Label`.  
`cs4Label` | `additional.fields[0].key` | Directly mapped from the `cs4Label` field.  
`cs5` | `additional.fields[2].value.string_value` | Directly mapped from the `cs5` field. Key is derived from `cs5Label`.  
`cs5Label` | `additional.fields[2].key` | Directly mapped from the `cs5Label` field.  
`cs6` | `additional.fields[7].value.string_value` | Directly mapped from the `cs6` field. Key is derived from `cs6Label`.  
`cs6Label` | `additional.fields[7].key` | Directly mapped from the `cs6Label` field.  
`deviceExternalId` | `about.asset.asset_id` | Used as part of the asset_id generation logic. The value "Trend Micro.Apex Central:" is prepended to this field.  
`deviceNtDomain` | `about.administrative_domain` | Directly mapped from the `deviceNtDomain` field.  
`devicePayloadId` | `additional.fields[3].value.string_value` | Directly mapped from the `devicePayloadId` field. Key is hardcoded as "devicePayloadId".  
`deviceProcessName` | `about.process.command_line` | Directly mapped from the `deviceProcessName` field.  
`dhost` | `target.hostname` | Directly mapped from the `dhost` field.  
`dntdom` | `target.administrative_domain` | Directly mapped from the `dntdom` field.  
`dst` | `target.ip` | Directly mapped from the `dst` field.  
`duser` | `target.user.userid`, `target.user.user_display_name` | Directly mapped from the `duser` field.  
`dvchost` | `about.hostname` | Directly mapped from the `dvchost` field.  
`fileHash` | `about.file.full_path` | Directly mapped from the `fileHash` field.  
`fname` | `additional.fields[9].value.string_value` | Directly mapped from the `fname` field. Key is hardcoded as "fname".  
`message` | `metadata.product_event_type` | The CEF header is extracted from the message field.  
`request` | `target.url` | Directly mapped from the `request` field.  
`rt` | `metadata.event_timestamp` | Directly mapped from the `rt` field.  
`shost` | `principal.hostname` | Directly mapped from the `shost` field.  
`src` | `principal.ip` | Directly mapped from the `src` field.  
`TMCMdevicePlatform` | `principal.platform` | Mapped based on logic in the parser. Values are normalized to "WINDOWS", "MAC", or "LINUX".  
`TMCMLogDetectedHost` | `principal.hostname` | Directly mapped from the `TMCMLogDetectedHost` field.  
`TMCMLogDetectedIP` | `principal.ip` | Directly mapped from the `TMCMLogDetectedIP` field. Derived from parser logic based on the presence of other fields. Possible values are "USER_UNCATEGORIZED", "STATUS_UPDATE", or "GENERIC_EVENT". Hardcoded to "TRENDMICRO_APEX_ONE". Hardcoded to "TRENDMICRO_APEX_ONE". Extracted from the CEF header in the `message` field. Hardcoded to "LOW".  
`TMCMdevicePlatform` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`filePath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`cnt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ihost` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`ihost` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`deviceFacility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApexCentralHost` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`ApexCentralHost` | `event.idm.read_only_udm.observer.asset.hostname` | Mapped from changelog  
`cs2` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`cs2` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`suser` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`fname` | `event.idm.read_only_udm.about.file.full_path` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`inter_ip` | `intermediary.ip` and `intermediary.asset.ip` | Mapped from changelog  
`intermediary` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`fileHash` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-one-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
