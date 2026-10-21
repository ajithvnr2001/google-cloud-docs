---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes
title: REST Resource: projects.locations.ipamAdminScopes \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:12.180594+00:00
---

# REST Resource: projects.locations.ipamAdminScopes  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  REST Resource: projects.locations.ipamAdminScopes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IpamAdminScope
    * JSON representation
  * AddOnPlatform
  * DiscoveryPipelineState
  * Methods



## Resource: IpamAdminScope

An IpamAdminScope defines the administrative boundary for IP address discovery and management. It configures which platforms and organizational scopes are enabled for IP tracking.

JSON representation  
---  
      
    
    {
      "name": string,
      "enabledAddonPlatforms": [
        enum ([AddOnPlatform](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes#AddOnPlatform))
      ],
      "scopes": [
        string
      ],
      "state": enum ([DiscoveryPipelineState](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes#DiscoveryPipelineState)),
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the IpamAdminScope.  
`enabledAddonPlatforms[]` |  `enum (`[AddOnPlatform](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes#AddOnPlatform)`)` Required. Add-on platforms that are enabled for this IpamAdminScope. Cloud Number Registry only discovers the IP addresses from the enabled platforms.  
`scopes[]` |  `string` Required. Administrative scopes enabled for IP address discovery and management. For example, "organizations/1234567890". Minimum of 1 scope is required. In preview, only one organization scope is allowed.  
`state` |  `enum (`[DiscoveryPipelineState](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes#DiscoveryPipelineState)`)` Output only. State of resource discovery pipeline.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the IpamAdminScope was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the IpamAdminScope was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## AddOnPlatform

Enum for add-on platforms.

Enums  
---  
`ADD_ON_PLATFORM_UNSPECIFIED` | Unspecified add-on platform.  
`COMPUTE_ENGINE` | Google Compute Engine.  
`GCE` | Deprecated: Use COMPUTE_ENGINE instead.This item is deprecated!  
  
## DiscoveryPipelineState

Enum for IpamAdminScope discovery pipeline state.

Enums  
---  
`DISCOVERY_PIPELINE_STATE_UNSPECIFIED` | Unspecified state.  
`INTERNAL_FAILURE` | Internal failure.  
`FAILED` | Failure.  
`SETUP_IN_PROGRESS` | Setup in progress.  
`READY_FOR_USE` | Ready for use.  
`DELETING_IN_PROGRESS` | Deleting in progress.  
`UPDATING` | Updating.  
`RECOVERING` | Recovering.  
`DISABLED` | Disabled.  
`DELETION_COMPLETED` | Deleting completed.  
`CLEANUP_IN_PROGRESS` | Cleanup in progress.  
`READY_FOR_DELETION` | Ready for deletion.  
  
## Methods  
  
---  
  
### `[checkAvailability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability)`

|  Checks the availability of IpamAdminScopes in a given project and location.  
  
### `[cleanup](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/cleanup)`

|  Cleans up a single IpamAdminScope.  
  
### `[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/create)`

|  Creates a new IpamAdminScope in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/delete)`

|  Deletes a single IpamAdminScope.  
  
### `[disable](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/disable)`

|  Disables a single IpamAdminScope.  
  
### `[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/get)`

|  Gets details of a single IpamAdminScope.  
  
### `[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/list)`

|  Lists IpamAdminScopes in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/patch)`

|  Updates the parameters of a single IpamAdminScope.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
