---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints
title: REST Resource: projects.locations.networkMonitoringProviders.monitoringPoints \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:31.001028+00:00
---

# REST Resource: projects.locations.networkMonitoringProviders.monitoringPoints  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.networkMonitoringProviders.monitoringPoints Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MonitoringPoint
    * JSON representation
  * ConnectionStatus
  * UpgradeType
  * NetworkInterface
    * JSON representation
  * ErrorCode
  * Host
    * JSON representation
  * DeploymentType
  * Methods



## Resource: MonitoringPoint

Message describing MonitoringPoint resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "originatingIp": string,
      "version": string,
      "type": string,
      "connectionStatus": enum ([ConnectionStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#ConnectionStatus)),
      "hostname": string,
      "geoLocation": {
        object ([GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/GeoLocation))
      },
      "upgradeType": enum ([UpgradeType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#UpgradeType)),
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#NetworkInterface))
        }
      ],
      "errors": [
        enum ([ErrorCode](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#ErrorCode))
      ],
      "autoGeoLocationEnabled": boolean,
      "providerTags": [
        {
          object ([ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/ProviderTag))
        }
      ],
      "host": {
        object ([Host](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#Host))
      },
      "upgradeAvailable": boolean,
      "guid": string,
      "deploymentType": enum ([DeploymentType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#DeploymentType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format: `projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}/monitoringPoints/{monitoring_point}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the MonitoringPoint was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the MonitoringPoint was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Output only. Display name of the MonitoringPoint.  
`originatingIp` |  `string` Output only. IP address visible when MonitoringPoint connects to the provider.  
`version` |  `string` Output only. Version of the software running on the MonitoringPoint.  
`type` |  `string` Output only. Deployment type of the MonitoringPoint.  
`connectionStatus` |  `enum (`[ConnectionStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#ConnectionStatus)`)` Output only. Connection status of the MonitoringPoint.  
`hostname` |  `string` Output only. The hostname of the MonitoringPoint.  
`geoLocation` |  `object (`[GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/GeoLocation)`)` Output only. The geographical location of the MonitoringPoint.  
`upgradeType` |  `enum (`[UpgradeType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#UpgradeType)`)` Output only. The type of upgrade available for the MonitoringPoint.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#NetworkInterface)`)` Output only. The network interfaces of the MonitoringPoint.  
`errors[]` |  `enum (`[ErrorCode](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#ErrorCode)`)` Output only. The codes of errors detected in the MonitoringPoint.  
`autoGeoLocationEnabled` |  `boolean` Output only. Indicates if automaitic geographic location is enabled for the MonitoringPoint.  
`providerTags[]` |  `object (`[ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/ProviderTag)`)` Output only. The provider tags of the MonitoringPoint.  
`host` |  `object (`[Host](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#Host)`)` Output only. The host information of the MonitoringPoint.  
`upgradeAvailable` |  `boolean` Output only. Indicates if an upgrade is available for the MonitoringPoint.  
`guid` |  `string` Output only. The GUID of the MonitoringPoint.  
`deploymentType` |  `enum (`[DeploymentType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#DeploymentType)`)` Output only. The deployment type of the MonitoringPoint.  
  
## ConnectionStatus

Enum for the connection status of MonitoringPoint.

Enums  
---  
`CONNECTION_STATUS_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`ONLINE` | MonitoringPoint is online.  
`OFFLINE` | MonitoringPoint is offline.  
  
## UpgradeType

Enum for the type of upgrade available for the MonitoringPoint.

Enums  
---  
`UPGRADE_TYPE_UNSPECIFIED` | The default value. This value is used if the upgrade type is omitted.  
`MANUAL` | Upgrades are performed manually.  
`MANAGED` | Upgrades are managed.  
`SCHEDULED` | Upgrade is scheduled.  
`AUTO` | Upgrades are performed automatically.  
`EXTERNAL` | Upgrades are performed externally.  
  
## NetworkInterface

Message describing network interfaces.

JSON representation  
---  
      
    
    {
      "interfaceName": string,
      "speed": string,
      "ipAddress": string,
      "cidr": string,
      "macAddress": string,
      "adapterDescription": string,
      "vlanId": string
    }  
  
Fields  
---  
`interfaceName` |  `string` Output only. The name of the network interface. Examples: eth0, eno1  
`speed` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Speed of the interface in millions of bits per second.  
`ipAddress` |  `string` Output only. The IP address of the interface.  
`cidr` |  `string` Output only. The IP address of the interface and subnet mask in CIDR format. Examples: 192.168.1.0/24, 2001:db8::/32  
`macAddress` |  `string` Output only. The MAC address of the interface.  
`adapterDescription` |  `string` Output only. The description of the interface.  
`vlanId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the VLAN.  
  
## ErrorCode

Enum for the error codes.

Enums  
---  
`ERROR_CODE_UNSPECIFIED` | The default value. This value is used if the error code is omitted.  
`NTP_ERROR` | Error detected in NTP service.  
`UPGRADE_ERROR` | Error detected during the upgrade process.  
`DOWNLOAD_FAILED` | Error detected while downloading.  
  
## Host

Message describing information about the host.

JSON representation  
---  
      
    
    {
      "os": string,
      "cloudProvider": string,
      "cloudProjectId": string,
      "cloudInstanceId": string,
      "cloudRegion": string,
      "cloudZone": string,
      "cloudVirtualNetworkIds": [
        string
      ]
    }  
  
Fields  
---  
`os` |  `string` Output only. The operating system of the host.  
`cloudProvider` |  `string` Output only. The cloud provider of the host.  
`cloudProjectId` |  `string` Output only. The cloud project id of the host.  
`cloudInstanceId` |  `string` Output only. The cloud instance id of the host.  
`cloudRegion` |  `string` Output only. The cloud region of the host.  
`cloudZone` |  `string` Output only. The cloud zone of the host.  
`cloudVirtualNetworkIds[]` |  `string` Output only. The ids of cloud virtual networks of the host.  
  
## DeploymentType

The deployment type of the MonitoringPoint. Currently supports only c-50. New values may be added in the future.

Enums  
---  
`DEPLOYMENT_TYPE_UNSPECIFIED` | The default value. This value is used if the type is omitted.  
`DOCKER` | The MonitoringPoint is deployed as a Docker container.  
`PODMAN` | The MonitoringPoint is deployed as a Podman container.  
`HELM` | The MonitoringPoint is deployed as a Helm chart.  
  
## Methods  
  
---  
  
### `[downloadInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript)`

|  Downloads an install script for MonitoringPoints for a given network monitoring provider.  
  
### `[downloadRecreateInstallScript](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadRecreateInstallScript)`

|  Downloads an install script for a specific Container MonitoringPoint.  
  
### `[downloadServerConnectConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadServerConnectConfig)`

|  Downloads the server connect configuration for a given network monitoring provider.  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/get)`

|  Gets the `[MonitoringPoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` resource.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints/list)`

|  Lists `[MonitoringPoints](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders.monitoringPoints#MonitoringPoint)` for a given network monitoring provider.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
