---
url: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:25:56.914202+00:00
---

# REST Resource: projects.locations.instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * State
  * ActivationState
  * Type
  * Methods



## Resource: Instance

Message describing Instance object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#State)),
      "region": string,
      "productActivation": {
        string: enum ([ActivationState](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#ActivationState)),
        ...
      },
      "licenseVersionId": string,
      "computeInstance": string,
      "externalInstance": string,
      "type": enum ([Type](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#Type))
    }  
  
Fields  
---  
`name` |  `string` Identifier. name of resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#State)`)` Output only. The state of the VM.  
`region` |  `string` Output only. The location of the VM.  
`productActivation` |  `map (key: string, value: enum (`[ActivationState](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#ActivationState)`))` Output only. Map with Product_Name and Activation State of the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`licenseVersionId` |  `string` Output only. license version id.  
`computeInstance  
**(deprecated)**` |  `string` This item is deprecated!Required. Compute Instance resource name, i.e. projects/{project}/zones/{zone}/instances/{instance}. Deprecated. Use externalInstance instead.  
`externalInstance` |  `string` Required. External instance resource name.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances#Type)`)` Required. The type of the external instance.  
  
## State

VM status enum.

Enums  
---  
`STATE_UNSPECIFIED` | The Status of the VM is unspecified.  
`PROVISIONING` | Resources are being allocated for the instance.  
`STAGING` | All required resources have been allocated and the instance is being started.  
`RUNNING` | The instance is running.  
`STOPPING` | The instance is currently stopping (either being deleted or terminated).  
`STOPPED` | The instance has stopped due to various reasons (user request, VM preemption, project freezing, etc.).  
`TERMINATED` | The instance has failed in some way.  
`REPAIRING` | The instance is in repair.  
  
## ActivationState

State of the License Key activation on the instance.

Enums  
---  
`ACTIVATION_STATE_UNSPECIFIED` | The Status of the activation is unspecified  
`ACTIVATION_STATE_KEY_REQUESTED` | Activation key (MAK) requested for the instance.  
`ACTIVATION_STATE_ACTIVATING` | License activation process is running on the instance.  
`ACTIVATION_STATE_ACTIVATED` | License activation is complete on the instance.  
`ACTIVATION_STATE_DEACTIVATING` | License Key is deactivating on the instance.  
`ACTIVATION_STATE_DEACTIVATED` | License Key is deactivated on the instance.  
`ACTIVATION_STATE_TERMINATED` | License Key activation failed on the instance.  
  
## Type

External instance type.

Enums  
---  
`TYPE_UNSPECIFIED` | The type of the external instance is unspecified.  
`TYPE_GCE` | The external instance is a Compute Engine instance.  
`TYPE_GCVE` | The external instance is a GCVE instance.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances/get)`

|  Gets details of a single Instance.  
  
### `[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances/list)`

|  Lists Instances in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
