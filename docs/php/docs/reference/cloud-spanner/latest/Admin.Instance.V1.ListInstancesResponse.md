---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse
title: Cloud Spanner V1 Client - Class ListInstancesResponse (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:21.238261+00:00
---

# Cloud Spanner V1 Client - Class ListInstancesResponse (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class ListInstancesResponse (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class ListInstancesResponse.

The response for [ListInstances](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Client.InstanceAdminClient#_Google_Cloud_Spanner_Admin_Instance_V1_Client_InstanceAdminClient__listInstances__).

Generated from protobuf message `google.spanner.admin.instance.v1.ListInstancesResponse`

## Namespace

Google \ Cloud \ Spanner \ Admin \ Instance \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ instances` |  `array<[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Instance)>`   
The list of requested instances.  
`↳ next_page_token` |  `string`   
`next_page_token` can be sent in a subsequent [ListInstances](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Client.InstanceAdminClient#_Google_Cloud_Spanner_Admin_Instance_V1_Client_InstanceAdminClient__listInstances__) call to fetch more of the matching instances.  
`↳ unreachable` |  `string[]`   
The list of unreachable instances. It includes the names of instances whose metadata could not be retrieved within [instance_deadline](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesRequest__getInstanceDeadline__).  
  
### getInstances

The list of requested instances.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Instance)>` |   
  
### setInstances

The list of requested instances.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Instance](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Instance)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNextPageToken

`next_page_token` can be sent in a subsequent [ListInstances](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Client.InstanceAdminClient#_Google_Cloud_Spanner_Admin_Instance_V1_Client_InstanceAdminClient__listInstances__) call to fetch more of the matching instances.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNextPageToken

`next_page_token` can be sent in a subsequent [ListInstances](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Client.InstanceAdminClient#_Google_Cloud_Spanner_Admin_Instance_V1_Client_InstanceAdminClient__listInstances__) call to fetch more of the matching instances.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUnreachable

The list of unreachable instances.

It includes the names of instances whose metadata could not be retrieved within [instance_deadline](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesRequest__getInstanceDeadline__).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setUnreachable

The list of unreachable instances.

It includes the names of instances whose metadata could not be retrieved within [instance_deadline](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesRequest__getInstanceDeadline__).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
