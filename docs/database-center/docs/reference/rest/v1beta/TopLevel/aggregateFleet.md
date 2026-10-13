---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet/
title: Method: aggregateFleet \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.375843+00:00
---

# Method: aggregateFleet  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: aggregateFleet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AggregateFleetRow
    * JSON representation
  * Dimension
    * JSON representation
  * ManagementType
  * Try it!



v1beta.aggregateFleet provides statistics about the fleet grouped by various fields.

### HTTP request

`GET https://databasecenter.googleapis.com/v1beta:aggregateFleet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `fullResourceName`, `resourceType`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resourceName', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`groupBy` |  `string` Optional. A field that statistics are grouped by. Valid values are any combination of the following: * container * product.type * product.engine * product.version * location * subResourceType * managementType * tag.key * tag.value * tag.source * tag.inherited * label.key * label.value * label.source * hasMaintenanceSchedule * hasDenyMaintenanceSchedules Comma separated list.  
`orderBy` |  `string` Optional. Valid values to order by are: * resourceGroupsCount * resourcesCount * and all fields supported by `groupBy` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields. For example: `orderBy = "resourceGroupsCount"` sorts response in ascending order `orderBy = "resourceGroupsCount DESC"` sorts response in descending order `orderBy = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order  
`pageSize` |  `integer` Optional. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `v1beta.aggregateFleet` call. Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for pageSize which can be different.  
`baselineDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date)`)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
### Request body

The request body must be empty.

### Response body

The response message to aggregate a fleet by some group by fields.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rows": [
        {
          object ([AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#AggregateFleetRow))
        }
      ],
      "resourceGroupsTotalCount": integer,
      "resourceTotalCount": integer,
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`rows[]` |  `object (`[AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#AggregateFleetRow)`)` Represents a row grouped by the fields in the input.  
`resourceGroupsTotalCount` |  `integer` Count of all resource groups in the fleet. This includes counts from all pages.  
`resourceTotalCount` |  `integer` Count of all resources in the fleet. This includes counts from all pages.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetStats.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AggregateFleetRow

Individual row grouped by a particular dimension.

JSON representation  
---  
      
    
    {
      "dimension": [
        {
          object ([Dimension](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#Dimension))
        }
      ],
      "resourceGroupsCount": integer,
      "resourcesCount": integer,
      "deltaDetails": {
        object ([DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DeltaDetails))
      }
    }  
  
Fields  
---  
`dimension[]` |  `object (`[Dimension](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#Dimension)`)` Group by dimension.  
`resourceGroupsCount` |  `integer` Number of resource groups that have a particular dimension.  
`resourcesCount` |  `integer` Number of resources that have a particular dimension.  
`deltaDetails` |  `object (`[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DeltaDetails)`)` Optional. Delta counts and details of resources which were added to/deleted from fleet.  
  
## Dimension

Dimension used to aggregate the fleet.

JSON representation  
---  
      
    
    {
    
      // Union field dimension can be only one of the following:
      "container": string,
      "productType": enum ([ProductType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ProductType)),
      "productEngine": enum ([Engine](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Engine)),
      "productVersion": string,
      "location": string,
      "resourceType": string,
      "subResourceType": enum ([SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SubResourceType)),
      "resourceCategory": enum ([ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceCategory)),
      "managementType": enum ([ManagementType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#ManagementType)),
      "edition": enum ([Edition](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Edition)),
      "tagKey": string,
      "tagValue": string,
      "tagSource": string,
      "tagInherited": boolean,
      "labelKey": string,
      "labelValue": string,
      "labelSource": string,
      "hasMaintenanceSchedule": boolean,
      "hasDenyMaintenanceSchedules": boolean
      // End of list of possible types for union field dimension.
    }  
  
Fields  
---  
Union field `dimension`. Followings are the dimensions to be used to aggregate the fleet. `dimension` can be only one of the following:  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`productType` |  `enum (`[ProductType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ProductType)`)` Type to identify a product  
`productEngine` |  `enum (`[Engine](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Engine)`)` Engine refers to underlying database binary running in an instance.  
`productVersion` |  `string` Version of the underlying database engine  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud.  
`resourceType` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`subResourceType` |  `enum (`[SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SubResourceType)`)` Subtype of the resource specified at creation time.  
`resourceCategory` |  `enum (`[ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceCategory)`)` The category of the resource.  
`managementType` |  `enum (`[ManagementType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet#ManagementType)`)` The management type of the resource.  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Edition)`)` The edition of the resource.  
`tagKey` |  `string` Tag key of the resource.  
`tagValue` |  `string` Tag value of the resource.  
`tagSource` |  `string` Tag source of the resource.  
`tagInherited` |  `boolean` Tag inheritance value of the resource.  
`labelKey` |  `string` Label key of the resource.  
`labelValue` |  `string` Label value of the resource.  
`labelSource` |  `string` Label source of the resource.  
`hasMaintenanceSchedule` |  `boolean` Whether the resource has a maintenance schedule.  
`hasDenyMaintenanceSchedules` |  `boolean` Whether the resource has deny maintenance schedules.  
  
## ManagementType

The management type of the resource.

Enums  
---  
`MANAGEMENT_TYPE_UNSPECIFIED` | Unspecified.  
`MANAGEMENT_TYPE_GCP_MANAGED` | Google-managed resource.  
`MANAGEMENT_TYPE_SELF_MANAGED` | Self-managed resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
