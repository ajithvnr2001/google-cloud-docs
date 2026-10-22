---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sccm/
title: SCCM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:31.517310+00:00
---

# SCCM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sccm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SCCM

**Important:** This integration refers to Microsoft Configuration Manager that is part of the Microsoft Intune family of products.

This document provides guidance on how to integrate SCCM with Google SecOps.

## Configure SCCM to work with Google Security Operations

### Connect SCCM to Linux

To run SCCM integration on the Centos server, first, install wmi:
    
    
    rpm -Uvh http://www6.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/wmi-1.3.14-4.el7.art.x86_64.rpm
    yum install wmi
    

After that, you can configure and use integration.

## Configure SCCM integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server Address | String | x.x.x.x | Yes | The IP address or DNS name of Microsoft SCCM server to connect to.  
Domain | String | domain | Yes | Microsoft SCCM server domain.  
Username | String | N/A | Yes | The username to use to connect to Microsoft SCCM.  
Password | Password | N/A | Yes | The password to use to connect to Microsoft SCCM.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Get Computer Properties

**Deprecated:** This action is deprecated. Use the "Enrich Entities" action instead.

#### Description

Get computer properties from Microsoft SCCM instance and use obtained information to enrich the provided Google SecOps Host entity.

#### Parameters

N/A

#### Use Cases

Get information about the host in the Google SecOps playbook from Microsoft SCCM and use this data for enrichment.

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
ClientEdition | Returns if it exists in JSON result  
SMSInstalledSites | Returns if it exists in JSON result  
MDMDeviceCategoryID | Returns if it exists in JSON result  
ManagementAuthority | Returns if it exists in JSON result  
IPAddresses | Returns if it exists in JSON result  
EASDeviceID | Returns if it exists in JSON result  
ResourceType | Returns if it exists in JSON result  
SID | Returns if it exists in JSON result  
DeviceOwner | Returns if it exists in JSON result  
IsWriteFilterCapable | Returns if it exists in JSON result  
HardwareID | Returns if it exists in JSON result  
IsMachineChangesPersisted | Returns if it exists in JSON result  
SMBIOSGUID | Returns if it exists in JSON result  
NetbiosName | Returns if it exists in JSON result  
Build | Returns if it exists in JSON result  
AgentSite | Returns if it exists in JSON result  
IPv6Addresses | Returns if it exists in JSON result  
ResourceNames | Returns if it exists in JSON result  
PrimaryGroupID | Returns if it exists in JSON result  
ClientVersion | Returns if it exists in JSON result  
ClientType | Returns if it exists in JSON result  
PreviousSMSUUID | Returns if it exists in JSON result  
ResourceId | Returns if it exists in JSON result  
IPv6Prefixes | Returns if it exists in JSON result  
ObjectGUID | Returns if it exists in JSON result  
SMSAssignedSites | Returns if it exists in JSON result  
SMSResidentSites | Returns if it exists in JSON result  
IsPortableOperatingSystem | Returns if it exists in JSON result  
MDMComplianceStatus | Returns if it exists in JSON result  
WTGUniqueKey | Returns if it exists in JSON result  
AMTStatus | Returns if it exists in JSON result  
SystemGroupName | Returns if it exists in JSON result  
AgentName | Returns if it exists in JSON result  
Active | Returns if it exists in JSON result  
SNMPCommunityName | Returns if it exists in JSON result  
ADSiteName | Returns if it exists in JSON result  
IsClientAMT30Compatible | Returns if it exists in JSON result  
IsVirtualMachine | Returns if it exists in JSON result  
AlwaysInternet | Returns if it exists in JSON result  
Decommissioned | Returns if it exists in JSON result  
Name | Returns if it exists in JSON result  
SystemOUName | Returns if it exists in JSON result  
SuppressAutoProvision | Returns if it exists in JSON result  
SMSUniqueIdentifier | Returns if it exists in JSON result  
ResourceDomainORWorkgroup | Returns if it exists in JSON result  
UserAccountControl | Returns if it exists in JSON result  
LastLogonTimestamp | Returns if it exists in JSON result  
AMTFullVersion | Returns if it exists in JSON result  
OperatingSystemNameandVersion | Returns if it exists in JSON result  
PublisherDeviceID | Returns if it exists in JSON result  
SystemContainerName | Returns if it exists in JSON result  
LastLogonUserName | Returns if it exists in JSON result  
InternetEnabled | Returns if it exists in JSON result  
SMSUUIDChangeDate | Returns if it exists in JSON result  
AgentTime | Returns if it exists in JSON result  
IsAssignedToUser | Returns if it exists in JSON result  
WipeStatus | Returns if it exists in JSON result  
SecurityGroupName | Returns if it exists in JSON result  
DistinguishedName | Returns if it exists in JSON result  
SystemRoles | Returns if it exists in JSON result  
Obsolete | Returns if it exists in JSON result  
SerialNumber | Returns if it exists in JSON result  
FullDomainName | Returns if it exists in JSON result  
IsAOACCapable | Returns if it exists in JSON result  
MACAddresses | Returns if it exists in JSON result  
IPSubnets | Returns if it exists in JSON result  
VirtualMachineType | Returns if it exists in JSON result  
CPUType | Returns if it exists in JSON result  
CreationDate | Returns if it exists in JSON result  
VirtualMachineHostName | Returns if it exists in JSON result  
OSBranch | Returns if it exists in JSON result  
LastLogonUserDomain | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_enriched | True/False | is_enriched:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "ClientEdition": "None",
                "SMSInstalledSites": "()",
                "MDMDeviceCategoryID": "None",
                "ManagementAuthority": "None",
                "IPAddresses": "(u'1.1.1.1', u'1.1.1.1')",
                "EASDeviceID": "None",
                "ResourceType": "5",
                "Unknown": "None",
                "SID": "S-1-5-21-2485274276-3947876705-1900992244-1487",
                "DeviceOwner": "None",
                "IsWriteFilterCapable": "None",
                "HardwareID": "None",
                "IsMachineChangesPersisted": "None",
                "SMBIOSGUID": "None",
                "NetbiosName": "PC_01",
                "Build": "None",
                "AgentSite": "(u'001',)",
                "IPv6Addresses": "()",
                "Client": "None",
                "ResourceNames": "(u'PC-01.DOMAIN.COM',)",
                "PrimaryGroupID": "515",
                "ClientVersion": "None",
                "ClientType": "None",
                "PreviousSMSUUID": "None",
                "ResourceId": "2097152157",
                "IPv6Prefixes": "()",
                "ObjectGUID": "(189, 112, 106, 52, 65, 87, 150, 71, 166, 96, 209, 16, 161, 133, 38, 242)",
                "SMSAssignedSites": "(u'001',)",
                "SMSResidentSites": "(u'001',)",
                "IsPortableOperatingSystem": "None",
                "MDMComplianceStatus": "None",
                "WTGUniqueKey": "None",
                "AMTStatus": "None",
                "SystemGroupName": "()",
                "AgentName": "(u'SMS_AD_SYSTEM_DISCOVERY_AGENT',)",
                "Active": "None",
                "SNMPCommunityName": "None",
                "ADSiteName": "Default-First-Site-Name",
                "IsClientAMT30Compatible": "None",
                "IsVirtualMachine": "None",
                "AlwaysInternet": "None",
                "Decommissioned": "0",
                "Name": "PC-01",
                "SystemOUName": "()",
                "SuppressAutoProvision": "None",
                "SMSUniqueIdentifier": "None",
                "ResourceDomainORWorkgroup": "DOMAIN",
                "UserAccountControl": "4096",
                "LastLogonTimestamp": "20190203084427.000000+***",
                "AMTFullVersion": "None",
                "OperatingSystemNameandVersion": "Microsoft Windows NT Workstation 10.0", "PublisherDeviceID": "None",
                "SystemContainerName": "(u'DOMAIN\\\\\\\\COMPUTERS',)",
                "LastLogonUserName": "None",
                "InternetEnabled": "None",
                "SMSUUIDChangeDate": "None",
                "AgentTime": "(u'20190207115148.000000+***',)",
                "IsAssignedToUser": "None",
                "WipeStatus": "None",
                "SecurityGroupName": "()",
                "SystemRoles": "()",
                "DistinguishedName": "CN=PC-01,CN=Computers,DC=DOMAIN,DC=COM",
                "Obsolete": "None",
                "SerialNumber": "None",
                "FullDomainName": "DOMAIN.COM",
                "IsAOACCapable": "None",
                "MACAddresses": "()",
                "IPSubnets": "()",
                "VirtualMachineType": "None",
                "CPUType": "None",
                "CreationDate": "20190128134818.000000+***",
                "VirtualMachineHostName": "None",
                "OSBranch": "None",
                "LastLogonUserDomain": "None"
            },
            "Entity": "PC_01"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If some or all of the provided entities were enriched:_ print "Following entities were enriched with SCCM data:\n {0}".format([entity list])___If some of the provided entities were not enriched:_ print "SCCM data for the following entities was not found:\n {0}".format([entity list])_If all of the provided entities were not enriched:_ print "No entities were enriched"**Action should fail and stop playbook execution:**_If critical error, like wrong credentials or network connectivity issues:_ print "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
Table | **Table name:** Microsoft SCCM query results for {0}.entity.Identifier**Table content:** content is dynamic, based on query results. | Entity  
  
### Get Login History

#### Description

Retrieve user login history from Microsoft SCCM instance based on the provided Google SecOps user entity.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Number of Records to Return | Integer | 100 | Yes | Maximum number of records to return in the action.  
  
#### Use Cases

Get user login info from SCCM in the playbook.

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Username | Returns if it exists in JSON result  
LoginCount | Returns if it exists in JSON result  
LastLoggedIn | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": [
                {
                    "Username": "pc-01\\\\local_users",
                    "LoginCount": 22,
                    "LastLoggedIn": "20170815103710.000000+***"
                }
            ],
            "Entity": "pc-01"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If got data for some or all of the provided entities:_ print "Found SCCM information on the following entities;:\n {0}".format([entity list])___If some of the provided entities were not found in SCCM:_ print "SCCM data for the following entities was not found:\n {0}".format([entity list])_If fail to find data for all of the provided entities:_ print "No results were found."**Action should fail and stop playbook execution:**_If critical error, like wrong credentials or network connectivity issues:_ print "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
Table | **Table name:** Microsoft SCCM login history for {0}.format(entity.Identifier)**Table content:** content is dynamic, based on query results. | Entity  
  
### Enrich Entities

#### Description

Enrich Google SecOps Host, IP or User entities based on the information from the Microsoft SCCM.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * User
  * Host
  * IP Address



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Example return for Host entity, the request was made in Powershell:
    
    
        __GENUS                       : 2
        __CLASS                       : SMS_R_System
        __SUPERCLASS                  : SMS_Resource
        __DYNASTY                     : SMS_BaseClass
        __RELPATH                     : SMS_R_System.ResourceId=16777219
        __PROPERTY_COUNT              : 77
        __DERIVATION                  : {SMS_Resource, SMS_BaseClass}
        __SERVER                      : SCCM-SCCM
        __NAMESPACE                   : ROOT\SMS\site_SCM
        __PATH                        : \\SCCM-SCCM\ROOT\SMS\site_SCM:SMS_R_System.ResourceId=16777219
        AADDeviceID                   : 00000000-0000-0000-0000-000000000000
        AADTenantID                   : 00000000-0000-0000-0000-000000000000
        Active                        : 1
        ADSiteName                    : Default-First-Site-Name
        AgentName                     : {SMS_AD_SYSTEM_DISCOVERY_AGENT, SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT, MP_ClientRegistration, Heartbeat Discovery}
        AgentSite                     : {SCM, SCM, SCM, SCM}
        AgentTime                     : {20200730230502.000000+***, 20200415051330.000000+***, 20200415055902.000000+***, 20200730231034.000000+***}
        AlwaysInternet                : 0
        AMTFullVersion                :
        AMTStatus                     :
        Build                         : 10.0.18363
        BuildExt                      : 10.0.18363.900
        Client                        : 1
        ClientEdition                 : 0
        ClientType                    : 1
        ClientVersion                 : 5.00.8790.1007
        CPUType                       : Intel64 Family 6 Model 63 Stepping 2
        CreationDate                  : 20200415121334.000000+***
        Decommissioned                : 0
        DeviceOwner                   : 1
        DistinguishedName             : CN=SCCM-W10,OU=Workstations,OU=SCCM,DC=sccm-lab,DC=local
        EASDeviceID                   :
        FullDomainName                : SCCM-LAB.LOCAL
        HardwareID                    : 2:39AC2A8E6794B559B4F8D5677EFE804D834DE6FF
        InternetEnabled               : 0
        IPAddresses                   : {172.30.202.92, fe80::4cca:c991:272d:24c3}
        IPSubnets                     : {172.30.202.0}
        IPv6Addresses                 : {}
        IPv6Prefixes                  : {}
        IsAOACCapable                 : False
        IsAssignedToUser              : False
        IsClientAMT30Compatible       :
        IsMachineChangesPersisted     : True
        IsPortableOperatingSystem     : False
        IsVirtualMachine              : True
        IsWriteFilterCapable          : False
        LastLogonTimestamp            : 20200731060204.000000+***
        LastLogonUserDomain           : SCCM-LAB
        LastLogonUserName             : Administrator
        MACAddresses                  : {00:50:56:A2:D7:A8}
        ManagementAuthority           : 0
        MDMComplianceStatus           :
        MDMDeviceCategoryID           :
        Name                          : SCCM-W10
        NetbiosName                   : SCCM-W10
        ObjectGUID                    : {230, 152, 150, 13...}
        Obsolete                      : 0
        OperatingSystemNameandVersion : Microsoft Windows NT Workstation 10.0
        OSBranch                      : 0
        PreviousSMSUUID               : Unknown
        PrimaryGroupID                : 515
        PublisherDeviceID             :
        ResourceDomainORWorkgroup     : SCCM-LAB
        ResourceId                    : 16777219
        ResourceNames                 : {SCCM-W10.sccm-lab.local}
        ResourceType                  : 5
        SecurityGroupName             : {SCCM-LAB\Domain Computers}
        SerialNumber                  :
        SID                           : S-1-5-21-3004247314-75612377-2250890222-1104
        SMBIOSGUID                    : 8ABD2242-1FEF-CCCE-12F5-77021D40BE0E
        SMSAssignedSites              : {SCM}
        SMSInstalledSites             : {SCM}
        SMSResidentSites              : {SCM}
        SMSUniqueIdentifier           : GUID:778CB685-B19A-40CD-9257-E9883A0E4AD3
        SMSUUIDChangeDate             : 20200701090912.000000+***
        SNMPCommunityName             :
        SuppressAutoProvision         :
        SystemContainerName           : {}
        SystemGroupName               : {SCCM-LAB\Domain Computers}
        SystemOUName                  : {SCCM-LAB.LOCAL/SCCM, SCCM-LAB.LOCAL/SCCM/WORKSTATIONS}
        SystemRoles                   : {}
        Unknown                       :
        UserAccountControl            : 4096
        VirtualMachineHostName        :
        VirtualMachineType            : 0
        WipeStatus                    :
        WTGUniqueKey                  :
        PSComputerName                : SCCM-SCCM
    
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:** _If some or all of the provided entities were enriched:_ "Following entities were enriched with SCCM data:\n {0}".format([entity list]) _If some of the provided entities were not enriched:_ "SCCM data for the following entities were not found:\n {0}".format([entity list]) _If all of the provided entities were not enriched:_ "No entities were enriched" **Action should fail and stop playbook execution:** _If critical error, like wrong credentials or network connectivity issues:_ "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
Table | **Table name:** Microsoft SCCM enrichment results for {0}.format(entity.Identifier) **Table content:** content is dynamic, based on query results. | Entity  
  
### Run WQL Query

#### Description

Run arbitrary Windows Management Instrumentation Query Language (WQL) query against Microsoft SCCM Instance.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query to run | String | SELECT UniqueUserName,LastLoginTime,LoginCount,ResourceName from SMS_UserMachineIntelligence JOIN SMS_R_User ON SMS_UserMachineIntelligence.UniqueUserName = SMS_R_User.UniqueUserName WHERE SMS_R_User.UserPrincipalName = "sccm_user@sccm-domain.com" | Yes | Specify WQL query to run. Consider the default example request for reference.  
Number of records to return | Integer | 100 | Yes | Maximum number of records to return in action.  
  
#### Use Cases

Run arbitrary queries against Microsoft SCCM instances to get needed data based on alert analysis in Google SecOps.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Example return for Host entity, the request was made in Powershell:
    
    
        __GENUS                       : 2
        __CLASS                       : SMS_R_System
        __SUPERCLASS                  : SMS_Resource
        __DYNASTY                     : SMS_BaseClass
        __RELPATH                     : SMS_R_System.ResourceId=16777219
        __PROPERTY_COUNT              : 77
        __DERIVATION                  : {SMS_Resource, SMS_BaseClass}
        __SERVER                      : SCCM-SCCM
        __NAMESPACE                   : ROOT\SMS\site_SCM
        __PATH                        : \\SCCM-SCCM\ROOT\SMS\site_SCM:SMS_R_System.ResourceId=16777219
        AADDeviceID                   : 00000000-0000-0000-0000-000000000000
        AADTenantID                   : 00000000-0000-0000-0000-000000000000
        Active                        : 1
        ADSiteName                    : Default-First-Site-Name
        AgentName                     : {SMS_AD_SYSTEM_DISCOVERY_AGENT, SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT, MP_ClientRegistration, Heartbeat Discovery}
        AgentSite                     : {SCM, SCM, SCM, SCM}
        AgentTime                     : {20200730230502.000000+***, 20200415051330.000000+***, 20200415055902.000000+***, 20200730231034.000000+***}
        AlwaysInternet                : 0
        AMTFullVersion                :
        AMTStatus                     :
        Build                         : 10.0.18363
        BuildExt                      : 10.0.18363.900
        Client                        : 1
        ClientEdition                 : 0
        ClientType                    : 1
        ClientVersion                 : 5.00.8790.1007
        CPUType                       : Intel64 Family 6 Model 63 Stepping 2
        CreationDate                  : 20200415121334.000000+***
        Decommissioned                : 0
        DeviceOwner                   : 1
        DistinguishedName             : CN=SCCM-W10,OU=Workstations,OU=SCCM,DC=sccm-lab,DC=local
        EASDeviceID                   :
        FullDomainName                : SCCM-LAB.LOCAL
        HardwareID                    : 2:39AC2A8E6794B559B4F8D5677EFE804D834DE6FF
        InternetEnabled               : 0
        IPAddresses                   : {172.30.202.92, fe80::4cca:c991:272d:24c3}
        IPSubnets                     : {172.30.202.0}
        IPv6Addresses                 : {}
        IPv6Prefixes                  : {}
        IsAOACCapable                 : False
        IsAssignedToUser              : False
        IsClientAMT30Compatible       :
        IsMachineChangesPersisted     : True
        IsPortableOperatingSystem     : False
        IsVirtualMachine              : True
        IsWriteFilterCapable          : False
        LastLogonTimestamp            : 20200731060204.000000+***
        LastLogonUserDomain           : SCCM-LAB
        LastLogonUserName             : Administrator
        MACAddresses                  : {00:50:56:A2:D7:A8}
        ManagementAuthority           : 0
        MDMComplianceStatus           :
        MDMDeviceCategoryID           :
        Name                          : SCCM-W10
        NetbiosName                   : SCCM-W10
        ObjectGUID                    : {230, 152, 150, 13...}
        Obsolete                      : 0
        OperatingSystemNameandVersion : Microsoft Windows NT Workstation 10.0
        OSBranch                      : 0
        PreviousSMSUUID               : Unknown
        PrimaryGroupID                : 515
        PublisherDeviceID             :
        ResourceDomainORWorkgroup     : SCCM-LAB
        ResourceId                    : 16777219
        ResourceNames                 : {SCCM-W10.sccm-lab.local}
        ResourceType                  : 5
        SecurityGroupName             : {SCCM-LAB\Domain Computers}
        SerialNumber                  :
        SID                           : S-1-5-21-3004247314-75612377-2250890222-1104
        SMBIOSGUID                    : 8ABD2242-1FEF-CCCE-12F5-77021D40BE0E
        SMSAssignedSites              : {SCM}
        SMSInstalledSites             : {SCM}
        SMSResidentSites              : {SCM}
        SMSUniqueIdentifier           : GUID:778CB685-B19A-40CD-9257-E9883A0E4AD3
        SMSUUIDChangeDate             : 20200701090912.000000+***
        SNMPCommunityName             :
        SuppressAutoProvision         :
        SystemContainerName           : {}
        SystemGroupName               : {SCCM-LAB\Domain Computers}
        SystemOUName                  : {SCCM-LAB.LOCAL/SCCM, SCCM-LAB.LOCAL/SCCM/WORKSTATIONS}
        SystemRoles                   : {}
        Unknown                       :
        UserAccountControl            : 4096
        VirtualMachineHostName        :
        VirtualMachineType            : 0
        WipeStatus                    :
        WTGUniqueKey                  :
        PSComputerName                : SCCM-SCCM
    
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If query is successful and got data:_ print "Query executed successfully and returned results"._If nothing found:_ print "Query executed successfully, but did not return any results."._If error:_ print "Query didn't complete due to error: {0}".format(exception.stacktrace)._If query results were truncated:_ print "Query results exceeded limits and were truncated!".**Action should fail and stop playbook execution:**_If critical error, like wrong credentials or network connectivity issues:_ print "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
Table | **Table name:** WQL Query results**Columns:** dynamically generate columns based on the query results | General  
Attachments | Run_WQL_query_response.json - contains returned by the action technical JSON data. | General  
JSON Viewer | Show the JSON viewer for the query result. | General  
  
### Create Scan Endpoint Task

#### Description

Create a scan endpoint task on Microsoft SCCM server for endpoint. Two types of scans are available - Full or Quick. The action works with either Host or IP Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scan Type | DDL | Quick Scan | Yes | Specify whether to run Full scan or Quick scan.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message\\* | **Action should not fail and not stop playbook execution:** _If task was created successfully for some or all of the provided entities:_ "Scan endpoint task was created for the following entities:\n {0}".format([entity list]) _If failed to create scan endpoint task for some of the provided entities were not enriched:_ "Failed to create scan endpoint task for the following entities:\n {0}".format([entity list]) _If fail to create a task for all of the provided entities:_ "Endpoint scan tasks were not created, check the action log for details" **Action should fail and stop playbook execution:** _If critical error, like wrong credentials or network connectivity issues:_ "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
  
### Ping

#### Description

Test connectivity to Microsoft SCCM instance with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use Cases

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and can be executed as manual action, which is not a part of playbooks.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
#### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:** _If successful:_ "Successfully connected to the Microsoft SCCM instance with the provided connection parameters!". **Action should fail and stop playbook execution:** _If not successful:_ "Failed to connect to the Microsoft SCCM instance! Error is {0}".format(exception.stacktrace). | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
