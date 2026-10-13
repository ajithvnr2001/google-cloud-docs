---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest
title: Cloud Spanner V1 Client - Class ListInstancesRequest (2.11.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:26.933995+00:00
---

# Cloud Spanner V1 Client - Class ListInstancesRequest (2.11.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner V1 Client - Class ListInstancesRequest (2.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner V1 Client class ListInstancesRequest.

The request for [ListInstances](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.Client.InstanceAdminClient#_Google_Cloud_Spanner_Admin_Instance_V1_Client_InstanceAdminClient__listInstances__).

Generated from protobuf message `google.spanner.admin.instance.v1.ListInstancesRequest`

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
`↳ parent` |  `string`   
Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`.  
`↳ page_size` |  `int`   
Number of instances to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`↳ page_token` |  `string`   
If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getNextPageToken__) from a previous [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).  
`↳ filter` |  `string`   
An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * * `name` * * `display_name` * * `labels.key` where key is the name of a label Some examples of using filters are: * * `name:*` \--> The instance has a name. * * `name:Howl` \--> The instance's name contains the string "howl". * * `name:HOWL` \--> Equivalent to above. * * `NAME:howl` \--> Equivalent to above. * * `labels.env:*` \--> The instance has the label "env". * * `labels.env:dev` \--> The instance has the label "env" and the value of the label contains the string "dev". * * `name:howl labels.env:dev` \--> The instance's name contains "howl" and it has the label "env" with its value containing "dev".  
`↳ instance_deadline` |  `Google\Protobuf\Timestamp`   
Deadline used while retrieving metadata for instances. Instances whose metadata cannot be retrieved within this deadline will be added to [unreachable](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getUnreachable__) in [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).  
  
### getParent

Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Number of instances to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Number of instances to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getNextPageToken__) from a previous [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getNextPageToken__) from a previous [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `display_name`
  * `labels.key` where key is the name of a label Some examples of using filters are:
  * `name:*` \--> The instance has a name.


  * `name:Howl` \--> The instance's name contains the string "howl".
    * `name:HOWL` \--> Equivalent to above.
    * `NAME:howl` \--> Equivalent to above.
    * `labels.env:*` \--> The instance has the label "env".
    * `labels.env:dev` \--> The instance has the label "env" and the value of the label contains the string "dev".
    * `name:howl labels.env:dev` \--> The instance's name contains "howl" and it has the label "env" with its value containing "dev".



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `display_name`
  * `labels.key` where key is the name of a label Some examples of using filters are:
  * `name:*` \--> The instance has a name.


  * `name:Howl` \--> The instance's name contains the string "howl".
    * `name:HOWL` \--> Equivalent to above.
    * `NAME:howl` \--> Equivalent to above.
    * `labels.env:*` \--> The instance has the label "env".
    * `labels.env:dev` \--> The instance has the label "env" and the value of the label contains the string "dev".
    * `name:howl labels.env:dev` \--> The instance's name contains "howl" and it has the label "env" with its value containing "dev".



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInstanceDeadline

Deadline used while retrieving metadata for instances.

Instances whose metadata cannot be retrieved within this deadline will be added to [unreachable](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getUnreachable__) in [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasInstanceDeadline

### clearInstanceDeadline

### setInstanceDeadline

Deadline used while retrieving metadata for instances.

Instances whose metadata cannot be retrieved within this deadline will be added to [unreachable](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse#_Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesResponse__getUnreachable__) in [ListInstancesResponse](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesResponse).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`. Please see InstanceAdminClient::projectName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListInstancesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Admin.Instance.V1.ListInstancesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
