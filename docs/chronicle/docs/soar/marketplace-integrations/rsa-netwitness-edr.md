---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness-edr/
title: RSA NetWitness EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:55.953038+00:00
---

# RSA NetWitness EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RSA NetWitness EDR

This document provides guidance on how to integrate RSA NetWitness EDR with Google SecOps.

## Use Cases

  1. Perform enrichment actions - get data from RSA NetWitness to enrich data in Google Security Operations Alerts.
  2. Perform remediation actions - add IPs/URLs to blacklists.



## Configure RSA NetWitness EDR integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://:9443 | Yes | API Root of the RSA NetWitness EDR instance.  
Username | String | N/A | Yes | Username of the RSA NetWitness EDR account.  
Password | Password | N/A | Yes | The password of the RSA NetWitness EDR account.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the RSA NetWitness EDR server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to RSA NetWitness EDR with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful:_ Print "Successfully connected to the RSA NetWitness EDR server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
****_If not successful:_ Print "Failed to connect to the RSA NetWitness EDR server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IIOC Score Threshold | Integer | 50 | No | Specify IIOC score threshold for the endpoint. If the endpoint exceeds the threshold, the related entity will be marked as suspicious. If nothing is specified, action won't check the IIOC score.  
Include IOC Information | Checkbox | Unchecked | No | If enabled, action will fetch information about the IOCs that are associated with the endpoint.  
Max IOCs To Return | Integer | 50 | No | Specify how many IOCs to return. Maximum is 50. This is RSA NetWitness EDR limitation.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | Logic-When to apply  
---|---  
RSA_EDR_DriverErrorCode | Returns if it exists in JSON result  
RSA_EDR_ServicePackOS | Returns if it exists in JSON result  
RSA_EDR_MachineStatus | Returns if it exists in JSON result  
RSA_EDR_Type | Returns if it exists in JSON result  
RSA_EDR_VersionInfo | Returns if it exists in JSON result  
RSA_EDR_UserName | Returns if it exists in JSON result  
RSA_EDR_OrganizationUnit | Returns if it exists in JSON result  
RSA_EDR_LocalIP | Returns if it exists in JSON result  
RSA_EDR_NetworkSegment | Returns if it exists in JSON result  
RSA_EDR_Gateway | Returns if it exists in JSON result  
RSA_EDR_RemoteIP | Returns if it exists in JSON result  
RSA_EDR_Group | Returns if it exists in JSON result  
RSA_EDR_AdminStatus | Returns if it exists in JSON result  
RSA_EDR_KernelDebuggerDetected | Returns if it exists in JSON result  
RSA_EDR_EarlyStart | Returns if it exists in JSON result  
RSA_EDR_NotifyShutdownModule | Returns if it exists in JSON result  
RSA_EDR_LoadedModuleModule | Returns if it exists in JSON result  
RSA_EDR_NotifyRoutineModule | Returns if it exists in JSON result  
RSA_EDR_UnloadedDriverModule | Returns if it exists in JSON result  
RSA_EDR_ErrorLogModule | Returns if it exists in JSON result  
RSA_EDR_LowLevelReaderModule | Returns if it exists in JSON result  
RSA_EDR_ProcessModule | Returns if it exists in JSON result  
RSA_EDR_WorkerThreadModule | Returns if it exists in JSON result  
RSA_EDR_WindowsHooksModule | Returns if it exists in JSON result  
RSA_EDR_DebuggerAttachedToProcess | Returns if it exists in JSON result  
RSA_EDR_ProcessMonitorModule | Returns if it exists in JSON result  
RSA_EDR_ThreadMonitorModule | Returns if it exists in JSON result  
RSA_EDR_ObjectMonitorModule | Returns if it exists in JSON result  
RSA_EDR_ImageMonitorModule | Returns if it exists in JSON result  
RSA_EDR_DriverMonitorModule | Returns if it exists in JSON result  
RSA_EDR_TdiMonitorModule | Returns if it exists in JSON result  
RSA_EDR_TrackingModule | Returns if it exists in JSON result  
RSA_EDR_TrackingRegistryMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingObjectMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingFileMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingRemoteThreadMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingCreateProcessMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingHardLinkMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingFileBlockMonitor | Returns if it exists in JSON result  
RSA_EDR_TrackingNetworkMonitor | Returns if it exists in JSON result  
RSA_EDR_ECATServerName | Returns if it exists in JSON result  
RSA_EDR_Online | Returns if it exists in JSON result  
RSA_EDR_IIOCScore | Returns if it exists in JSON result  
RSA_EDR_ChassisType | Returns if it exists in JSON result  
RSA_EDR_ContainmentSupported | Returns if it exists in JSON result  
RSA_EDR_AgentID | Returns if it exists in JSON result  
RSA_EDR_BIOS | Returns if it exists in JSON result  
RSA_EDR_OSBuildNumber | Returns if it exists in JSON result  
RSA_EDR_Comment | Returns if it exists in JSON result  
RSA_EDR_ConnectionTime | Returns if it exists in JSON result  
RSA_EDR_Language | Returns if it exists in JSON result  
RSA_EDR_DNS | Returns if it exists in JSON result  
RSA_EDR_DomainRole | Returns if it exists in JSON result  
RSA_EDR_ECATServiceCompileTime | Returns if it exists in JSON result  
RSA_EDR_ECATPackageTime | Returns if it exists in JSON result  
RSA_EDR_StartTime | Returns if it exists in JSON result  
RSA_EDR_ECATDriverCompileTime | Returns if it exists in JSON result  
RSA_EDR_DomainName | Returns if it exists in JSON result  
RSA_EDR_Idle | Returns if it exists in JSON result  
RSA_EDR_IncludedinMonitoring | Returns if it exists in JSON result  
RSA_EDR_IncludedinScanSchedule | Returns if it exists in JSON result  
RSA_EDR_InstallationFailed | Returns if it exists in JSON result  
RSA_EDR_InstallTime | Returns if it exists in JSON result  
RSA_EDR_IIOCLevel0 | Returns if it exists in JSON result  
RSA_EDR_IIOCLevel1 | Returns if it exists in JSON result  
RSA_EDR_IIOCLevel2 | Returns if it exists in JSON result  
RSA_EDR_IIOCLevel3 | Returns if it exists in JSON result  
RSA_EDR_Country | Returns if it exists in JSON result  
RSA_EDR_BootTime | Returns if it exists in JSON result  
RSA_EDR_LastScan | Returns if it exists in JSON result  
RSA_EDR_LastSeen | Returns if it exists in JSON result  
RSA_EDR_MAC | Returns if it exists in JSON result  
RSA_EDR_MachineID | Returns if it exists in JSON result  
RSA_EDR_MachineName | Returns if it exists in JSON result  
RSA_EDR_AllowAccessDataSourceDomain | Returns if it exists in JSON result  
RSA_EDR_AllowDisplayMixedContent | Returns if it exists in JSON result  
RSA_EDR_AntiVirusDisabled | Returns if it exists in JSON result  
RSA_EDR_BadCertificateWarningDisabled | Returns if it exists in JSON result  
RSA_EDR_CookiesCleanupDisabled | Returns if it exists in JSON result  
RSA_EDR_CrosssiteScriptFilterDisabled | Returns if it exists in JSON result  
RSA_EDR_FirewallDisabled | Returns if it exists in JSON result  
RSA_EDR_IEDepDisabled | Returns if it exists in JSON result  
RSA_EDR_IEEnhancedSecurityDisabled | Returns if it exists in JSON result  
RSA_EDR_IntranetZoneNotificationDisabled | Returns if it exists in JSON result  
RSA_EDR_LUADisabled | Returns if it exists in JSON result  
RSA_EDR_NoAntivirusNotificationDisabled | Returns if it exists in JSON result  
RSA_EDR_NoFirewallNotificationDisabled | Returns if it exists in JSON result  
RSA_EDR_NoUACNotificationDisabled | Returns if it exists in JSON result  
RSA_EDR_NoWindowsUpdateDisabled | Returns if it exists in JSON result  
RSA_EDR_RegistryToolsDisabled | Returns if it exists in JSON result  
RSA_EDR_SmartscreenFilterDisabled | Returns if it exists in JSON result  
RSA_EDR_SystemRestoreDisabled | Returns if it exists in JSON result  
RSA_EDR_TaskManagerDisabled | Returns if it exists in JSON result  
RSA_EDR_UACDisabled | Returns if it exists in JSON result  
RSA_EDR_WarningOnZoneCrossingDisabled | Returns if it exists in JSON result  
RSA_EDR_WarningPostRedirectionDisabled | Returns if it exists in JSON result  
RSA_EDR_Manufacturer | Returns if it exists in JSON result  
RSA_EDR_Model | Returns if it exists in JSON result  
RSA_EDR_NetworkAdapterPromiscModel | Returns if it exists in JSON result  
RSA_EDR_OperatingSystem | Returns if it exists in JSON result  
RSA_EDR_ProcessorArchitecture | Returns if it exists in JSON result  
RSA_EDR_ProcessorCount | Returns if it exists in JSON result  
RSA_EDR_Platform | Returns if it exists in JSON result  
RSA_EDR_ProcessorIs32bits | Returns if it exists in JSON result  
RSA_EDR_Processoris64 | Returns if it exists in JSON result  
RSA_EDR_ProcessorName | Returns if it exists in JSON result  
RSA_EDR_Scanning | Returns if it exists in JSON result  
RSA_EDR_ScanStartTime | Returns if it exists in JSON result  
RSA_EDR_Serial | Returns if it exists in JSON result  
RSA_EDR_TimeZone | Returns if it exists in JSON result  
RSA_EDR_TotalPhysicalMemory | Returns if it exists in JSON result  
RSA_EDR_HTTPSFallbackMode | Returns if it exists in JSON result  
RSA_EDR_BlockingActive | Returns if it exists in JSON result  
RSA_EDR_RoamingAgentsRelaySystemActive | Returns if it exists in JSON result  
RSA_EDR_UserID | Returns if it exists in JSON result  
RSA_EDR_WindowsDirectory | Returns if it exists in JSON result  
RSA_EDR_NetWitnessInvestigate | Returns if it exists in JSON result  
RSA_EDR_ContainmentStatus | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Machine": {
            "DriverErrorCode": "0xe0010014",
            "ServicePackOS": "0",
            "MachineStatus": "Offline-DriverError",
            "Type": "Windows",
            "VersionInfo": "4.4.0.0",
            "UserName": "",
            "OrganizationUnit": "",
            "LocalIP": "172.30.203.155",
            "NetworkSegment": "172.30.203.0",
            "Gateway": "172.30.203.1",
            "RemoteIP": "172.30.203.155",
            "Group": "Default",
            "AdminStatus": "",
            "KernelDebuggerDetected": "False",
            "EarlyStart": "False",
            "NotifyShutdownModule": "False",
            "LoadedModuleModule": "False",
            "NotifyRoutineModule": "False",
            "UnloadedDriverModule": "False",
            "ErrorLogModule": "False",
            "LowLevelReaderModule": "False",
            "ProcessModule": "False",
            "WorkerThreadModule": "False",
            "WindowsHooksModule": "False",
            "DebuggerAttachedToProcess": "False",
            "ProcessMonitorModule": "False",
            "ThreadMonitorModule": "False",
            "ObjectMonitorModule": "False",
            "ImageMonitorModule": "False",
            "DriverMonitorModule": "False",
            "TdiMonitorModule": "False",
            "TrackingModule": "False",
            "TrackingRegistryMonitor": "False",
            "TrackingObjectMonitor": "False",
            "TrackingFileMonitor": "False",
            "TrackingRemoteThreadMonitor": "False",
            "TrackingCreateProcessMonitor": "False",
            "TrackingHardLinkMonitor": "False",
            "TrackingFileBlockMonitor": "False",
            "TrackingNetworkMonitor": "False",
            "ECATServerName": "RSA-EDR",
            "Online": "False",
            "IIOCScore": "39",
            "ChassisType": "Other",
            "ContainmentSupported": "False",
            "AgentID": "d96de745-c39b-b513-420d-598952bd463e",
            "BIOS": "Phoenix Technologies LTD - 6.00 - PhoenixBIOS 4.0 Release 6.0",
            "OSBuildNumber": "18363",
            "Comment": "",
            "ConnectionTime": "7/31/2020 9:01:11 AM",
            "Language": "en-US",
            "DNS": "172.30.202.237",
            "DomainRole": "Member Workstation",
            "ECATServiceCompileTime": "9/15/2017 10:26:23 PM",
            "ECATPackageTime": "6/26/2020 6:39:59 AM",
            "StartTime": "6/29/2020 11:56:36 AM",
            "ECATDriverCompileTime": "9/15/2017 10:20:48 PM",
            "DomainName": "ecat.local",
            "Idle": "False",
            "IncludedinMonitoring": "True",
            "IncludedinScanSchedule": "True",
            "InstallationFailed": "False",
            "InstallTime": "6/26/2020 6:42:20 AM",
            "IIOCLevel0": "0",
            "IIOCLevel1": "0",
            "IIOCLevel2": "4",
            "IIOCLevel3": "9",
            "Country": "USA",
            "BootTime": "6/29/2020 11:56:31 AM",
            "LastScan": "6/26/2020 6:47:54 AM",
            "LastSeen": "7/31/2020 9:31:12 AM",
            "MAC": "00:50:56:A2:10:9E",
            "MachineID": "422518b6-54d8-4814-b5d7-02b043ca0103",
            "MachineName": "RSA-HOST02",
            "AllowAccessDataSourceDomain": "False",
            "AllowDisplayMixedContent": "False",
            "AntiVirusDisabled": "False",
            "BadCertificateWarningDisabled": "False",
            "CookiesCleanupDisabled": "False",
            "CrosssiteScriptFilterDisabled": "False",
            "FirewallDisabled": "False",
            "IEDepDisabled": "False",
            "IEEnhancedSecurityDisabled": "False",
            "IntranetZoneNotificationDisabled": "False",
            "LUADisabled": "False",
            "NoAntivirusNotificationDisabled": "False",
            "NoFirewallNotificationDisabled": "False",
            "NoUACNotificationDisabled": "False",
            "NoWindowsUpdateDisabled": "False",
            "RegistryToolsDisabled": "False",
            "SmartscreenFilterDisabled": "False",
            "SystemRestoreDisabled": "False",
            "TaskManagerDisabled": "False",
            "UACDisabled": "False",
            "WarningOnZoneCrossingDisabled": "False",
            "WarningPostRedirectionDisabled": "False",
            "Manufacturer": "VMware, Inc.",
            "Model": "VMware Virtual Platform",
            "NetworkAdapterPromiscMode": "False",
            "OperatingSystem": "Microsoft Windows 10 Enterprise Evaluation",
            "ProcessorArchitecture": "x64",
            "ProcessorCount": "2",
            "Platform": "64-bit (x64)",
            "ProcessorIs32bits": "False",
            "Processoris64": "True",
            "ProcessorName": "Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz",
            "Scanning": "False",
            "ScanStartTime": "7/31/2020 9:07:58 AM",
            "Serial": "VMware-42 22 a8 f8 6a 01 41 ca-12 10 80 75 56 bf 21 4b",
            "TimeZone": "Pacific Standard Time",
            "TotalPhysicalMemory": "4294430720",
            "HTTPSFallbackMode": "False",
            "BlockingActive": "True",
            "RoamingAgentsRelaySystemActive": "True",
            "UserID": "00000000-0000-0000-0000-000000000000",
            "WindowsDirectory": "C:\\Windows",
            "NetWitnessInvestigate": "True",
            "ContainmentStatus": "Not Contained"
        },
        "Iocs": [
            {
                "Alertable": "False",
                "EvaluationDate": "6/26/2020 6:48:11 AM",
                "IOCContext": "0",
                "IOCTriggeredOnMachine": "True",
                "BiasStatus": "Undefined",
                "Active": "True",
                "Description": "Likely packed",
                "Type": "Module",
                "IOCLevel": "2",
                "LastExecuted": "7/31/2020 9:08:11 AM",
                "Name": "Likely Packed.sql",
                "Priority": "0",
                "Query": "\r\n\r\nSELECT DISTINCT\r\n\t[mp].[FK_Machines] AS [FK_Machines],\r\n\t[mp].[PK_MachineModulePaths] AS [FK_MachineModulePaths]           \r\nFROM\r\n\t[dbo].[MachineModulePaths] AS [mp] WITH(NOLOCK)\r\n\tINNER JOIN [dbo].[MachinesToEvaluate] AS [me] WITH(NOLOCK) ON ([me].[RK_Machines] = [mp].[FK_Machines])\r\n\tINNER JOIN [dbo].[Modules] AS [mo] WITH(NOLOCK) ON ([mo].[PK_Modules] = [mp].[FK_Modules])\r\nWHERE \r\n\t[mo].[ModulePacked] = 0 AND\r\n\t(\r\n\t\t[mo].[ModuleCodeSectionWritable] = 1 OR\r\n\t\t[mo].[ModuleDuplicateSectionName] = 1 OR\r\n\t\t[mo].[ModuleEmptySectionName] = 1\r\n\t) AND\r\n\t[mo].[Entropy] >= 6.8 AND\r\n\t[mp].[MarkedAsDeleted]  = 0\r\n\r\n",
                "MachineCount": "1",
                "ModuleCount": "2"
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_ Print "Successfully enriched the following endpoints from RSA NetWitness EDR: \n {0}".format(entity.identifier list)  
****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to enrich the following endpoints from RSA NetWitness EDR \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_ Print: "No entities were enriched."******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich Endpoint". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | If "Include IOCs Information" == True **Table Name:** "{0} - IOCs".format(entity.identifier)**Table Column:**

  * Name (mapped as Name)
  * Type (mapped as Type)
  * IOC Level (mapped as IOCLevel)
  * Active (mapped as Active)
  * Priority (mapped as Priority)
  * Description (mapped as Description)
  * Last Executed (mapped as Last Executed)

| General  
  
### Get IOC Details

#### Description

Enrich Google SecOps Entities with information about IOCs from RSA NetWitness EDR.

**Warning:** There is a limitation with API. If the entity identifier contains a "/" character, the API request will fail.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
IOC Level Threshold | DDL | MediumPossible Values:CriticalHighMediumLow | Yes | Specify IOC level threshold for the entity. If the entity exceeds the threshold, the related entity will be marked as suspicious.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | Logic-When to apply  
---|---  
RSA_EDR_Active | Returns if it exists in JSON result  
RSA_EDR_Alertable | Returns if it exists in JSON result  
RSA_EDR_BlacklistedCount | Returns if it exists in JSON result  
RSA_EDR_GraylistedCount | Returns if it exists in JSON result  
RSA_EDR_Description | Returns if it exists in JSON result  
RSA_EDR_ErrorMessage | Returns if it exists in JSON result  
RSA_EDR_EvaluationMachineCount | Returns if it exists in JSON result  
RSA_EDR_Type | Returns if it exists in JSON result  
RSA_EDR_IOCLevel | Returns if it exists in JSON result  
RSA_EDR_LastEvaluationDuration | Returns if it exists in JSON result  
RSA_EDR_LastExecuted | Returns if it exists in JSON result  
RSA_EDR_MachineCount | Returns if it exists in JSON result  
RSA_EDR_ModuleCount | Returns if it exists in JSON result  
RSA_EDR_Name | Returns if it exists in JSON result  
RSA_EDR_Persistent | Returns if it exists in JSON result  
RSA_EDR_Priority | Returns if it exists in JSON result  
RSA_EDR_UserDefined | Returns if it exists in JSON result  
RSA_EDR_WhitelistedCount | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "iocQuery": {
            "Active": "True",
            "Alertable": "False",
            "BlacklistedCount": "0",
            "GraylistedCount": "0",
            "Description": "Autorun unsigned BHO",
            "ErrorMessage": "",
            "EvaluationMachineCount": "1",
            "Type": "Windows",
            "IOCLevel": "2",
            "LastEvaluationDuration": "0",
            "LastExecutionDuration": "0",
            "LastExecuted": "7/31/2020 9:08:12 AM",
            "MachineCount": "0",
            "ModuleCount": "0",
            "Name": "Autorun_Unsigned_BHO.sql",
            "Persistent": "True",
            "Priority": "5",
            "Query": "\r\n\r\nSELECT DISTINCT\r\n\t[mp].[FK_Machines] AS [FK_Machines],\r\n\t[mp].[PK_MachineModulePaths] AS [FK_MachineModulePaths]           \r\nFROM\r\n\t[dbo].[mocAutoruns] AS [ar] WITH(NOLOCK)\r\n\tINNER JOIN [dbo].[MachinesToEvaluate] AS [me] WITH(NOLOCK) ON ([me].[RK_Machines] = [ar].[FK_Machines])\r\n\tINNER JOIN [dbo].[Paths] AS [pa] WITH(NOLOCK) ON ([pa].[PK_Paths] = [ar].[FK_Paths__RegistryPath])\r\n\tINNER JOIN [dbo].[MachineModulePaths] AS [mp] WITH(NOLOCK) ON ([mp].[PK_MachineModulePaths] = [ar].[FK_MachineModulePaths] AND [mp].[FK_Machines] = [ar].[FK_Machines])\r\n\tINNER JOIN [dbo].[Modules] AS [mo] WITH(NOLOCK) ON ([mo].[PK_Modules] = [mp].[FK_Modules])\r\nWHERE \r\n\t[ar].[Type] = 5 AND\r\n\t[pa].[Path] LIKE N'%\\SOFTWARE%Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects\\%' AND\r\n\t[mo].[ModuleSignaturePresent] = 0 AND\r\n\t[ar].[MarkedAsDeleted] = 0\r\n\r\n",
            "UserDefined": "False",
            "WhitelistedCount": "0"
        }
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_  
****Print "Action was not able to enrich the following entities from RSA NetWitness EDR \n: {0}".format([entity.identifier])****_If fail to enrich specific entities(is_success = true):_  
****Print "Successfully enriched the following entities from RSA NetWitness EDR: \n {0}".format(entity.identifier list)****_If fail to enrich for all entities (is_success = false):_  
****Print: "No entities were enriched."  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add IP To Blacklist

#### Description

Add IP To Blacklist in RSA NetWitness EDR.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Ips": [
            "10.0.0.2"
        ],
        "ResponseStatus": {
            "ErrorCode": "200",
            "Message": "Some of the IPs could not be processed. The HTTP response body contains all successfully processed IPs"
        }
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_  
****Print "Successfully add the following IPs to blacklist in RSA NetWitness EDR: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_  
****Print "Action was not able to add the following IPs to blacklist in RSA NetWitness EDR \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_  
****Print: "No IPs were added to the blacklist in RSA NetWitness EDR."  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Add IP To Blacklist". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add URL To Blacklist

#### Description

Add URL To Blacklist in RSA NetWitness EDR.

#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "Domains": [
            "фів"
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_  
****Print "Successfully add the following URLs to blacklist in RSA NetWitness EDR: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_  
****Print "Action was not able to add the following URLs to blacklist in RSA NetWitness EDR \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_  
****Print: "No URLs were added to the blacklist in RSA NetWitness EDR."  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Add URL To Blacklist". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
