---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-av/
title: Collect Windows Defender Antivirus logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:02.015940+00:00
---

# Collect Windows Defender Antivirus logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-av/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Windows Defender Antivirus logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Windows Defender Antivirus logs to Google Security Operations using Bindplane.

Windows Defender Antivirus is the built-in antimalware engine in Microsoft Windows that provides real-time threat detection, scan results, and protection event logs. The Bindplane agent collects exported Windows Defender event log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator access to Windows endpoints running Windows Defender Antivirus



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
              - C:\Logs\defender-av\*.evtx
            start_at: beginning
        
        exporters:
          chronicle/windows_defender_av:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: WINDOWS_DEFENDER_AV
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/defender_av_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/windows_defender_av
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Set this to the location where you export Windows Defender event logs (for example, `C:\Logs\defender-av\*.evtx`)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `windows_defender_av`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `WINDOWS_DEFENDER_AV`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `defender_av_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/windows_defender_av:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WINDOWS_DEFENDER_AV
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
         




## Configure Windows Defender Antivirus log export

Windows Defender Antivirus logs are stored in the Windows Event Log under `Microsoft-Windows-Windows Defender/Operational`. You need to export these logs to files on disk so the Bindplane agent can collect them.

  1. Create a directory to store the exported log files:
         
         mkdir C:\Logs\defender-av
         

  2. Export Windows Defender Antivirus event logs using `wevtutil`:
         
         wevtutil epl "Microsoft-Windows-Windows Defender/Operational" C:\Logs\defender-av\defender-av.evtx
         

  3. (Optional) Schedule regular exports using Windows Task Scheduler:
         
         $action = New-ScheduledTaskAction -Execute "wevtutil" -Argument 'epl "Microsoft-Windows-Windows Defender/Operational" C:\Logs\defender-av\defender-av.evtx /ow:true'
         $trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -Once -At (Get-Date)
         Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "ExportDefenderLogs" -Description "Export Windows Defender AV logs for Bindplane agent"
         

  4. Verify that the exported log file is being created at `C:\Logs\defender-av`.

  5. Ensure the Bindplane agent `include` path in `config.yaml` matches the export directory.

**Note:** The `/ow:true` flag overwrites the existing export file. Adjust the export strategy based on your log retention requirements. The Bindplane agent service account must have read access to the export directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
OpcodeValue, ThreadID, Channel, engine_version, security_intelligence_version, network_realtime_inspection_engine_version, network_realtime_inspection_security_intelligence_version, rtp_state, oa_state, ioav_state, bm_state, antivirus_security_intelligence_age, antispyware_security_intelligence_age, last_quick_scan_age, last_full_scan_age, antivirus_security_intelligence_creation_time, antispyware_security_intelligence_creation_time, last_quick_scan_start_time, last_quick_scan_end_time, last_quick_scan_source, last_full_scan_start_time, last_full_scan_end_time, last_full_scan_source, product_status | additional.fields | Merged with label maps {key: field name, value: {string_value: field value}} if not empty  
| metadata.description | Set to event-specific description string based on EventID  
| metadata.event_type | Set to "SCAN_HOST" if has_principal true, else "GENERIC_EVENT"; "SCAN_FILE" for EventID 1011,1116,1117  
ProviderGuid | metadata.product_deployment_id | Value from ProviderGuid after removing {}  
| metadata.product_event_type | Set to event-specific product event type string based on EventID  
RecordNumber | metadata.product_log_id | Value copied directly as string  
platform_version | metadata.product_version | Value copied directly  
FWLink | metadata.url_back_to_product | Value copied directly  
| metadata.vendor_name | Set to "Microsoft"  
| metadata.product_name | Set to "Windows Defender AV"  
SourceModuleType | observer.application | Value copied directly  
Domain, _domain | principal.administrative_domain | Value from Domain, or _domain extracted from Detection User using grok for EventID 1116,1117  
Hostname | principal.hostname | Value copied directly  
Process Name | principal.process.file.full_path | Value copied directly for EventID 1116,1117  
ProcessID | principal.process.pid | Value copied directly  
SourceModuleName | principal.resource.name | Value copied directly  
AccountType | principal.user.role_description | Value copied directly  
AccountName | principal.user.user_display_name | Value copied directly  
User, UserID, _account | principal.user.userid | Value from User, or UserID if not empty, or _account extracted from Detection User using grok for EventID 1116,1117  
SourceName | security_result.about.resource.attribute.labels | Merged with label map {key: "SourceName", value: SourceName} if not empty  
| security_result.action | Set to "ALLOW" by default; "BLOCK" for EventID 1116; "QUARANTINE" for EventID 1117  
| security_result.category | Set to "SOFTWARE_MALICIOUS" for EventID 1011,1116,1117  
ActivityID | security_result.detection_fields | Merged with detection_fields {key: "Activity ID", value: ActivityID} if ActivityID not empty and not "-"  
EventID | security_result.description | Set to "EventID: %{EventID}"  
Threat Name | security_result.rule_name | Value copied directly for EventID 1011,1116,1117  
Severity, Level, EventType | security_result.severity | Set to LOW if Severity matches verbose|information|info, MEDIUM if warning|error, HIGH if critical; Severity set from Level (5|4 -> information, 2|3 -> warning, 1 -> critical); or from EventType (ERROR -> %{severity}, INFO -> "INFORMATIONAL", else severity_details)  
Severity Name, severity | security_result.severity_details | Value from Severity Name for EventID 1011,1116,1117; or from severity for EventType not ERROR or INFO  
Threat Name | security_result.summary | Value copied directly for EventID 1011,1116,1117  
Category Name | security_result.threat_name | Value copied directly for EventID 1011,1116,1117  
FWLink | security_result.url_back_to_product | Value copied directly for EventID 1011,1116,1117  
Path | target.file.full_path | Value copied directly for EventID 1116,1117  
| target.hostname | Set to "" for EventID 1117  
Path | target.registry.registry_key | Value copied directly for EventID 1011  
`EventRecordID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`Product Version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`ProviderGuid` | `event.idm.read_only_udm.metadata.product_deployment_id` | Mapped from changelog  
`Hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`xmlns` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`Threat Resource Path` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`Hashes` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`RenderingInfoLevel` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`Action Name` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`Detection Time` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`Threat ID` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`Remediation User` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Status Description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Action ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Additional Actions ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Additional Actions String` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Category ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Detection ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Engine Version` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Error Code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Error Description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Execution ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Execution Name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Origin ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Origin Name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Post Clean Status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Pre Execution Status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Security Intelligence Version` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Severity ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Source ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`State` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Status Code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Type ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Type Name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Culture` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Keywords` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Opcode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Product Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Provider Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RenderingInfoMessage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Task` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Security UserID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EventID` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-av-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
