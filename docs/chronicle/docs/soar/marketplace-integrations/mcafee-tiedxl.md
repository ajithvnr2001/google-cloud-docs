---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-tiedxl/
title: McAfee TIE DXL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:48.573556+00:00
---

# McAfee TIE DXL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-tiedxl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee TIE DXL

**Important:** This integration refers to McAfee Threat Intelligence Exchange (TIE) DXL.

This document provides guidance on how to integrate McAfee TIE DXL with Google SecOps.

## Configure McAfee TIE DXL integration to work with Google Security Operations

### Generate Certificates

To begin, you'll need to create certificates so that Trellix ePO and DXL are able to properly communicate with the Google SecOps system. Please follow the instructions below to generate the certificate you will need for this integration to function properly.

  1. SSH into your Google SecOps server.

**Note:** Optionally, you may perform this on your local machine instead and copy to your Google SecOps server.
  2. Issue the following command: `pip install dxlclient`

  3. Change directory to /etc/pki/tls/: `cd /etc/pki/tls/`

  4. Switch the user to scripting: `su -l scripting`

  5. Make a directory for your new certificates and open the new directory:
         
         mkdir tiedxl
         cd tiedxl
         




Follow the instructions here to generate your certificates:

  1. [https://opendxl.github.io/opendxl-client](https://opendxl.github.io/opendxl-client-python/pydoc/basiccliprovisioning.html#basiccliprovisioning)
  2. [python/pydoc/basiccliprovisioning.html#basiccliprovisioning](https://opendxl.github.io/opendxl-client-python/pydoc/basiccliprovisioning.html#basiccliprovisioning)



### Add Your Certificates to Trellix ePO

Follow the instructions at [ePO Certificate Authority (CA) Import](https://opendxl.github.io/opendxl-client-python/pydoc/epocaimport.html) to add your ca-bundle.crt file to your Trellix ePO instance.

For more information, see [Command Line Provisioning (Basic)](https://opendxl.github.io/opendxl-client-python/pydoc/basiccliprovisioning.html). It contains a script, that creates the necessary files for the integrations.

Also, as seen in the image below, in Trellix ePO we can find the address of the broker and its port (Server settings > DXL Topology). And in DXL Certificates tabs we can manage the certificate files (as documented in the links above).

![Location of broker address and its port in
Trellix ePO](https://docs.cloud.google.com/static/chronicle/images/integrations/mcafee-tiedxl-broker-address-and-port-location.png)

## Configure McAfee TIE DXL integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add Tag

#### Description

Add a tag to an endpoint. (Only tags that exist in the system).

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Tag Name | String | N/A | The name of the tag to add.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Compare Server and Agent DAT

#### Description

Compare a server and agent DAT.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
agent_dat_status | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Agent Information

#### Description

Get information regarding a Trellix ePO endpoint.

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
LastUpdate | Returns if it exists in JSON result  
ManagedState | Returns if it exists in JSON result  
Tags | Returns if it exists in JSON result  
ExcludedTags | Returns if it exists in JSON result  
AgentVersion | Returns if it exists in JSON result  
AgentGUID | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          {
             "LastUpdate": "2019-01-22T13:04:49+02:00",
             "ManagedState": "1",
             "Tags": "Server, Workstation",
             "ExcludedTags": "",
             "AgentVersion": "1.1.1.1",
             "AgentGUID": "F673D1DF-786C-41E5-A84D-1676A39F7AE8"
           },
       "Entity": "1.1.1.1"
    }]
    

### Dat Version

#### Description

Retrieve the version of DAT that is installed on an endpoint.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Dat Version | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get Events for Hash

#### Description

Get event details for the MD5 hash.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Fetch Events From EPExtendedEvent Table | Checkbox | N/A | Whether to fetch events from the EPExtendedEvent table**.**  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
EPOEvents.ThreatCategory | Returns if it exists in JSON result  
EPOEvents.TargetUserName | Returns if it exists in JSON result  
EPOEvents.TargetPort | Returns if it exists in JSON result  
EPOEvents.TargetFileName | Returns if it exists in JSON result  
EPOEvents.TargetIPV4 | Returns if it exists in JSON result  
EPOEvents.ThreatName | Returns if it exists in JSON result  
EPOEvents.SourceUserName | Returns if it exists in JSON result  
EPOEvents.TargetProcessName | Returns if it exists in JSON result  
EPOEvents.SourceProcessName | Returns if it exists in JSON result  
EPOEvents.ThreatType | Returns if it exists in JSON result  
EPOEvents.SourceIPV4 | Returns if it exists in JSON result  
EPOEvents.TargetProtocol | Returns if it exists in JSON result  
VSECustomEvent.MD5 | Returns if it exists in JSON result  
EPOEvents.SourceURL | Returns if it exists in JSON result  
EPOEvents.ThreatActionTaken | Returns if it exists in JSON result  
EPOEvents.TargetHostName | Returns if it exists in JSON result  
EPOEvents.ThreatHandled | Returns if it exists in JSON result  
EPOEvents.SourceHostName | Returns if it exists in JSON result  
  
##### Insights

Yes

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         [{
            "EPOEvents.ThreatCategory": "av.detect",
            "EPOEvents.TargetUserName": "VM-EPOAGENTTEST\\\\\\\\Admin",
            "EPOEvents.TargetPort": "None",
            "EPOEvents.TargetFileName": "C:\\\\\\\\Users\\\\\\\\Admin\\\\\\\\Desktop\\\\\\\\eicar.txt",
            "EPOEvents.TargetIPV4": -1979711347,
            "EPOEvents.ThreatName": "EICAR test file",
            "EPOEvents.SourceUserName": "None",
            "EPOEvents.TargetProcessName": "None",
            "EPOEvents.SourceProcessName": "None",
            "EPOEvents.ThreatType": "test",
            "EPOEvents.SourceIPV4": -1979711347,
            "EPOEvents.TargetProtocol": "None",
            "VSECustomEvent.MD5": "44d88612fea8a8f36de82e1278abb02f",
            "EPOEvents.SourceURL": "None",
            "EPOEvents.ThreatActionTaken": "deleted",
            "EPOEvents.TargetHostName": "VM-EPOAGENTTEST",
            "EPOEvents.ThreatHandled": "True",
            "EPOEvents.SourceHostName": "_"
          }, {
            "EPOEvents.ThreatCategory": "av.detect",
            "EPOEvents.TargetUserName": "VM-EPOAGENTTEST\\\\\\\\Admin",
            "EPOEvents.TargetPort": "None",
            "EPOEvents.TargetFileName": "C:\\\\\\\\Users\\\\\\\\Admin\\\\\\\\Desktop\\\\\\\\eicar.txt",
            "EPOEvents.TargetIPV4": -1979711347,
            "EPOEvents.ThreatName": "EICAR test file",
            "EPOEvents.SourceUserName": "None",
            "EPOEvents.TargetProcessName": "None",
            "EPOEvents.SourceProcessName": "None",
            "EPOEvents.ThreatType": "test",
            "EPOEvents.SourceIPV4": -1979711347,
            "EPOEvents.TargetProtocol": "None",
            "VSECustomEvent.MD5": "44d88612fea8a8f36de82e1278abb02f",
            "EPOEvents.SourceURL": "None",
            "EPOEvents.ThreatActionTaken": "deleted",
            "EPOEvents.TargetHostName": "VM-EPOAGENTTEST",
            "EPOEvents.ThreatHandled": "True",
            "EPOEvents.SourceHostName": "_"
          }],
      "Entity": "44d88612fea8a8f36de82e1278abb02f"
    }]
    

### Get Host IPs Status

#### Description

Get the status of an IP for the host.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_status_received | True/False | is_status_received:False  
  
##### JSON Result
    
    
    N/A
    

### Get Host Network IPs Status

#### Description

Get the status of an IP for the host network.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_status_received | True/False | is_status_received:False  
  
##### JSON Result
    
    
    N/A
    

### Get Host Solid Core Status

#### Description

Retrieve the status of the solid core regarding the host.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_status_received | True/False | is_status_received:False  
  
##### JSON Result
    
    
    N/A
    

### Get Last Communication Time

#### Description

Receive the last communication time for the host.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
isSuccess | True/False | isSuccess:False  
  
##### JSON Result
    
    
    N/A
    

### Get McAfee EPO Agent Version

#### Description

Retrieve the agent version of Trellix ePO.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
McAfee Agent Version | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Get System Information

#### Description

Get system information on an endpoint from Trellix ePO.

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
FreeDiskSpace | Returns if it exists in JSON result  
UserName | Returns if it exists in JSON result  
DomainName | Returns if it exists in JSON result  
LastAgentHandler | Returns if it exists in JSON result  
IPV4x | Returns if it exists in JSON result  
OSBitMode | Returns if it exists in JSON result  
IPV6 | Returns if it exists in JSON result  
OSType | Returns if it exists in JSON result  
SysvolFreeSpace | Returns if it exists in JSON result  
IPHostName | Returns if it exists in JSON result  
CPUSerialNum | Returns if it exists in JSON result  
IPSubnetMask | Returns if it exists in JSON result  
SysvolTotalSpace | Returns if it exists in JSON result  
IPSubnet | Returns if it exists in JSON result  
Description | Returns if it exists in JSON result  
FreeMemory | Returns if it exists in JSON result  
CPUSpeed | Returns if it exists in JSON result  
SubnetMask | Returns if it exists in JSON result  
IPAddress | Returns if it exists in JSON result  
DefaultLangID | Returns if it exists in JSON result  
OSPlatform | Returns if it exists in JSON result  
ComputerName | Returns if it exists in JSON result  
OSOEMID | Returns if it exists in JSON result  
NetAddress | Returns if it exists in JSON result  
TotalDiskSpace | Returns if it exists in JSON result  
SubnetAddress | Returns if it exists in JSON result  
NumOfCPU | Returns if it exists in JSON result  
TimeZone | Returns if it exists in JSON result  
SystemDescription | Returns if it exists in JSON result  
Vdi | Returns if it exists in JSON result  
OSBuildNum | Returns if it exists in JSON result  
OSVersion | Returns if it exists in JSON result  
IsPortable | Returns if it exists in JSON result  
TotalPhysicalMemory | Returns if it exists in JSON result  
IPXAddress | Returns if it exists in JSON result  
UserProperty7 | Returns if it exists in JSON result  
UserProperty6 | Returns if it exists in JSON result  
UserProperty5 | Returns if it exists in JSON result  
UserProperty4 | Returns if it exists in JSON result  
UserProperty3 | Returns if it exists in JSON result  
UserProperty2 | Returns if it exists in JSON result  
UserProperty1 | Returns if it exists in JSON result  
ParentID | Returns if it exists in JSON result  
CPUType | Returns if it exists in JSON result  
UserProperty8 | Returns if it exists in JSON result  
  
##### Insights

YES

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
          {
            "FreeDiskSpace": "444316",
            "UserName": "Admin",
            "OSServicePackVer": "",
            "DomainName": "WORKGROUP",
            "LastAgentHandler": "1",
            "IPV4x": "-1979711239",
            "OSBitMode": "1",
            "IPV6": "0:0:0:0:0:FFFF:A00:F9",
            "OSType": "Windows Server 2012 R2",
            "SysvolFreeSpace": "94782",
            "IPHostName": "McAfee-ePO",
            "CPUSerialNum": "N/A",
            "IPSubnetMask": "0:0:0:0:0:FFFF:FFFF:FE00",
            "SysvolTotalSpace": "161647",
            "IPSubnet": "0:0:0:0:0:FFFF:A00:0",
            "Description": "None",
            "FreeMemory": "1626767360",
            "CPUSpeed": "2400",
            "SubnetMask": "",
            "IPAddress": "1.1.1.1",
            "DefaultLangID": "0409",
            "OSPlatform": "Server",
            "ComputerName": "MCAFEE-EPO",
            "OSOEMID": "00252-00112-26656-AA653",
            "NetAddress": "005056A56847",
            "TotalDiskSpace": "511646",
            "SubnetAddress": "",
            "NumOfCPU": "4",
            "TimeZone": "Jerusalem Standard Time",
            "SystemDescription": "N/A",
            "Vdi": "0",
            "OSBuildNum": "9600",
            "OSVersion": "6.3",
            "IsPortable": "0",
            "TotalPhysicalMemory": "6441984000",
            "IPXAddress": "N/A",
            "UserProperty7": "",
            "UserProperty6": "",
            "UserProperty5": "",
            "UserProperty4": "",
            "UserProperty3": "",
            "UserProperty2": "",
            "UserProperty1": "",
            "ParentID": "8",
            "CPUType": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz",
            "UserProperty8": ""
         },
     "Entity": "1.1.1.1"
    }]​​
    

### Get Virus Engine Agent Version

#### Description

Retrieve the engine version of Trellix ePO.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Virus Engine Agent Version | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Ping

#### Description

Test Connectivity.

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

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Remove Tag

#### Description

Remove a tag from the endpoint.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Tag Name | String | N/A | The name of the tag to remove.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Run Full Scan

#### Description

Run a full scan on an endpoint.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Tag Name | String | N/A | The name of the task to run.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
RunTask_Status | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Update Mcafee Agent

#### Description

Run a task to update the McAfee agent.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Tag Name | String | N/A | The name of the task to run.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Update_Status | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
