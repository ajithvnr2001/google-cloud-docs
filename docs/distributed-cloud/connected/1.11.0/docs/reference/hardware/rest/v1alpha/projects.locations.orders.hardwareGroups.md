---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups
title: REST Resource: projects.locations.orders.hardwareGroups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:47.402700+00:00
---

# REST Resource: projects.locations.orders.hardwareGroups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups




#  REST Resource: projects.locations.orders.hardwareGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HardwareGroup
    * JSON representation
  * State
  * Methods



## Resource: HardwareGroup

A group of hardware that is part of the same order, has the same SKU, and is delivered to the same site.

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
      "hardwareCount": integer,
      "config": {
        object ([HardwareConfig](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/HardwareConfig))
      },
      "site": string,
      "state": enum ([State](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups#State)),
      "zone": string,
      "requestedInstallationDate": {
        object ([Date](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/Date))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of this hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardwareGroup}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when this hardware group was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when this hardware group was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels associated with this hardware group as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`hardwareCount` |  `integer` Required. Number of hardware in this HardwareGroup.  
`config` |  `object (`[HardwareConfig](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/HardwareConfig)`)` Required. Configuration for hardware in this HardwareGroup.  
`site` |  `string` Required. Name of the site where the hardware in this HardwareGroup will be delivered. Format: `projects/{project}/locations/{location}/sites/{site}`  
`state` |  `enum (`[State](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups#State)`)` Output only. Current state of this HardwareGroup.  
`zone` |  `string` Optional. Name of the zone that the hardware in this HardwareGroup belongs to. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`requestedInstallationDate  
**(deprecated)**` |  `object (`[Date](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/Date)`)` This item is deprecated!Optional. Deprecated: This value is not used. Use the requestedInstallationDate field in the Order resource instead.  
  
## State

Valid states of a HardwareGroup.

Enums  
---  
`STATE_UNSPECIFIED` | State of the HardwareGroup is unspecified.  
`ADDITIONAL_INFO_NEEDED` | More information is required from the customer to make progress.  
`BUILDING` | Google has initiated building hardware for this HardwareGroup.  
`SHIPPING` | The hardware has been built and is being shipped.  
`INSTALLING` | The hardware is being installed.  
`PARTIALLY_INSTALLED` | Some hardware in the HardwareGroup have been installed.  
`INSTALLED` | All hardware in the HardwareGroup have been installed.  
`FAILED` | An error occurred and customer intervention is required.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/create)`

|  Creates a new hardware group in a given order.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/delete)`

|  Deletes a hardware group.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/get)`

|  Gets details of a hardware group.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/list)`

|  Lists hardware groups in a given order.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/patch)`

|  Updates the parameters of a hardware group.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
