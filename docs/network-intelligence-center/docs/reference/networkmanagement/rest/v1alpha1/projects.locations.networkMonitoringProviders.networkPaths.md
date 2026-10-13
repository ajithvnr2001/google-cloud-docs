---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths
title: REST Resource: projects.locations.networkMonitoringProviders.networkPaths \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:42.905825+00:00
---

# REST Resource: projects.locations.networkMonitoringProviders.networkPaths  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.networkMonitoringProviders.networkPaths Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NetworkPath
    * JSON representation
  * NetworkProtocol
  * MonitoringStatus
  * Methods



## Resource: NetworkPath

Message describing NetworkPath resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "sourceMonitoringPointId": string,
      "destinationMonitoringPointId": string,
      "destination": string,
      "dualEnded": boolean,
      "displayName": string,
      "destinationGeoLocation": {
        object ([GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/GeoLocation))
      },
      "networkProtocol": enum ([NetworkProtocol](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkProtocol)),
      "monitoringEnabled": boolean,
      "monitoringStatus": enum ([MonitoringStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#MonitoringStatus)),
      "providerTags": [
        {
          object ([ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag))
        }
      ],
      "monitoringPolicyId": string,
      "monitoringPolicyDisplayName": string,
      "providerUiUri": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format: `projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}/networkPaths/{network_path}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the NetworkPath was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the NetworkPath was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sourceMonitoringPointId` |  `string` Output only. Provider's UUID of the source MonitoringPoint. This id may not point to a resource in the Google Cloud.  
`destinationMonitoringPointId` |  `string` Output only. Provider's UUID of the destination MonitoringPoint. This id may not point to a resource in the Google Cloud.  
`destination` |  `string` Output only. IP address or hostname of the network path destination.  
`dualEnded` |  `boolean` Output only. Indicates if the network path is dual ended.When true, the network path is measured both: from both source to destination, and from destination to source.When false, the network path is measured from the source through the destination back to the source (round trip measurement).  
`displayName` |  `string` Output only. The display name of the network path.  
`destinationGeoLocation` |  `object (`[GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/GeoLocation)`)` Output only. Geographical location of the destination MonitoringPoint. ;  
`networkProtocol` |  `enum (`[NetworkProtocol](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkProtocol)`)` Output only. The network protocol of the network path.  
`monitoringEnabled` |  `boolean` Output only. Is monitoring enabled for the network path.  
`monitoringStatus` |  `enum (`[MonitoringStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#MonitoringStatus)`)` Output only. The monitoring status of the network path.  
`providerTags[]` |  `object (`[ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag)`)` Output only. The provider tags of the network path.  
`monitoringPolicyId` |  `string` Output only. ID of monitoring policy.  
`monitoringPolicyDisplayName` |  `string` Output only. Display name of the monitoring policy.  
`providerUiUri` |  `string` Output only. Link to provider's UI; link shows the `[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)`.  
  
## NetworkProtocol

Enum for the network protocol.

Enums  
---  
`NETWORK_PROTOCOL_UNSPECIFIED` | The default value. This value is used if the network protocol is omitted.  
`ICMP` | ICMP.  
`UDP` | UDP.  
`TCP` | TCP.  
  
## MonitoringStatus

Enum for the monitoring status of the network path.

Enums  
---  
`MONITORING_STATUS_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`MONITORING` | Monitoring is enabled.  
`POLICY_MISMATCH` | Policy is mismatched.  
`MONITORING_POINT_OFFLINE` | Monitoring point is offline.  
`DISABLED` | Monitoring is disabled.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/get)`

|  Gets the `[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` resource.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/list)`

|  Lists `[NetworkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` for a given network monitoring provider.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-17 UTC."],[],[]] 
