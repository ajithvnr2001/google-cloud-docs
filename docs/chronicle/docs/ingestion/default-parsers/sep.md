---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sep/
title: Collect Symantec Endpoint Protection logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:45:57.680845+00:00
---

# Collect Symantec Endpoint Protection logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sep/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec Endpoint Protection logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec Endpoint Protection (SEP) logs to Google Security Operations using the Bindplane agent.

Symantec Endpoint Protection is an endpoint security solution that generates syslog messages for malware detections, intrusion prevention events, firewall activity, application and device control events, and audit logs. The parser extracts fields from multiple log formats (syslog, CEF, Windows Event Log) using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec Endpoint Protection Manager (SEPM)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec Endpoint Protection Manager web UI



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
            chronicle/sep:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SEP
                raw_log_field: body
        
        service:
            pipelines:
                logs/sep_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/sep
        




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
             




## Configure syslog in Symantec Endpoint Protection

  1. Sign in to the **Symantec Endpoint Protection Manager** web UI.
  2. Click the **Admin** icon.
  3. Locate the **View Servers** section, and click **Servers**.
  4. Click **Local Site > Configure External Logging**.
  5. Select the **Enable Transmission of Logs to a Syslog Server** checkbox.
  6. Provide the following configuration details: 
     * **Syslog Server** : Enter the Bindplane IP address.
     * **UDP Destination Port** : Enter the Bindplane port number (for example, `514` for **UDP**).
     * **Log Facility** : Enter **Local6**.
     * Select the **Audit Logs** checkbox.
     * Select the **Security Logs** checkbox.
     * Select the **Risks** checkbox.
  7. Click **OK**.



## UDM mapping table

Log field | UDM mapping | Remark  
---|---|---  
`_DB_HOST` | `target.hostname` |   
`a_record` | `network.dns.questions.type` |   
`AccessCheckResults` | `security_result.detection_fields` |   
`Accesses` | `security_result.detection_fields` |   
`AccessList` | `security_result.detection_fields` |   
`AccessMask` | `security_result.detection_fields` |   
`AccessReason` | `security_result.description` |   
`AccountName` | `target.user.user_display_name` |   
`AccountType` | `principal.user.attribute.roles` |   
`ACTION` | `security_result.detection_fields` |   
`ACTION_TYPE` | `security_result.action_details` |   
`ActiveProfile` | `target.resource.name` |   
`ActivityID` | `additional.fields` |   
`AdditionalInfo2` | `security_result.detection_fields` |   
`ADMIN_NAME` | `principal.user.userid` |   
`AGENT_SECURITY_LOG_IDX` | `metadata.product_log_id` |   
`AgentVer` | `additional.fields` |   
`Alert` | `security_result.detection_fields` |   
`ALERT_IDX` | `security_result.rule_id` |   
`ALERTDATETIME` | `security_result.first_discovered_time` |   
`ALERTENDDATETIME` | `security_result.last_discovered_time` |   
`ALERTINSERTTIME` | `security_result.detection_fields` |   
`AlgorithmName` | `security_result.detection_fields` |   
`Allowedapplicationreason` | `security_result.detection_fields` |   
`APP_NAME` | `target.application` |   
`app_name` | `principal.application` |   
`AppPoolID` | `target.application` |   
`AuthenticationPackageName` | `additional.fields` |   
`AuthenticationSetId` | `security_result.detection_fields` |   
`AuthenticationSetName` | `target.resource.name` |   
`BitlockerUserInputTime` | `additional.fields` |   
`BootMenuPolicy` | `additional.fields` |   
`BootType` | `additional.fields` |   
`BU` | `additional.fields` |   
`BugcheckString` | `additional.fields` |   
`CALLER_PROCESS_ID` | `principal.process.pid` |   
`CALLER_PROCESS_NAME` | `principal.process.file.full_path` |   
`callerReturnAddress` | `additional.fields` |   
`callerReturnModuleName` | `additional.fields` |   
`Caption` | `target.application` |   
`Category` | `security_result.category_details` |   
`Channel` | `security_result.about.resource.attribute.labels` |   
`CIDS_SIGN_SUB_ID` | `additional.fields` |   
`CLIENT_USER2` | `principal.user.userid` |   
`Comment` | `metadata.description` |   
`Component` | `security_result.detection_fields` |   
`connection.ether_type` | `security_result.about.labels` |   
`ConnectionSecurityRuleName` | `target.resource.name` |   
`ConnectionSecurityRuleId` | `security_result.detection_fields` |   
`CryptographicSetId` | `security_result.detection_fields` |   
`CryptographicSetName` | `target.resource.name` |   
`CSPEID` | `additional.fields` |   
`DCName` | `intermediary.hostname` |   
`Desc` | `metadata.description` |   
`DesiredAccess` | `security_result.detection_fields` |   
`device.last_app_connection` | `target.asset.last_discover_time` |   
`device.wss_feature` | `target.asset.attribute.labels` |   
`DeviceName` | `target.resource.name` |   
`DeviceNameLength` | `additional.fields` |   
`DeviceTime` | `additional.fields` |   
`DeviceVersionMajor` | `additional.fields` |   
`DeviceVersionMinor` | `additional.fields` |   
`disposition` | `security_result.detection_fields` |   
`dns_direction` | `security_result.detection_fields` |   
`domain` | `target.administrative_domain` |   
`Domain` | `principal.administrative_domain` |   
`DOMAIN_ID` | `target.resource.product_object_id` |   
`EDate` | `additional.fields` |   
`EDateUTC` | `metadata.event_timestamp` |   
`elevated_token` | `additional.fields` |   
`EntryCount` | `additional.fields` |   
`Error` | `security_result.description` |   
`error` | `security_result.detection_fields` |   
`ErrorCode` | `security_result.description` |   
`ErrorDescription` | `security_result.description` |   
`Event` | `metadata.description` |   
`EVENT_DATA` | `additional.fields` |   
`event_type` | `metadata.product_event_type` |   
`EventData.Binary` | `additional.fields` |   
`eventDesc` | `metadata.description` |   
`eventInsertTime` | `metadata.collected_timestamp` |   
`EventReceivedTime` | `metadata.collected_timestamp` |   
`EventTime` | `metadata.event_timestamp` |   
`EventType` | `metadata.product_event_type` |   
`ExceptionCode` | `security_result.detection_fields` |   
`executionPolicy` | `security_result.rule_name` |   
`ExecutionProcessID` | `principal.process.pid` |   
`ExecutionThreadID` | `principal.process.product_specific_process_id` |   
`ExtensionId` | `security_result.detection_fields` |   
`ExtensionName` | `target.resource.name` |   
`ExtraInfoLength` | `additional.fields` |   
`ExtraInfoString` | `additional.fields` |   
`FailureId` | `security_result.detection_fields` |   
`faulting_application_name` | `principal.process.file.names` |   
`faulting_application_path` | `principal.process.file.full_path` |   
`FaultingModuleName` | `additional.fields` |   
`FaultingModulePath` | `additional.fields` |   
`FaultOffset` | `additional.fields` |   
`FILE_SIZE` | `about.file.size` |   
`FilterID` | `security_result.detection_fields` |   
`FinalStatus` | `security_result.description` |   
`GPODisplayName` | `target.resource.name` |   
`GPOFileSystemPath` | `target.file.full_path` |   
`Group` | `principal.resource.attribute.labels` |   
`HACK_TYPE` | `security_result.category_details` |   
`HandleId` | `target.resource.attribute.labels` |   
`HID_LEVEL` | `additional.fields` |   
`HN` | `additional.fields` |   
`host` | `principal.hostname` |   
`Hostname` | `principal.hostname` |   
`id` | `metadata.product_log_id` |   
`IdleImplementation` | `additional.fields` |   
`IdleStateCount` | `additional.fields` |   
`ImpersonationLevel` | `additional.fields` |   
`IntensiveProtectionLevel` | `security_result.detection_fields` |   
`Interface` | `security_result.detection_fields` |   
`intermediary_host` | `intermediary.ipintermediary.hostname` | Maps to `intermediary.ip` if the value is an IP address. Maps to `intermediary.hostname` if the value is a hostname.  
`INTRUSION_PAYLOAD_URL` | `target.url` |   
`INTRUSION_URL` | `target.url` |   
`IP` | `principal.ip` |   
`IP_ADDR` | `src.ip` |   
`IpAddress` | `principal.ip` |   
`IpPort` | `principal.port` |   
`KERNEL` | `principal.platform_patch_level` |   
`KeyFilePath` | `target.file.full_path` |   
`KeyLength` | `additional.fields` |   
`KeyName` | `security_result.detection_fields` |   
`KeyType` | `security_result.detection_fields` |   
`lastUpdateTime` | `target.resource.attribute.last_update_time` |   
`LmPackageName` | `security_result.detection_fields` |   
`LoadOptions` | `additional.fields` |   
`LogonGuid` | `network.session_id` |   
`LogonProcessName` | `target.application` |   
`LogonType` | `extensions.auth.auth_details` |   
`MandatoryLabel` | `target.resource.attribute.labels` |   
`MasterKeyId` | `security_result.detection_fields` |   
`MaximumPerformancePercent` | `additional.fields` |   
`Message` | `metadata.description` |   
`MinimumPerformancePercent` | `additional.fields` |   
`MinimumThrottlePercent` | `additional.fields` |   
`Minutes` | `target.resource.attribute.labels` |   
`NewFile` | `target.file.full_path` |   
`NewGrp` | `target.group.group_display_name` |   
`NewModDt` | `target.file.last_modification_time` |   
`NewOwn` | `additional.fields` |   
`NewPerms` | `additional.fields` |   
`NewProcessId` | `target.process.pid` |   
`NewProcessName` | `target.process.file.full_path` |   
`NewSecurityDescriptor` | `security_result.description` |   
`NewSize` | `additional.fields` |   
`NominalFrequency` | `principal.resource.attribute.labels` |   
`Number` | `principal.resource.attribute.labels` |   
`NumberOfGroupPolicyObjects` | `additional.fields` |   
`ObjectName` | `target.resource.name` |   
`ObjectServer` | `target.resource.attribute.labels` |   
`ObjectType` | `target.resource.resource_type` |   
`ObjId` | `target.resource.attribute.labels` |   
`OldFile` | `src.file.full_path` |   
`OldGrp` | `src.group.group_display_name` |   
`OldModDt` | `src.file.last_modification_time` |   
`OldOwn` | `additional.fields` |   
`OldPerms` | `additional.fields` |   
`OldSize` | `additional.fields` |   
`omittedFiles` | `security_result.detection_fields` |   
`Opcode` | `additional.fields` |   
`OpcodeValue` | `metadata.product_event_type` |   
`Operation` | `security_result.description` |   
`Operation` | `additional.fields` |   
`OperationType` | `security_result.category_details` |   
`OriginalSecurityDescriptor` | `additional.fields` |   
`OS` | `principal.platform` |   
`OSVER` | `principal.platform_version` |   
`param2` | `security_result.detection_fields` |   
`param3` | `security_result.detection_fields` |   
`param4` | `security_result.detection_fields` |   
`PARAM_DEVICE_ID` | `principal.hostname` |   
`PARAMETER` | `target.file.full_path` |   
`parameters` | `additional.fields` |   
`PARENT_SERVER_TYPE` | `additional.fields` |   
`PerformanceImplementation` | `additional.fields` |   
`POLNm` | `additional.fields` |   
`prevalence` | `security_result.detection_fields` |   
`Priority` | `security_result.detection_fields` |   
`PrivilegeList` | `target.resource.attribute.permissions.name` |   
`PrivilegesUsedForAccessCheck` | `security_result.detection_fields` |   
`ProblemID` | `additional.fields` |   
`ProcessId` | `principal.process.pid` |   
`ProcessID` | `target.process.pid` |   
`ProcessingMode` | `additional.fields` |   
`ProcessingTimeInMilliseconds` | `additional.fields` |   
`ProcessName` | `principal.process.file.full_path` |   
`ProcName` | `principal.process.file.names` |   
`ProcPath` | `principal.process.file.full_path` |   
`product_event_type` | `metadata.product_event_type` |   
`PROFILE_SERIAL_NO` | `additional.fields` |   
`protected` | `security_result.detection_fields` |   
`ProviderGuid` | `metadata.product_deployment_id` |   
`ProviderName` | `security_result.detection_fields` |   
`PuaCount` | `additional.fields` |   
`PuaPolicyId` | `additional.fields` |   
`PUB_KEY` | `additional.fields` |   
`Reason` | `additional.fields` |   
`ReasonCode` | `additional.fields` |   
`RecordNumber` | `metadata.product_log_id` |   
`RecoveryReason` | `security_result.description` |   
`RecType` | `metadata.product_event_type` |   
`RelativeTargetName` | `target.user.user_display_name` |   
`report_id` | `metadata.product_log_id` |   
`request` | `additional.fields` |   
`restricted_admin_mode` | `additional.fields` |   
`restricted_sid_count` | `additional.fields` |   
`risks` | `security_result.detection_fields` |   
`Rule` | `security_result.rule_name` |   
`RuleName` | `security_result.rule_name` |   
`RuleType` | `additional.fields` |   
`scan_duration` | `security_result.detection_fields` |   
`scan_state` | `security_result.detection_fields` |   
`scan_type` | `security_result.detection_fields` |   
`scanned_number` | `security_result.detection_fields` |   
`ScriptType` | `additional.fields` |   
`SecurityPackageName` | `about.file.full_path` |   
`SEQ_ID` | `additional.fields` |   
`Service` | `target.application` |   
`SeverityValue` | `security_result.severity_details` |   
`sha256` | `principal.process.file.sha256` |   
`ShareLocalPath` | `target.file.full_path` |   
`ShareName` | `target.resource.name` |   
`SITE_IDX` | `additional.fields` |   
`skipped_files` | `security_result.detection_fields` |   
`SourceModuleName` | `additional.fields` |   
`SourceModuleType` | `additional.fields` |   
`SourceName` | `principal.application` |   
`spn1` | `target.resource.attribute.labels` |   
`spn2` | `target.resource.attribute.labels` |   
`standard_schemes` | `security_result.detection_fields` |   
`State` | `additional.fields` |   
`Status` | `target.resource.attribute.labels` |   
`StopTime` | `additional.fields` |   
`SubjectDomainName` | `principal.administrative_domain` |   
`SubjectLogonId` | `principal.user.userid` |   
`SubjectUserName` | `principal.user.userid` |   
`SubjectUserSid` | `principal.user.windows_sid` |   
`SupportInfo1` | `additional.fields` |   
`SupportInfo2` | `additional.fields` |   
`syslogServer` | `intermediary.ipintermediary.hostname` | The value (the IP address or hostname) is from header of the log, and it is associated with an intermediary.  
`TargetDomainName` | `target.administrative_domain` |   
`TargetLogonId` | `target.user.userid` |   
`TargetUserName` | `target.user.userid` |   
`TargetUserSid` | `target.user.windows_sid` |   
`TaskContentNew` | `additional.fields` |   
`TaskName` | `target.resource.name` |   
`TaskValue` | `metadata.description` |   
`THREATS` | `security_result.detection_fields` |   
`threats` | `security_result.detection_fields` |   
`TimeDifferenceMilliseconds` | `additional.fields` |   
`TimeSampleSeconds` | `additional.fields` |   
`timestamp` | `metadata.event_timestamp` |   
`TokenElevationType` | `target.resource.attribute.labels` |   
`transaction_id` | `metadata.product_log_id` |   
`TransitedServices` | `security_result.detection_fields` |   
`TSId` | `network.session_id` |   
`type` | `security_result.threat_name` |   
`UMDFDeviceInstallBegin.version` | `target.resource.attribute.labels` |   
`UMDFReflectorDependencyMissing.Dependency` | `additional.fields` |   
`updateGuid` | `target.process.product_specific_process_id` |   
`updateRevisionNumber` | `target.resource.attribute.labels` |   
`updateTitle` | `target.resource.name` |   
`UpdateType` | `additional.fields` |   
`Url` | `target.url` |   
`urlTrackingStatus` | `security_result.detection_fields` |   
`User` | `principal.user.userid` |   
`UserID` | `target.user.userid` |   
`UserSid` | `target.user.windows_sid` |   
`VAPI_NAME` | `security_result.summary` |   
`VAST` | `additional.fields` |   
`Version` | `metadata.product_version` |   
`virtual_account` | `additional.fields` |   
`VSAD` | `additional.fields` |   
`WorkstationName` | `additional.fields` |   
N/A | `metadata.log_type` | The log type is hardcoded to `SEP`.  
N/A | `metadata.product_name` | The product name is hardcoded to `SEP`.  
N/A | `metadata.vendor_name` | The vendor name is hardcoded to `Symantec`.  
`COMMAND_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ATP_DEVICE_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DEVICE_INFO` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pattern_idx` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vrType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`locale` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`group_type` | `event.idm.read_only_udm.target.group.attribute.labels` | Mapped from changelog  
`group_name` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`deleted` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`discovered` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`virusname_idx` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`stealth` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`removal` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`performance` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`privacy` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dependency` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dynacat` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`catDes` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`virusname` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`RemotePort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`custom_politica_infringida` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`custom_incidente` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection.ether_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`feature_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`computer` | `intermediary.hostname` | Mapped from changelog  
`anvpap-srv1` | `intermediary.hostname` | Mapped from changelog  
`SymantecServer` | `principal.hostname` | Mapped from changelog  
`Remote Host Name` | `target.hostname` | Mapped from changelog  
`Remote Port` | `target.port` | Mapped from changelog  
`Remote Host IP` | `target.ip` | Mapped from changelog  
`Local Port` | `principal.port` | Mapped from changelog  
`Remote Host MAC` | `principal.mac` | Mapped from changelog  
`ICMP` | `network.ip_protocol` | Mapped from changelog  
`Inbound` | `network.direction` | Mapped from changelog  
`Application` | `principal.process.file.full_path` | Mapped from changelog  
`Action` | `security_result.action` | Mapped from changelog  
`SHA-256` | `principal.process.file.sha256` | Mapped from changelog  
`Size` | `principal.process.file.size` | Mapped from changelog  
`SITE_NAME" and "SOURCE` | `additional.fields` | Mapped from changelog  
`SOURCE` | `security_result.description` | Mapped from changelog  
`SCAN_ID", "CATEGORY_DESC", "CLIENT_TYPE", "DETECTION_TYPE", "HELP_VIRUS_IDX", "HPP_APP_TYPE", "IDX", "LAST_LOG_SESSION_GUID", "SITE_TYPE", "UUID", "VBIN_ID", and "VIRUS_TYPE` | `additional.fields` | Mapped from changelog  
`USER_DOMAIN_NAME` | `target.administrative_domain` | Mapped from changelog  
`COMPUTER_DOMAIN_NAME` | `principal.administrative_domain` | Mapped from changelog  
`IP_ADDR1` | `src.ip` | Mapped from changelog  
`SOURCE_COMPUTER_NAME` | `src.asset.hostname` | Mapped from changelog  
`COMPUTER_NAME` | `principal.asset.hostname` | Mapped from changelog  
`OPERATION_SYSTEM` | `principal.asset.platform_software.platform` | Mapped from changelog  
`SERVICE_PACK` | `principal.asset.platform_software.platform_version` | Mapped from changelog  
`SOURCE_COMPUTER_IP` | `principal.ip` | Mapped from changelog  
`USER_NAME` | `principal.user.userid` | Mapped from changelog  
`BIOS_SERIALNUMBER` | `principal.asset.hardware.serial_number` | Mapped from changelog  
`ACTUALACTION` | `security_result.action_details` | Mapped from changelog  
`VIRUSNAME` | `security_result.threat_name` | Mapped from changelog  
`NOOFVIRUSES` | `security_result.verdict_info.malicious_count` | Mapped from changelog  
`SOURCE", "DESCRIPTION", "REQUESTEDACTION` | `security_result.detection_fields` | Mapped from changelog  
`CLIENT_GROUP` | `principal.group.group_display_name` | Mapped from changelog  
`downloader` | `principal.process.file.full_path` | Mapped from changelog  
`REQUESTEDACTION` | `security_result.action_details` | Mapped from changelog  
`SECONDARYACTION", "ACTUALACTION", "VIRUSNAME", and "NOOFVIRUSES` | `security_result.detection_fields` | Mapped from changelog  
`SOURCE` | `additional.fields` | Mapped from changelog  
`HPP_APP_HASH` | `target.file.sha256` | Mapped from changelog  
`HPP_APP_NAME` | `target.file.names` | Mapped from changelog  
`FILEPATH` | `target.file.full_path` | Mapped from changelog  
`CLIENT_GROUP` | `target.user.group_identifiers` | Mapped from changelog  
`target_file_name" from "target.file.full_path` | `target.file.names` | Mapped from changelog  
`security_result.action` | `BLOCK` | Mapped from changelog  
`type", "utility-sub-type", "lang", "service-sandbox-type", "mojo-platform-channel-handle", "field-trial-handle", "disable-features` | `security_result.detection_fields` | Mapped from changelog  
`target_arguments` | `read_only_udm.additional.fields` | Mapped from changelog  
`user-data-dir` | `sec_result.about.file.full_path` | Mapped from changelog  
`security-realm` | `security_result.summary` | Mapped from changelog  
`startup-url` | `principal.url` | Mapped from changelog  
`source_ip` | `target.ip` | Mapped from changelog  
`action_word` | `security_result.action_details` | Mapped from changelog  
`payload.domain_name` | `principal.administrative_domain` | Mapped from changelog  
`Applicationtype` | `principal.resource.attribute.labels` | Mapped from changelog  
`mail` | `target.user.email_addresses` | Mapped from changelog  
`server_name_1` | `principal.hostname` | Mapped from changelog  
`computer` | `principal.hostname` | Mapped from changelog  
`event_description` | `metadata.description` | Mapped from changelog  
`EventDescription` | `metadata.description` | Mapped from changelog  
`LocalHostIP","IPAddress","source_ip` | `principal.ip` | Mapped from changelog  
`LocalHostMAC` | `principal.mac` | Mapped from changelog  
`guid` | `principal.asset.asset_id` | Mapped from changelog  
`DeviceID` | `principal.resource.product_object_id` | Mapped from changelog  
`Filesize` | `target.file.size` | Mapped from changelog  
`SHA256` | `target.file.sha256` | Mapped from changelog  
`User1` | `principal.user.userid` | Mapped from changelog  
`file_path` | `target.file.full_path` | Mapped from changelog  
`GroupName` | `principal.group.group_display_name` | Mapped from changelog  
`Begin` | `vulnerabilities.scan_start_time` | Mapped from changelog  
`EndTime` | `vulnerabilities.scan_end_time` | Mapped from changelog  
`ScanID` | `principal.process.product_specific_process_id` | Mapped from changelog  
`inter_host` | `intermediary.hostname` | Mapped from changelog  
`inter_ip` | `intermediary.ip` | Mapped from changelog  
`ActionType` | `additional.fields` | Mapped from changelog  
`CIDS Signature ID` | `target.resource.attribute.labels` | Mapped from changelog  
`CIDS Signature SubID` | `target.resource.attribute.labels` | Mapped from changelog  
`CIDS Signature string` | `target.resource.attribute.labels` | Mapped from changelog  
`Intrusion URL` | `principal.url` | Mapped from changelog  
`User Name` | `principal.user.userid` | Mapped from changelog  
`Actual action` | `security_result.action_details` | Mapped from changelog  
`Application hash` | `target.file.sha256` | Mapped from changelog  
`Application name` | `target.application` | Mapped from changelog  
`Application type` | `target.resource.attribute.labels` | Mapped from changelog  
`Certificate issuer` | `network.tls.server.certificate.issuer` | Mapped from changelog  
`Certificate serial number` | `network.tls.server.certificate.serial` | Mapped from changelog  
`Certificate signer` | `network.tls.server.certificate.subject` | Mapped from changelog  
`Certificate thumbprint` | `network.tls.server.certificate.sha256` | Mapped from changelog  
`Secondary action` | `target.resource.attribute.labels` | Mapped from changelog  
`First Seen` | `security_result.detection_fields` | Mapped from changelog  
`Risk Name` | `security_result.detection_fields` | Mapped from changelog  
`Risk Type` | `security_result.detection_fields` | Mapped from changelog  
`Permitted application reason` | `security_result.detection_fields` | Mapped from changelog  
`Company name` | `target.user.company_name` | Mapped from changelog  
`Computer name` | `principal.hostname` | Mapped from changelog  
`Server Name` | `principal.asset.network_domain` | Mapped from changelog  
`Confidence` | `security_result.description` | Mapped from changelog  
`Detection Type` | `security_result.summary` | Mapped from changelog  
`Group Name` | `principal.group.group_display_name` | Mapped from changelog  
`Risk Level` | `security_result.severity_details` | Mapped from changelog  
`File size (bytes)` | `target.file.size` | Mapped from changelog  
`eventDescription` | `metadata.description` | Mapped from changelog  
`hostName` | `principal.hostname` | Mapped from changelog  
`machineDomainName` | `principal.administrative_domain` | Mapped from changelog  
`domainName` | `target.administrative_domain` | Mapped from changelog  
`serverName` | `intermediary.hostname` | Mapped from changelog  
`userName` | `principal.user.userid` | Mapped from changelog  
`siteName` | `read_only_udm.additional.fields` | Mapped from changelog  
`hostName` | `target.hostname` | Mapped from changelog  
`machineDomainName` | `target.administrative_domain` | Mapped from changelog  
`domainName` | `principal.administrative_domain` | Mapped from changelog  
`serverName` | `principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sep-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
