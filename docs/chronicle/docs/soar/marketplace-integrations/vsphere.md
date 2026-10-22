---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vsphere/
title: vSphere \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:55.228738+00:00
---

# vSphere  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vsphere/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# vSphere

This document provides guidance on how to integrate vSphere with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/VSphere.zip).

## Network

**Access from Google Security Operations to vSphere** Allow traffic over ports 443 (HTTPS) and 8443 (API over SSL), or as configured in your environment.

## Configure vSphere integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Get System Info

#### Description

Get information about a VM.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Vm Name | String | N/A | Target VM name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "Guest": "Microsoft Windows 7 (64-bit)",
        "Bios UUID": "423503ea-af3c-58a8-188c-f6285cec98e5",
        "VMware Tools": "toolsNotInstalled",
        "Ip Address": "1.1.1.1",
        "State": "poweredOn",
        "Template": false,
        "Path": "[DataStore] vm/vn.vmx",
        "Name": "vm",
        "Instance UUID": "50359be7-424b-e53d-5133-3f98f0e705ef"
    }
    

### Get VM by IP

#### Description

Get VM name by the IP address.

#### Parameters

N/A

#### Run On

This action run on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Guest | Returns if it exists in JSON result  
Bios UUID | Returns if it exists in JSON result  
VMware Tools | Returns if it exists in JSON result  
Ip Address | Returns if it exists in JSON result  
State | Returns if it exists in JSON result  
Template | Returns if it exists in JSON result  
Path | Returns if it exists in JSON result  
Instance UUID | Returns if it exists in JSON result  
Name | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Guest": "Microsoft Windows 7 (64-bit)",
                "Bios UUID": "423503ea-af3c-58a8-188c-f6285cec98e5",
                "VMware Tools": "toolsNotInstalled",
                "Ip Address": "1.1.1.1",
                "State": "poweredOn",
                "Template": false,
                "Path": "[DataStore] vm/vn.vmx",
                "Instance UUID": "50359be7-424b-e53d-5133-3f98f0e705ef",
                "Name": "vm"
            },
            "Entity": "1.1.1.1"
        }
    ]
    
    

### List VMs

#### Description

Get a list of all VMs that are registered.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        {
            "Guest": "Microsoft Windows 7 (64-bit)",
            "Bios UUID": "423503ea-af3c-58a8-188c-f6285cec98e5",
            "VMware Tools": "toolsNotInstalled",
            "Ip Address": "1.1.1.1",
            "State": "poweredOn",
            "Template": false,
            "Path": "[DataStore] vm/vn.vmx",
            "Name": "vm",
            "Instance UUID": "50359be7-424b-e53d-5133-3f98f0e705ef"
        }
    ]
    

### Ping

#### Description

Verify that the user has a connection to VMWare vSphere via the user's device.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Power Off

#### Description

Power off a VM.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | Target VM name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Power On

#### Description

Power on a VM.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | N/A  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | isuccess:False  
  
### Reset

#### Description

Reset a VM.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | The name of the target VM.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Revert to Snapshot

#### Description

Revert a VM settings to a state recorded in a snapshot.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | The name of the target VM.  
Snapshot Name | String | N/A | The name of the target snapshot.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Suspend

#### Description

Suspend a VM.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | The name of the target VM.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
### Take Snapshot

#### Description

Take a VM state snapshot.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
VM Name | String | N/A | The name of the target VM.  
Snapshot Name | String | N/A | The name of the target snapshot.  
Snapshot Description | String | N/A | Snapshot description value.  
  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
