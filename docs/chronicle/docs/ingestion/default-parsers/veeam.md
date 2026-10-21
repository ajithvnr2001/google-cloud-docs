---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veeam/
title: Collect Veeam logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:29:22.092926+00:00
---

# Collect Veeam logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veeam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Veeam logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Veeam logs to Google Security Operations using the Bindplane agent.

Veeam Backup & Replication is a data protection platform that generates syslog messages for backup jobs, replication tasks, restore operations, and system events. The parser extracts fields from syslog messages using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Veeam Backup & Replication server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Veeam



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
            chronicle/veeam:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VEEAM
                raw_log_field: body
        
        service:
            pipelines:
                logs/veeam_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/veeam
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure syslog for Veeam

  1. Sign in to the **Veeam Backup & Replication** console.
  2. Go to **Menu > Options > SIEM Integrations**.
  3. On the **Syslog servers** section, click **Add**.
  4. Provide the following configuration details: 
     * **Name** : Enter the Bindplane agent IP address and port number (for example, `192.168.1.1:514`).
     * **Transport** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
  5. Click **OK** to save.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application` | `principal.application` | Directly mapped from the `application` field extracted by the grok pattern.  
`CredentialId` | `principal.resource.attribute.labels.[]` | Directly mapped from the `CredentialId` field extracted by the kv filter. A label with key "CredentialId" is created.  
`date_2`, `time_2`, `year` | `metadata.event_timestamp` | The `date_2`, `time_2`, and `year` fields are concatenated and parsed using the `date` filter to create the `metadata.event_timestamp`.  
`date_2`, `time_2` | `metadata.event_timestamp` | The `date_2` and `time_2` fields are concatenated and parsed using the `date` filter to create the `metadata.event_timestamp`.  
`deviceId` | `principal.resource.product_object_id` | Directly mapped from the `deviceId` field extracted by the kv filter.  
`description` | `security_result.description` | Directly mapped from the `description` field extracted by the grok pattern.  
`error_code` | `security_result.detection_fields.[]` | Directly mapped from the `error_code` field extracted by the grok pattern. A label with key "error_code" is created.  
`executing_feature` | `principal.hostname`, `principal.asset.hostname` | Directly mapped from the `executing_feature` field extracted by the grok pattern.  
`host` | `principal.hostname`, `principal.asset.hostname` | Directly mapped from the `host` field extracted by the grok pattern.  
`ManagementIP` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `ManagementIP` field extracted by the kv filter.  
`pid` | `principal.process.pid` | Directly mapped from the `pid` field extracted by the grok pattern.  
`previousSeverity` | `security_result.severity_details` | Directly mapped from the `previousSeverity` field extracted by the grok pattern.  
`prod_event_type` | `metadata.product_event_type` | Directly mapped from the `prod_event_type` field extracted by the grok pattern.  
`query` | `security_result.detection_fields.[]` | Directly mapped from the `query` field extracted by the grok pattern. A label with key "query" is created.  
`reportingAddress` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `reportingAddress` field extracted by the grok pattern.  
`severity` | `security_result.severity` | Mapped from the `severity` field. The value is determined by conditional logic based on the `severity` field (ERROR, MAJOR/WARN, INFO map to specific UDM severity values).  
`src_ip` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `src_ip` field extracted by the grok pattern.  
`summary` | `security_result.summary` | Directly mapped from the `summary` field extracted by the grok pattern.  
`target_ip` | `target.ip`, `target.asset.ip` | Directly mapped from the `target_ip` field extracted by the grok pattern.  
`thread_id` | `security_result.detection_fields.[]` | Directly mapped from the `thread_id` field extracted by the grok pattern. A label with key "thread_id" is created.  
(N/A) | `event_type` | Determined by logic in the parser. If both `principal` and `target` have MID data present, it's `NETWORK_UNCATEGORIZED`. If only `principal` has MID data, it's `STATUS_UPDATE`. Otherwise, it's `GENERIC_EVENT`.  
(N/A) | `metadata.event_type` | Copied from the internally generated `event_type` field.  
(N/A) | `metadata.vendor_name` | Hardcoded to "VEEAM".  
(N/A) | `metadata.product_name` | Hardcoded to "Veeam".  
(N/A) | `event.timestamp` | The event timestamp is taken from the Log Entry's `collection_time` field.  
`enterpriseId` | `additional.fields` | Mapped from changelog  
`recipient_emailid` | `additional.fields` | Mapped from changelog  
`description` | `metadata.description` | Mapped from changelog  
`version` | `additional.fields` | Mapped from changelog  
`categoryId` | `additional.fields` | Mapped from changelog  
`instanceId` | `additional.fields` | Mapped from changelog  
`VbrVersion` | `metadata.product_version` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veeam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
