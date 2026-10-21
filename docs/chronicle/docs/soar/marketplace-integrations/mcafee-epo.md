---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-epo/
title: McAfee ePO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:18.892534+00:00
---

# McAfee ePO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-epo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee ePO

**Important:** McAfee ePO became part of the Trellix product portfolio and was renamed to Trellix ePO.

This document provides guidance on how to integrate McAfee ePO with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/McAfeeEPO.zip).

## Configure McAfee ePO integration in Google Security Operations

### Configure McAfee ePO integration with a CA certificate

You can verify your connection with a CA certificate file if needed.

Before you start, ensure you have the following:

  * The CA certificate file
  * The latest McAfee ePO integration version



To configure the integration with a CA certificate, complete the following steps:

  1. Parse your CA certificate file into a Base64 String.
  2. Open the integration configuration parameters page.
  3. Insert the string in the **CA Certificate File** field.
  4. To test that the integration is successfully configured, select the **Verify SSL** checkbox and click **Test**.



For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the instance.  
Server address | String | https://<ServerAddress>:8443/remote/ | Yes | Server Address of the Trellix ePO. Example: https://127.0.0.1:8443/remote/  
Username | String | N/A | Yes | The user name for server authentication.  
Password | Password | N/A | Yes | The password for server authentication.  
Group Name | String | N/A | No | Name of the group.  
CA Certificate File - parsed into Base64 String | String | N/A | No | N/A  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add Tag

#### Description

Add a tag to an endpoint in Trellix ePO. Note: you can only apply tags that exist in the system. Supported entities: Hostname, IP.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Tag Name | String | N/A | Yes | Specify the name of the tag that needs to be added to the endpoints.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If success for one (is_success=true):_ Successfully added tag "{tag name}" to the following endpoints in Trellix ePO: {entity.identifier}_If tag is already a part of the endpoint: (is_success=true):_ Tag "{tag}" was already a part of the following endpoints in Trellix ePO: {entity.identifier}_If not success for one (is_success=true)_ Action wasn't able to add tag "{tag name}" to the following endpoints in Trellix ePO: {entity.identifier}_If not success for all (is_success=false):_ Tag "{tag} wasn't added to the provided endpoints."_if critical error (fail):_ Error executing action "Add Tag". Reason: {traceback}_If invalid tag (fail)_ Error executing action "Add Tag", Reason: tag "{tag name}" wasn't found in Trellix ePO. | General  
  
### Compare Server and Agent DAT

#### Description

Retrieve server and agent DAT information from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Alert.DstPort | Returns if it exists in JSON result  
Rule.msg | Returns if it exists in JSON result  
Alert.IPSIDAlertID | Returns if it exists in JSON result  
Alert.SrcIP | Returns if it exists in JSON result  
Alert.LastTime | Returns if it exists in JSON result  
Alert.Protocol | Returns if it exists in JSON result  
Alert.SrcPort | Returns if it exists in JSON result  
Alert.DstIP | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
##### JSON Result
    
    
    {
    
    "server_version": {server_version}
    
    "dat_version": {dat_version}
    
    "equal": true → if server_version == dat_version, else false
    
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved server and agent DAT information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve server and agent DAT information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about server and agent DAT was found on the provided endpoints._if critical error (fail):_ Error executing action "Compare Server and Agent DAT". Reason: {traceback} | General  
  
### Get Agent Information

#### Description

Retrieve information about endpoint's agents from Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
EPO_LastUpdate | Returns if it exists in JSON result  
EPO_ManagedState | Returns if it exists in JSON result  
EPO_Tags | Returns if it exists in JSON result  
EPO_ExcludedTags | Returns if it exists in JSON result  
EPO_AgentVersion | Returns if it exists in JSON result  
EPO_AgentGUID | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
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
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If success for one (is_success=true):_ Successfully retrieved agent information about the following endpoints in Trellix ePO: {entity.identifier}_If not success for one (is_success=true)_ Action wasn't able to retrieve agent information about the following endpoints in Trellix ePO: {entity.identifier}_If not success for all (is_success=false):_ No agend information was found for the provided hosts._if critical error (fail):_ Error executing action "Get Agent Information". Reason: {traceback} | General  
  
### Get Dat Version

#### Description

Retrieve DAT information from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Dat Version | N/A | N/A  
  
##### JSON Result
    
    
    {
    "DAT_version": {DAT version}
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved DAT information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve DAT information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about DAT was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Dat Version". Reason: {traceback} | General  
  
### Get Events for Hash

#### Description

Retrieve information about events related to hashes. Note: only MD5 hashes are supported.

#### Parameters

**Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Fetch Events From EPExtendedEvent Table | Checkbox | Unchecked | No | If enabled, action also will use "EPExtendedEvent" Table to find information about hashes.  
Mark As Suspicious | Checkbox | Yes | False | If enabled, action will mark all of the hashes for which events were found as suspicious.  
Create Insight | Checkbox | No | False | If enabled, action will create an insight containing information about which hashes have events associated with them.  
Fields To Return | CSV | EPOEvents.ThreatName,  
EPOEvents.ThreatType,  
EPOEvents.ThreatActionTaken,  
EPOEvents.ThreatHandled,  
EPOEvents.ThreatCategory  
,EPOEvents.TargetHostName,  
EPOEvents.TargetUserName,  
EPOEvents.TargetFileName,  
EPOEvents.TargetProcessName,  
EPOEvents.TargetPort,EPOEvents.  
TargetProtocol,EPOEvents.  
ThreatCategory,EPOEvents.  
TargetIPV4,EPOEvents.  
SourceHostName,EPOEvents.  
SourceIPV4,EPOEvents.  
SourceUserName,EPOEvents.  
SourceProcessName,EPOEvents.  
SourceURL | False | Specify what fields to return. If nothing is specified action will return all available fields.  
Sort Field | String | N/A | False | Specify what field should be used for ordering of the results.  
Sort Order | DDL | ASCPossible Values:ASCDESC | False | Specify what sort order should be applied to the query.  
Time Frame | DDL | Last HourPossible Values:Last HourLast 6 HoursLast 24 HoursLast WeekLast MonthCustom | False | Specify a time frame for the events. If "Custom" is selected, you also need to provide "Start Time".  
Start Time | String | N/A | False | Specify the start time for the events. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | False | Specify the end time for the events. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.  
Max Events To Return | Integer | 50 | False | Specify how many events to return. Default: 50.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
EPOEvents.ThreatCategory | Returns if it exists in JSON result  
EPOEvents.TargetUserName | Returns if it exists in JSON result  
EPOEvents.TargetPort | Returns if it exists in JSON result  
EPOEvents.TargetFileName | Returns if it exists in JSON result  
EPOEvents.TargetIPV4 | Returns if it exists in JSON result  
EPO_AgentGUID | Returns if it exists in JSON result  
  
##### Insights

Insight will be created for events that are found at Trellix ePO for current hash.

##### JSON Result
    
    
    [
        {
            "EntityResult":
            [
                {
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
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If successful and results are available: (is_success=true)_ "Successfully returned available events for the following hashes in Trellix ePO: {entity.identifier}"_If not successful for one: (is_success=true)_ "Action wasn't able to find events for the following hashes in Trellix ePO: {entity.identifier}"_If not successful for all (is_success=false):_ "No events were found for the provided endpoints in Trellix ePO."_if fatal error, like wrong credentials, no connection to server, other (fail):_ "Error executing action "Get Endpoint Threats". Reason: {0}''.format(error.Stacktrace)_If Error is in the response (fail):_ "Error executing action "Execute Entity Query". Reason: {0}''.format( response text)_if Start Time is empty, when "Time Frame" is "Custom" (fail):_ "Error executing action "Get Endpoint Threats". Reason: "Start Time" should be provided, when "Custom" is selected in "Time Frame" parameter." | General  
  
### Get Host IPs Status

#### Description

Retrieve IPS information from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_status_received | True/False | is_status_received:False  
  
##### JSON Result
    
    
    {
    "IPS_status": {IPS_status}
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved IPS information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve IPS information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about IPS was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Host IPS Status". Reason: {traceback} | General  
  
### Get Host Network IPs Status

#### Description

Retrieve Network IPS information from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_status_received | True/False | is_status_received:False  
  
##### JSON Result
    
    
    {
    "Network_IPS_status": {Network_IPS_status}
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved Network IPS information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve Network IPS information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about Network IPS was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Host Network IPS Status". Reason: {traceback} | General  
  
### Get Last Communication Time

#### Description

Retrieve information about the last communication time from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Use cases

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
    
    
    {
    "last_communication_time": {last_communication_time}
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved last communication time information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve last communication time information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about last communication time was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Last Communication Time". Reason: {traceback} | General  
  
### Get McAfee Epo Agent Version

#### Description

Retrieve information about agent version from the endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Use cases

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
    
    
    {
    "ePO_agent_version": ePO_agent_version
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved agent version information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve agent version information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about agent version was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Last Communication Time". Reason: {traceback} | General  
  
### Get System Information

#### Description

Return system information about the endpoints from Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Create Insight | Checkbox | Checkbox Checked |  | If enabled, action will create an insight containing information about the endpoint.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
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
ParentID | Returns if it exists in JSON result  
CPUType | Returns if it exists in JSON result  
  
##### Insights

N/A

##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "FreeDiskSpace": "444316",
                "UserName": "Admin",
                "OSServicePackVer": " ",
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
                "SubnetMask": " ",
                "IPAddress": "1.1.1.1",
                "DefaultLangID": "0409",
                "OSPlatform": "Server",
                "ComputerName": "MCAFEE-EPO",
                "OSOEMID": "00252-00112-26656-AA653",
                "NetAddress": "005056A56847",
                "TotalDiskSpace": "511646",
                "SubnetAddress": " ",
                "NumOfCPU": "4",
                "TimeZone": "Jerusalem Standard Time",
                "SystemDescription": "N/A",
                "Vdi": "0",
                "OSBuildNum": "9600",
                "OSVersion": "6.3",
                "IsPortable": "0",
                "TotalPhysicalMemory": "6441984000",
                "IPXAddress": "N/A",
                "UserProperty7": " ",
                "UserProperty6": " ",
                "UserProperty5": " ",
                "UserProperty4": " ",
                "UserProperty3": " ",
                "UserProperty2": " ",
                "UserProperty1": " ",
                "ParentID": "8",
                "CPUType": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz",
                "UserProperty8": " "
            },
            "Entity": "1.1.1.1"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If successful for one (is_success=true):_ Successfully retrieved system information about the following endpoints from Trellix ePO: {entity.identifier}_If not successful for one (is_success=true):_ Action wasn't able to retrieve system information about the following endpoints from Trellix ePO: {entity.identifier}_If not successful for all (is_success=false)_ No system information was found about the provided endpoints._If critical error:_ Error executing action "Get System Information". Reason: {error.traceback} | General  
  
### Get Virus Engine Agent Version

#### Description

Retrieve Virus Engine agent version information from the endpoints in McAfee ePO. Supported entities: Hostname, IP.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Virus Engine Agent Version | N/A | N/A  
  
##### JSON Result
    
    
    {
    "Virus_Engine_Agent_version": {Virus_engine_agent_version}
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if success for one_ Successfully retrieved Virus Engine agent version information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for one_ Action wasn't able to retrieve Virus Engine agent version information from the following endpoints in Trellix ePO: {entity.identifier}_if not success for all_ No information about Virus Engine agent version was found on the provided endpoints._if critical error (fail):_ Error executing action "Get Virus Engine Agent Version". Reason: {traceback} | General  
  
### Ping

#### Description

Test connectivity to Trellix ePO with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
null | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

### Remove Tag

#### Description

Remove a tag from an endpoint in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Tag Name | String | N/A | Yes | Specify the name of the tag that needs to be removed from the endpoints.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If success for one (is_success=true):_ Successfully removed tag "{tag name}" from the following endpoints in Trellix ePO: {entity.identifier}_If tag is not a part of the endpoint: (is_success=true):_ Tag "{tag}" wasn't a part of the following endpoints in Trellix ePO: {entity.identifier}_If not success for one (is_success=true)_ Action wasn't able to remove tag "{tag name}" from the following endpoints in Trellix ePO: {entity.identifier}_If not success for all (is_success=false):_ Tag "{tag} wasn't removed from the provided endpoints."_if critical error (fail):_ Error executing action "Remove Tag". Reason: {traceback}_If invalid tag (fail)_ Error executing action "Remove Tag", Reason: tag "{tag name}" wasn't found in Trellix ePO. | General  
  
### Run Full Scan

#### Description

Run full scan on the provided endpoints in Trellix ePO. Supported entities: Hostname, IP.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Task Name | String | On-Demand Scan - Full Scan | Yes | Specify what task should be executed in order to get a full scan.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
RunTask_Status | N/A | N/A  
  
##### JSON Result
    
    
    {
    "status": "success" or "failure"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If success for one:_ Successfully ran full scan based on the task "{task name}" on the following endpoints in Trellix ePO: {entity.identifier}_If not success for one:_ Action wasn't able to run full scan based on the task "{task name}" on the following endpoints in Trellix ePO: {entity.identifier}If not success for all:Full scan wasn't executed on the provided endpoints._if critical error (fail):_ Error executing action "Run Full Scan". Reason: {error traceback}_if task is not found (fail):_ Error executing action "Run Full Scan". Reason: Task "{task name}" wasn't found in Trellix ePO. Please check the spelling. | General  
  
### Update McAfee Agent

#### Description

Update McAfee Agent on the provided endpoints in Trellix ePO. Task for Windows: DAT_Update_Windows_CWS. Task for Linux: DAT_Update_Linux_CWS. Supported entities: Hostname, IP.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Task Name | String | DAT_Update_Windows_CWS | Yes | Specify what task should be executed in order to update the McAfee Agent. Default for Windows is DAT_Update_Windows_CWS. For Linux it's DAT_Update_Linux_CWS  
  
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
    
    
    {
    "status": "success" or "failure"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _If success for one:_ Successfully updated agents based on the task "{task name}" on the following endpoints in Trellix ePO: {entity.identifier}_If not success for one:_ Action wasn't able to update agent based on the task "{task name}" on the following endpoints in Trellix ePO: {entity.identifier}If not success for all:None of the agents were updated._if critical error (fail):_ Error executing action "Update McAfee Agent". Reason: {error traceback}_if task is not found (fail):_ Error executing action "Update McAfee Agent". Reason: Task "{task name}" wasn't found in Trellix ePO. Please check the spelling. | General  
  
## Connector

### McAfee EPO - Threats Connector

#### Description

Pull events from the EPOEvents table into Google SecOps. Whitelist works with Analyzer names.

#### Configure McAfee EPO - Threats Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | EPOEvents_ThreatType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | http://x.x.x.x:8443/remote/ | Yes | API root of the Trellix ePO instance.  
Username | String | N/A | Yes | Username of the Trellix ePO instance.  
Password | Password |  | Yes | Password of the Trellix ePO instance.  
Group Name | String |  | No | If provided, the connector will only fetch threats from endpoints that are a part of that group.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max Events To Fetch | Integer | 10 | No | How many events to process per one connector iteration. Default: 10.  
Lowest Severity To Fetch | String | Medium | No | Lowest severity of the events to fetch. By default, the connector will ingest all of the events. Possible Values: Info, Low, Medium, High, Critical.  
Use whitelist as a blacklist | Checkbox | Checked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix ePO server is valid.  
CA Certificate File | String | N/A | False | Base 64 encoded CA certificate file.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
