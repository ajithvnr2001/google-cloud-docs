---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps/
title: Collect Microsoft LAPS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:23:27.577260+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
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

    * `creds_file_path`: Full path to ingestion authentication file (`C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`)
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
