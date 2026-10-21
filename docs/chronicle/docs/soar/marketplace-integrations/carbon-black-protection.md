---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-protection/
title: Carbon Black Protection \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:52.503114+00:00
---

# Carbon Black Protection  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Carbon Black Protection

**Important:** Carbon Black Protection was acquired by VMware and became VMware Carbon Black App Control (App Control).

This document describes how to integrate Carbon Black App Control with Google Security Operations.

## Configure VMware Carbon Black App Control (App Control) to work with Google Security Operations

### API Key

To find an **API key** corresponding with a particular VMware Carbon Black App Control (App Control) user account, complete following steps:

  1. Log into the console as an administrator.
  2. Select **Administration** > **Login Accounts**.
  3. Find the user in the list then click the **Edit** button on the left hand side of the row containing their username.

**Note:** For detailed information regarding VMware Carbon Black App Control (App Control) authentication, see [here](https://developer.carbonblack.com/reference/enterprise-protection/authentication/).

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Carbon Black Protection integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://x.x.x.x | Yes | The address of the VMware Carbon Black App Control (App Control) instance.  
Api Key | String | N/A | Yes | API key generated in VMware Carbon Black App Control (App Control)'s console.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Analyze File

#### Description

Analyze a file.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Connector Name | String | N/A | Yes | The name of the analyzing connector. Example: Palo Alto Networks  
Priority | String | N/A | Yes | The priority of the analysis (-2 to 2).  
Timeout | String | N/A | Yes | Wait timeout. Example: 120  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entity is marked as suspicious if CB Protection detects an MSI file that has data appended after the signature.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
computerId | Returns if it exists in JSON result  
connectorId | Returns if it exists in JSON result  
analysisStatus | Returns if it exists in JSON result  
dateCreated | Returns if it exists in JSON result  
priority | Returns if it exists in JSON result  
createdByUserId | Returns if it exists in JSON result  
is_malicious | Returns if it exists in JSON result  
pathName | Returns if it exists in JSON result  
fileCatalogId | Returns if it exists in JSON result  
createdBy | Returns if it exists in JSON result  
analysisResult | Returns if it exists in JSON result  
dateModified | Returns if it exists in JSON result  
fileName | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
analysisTarget | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
        "EntityResult":
            {
              "computerId": 1,
              "connectorId": 2,
              "analysisStatus": 0,
              "dateCreated": "2019-01-17T09:17:41.663Z",
              "priority": 0,
              "createdByUserId": 0,
              "is_malicious": "True",
              "pathName": "c:\\\\\\\\windows\\\\\\\\winsxs\\\\\\\\trojan.conf",
              "fileCatalogId": 23718,
              "createdBy": "admin",
              "analysisResult": 0,
              "dateModified": "2019-01-17T09:30:28.053Z",
              "fileName": "iexpress.exe",
              "id": 17,
              "analysisTarget": ""
             },
         "Entity": "FSFSD213CGJK3423423FCFS33dFSV123"
    }]
    

### Block Hash

#### Description

Block a hash on specific policies or globally.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Policy Names | String | N/A | No | Example: Default Policy, Local Approval Policy  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Change Computer Policy

#### Description

Move a computer to a new policy.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Policy Name | String | N/A | Yes | The new policy name. Example: Default Policy  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Find File

#### Description

Find a file instance on multiple computers.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
executed | Returns if it exists in JSON result  
fileName | Returns if it exists in JSON result  
computerId | Returns if it exists in JSON result  
unifiedSource | Returns if it exists in JSON result  
policyId | Returns if it exists in JSON result  
detailedLocalState | Returns if it exists in JSON result  
dateCreated | Returns if it exists in JSON result  
topLevel | Returns if it exists in JSON result  
certificateId | Returns if it exists in JSON result  
pathName | Returns if it exists in JSON result  
localState | Returns if it exists in JSON result  
initialized | Returns if it exists in JSON result  
detachedCertificateId | Returns if it exists in JSON result  
detachedPublisherId | Returns if it exists in JSON result  
fileInstanceGroupId | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
fileCatalogId | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
       "executed": "true",
       "fileName": "iexpress.exe",
       "computerId": 1,
       "unifiedSource": "null",
       "policyId": 1,
       "detailedLocalState": 3,
       "dateCreated": "2018-05-29T10:09:27Z",
       "topLevel": "false",
       "certificateId": 0,
       "pathName": "c:\\\\\\\\windows\\\\\\\\syswow64",
       "localState": 3,
       "initialized": "true",
       "detachedCertificateId": 33,
       "detachedPublisherId": 8,
       "fileInstanceGroupId": 1,
       "id": 37372,
       "fileCatalogId": 23718
    }]
    

### Get Computers by File

#### Description

Get the computers on which a file with the given SHA-256 value exists.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": "00:50:56:11:22:33",
            "Entity": "macAddress"
        }, {
            "EntityResult": 0,
            "Entity": "systemMemoryDumps"
        }, {
            "EntityResult": "Agent did not receive all the rules yet",
            "Entity": "policyStatusDetails"
        }, {
            "EntityResult": "False",
            "Entity": "prioritized"
        }, {
            "EntityResult": 1,
            "Entity": "platformId"
        }, {
            "EntityResult": "None",
            "Entity": "upgradeErrorTime"
        }, {
            "EntityResult": 0,
            "Entity": "tdCount"
        }, {
            "EntityResult": "False",
            "Entity": "hasDuplicates"
        }, {
            "EntityResult": 60,
            "Entity": "disconnectedEnforcementLevel"
        }, {
            "EntityResult": "False",
            "Entity": "hasHealthCheckErrors"
        }, {
            "EntityResult": 100,
            "Entity": "syncPercent"
        }, {
            "EntityResult": 0,
            "Entity": "agentQueueSize"
        }, {
            "EntityResult": "1.1.1.1",
            "Entity": "agentVersion"
        }, {
            "EntityResult": 0,
            "Entity": "activeDebugLevel"
        }, {
            "EntityResult": "True",
            "Entity": "tamperProtectionActive"
        }, {
            "EntityResult": 0,
            "Entity": "refreshFlags"
        }, {
            "EntityResult": 0,
            "Entity": "cbSensorFlags"
        }, {
            "EntityResult": "None",
            "Entity": "templateCloneCleanupMode"
        }, {
            "EntityResult": 2,
            "Entity": "activeKernelDebugLevel"
        }, {
            "EntityResult": "None",
            "Entity": "description"
        }, {
            "EntityResult": "Default Policy",
            "Entity": "policyName"
        }, {
            "EntityResult": 60,
            "Entity": "enforcementLevel"
        }, {
            "EntityResult": "None",
            "Entity": "templateDate"
        }, {
            "EntityResult": 6,
            "Entity": "previousPolicyId"
        }, {
            "EntityResult": 8192,
            "Entity": "memorySize"
        }, {
            "EntityResult": 1212,
            "Entity": "clVersion"
        }, {
            "EntityResult": 1,
            "Entity": "id"
        }, {
            "EntityResult": "Approvals out of date",
            "Entity": "policyStatus"
        }, {
            "EntityResult": 2200.0,
            "Entity": "processorSpeed"
        }, {
            "EntityResult": 0,
            "Entity": "ccFlags"
        }, {
            "EntityResult": "False",
            "Entity": "template"
        }, {
            "EntityResult": "False",
            "Entity": "initializing"
        }, {
            "EntityResult": "False",
            "Entity": "uninstalled"
        }, {
            "EntityResult": 0,
            "Entity": "upgradeErrorCount"
        }, {
            "EntityResult": 0,
            "Entity": "templateComputerId"
        }, {
            "EntityResult": 55,
            "Entity": "daysOffline"
        }, {
            "EntityResult": "None",
            "Entity": "upgradeError"
        }, {
            "EntityResult": "False",
            "Entity": "automaticPolicy"
        }, {
            "EntityResult": "WORKGROUP\\\\\\\\TEST$,Window Manager\\\\\\\\TEST-4",
            "Entity": "users"
        }, {
            "EntityResult": "Windows Server 2012",
            "Entity": "osShortName"
        }, {
            "EntityResult": "False",
            "Entity": "deleted"
        }, {
            "EntityResult": 100,
            "Entity": "initPercent"
        }, {
            "EntityResult": "False",
            "Entity": "templateTrackModsOnly"
        }, {
            "EntityResult": 16,
            "Entity": "activeDebugFlags"
        }, {
            "EntityResult": "TEST-TEST-TEST-TEST",
            "Entity": "CLIPassword"
        }, {
            "EntityResult": "2018-05-29T10:10:19.26Z",
            "Entity": "dateCreated"
        }, {
            "EntityResult": "Yes",
            "Entity": "virtualized"
        }, {
            "EntityResult": 0,
            "Entity": "agentMemoryDumps"
        }, {
            "EntityResult": "False",
            "Entity": "connected"
        }, {
            "EntityResult": -1,
            "Entity": "debugLevel"
        }, {
            "EntityResult": "None",
            "Entity": "cbSensorVersion"
        }, {
            "EntityResult": "Up to date",
            "Entity": "upgradeStatus"
        }, {
            "EntityResult": "False",
            "Entity": "localApproval"
        }, {
            "EntityResult": "False",
            "Entity": "isActive"
        }, {
            "EntityResult": "WORKGROUP\\\\\\\\TEST",
            "Entity": "name"
        }, {
            "EntityResult": 0,
            "Entity": "debugFlags"
        }, {
            "EntityResult": "VMware",
            "Entity": "virtualPlatform"
        }, {
            "EntityResult": "None",
            "Entity": "computerTag"
        }, {
            "EntityResult": "2018-11-22T10:49:41.583Z",
            "Entity": "lastRegisterDate"
        }, {
            "EntityResult": 0,
            "Entity": "debugDuration"
        }, {
            "EntityResult": 0,
            "Entity": "cbSensorId"
        }, {
            "EntityResult": 0,
            "Entity": "SCEPStatus"
        }, {
            "EntityResult": 43432,
            "Entity": "agentCacheSize"
        }, {
            "EntityResult": 4,
            "Entity": "processorCount"
        }, {
            "EntityResult": "VMware Virtual Platform",
            "Entity": "machineModel"
        }, {
            "EntityResult": "Microsoft Windows Server 2012 R2 x64 Server Standard (Evaluation) (6.3.9600)",
            "Entity": "osName"
        }, {
            "EntityResult": "None",
            "Entity": "templateCloneCleanupTimeScale"
        }, {
            "EntityResult": 1,
            "Entity": "policyId"
        }, {
            "EntityResult": "False",
            "Entity": "forceUpgrade"
        }, {
            "EntityResult": "2018-11-23T21:59:12.613Z",
            "Entity": "lastPollDate"
        }, {
            "EntityResult": "None",
            "Entity": "templateCloneCleanupTime"
        }, {
            "EntityResult": "True",
            "Entity": "supportedKernel"
        }, {
            "EntityResult": 0,
            "Entity": "kernelDebugLevel"
        }, {
            "EntityResult": 0,
            "Entity": "ccLevel"
        }, {
            "EntityResult": "1.1.1.1",
            "Entity": "ipAddress"
        }, {
            "EntityResult": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
            "Entity": "processorModel"
        }, {
            "EntityResult": 8,
            "Entity": "syncFlags"
        }
    ]
    

### Get System Info

#### Description

Get information about a computer.

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
macAddress | Returns if it exists in JSON result  
systemMemoryDumps | Returns if it exists in JSON result  
policyStatusDetails | Returns if it exists in JSON result  
prioritized | Returns if it exists in JSON result  
platformId | Returns if it exists in JSON result  
upgradeErrorTime | Returns if it exists in JSON result  
tdCount | Returns if it exists in JSON result  
hasDuplicates | Returns if it exists in JSON result  
disconnectedEnforcementLevel | Returns if it exists in JSON result  
hasHealthCheckErrors | Returns if it exists in JSON result  
syncPercent | Returns if it exists in JSON result  
agentVersion | Returns if it exists in JSON result  
activeDebugLevel | Returns if it exists in JSON result  
templateCloneCleanupMode | Returns if it exists in JSON result  
processorCount | Returns if it exists in JSON result  
kernelDebugLevel | Returns if it exists in JSON result  
refreshFlags | Returns if it exists in JSON result  
activeKernelDebugLevel | Returns if it exists in JSON result  
users | Returns if it exists in JSON result  
policyName | Returns if it exists in JSON result  
enforcementLevel | Returns if it exists in JSON result  
templateDate | Returns if it exists in JSON result  
previousPolicyId | Returns if it exists in JSON result  
memorySize | Returns if it exists in JSON result  
machineModel | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
policyStatus | Returns if it exists in JSON result  
processorSpeed | Returns if it exists in JSON result  
ccFlags | Returns if it exists in JSON result  
template | Returns if it exists in JSON result  
initializing | Returns if it exists in JSON result  
initPercent | Returns if it exists in JSON result  
uninstalled | Returns if it exists in JSON result  
computerTag | Returns if it exists in JSON result  
templateComputerId | Returns if it exists in JSON result  
initPercent | Returns if it exists in JSON result  
uninstalled | Returns if it exists in JSON result  
computerTag | Returns if it exists in JSON result  
templateComputerId | Returns if it exists in JSON result  
daysOffline | Returns if it exists in JSON result  
upgradeError | Returns if it exists in JSON result  
automaticPolicy | Returns if it exists in JSON result  
description | Returns if it exists in JSON result  
osShortName | Returns if it exists in JSON result  
deleted | Returns if it exists in JSON result  
localApproval | Returns if it exists in JSON result  
tamperProtectionActive | Returns if it exists in JSON result  
lastPollDate | Returns if it exists in JSON result  
activeDebugFlags | Returns if it exists in JSON result  
CLIPassword | Returns if it exists in JSON result  
dateCreated | Returns if it exists in JSON result  
virtualPlatform | Returns if it exists in JSON result  
connected | Returns if it exists in JSON result  
supportedKernel | Returns if it exists in JSON result  
debugLevel | Returns if it exists in JSON result  
cbSensorVersion | Returns if it exists in JSON result  
upgradeStatus | Returns if it exists in JSON result  
upgradeErrorCount | Returns if it exists in JSON result  
upgradeErrorCount | Returns if it exists in JSON result  
isActive | Returns if it exists in JSON result  
debugFlags | Returns if it exists in JSON result  
agentMemoryDumps | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
lastRegisterDate | Returns if it exists in JSON result  
ipAddress | Returns if it exists in JSON result  
cbSensorId | Returns if it exists in JSON result  
SCEPStatus | Returns if it exists in JSON result  
agentCacheSize | Returns if it exists in JSON result  
cbSensorFlags | Returns if it exists in JSON result  
clVersion | Returns if it exists in JSON result  
osName | Returns if it exists in JSON result  
templateCloneCleanupTimeScale | Returns if it exists in JSON result  
policyId | Returns if it exists in JSON result  
forceUpgrade | Returns if it exists in JSON result  
templateTrackModsOnly | Returns if it exists in JSON result  
templateCloneCleanupTime | Returns if it exists in JSON result  
agentQueueSize | Returns if it exists in JSON result  
virtualized | Returns if it exists in JSON result  
ccLevel | Returns if it exists in JSON result  
debugDuration | Returns if it exists in JSON result  
processorModel | Returns if it exists in JSON result  
syncFlags | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
      "macAddress": "00:50:56:B5:30:57",
      "systemMemoryDumps": 0,
      "policyStatusDetails": "Agent did not receive all the rules yet",
      "prioritized": "False",
      "platformId": 1,
      "upgradeErrorTime": "None",
      "tdCount": 0,
      "hasDuplicates": "False",
      "disconnectedEnforcementLevel": 60,
      "hasHealthCheckErrors": "False",
      "syncPercent": 100,
      "agentVersion": "8.0.0.2562",
      "activeDebugLevel": 0,
      "templateCloneCleanupMode": "None",
      "processorCount": 4,
      "kernelDebugLevel": 0,
      "refreshFlags": 0,
      "activeKernelDebugLevel": 2,
      "users": "WORKGROUP\\\\\\\\SIEMPLIFY$,Window Manager\\\\\\\\DWM-4",
      "policyName": "Default Policy",
      "enforcementLevel": 60,
      "templateDate": "None",
      "previousPolicyId": 6,
      "memorySize": 8192,
      "machineModel": "VMware Virtual Platform",
      "id": 1,
      "policyStatus": "Approvals out of date",
      "processorSpeed": 2200.0,
      "ccFlags": 0,
      "template": "False",
      "initializing": "False",
      "initPercent": 100,
      "uninstalled": "False",
      "computerTag": "None",
      "templateComputerId": 0,
      "daysOffline": 55,
      "upgradeError": "None",
      "automaticPolicy": "False",
      "description": "None",
      "osShortName": "Windows Server 2012",
      "deleted": "False",
      "localApproval": "False",
      "tamperProtectionActive": "True",
      "lastPollDate": "2018-11-23T21:59:12.613Z",
      "activeDebugFlags": 16,
      "CLIPassword": "EYTL-TOYF-EYKG-NIHJ",
      "dateCreated": "2018-05-29T10:10:19.26Z",
      "virtualPlatform": "VMware",
      "connected": "False",
      "supportedKernel": "True",
      "debugLevel": -1,
      "cbSensorVersion": "None",
      "upgradeStatus": "Up to date",
      "upgradeErrorCount": 0,
      "isActive": "False",
      "debugFlags": 0,
      "agentMemoryDumps": 0,
      "name": "WORKGROUP\\\\\\\\SIEMPLIFY",
      "lastRegisterDate": "2018-11-22T10:49:41.583Z",
      "ipAddress": "10.0.0.67",
      "cbSensorId": 0,
      "SCEPStatus": 0,
      "agentCacheSize": 43432,
      "cbSensorFlags": 0,
      "clVersion": 1212,
      "osName": "Microsoft Windows Server 2012 R2 x64 Server Standard (Evaluation) (6.3.9600)",
      "templateCloneCleanupTimeScale": "None",
      "policyId": 1,
       "forceUpgrade": "False",
       "templateTrackModsOnly": "False",
       "templateCloneCleanupTime": "None",
       "agentQueueSize": 0,
       "virtualized": "Yes",
       "ccLevel": 0,
       "debugDuration": 0,
       "processorModel": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
       "syncFlags": 8
    }
    

### Ping

#### Description

Test connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Unblock Hash

#### Description

Unblock a hash on specific policies or globally.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Policy Names | String | N/A | No | Separated by comma. Example: Default Policy, Local Approval Policy  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
