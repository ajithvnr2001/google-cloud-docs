---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups/
title: Method: queryDatabaseResourceGroups \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.490039+00:00
---

# Method: queryDatabaseResourceGroups  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: queryDatabaseResourceGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SignalFilter
    * JSON representation
  * DatabaseResourceGroup
    * JSON representation
  * IssueCount
    * JSON representation
  * Try it!



v1beta.queryDatabaseResourceGroups returns paginated results of database groups.

### HTTP request

`POST https://databasecenter.googleapis.com/v1beta:queryDatabaseResourceGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "signalTypeGroups": [
        {
          object ([SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalTypeGroup))
        }
      ],
      "signalFilters": [
        {
          object ([SignalFilter](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#SignalFilter))
        }
      ],
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.The following fields are filterable: * fullResourceName * resourceType * container * product.type * product.engine * product.version * location * labels * resourceCategory * machineConfig.cpu_count * machineConfig.memory_size_bytes * machineConfig.shard_count * resourceName * tags * backupdrConfig.backupdr_managed * editionThe expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"` Example: `fullResourceName=~"test"` Example: `fullResourceName=~"test.*master"`  
`signalTypeGroups[]` |  `object (`[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalTypeGroup)`)` Optional. Groups of signal types that are requested.  
`signalFilters[]` |  `object (`[SignalFilter](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#SignalFilter)`)` Optional. Filters based on signals. The list will be ORed together and then ANDed with the `filters` field above.  
`orderBy` |  `string` Optional. A field that specifies the sort order of the results.The following fields are sortable: * fullResourceName * product.type * product.engine * product.version * container * issueCount * machineConfig.vcpu_count * machineConfig.memory_size_bytes * machineConfig.shard_count * resourceName * issueSeverity * signalType * location * resourceType * instance_type * edition * metrics.p99_cpu_utilization * metrics.p95_cpu_utilization * metrics.current_storage_used_bytes * metrics.node_count * metrics.processing_unit_count * metrics.current_memory_used_bytes * metrics.peak_storage_utilization * metrics.peak_number_connections * metrics.peak_memory_utilizationThe default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.For example: `orderBy = "fullResourceName"` sorts response in ascending order `orderBy = "fullResourceName DESC"` sorts response in descending order `orderBy = "issueCount DESC"` sorts response in descending order of count of all issues associated with a resource.More explicitly, `orderBy = "fullResourceName, product"` is not supported.  
`pageSize` |  `integer` Optional. If unspecified, at most 50 resource groups will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `QueryDatabaseResourceGroupsRequest` call. Provide this to retrieve the subsequent page. All parameters except pageToken should match the parameters in the call that provided the page page token.  
  
### Response body

QueryDatabaseResourceGroupsResponse represents the response message containing a list of resource groups.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resourceGroups": [
        {
          object ([DatabaseResourceGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#DatabaseResourceGroup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`resourceGroups[]` |  `object (`[DatabaseResourceGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#DatabaseResourceGroup)`)` List of database resource groups that pass the filter.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.databaseGroups.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SignalFilter

A filter for Signals.

If signalType is left unset, all signals should be returned. For example, the following filter returns all issues. signal_filter: { signalStatus: SIGNAL_STATUS_ISSUE; }

Another example, the following filter returns issues of the given type: signal_filter: { type: SIGNAL_TYPE_NO_PROMOTABLE_REPLICA signalStatus: ISSUE }

If signalStatus is left unset or set to SIGNAL_STATE_UNSPECIFIED, an error should be returned.

JSON representation  
---  
      
    
    {
      "signalType": enum ([SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)),
      "signalStatus": enum ([SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalStatus))
    }  
  
Fields  
---  
`signalType` |  `enum (`[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)`)` Optional. Represents the type of the Signal for which the filter is for.  
`signalStatus` |  `enum (`[SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalStatus)`)` Optional. Represents the status of the Signal for which the filter is for.  
  
## DatabaseResourceGroup

DatabaseResourceGroup represents all resources that serve a common data set. It is considered notionally as a single entity, powered by any number of units of compute and storage.

JSON representation  
---  
      
    
    {
      "rootResources": [
        {
          object ([DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource))
        }
      ],
      "signalGroups": [
        {
          object ([IssueCount](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#IssueCount))
        }
      ]
    }  
  
Fields  
---  
`rootResources[]` |  `object (`[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource)`)` A database resource that serves as a root of the group of database resources. It is repeated just in case we have the concept of multiple roots in the future, however, it will only be populated with a single value for now.  
`signalGroups[]` |  `object (`[IssueCount](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups#IssueCount)`)` The filtered signal groups and the count of issues associated with the resources that have been filtered in.  
  
## IssueCount

Count of issues for a group of signals.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "issueCount": integer
    }  
  
Fields  
---  
`displayName` |  `string` Title of a signal group corresponding to the request.  
`issueCount` |  `integer` The count of the number of issues associated with those resources that are explicitly filtered in by the filters present in the request. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
