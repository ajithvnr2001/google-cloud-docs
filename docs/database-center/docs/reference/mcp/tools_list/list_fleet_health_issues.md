---
url: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues/
title: MCP Tools Reference: databasecenter.googleapis.com \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:30.044616+00:00
---

# MCP Tools Reference: databasecenter.googleapis.com  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  MCP Tools Reference: databasecenter.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_fleet_health_issues`

This tool provides statistics about various health issues and signals detected across the database fleet. It helps in identifying the number of resources affected by different types of issues, categorized by signal types.

The following sample demonstrate how to use `curl` to invoke the `list_fleet_health_issues` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://databasecenter.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_fleet_health_issues",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

AggregateIssueStatsRequest represents the input to the AggregateIssueStats method.

### AggregateIssueStatsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "signalTypeGroups": [
        {
          object ([SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Input.Schema.SignalTypeGroup))
        }
      ],
    
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

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info,'resource_name', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`signalTypeGroups[]` |  `object (`[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Input.Schema.SignalTypeGroup)`)` Optional. Lists of signal types that are issues.  
Union field `_baseline_date`.`_baseline_date` can be only one of the following:  
`baselineDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date)`)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
### SignalTypeGroup

JSON representation  
---  
      
    
    {
      "displayName": string,
      "signalTypes": [
        enum (SignalType)
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Required. The display name of a signal group.  
`signalTypes[]` |  `enum (`SignalType`)` Optional. List of signal types present in the group.  
  
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

The response message containing one of more group of relevant health issues for database resources.

### AggregateIssueStatsResponse

JSON representation  
---  
      
    
    {
      "issueGroupStats": [
        {
          object ([IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Output.Schema.IssueGroupStats))
        }
      ],
      "totalResourcesCount": integer,
      "totalResourceGroupsCount": integer,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`issueGroupStats[]` |  `object (`[IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Output.Schema.IssueGroupStats)`)` List of issue group stats where each group contains stats for resources having a particular combination of relevant issues.  
`totalResourcesCount` |  `integer` Total count of the resources filtered in based on the user given filter.  
`totalResourceGroupsCount` |  `integer` Total count of the resource filtered in based on the user given filter.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### IssueGroupStats

JSON representation  
---  
      
    
    {
      "displayName": string,
      "resourceGroupsCount": integer,
      "resourcesCount": integer,
      "healthyResourceGroupsCount": integer,
      "healthyResourcesCount": integer,
      "issueStats": [
        {
          object ([IssueStats](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Output.Schema.IssueStats))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Database resource level health card name. This will corresponds to one of the requested input group names.  
`resourceGroupsCount` |  `integer` Total count of the groups of resources returned by the filter that also have one or more resources for which any of the specified issues are applicable.  
`resourcesCount` |  `integer` Total count of resources returned by the filter for which any of the specified issues are applicable.  
`healthyResourceGroupsCount` |  `integer` The number of resource groups from the total groups as defined above that are healthy with respect to all of the specified issues.  
`healthyResourcesCount` |  `integer` The number of resources from the total defined above in field total_resources_count that are healthy with respect to all of the specified issues.  
`issueStats[]` |  `object (`[IssueStats](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues#Output.Schema.IssueStats)`)` List of issues stats containing count of resources having particular issue category.  
  
### IssueStats

JSON representation  
---  
      
    
    {
      "signalType": enum (SignalType),
      "resourceCount": integer,
    
      // Union field _delta_details can be only one of the following:
      "deltaDetails": {
        object ([DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.DeltaDetails))
      }
      // End of list of possible types for union field _delta_details.
    
      // Union field _issue_severity can be only one of the following:
      "issueSeverity": enum (IssueSeverity)
      // End of list of possible types for union field _issue_severity.
    }  
  
Fields  
---  
`signalType` |  `enum (`SignalType`)` Type of signal which is an issue.  
`resourceCount` |  `integer` Number of resources having issues of a given type.  
Union field `_delta_details`.`_delta_details` can be only one of the following:  
`deltaDetails` |  `object (`[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Output.Schema.DeltaDetails)`)` Optional. Delta counts and details of resources for which issue was raised or fixed.  
Union field `_issue_severity`.`_issue_severity` can be only one of the following:  
`issueSeverity` |  `enum (`IssueSeverity`)` Severity of the issue.  
  
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
