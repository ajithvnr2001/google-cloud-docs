---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/acalvio/
title: Collect Acalvio logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:31:07.279144+00:00
---

# Collect Acalvio logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/acalvio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Acalvio logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Acalvio logs to Google Security Operations using the Bindplane agent.

Acalvio ShadowPlex is a deception technology platform that deploys decoys and honeypots across your network to detect lateral movement, reconnaissance, and other adversary activities. It provides real-time alerts on attacker interactions with deception assets.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Acalvio ShadowPlex
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Installed Acalvio ShadowPlex Integration Server
  * Privileged access to the Acalvio ShadowPlex service and instance



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
          chronicle/acalvio:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ACALVIO
            raw_log_field: body
        
        service:
          pipelines:
            logs/acalvio_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/acalvio
        




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
          chronicle/acalvio:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ACALVIO
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
             




## Configure syslog forwarding in Acalvio ShadowPlex

  1. Sign in to the **ShadowPlex Integration Server** UI.
  2. Go to **Settings > SIEM**.
  3. Provide the following configuration details: 
     * Click the **Enable** toggle.
     * **Hostname or IP** : Enter the Bindplane agent IP address (for example, `192.168.1.100`).
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Protocol** : Select **UDP**.
     * **Sensor** : Select the Sensor from which the data is streamed.
  4. Click **Test and Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`adc_email` | `read_only_udm.target.user.email_addresses` | Value taken from `adc_email` field.  
`app` | `read_only_udm.principal.application` | Value taken from `app` field.  
`cat` | `read_only_udm.security_result.summary` | Value taken from `cat` field. If `cat` is `Vulnerability Exploited`, the value is overwritten with the value of `Intrusion_method_used` field.  
`customer_id` | `read_only_udm.metadata.description` | Value is added to the description field: `CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}`  
`deviceProduct` | `read_only_udm.metadata.product_name` | Value taken from `deviceProduct` field.  
`deviceVendor` | `read_only_udm.metadata.vendor_name` | Value taken from `deviceVendor` field.  
`deviceVersion` | `read_only_udm.metadata.product_version` | Value taken from `deviceVersion` field.  
`dstHostName` | `read_only_udm.target.hostname` | Value taken from `dstHostName` field.  
`dstIp` | `read_only_udm.target.ip` | Value taken from `dstIp` field.  
`dstMAC` | `read_only_udm.target.mac` | Value taken from `dstMAC` field.  
`dstPort` | `read_only_udm.target.port` | Value taken from `dstPort` field and converted to integer.  
`incidentid` | `read_only_udm.metadata.product_log_id` | Value taken from `incidentid` field.  
`incidentSubCategory` | `read_only_udm.metadata.product_event_type,`, `read_only_udm.security_result.description` | Value taken from `incidentSubCategory` field.  
`Intrusion_method_used` | `read_only_udm.security_result.summary` | Value taken from `Intrusion_method_used` field if `cat` is `Vulnerability Exploited`.  
`investigation_id` | `read_only_udm.metadata.description` | Value is added to the description field: `CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}`  
`job_id` | `read_only_udm.metadata.description` | Value is added to the description field: `CustomerId: %{customer_id}, JobId: %{job_id}, InvestigationId: %{investigation_id}`  
| `read_only_udm.metadata.event_type` | Set to `GENERIC_EVENT` if `srcIp` is `Unknown` or empty. Set to `STATUS_UPDATE` otherwise.  
| `read_only_udm.principal.resource.type` | Hardcoded to `scan_type`.  
| `read_only_udm.security_result.category` | Determined based on the values of `cat,incidentSubCategory,` and `sr_category` fields.  
| `read_only_udm.security_result.severity` | Set to `HIGH` if `severity` is greater than `7`, `MEDIUM` if `severity` is greater than `3`, and `LOW` otherwise.  
`srcIp` | `read_only_udm.principal.ip` | Value taken from `srcIp` field.  
`startTime` | `read_only_udm.metadata.event_timestamp` | Value taken from`startTime` field and parsed as a timestamp. If `startTime` is empty, the value is set to `%{ts_month} %{ts_day} %{ts_time}`.  
`userIdsUsed` | `read_only_udm.principal.user.userid` | Value taken from `userIdsUsed` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/acalvio-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
