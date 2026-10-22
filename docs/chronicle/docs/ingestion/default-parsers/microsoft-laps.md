---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps/
title: Collect Microsoft LAPS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:02.739026+00:00
---

# Collect Microsoft LAPS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft LAPS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft Windows LAPS (Local Administrator Password Solution) logs to Google Security Operations using the Bindplane agent.

Windows LAPS manages local administrator account passwords on domain-joined devices and generates event log entries for password rotation, policy processing, and management operations. The parser extracts fields from Windows Event Log XML format and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with the Bindplane agent installed
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Windows LAPS configured and deployed in your environment



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

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Windows Event Log and send to Google SecOps

### Locate the configuration file

  * Use the following syntax to locate the configuration file:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          windowseventlog/laps_operational:
            channel: Microsoft-Windows-LAPS/Operational
            max_reads: 100
            poll_interval: 5s
            raw: true
            start_at: end
        
        processors:
          batch:
        
        exporters:
          chronicle/laps:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: WINDOWS_LAPS
            override_log_type: false
            raw_log_field: body
        
        service:
          pipelines:
            logs/laps:
              receivers:
                - windowseventlog/laps_operational
              processors: [batch]
              exporters: [chronicle/laps]
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `channel`: Windows Event Log channel to read from (`Microsoft-Windows-LAPS/Operational`)
    * `max_reads`: Maximum number of log entries to read per poll cycle
    * `poll_interval`: How frequently to poll for new events
    * `start_at`: Where to begin reading (`end` for new events only)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1) (`C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`)
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/laps:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WINDOWS_LAPS
            override_log_type: false
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

Click **File > Save**.

## Restart the Bindplane agent to apply the changes

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
           




## Configure Microsoft Windows LAPS

  1. Type `eventvwr.msc` at an elevated **command prompt** and press ENTER to open **Event Viewer**.
  2. Go to **Applications and Services Logs > Microsoft > Windows > LAPS**.
  3. Expand **LAPS**.
  4. Right-click **LAPS** , and then click **Properties**.
  5. Select the **Enable logging** checkbox.
  6. Click **OK** when asked if the log is enabled.
  7. Click **OK**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Channel | read_only_udm.additional.fields.key | Value is taken from the `Channel` field in the raw log and assigned to the `key` field.  
Channel | read_only_udm.additional.fields.value.string_value | Value is taken from the `Channel` field in the raw log and assigned to the `string_value` field.  
Computer | read_only_udm.principal.hostname | Value is taken from the `Computer` field in the raw log.  
Computer | read_only_udm.principal.asset.hostname | Value is taken from the `Computer` field in the raw log.  
EventData.%1 | read_only_udm.additional.fields.value.string_value | Value is taken from the `EventData.%1` field in the raw log and assigned to the `string_value` field.  
EventId | read_only_udm.metadata.product_event_type | Value is taken from the `EventId` field in the raw log.  
EventId | read_only_udm.security_result.rule_name | Value is taken from the `EventId` field in the raw log and appended to `EventID:`.  
EventRecordID | read_only_udm.metadata.product_log_id | Value is taken from the `EventRecordID` field in the raw log.  
Keywords | read_only_udm.additional.fields.key | Value is taken from the `Keywords` field in the raw log and assigned to the `key` field.  
Keywords | read_only_udm.additional.fields.value.string_value | Value is taken from the `Keywords` field in the raw log and assigned to the `string_value` field.  
Level | read_only_udm.security_result.severity | Value is taken from the `Level` field in the raw log and mapped to: `INFORMATIONAL` for `INFO`, `Informational`, `Information`, `Normal`, `NOTICE`; `ERROR` for `ERROR`, `Error`; `CRITICAL` for `Critical`.  
Opcode | read_only_udm.additional.fields.key | Value is taken from the `Opcode` field in the raw log and assigned to the `key` field.  
Opcode | read_only_udm.additional.fields.value.string_value | Value is taken from the `Opcode` field in the raw log and assigned to the `string_value` field.  
ProcessID | read_only_udm.principal.process.pid | Value is taken from the `ProcessID` field in the raw log.  
ProviderName | read_only_udm.metadata.product_name | Value is taken from the `ProviderName` field in the raw log.  
Task | read_only_udm.additional.fields.key | Value is taken from the `Task` field in the raw log and assigned to the `key` field.  
Task | read_only_udm.additional.fields.value.string_value | Value is taken from the `Task` field in the raw log and assigned to the `string_value` field.  
ThreadID | read_only_udm.additional.fields.key | Value is taken from the `ThreadID` field in the raw log and assigned to the `key` field.  
ThreadID | read_only_udm.additional.fields.value.string_value | Value is taken from the `ThreadID` field in the raw log and assigned to the `string_value` field.  
TimeCreated | read_only_udm.metadata.event_timestamp | Value is taken from the `TimeCreated` field in the raw log, parsed as UNIX_MS timestamp.  
TimeCreated | events.timestamp | Value is taken from the `TimeCreated` field in the raw log, parsed as UNIX_MS timestamp.  
Version | read_only_udm.additional.fields.key | Value is taken from the `Version` field in the raw log and assigned to the `key` field.  
Version | read_only_udm.additional.fields.value.string_value | Value is taken from the `Version` field in the raw log and assigned to the `string_value` field.  
| read_only_udm.additional.fields.key | Assigned the value `EventData_P1`.  
| read_only_udm.metadata.event_type | Conditionally assigned `STATUS_UNCATEGORIZED` if EventId is `7` or `2`, else `GENERIC_EVENT`.  
| read_only_udm.metadata.vendor_name | Assigned the value `Microsoft`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-laps-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
