---
url: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.AggregateFleetRequest
title: Google Cloud Database Center V1beta Client - Class AggregateFleetRequest (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:02.052971+00:00
---

# Google Cloud Database Center V1beta Client - Class AggregateFleetRequest (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-databasecenter/latest/V1beta.AggregateFleetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Database Center V1beta Client - Class AggregateFleetRequest (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Database Center V1beta Client class AggregateFleetRequest.

The request message to aggregate fleet which are grouped by a field.

Generated from protobuf message `google.cloud.databasecenter.v1beta.AggregateFleetRequest`

## Namespace

Google \ Cloud \ DatabaseCenter \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The allowed values are: * * projects/{PROJECT_ID} (e.g., "projects/foo-bar") * * projects/{PROJECT_NUMBER} (e.g., "projects/12345678") * * folders/{FOLDER_NUMBER} (e.g., "folders/1234567") * * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")  
`↳ filter` |  `string`   
Optional. The expression to filter resources. Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`↳ group_by` |  `string`   
Optional. A field that statistics are grouped by. Valid values are any combination of the following: * * container * * product.type * * product.engine * * product.version * * location * * sub_resource_type * * management_type * * tag.key * * tag.value * * tag.source * * tag.inherited * * label.key * * label.value * * label.source * * has_maintenance_schedule * * has_deny_maintenance_schedules Comma separated list.  
`↳ order_by` |  `string`   
Optional. Valid values to order by are: * * resource_groups_count * * resources_count * * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields. For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order  
`↳ page_size` |  `int`   
Optional. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`↳ page_token` |  `string`   
Optional. A page token, received from a previous `AggregateFleet` call. Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.  
`↳ baseline_date` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
### getParent

Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.

The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.

The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. The expression to filter resources.

Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. The expression to filter resources.

Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGroupBy

Optional. A field that statistics are grouped by.

Valid values are any combination of the following:

  * container
  * product.type
  * product.engine
  * product.version
  * location
  * sub_resource_type
  * management_type
  * tag.key
  * tag.value
  * tag.source
  * tag.inherited
  * label.key
  * label.value
  * label.source
  * has_maintenance_schedule
  * has_deny_maintenance_schedules Comma separated list.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setGroupBy

Optional. A field that statistics are grouped by.

Valid values are any combination of the following:

  * container
  * product.type
  * product.engine
  * product.version
  * location
  * sub_resource_type
  * management_type
  * tag.key
  * tag.value
  * tag.source
  * tag.inherited
  * label.key
  * label.value
  * label.source
  * has_maintenance_schedule
  * has_deny_maintenance_schedules Comma separated list.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. Valid values to order by are:

  * resource_groups_count
  * resources_count
  * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields.



For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. Valid values to order by are:

  * resource_groups_count
  * resources_count
  * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields.



For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. If unspecified, at most 50 items will be returned.

The maximum value is 1000; values above 1000 will be coerced to 1000.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. If unspecified, at most 50 items will be returned.

The maximum value is 1000; values above 1000 will be coerced to 1000.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A page token, received from a previous `AggregateFleet` call.

Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A page token, received from a previous `AggregateFleet` call.

Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBaselineDate

Optional. The baseline date w.r.t. which the delta counts are calculated.

If not set, delta counts are not included in the response and the response indicates the current state of the fleet.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)|null` |   
  
### hasBaselineDate

### clearBaselineDate

### setBaselineDate

Optional. The baseline date w.r.t. which the delta counts are calculated.

If not set, delta counts are not included in the response and the response indicates the current state of the fleet.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\Date](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Date.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
