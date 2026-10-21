---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-defense/
title: Carbon Black Defense \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:16:49.957386+00:00
---

# Carbon Black Defense  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-defense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Carbon Black Defense

**Important:** Carbon Black Defense was acquired by VMware and became VMware Carbon Black Endpoint Standard (Endpoint Standard).

This document describes how to integrate Carbon Black Defense with Google Security Operations.

## Configure VMware Carbon Black Endpoint Standard (Endpoint Standard) to work with Google Security Operations

### API Key

  1. Log in to the Carbon Black console.
  2. Navigate to the username in the upper right side of the page and select **Profile info**.
  3. Click **API Token** on the left side of the page to reveal your API token.

If there is no API token displayed, click **Reset** to create a new one.


**Note:** Carbon Black Configuration is used for both CB Defense and CB Response. For detailed information, see [CB Response Rest API Authentication page](https://developer.carbonblack.com/reference/enterprise-response/authentication/).

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Carbon Black Defense integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://{server-addres} | Yes | VMware Carbon Black Endpoint Standard (Endpoint Standard) API Root URL.  
API Secret Key | String | N/A | Yes | VMware Carbon Black Endpoint Standard (Endpoint Standard) API Key.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Change Device Status

**Important:** Action "Change Device Status" is no longer supported by Carbon Black Defense API.

#### Description

Change the status of a device.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Device Status | String | N/A | Yes | The new status. Example: REGISTERED  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
cb_defense_deviceId | N/A  
cb_defense_device_status | N/A  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
### Change Policy

#### Description

Change the CB Defense policy appointed to each of the queries outcome entities.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | The new policy name. Example: DFLabs_Policy  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
cb_defense_deviceId | N/A  
cb_defense_policy | N/A  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Create Policy

#### Description

Create a new policy on Cb Defense.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Name for the policy.  
Policy Description | String | N/A | Yes | A description of the policy.  
Priority Level | String | LOW | Yes | The priority score associated with sensors assigned to this policy. Example: LOW  
Policy Details | String | N/A | Yes | The policy details.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
new_policy_id | N/A | N/A  
  
### Delete Policy

#### Description

Delete a policy from Cb Defense.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Policy name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
### Delete Rule From Policy

#### Description

Remove a rule from an existing policy.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Policy name.  
Rule ID | String | N/A | Yes | Rule ID. Example: 1  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
### Get Device Info

#### Description

Get information about a device.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
assignedToName | Returns if it exists in JSON result  
macAddress | Returns if it exists in JSON result  
adGroupId | Returns if it exists in JSON result  
avEngine | Returns if it exists in JSON result  
avVdfVersion | Returns if it exists in JSON result  
rootedByAnalyticsTime | Returns if it exists in JSON result  
linuxKernelVersion | Returns if it exists in JSON result  
lastExternalIpAddress | Returns if it exists in JSON result  
lastDevicePolicyRequestedTime | Returns if it exists in JSON result  
activationCodeExpiryTime | Returns if it exists in JSON result  
currentSensorPolicyName | Returns if it exists in JSON result  
organizationName | Returns if it exists in JSON result  
deviceGuid | Returns if it exists in JSON result  
loginUserName | Returns if it exists in JSON result  
lastPolicyUpdatedTime | Returns if it exists in JSON result  
registeredTime | Returns if it exists in JSON result  
deviceSessionId | Returns if it exists in JSON result  
lastDevicePolicyChangedTime | Returns if it exists in JSON result  
windowsPlatform | Returns if it exists in JSON result  
osVersion | Returns if it exists in JSON result  
firstVirusActivityTime | Returns if it exists in JSON result  
avUpdateServers | Returns if it exists in JSON result  
lastReportedTime | Returns if it exists in JSON result  
middleName | Returns if it exists in JSON result  
activationCode | Returns if it exists in JSON result  
deregisteredTime | Returns if it exists in JSON result  
lastResetTime | Returns if it exists in JSON result  
lastInternalIpAddress | Returns if it exists in JSON result  
deviceOwnerId | Returns if it exists in JSON result  
avMaster | Returns if it exists in JSON result  
lastLocation | Returns if it exists in JSON result  
deviceType | Returns if it exists in JSON result  
targetPriorityType | Returns if it exists in JSON result  
encodedActivationCode | Returns if it exists in JSON result  
lastVirusActivityTime | Returns if it exists in JSON result  
avStatus | Returns if it exists in JSON result  
sensorStates | Returns if it exists in JSON result  
email | Returns if it exists in JSON result  
virtualizationProvider | Returns if it exists in JSON result  
avPackVersion | Returns if it exists in JSON result  
assignedToId | Returns if it exists in JSON result  
scanStatus | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
policyName | Returns if it exists in JSON result  
scanLastActionTime | Returns if it exists in JSON result  
vdiBaseDevice | Returns if it exists in JSON result  
rootedByAnalytics | Returns if it exists in JSON result  
testId | Returns if it exists in JSON result  
avProductVersion | Returns if it exists in JSON result  
rootedBySensorTime | Returns if it exists in JSON result  
lastShutdownTime | Returns if it exists in JSON result  
quarantined | Returns if it exists in JSON result  
createTime | Returns if it exists in JSON result  
deviceId | Returns if it exists in JSON result  
sensorVersion | Returns if it exists in JSON result  
passiveMode | Returns if it exists in JSON result  
virtualMachine | Returns if it exists in JSON result  
firstName | Returns if it exists in JSON result  
uninstallCode | Returns if it exists in JSON result  
uninstalledTime | Returns if it exists in JSON result  
messages | Returns if it exists in JSON result  
policyOverride | Returns if it exists in JSON result  
organizationId | Returns if it exists in JSON result  
sensorOutOfDate | Returns if it exists in JSON result  
avAveVersion | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
policyId | Returns if it exists in JSON result  
deviceMetaDataItemList | Returns if it exists in JSON result  
lastName | Returns if it exists in JSON result  
originEventHash | Returns if it exists in JSON result  
avLastScanTime | Returns if it exists in JSON result  
rootedBySensor | Returns if it exists in JSON result  
scanLastCompleteTime | Returns if it exists in JSON result  
lastContact | Returns if it exists in JSON result  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
      "EntityResult":
        {
         "assignedToName": null,
         "macAddress": null,
         "adGroupId": 0,
         "avEngine": "",
         "avVdfVersion": null,
         "rootedByAnalyticsTime": null,
         "linuxKernelVersion": null,
         "lastExternalIpAddress": "1.1.1.1",
         "lastDevicePolicyRequestedTime": null,
         "activationCodeExpiryTime": 1513776891190,
         "currentSensorPolicyName": null,
         "organizationName": "cb-internal-alliances.com",
         "deviceGuid": null,
         "loginUserName": null,
         "lastPolicyUpdatedTime": null,
         "registeredTime": 1513172091219,
         "deviceSessionId": null,
         "lastDevicePolicyChangedTime": null,
         "windowsPlatform": null,
         "osVersion": "Windows 10 x64",
         "firstVirusActivityTime": 0,
         "avUpdateServers": null,
         "lastReportedTime": 1520325064134,
         "middleName": null,
         "activationCode": null,
         "deregisteredTime": null,
         "lastResetTime": 0,
         "lastInternalIpAddress": "1.1.1.1",
         "deviceOwnerId": 260377,
         "avMaster": false,
         "lastLocation": "OFFSITE",
         "deviceType": "WINDOWS",
         "targetPriorityType": "MEDIUM",
         "encodedActivationCode": null,
         "lastVirusActivityTime": 0,
         "avStatus": ["AV_BYPASS"],
         "sensorStates": ["ACTIVE","LIVE_RESPONSE_NOT_RUNNING","LIVE_RESPONSE_NOT_KILLED"],
         "email": "ACorona",
         "virtualizationProvider": null,
         "avPackVersion": null,
         "assignedToId": null,
         "scanStatus": null,
         "name": "HP-01",
         "policyName": "default",
         "scanLastActionTime": 0,
         "vdiBaseDevice": null,
         "rootedByAnalytics": false,
         "testId": -1,
         "avProductVersion": null,
         "rootedBySensorTime": null,
         "lastShutdownTime": 1519811818082,
         "quarantined": false,
         "createTime": null,
         "deviceId": 605341,
         "sensorVersion": "1.1.1.1",
         "passiveMode": false,
         "virtualMachine": false,
         "firstName": null,
         "uninstallCode": null,
         "uninstalledTime": null,
         "messages": null,
         "policyOverride": false,
         "organizationId": 1105,
         "sensorOutOfDate": false,
         "avAveVersion": null,
         "status": "REGISTERED",
         "policyId": 6525,
         "deviceMetaDataItemList": null,
         "lastName": null,
         "originEventHash": null,
         "avLastScanTime": 0,
         "rootedBySensor": false,
         "scanLastCompleteTime": 0,
         "lastContact": 1520325053567
     },
     "Entity": "HP-01"
    }
    ]
    

### Get Events

#### Description

Get events by entity.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Time Frame | string | N/A | Yes | Time frame of the search. Example: 3h  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
eventId | Returns if it exists in JSON result  
parentApp | Returns if it exists in JSON result  
eventTime | Returns if it exists in JSON result  
selectedApp | Returns if it exists in JSON result  
attackStage | Returns if it exists in JSON result  
processDetails | Returns if it exists in JSON result  
eventType | Returns if it exists in JSON result  
targetAp | Returns if it exists in JSON result  
longDescription | Returns if it exists in JSON result  
threatIndicators | Returns if it exists in JSON result  
securityEventCode | Returns if it exists in JSON result  
registryValue | Returns if it exists in JSON result  
incidentId | Returns if it exists in JSON result  
shortDescription | Returns if it exists in JSON result  
createTime | Returns if it exists in JSON result  
alertScore | Returns if it exists in JSON result  
alertCategory | Returns if it exists in JSON result  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "0":
                {
                    "eventId": "1defe38112e911e7b34047d6447797bd",
                    "parentApp":
                    {
                        "applicationName": "C: \\\\Windows\\\\System32\\\\svchost.exe",
                        "md5Hash": null,
                        "reputationProperty": null,
                        "effectiveReputation": null,
                        "applicationPath": null,
                        "virusName": null,
                        "effectiveReputationSource": null,
                        "virusCategory": null
                        "sha256Hash": "c7db4ae8175c33a47baa3ddfa089fad17bc8e362f21e835d78ab22c9231fe370",
                        "virusSubCategory": null
                    },
                    "eventTime": 1490617768036,
                    "selectedApp":
                    {
                        "applicationName": "taskeng.exe",
                        "md5Hash": "a21ac8d41e63cf1aa24ebc165ae82c9a",
                        "reputationProperty": "TRUSTED_WHITE_LIST",
                        "effectiveReputation": null,
                        "applicationPath": "C: \\\\Windows\\\\System32\\\\taskeng.exe",
                        "virusName": null,
                        "effectiveReputationSource": null,
                        "virusCategory": null,
                        "sha256Hash": "74b9cf472d5008e00735482f084f886eaa201248d6e87ab6b1990e3670bd6693",
                        "virusSubCategory": null
                    },
                    "attackStage": null,
                    "processDetails":
                    {
                        "userName": "SYSTEM",
                        "interpreterHash": null,
                        "parentCommandLine": "C: Windows\\\\system32\\\\svchost.exe-knetsvcs",
                        "milisSinceProcessStart": 32,
                        "name": "taskeng.exe",
                        "parentPid": 772,
                        "processId": 2872,
                        "interpreterName": null,
                        "commandLine": "taskeng.exe{5267BC82-9B0D-4F0B-A566-E06CDE5602F1}S-1-5-18: NTAUTHORITY\\\\System: Service: ",
                        "parentName": "svchost.exe",
                        "parentPrivatePid": "772-1489763380982-18",
                        "targetPrivatePid": "2468-1490617768051-975",
                        "targetPid": 2468,
                        "targetCommandLine": "C: \\\\ProgramFiles(x86)\\\\Google\\\\Update\\\\GoogleUpdate.exe",
                        "privatePid": "2872-1490617768004-974",
                        "targetName": "GoogleUpdate.exe",
                        "fullUserName": "NTAUTHORITY\\\\SYSTEM"
                    },
                    "eventType": "SYSTEM_API_CALL",
                    "targetApp":
                    {
                        "applicationName": "C: \\\\ProgramFiles(x86)\\\\Google\\\\Update\\\\GoogleUpdate.exe",
                        "md5Hash": null,
                        "reputationProperty": "TRUSTED_WHITE_LIST",
                        "effectiveReputation": null,
                        "applicationPath": null,
                        "virusName": null,
                        "effectiveReputationSource": null,
                        "virusCategory": null,
                        "sha256Hash": "52fc3aa9f704300041e486e57fe863218e4cdf4c8eee05ca6b99a296efee5737",
                        "virusSubCategory": null
                    },
                    "longDescription": "",
                    "threatIndicators": ["SUSPENDED_PROCESS"],
                    "securityEventCode": null,
                    "registryValue": null,
                    "incidentId": null,
                    "shortDescription": "",
                    "createTime": 1490617872232,
                    "alertScore": 0,
                    "alertCategory": null
                }
            },
            "Entity": "HP-01"
        }
    ]
    

### Get Processes

#### Description

List processes by device.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Time Frame | string | 3h | Yes | Time frame of the search. Example: 3h  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
applicationName | Returns if it exists in JSON result  
processId | Returns if it exists in JSON result  
numEvents | Returns if it exists in JSON result  
applicationPath | Returns if it exists in JSON result  
privatePid | Returns if it exists in JSON result  
sha256Hash | Returns if it exists in JSON result  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "0":
                {
                    "applicationName": "chrome.exe",
                    "processId": 3052,
                    "numEvents": 252,
                    "applicationPath": null,
                    "privatePid": "3052-1489181082476-30",
                    "sha256Hash": "c8b01dd0153bbe4527630fb002f9ef8b4e04127bdff212831ff67bd6ab0ea265"
                }
            },
            "Entity": "HP-01"
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
