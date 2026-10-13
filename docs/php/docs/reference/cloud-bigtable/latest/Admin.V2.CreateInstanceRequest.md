---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateInstanceRequest
title: Cloud Bigtable V2 Client - Class CreateInstanceRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:38.501084+00:00
---

# Cloud Bigtable V2 Client - Class CreateInstanceRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class CreateInstanceRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class CreateInstanceRequest.

Request message for BigtableInstanceAdmin.CreateInstance.

Generated from protobuf message `google.bigtable.admin.v2.CreateInstanceRequest`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`.  
`↳ instance_id` |  `string`   
Required. The ID to be used when referring to the new instance within its project, e.g., just `myinstance` rather than `projects/myproject/instances/myinstance`.  
`↳ instance` |  `[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)`   
Required. The instance to create. Fields marked `OutputOnly` must be left blank.  
`↳ clusters` |  `array|Google\Protobuf\Internal\MapField`   
Required. The clusters to be created within the instance, mapped by desired cluster ID, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`. Fields marked `OutputOnly` must be left blank.  
  
### getParent

Required. The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInstanceId

Required. The ID to be used when referring to the new instance within its project, e.g., just `myinstance` rather than `projects/myproject/instances/myinstance`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setInstanceId

Required. The ID to be used when referring to the new instance within its project, e.g., just `myinstance` rather than `projects/myproject/instances/myinstance`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInstance

Required. The instance to create.

Fields marked `OutputOnly` must be left blank.

**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)|null` |   
  
### hasInstance

### clearInstance

### setInstance

Required. The instance to create.

Fields marked `OutputOnly` must be left blank.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClusters

Required. The clusters to be created within the instance, mapped by desired cluster ID, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.

Fields marked `OutputOnly` must be left blank.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setClusters

Required. The clusters to be created within the instance, mapped by desired cluster ID, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.

Fields marked `OutputOnly` must be left blank.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`. Please see BigtableInstanceAdminClient::projectName() for help formatting this field.  
`instanceId` |  `string`   
Required. The ID to be used when referring to the new instance within its project, e.g., just `myinstance` rather than `projects/myproject/instances/myinstance`.  
`instance` |  `[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance)`   
Required. The instance to create. Fields marked `OutputOnly` must be left blank.  
`clusters` |  `array`   
Required. The clusters to be created within the instance, mapped by desired cluster ID, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`. Fields marked `OutputOnly` must be left blank.  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstanceRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateInstanceRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
