---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders
title: REST Resource: projects.locations.networkMonitoringProviders \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:29.060838+00:00
---

# REST Resource: projects.locations.networkMonitoringProviders  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.networkMonitoringProviders Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NetworkMonitoringProvider
    * JSON representation
  * ProviderType
  * State
  * Methods



## Resource: NetworkMonitoringProvider

Message describing NetworkMonitoringProvider resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "providerType": enum ([ProviderType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#ProviderType)),
      "providerUri": string,
      "state": enum ([State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#State)),
      "errors": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Name of the resource. Format: `projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the NetworkMonitoringProvider was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the NetworkMonitoringProvider was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`providerType` |  `enum (`[ProviderType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#ProviderType)`)` Required. Type of the NetworkMonitoringProvider.  
`providerUri` |  `string` Output only. Link to the provider's UI.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#State)`)` Output only. State of the NetworkMonitoringProvider.  
`errors[]` |  `string` Output only. The list of error messages detected for the NetworkMonitoringProvider.  
  
## ProviderType

Possible types of NetworkMonitoringProvider resource.

Enums  
---  
`PROVIDER_TYPE_UNSPECIFIED` | The default value. This value is used if the type is omitted.  
`EXTERNAL` | External provider.  
  
## State

Possible states of NetworkMonitoringProvider resource.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`ACTIVATING` | NetworkMonitoringProvider is being activated.  
`ACTIVE` | NetworkMonitoringProvider is active.  
`SUSPENDING` | NetworkMonitoringProvider is being suspended.  
`SUSPENDED` | NetworkMonitoringProvider is suspended.  
`DELETING` | NetworkMonitoringProvider is being deleted.  
`DELETED` | NetworkMonitoringProvider is deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/create)`

|  Creates a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
  
### `[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/delete)`

|  Deletes a `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource and all of its child resources.  
  
### `[generateMonitoringPointConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateMonitoringPointConfig)`

|  Generates Monitoring Point configuration of a NetworkMonitoringProvider resource.  
  
### `[generateProviderAccessToken](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/generateProviderAccessToken)`

|  Generates a provider access token for a given Google access token.  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/get)`

|  Gets the `[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` resource.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders/list)`

|  Lists `[NetworkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` for a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
