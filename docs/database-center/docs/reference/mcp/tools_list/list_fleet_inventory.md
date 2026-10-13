---
url: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory/
title: MCP Tools Reference: databasecenter.googleapis.com \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:29.886256+00:00
---

# MCP Tools Reference: databasecenter.googleapis.com  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  MCP Tools Reference: databasecenter.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_fleet_inventory`

This tool retrieves aggregated statistics and inventory information about the database resources. It can group the results by various dimensions like product type, engine, location, etc. This is useful for understanding the overall composition and distribution of the database fleet.

The following sample demonstrate how to use `curl` to invoke the `list_fleet_inventory` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://databasecenter.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_fleet_inventory",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request message to aggregate fleet which are grouped by a field.

### AggregateFleetRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "groupBy": string,
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string,
    
      // Union field _baseline_date can be only one of the following:
      "baselineDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date))
      }
      // End of list of possible types for union field _baseline_date.
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`groupBy` |  `string` Optional. A field that statistics are grouped by. Valid values are any combination of the following: * container * product.type * product.engine * product.version * location * sub_resource_type * management_type * tag.key * tag.value * tag.source * tag.inherited * label.key * label.value * label.source * has_maintenance_schedule * has_deny_maintenance_schedules Comma separated list.  
`orderBy` |  `string` Optional. Valid values to order by are: * resource_groups_count * resources_count * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields. For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order  
`pageSize` |  `integer` Optional. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `AggregateFleet` call. Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.  
Union field `_baseline_date`.`_baseline_date` can be only one of the following:  
`baselineDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date)`)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
### Date

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
## Output Schema

The response message to aggregate a fleet by some group by fields.

### AggregateFleetResponse

JSON representation  
---  
      
    
    {
      "rows": [
        {
          object ([AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.AggregateFleetRow))
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
`rows[]` |  `object (`[AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.AggregateFleetRow)`)` Represents a row grouped by the fields in the input.  
`resourceGroupsTotalCount` |  `integer` Count of all resource groups in the fleet. This includes counts from all pages.  
`resourceTotalCount` |  `integer` Count of all resources in the fleet. This includes counts from all pages.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### AggregateFleetRow

JSON representation  
---  
      
    
    {
      "dimension": [
        {
          object ([Dimension](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.Dimension))
        }
      ],
      "resourceGroupsCount": integer,
      "resourcesCount": integer,
    
      // Union field _delta_details can be only one of the following:
      "deltaDetails": {
        object ([DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.DeltaDetails))
      }
      // End of list of possible types for union field _delta_details.
    }  
  
Fields  
---  
`dimension[]` |  `object (`[Dimension](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.Dimension)`)` Group by dimension.  
`resourceGroupsCount` |  `integer` Number of resource groups that have a particular dimension.  
`resourcesCount` |  `integer` Number of resources that have a particular dimension.  
Union field `_delta_details`.`_delta_details` can be only one of the following:  
`deltaDetails` |  `object (`[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.DeltaDetails)`)` Optional. Delta counts and details of resources which were added to/deleted from fleet.  
  
### Dimension

JSON representation  
---  
      
    
    {
    
      // Union field dimension can be only one of the following:
      "container": string,
      "productType": enum (ProductType),
      "productEngine": enum (Engine),
      "productVersion": string,
      "location": string,
      "resourceType": string,
      "subResourceType": enum (SubResourceType),
      "resourceCategory": enum (ResourceCategory),
      "managementType": enum (ManagementType),
      "edition": enum (Edition),
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
`productType` |  `enum (`ProductType`)` Type to identify a product  
`productEngine` |  `enum (`Engine`)` Engine refers to underlying database binary running in an instance.  
`productVersion` |  `string` Version of the underlying database engine  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud.  
`resourceType` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`subResourceType` |  `enum (`SubResourceType`)` Subtype of the resource specified at creation time.  
`resourceCategory` |  `enum (`ResourceCategory`)` The category of the resource.  
`managementType` |  `enum (`ManagementType`)` The management type of the resource.  
`edition` |  `enum (`Edition`)` The edition of the resource.  
`tagKey` |  `string` Tag key of the resource.  
`tagValue` |  `string` Tag value of the resource.  
`tagSource` |  `string` Tag source of the resource.  
`tagInherited` |  `boolean` Tag inheritance value of the resource.  
`labelKey` |  `string` Label key of the resource.  
`labelValue` |  `string` Label value of the resource.  
`labelSource` |  `string` Label source of the resource.  
`hasMaintenanceSchedule` |  `boolean` Whether the resource has a maintenance schedule.  
`hasDenyMaintenanceSchedules` |  `boolean` Whether the resource has deny maintenance schedules.  
  
### DeltaDetails

JSON representation  
---  
      
    
    {
      "increasedResources": [
        {
          object ([ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.ResourceDetails))
        }
      ],
      "decreasedResources": [
        {
          object ([ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.ResourceDetails))
        }
      ]
    }  
  
Fields  
---  
`increasedResources[]` |  `object (`[ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.ResourceDetails)`)` Details of resources that have increased.  
`decreasedResources[]` |  `object (`[ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.ResourceDetails)`)` Details of resources that have decreased.  
  
### ResourceDetails

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "container": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product))
      },
      "location": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Full resource name of the resource.  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product)`)` Product type of the resource.  
`location` |  `string` Location of the resource.  
  
### Product

JSON representation  
---  
      
    
    {
      "type": enum (ProductType),
      "engine": enum (Engine),
      "version": string,
      "minorVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`ProductType`)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `enum (`Engine`)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minorVersion` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
