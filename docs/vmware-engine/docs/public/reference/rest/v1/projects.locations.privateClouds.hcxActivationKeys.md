---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys
title: REST Resource: projects.locations.privateClouds.hcxActivationKeys \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:15.537353+00:00
---

# REST Resource: projects.locations.privateClouds.hcxActivationKeys  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.hcxActivationKeys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HcxActivationKey
    * JSON representation
  * State
  * Methods



## Resource: HcxActivationKey

HCX activation key. A default key is created during private cloud provisioning, but this behavior is subject to change and you should always verify active keys. Use `[VmwareEngine.ListHcxActivationKeys](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/list#google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys)` to retrieve existing keys and `[VmwareEngine.CreateHcxActivationKey](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/create#google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey)` to create new ones.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys#State)),
      "activationKey": string,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this HcxActivationKey. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of HCX activation key.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys#State)`)` Output only. State of HCX activation key.  
`activationKey` |  `string` Output only. HCX activation key.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
  
## State

State of HCX activation key

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`AVAILABLE` | State of a newly generated activation key.  
`CONSUMED` | State of key when it has been used to activate HCX appliance.  
`CREATING` | State of key when it is being created.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/create)`

|  Creates a new HCX activation key in a given private cloud.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/get)`

|  Retrieves a `HcxActivationKey` resource by its resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/list)`

|  Lists `HcxActivationKey` resources in a given private cloud.  
  
### `[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.hcxActivationKeys/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
