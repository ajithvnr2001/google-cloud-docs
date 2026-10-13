---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths
title: REST Resource: projects.locations.networkMonitoringProviders.webPaths \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:43.718478+00:00
---

# REST Resource: projects.locations.networkMonitoringProviders.webPaths  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.networkMonitoringProviders.webPaths Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WebPath
    * JSON representation
  * MonitoringStatus
  * WorkflowType
  * Methods



## Resource: WebPath

Message describing WebPath resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "sourceMonitoringPointId": string,
      "displayName": string,
      "destination": string,
      "monitoringEnabled": boolean,
      "monitoringStatus": enum ([MonitoringStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#MonitoringStatus)),
      "interval": string,
      "workflowType": enum ([WorkflowType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WorkflowType)),
      "relatedNetworkPathId": string,
      "providerTags": [
        {
          object ([ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag))
        }
      ],
      "monitoringPolicyId": string,
      "monitoringPolicyDisplayName": string,
      "providerUiUri": string,
      "destinationGeoLocation": {
        object ([GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/GeoLocation))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format: `projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}/webPaths/{web_path}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the WebPath was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the WebPath was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sourceMonitoringPointId` |  `string` Output only. ID of the source MonitoringPoint.  
`displayName` |  `string` Output only. Display name of the WebPath.  
`destination` |  `string` Output only. Web monitoring target.  
`monitoringEnabled` |  `boolean` Output only. Is monitoring enabled for the WebPath.  
`monitoringStatus` |  `enum (`[MonitoringStatus](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#MonitoringStatus)`)` Output only. The monitoring status of the WebPath.  
`interval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Monitoring interval.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`workflowType` |  `enum (`[WorkflowType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WorkflowType)`)` Output only. The workflow type of the WebPath.  
`relatedNetworkPathId` |  `string` Output only. Provider's UUID of the related `[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)`.  
`providerTags[]` |  `object (`[ProviderTag](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag)`)` Output only. The provider tags of the web path.  
`monitoringPolicyId` |  `string` Output only. ID of the monitoring policy.  
`monitoringPolicyDisplayName` |  `string` Output only. Display name of the monitoring policy.  
`providerUiUri` |  `string` Output only. Link to provider's UI; link shows the `[WebPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WebPath)`.  
`destinationGeoLocation` |  `object (`[GeoLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/GeoLocation)`)` Output only. Geographical location of the destination.  
  
## MonitoringStatus

Enum for monitoring status of the WebPath.

Enums  
---  
`MONITORING_STATUS_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`MONITORING` | Monitoring is enabled.  
`POLICY_MISMATCH` | Policy is mismatched.  
`MONITORING_POINT_OFFLINE` | Monitoring point is offline.  
`DISABLED` | Monitoring is disabled.  
  
## WorkflowType

Enum for workflow type.

Enums  
---  
`WORKFLOW_TYPE_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`BROWSER` | Browser.  
`HTTP` | HTTP.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths/get)`

|  Gets the `[WebPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` resource.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths/list)`

|  Lists `[WebPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.webPaths#WebPath)` for a given network monitoring provider.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-17 UTC."],[],[]] 
