---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance
title: Cloud Bigtable V2 Client - Class Instance (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:46.803976+00:00
---

# Cloud Bigtable V2 Client - Class Instance (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Instance (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Instance.

A collection of Bigtable [Tables](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table) and the resources that serve them.

All tables in an instance are served from all [Clusters](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster) in the instance.

Generated from protobuf message `google.bigtable.admin.v2.Instance`

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
`↳ name` |  `string`   
The unique name of the instance. Values are of the form `projects/{project}/instances/[a-z][a-z0-9\\-]+[a-z0-9]`.  
`↳ display_name` |  `string`   
Required. The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion.  
`↳ state` |  `int`   
Output only. The current state of the instance.  
`↳ type` |  `int`   
The type of the instance. Defaults to `PRODUCTION`.  
`↳ edition` |  `int`   
Optional. The edition of the instance. See [Edition](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Edition) for details.  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}`. * * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * * No more than 64 labels can be associated with a given resource. * * Keys and values must both be under 128 bytes.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.  
`↳ satisfies_pzs` |  `bool`   
Output only. Reserved for future use.  
`↳ satisfies_pzi` |  `bool`   
Output only. Reserved for future use.  
`↳ tags` |  `array|Google\Protobuf\Internal\MapField`   
Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: - "123/environment": "production", - "123/costCenter": "marketing" Tags and Labels (above) are both used to bind metadata to resources, with different use-cases. See <https://cloud.google.com/resource-manager/docs/tags/tags-overview> for an in-depth overview on the difference between tags and labels.  
  
### getName

The unique name of the instance. Values are of the form `projects/{project}/instances/[a-z][a-z0-9\\-]+[a-z0-9]`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the instance. Values are of the form `projects/{project}/instances/[a-z][a-z0-9\\-]+[a-z0-9]`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The descriptive name for this instance as it appears in UIs.

Can be changed at any time, but should be kept globally unique to avoid confusion.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The descriptive name for this instance as it appears in UIs.

Can be changed at any time, but should be kept globally unique to avoid confusion.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the instance.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.State).  
  
### setState

Output only. The current state of the instance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

The type of the instance. Defaults to `PRODUCTION`.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Type).  
  
### setType

The type of the instance. Defaults to `PRODUCTION`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Type](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Type).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEdition

Optional. The edition of the instance. See [Edition](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Edition) for details.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Edition](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Edition).  
  
### setEdition

Optional. The edition of the instance. See [Edition](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Edition) for details.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Edition](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance.Edition).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics.

  * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}`.
  * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`.
  * No more than 64 labels can be associated with a given resource.
  * Keys and values must both be under 128 bytes.



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics.

  * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}`.
  * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`.
  * No more than 64 labels can be associated with a given resource.
  * Keys and values must both be under 128 bytes.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSatisfiesPzs

Output only. Reserved for future use.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasSatisfiesPzs

### clearSatisfiesPzs

### setSatisfiesPzs

Output only. Reserved for future use.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSatisfiesPzi

Output only. Reserved for future use.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasSatisfiesPzi

### clearSatisfiesPzi

### setSatisfiesPzi

Output only. Reserved for future use.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTags

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example:

  * "123/environment": "production",
  * "123/costCenter": "marketing" Tags and Labels (above) are both used to bind metadata to resources, with different use-cases. See <https://cloud.google.com/resource-manager/docs/tags/tags-overview> for an in-depth overview on the difference between tags and labels.



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setTags

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example:

  * "123/environment": "production",
  * "123/costCenter": "marketing" Tags and Labels (above) are both used to bind metadata to resources, with different use-cases. See <https://cloud.google.com/resource-manager/docs/tags/tags-overview> for an in-depth overview on the difference between tags and labels.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
