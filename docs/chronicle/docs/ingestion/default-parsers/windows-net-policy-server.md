---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-net-policy-server/
title: Collect Windows Network Policy Server logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:51:54.743126+00:00
---

# Collect Windows Network Policy Server logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-net-policy-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Windows Network Policy Server logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Windows Network Policy Server (NPS) logs to Google Security Operations using Bindplane.

Windows Network Policy Server (NPS) is a Microsoft RADIUS server that generates authentication, authorization, and accounting logs for network access control. The Bindplane agent collects NPS accounting log files and exported event logs directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Windows Server with the Network Policy Server role installed



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - C:\Windows\System32\LogFiles\IN*.log
                start_at: beginning
        
        exporters:
            chronicle/windows_nps:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: WINDOWS_NET_POLICY_SERVER
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/nps_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/windows_nps
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Set this to the location of NPS accounting log files (for example, `C:\Windows\System32\LogFiles\IN*.log`) or exported event logs (for example, `C:\Logs\nps\*.evtx`)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `windows_nps`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `WINDOWS_NET_POLICY_SERVER`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `nps_to_chronicle`: Descriptive name for the pipeline



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
         




## Configure Windows NPS log export

Windows NPS generates two types of logs: NPS accounting log files (IAS format) stored on disk and NPS-related events in the Windows Event Log. You can collect either or both.

### Option 1: Collect NPS accounting log files (default)

NPS accounting log files are stored by default at `C:\Windows\System32\LogFiles\` with filenames starting with`IN`(for example,`IN2301.log`).

  1. Open **Server Manager > Network Policy Server**.
  2. Go to **Accounting > Configure Accounting**.
  3. Verify that **Log to a text file (local)** is enabled.
  4. Note the log file directory (default: `%systemroot%\system32\LogFiles`).
  5. Ensure the Bindplane agent `include` path in `config.yaml` matches the log file location.

**Note:** NPS accounting logs use IAS or DTS format. The default `include` path `C:\Windows\System32\LogFiles\IN*.log` matches the standard NPS log naming convention.



### Option 2: Export NPS event logs

NPS authentication events (Event IDs 6272-6280) are logged in the Windows Security event log.

  1. Create a directory to store the exported log files:
         
         mkdir C:\Logs\nps
         

  2. Export NPS-related Security events using `wevtutil`:
         
         wevtutil epl "Security" /q:"*[System[Provider[@Name='Microsoft-Windows-Security-Auditing'] and (EventID>=6272 and EventID<=6280)]]" C:\Logs\nps\nps-security.evtx
         

  3. (Optional) Schedule regular exports using Windows Task Scheduler:
         
         $action = New-ScheduledTaskAction -Execute "wevtutil" -Argument 'epl "Security" /q:"*[System[Provider[@Name=''Microsoft-Windows-Security-Auditing''] and (EventID>=6272 and EventID<=6280)]]" C:\Logs\nps\nps-security.evtx /ow:true'
         $trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -Once -At (Get-Date)
         Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "ExportNPSLogs" -Description "Export Windows NPS logs for Bindplane agent"
         

  4. Update the Bindplane agent `include` path in `config.yaml` to match:
         
         include:
             - C:\Logs\nps\*.evtx
         

**Note:** The Bindplane agent service account must have read access to the log directory.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`EventID` | `about` | Mapped values (5 total, e.g., `4800, 4801` → `session_about`, `5137, 5141` → `token_about...)  
`SourceName` | `about` | Mapped values (6 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`about_host` | `about` | Merged  
`about_token` | `about` | Merged  
`jsonPayload_about` | `about` | Merged  
`session_about` | `about` | Merged  
`token_about` | `about` | Merged  
`fqdn` | `about.administrative_domain` | Directly mapped  
`param1` | `about.file.full_path` | Directly mapped  
`DCDNSName` | `about.hostname` | Directly mapped  
`LocalEMPrincipalName` | `about.hostname` | Directly mapped  
`EventID` | `about.ip` | Mapped: `4908, 4964` → `address`  
`SourceName` | `about.ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `a...  
`address` | `about.ip` | Merged  
`EventID` | `about.labels` | Mapped values (15 total, e.g., `4625, 4776, 4794` → `keywords_label`, `4774, 4775` → `map...)  
`ImpersonationLevel_label` | `about.labels` | Merged  
`RestrictedAdminMode_label` | `about.labels` | Merged  
`SourceName` | `about.labels` | Mapped values (23 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec...)  
`additional_data_label` | `about.labels` | Merged  
`audit_policy_changes_label` | `about.labels` | Merged  
`ca_label` | `about.labels` | Merged  
`category_label` | `about.labels` | Merged  
`keywords_label` | `about.labels` | Merged  
`labels0` | `about.labels` | Merged  
`labels101` | `about.labels` | Merged  
`labels202` | `about.labels` | Merged  
`labels401` | `about.labels` | Merged  
`level_label` | `about.labels` | Merged  
`mapped_name_label` | `about.labels` | Merged  
`mapping_by_label` | `about.labels` | Merged  
`mapping_channel` | `about.labels` | Merged  
`mapping_opcode` | `about.labels` | Merged  
`system_keyword_label` | `about.labels` | Merged  
`task_label` | `about.labels` | Merged  
`thread_id_label` | `about.labels` | Merged  
`value_is_near_0` | `about.labels` | Mapped: `true` → `labels101`  
`value_is_near_1` | `about.labels` | Mapped: `true` → `labels202`  
`version_label` | `about.labels` | Merged  
`param3` | `about.registry.registry_key` | Directly mapped  
`EventID` | `about.resource.attribute.labels` | Mapped: `4908, 4964` → `label_for_resource_attribute`  
`SourceName` | `about.resource.attribute.labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `l...  
`label_for_resource_attribute` | `about.resource.attribute.labels` | Merged  
`ProviderName` | `about.resource.name` | Directly mapped  
`ProviderKey` | `about.resource.product_object_id` | Directly mapped  
`temp` | `about.resource.product_object_id` | Directly mapped  
`Url` | `about.url` | Directly mapped  
`cacheDenyUrls` | `about.url` | Directly mapped  
`EventID` | `about.user.attribute.labels` | Mapped: `4765, 4766` → `about_user_label`, `4908, 4964` → `about_user_label`, ` 4908, ...  
`SourceName` | `about.user.attribute.labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `a...  
`about_user_label` | `about.user.attribute.labels` | Merged  
`label_for_user_attribute` | `about.user.attribute.labels` | Merged  
`SourceUserName` | `about.user.userid` | Directly mapped  
`about_user_windows_sid` | `about.user.windows_sid` | Directly mapped  
`EventID` | `additiona.fields` | Mapped: `4908, 4964` → `function_label`, `4104, 4105` → `function_label`  
`SourceName` | `additiona.fields` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `f...  
`function_label` | `additiona.fields` | Merged  
`AccountAvailableKeys_label` | `additional.fields` | Merged  
`AccountSupportedEncryptionTypes_label` | `additional.fields` | Merged  
`ActiveProfile_label` | `additional.fields` | Merged  
`AdvancedOptions_label` | `additional.fields` | Merged  
`AppCorrelationID_label` | `additional.fields` | Merged  
`AppId_label` | `additional.fields` | Merged  
`AttributeSyntaxOID_label` | `additional.fields` | Merged  
`AuditResult_label` | `additional.fields` | Merged  
`AuditType_label` | `additional.fields` | Merged  
`AuthProtocol_label` | `additional.fields` | Merged  
`Binding_type_label` | `additional.fields` | Merged  
`Cache_Control_label` | `additional.fields` | Merged  
`ClaimsProvider_label` | `additional.fields` | Merged  
`ClientAdvertizedEncryptionTypes_label` | `additional.fields` | Merged  
`ClientCreationTime_label` | `additional.fields` | Merged  
`CommandName_label` | `additional.fields` | Merged  
`CommandType_label` | `additional.fields` | Merged  
`ConfigAccessPolicy_label` | `additional.fields` | Merged  
`ConfiguredNames_label` | `additional.fields` | Merged  
`Connection_label` | `additional.fields` | Merged  
`Content_Type_label` | `additional.fields` | Merged  
`DCAvailableKeys_label` | `additional.fields` | Merged  
`DCSupportedEncryptionTypes_label` | `additional.fields` | Merged  
`DN_label` | `additional.fields` | Merged  
`DSType_label` | `additional.fields` | Merged  
`DetailSequence_label` | `additional.fields` | Merged  
`DetailTotal_label` | `additional.fields` | Merged  
`Details_label` | `additional.fields` | Merged  
`DeviceAuth_label` | `additional.fields` | Merged  
`DeviceId_label` | `additional.fields` | Merged  
`DirectiveName_label` | `additional.fields` | Merged  
`DisableIntegrityChecks_label` | `additional.fields` | Merged  
`Endpoint_label` | `additional.fields` | Merged  
`EngineVersion_label` | `additional.fields` | Merged  
`ErrorCode_label` | `additional.fields` | Merged  
`EventID` | `additional.fields` | Mapped values (420 total, e.g., `4719` → `additional_field_task_category`, ` 4692, 4693, 4694... )  
`FQDN_label` | `additional.fields` | Merged  
`FWLink_label` | `additional.fields` | Merged  
`FailureType_label` | `additional.fields` | Merged  
`FaultingApplicationPath_label` | `additional.fields` | Merged  
`FaultingModulePath_label` | `additional.fields` | Merged  
`FlightSigning_label` | `additional.fields` | Merged  
`ForwardedIpAddress_label` | `additional.fields` | Merged  
`GroupPolicyApplied_label` | `additional.fields` | Merged  
`HandleId_label` | `additional.fields` | Merged  
`HandleId_label_1` | `additional.fields` | Merged  
`HostID_label` | `additional.fields` | Merged  
`HostId_label` | `additional.fields` | Merged  
`HostName_label` | `additional.fields` | Merged  
`HostVersion_label` | `additional.fields` | Merged  
`Host_label` | `additional.fields` | Merged  
`HypervisorDebug_label` | `additional.fields` | Merged  
`HypervisorLaunchType_label` | `additional.fields` | Merged  
`HypervisorLoadOptions_label` | `additional.fields` | Merged  
`ImpersonationLevel_label` | `additional.fields` | Merged  
`IpAddress_label` | `additional.fields` | Merged  
`KernelDebug_label` | `additional.fields` | Merged  
`KeyLength_label` | `additional.fields` | Merged  
`LmPackageName_label` | `additional.fields` | Merged  
`LoadOptions_label` | `additional.fields` | Merged  
`LogDroppedPacketsEnabled_label` | `additional.fields` | Merged  
`LogSuccessfulConnectionsEnabled_label` | `additional.fields` | Merged  
`MandatoryLabel_label` | `additional.fields` | Merged  
`MessageNumber_label` | `additional.fields` | Merged  
`MessageTotal_label` | `additional.fields` | Merged  
`Message_label` | `additional.fields` | Merged  
`MfaMethod_label` | `additional.fields` | Merged  
`MfaPerformed_label` | `additional.fields` | Merged  
`MulticastFlowsEnabled_label` | `additional.fields` | Merged  
`NetworkIpAddress_label` | `additional.fields` | Merged  
`NetworkLocation_label` | `additional.fields` | Merged  
`NewEngineState_label` | `additional.fields` | Merged  
`NewState_label` | `additional.fields` | Merged  
`NotificationInterval_label` | `additional.fields` | Merged  
`OAuthClientId_label` | `additional.fields` | Merged  
`OAuthGrant_label` | `additional.fields` | Merged  
`ObjectServer_label` | `additional.fields` | Merged  
`OpCorrelationID_label` | `additional.fields` | Merged  
`OperationMode_label` | `additional.fields` | Merged  
`OperationType_label` | `additional.fields` | Merged  
`Operation_label` | `additional.fields` | Merged  
`PacketType_label` | `additional.fields` | Merged  
`Payload_label` | `additional.fields` | Merged  
`PipelineID_label` | `additional.fields` | Merged  
`PipelineId_label` | `additional.fields` | Merged  
`PreAuthEncryptionType_label` | `additional.fields` | Merged  
`PreviousEngineState_label` | `additional.fields` | Merged  
`PrimaryAuth_label` | `additional.fields` | Merged  
`Product_Name_label` | `additional.fields` | Merged  
`Product_Version_label` | `additional.fields` | Merged  
`Profile_label` | `additional.fields` | Merged  
`Profiles_label` | `additional.fields` | Merged  
`ProxyIpAddress_label` | `additional.fields` | Merged  
`ProxyServer_label` | `additional.fields` | Merged  
`RelyingParty_label` | `additional.fields` | Merged  
`RemoteAdminEnabled_label` | `additional.fields` | Merged  
`RemoteEventLogging_label` | `additional.fields` | Merged  
`RequestTicketHash_label` | `additional.fields` | Merged  
`ResourceManager_label` | `additional.fields` | Merged  
`ResponseTicketHash_label` | `additional.fields` | Merged  
`RestrictedAdminMode_label` | `additional.fields` | Merged  
`ReturnCode_label` | `additional.fields` | Merged  
`RunspaceID_label` | `additional.fields` | Merged  
`RunspaceId_label` | `additional.fields` | Merged  
`SequenceNumber_label` | `additional.fields` | Merged  
`Server_label` | `additional.fields` | Merged  
`ServiceAvailableKeys_label` | `additional.fields` | Merged  
`ServiceStartType_label` | `additional.fields` | Merged  
`ServiceSupportedEncryptionTypes_label` | `additional.fields` | Merged  
`ServiceType_label` | `additional.fields` | Merged  
`SessionKeyEncryptionType_label` | `additional.fields` | Merged  
`SkuId_label` | `additional.fields` | Merged  
`SourceName` | `additional.fields` | Mapped values (564 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows se... )  
`SsoBindingValidationLevel_label` | `additional.fields` | Merged  
`StartType_label` | `additional.fields` | Merged  
`SubjectLogonId_label` | `additional.fields` | Merged  
`THostName_label` | `additional.fields` | Merged  
`TargetLinkedLogonId_label` | `additional.fields` | Merged  
`TestSigning_label` | `additional.fields` | Merged  
`Ticket_type_label` | `additional.fields` | Merged  
`TokenBindingProvidedId_label` | `additional.fields` | Merged  
`TokenBindingReferredId_label` | `additional.fields` | Merged  
`TokenElevationType_label` | `additional.fields` | Merged  
`TransactionId_label` | `additional.fields` | Merged  
`TransmittedServices_label` | `additional.fields` | Merged  
`Trigger_label` | `additional.fields` | Merged  
`UserAgentString_label` | `additional.fields` | Merged  
`UserId_label` | `additional.fields` | Merged  
`VirtualAccount_label` | `additional.fields` | Merged  
`VsmLaunchType_label` | `additional.fields` | Merged  
`X_MS_Endpoint_Absolute_Path_label1` | `additional.fields` | Merged  
`acc_mask_label` | `additional.fields` | Merged  
`access_mask_label` | `additional.fields` | Merged  
`account_name_label` | `additional.fields` | Merged  
`acct_authentic` | `additional.fields` | Merged  
`acct_input_octets` | `additional.fields` | Merged  
`acct_input_packets` | `additional.fields` | Merged  
`acct_link_count` | `additional.fields` | Merged  
`acct_output_octets` | `additional.fields` | Merged  
`acct_output_packets` | `additional.fields` | Merged  
`acct_session_time` | `additional.fields` | Merged  
`acct_status_type` | `additional.fields` | Merged  
`activity_id_label` | `additional.fields` | Merged  
`add_label` | `additional.fields` | Merged  
`add_labels202` | `additional.fields` | Merged  
`addition_ObjectClass` | `additional.fields` | Merged  
`additional_ClientAdvertizedEncryptionTypes` | `additional.fields` | Merged  
`additional_ParameterBinding_Add-Type` | `additional.fields` | Merged  
`additional_Requested_Operation_Desired_Access` | `additional.fields` | Merged  
`additional_TargetDomainName` | `additional.fields` | Merged  
`additional_The_SSPI_client_process_is_SYSTEM_PID` | `additional.fields` | Merged  
`additional_access_mask` | `additional.fields` | Merged  
`additional_data_label` | `additional.fields` | Merged  
`additional_field` | `additional.fields` | Merged  
`additional_field_subject_domain_name` | `additional.fields` | Merged  
`additional_field_task_category` | `additional.fields` | Merged  
`additional_information_label` | `additional.fields` | Merged  
`additional_member_name` | `additional.fields` | Merged  
`additional_user_data` | `additional.fields` | Merged  
`attribute_label` | `additional.fields` | Merged  
`attribute_ldap_display_name_label` | `additional.fields` | Merged  
`attribute_selection_label` | `additional.fields` | Merged  
`attributes_preventing_optimization_label` | `additional.fields` | Merged  
`audit_policy_changes_label` | `additional.fields` | Merged  
`audit_schema_version_label` | `additional.fields` | Merged  
`authentication_type_label` | `additional.fields` | Merged  
`backup_type_label` | `additional.fields` | Merged  
`ca_label` | `additional.fields` | Merged  
`cab_id_label` | `additional.fields` | Merged  
`caller_identity_label` | `additional.fields` | Merged  
`caller_user_name_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`certificate_identity_label` | `additional.fields` | Merged  
`charset_label` | `additional.fields` | Merged  
`check_field_server_names` | `additional.fields` | Merged  
`class` | `additional.fields` | Merged  
`class_type_label` | `additional.fields` | Merged  
`clean_pages_modified_label` | `additional.fields` | Merged  
`client_options1_label` | `additional.fields` | Merged  
`client_options_label` | `additional.fields` | Merged  
`client_request_id_label` | `additional.fields` | Merged  
`connect_info` | `additional.fields` | Merged  
`connect_options_label` | `additional.fields` | Merged  
`content_length_label` | `additional.fields` | Merged  
`data_1_label` | `additional.fields` | Merged  
`data_2_label` | `additional.fields` | Merged  
`data_3_label` | `additional.fields` | Merged  
`dirty_pages_modified_label` | `additional.fields` | Merged  
`disposition_label` | `additional.fields` | Merged  
`domain_label` | `additional.fields` | Merged  
`environment_label` | `additional.fields` | Merged  
`event_data_d_word_val_label` | `additional.fields` | Merged  
`event_data_method_label` | `additional.fields` | Merged  
`event_data_p10_label` | `additional.fields` | Merged  
`event_data_p11_label` | `additional.fields` | Merged  
`event_data_p12_label` | `additional.fields` | Merged  
`event_data_p13_label` | `additional.fields` | Merged  
`event_data_p14_label` | `additional.fields` | Merged  
`event_data_p15_label` | `additional.fields` | Merged  
`event_data_p16_label` | `additional.fields` | Merged  
`event_data_p17_label` | `additional.fields` | Merged  
`event_data_p18_label` | `additional.fields` | Merged  
`event_data_p19_label` | `additional.fields` | Merged  
`event_data_p1_label` | `additional.fields` | Merged  
`event_data_p20_label` | `additional.fields` | Merged  
`event_data_p21_label` | `additional.fields` | Merged  
`event_data_p22_label` | `additional.fields` | Merged  
`event_data_p23_label` | `additional.fields` | Merged  
`event_data_p24_label` | `additional.fields` | Merged  
`event_data_p25_label` | `additional.fields` | Merged  
`event_data_p26_label` | `additional.fields` | Merged  
`event_data_p27_label` | `additional.fields` | Merged  
`event_data_p28_label` | `additional.fields` | Merged  
`event_data_p29_label` | `additional.fields` | Merged  
`event_data_p2_label` | `additional.fields` | Merged  
`event_data_p30_label` | `additional.fields` | Merged  
`event_data_p31_label` | `additional.fields` | Merged  
`event_data_p32_label` | `additional.fields` | Merged  
`event_data_p33_label` | `additional.fields` | Merged  
`event_data_p34_label` | `additional.fields` | Merged  
`event_data_p35_label` | `additional.fields` | Merged  
`event_data_p36_label` | `additional.fields` | Merged  
`event_data_p37_label` | `additional.fields` | Merged  
`event_data_p38_label` | `additional.fields` | Merged  
`event_data_p39_label` | `additional.fields` | Merged  
`event_data_p3_label` | `additional.fields` | Merged  
`event_data_p40_label` | `additional.fields` | Merged  
`event_data_p41_label` | `additional.fields` | Merged  
`event_data_p42_label` | `additional.fields` | Merged  
`event_data_p43_label` | `additional.fields` | Merged  
`event_data_p44_label` | `additional.fields` | Merged  
`event_data_p45_label` | `additional.fields` | Merged  
`event_data_p46_label` | `additional.fields` | Merged  
`event_data_p47_label` | `additional.fields` | Merged  
`event_data_p48_label` | `additional.fields` | Merged  
`event_data_p49_label` | `additional.fields` | Merged  
`event_data_p4_label` | `additional.fields` | Merged  
`event_data_p50_label` | `additional.fields` | Merged  
`event_data_p51_label` | `additional.fields` | Merged  
`event_data_p52_label` | `additional.fields` | Merged  
`event_data_p53_label` | `additional.fields` | Merged  
`event_data_p54_label` | `additional.fields` | Merged  
`event_data_p55_label` | `additional.fields` | Merged  
`event_data_p56_label` | `additional.fields` | Merged  
`event_data_p57_label` | `additional.fields` | Merged  
`event_data_p58_label` | `additional.fields` | Merged  
`event_data_p59_label` | `additional.fields` | Merged  
`event_data_p5_label` | `additional.fields` | Merged  
`event_data_p60_label` | `additional.fields` | Merged  
`event_data_p61_label` | `additional.fields` | Merged  
`event_data_p62_label` | `additional.fields` | Merged  
`event_data_p63_label` | `additional.fields` | Merged  
`event_data_p64_label` | `additional.fields` | Merged  
`event_data_p65_label` | `additional.fields` | Merged  
`event_data_p66_label` | `additional.fields` | Merged  
`event_data_p67_label` | `additional.fields` | Merged  
`event_data_p68_label` | `additional.fields` | Merged  
`event_data_p69_label` | `additional.fields` | Merged  
`event_data_p6_label` | `additional.fields` | Merged  
`event_data_p70_label` | `additional.fields` | Merged  
`event_data_p71_label` | `additional.fields` | Merged  
`event_data_p72_label` | `additional.fields` | Merged  
`event_data_p73_label` | `additional.fields` | Merged  
`event_data_p74_label` | `additional.fields` | Merged  
`event_data_p75_label` | `additional.fields` | Merged  
`event_data_p76_label` | `additional.fields` | Merged  
`event_data_p77_label` | `additional.fields` | Merged  
`event_data_p78_label` | `additional.fields` | Merged  
`event_data_p79_label` | `additional.fields` | Merged  
`event_data_p7_label` | `additional.fields` | Merged  
`event_data_p80_label` | `additional.fields` | Merged  
`event_data_p81_label` | `additional.fields` | Merged  
`event_data_p82_label` | `additional.fields` | Merged  
`event_data_p83_label` | `additional.fields` | Merged  
`event_data_p84_label` | `additional.fields` | Merged  
`event_data_p85_label` | `additional.fields` | Merged  
`event_data_p86_label` | `additional.fields` | Merged  
`event_data_p87_label` | `additional.fields` | Merged  
`event_data_p88_label` | `additional.fields` | Merged  
`event_data_p89_label` | `additional.fields` | Merged  
`event_data_p8_label` | `additional.fields` | Merged  
`event_data_p90_label` | `additional.fields` | Merged  
`event_data_p91_label` | `additional.fields` | Merged  
`event_data_p92_label` | `additional.fields` | Merged  
`event_data_p9_label` | `additional.fields` | Merged  
`event_data_param1_label` | `additional.fields` | Merged  
`event_data_param2_label` | `additional.fields` | Merged  
`event_data_param3_label` | `additional.fields` | Merged  
`event_data_param4_label` | `additional.fields` | Merged  
`event_data_param5_label` | `additional.fields` | Merged  
`event_data_param6_label` | `additional.fields` | Merged  
`event_data_param7_label` | `additional.fields` | Merged  
`event_data_processing_mode_label` | `additional.fields` | Merged  
`event_data_processing_time_in_milliseconds_label` | `additional.fields` | Merged  
`event_data_stage_label` | `additional.fields` | Merged  
`event_data_support_info1_label` | `additional.fields` | Merged  
`event_data_support_info2_label` | `additional.fields` | Merged  
`event_data_thumbprint_label` | `additional.fields` | Merged  
`event_id_label` | `additional.fields` | Merged  
`event_in_seq_label` | `additional.fields` | Merged  
`event_time_label` | `additional.fields` | Merged  
`exception_info_label` | `additional.fields` | Merged  
`expensive_search_operations_label` | `additional.fields` | Merged  
`failure_reason_label` | `additional.fields` | Merged  
`framework_version_label` | `additional.fields` | Merged  
`hashed_bucket_label` | `additional.fields` | Merged  
`inefficient_search_operations_label` | `additional.fields` | Merged  
`install_date_label` | `additional.fields` | Merged  
`is_column_permission_label` | `additional.fields` | Merged  
`is_dac_label` | `additional.fields` | Merged  
`keywords_label` | `additional.fields` | Merged  
`label01` | `additional.fields` | Merged  
`label02` | `additional.fields` | Merged  
`label03` | `additional.fields` | Merged  
`label461` | `additional.fields` | Merged  
`label462` | `additional.fields` | Merged  
`label463` | `additional.fields` | Merged  
`label46561` | `additional.fields` | Merged  
`label46562` | `additional.fields` | Merged  
`label46563` | `additional.fields` | Merged  
`label46564` | `additional.fields` | Merged  
`label46565` | `additional.fields` | Merged  
`label46571` | `additional.fields` | Merged  
`label46572` | `additional.fields` | Merged  
`label47681` | `additional.fields` | Merged  
`label47682` | `additional.fields` | Merged  
`label501` | `additional.fields` | Merged  
`label601` | `additional.fields` | Merged  
`label_for_additional_fields` | `additional.fields` | Merged  
`labels0` | `additional.fields` | Merged  
`labels401` | `additional.fields` | Merged  
`labels46411` | `additional.fields` | Merged  
`labels46412` | `additional.fields` | Merged  
`labels46413` | `additional.fields` | Merged  
`labels46414` | `additional.fields` | Merged  
`labels46415` | `additional.fields` | Merged  
`labels46416` | `additional.fields` | Merged  
`labels46417` | `additional.fields` | Merged  
`level_label` | `additional.fields` | Merged  
`logon_guid_label` | `additional.fields` | Merged  
`logon_id_label` | `additional.fields` | Merged  
`mapped_name_label` | `additional.fields` | Merged  
`mapping_by_label` | `additional.fields` | Merged  
`mapping_channel` | `additional.fields` | Merged  
`mapping_opcode` | `additional.fields` | Merged  
`method` | `additional.fields` | Merged  
`method_executed_label` | `additional.fields` | Merged  
`namespace_label` | `additional.fields` | Merged  
`nas_port_type_label` | `additional.fields` | Merged  
`network_information_label` | `additional.fields` | Merged  
`new_obj_dn_label` | `additional.fields` | Merged  
`new_target_user_name_label` | `additional.fields` | Merged  
`number_of_search_operations_label` | `additional.fields` | Merged  
`object_class_label` | `additional.fields` | Merged  
`object_dn_label` | `additional.fields` | Merged  
`operation_type_label` | `additional.fields` | Merged  
`p10_label` | `additional.fields` | Merged  
`p2_label` | `additional.fields` | Merged  
`p3_label` | `additional.fields` | Merged  
`p4_label` | `additional.fields` | Merged  
`p5_label` | `additional.fields` | Merged  
`p6_label` | `additional.fields` | Merged  
`p7_label` | `additional.fields` | Merged  
`p8_label` | `additional.fields` | Merged  
`p9_label` | `additional.fields` | Merged  
`package_label` | `additional.fields` | Merged  
`packet_data_size_label` | `additional.fields` | Merged  
`pages_preread_from_disk_label` | `additional.fields` | Merged  
`pages_read_from_disk_label` | `additional.fields` | Merged  
`pages_referenced_label` | `additional.fields` | Merged  
`parent_id_label` | `additional.fields` | Merged  
`payload_label` | `additional.fields` | Merged  
`perm_consumer_label` | `additional.fields` | Merged  
`permission_bitmask_label` | `additional.fields` | Merged  
`platform_label` | `additional.fields` | Merged  
`pooled_connection_label` | `additional.fields` | Merged  
`problem_signature_label` | `additional.fields` | Merged  
`protocol_seq_label` | `additional.fields` | Merged  
`proxy_dns_name_label` | `additional.fields` | Merged  
`query_string_label` | `additional.fields` | Merged  
`reason_code` | `additional.fields` | Merged  
`reason_code_labels` | `additional.fields` | Merged  
`report_id_label` | `additional.fields` | Merged  
`report_status_label` | `additional.fields` | Merged  
`req_id_label` | `additional.fields` | Merged  
`request_detail_label` | `additional.fields` | Merged  
`request_id_label` | `additional.fields` | Merged  
`request_path_label` | `additional.fields` | Merged  
`requester_label` | `additional.fields` | Merged  
`response_detail_label` | `additional.fields` | Merged  
`response_label` | `additional.fields` | Merged  
`returned_entries_label` | `additional.fields` | Merged  
`search_scope_label` | `additional.fields` | Merged  
`search_time_ms_label` | `additional.fields` | Merged  
`sequence_group_id_label` | `additional.fields` | Merged  
`sequence_number_label` | `additional.fields` | Merged  
`session_label` | `additional.fields` | Merged  
`sidtype_label` | `additional.fields` | Merged  
`source_group_label` | `additional.fields` | Merged  
`source_module_label` | `additional.fields` | Merged  
`span_id_label` | `additional.fields` | Merged  
`stage` | `additional.fields` | Merged  
`starting_node_label` | `additional.fields` | Merged  
`statement_label` | `additional.fields` | Merged  
`subject_key_label` | `additional.fields` | Merged  
`subject_label` | `additional.fields` | Merged  
`subject_logon_id_label` | `additional.fields` | Merged  
`subject_logon_id_label_1` | `additional.fields` | Merged  
`subject_machine_name_label` | `additional.fields` | Merged  
`subject_user_name_label` | `additional.fields` | Merged  
`suppress_count_label` | `additional.fields` | Merged  
`suppress_label` | `additional.fields` | Merged  
`system_keyword_label` | `additional.fields` | Merged  
`target_label` | `additional.fields` | Merged  
`target_labels` | `additional.fields` | Merged  
`target_logon_id_label` | `additional.fields` | Merged  
`target_relying_party_label` | `additional.fields` | Merged  
`target_user_id_label` | `additional.fields` | Merged  
`temp_additional_event_category` | `additional.fields` | Merged  
`temp_additional_event_type` | `additional.fields` | Merged  
`temp_additional_insert_id` | `additional.fields` | Merged  
`temp_additional_log_name` | `additional.fields` | Merged  
`temp_additional_qualifiers` | `additional.fields` | Merged  
`temp_additional_time_gen` | `additional.fields` | Merged  
`temp_additional_time_written` | `additional.fields` | Merged  
`temp_query` | `additional.fields` | Merged  
`these_files_may_be_available_here_label` | `additional.fields` | Merged  
`thread_id_label` | `additional.fields` | Merged  
`through_proxy_label` | `additional.fields` | Merged  
`ticket_options_label` | `additional.fields` | Merged  
`time_interval_hours_label` | `additional.fields` | Merged  
`token_@_xmlns_` | `additional.fields` | Merged  
`token_subject_logon_id` | `additional.fields` | Merged  
`trace_id_label` | `additional.fields` | Merged  
`transaction_id_label` | `additional.fields` | Merged  
`uf_type_label` | `additional.fields` | Merged  
`uf_version_label` | `additional.fields` | Merged  
`used_indexes_label` | `additional.fields` | Merged  
`user_data_0x8000003F_@_xmlns__label` | `additional.fields` | Merged  
`user_data_0x8000003F_process_id_label` | `additional.fields` | Merged  
`user_data_0x8000003F_providers_in_host_label` | `additional.fields` | Merged  
`user_data_0x8000003F_quota_name_label` | `additional.fields` | Merged  
`user_data_0x8000003F_quota_threshold_label` | `additional.fields` | Merged  
`user_data_0x8000003F_quota_value_label` | `additional.fields` | Merged  
`user_defined_event_id_label` | `additional.fields` | Merged  
`user_defined_information_label` | `additional.fields` | Merged  
`user_id_label` | `additional.fields` | Merged  
`value_is_near_1` | `additional.fields` | Mapped: `true` → `add_labels202`  
`var_client_name` | `additional.fields` | Merged  
`var_workstation_name` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`visited_entries_label` | `additional.fields` | Merged  
`vsad_label` | `additional.fields` | Merged  
`x_ms_adfs_proxy_client_ip_label` | `additional.fields` | Merged  
`x_ms_client_application_label` | `additional.fields` | Merged  
`x_ms_client_user_agent_label` | `additional.fields` | Merged  
`x_ms_forwarded_client_ip_label` | `additional.fields` | Merged  
`x_ms_proxy_label` | `additional.fields` | Merged  
`xmlns_label1` | `additional.fields` | Merged  
`LogonType` | `extensions.auth.auth_details` | Renamed/mapped  
`EventID` | `extensions.auth.mechanism` | Mapped: `4908, 4964` → `auth_mechanism1`, `4908, 4964` → `auth_mechanism`, ` 1202,1203...  
`SourceName` | `extensions.auth.mechanism` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `a...  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`auth_mechanism1` | `extensions.auth.mechanism` | Merged  
`auth_type` | `extensions.auth.type` | Renamed/mapped  
`EventID` | `intermediary` | Mapped: `4908, 4964` → `intermediary_label`, ` 8015, 8018, 8019, 8020, 8027, 8033, 8010, ...  
`SourceName` | `intermediary` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `i...  
`intermediary_label` | `intermediary` | Merged  
`ComputerName` | `intermediary.hostname` | Directly mapped  
`HostName` | `intermediary.hostname` | Directly mapped  
`Hostname` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`metadata_description` | `metadata.description` | Directly mapped  
`Detection Time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`EventReceivedTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`EventTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`NewTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`PasswordLastSet` | `metadata.event_timestamp` | Parsed as `M/dd/yyyy H:mm:ss A`  
`PreviousTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ValidFrom` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ValidTo` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_time` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`event_timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`eventtime1` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`receiveTimestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`syslog_ts` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss Z`  
`EventID` | `metadata.event_type` | Mapped values (18 total, e.g., `4908, 4964` → `STATUS_UPDATE`, `4908, 4964` → `GENERIC_... )  
`SourceName` | `metadata.event_type` | Mapped values (9 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`udm_event_type` | `metadata.event_type` | Renamed/mapped  
`ProviderGuid` | `metadata.product_deployment_id` | Renamed/mapped  
`EventID` | `metadata.product_event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`RecordNumber` | `metadata.product_log_id` | Renamed/mapped  
`SourceName` | `metadata.product_name` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `M...  
`EventID` | `metadata.vendor_name` | Mapped: `4908, 4964` → `Microsoft`  
`SourceName` | `metadata.vendor_name` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `M...  
`app_protocol` | `network.application_protocol` | Renamed/mapped  
`Direction` | `network.direction` | Renamed/mapped  
`EventID` | `network.dns.questions` | Mapped: `4908, 4964` → `questions`, `1014, 3008` → `questions`  
`SourceName` | `network.dns.questions` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `q...  
`questions` | `network.dns.questions` | Merged  
`http_method` | `network.http.method` | Directly mapped  
`_userAgentString` | `network.http.parsed_user_agent` | Renamed/mapped  
`_userAgentString` | `network.http.user_agent` | Directly mapped  
`ac-user-agent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Renamed/mapped  
`AcctMultiSsnID` | `network.session_id` | Directly mapped  
`SessionID` | `network.session_id` | Directly mapped  
`SessionId` | `network.session_id` | Directly mapped  
`SessionName` | `network.session_id` | Renamed/mapped  
`session_id` | `network.session_id` | Directly mapped  
`CAName` | `network.tls.client.certificate.issuer` | Directly mapped  
`Issuer` | `network.tls.client.certificate.issuer` | Renamed/mapped  
`LocalMMIssuingCA` | `network.tls.client.certificate.issuer` | Directly mapped  
`CertificateHash` | `network.tls.client.certificate.md5` | Directly mapped  
`SerialNumber` | `network.tls.client.certificate.serial` | Directly mapped  
`client_certificate_serial` | `network.tls.client.certificate.serial` | Renamed/mapped  
`CertificateHash` | `network.tls.client.certificate.sha1` | Directly mapped  
`client_certificate_sha1` | `network.tls.client.certificate.sha1` | Renamed/mapped  
`CertificateHash` | `network.tls.client.certificate.sha256` | Directly mapped  
`client_certificate_subject` | `network.tls.client.certificate.subject` | Renamed/mapped  
`RemoteMMIssuingCA` | `network.tls.server.certificate.issuer` | Directly mapped  
`server_certificate_subject` | `network.tls.server.certificate.subject` | Renamed/mapped  
`SourceModuleType` | `observer.application` | Renamed/mapped  
`IssuingKDC` | `observer.asset.asset_id` | Directly mapped  
`EventID` | `observer.labels` | Mapped: `4908, 4964` → `verb_label`, `4908, 4964` → `source_module_label`  
`SourceName` | `observer.labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `v...  
`source_module_label` | `observer.labels` | Merged  
`verb_label` | `observer.labels` | Merged  
`AccountDomain` | `principal.administrative_domain` | Renamed/mapped  
`CallerDomainName` | `principal.administrative_domain` | Renamed/mapped  
`Domain` | `principal.administrative_domain` | Renamed/mapped  
`SubjectDomainName` | `principal.administrative_domain` | Renamed/mapped  
`administrative_domain` | `principal.administrative_domain` | Directly mapped  
`principal_domain_name` | `principal.administrative_domain` | Renamed/mapped  
`principal_application` | `principal.application` | Renamed/mapped  
`src_application` | `principal.application` | Renamed/mapped  
`device-uid` | `principal.asset.asset_id` | Directly mapped  
`EventID` | `principal.asset.attribute.labels` | Mapped values (7 total, e.g., `4908, 4964` → `server_principal_id_label`, `4908, 4964` ... )  
`SourceName` | `principal.asset.attribute.labels` | Mapped values (7 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`label_for_principal_asset` | `principal.asset.attribute.labels` | Merged  
`server_instance_name_label` | `principal.asset.attribute.labels` | Merged  
`server_principal_id_label` | `principal.asset.attribute.labels` | Merged  
`server_principal_name_label` | `principal.asset.attribute.labels` | Merged  
`server_principal_sid_label` | `principal.asset.attribute.labels` | Merged  
`session_server_principal_name_label` | `principal.asset.attribute.labels` | Merged  
`token_new` | `principal.asset.attribute.labels` | Merged  
`hardware` | `principal.asset.hardware` | Merged  
`Hostname` | `principal.asset.hostname` | Directly mapped  
`auth_server_host` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`principal_asset_hostname` | `principal.asset.hostname` | Renamed/mapped  
`principal_hostname` | `principal.asset.hostname` | Directly mapped  
`FramedIPAddress` | `principal.asset.ip` | Merged  
`SourceName` | `principal.asset.ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `F...  
`calling_station_id` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`var_domain_name` | `principal.asset.network_domain` | Directly mapped  
`MachineInventory` | `principal.asset.platform_software.platform_version` | Renamed/mapped  
`device-platform-version` | `principal.asset.platform_software.platform_version` | Directly mapped  
`platform_version` | `principal.asset.platform_software.platform_version` | Renamed/mapped  
`device-uid-global` | `principal.asset.product_object_id` | Directly mapped  
`EventID` | `principal.asset.software` | Mapped: `4908, 4964` → `software_version`  
`SourceName` | `principal.asset.software` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `s...  
`software_version` | `principal.asset.software` | Merged  
`ClientRealm` | `principal.domain.name` | Directly mapped  
`Path` | `principal.file.full_path` | Directly mapped  
`PrincipalFileName` | `principal.file.full_path` | Renamed/mapped  
`Hostname` | `principal.hostname` | Directly mapped  
`auth_server_host` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`principal_asset_hostname` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`EventID` | `principal.ip` | Mapped: `4625, 4776, 4794` → `temp_ip`, `4908, 4964` → `ip_address`, `4908, 4964` → ...  
`FramedIPAddress` | `principal.ip` | Merged  
`SourceName` | `principal.ip` | Mapped values (5 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu...  
`calling_station_id` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`ip_address` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`principal_ip1` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`temp_ip` | `principal.ip` | Merged  
`AdvancedOptions_label` | `principal.labels` | Merged  
`ClientCreationTime_label` | `principal.labels` | Merged  
`ConfigAccessPolicy_label` | `principal.labels` | Merged  
`DisableIntegrityChecks_label` | `principal.labels` | Merged  
`EventID` | `principal.labels` | Mapped values (28 total, e.g., `4692, 4693, 4694, 4695, 4983, 4984` → `subject_logon_id_lab...  
`FlightSigning_label` | `principal.labels` | Merged  
`HypervisorDebug_label` | `principal.labels` | Merged  
`HypervisorLaunchType_label` | `principal.labels` | Merged  
`HypervisorLoadOptions_label` | `principal.labels` | Merged  
`KernelDebug_label` | `principal.labels` | Merged  
`LoadOptions_label` | `principal.labels` | Merged  
`RemoteEventLogging_label` | `principal.labels` | Merged  
`SourceName` | `principal.labels` | Mapped values (36 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`SubjectLogonId_label` | `principal.labels` | Merged  
`TestSigning_label` | `principal.labels` | Merged  
`VsmLaunchType_label` | `principal.labels` | Merged  
`acc_mask_label` | `principal.labels` | Merged  
`account_name_label` | `principal.labels` | Merged  
`caller_user_name_label` | `principal.labels` | Merged  
`data_1_label` | `principal.labels` | Merged  
`data_2_label` | `principal.labels` | Merged  
`data_3_label` | `principal.labels` | Merged  
`label01` | `principal.labels` | Merged  
`label03` | `principal.labels` | Merged  
`label461` | `principal.labels` | Merged  
`label501` | `principal.labels` | Merged  
`logon_id_label` | `principal.labels` | Merged  
`method_executed_label` | `principal.labels` | Merged  
`namespace_label` | `principal.labels` | Merged  
`subject_logon_id_label` | `principal.labels` | Merged  
`subject_machine_name_label` | `principal.labels` | Merged  
`subject_user_name_label` | `principal.labels` | Merged  
`user_id_label` | `principal.labels` | Merged  
`var_client_name` | `principal.labels` | Merged  
`var_workstation` | `principal.labels` | Merged  
`var_workstation_name` | `principal.labels` | Merged  
`CallingStationID` | `principal.mac` | Mapped: `(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$` → `CallingStationID`  
`EventID` | `principal.mac` | Mapped: `4908, 4964` → `principal_mac`  
`SourceName` | `principal.mac` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `p...  
`calling_station_id` | `principal.mac` | Merged  
`device-mac` | `principal.mac` | Merged  
`mac` | `principal.mac` | Merged  
`principal_mac` | `principal.mac` | Merged  
`principal_port` | `principal.port` | Renamed/mapped  
`AccessMask` | `principal.process.access_mask` | Renamed/mapped  
`am` | `principal.process.access_mask` | Renamed/mapped  
`ParentCommandLine` | `principal.process.command_line` | Renamed/mapped  
`ProcessName` | `principal.process.command_line` | Renamed/mapped  
`principal_process_command_line` | `principal.process.command_line` | Renamed/mapped  
`task_arguments` | `principal.process.command_line` | Renamed/mapped  
`CallerProcessName` | `principal.process.file.full_path` | Renamed/mapped  
`ParentImage` | `principal.process.file.full_path` | Renamed/mapped  
`SourceImage` | `principal.process.file.full_path` | Renamed/mapped  
`principal_process_name` | `principal.process.file.full_path` | Renamed/mapped  
`task_command` | `principal.process.file.full_path` | Renamed/mapped  
`SourceName` | `principal.process.file.names` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `v...  
`var_process_parent_name` | `principal.process.file.names` | Merged  
`ParentProcessId` | `principal.process.parent_process.pid` | Renamed/mapped  
`principal_process_pid` | `principal.process.pid` | Renamed/mapped  
`process_id` | `principal.process.pid` | Renamed/mapped  
`ObjectPath` | `principal.registry.registry_key` | Renamed/mapped  
`EventID` | `principal.resource.attribute.permissions` | Mapped: `4659, 5140, 5145` → `permissions`  
`SourceName` | `principal.resource.attribute.permissions` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `p...  
`permissions` | `principal.resource.attribute.permissions` | Merged  
`principal_resource_product_object_id` | `principal.resource.product_object_id` | Renamed/mapped  
`EventID` | `principal.user.attribute.labels` | Mapped: `4908, 4964` → `label_for_principal_user`, `4908, 4964` → `user_label`, ` 4908...  
`SourceName` | `principal.user.attribute.labels` | Mapped values (6 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`account_name_label` | `principal.user.attribute.labels` | Merged  
`label_for_principal_user` | `principal.user.attribute.labels` | Merged  
`sam_acc_label` | `principal.user.attribute.labels` | Merged  
`sid_history_label` | `principal.user.attribute.labels` | Merged  
`subject_user_sid_name_label` | `principal.user.attribute.labels` | Merged  
`user_label` | `principal.user.attribute.labels` | Merged  
`EventID` | `principal.user.attribute.roles` | Mapped values (20 total, e.g., `4908, 4964` → `roles`, ` 7000, 7011, 7022, 7023, 7024, 702... )  
`SourceName` | `principal.user.attribute.roles` | Mapped values (63 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`roles` | `principal.user.attribute.roles` | Merged  
`Subject_Logon_GUID` | `principal.user.product_object_id` | Directly mapped  
`principal_user_display_name` | `principal.user.user_display_name` | Renamed/mapped  
`AccountName` | `principal.user.userid` | Renamed/mapped  
`AccountToReset` | `principal.user.userid` | Renamed/mapped  
`CallerUserName` | `principal.user.userid` | Renamed/mapped  
`SubjectMachineName` | `principal.user.userid` | Renamed/mapped  
`SubjectUserName` | `principal.user.userid` | Renamed/mapped  
`principal_user_id` | `principal.user.userid` | Renamed/mapped  
`subject_machine_name` | `principal.user.userid` | Renamed/mapped  
`principal_user_windows_sid` | `principal.user.windows_sid` | Renamed/mapped  
`subject_machine_sid` | `principal.user.windows_sid` | Directly mapped  
`EventID` | `security_result` | Mapped values (5 total, e.g., `4953, 4957, 4951, 4952, 4958` → `security_result1`, ` 4908, ... )  
`SourceName` | `security_result` | Mapped values (11 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`category_details` | `security_result` | Mapped values (9 total, e.g., ` "Security State Change", "Security System Extension", "System... )  
`label_security_result` | `security_result` | Merged  
`security_result1` | `security_result` | Merged  
`security_result2` | `security_result` | Merged  
`security_result_1` | `security_result` | Merged  
`security_result_2` | `security_result` | Merged  
`security_result_3` | `security_result` | Merged  
`security_result_4` | `security_result` | Merged  
`security_result_5` | `security_result` | Merged  
`KeyUserPath` | `security_result.about.file.full_path` | Directly mapped  
`EventID` | `security_result.about.labels` | Mapped: `4625, 4776, 4794` → `failure_reason_label`, `4908, 4964` → `label_for_security...  
`SourceName` | `security_result.about.labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `f...  
`failure_reason_label` | `security_result.about.labels` | Merged  
`label_for_security_result_about_label` | `security_result.about.labels` | Merged  
`EventID` | `security_result.about.resource.attribute.labels` | Mapped values (14 total, e.g., `4908, 4964` → `label`, `4908, 4964` → `label1`, ` 4908,... )  
`SourceName` | `security_result.about.resource.attribute.labels` | Mapped values (29 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`TicketOptions_label` | `security_result.about.resource.attribute.labels` | Merged  
`label` | `security_result.about.resource.attribute.labels` | Merged  
`label1` | `security_result.about.resource.attribute.labels` | Merged  
`label10` | `security_result.about.resource.attribute.labels` | Merged  
`label11` | `security_result.about.resource.attribute.labels` | Merged  
`label12` | `security_result.about.resource.attribute.labels` | Merged  
`label13` | `security_result.about.resource.attribute.labels` | Merged  
`label2` | `security_result.about.resource.attribute.labels` | Merged  
`label3` | `security_result.about.resource.attribute.labels` | Merged  
`label4` | `security_result.about.resource.attribute.labels` | Merged  
`label5` | `security_result.about.resource.attribute.labels` | Merged  
`label6` | `security_result.about.resource.attribute.labels` | Merged  
`label7` | `security_result.about.resource.attribute.labels` | Merged  
`label8` | `security_result.about.resource.attribute.labels` | Merged  
`label9` | `security_result.about.resource.attribute.labels` | Merged  
`security_result_about_resource_name` | `security_result.about.resource.name` | Renamed/mapped  
`EventID` | `security_result.action` | Mapped: `4908, 4964` → `action`  
`SourceName` | `security_result.action` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `a...  
`action` | `security_result.action` | Merged  
`security_action` | `security_result.action` | Merged  
`Action Name` | `security_result.action_details` | Directly mapped  
`action_details` | `security_result.action_details` | Renamed/mapped  
`action_id` | `security_result.action_details` | Directly mapped  
`EventID` | `security_result.category` | Mapped: `4908, 4964` → `category`  
`SourceName` | `security_result.category` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `c...  
`category` | `security_result.category` | Merged  
`Category` | `security_result.category_details` | Merged  
`CategoryId` | `security_result.category_details` | Merged  
`CategoryName` | `security_result.category_details` | Merged  
`EventID` | `security_result.category_details` | Mapped: `4908, 4964` → `Category`, `4908, 4964` → `CategoryName`, ` 102, 103, 300, 301...  
`SourceName` | `security_result.category_details` | Mapped values (9 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`AccessReason` | `security_result.description` | Directly mapped  
`AdditionalInfo` | `security_result.description` | Renamed/mapped  
`AuditPolicyChanges` | `security_result.description` | Directly mapped  
`Data_2` | `security_result.description` | Directly mapped  
`Error Description` | `security_result.description` | Directly mapped  
`ErrorContext` | `security_result.description` | Directly mapped  
`ErrorMessage` | `security_result.description` | Directly mapped  
`Message` | `security_result.description` | Directly mapped  
`ReasonForRejection` | `security_result.description` | Renamed/mapped  
`RootCause` | `security_result.description` | Directly mapped  
`description` | `security_result.description` | Renamed/mapped  
`security_description` | `security_result.description` | Directly mapped  
`status` | `security_result.description` | Directly mapped  
`AdditionalInfo2_label` | `security_result.detection_fields` | Merged  
`AppendData_or_AddSubdirectory_or_CreatePipeInstance_label` | `security_result.detection_fields` | Merged  
`ApplicationDomain_label` | `security_result.detection_fields` | Merged  
`ApplicationPath_label` | `security_result.detection_fields` | Merged  
`ApplicationVirtualPath_label` | `security_result.detection_fields` | Merged  
`AuthenticationType_label` | `security_result.detection_fields` | Merged  
`CONTROL_label` | `security_result.detection_fields` | Merged  
`CustomEventDetails_label` | `security_result.detection_fields` | Merged  
`DAC_label` | `security_result.detection_fields` | Merged  
`DELETE_label` | `security_result.detection_fields` | Merged  
`ErrorCode_label` | `security_result.detection_fields` | Merged  
`EventCode_label` | `security_result.detection_fields` | Merged  
`EventDetailCode_label` | `security_result.detection_fields` | Merged  
`EventID` | `security_result.detection_fields` | Mapped values (150 total, e.g., `5158,5159,5154,5153,5155` → `labels0`, ` 5158,5159,5154,51... )  
`EventId_label` | `security_result.detection_fields` | Merged  
`EventOccurrence_label` | `security_result.detection_fields` | Merged  
`EventSequence_label` | `security_result.detection_fields` | Merged  
`FailureId_label` | `security_result.detection_fields` | Merged  
`GPOList_label` | `security_result.detection_fields` | Merged  
`IsAuthenticated_label` | `security_result.detection_fields` | Merged  
`IsImpersonating_label` | `security_result.detection_fields` | Merged  
`MasterKeyId_label` | `security_result.detection_fields` | Merged  
`ReadAttributes_label` | `security_result.detection_fields` | Merged  
`RecoveryKeyId_label` | `security_result.detection_fields` | Merged  
`RequestPath_label` | `security_result.detection_fields` | Merged  
`SecurityDescriptor_label` | `security_result.detection_fields` | Merged  
`Sid_Filtering_label` | `security_result.detection_fields` | Merged  
`SourceName` | `security_result.detection_fields` | Mapped values (357 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows se... )  
`StackTrace_label` | `security_result.detection_fields` | Merged  
`ThreadAccountName_label` | `security_result.detection_fields` | Merged  
`ThreadId_label` | `security_result.detection_fields` | Merged  
`TrustLevel_label` | `security_result.detection_fields` | Merged  
`Trust_Attributes_label` | `security_result.detection_fields` | Merged  
`Trust_Direction_label` | `security_result.detection_fields` | Merged  
`Trust_Type_label` | `security_result.detection_fields` | Merged  
`WriteAttributes_label` | `security_result.detection_fields` | Merged  
`WriteData_or_AddFile_label` | `security_result.detection_fields` | Merged  
`WriteEA_label` | `security_result.detection_fields` | Merged  
`account_name_label` | `security_result.detection_fields` | Merged  
`action_id_label` | `security_result.detection_fields` | Merged  
`affected_rows_label` | `security_result.detection_fields` | Merged  
`analysis_symbol_label` | `security_result.detection_fields` | Merged  
`application_information_label` | `security_result.detection_fields` | Merged  
`application_name_label` | `security_result.detection_fields` | Merged  
`audit_event_label` | `security_result.detection_fields` | Merged  
`audit_schema_version_label` | `security_result.detection_fields` | Merged  
`cert_issuer_name_label` | `security_result.detection_fields` | Merged  
`cert_serial_number_label` | `security_result.detection_fields` | Merged  
`cert_thumbprint_label` | `security_result.detection_fields` | Merged  
`class_type_label` | `security_result.detection_fields` | Merged  
`client_ip_label` | `security_result.detection_fields` | Merged  
`client_name_label` | `security_result.detection_fields` | Merged  
`client_name_session_id_label` | `security_result.detection_fields` | Merged  
`client_tls_version_label` | `security_result.detection_fields` | Merged  
`client_tls_version_name_label` | `security_result.detection_fields` | Merged  
`connection_id_label` | `security_result.detection_fields` | Merged  
`database_name_label` | `security_result.detection_fields` | Merged  
`database_principal_id_label` | `security_result.detection_fields` | Merged  
`database_principal_name_label` | `security_result.detection_fields` | Merged  
`database_transaction_id_label` | `security_result.detection_fields` | Merged  
`detect_field` | `security_result.detection_fields` | Merged  
`detection_fields` | `security_result.detection_fields` | Merged  
`detection_label` | `security_result.detection_fields` | Merged  
`device_guid_label` | `security_result.detection_fields` | Merged  
`duration_milliseconds_label` | `security_result.detection_fields` | Merged  
`error_label` | `security_result.detection_fields` | Merged  
`event_detail_code_label` | `security_result.detection_fields` | Merged  
`event_id_label` | `security_result.detection_fields` | Merged  
`event_message_label` | `security_result.detection_fields` | Merged  
`event_name_label` | `security_result.detection_fields` | Merged  
`event_occurrence_label` | `security_result.detection_fields` | Merged  
`event_sequence_label` | `security_result.detection_fields` | Merged  
`event_time_label` | `security_result.detection_fields` | Merged  
`event_time_utc_label` | `security_result.detection_fields` | Merged  
`exce_label` | `security_result.detection_fields` | Merged  
`exception_information_label` | `security_result.detection_fields` | Merged  
`external_policy_permissions_checked_label` | `security_result.detection_fields` | Merged  
`failure_status_label` | `security_result.detection_fields` | Merged  
`host_name_label` | `security_result.detection_fields` | Merged  
`is_column_permission_label` | `security_result.detection_fields` | Merged  
`is_impersonating_label` | `security_result.detection_fields` | Merged  
`is_local_secondary_replica_label` | `security_result.detection_fields` | Merged  
`label` | `security_result.detection_fields` | Merged  
`label_for_security_result_detection` | `security_result.detection_fields` | Merged  
`labels0` | `security_result.detection_fields` | Merged  
`labels1` | `security_result.detection_fields` | Merged  
`labels2` | `security_result.detection_fields` | Merged  
`labels3` | `security_result.detection_fields` | Merged  
`ledger_start_sequence_number_label` | `security_result.detection_fields` | Merged  
`machine_name_label` | `security_result.detection_fields` | Merged  
`nas_port_field` | `security_result.detection_fields` | Merged  
`network_protocol_label` | `security_result.detection_fields` | Merged  
`object_id_label` | `security_result.detection_fields` | Merged  
`object_name_label` | `security_result.detection_fields` | Merged  
`obo_middle_tier_app_id_label` | `security_result.detection_fields` | Merged  
`permission_bitmask_label` | `security_result.detection_fields` | Merged  
`proxy_policy_name` | `security_result.detection_fields` | Merged  
`req_url_label` | `security_result.detection_fields` | Merged  
`response_rows_label` | `security_result.detection_fields` | Merged  
`response_ticket_label` | `security_result.detection_fields` | Merged  
`schema_name_label` | `security_result.detection_fields` | Merged  
`sec_error_label` | `security_result.detection_fields` | Merged  
`security_detection1` | `security_result.detection_fields` | Merged  
`security_detection2` | `security_result.detection_fields` | Merged  
`security_detection3` | `security_result.detection_fields` | Merged  
`security_detection4` | `security_result.detection_fields` | Merged  
`sequence_group_id_label` | `security_result.detection_fields` | Merged  
`sequence_number_label` | `security_result.detection_fields` | Merged  
`server_instance_name_label` | `security_result.detection_fields` | Merged  
`server_principal_id_label` | `security_result.detection_fields` | Merged  
`server_principal_name_label` | `security_result.detection_fields` | Merged  
`server_principal_sid_label` | `security_result.detection_fields` | Merged  
`session_id_label` | `security_result.detection_fields` | Merged  
`session_server_principal_name_label` | `security_result.detection_fields` | Merged  
`statement_label` | `security_result.detection_fields` | Merged  
`succeeded_label` | `security_result.detection_fields` | Merged  
`target_database_principal_id_label` | `security_result.detection_fields` | Merged  
`target_database_principal_name_label` | `security_result.detection_fields` | Merged  
`target_server_principal_id_label` | `security_result.detection_fields` | Merged  
`target_server_principal_name_label` | `security_result.detection_fields` | Merged  
`target_server_principal_sid_label` | `security_result.detection_fields` | Merged  
`transaction_id_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`user_defined_event_id_label` | `security_result.detection_fields` | Merged  
`user_defined_information_label` | `security_result.detection_fields` | Merged  
`var_Action_ID` | `security_result.detection_fields` | Merged  
`var_Additional_Actions_ID` | `security_result.detection_fields` | Merged  
`var_Additional_Actions_String` | `security_result.detection_fields` | Merged  
`var_Category_ID` | `security_result.detection_fields` | Merged  
`var_DetectionOrigin` | `security_result.detection_fields` | Merged  
`var_DetectionSource` | `security_result.detection_fields` | Merged  
`var_DetectionType` | `security_result.detection_fields` | Merged  
`var_Detection_ID` | `security_result.detection_fields` | Merged  
`var_EngineVersion` | `security_result.detection_fields` | Merged  
`var_Error_Code` | `security_result.detection_fields` | Merged  
`var_Execution_ID` | `security_result.detection_fields` | Merged  
`var_Execution_Name` | `security_result.detection_fields` | Merged  
`var_Origin_ID` | `security_result.detection_fields` | Merged  
`var_Post_Clean_Status` | `security_result.detection_fields` | Merged  
`var_Pre_Execution_Status` | `security_result.detection_fields` | Merged  
`var_SecurityintelligenceVersion` | `security_result.detection_fields` | Merged  
`var_SeverityName` | `security_result.detection_fields` | Merged  
`var_Severity_ID` | `security_result.detection_fields` | Merged  
`var_Source_ID` | `security_result.detection_fields` | Merged  
`var_State` | `security_result.detection_fields` | Merged  
`var_Status_Code` | `security_result.detection_fields` | Merged  
`var_Type_ID` | `security_result.detection_fields` | Merged  
`var_process_information` | `security_result.detection_fields` | Merged  
`var_process_name` | `security_result.detection_fields` | Merged  
`var_request_information` | `security_result.detection_fields` | Merged  
`var_stack_trace` | `security_result.detection_fields` | Merged  
`var_thread_account_name` | `security_result.detection_fields` | Merged  
`Priority` | `security_result.priority_details` | Renamed/mapped  
`RuleId` | `security_result.rule_id` | Renamed/mapped  
`EventID` | `security_result.rule_labels` | Mapped: `4908, 4964` → `Title_label`, `4908, 4964` → `label_for_security_result_rule_l...  
`SourceName` | `security_result.rule_labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `T...  
`Title_label` | `security_result.rule_labels` | Merged  
`label_for_security_result_rule_label` | `security_result.rule_labels` | Merged  
`EventID` | `security_result.rule_name` | Directly mapped  
`connection_req_policy` | `security_result.rule_name` | Directly mapped  
`Severity` | `security_result.severity` | Renamed/mapped  
`BlockReasonErrorCode` | `security_result.summary` | Directly mapped  
`CorruptionActionState` | `security_result.summary` | Directly mapped  
`CrashOnAuditFailValue` | `security_result.summary` | Directly mapped  
`Error` | `security_result.summary` | Directly mapped  
`ErrorCode` | `security_result.summary` | Directly mapped  
`FailureReason` | `security_result.summary` | Directly mapped  
`FinalStatus` | `security_result.summary` | Directly mapped  
`QueryResults` | `security_result.summary` | Directly mapped  
`Reason` | `security_result.summary` | Directly mapped  
`Status` | `security_result.summary` | Directly mapped  
`Win32Error` | `security_result.summary` | Directly mapped  
`error` | `security_result.summary` | Directly mapped  
`hr` | `security_result.summary` | Directly mapped  
`param1` | `security_result.summary` | Directly mapped  
`sec_summary` | `security_result.summary` | Directly mapped  
`security_summary` | `security_result.summary` | Directly mapped  
`status` | `security_result.summary` | Directly mapped  
`summary` | `security_result.summary` | Renamed/mapped  
`ThreatID` | `security_result.threat_id` | Directly mapped  
`ThreatName` | `security_result.threat_name` | Directly mapped  
`src_path` | `src.file.full_path` | Renamed/mapped  
`CallerComputerName` | `src.hostname` | Directly mapped  
`EventID` | `src.ip` | Mapped: `4908, 4964` → `varclientip`, ` 1162, 1311, 1535, 1566, 1644, 1865, 1925, 2085, 2...  
`SourceName` | `src.ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `v...  
`varclientip` | `src.ip` | Merged  
`varclientport` | `src.port` | Renamed/mapped  
`Service` | `src.resource.name` | Renamed/mapped  
`SourceDRA` | `src.resource.name` | Directly mapped  
`SourceHandleId` | `src.resource.name` | Renamed/mapped  
`EventID` | `target` | Mapped: `4908, 4964` → `clsid_labels`, `10001, 10002, 10100` → `clsid_labels`  
`SourceName` | `target` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `c...  
`clsid_labels` | `target` | Merged  
`DomainName` | `target.administrative_domain` | Renamed/mapped  
`ServerRealm` | `target.administrative_domain` | Directly mapped  
`TargetDomainName` | `target.administrative_domain` | Renamed/mapped  
`subject_domain_name` | `target.administrative_domain` | Renamed/mapped  
`target_domain_name` | `target.administrative_domain` | Renamed/mapped  
`ServiceName` | `target.application` | Directly mapped  
`Targetname` | `target.application` | Directly mapped  
`event_source` | `target.application` | Directly mapped  
`target_application` | `target.application` | Renamed/mapped  
`UserData.InstallDeviceID.DeviceInstanceID` | `target.asset.asset_id` | Directly mapped  
`EventID` | `target.asset.attribute.labels` | Mapped values (10 total, e.g., `4741, 4742` → `dns_host_label`, `4908, 4964` → `user_dat... )  
`SourceName` | `target.asset.attribute.labels` | Mapped values (14 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`dns_host_label` | `target.asset.attribute.labels` | Merged  
`label_for_target_asset` | `target.asset.attribute.labels` | Merged  
`target_server_principal_id_label` | `target.asset.attribute.labels` | Merged  
`target_server_principal_name_label` | `target.asset.attribute.labels` | Merged  
`target_server_principal_sid_label` | `target.asset.attribute.labels` | Merged  
`token_new` | `target.asset.attribute.labels` | Merged  
`user_data_install_device_id_is_driver_oem_label` | `target.asset.attribute.labels` | Merged  
`user_data_install_device_id_reboot_option_label` | `target.asset.attribute.labels` | Merged  
`user_data_install_device_id_setup_class_label` | `target.asset.attribute.labels` | Merged  
`user_data_install_device_id_upgrade_device_label` | `target.asset.attribute.labels` | Merged  
`AccountName` | `target.asset.hostname` | Directly mapped  
`NodeName` | `target.asset.hostname` | Directly mapped  
`client_name` | `target.asset.hostname` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`ClientIPAddress` | `target.asset.ip` | Merged  
`NASIPAddress` | `target.asset.ip` | Merged  
`SourceName` | `target.asset.ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `N...  
`called_station_id` | `target.asset.ip` | Merged  
`client_ip` | `target.asset.ip` | Merged  
`nas_ip` | `target.asset.ip` | Merged  
`UserData.InstallDeviceID.DeviceInstanceID` | `target.asset_id` | Directly mapped  
`Data_1` | `target.domain.name` | Directly mapped  
`TargetName` | `target.domain.name` | Directly mapped  
`TargetRealm` | `target.domain.name` | Directly mapped  
`param2` | `target.domain.name` | Directly mapped  
`AutoBackup.BackupPath` | `target.file.full_path` | Renamed/mapped  
`BackupFileName` | `target.file.full_path` | Renamed/mapped  
`FileName` | `target.file.full_path` | Renamed/mapped  
`FilePath` | `target.file.full_path` | Renamed/mapped  
`KeyFilePath` | `target.file.full_path` | Renamed/mapped  
`KeyUserPath` | `target.file.full_path` | Renamed/mapped  
`Namespace` | `target.file.full_path` | Renamed/mapped  
`PublishURLs` | `target.file.full_path` | Renamed/mapped  
`ServiceFileName` | `target.file.full_path` | Renamed/mapped  
`ShareLocalPath` | `target.file.full_path` | Renamed/mapped  
`target_file_name` | `target.file.full_path` | Renamed/mapped  
`MD5` | `target.file.md5` | Renamed/mapped  
`EventID` | `target.file.names` | Mapped: ` 5049, 5140 , 5145, 5142, 5143, 5144, 4698, 4702, 4699, 4700, 4701, 4946, 4690, 4...  
`RelativeTargetName` | `target.file.names` | Merged  
`ScriptName` | `target.file.names` | Merged  
`SourceName` | `target.file.names` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `R...  
`SHA1` | `target.file.sha1` | Renamed/mapped  
`SHA256` | `target.file.sha256` | Renamed/mapped  
`NewSize` | `target.file.size` | Renamed/mapped  
`target_file_size` | `target.file.size` | Renamed/mapped  
`EventID` | `target.group.attribute.labels` | Mapped: `4908, 4964` → `label_for_target_group`  
`SourceName` | `target.group.attribute.labels` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `l...  
`label_for_target_group` | `target.group.attribute.labels` | Merged  
`EventID` | `target.group.attribute.permissions` | Mapped: ` 4656, 4704, 4672, 4731, 4720, 4723, 4726, 4728, 4729, 4730, 4732, 4733, 4734, 47...  
`SourceName` | `target.group.attribute.permissions` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `p...  
`privilege_list` | `target.group.attribute.permissions` | Merged  
`target_group_display_name` | `target.group.group_display_name` | Renamed/mapped  
`target_group_product_object_id` | `target.group.product_object_id` | Renamed/mapped  
`target_group_windows_sid` | `target.group.windows_sid` | Renamed/mapped  
`AccountName` | `target.hostname` | Directly mapped  
`client_name` | `target.hostname` | Directly mapped  
`target_asset_hostname` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Renamed/mapped  
`ClientIPAddress` | `target.ip` | Merged  
`EventID` | `target.ip` | Mapped: `4908, 4964` → `target_ip`  
`NASIPAddress` | `target.ip` | Merged  
`SourceName` | `target.ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `v...  
`called_station_id` | `target.ip` | Merged  
`client_ip` | `target.ip` | Merged  
`nas_ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`var_valid_ip` | `target.ip` | Merged  
`ActiveProfile_label` | `target.labels` | Merged  
`AppId_label` | `target.labels` | Merged  
`CommandName_label` | `target.labels` | Merged  
`ConfiguredNames_label` | `target.labels` | Merged  
`DN_label` | `target.labels` | Merged  
`DSType_label` | `target.labels` | Merged  
`DirectiveName_label` | `target.labels` | Merged  
`EngineVersion_label` | `target.labels` | Merged  
`EventID` | `target.labels` | Mapped values (35 total, e.g., `4907 , 4817, 4715` → `ObjectServer_label`, ` 4907 , 4817, 4... )  
`FQDN_label` | `target.labels` | Merged  
`HandleId_label` | `target.labels` | Merged  
`HostId_label` | `target.labels` | Merged  
`HostVersion_label` | `target.labels` | Merged  
`KeyLength_label` | `target.labels` | Merged  
`LmPackageName_label` | `target.labels` | Merged  
`MandatoryLabel_label` | `target.labels` | Merged  
`NewState_label` | `target.labels` | Merged  
`NotificationInterval_label` | `target.labels` | Merged  
`ObjectServer_label` | `target.labels` | Merged  
`Operation_label` | `target.labels` | Merged  
`PipelineId_label` | `target.labels` | Merged  
`Profiles_label` | `target.labels` | Merged  
`ResourceManager_label` | `target.labels` | Merged  
`ReturnCode_label` | `target.labels` | Merged  
`RunspaceId_label` | `target.labels` | Merged  
`ServiceStartType_label` | `target.labels` | Merged  
`ServiceType_label` | `target.labels` | Merged  
`SkuId_label` | `target.labels` | Merged  
`SourceName` | `target.labels` | Mapped values (77 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows sec... )  
`TargetLinkedLogonId_label` | `target.labels` | Merged  
`TokenElevationType_label` | `target.labels` | Merged  
`TransactionId_label` | `target.labels` | Merged  
`TransmittedServices_label` | `target.labels` | Merged  
`Trigger_label` | `target.labels` | Merged  
`VirtualAccount_label` | `target.labels` | Merged  
`client_friendly_name_label` | `target.labels` | Merged  
`event_in_seq_label` | `target.labels` | Merged  
`label02` | `target.labels` | Merged  
`label462` | `target.labels` | Merged  
`label463` | `target.labels` | Merged  
`label46561` | `target.labels` | Merged  
`label46562` | `target.labels` | Merged  
`label46563` | `target.labels` | Merged  
`label46564` | `target.labels` | Merged  
`label46565` | `target.labels` | Merged  
`label46571` | `target.labels` | Merged  
`label46572` | `target.labels` | Merged  
`label47681` | `target.labels` | Merged  
`label47682` | `target.labels` | Merged  
`label501` | `target.labels` | Merged  
`label601` | `target.labels` | Merged  
`labels46411` | `target.labels` | Merged  
`labels46412` | `target.labels` | Merged  
`labels46413` | `target.labels` | Merged  
`labels46414` | `target.labels` | Merged  
`labels46415` | `target.labels` | Merged  
`labels46416` | `target.labels` | Merged  
`labels46417` | `target.labels` | Merged  
`nas_port_type` | `target.labels` | Merged  
`new_target_user_name_label` | `target.labels` | Merged  
`object_class_label` | `target.labels` | Merged  
`object_dn_label` | `target.labels` | Merged  
`target_label` | `target.labels` | Merged  
`target_labels` | `target.labels` | Merged  
`target_logon_id_label` | `target.labels` | Merged  
`target_user_id_label` | `target.labels` | Merged  
`EventID` | `target.mac` | Mapped: `4908, 4964` → `target_mac`  
`NASIdentifier` | `target.mac` | Mapped: `(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$` → `NASIdentifier`  
`SourceName` | `target.mac` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `t...  
`mac_address` | `target.mac` | Merged  
`target_mac` | `target.mac` | Merged  
`PeerPrivateAddress` | `target.nat_ip` | Merged  
`SourceName` | `target.nat_ip` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `P...  
`NASPort` | `target.nat_port` | Renamed/mapped  
`var_http_method` | `target.network.http.method` | Directly mapped  
`target_platform_version` | `target.platform_version` | Renamed/mapped  
`nas_port` | `target.port` | Renamed/mapped  
`targetport` | `target.port` | Renamed/mapped  
`CommandLine` | `target.process.command_line` | Renamed/mapped  
`target_process_command_line` | `target.process.command_line` | Renamed/mapped  
`ImagePath` | `target.process.file.full_path` | Renamed/mapped  
`NewProcessName` | `target.process.file.full_path` | Renamed/mapped  
`TargetProcessName` | `target.process.file.full_path` | Renamed/mapped  
`target_process_file_full_path` | `target.process.file.full_path` | Renamed/mapped  
`MD5` | `target.process.file.md5` | Directly mapped  
`SourceName` | `target.process.file.names` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `v...  
`var_process_file_name` | `target.process.file.names` | Merged  
`SHA1` | `target.process.file.sha1` | Directly mapped  
`SHA256` | `target.process.file.sha256` | Directly mapped  
`target_parent_process_command_line` | `target.process.parent_process.command_line` | Renamed/mapped  
`target_parent_process_file_full_path` | `target.process.parent_process.file.full_path` | Renamed/mapped  
`target_parent_process_pid` | `target.process.parent_process.pid` | Renamed/mapped  
`TargetProcessId` | `target.process.pid` | Renamed/mapped  
`target_process_pid` | `target.process.pid` | Renamed/mapped  
`EventOriginId` | `target.process.product_specific_process_id` | Directly mapped  
`ObjectName` | `target.registry.registry_key` | Directly mapped  
`ObjectVirtualPath` | `target.registry.registry_key` | Renamed/mapped  
`target_registry_key` | `target.registry.registry_key` | Renamed/mapped  
`NewValue` | `target.registry.registry_value_data` | Renamed/mapped  
`target_registry_registry_value_data` | `target.registry.registry_value_data` | Renamed/mapped  
`ObjectValueName` | `target.registry.registry_value_name` | Renamed/mapped  
`registry_value` | `target.registry.registry_value_name` | Renamed/mapped  
`target_registry_registry_value_name` | `target.registry.registry_value_name` | Renamed/mapped  
`AlgorithmName_label` | `target.resource.attribute.labels` | Merged  
`ClassId_label` | `target.resource.attribute.labels` | Merged  
`ClassName_label` | `target.resource.attribute.labels` | Merged  
`CompatibleIds_label` | `target.resource.attribute.labels` | Merged  
`DomainBehaviorVersion_label` | `target.resource.attribute.labels` | Merged  
`ErrorCode_label` | `target.resource.attribute.labels` | Merged  
`EventID` | `target.resource.attribute.labels` | Mapped values (101 total, e.g., `4907 , 4817, 4715` → `label0`, `4907 , 4817, 4715` → `la... )  
`ForceLogoff_label` | `target.resource.attribute.labels` | Merged  
`HandleID_label` | `target.resource.attribute.labels` | Merged  
`HardwareIds_label` | `target.resource.attribute.labels` | Merged  
`KeyType_label` | `target.resource.attribute.labels` | Merged  
`LocationInformation_label` | `target.resource.attribute.labels` | Merged  
`LockoutDuration_label` | `target.resource.attribute.labels` | Merged  
`LockoutObservationWindow_label` | `target.resource.attribute.labels` | Merged  
`LockoutThreshold_label` | `target.resource.attribute.labels` | Merged  
`MachineAccountQuota_label` | `target.resource.attribute.labels` | Merged  
`MaxPasswordAge_label` | `target.resource.attribute.labels` | Merged  
`MinPasswordAge_label` | `target.resource.attribute.labels` | Merged  
`MinPasswordLength_label` | `target.resource.attribute.labels` | Merged  
`MixedDomainMode_label` | `target.resource.attribute.labels` | Merged  
`ModifiedObjectProperties_label` | `target.resource.attribute.labels` | Merged  
`ObjectIdentifyingProperties_label` | `target.resource.attribute.labels` | Merged  
`ObjectProperties_label` | `target.resource.attribute.labels` | Merged  
`ObjectServer_label` | `target.resource.attribute.labels` | Merged  
`OemInformation_label` | `target.resource.attribute.labels` | Merged  
`PasswordHistoryLength_label` | `target.resource.attribute.labels` | Merged  
`PasswordProperties_label` | `target.resource.attribute.labels` | Merged  
`ProfileChanged_label` | `target.resource.attribute.labels` | Merged  
`ProfileUsed_label` | `target.resource.attribute.labels` | Merged  
`ProviderName_label` | `target.resource.attribute.labels` | Merged  
`PuaCount_label` | `target.resource.attribute.labels` | Merged  
`ResourceAttributes_label` | `target.resource.attribute.labels` | Merged  
`SettingValue_label` | `target.resource.attribute.labels` | Merged  
`SourceName` | `target.resource.attribute.labels` | Mapped values (120 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows se... )  
`TemplateContent_label` | `target.resource.attribute.labels` | Merged  
`TemplateDSObjectFQDN_label` | `target.resource.attribute.labels` | Merged  
`TemplateSchemaVersion_label` | `target.resource.attribute.labels` | Merged  
`TemplateVersion_label` | `target.resource.attribute.labels` | Merged  
`TransactionId_label` | `target.resource.attribute.labels` | Merged  
`database_principal_id_label` | `target.resource.attribute.labels` | Merged  
`database_principal_name_label` | `target.resource.attribute.labels` | Merged  
`entry_type_label` | `target.resource.attribute.labels` | Merged  
`label0` | `target.resource.attribute.labels` | Merged  
`label00` | `target.resource.attribute.labels` | Merged  
`label01` | `target.resource.attribute.labels` | Merged  
`label02` | `target.resource.attribute.labels` | Merged  
`label03` | `target.resource.attribute.labels` | Merged  
`label04` | `target.resource.attribute.labels` | Merged  
`label05` | `target.resource.attribute.labels` | Merged  
`label06` | `target.resource.attribute.labels` | Merged  
`label07` | `target.resource.attribute.labels` | Merged  
`label08` | `target.resource.attribute.labels` | Merged  
`label09` | `target.resource.attribute.labels` | Merged  
`label1` | `target.resource.attribute.labels` | Merged  
`label2` | `target.resource.attribute.labels` | Merged  
`label3` | `target.resource.attribute.labels` | Merged  
`label4` | `target.resource.attribute.labels` | Merged  
`label4681` | `target.resource.attribute.labels` | Merged  
`label4682` | `target.resource.attribute.labels` | Merged  
`label4683` | `target.resource.attribute.labels` | Merged  
`label4684` | `target.resource.attribute.labels` | Merged  
`label5` | `target.resource.attribute.labels` | Merged  
`label6` | `target.resource.attribute.labels` | Merged  
`label_SessionStateChangeTrigger_Enabled` | `target.resource.attribute.labels` | Merged  
`label_SessionStateChangeTrigger_StateChange` | `target.resource.attribute.labels` | Merged  
`label_for_target_resource` | `target.resource.attribute.labels` | Merged  
`labels0` | `target.resource.attribute.labels` | Merged  
`labels1` | `target.resource.attribute.labels` | Merged  
`labels10` | `target.resource.attribute.labels` | Merged  
`labels11` | `target.resource.attribute.labels` | Merged  
`labels12` | `target.resource.attribute.labels` | Merged  
`labels13` | `target.resource.attribute.labels` | Merged  
`labels14` | `target.resource.attribute.labels` | Merged  
`labels15` | `target.resource.attribute.labels` | Merged  
`labels16` | `target.resource.attribute.labels` | Merged  
`labels17` | `target.resource.attribute.labels` | Merged  
`labels19` | `target.resource.attribute.labels` | Merged  
`labels2` | `target.resource.attribute.labels` | Merged  
`labels21` | `target.resource.attribute.labels` | Merged  
`labels26` | `target.resource.attribute.labels` | Merged  
`labels3` | `target.resource.attribute.labels` | Merged  
`labels35` | `target.resource.attribute.labels` | Merged  
`labels4` | `target.resource.attribute.labels` | Merged  
`labels41` | `target.resource.attribute.labels` | Merged  
`labels5` | `target.resource.attribute.labels` | Merged  
`labels6` | `target.resource.attribute.labels` | Merged  
`labels7` | `target.resource.attribute.labels` | Merged  
`labels8` | `target.resource.attribute.labels` | Merged  
`labels9` | `target.resource.attribute.labels` | Merged  
`nas_port_label` | `target.resource.attribute.labels` | Merged  
`netbios_name_label` | `target.resource.attribute.labels` | Merged  
`object_id_label` | `target.resource.attribute.labels` | Merged  
`object_name_label` | `target.resource.attribute.labels` | Merged  
`operation_id_label` | `target.resource.attribute.labels` | Merged  
`schema_name_label` | `target.resource.attribute.labels` | Merged  
`target_database_principal_id_label` | `target.resource.attribute.labels` | Merged  
`target_database_principal_name_label` | `target.resource.attribute.labels` | Merged  
`top_level_name_label` | `target.resource.attribute.labels` | Merged  
`uac_label` | `target.resource.attribute.labels` | Merged  
`user_data_install_device_id_@_xmlns__label` | `target.resource.attribute.labels` | Merged  
`user_data_install_device_id_driver_description_label` | `target.resource.attribute.labels` | Merged  
`user_data_install_device_id_driver_provider_label` | `target.resource.attribute.labels` | Merged  
`user_data_install_device_id_driver_version_label` | `target.resource.attribute.labels` | Merged  
`user_data_install_device_id_install_status_label` | `target.resource.attribute.labels` | Merged  
`volume_label` | `target.resource.attribute.labels` | Merged  
`EventID` | `target.resource.attribute.permissions` | Mapped: `4663, 4656, 4659` → `permissions`, `4908, 4964` → `permissions`  
`SourceName` | `target.resource.attribute.permissions` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `p...  
`permissions` | `target.resource.attribute.permissions` | Merged  
`DeviceId` | `target.resource.id` | Renamed/mapped  
`ContextName` | `target.resource.name` | Directly mapped  
`DestinationDRA` | `target.resource.name` | Directly mapped  
`DfsNamespace` | `target.resource.name` | Renamed/mapped  
`DomainPolicyChanged` | `target.resource.name` | Renamed/mapped  
`ExtensionName` | `target.resource.name` | Renamed/mapped  
`HiveName` | `target.resource.name` | Renamed/mapped  
`SecurityPackageName` | `target.resource.name` | Renamed/mapped  
`TicketOptions` | `target.resource.name` | Directly mapped  
`attribute_value` | `target.resource.name` | Renamed/mapped  
`target_resource_name` | `target.resource.name` | Renamed/mapped  
`updateTitle` | `target.resource.name` | Renamed/mapped  
`ObjectServer` | `target.resource.parent` | Renamed/mapped  
`AppInstance` | `target.resource.product_object_id` | Renamed/mapped  
`AuthenticationSetId` | `target.resource.product_object_id` | Renamed/mapped  
`ConnectionSecurityRuleId` | `target.resource.product_object_id` | Renamed/mapped  
`CryptographicSetId` | `target.resource.product_object_id` | Renamed/mapped  
`DeviceId` | `target.resource.product_object_id` | Directly mapped  
`ExtensionId` | `target.resource.product_object_id` | Renamed/mapped  
`FilterId` | `target.resource.product_object_id` | Renamed/mapped  
`IpSecSecurityAssociationId` | `target.resource.product_object_id` | Renamed/mapped  
`ObjectGUID` | `target.resource.product_object_id` | Renamed/mapped  
`PuaPolicyId` | `target.resource.product_object_id` | Renamed/mapped  
`TargetJobId` | `target.resource.product_object_id` | Renamed/mapped  
`TemplateOID` | `target.resource.product_object_id` | Renamed/mapped  
`target_resource_product_object_id` | `target.resource.product_object_id` | Renamed/mapped  
`updateGuid` | `target.resource.product_object_id` | Renamed/mapped  
`val_instance_id` | `target.resource.product_object_id` | Directly mapped  
`KeyType` | `target.resource.resource_subtype` | Renamed/mapped  
`ObjectType` | `target.resource.resource_subtype` | Directly mapped  
`TicketEncryptionType` | `target.resource.resource_subtype` | Directly mapped  
`resource_subtype` | `target.resource.resource_subtype` | Renamed/mapped  
`EventID` | `target.resource.resource_type` | Mapped: `4908, 4964` → `SETTING`, `4908, 4964` → `TASK`  
`SourceName` | `target.resource.resource_type` | Mapped values (6 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`resource_type` | `target.resource.resource_type` | Renamed/mapped  
`EventID` | `target.resource.type` | Mapped: `4908, 4964` → `DATABASE`  
`SourceName` | `target.resource.type` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `D...  
`SourceName` | `target.resource_ancestors` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `r...  
`resource_ancestors` | `target.resource_ancestors` | Merged  
`SubscriptionManagerAddress` | `target.url` | Renamed/mapped  
`target_url` | `target.url` | Renamed/mapped  
`fileLength` | `target.url_metadata.last_http_response_content_length` | Renamed/mapped  
`EventID` | `target.user.attribute.labels` | Mapped: `4908, 4964` → `label_for_target_user`, `4908, 4964` → `user_label1`  
`MembershipExpirationTime_label` | `target.user.attribute.labels` | Merged  
`SourceName` | `target.user.attribute.labels` | Mapped values (7 total, e.g., `"Microsoft-Windows-Security-Auditing", "Microsoft Windows secu... )  
`TargetOutboundDomainName_label` | `target.user.attribute.labels` | Merged  
`label_for_target_user` | `target.user.attribute.labels` | Merged  
`target_group_membership_name_label` | `target.user.attribute.labels` | Merged  
`target_user_sid_name_label` | `target.user.attribute.labels` | Merged  
`user_att` | `target.user.attribute.labels` | Merged  
`user_label1` | `target.user.attribute.labels` | Merged  
`EventID` | `target.user.attribute.permissions` | Mapped: ` 4656, 4704, 4672, 4731, 4720, 4723, 4726, 4728, 4729, 4730, 4732, 4733, 4734, 47...  
`SourceName` | `target.user.attribute.permissions` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `a...  
`access_granted` | `target.user.attribute.permissions` | Merged  
`access_removed_list` | `target.user.attribute.permissions` | Merged  
`privilege_list` | `target.user.attribute.permissions` | Merged  
`EventID` | `target.user.group_identifiers` | Mapped: `4908, 4964` → `new_sid`  
`SourceName` | `target.user.group_identifiers` | Mapped: `"Microsoft-Windows-Security-Auditing", "Microsoft Windows security auditing."` → `i...  
`input_sid` | `target.user.group_identifiers` | Merged  
`new_sid` | `target.user.group_identifiers` | Merged  
`DisplayName` | `target.user.user_display_name` | Renamed/mapped  
`FullName` | `target.user.user_display_name` | Directly mapped  
`target_user_display_name` | `target.user.user_display_name` | Renamed/mapped  
`DetectionUser` | `target.user.userid` | Directly mapped  
`NewTargetUserName` | `target.user.userid` | Renamed/mapped  
`UserName` | `target.user.userid` | Directly mapped  
`subject_user_name` | `target.user.userid` | Renamed/mapped  
`target_user_id` | `target.user.userid` | Renamed/mapped  
`subject_user_sid` | `target.user.windows_sid` | Directly mapped  
`target_user_windows_sid` | `target.user.windows_sid` | Renamed/mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `Microsoft-Windows-Security-Auditing`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `target.resource.resource_type` | Constant: `BACKEND_SERVICE`  
N/A | `target.resource.type` | Constant: `DATABASE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-net-policy-server-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
