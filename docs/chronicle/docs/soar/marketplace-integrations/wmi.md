---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wmi/
title: WMI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:17.921434+00:00
---

# WMI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wmi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# WMI

This document provides guidance on how to integrate WMI with Google SecOps.

## Configure WMI integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Install WMI client

To run the WMI client, execute the following commands to install the WMI client on the Google SecOps Linux Server. Make sure you have the appropriate permissions to run the commands (root). When working with the Remote Agent, run the commands on the Remote Agent server.
    
    
    wget http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/wmi-1.3.14-4.el7.art.x86_64.rpm
    sudo yum localinstall wmi-1.3.14-4.el7.art.x86_64.rpm
    

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Get System Info

#### Description

Get information about a system.

#### Parameters

**Parameter** | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | N/A | Yes | N/A  
Username | String | N/A | No | N/A  
Password | String | N/A | No | N/A  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
system_info | True/False | system_info:False  
  
##### JSON Result
    
    
    {
        "NumberOfProcessors": 1,
        "MaxProcessMemorySize": "137438953344",
        "SystemDrive": "C:",
        "WakeUpType": 6,
        "ChassisSKUNumber": "Notebook",
        "BootROMSupported": true,
        "ForegroundApplicationBoost": 2,
        "OperatingSystemSKU": 126,
        "AdminPasswordStatus": 3,
        "SuiteMask": 272,
        "InstallDate": "20161205114436.000000+120",
        "Distributed": false,
        "EncryptionLevel": 256,
        "FrontPanelResetStatus": 3,
        "Debug": false,
        "Organization": "",
        "AutomaticManagedPagefile": true,
        "PowerSupplyState": 3,
        "InfraredSupported": false,
        "LargeSystemCache": null,
        "CodeSet": "1252",
        "FreeSpaceInPagingFiles": "2415000",
        "DataExecutionPrevention_32BitApplications": true,
        "PrimaryOwnerContact": null,
        "KeyboardPasswordStatus": 3,
        "BootStatus": [0, 0, 0],
        "MaxNumberOfProcesses": -1,
        "FreePhysicalMemory": "8962948",
        "DataExecutionPrevention_Available": true,
        "PCSystemTypeEx": 2,
        "CSDVersion": null,
        "PartOfDomain": true,
        "SystemFamily": "Latitude",
        "DomainRole": 1,
        "CurrentTimeZone": 120,
        "OSType": 18,
        "SystemDirectory": "C:\\\\Windows\\\\system32",
        "Workgroup": null,
        "CountryCode": "1",
        "NameFormat": null,
        "PAEEnabled": null,
        "AutomaticResetCapability": true,
        "DataExecutionPrevention_Drivers": true,
        "TotalVirtualMemorySize": "18896472",
        "NumberOfLicensedUsers": 0,
        "DataExecutionPrevention_SupportPolicy": 2,
        "TotalSwapSpaceSize": null,
        "PowerOnPasswordStatus": 3,
        "HypervisorPresent": false,
        "SystemStartupSetting": null,
        "LocalDateTime": "20180220173653.403000+120",
        "SystemDevice": "\\\\Device\\\\HarddiskVolume2",
        "PortableOperatingSystem": false,
        "Domain": "DOMAIN.COM",
        "TotalPhysicalMemory": "16799850496",
        "ChassisBootupState": 3,
        "SystemType": "x64-based PC",
        "DNSHostName": "PC-01",
        "EnableDaylightSavingsTime": true,
        "PCSystemType": 2,
        "PrimaryOwnerName": "Windows User",
        "WindowsDirectory": "C:\\\\Windows",
        "PowerState": 0,
        "ResetCount": -1,
        "LastLoadInfo": null,
        "ServicePackMinorVersion": 0,
        "OEMStringArray": ["Dell System", "1[07A0]", "3[1.0]"],
        "BootOptionOnWatchDog": null,
        "Status": "OK",
        "OSArchitecture": "64-bit",
        "SystemStartupOptions": null,
        "OSLanguage": 1033,
        "InitialLoadInfo": null,
        "Manufacturer": "Microsoft Corporation",
        "BuildType": "Multiprocessor Free",
        "FreeVirtualMemory": "9128168",
        "OtherTypeDescription": null,
        "OEMLogoBitmap": null,
        "ServicePackMajorVersion": 0,
        "Version": "10.0.14393",
        "ThermalState": 3,
        "LastBootUpTime": "20180218183758.487061+120",
        "SizeStoredInPagingFiles": "2490368",
        "NumberOfProcesses": 133,
        "PowerManagementSupported": null,
        "CSName": "PC-01",
        "SerialNumber": "00378-30000-00003-AA585",
         "MUILanguages": ["en-US"],
         "SupportContactDescription": null,
         "Primary": true,
         "SystemStartupDelay": null,
         "ResetLimit": -1,
         "ProductType": 1,
         "RegisteredUser": "Windows User",
         "Roles": ["LM_Workstation",
                   "LM_Server",
                   "SQLServer"],
         "PlusProductID": null,
         "ResetCapability": 1,
         "SystemSKUNumber": "07A0",
         "OSProductSuite": 256,
         "PauseAfterReset": "-1",
         "NumberOfUsers": 6,
         "BootupState": "Normal boot",
         "Name": "Microsoft Windows 10 Enterprise N 2016   LTSB|C:\\\\Windows|\\\\Device\\\\Harddisk0\\\\Partition2",
         "AutomaticResetBootOption": true,
         "Caption": "Microsoft Windows 10 Enterprise N 2016 LTSB",
         "TotalVisibleMemorySize": "16406104",
         "PowerManagementCapabilities": null,
         "Model": "Latitude 7480",
         "PlusVersionNumber": null,
         "Description": "",
         "NetworkServerModeEnabled": true,
         "NumberOfLogicalProcessors": 4,
         "BootOptionOnLimit": null,
         "Locale": "0409",
         "CSCreationClassName": "Win32_ComputerSystem",
         "UserName": "DOMAIN\\\\User",
         "BuildNumber": "14393",
         "DaylightInEffect": false,
         "CreationClassName": "Win32_OperatingSystem",
         "BootDevice": "\\\\Device\\\\HarddiskVolume1"
    }
    

### List Services

#### Description

Get the list of installed services on the system.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | N/A | Yes | N/A  
Username | String | N/A | No | N/A  
Password | String | N/A | No | N/A  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
services | True/False | services:False  
  
##### JSON Result
    
    
    [
        {
            "DisplayName": "Adobe Flash Player Update Service",
            "ServiceSpecificExitCode": 0,
            "State": "Stopped",
            "SystemName": "PC-01",
            "ErrorControl": "Normal",
            "Status": "OK",
            "ProcessId": 0,
            "DesktopInteract": false,
            "Started": false,
            "AcceptStop": false,
            "CheckPoint": 0,
            "PathName": "C:\\\\Windows\\\\SysWOW64\\\\Macromed\\\\Flash\\\\FlashPlayerUpdateService.exe",
            "WaitHint": 0,
            "Name": "AdobeFlashPlayerUpdateSvc",
            "InstallDate": null,
            "Caption": "Adobe Flash Player Update Service",
            "StartMode": "Manual",
            "Description": "This service keeps your Adobe Flash Player installation up to date with the latest enhancements and security fixes.",
            "ServiceType": "Own Process",
            "TagId": 0,
            "DelayedAutoStart": false,
            "StartName": "LocalSystem",
            "AcceptPause": false,
            "CreationClassName": "Win32_Service",
            "SystemCreationClassName": "Win32_ComputerSystem",
            "ExitCode": 0
        }
    ]
    

### List Users

#### Description

List all users configured on a system.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | N/A | Yes | N/A  
Username | String | N/A | No | N/A  
Password | String | N/A | No | User's full name.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
users | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "Status": "Degraded",
            "Domain": "PC-01",
            "Description": "Built-in account for administering the computer/domain",
            "InstallDate": null,
            "Caption": "PC-01\\\\Administrator",
            "Disabled": true,
            "PasswordChangeable": true,
            "Lockout": false,
            "AccountType": 512,
            "SID": "S-1-5-21-3501119061-1410835827-1917537121-500",
            "LocalAccount": true,
            "FullName": "",
            "SIDType": 1,
            "PasswordRequired": true,
            "PasswordExpires": false,
            "Name": "Administrator"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_connected | True/False | is_connected:False  
  
##### JSON Result
    
    
    N/A
    

### Run Query

#### Description

Run an arbitrary query using WQL on the system.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Server Address | String | N/A | Yes | N/A  
Username | String | N/A | No | N/A  
Password | String | N/A | No | N/A  
WQL Query | String | N/A | Yes | Query content(e.g: SELECT Caption, Description FROM Win32_LogicalDisk WHERE DriveType <> 3).  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
results | True/False | results:False  
  
##### JSON Result
    
    
    [
       {
         "Caption": "C:",
         "Description": "Local Fixed Disk",
         "DeviceID": "C:"
       },
       {
         "Caption": "I:",
         "Description": "Local Fixed Disk",
         "DeviceID": "I:"
       }
     ]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
