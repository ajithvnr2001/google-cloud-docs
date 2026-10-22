---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-hyperv/
title: Collect Windows Hyper-V logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:50.612230+00:00
---

# Collect Windows Hyper-V logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-hyperv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Windows Hyper-V logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Windows Hyper-V logs to Google Security Operations using Bindplane.

Windows Hyper-V is a Microsoft hypervisor that generates VM lifecycle, network, storage, and security event logs. The Bindplane agent collects exported Hyper-V event log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Windows Hyper-V host with administrator permissions



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

Install the Bindplane agent on your Windows operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - C:\HyperVLogs\*.evtx
            start_at: beginning
        
        exporters:
          chronicle/windows_hyperv:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: WINDOWS_HYPERV
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/hyperv_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/windows_hyperv
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Set this to the location where you export Hyper-V event logs (for example, `C:\HyperVLogs\*.evtx`)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `windows_hyperv`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `WINDOWS_HYPERV`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `hyperv_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/windows_hyperv:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WINDOWS_HYPERV
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

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
         




## Configure Windows Hyper-V log export

Windows Hyper-V logs are stored as Windows Event Log entries. You need to export these logs to files on disk so the Bindplane agent can collect them.

  1. Create a directory to store the exported log files:
         
         mkdir C:\HyperVLogs
         

  2. Export Hyper-V event logs using `wevtutil`:
         
         wevtutil epl Microsoft-Windows-Hyper-V-VMMS-Admin C:\HyperVLogs\hyperv-vmms-admin.evtx
         wevtutil epl Microsoft-Windows-Hyper-V-Worker-Admin C:\HyperVLogs\hyperv-worker-admin.evtx
         

You can export additional Hyper-V event channels as needed. Available channels include:

     * `Microsoft-Windows-Hyper-V-VMMS-Admin` (Virtual Machine Management Service)
     * `Microsoft-Windows-Hyper-V-Worker-Admin` (VM Worker processes)
     * `Microsoft-Windows-Hyper-V-Hypervisor-Admin` (Hypervisor events)
     * `Microsoft-Windows-Hyper-V-Config-Admin` (Configuration events)
  3. (Optional) Schedule regular exports using PowerShell:
         
         $action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument '/c wevtutil epl Microsoft-Windows-Hyper-V-VMMS-Admin C:\HyperVLogs\hyperv-vmms-admin.evtx /ow:true && wevtutil epl Microsoft-Windows-Hyper-V-Worker-Admin C:\HyperVLogs\hyperv-worker-admin.evtx /ow:true'
         $trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -Once -At (Get-Date)
         Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "ExportHyperVLogs" -Description "Export Hyper-V logs for Bindplane agent"
         

  4. Verify that the exported log files are being created at `C:\HyperVLogs`.

  5. Ensure the Bindplane agent `include` path in `config.yaml` matches the export directory.

**Note:** The `/ow:true` flag overwrites existing export files. The Bindplane agent service account must have read access to the export directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
channel, event_data.data, event_id.id, event_id.qualifiers, keywords, task, SeverityValue, OpcodeValue, EventID, ProviderGuid, ActivityId, Version, RecordNumber, ProcessID, ThreadID, Channel, AccountName, UserID, AccountType, Opcode, SourceModuleName, SourceModuleType | additional.fields | Merged with labels created from these fields  
system_time, EventReceivedTime | metadata.collected_timestamp | Parsed from system_time with formats, or from EventReceivedTime as UNIX or UNIX_MS  
Message | metadata.description | Value copied directly  
EventTime, EventReceivedTime | metadata.event_timestamp | Parsed from EventTime as UNIX or UNIX_MS, or from EventReceivedTime as UNIX or UNIX_MS  
| metadata.event_type | Set to "PROCESS_LAUNCH" if has_principal and has_target_process, else "USER_LOGIN" if has_principal and has_target and not has_target_process, else "STATUS_UPDATE" if has_principal and not has_target, else "USER_RESOURCE_ACCESS" if has_target, else "GENERIC_EVENT"  
provider.event_source | metadata.product_event_type | Value copied directly  
record_id, RecordNumber | metadata.product_log_id | Converted to string from record_id if not empty, or from RecordNumber if not empty  
provider.name, SourceName | metadata.product_name | Value from provider.name if not empty, else SourceName if not empty, else "Microsoft-Windows-Hyper-V"  
Version | metadata.product_version | Converted to string  
message | network.session_duration.nanos | Extracted from message using grok pattern, converted to integer  
Domain | principal.administrative_domain | Value copied directly  
computer | principal.asset.hostname | Value copied directly  
computer, Hostname | principal.hostname | Value from computer if not empty, then from Hostname if not empty  
AccountName | principal.user.role_description | Value copied directly  
AccountType | principal.user.role_name | Value copied directly  
event_data.name | principal.user.user_display_name | Value copied directly  
security.user_id, UserID | principal.user.userid | Value from security.user_id if not empty, then from UserID if not empty  
message | security_result.description | Extracted from message using grok pattern  
message, ActivityId | security_result.detection_fields | Merged with label from nt_status extracted from message using grok, and from ActivityId  
level, Severity | security_result.severity | Set based on level value (1-3 INFORMATIONAL, 4 ERROR, 5 CRITICAL, else UNKNOWN_SEVERITY), or based on Severity (INFO INFORMATIONAL, WARN MEDIUM, ERROR ERROR)  
EventType | security_result.severity_details | Value copied directly  
execution.process_id, ProcessID | target.process.pid | Converted to string from execution.process_id if not empty, or from ProcessID if not empty  
execution.thread_id, ThreadID | target.process.product_specific_process_id | Set to "ThreadID: " from execution.thread_id if not empty, or from ThreadID if not empty  
provider.guid, ProviderGuid | target.resource.id | Value from provider.guid after removing { }, or from ProviderGuid after removing { }  
message | target.resource.product_object_id | Extracted from message using grok pattern  
provider.guid | target.resource.type | Set to "Hyper-V VmSwitch" if not empty  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-hyperv-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
