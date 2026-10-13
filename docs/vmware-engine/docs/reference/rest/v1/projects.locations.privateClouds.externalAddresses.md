---
url: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses
title: REST Resource: projects.locations.privateClouds.externalAddresses \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:57.993362+00:00
---

# REST Resource: projects.locations.privateClouds.externalAddresses  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback 

#  REST Resource: projects.locations.privateClouds.externalAddresses Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExternalAddress
    * JSON representation
  * State
  * Methods



## Resource: ExternalAddress

Represents an allocated external IP address and its corresponding internal IP address in a private cloud.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "internalIp": string,
      "externalIp": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses#State)),
      "uid": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this external IP address. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`internalIp` |  `string` The internal IP address of a workload VM.  
`externalIp` |  `string` Output only. The external IP address of a workload VM.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses#State)`)` Output only. The state of the resource.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`description` |  `string` User-provided description for this resource.  
  
## State

Enum State defines possible states of external addresses.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | The address is ready.  
`CREATING` | The address is being created.  
`UPDATING` | The address is being updated.  
`DELETING` | The address is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses/create)`

|  Creates a new `ExternalAddress` resource in a given private cloud.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses/delete)`

|  Deletes a single external IP address.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses/get)`

|  Gets details of a single external IP address.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses/list)`

|  Lists external IP addresses assigned to VMware workload VMs in a given private cloud.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses/patch)`

|  Updates the parameters of a single external IP address.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
