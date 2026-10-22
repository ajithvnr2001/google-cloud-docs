---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/powershell/
title: Collect Microsoft PowerShell logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:18.242796+00:00
---

# Collect Microsoft PowerShell logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/powershell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft PowerShell logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft PowerShell logs to Google Security Operations using the Bindplane agent.

Microsoft PowerShell is a task automation and configuration management framework from Microsoft, consisting of a command-line shell and scripting language. PowerShell logs capture script execution, module activity, and command invocations, providing visibility into PowerShell operations for security monitoring and forensic analysis.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows Server 2016 or later
  * Network connectivity between the Windows host and Google SecOps
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Windows host to configure PowerShell logging and install the Bindplane agent



## Configure PowerShell logging

PowerShell logging must be enabled on Windows hosts before logs can be collected. By default, PowerShell logging is minimal. Enable Script Block Logging to capture detailed PowerShell activity.

### Enable Script Block Logging using group policy

  1. Open the **Local Group Policy Editor** by running `gpedit.msc` as an administrator.
  2. Go to **Computer Configuration > Administrative Templates > Windows Components > Windows PowerShell**.
  3. Double-click **Turn on PowerShell Script Block Logging**.
  4. Select **Enabled**.
  5. Optionally, check **Log script block invocation start / stop events** to capture start and stop events for each script block. Note that this option generates a high volume of logs.
  6. Click **OK**.
  7. Open **Command Prompt** as an administrator and run `gpupdate /force` to apply the policy immediately.



### Enable Script Block Logging using the registry

Alternatively, you can enable Script Block Logging by setting the following registry value:

  1. Open the **Registry Editor** by running `regedit` as an administrator.
  2. Navigate to `HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging`.
  3. If the key does not exist, create it.
  4. Create a new **DWORD (32-bit) Value** named `EnableScriptBlockLogging` and set its value to `1`.
  5. Restart PowerShell sessions for the change to take effect.



PowerShell Script Block Logging writes events to the **Microsoft-Windows-PowerShell/Operational** event log channel with Event ID 4104.

### Optional: Enable module logging

Module Logging records pipeline execution details for specified modules. To enable Module Logging for all modules, do the following:

  1. In the **Local Group Policy Editor** , go to **Computer Configuration > Administrative Templates > Windows Components > Windows PowerShell**.
  2. Double-click **Turn on Module Logging**.
  3. Select **Enabled**.
  4. Click **Show** next to **Module Names**.
  5. Enter `*` to log all modules.
  6. Click **OK** in the **Module Names** window.
  7. Click **OK** in the **Module Logging** window.
  8. Run `gpupdate /force` to apply the policy.



Module Logging events are written to the **Windows PowerShell** event log with Event ID 4103.

### Optional: Enable transcription

Transcription creates a text-based record of all PowerShell session input and output. To enable Transcription, do the following:

  1. In the **Local Group Policy Editor** , go to **Computer Configuration > Administrative Templates > Windows Components > Windows PowerShell**.
  2. Double-click **Turn on PowerShell Transcription**.
  3. Select **Enabled**.
  4. Optionally, specify a **Transcript output directory**. If left blank, transcripts are saved to each user's Documents folder.
  5. Check **Include invocation headers** to include timestamps and metadata.
  6. Click **OK**.
  7. Run `gpupdate /force` to apply the policy.



Transcripts are written to text files with names beginning with `PowerShell_transcript`.

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



## Install Bindplane agent

Install the Bindplane agent on your Windows host according to the following instructions.

### Windows installation

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

## Configure the Bindplane agent to collect PowerShell logs

### Locate the Windows configuration file

  * Locate the Windows configuration file as follows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          windowseventlog/powershell:
            channel: Microsoft-Windows-PowerShell/Operational
            max_reads: 100
            poll_interval: 5s
            raw: true
            start_at: end
        
        processors:
          batch:
        
        exporters:
          chronicle/powershell:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: 'POWERSHELL'
            raw_log_field: body
            override_log_type: false
        
        service:
          pipelines:
            logs/powershell:
              receivers:
                - windowseventlog/powershell
              processors:
                - batch
              exporters:
                - chronicle/powershell
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `channel`: The Windows Event Log channel to collect from. For PowerShell Script Block Logging, use `Microsoft-Windows-PowerShell/Operational`. For Module Logging, use `Windows PowerShell`.
    * `raw`: Set to `true` to send raw Windows Event Log XML to Google SecOps.
    * `start_at`: Set to `end` to collect only new events after the agent starts. Set to `beginning` to collect all existing events.
  * **Exporter configuration:**

    * `<CUSTOMER_ID>`: Replace with the customer ID from the previous step.
    * `creds_file_path`: Full path to the service account JSON key file (Option 1). Copy the credentials file to this location.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.

    * `log_type`: Set to `POWERSHELL` to use the PowerShell parser.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/powershell:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'POWERSHELL'
            raw_log_field: body
            override_log_type: false
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file by clicking **File > Save**.

## Restart the Bindplane agent to apply the changes

### Windows

  * Using Command Prompt or PowerShell as administrator:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        

  * Or using the Services console:

    1. Press `Win+R`, type `services.msc`, and press Enter.
    2. Locate **observIQ OpenTelemetry Collector**.
    3. Right-click and select **Restart**.
    4. Verify the service is running:
           
           sc query observiq-otel-collector
           

    5. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Verify log ingestion

After configuring the Bindplane agent and restarting the service, PowerShell logs should begin flowing to Google SecOps.

  1. Sign in to the Google SecOps console.
  2. Go to **Investigate > Search**.
  3. Run the following search to verify PowerShell logs are being ingested:
         
         metadata.log_type = "POWERSHELL"
         

  4. Verify that events appear with recent timestamps.




PowerShell Script Block Logging events (Event ID 4104) will appear with details of executed script blocks, including the script content, script block ID, and execution context.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
HostId | principal.resource.product_object_id | Unique identifier for the product object associated with the principal resource  
System.Version | metadata.product_version | Version of the product that generated the event  
System.EventId, EventID, winlog.event_id | metadata.product_event_type | Type of event as defined by the product  
Computer, System.Computer, computer, winlog.computer_name | principal.hostname | Hostname of the principal entity  
Computer, System.Computer, computer, winlog.computer_name | principal.asset.hostname | Hostname of the asset associated with the principal  
System.EventRecordID, RecordNumber, winlog.record_id | metadata.product_log_id | Unique identifier for the log entry within the product's logging system  
System.Opcode, opcode, winlog.opcode | metadata.description | Description of the event or additional context  
ProviderGuid, winlog.provider_guid | metadata.product_deployment_id | Unique identifier for the deployment of the product  
System.ProcessID, ProcessID, ExecutionProcessID, execution.process_id, winlog.process.pid | principal.process.pid | Process ID of the principal process  
SourceModuleName | principal.resource.name | Name of the resource associated with the principal  
SourceModuleType | principal.resource.resource_subtype | Subtype of the resource associated with the principal  
security.user_id, UserID, winlog.user.identifier | principal.user.windows_sid | Windows Security Identifier (SID) for the principal user  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
SourceName, winlog.provider_name | metadata.product_name | Name of the product that produced the event  
AccountName, Username, UserName, winlog.user.name | principal.user.userid | User ID of the principal user  
Domain, winlog.user.domain | principal.administrative_domain | Administrative domain of the principal  
Path, target_file, ScriptName, script_name, ContextInfo_Script Name, file_path | target.process.file.full_path | Full path to the file associated with the target process  
HostName, powershell.Host Name, ContextInfo_Host Name | target.hostname | Hostname of the target entity  
HostName, powershell.Host Name, ContextInfo_Host Name | target.asset.hostname | Hostname of the asset associated with the target  
Host ID, HostID, ContextInfo_Host ID | target.asset.asset_id | Unique identifier for the target asset  
Nombre_de_comando, ContextInfo_Command Name, CommandName | target.application | Name of the application associated with the target  
HostApplication, ContextInfo_Host Application | target.process.command_line | Command line used to launch the target process  
ScriptBlockText | target.process.command_line | Command line used to launch the target process  
MessageSourceAddress | principal.ip | IP address of the principal  
MessageSourceAddress | principal.asset.ip | IP address of the asset associated with the principal  
Nombre_de_host | principal.application | Name of the application associated with the principal  
Version_de_host | principal.platform_version | Version of the platform associated with the principal  
Id_de_host | principal.resource.id | Unique identifier for the principal resource  
Application_host | principal.process.file.full_path | Full path to the file associated with the principal process  
HostApplication | principal.process.command_line | Command line used to launch the principal process  
Usuario, admin_domain | principal.user.userid | User ID of the principal user  
Usuario, admin_domain | principal.administrative_domain | Administrative domain of the principal  
CommandLine | principal.process.command_line | Command line used to launch the principal process  
Machine, machine_id | principal.asset.asset_id | Unique identifier for the principal asset  
Machine, platform_software | principal.asset.platform_software.platform | Platform type of the asset (e.g., WINDOWS, LINUX)  
Machine, platform_software | principal.asset.platform_software.platform_version | Version of the platform software on the asset  
MessageSourceAddress | intermediary.ip | IP address of the intermediary entity  
MessageSourceAddress, Hostname | intermediary.hostname | Hostname of the intermediary entity  
MessageSourceAddress, Hostname | intermediary.asset.hostname | Hostname of the asset associated with the intermediary  
MessageSourceAddress | intermediary.port | Port number used by the intermediary  
HostApplication | target.process.command_line | Command line used to launch the target process  
HostId | target.asset.asset_id | Unique identifier for the target asset  
SequenceNumber, ContextInfo_Sequence Number, Sequence Number | security_result.detection_fields | Key-value pairs of additional detection information  
ProviderName | principal.resource.attribute.labels | Labels or attributes associated with the principal resource  
NewEngineState | additional.fields | Additional custom fields not covered by standard UDM schema  
PreviousEngineState | additional.fields | Additional custom fields not covered by standard UDM schema  
ScriptName | additional.fields | Additional custom fields not covered by standard UDM schema  
ManagementGroupName | additional.fields | Additional custom fields not covered by standard UDM schema  
Source | additional.fields | Additional custom fields not covered by standard UDM schema  
RenderedDescription | security_result.description | Description of the security result or action taken  
TenantId | additional.fields | Additional custom fields not covered by standard UDM schema  
UserName | principal.user.userid | User ID of the principal user  
ActivityID | security_result.detection_fields | Key-value pairs of additional detection information  
ExecutionThreadID, execution.thread_id, winlog.process.thread.id | security_result.detection_fields | Key-value pairs of additional detection information  
Output | security_result.detection_fields | Key-value pairs of additional detection information  
Data | security_result.detection_fields | Key-value pairs of additional detection information  
Data_1 | additional.fields | Additional custom fields not covered by standard UDM schema  
data_1 | security_result.detection_fields | Key-value pairs of additional detection information  
Data_2 | security_result.detection_fields | Key-value pairs of additional detection information  
winlog.activity_id | security_result.detection_fields | Key-value pairs of additional detection information  
winlog.api | additional.fields | Additional custom fields not covered by standard UDM schema  
winlog.channel | principal.resource.attribute.labels | Labels or attributes associated with the principal resource  
Offset | additional.fields | Additional custom fields not covered by standard UDM schema  
SeverityValue | security_result.detection_fields | Key-value pairs of additional detection information  
intermediary | intermediary | Details about intermediary entities involved in the event  
security_result | security_result | Overall security result including actions, severities, and detections  
| metadata.vendor_name | Name of the vendor that produced the event  
SourceName | metadata.product_name | Name of the product that produced the event  
`syslog_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Computer` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`Task` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`OpcodeValue` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ThreadID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`AccountType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Offset` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SeverityValue` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NewEngineState", "PreviousEngineState", "HostVersion", "RunspaceId", "SequenceNumber", "EngineVersion" and "PipelineId` | `additional.fields` | Mapped from changelog  
`Payload` | `security_result.detection_fields` | Mapped from changelog  
`Script Name` | `target.file.full_path` | Mapped from changelog  
`SystemTime` | `metadata.event_timestamp` | Mapped from changelog  
`channel", "keywords", "MessageNumber", "MessageTotal", and "ScriptBlockId` | `security_result.detection_fields` | Mapped from changelog  
`System.ProviderName` | `principal.resource.attribute.labels` | Mapped from changelog  
`HostVersion", "RunspaceId", "PipelineId", "EngineVersion", "DetailSequence", "DetailTotal", "SequenceNumber", and "ScriptName` | `additional.fields` | Mapped from changelog  
`System.EventRecordID", "System.Task", "System.Keywords", "System.Opcode", and "System.ThreadID` | `security.detection_fields` | Mapped from changelog  
`EventLevelName` | `security_result.severity` | Mapped from changelog  
`ManagementGroupName", "Source", "TenantId` | `additional_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/powershell-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
