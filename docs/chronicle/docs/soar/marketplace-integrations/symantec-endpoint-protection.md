---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-protection/
title: Symantec Endpoint Protection \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:22.863819+00:00
---

# Symantec Endpoint Protection  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/symantec-endpoint-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Symantec Endpoint Protection

This document provides guidance on how to integrate Symantec Endpoint Protection with Google SecOps.

## Configure Symantec Endpoint Protection integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Assistance  
---|---|---|---|---  
Username | String | N/A | Yes | Username to use in integration.  
Password | Password | N/A | Yes | Password to use in integration.  
Domain | String | N/A | Yes | **To find the domain:**

  1. In the console, click **Admin**.
  2. On the **Admin** page, click **Domains.**

  
API Root | String | N/A | Yes | For example: https://SEPM_IP:8446  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Symantec Endpoint Protection server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Block Hash

#### Description

Blocks a particular hash on endpoints.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Block List name | String | N/A | The black list name to add the hash to.  
  
#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Disable Download Insight

#### Description

Disable download insight on endpoints.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Time Period | String | N/A | N/A  
  
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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Disable NTP

#### Description

Disable NTP on endpoints.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Time Period | String | 5 | N/A  
  
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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Enable Download Insight

#### Description

Enable download insight on endpoints.

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

N/A ##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Enable NTP

#### Description

Enable NTP on endpoints.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Get Report

#### Description

Get a command status report.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Command IDS | String | 7E975C32C71349E9BE495EC2220B902F | N/A  
  
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
reports | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "computerName": "HOST_1",
        "subStateId": 0,
        "hardwareKey": "36817A7B13C3A6317932AD9819097123",
        "computerId": "9C9850840A0000BD3566F8ECC8417123",
        "domainName": "Default",
        "stateId": 0,
        "computerIp": "1.1.1.1",
        "currentLoginUserName": "admin"
      },
      {
        "computerName": "HOST_2",
        "subStateId": 0,
        "hardwareKey": "36817A7B13C3A6317932AD9819097123",
        "computerId": "9C9850840A0000BD3566F8ECC8417123",
        "domainName": "Default",
        "stateId": 0,
        "computerIp": "1.1.1.1",
        "currentLoginUserName": "admin"
      }
    ]
    

### Get Report and Enrich

#### Description

Get a command status report and enrich entities.

#### Parameters

**Parameter** | **Type** | Default Value | Description  
---|---|---|---  
Command IDS | String | 7E975C32C71349E9BE495EC2220B902F | N/A  
  
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
reports | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "computerName": "HOST_3",
        "subStateId": 0,
        "hardwareKey": "36817A7B13C3A6317932AD9819097123",
        "computerId": "9C9850840A0000BD3566F8ECC8417123",
        "domainName": "Default",
        "stateId": 0,
        "computerIp": "1.1.1.1",
        "currentLoginUserName": "admin"
      },
      {
        "computerName": "HOST_4",
        "subStateId": 0,
        "hardwareKey": "36817A7B13C3A6317932AD9819097123",
        "computerId": "9C9850840A0000BD3566F8ECC8417123",
        "domainName": "Default",
        "stateId": 0,
        "computerIp": "1.1.1.1",
        "currentLoginUserName": "admin"
      }
    ]
    

### Get System Info

#### Description

Get system information for endpoints.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This cation runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
profileVersion | Returns if it exists in JSON result  
elamOnOff | Returns if it exists in JSON result  
avEngineOnOff | Returns if it exists in JSON result  
majorVersion | Returns if it exists in JSON result  
profileChecksum | Returns if it exists in JSON result  
atpDeviceId | Returns if it exists in JSON result  
processorType | Returns if it exists in JSON result  
oslanguage | Returns if it exists in JSON result  
licenseId | Returns if it exists in JSON result  
licenseStatus | Returns if it exists in JSON result  
group | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
uuid | Returns if it exists in JSON result  
groupUpdateProvider | Returns if it exists in JSON result  
edrStatus | Returns if it exists in JSON result  
freeDisk | Returns if it exists in JSON result  
snacicenseId | Returns if it exists in JSON result  
diskDrive | Returns if it exists in JSON result  
osFunction | Returns if it exists in JSON result  
cidsDrvMulfCode | Returns if it exists in JSON result  
mobilePhone | Returns if it exists in JSON result  
jobTitle | Returns if it exists in JSON result  
lastHeuristicThreatTime | Returns if it exists in JSON result  
osname | Returns if it exists in JSON result  
winServers | Returns if it exists in JSON result  
idsSerialNo | Returns if it exists in JSON result  
employeeNumber | Returns if it exists in JSON result  
lastSiteId | Returns if it exists in JSON result  
uwf | Returns if it exists in JSON result  
currentClientId | Returns if it exists in JSON result  
osbitness | Returns if it exists in JSON result  
osanguage | Returns if it exists in JSON result  
lastScanTime | Returns if it exists in JSON result  
dnsServers | Returns if it exists in JSON result  
securityVirtualAppliance | Returns if it exists in JSON result  
worstInfectionIdx | Returns if it exists in JSON result  
encryptedDevicePassword | Returns if it exists in JSON result  
ptpOnOff | Returns if it exists in JSON result  
kernel | Returns if it exists in JSON result  
svaId | Returns if it exists in JSON result  
lastConnectedIpAddr | Returns if it exists in JSON result  
agentVersion | Returns if it exists in JSON result  
ipAddresses | Returns if it exists in JSON result  
agentTimeStamp | Returns if it exists in JSON result  
osfunction | Returns if it exists in JSON result  
osMajor | Returns if it exists in JSON result  
deploymentTargetVersion | Returns if it exists in JSON result  
osMinor | Returns if it exists in JSON result  
****  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### List Endpoints

#### Description

List all the endpoints/sensors configured on a particular device.

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
endpoints | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "EntityResult": {
          "profileVersion": "14.0.1904",
          "elamOnOff": 1,
          "avEngineOnOff": 1,
          "majorVersion": 14,
          "profileChecksum": "None",
          "atpDeviceId": "",
          "processorType": "Intel64 Family 6 Model 78 Stepping 3",
          "oslanguage": "None",
          "licenseId": "",
          "licenseStatus": -1,
          "group": {
            "domain": {
              "id": "163240A90A0000BD1BAAF73394A403B0",
              "name": "Default"
            },
            "fullPathName": "None",
            "id": "201DB33F0A0000BD587D90FA64799744",
            "name": "My Company\\\\Default Group"
          },
          "uuid": "4C4C4544-0047-5310-8054-B9C04F504632",
          "groupUpdateProvider": "",
          "edrStatus": 0,
          "freeDisk": 10328551424,
          "snacicenseId": "",
          "diskDrive": "C:\\\\",
          "osFunction": "Workstation",
          "cidsDrvMulfCode": 0,
          "mobilePhone": "",
          "jobTitle": "",
          "lastHeuristicThreatTime": 0,
          "osname": "Windows 10",
          "winServers": [
            "0.0.0.0",
            "0.0.0.0"
          ],
          "deploymentMessage": "",
          "idsSerialNo": "",
          "employeeNumber": "",
          "lastSiteId": "C485F8390A0000BD0F806737FA94B6EF",
          "uwf": 2,
          "currentClientId": "D630A2D10A0000BD3566F8EC3AF38258",
          "osbitness": "x64",
          "osanguage": "None",
          "lastScanTime": 1549277509000,
          "dnsServers": [
            "10.0.0.190",
            "..."
          ],
          "securityVirtualAppliance": "None",
          "worstInfectionIdx": "0",
          "encryptedDevicePassword": "",
          "ptpOnOff": 1,
          "kernel": "None",
          "svaId": "",
          "lastConnectedIpAddr": "1.1.1.1",
          "agentVersion": "14.0.1904.0000",
          "ipAddresses": [
            "10.0.0.40",
            "192.168.56.1",
            "192.168.184.1"
          ],
          "agentTimeStamp": 1549287166434,
          "osfunction": "Workstation",
          "osMajor": 10,
          "deploymentTargetVersion": "14.0.1904.0000",
          "osMinor": 0,
          "osFlavorNumber": 126,
          "logicalCpus": 0,
          "deploymentPreVersion": "",
          "hypervisorVendorId": "0",
          "fbwf": 2,
          "osversion": "10.0",
          "email": "",
          "vsicStatus": 3,
          "lastServerId": "5B0090390A0000BD0EA208CFABAB79BF",
          "deleted": 0,
          "deploymentStatus": "302449921",
          "computerTimeStamp": 1549270030452,
          "bwf": 2,
          "totalDiskSpace": 121601,
          "homePhone": "",
          "daOnOff": 1,
          "computerDescription": "P-VICTORS",
          "pepOnOff": 1,
          "bashStatus": 1,
          "agentUsn": 4634006,
          "osName": "Windows 10",
          "patternIdx": "12D025D1F97B4681135C679CFB528DC0",
          "employeeStatus": "",
          "timeZone": -120,
          "rebootRequired": 0,
          "subnetMasks": [
            "255.255.254.0",
            "255.255.255.0",
            "255.255.255.0"
          ],
          "minorVersion": 0,
          "osservicePack": "",
          "lastSiteName": "testSite",
          "cidsEngineVersion": "1.1.1.1",
          "lastDeploymentTime": 1549269576000,
          "isGrace": 0,
          "computerUsn": 4628006,
          "agentId": "AA2625F10A0000BD3566F8EC8ADC3D2A",
          "cidsBrowserFfOnOff": 1,
          "domainOrWorkgroup": "SIEMPIFY.OCA",
          "lastUpdateTime": 1549287166434,
          "loginDomain": "SIEMPIFY.OCA",
          "lastServerName": "surajsep",
          "contentUpdate": 1,
          "writeFiltersStatus": "None",
          "infected": 0,
          "memory": 16827695104,
          "osminor": 0,
          "freeMem": 9575374848,
          "officePhone": "",
          "lastVirusTime": 1530785567000,
          "idsVersion": "",
          "cidsBrowserIeOnOff": 1,
          "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQBt1Cn6nstqwypo5vUwmPVs+Ebx0JltYQJCHqfuWRhyUqnTyRniQZRCOY92MS2fMS6vouWJx+DMqlu8vbIs3G4nFoSxXAXuPXaafpWObEUhsXrN4Gxt/Rwoi8uOXjODW4kt9FKw9xoVHMquSF/jhobMrcozXTtUf5QRTQoGheRSIOPN+JfjEuT1XAbt2uS+IbX3Sp648yyl94/XI7ZUGHaviq3eaYjK+FMN3S2Uv/i/3uxB+/gOHDHfOsn6wES6HEhN9jzrM3arlZlWXc7783SzUfq8uAZ13cWOPb8BnUKaY2A1r+Ca95dJatvo7pg1flmX4TGT72UOVM7kzI029",
          "quarantineDesc": "Host Integrity check passed   Requirement: ",
          "biosVersion": "DE   - 1072009 BIOS Date: 08/26/16 02:41:50 Ver: 1.1.1.1",
          "processorClock": 2808,
          "rebootReason": "",
          "cidsSilentMode": 0,
          "creationTime": 1530429396647,
          "macAddresses": [
            "18-DB-F2-46-23-C0",
            "0A-00-27-00-00-15",
            "00-50-56-C0-00-01"
          ],
          "idsChecksum": "None",
          "operatingSystem": "Windows 10 Enterprise 2015 TSB",
          "osmajor": 10,
          "virtualizationPlatform": "Unknown",
          "deploymentRunningVersion": "14.0.1904.0000",
          "physicalCpus": 4,
          "osBitness": "x64",
          "cidsDefsetVersion": "190201061",
          "cidsDrvOnOff": 1,
          "computerName": "P-NOYS",
          "logonUserName": "johndoe1",
          "atpServer": "",
          "gateways": [
            "10.0.0.138",
            "0.0.0.0",
            "0.0.0.0"
          ],
          "uniqueId": "9C9850840A0000BD3566F8ECC8417F64",
          "department": "",
          "isNpvdiClient": 0,
          "dhcpServer": "1.1.1.1",
          "description": "None",
          "osflavorNumber": 126,
          "tpmDevice": "0",
          "onlineStatus": 1,
          "lastDownloadTime": 1549150265991,
          "apOnOff": 1,
          "fullName": "",
          "osVersion": "10.0",
          "tmpDevice": "None",
          "attributeExtension": "",
          "licenseExpiry": 0,
          "tamperOnOff": 1,
          "osServicePack": "",
          "agentType": "105",
          "serialNumber": "9GSTPF2",
          "osElamStatus": 0,
          "installType": "0",
          "profileSerialNo": "201D-10/29/2018 21:39:09 743",
          "hardwareKey": "36817A7B13C3A6317932AD9819097322",
          "firewallOnOff": 1
        },
        "Entity": "HOST_1"
      },
      {
        "EntityResult": {
          "profileVersion": "14.0.1904",
          "elamOnOff": 1,
          "avEngineOnOff": 1,
          "majorVersion": 14,
          "profileChecksum": "None",
          "atpDeviceId": "",
          "processorType": "Intel64 Family 6 Model 78 Stepping 3",
          "oslanguage": "None",
          "licenseId": "",
          "licenseStatus": -1,
          "group": {
            "domain": {
              "id": "163240A90A0000BD1BAAF73394A403B0",
              "name": "Default"
            },
            "fullPathName": "None",
            "id": "201DB33F0A0000BD587D90FA64799744",
            "name": "My Company\\\\Default Group"
          },
          "uuid": "4C4C4544-0047-5310-8054-B9C04F504632",
          "groupUpdateProvider": "",
          "edrStatus": 0,
          "freeDisk": 10328551424,
          "snacicenseId": "",
          "diskDrive": "C:\\\\",
          "osFunction": "Workstation",
          "cidsDrvMulfCode": 0,
          "mobilePhone": "",
          "jobTitle": "",
          "lastHeuristicThreatTime": 0,
          "osname": "Windows 10",
          "winServers": [
            "0.0.0.0",
            "0.0.0.0"
          ],
          "deploymentMessage": "",
          "idsSerialNo": "",
          "employeeNumber": "",
          "lastSiteId": "C485F8390A0000BD0F806737FA94B6EF",
          "uwf": 2,
          "currentClientId": "D630A2D10A0000BD3566F8EC3AF38258",
          "osbitness": "x64",
          "osanguage": "None",
          "lastScanTime": 1549277509000,
          "dnsServers": [
            "10.0.0.190",
            "..."
          ],
          "securityVirtualAppliance": "None",
          "worstInfectionIdx": "0",
          "encryptedDevicePassword": "",
          "ptpOnOff": 1,
          "kernel": "None",
          "svaId": "",
          "lastConnectedIpAddr": "1.1.1.1",
          "agentVersion": "14.0.1904.0000",
          "ipAddresses": [
            "10.0.0.40",
            "192.168.56.1",
            "192.168.184.1"
          ],
          "agentTimeStamp": 1549287166434,
          "osfunction": "Workstation",
          "osMajor": 10,
          "deploymentTargetVersion": "14.0.1904.0000",
          "osMinor": 0,
          "osFlavorNumber": 126,
          "logicalCpus": 0,
          "deploymentPreVersion": "",
          "hypervisorVendorId": "0",
          "fbwf": 2,
          "osversion": "10.0",
          "email": "",
          "vsicStatus": 3,
          "lastServerId": "5B0090390A0000BD0EA208CFABAB79BF",
          "deleted": 0,
          "deploymentStatus": "302449921",
          "computerTimeStamp": 1549270030452,
          "bwf": 2,
          "totalDiskSpace": 121601,
          "homePhone": "",
          "daOnOff": 1,
          "computerDescription": "P-VICTORS",
          "pepOnOff": 1,
          "bashStatus": 1,
          "agentUsn": 4634006,
          "osName": "Windows 10",
          "patternIdx": "12D025D1F97B4681135C679CFB528DC0",
          "employeeStatus": "",
          "timeZone": -120,
          "rebootRequired": 0,
          "subnetMasks": [
            "255.255.254.0",
            "255.255.255.0",
            "255.255.255.0"
          ],
          "minorVersion": 0,
          "osservicePack": "",
          "lastSiteName": "testSite",
          "cidsEngineVersion": "1.1.1.1",
          "lastDeploymentTime": 1549269576000,
          "isGrace": 0,
          "computerUsn": 4628006,
          "agentId": "AA2625F10A0000BD3566F8EC8ADC3D2A",
          "cidsBrowserFfOnOff": 1,
          "domainOrWorkgroup": "SIEMPIFY.OCA",
          "lastUpdateTime": 1549287166434,
          "loginDomain": "SIEMPIFY.OCA",
          "lastServerName": "surajsep",
          "contentUpdate": 1,
          "writeFiltersStatus": "None",
          "infected": 0,
          "memory": 16827695104,
          "osminor": 0,
          "freeMem": 9575374848,
          "officePhone": "",
          "lastVirusTime": 1530785567000,
          "idsVersion": "",
          "cidsBrowserIeOnOff": 1,
          "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQBt1Cn6nstqwypo5vUwmPVs+Ebx0JltYQJCHqfuWRhyUqnTyRniQZRCOY92MS2fMS6vouWJx+DMqlu8vbIs3G4nFoSxXAXuPXaafpWObEUhsXrN4Gxt/Rwoi8uOXjODW4kt9FKw9xoVHMquSF/jhobMrcozXTtUf5QRTQoGheRSIOPN+JfjEuT1XAbt2uS+IbX3Sp648yyl94/XI7ZUGHaviq3eaYjK+FMN3S2Uv/i/3uxB+/gOHDHfOsn6wES6HEhN9jzrM3arlZlWXc7783SzUfq8uAZ13cWOPb8BnUKaY2A1r+Ca95dJatvo7pg1flmX4TGT72UOVM7kzI029",
          "quarantineDesc": "Host Integrity check passed   Requirement: ",
          "biosVersion": "DE   - 1072009 BIOS Date: 08/26/16 02:41:50 Ver: 1.1.1.1",
          "processorClock": 2808,
          "rebootReason": "",
          "cidsSilentMode": 0,
          "creationTime": 1530429396647,
          "macAddresses": [
            "18-DB-F2-46-23-C0",
            "0A-00-27-00-00-15",
            "00-50-56-C0-00-01"
          ],
          "idsChecksum": "None",
          "operatingSystem": "Windows 10 Enterprise 2015 TSB",
          "osmajor": 10,
          "virtualizationPlatform": "Unknown",
          "deploymentRunningVersion": "14.0.1904.0000",
          "physicalCpus": 4,
          "osBitness": "x64",
          "cidsDefsetVersion": "190201061",
          "cidsDrvOnOff": 1,
          "computerName": "P-NOYS",
          "logonUserName": "johndoe1",
          "atpServer": "",
          "gateways": [
            "10.0.0.138",
            "0.0.0.0",
            "0.0.0.0"
          ],
          "uniqueId": "9C9850840A0000BD3566F8ECC8417F64",
          "department": "",
          "isNpvdiClient": 0,
          "dhcpServer": "1.1.1.1",
          "description": "None",
          "osflavorNumber": 126,
          "tpmDevice": "0",
          "onlineStatus": 1,
          "lastDownloadTime": 1549150265991,
          "apOnOff": 1,
          "fullName": "",
          "osVersion": "10.0",
          "tmpDevice": "None",
          "attributeExtension": "",
          "licenseExpiry": 0,
          "tamperOnOff": 1,
          "osServicePack": "",
          "agentType": "105",
          "serialNumber": "9GSTPF2",
          "osElamStatus": 0,
          "installType": "0",
          "profileSerialNo": "201D-10/29/2018 21:39:09 743",
          "hardwareKey": "36817A7B13C3A6317932AD9819097322",
          "firewallOnOff": 1
        },
        "Entity": "HOST_2"
      }
    ]
    

### List Groups

#### Description

List all the groups configured on a particular device.

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
groups | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "policyDate": 1540849149743,
        "domain": {
          "id": "163240A90A0000BD1BAAF73394A403B0",
          "name": "Default"
        },
        "policySerialNumber": "201D-10/29/2018 21:39:09 743",
        "description": "",
        "created": 1480348907173,
        "customIpsNumber": "",
        "fullPathName": "My Company\\\\Default Group",
        "childGroups": "None",
        "numberOfPhysicalComputers": 1,
        "numberOfRegisteredUsers": 1,
        "createdBy": "AF3C39A10A320801000000DBF200C60A",
        "lastModified": 1480348907173,
        "id": "201DB33F0A0000BD587D90FA64799744",
        "policyInheritanceEnabled": "False",
        "name": "Default Group"
      },
      {
        "policyDate": 1540849149743,
        "domain": {
          "id": "163240A90A0000BD1BAAF73394A403B0",
          "name": "Default"
        },
        "policySerialNumber": "E25C-10/29/2018 21:39:09 743",
        "description": "",
        "created": 1480348907173,
        "customIpsNumber": "",
        "fullPathName": "My Company",
        "childGroups": "None",
        "numberOfPhysicalComputers": 0,
        "numberOfRegisteredUsers": 0,
        "createdBy": "AF3C39A10A320801000000DBF200C60A",
        "lastModified": 1480348907173,
        "id": "E25CFEAB0A0000BD6CF5CB6BC7A8505E",
        "policyInheritanceEnabled": "False",
        "name": "My Company"
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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Quarantine Endpoint

#### Description

Quarantine an endpoint.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Scan Endpoint

#### Description

Scan an endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Scan Type | List` | ScanNow_Full | The type of the scan to perform. ScanNow_Full = Full scan, ScanNow_Quick = quick scan, ScanNow_Custom = custom scan.  
  
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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Unblock Hash

#### Description

Unblock a particular hash.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Unquarantine Endpoint

#### Description

Unquarantine an endpoint.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Update and Scan Endpoint

#### Description

Update and scan an endpoint.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Update Endpoint

#### Description

Update an endpoint.

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
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
