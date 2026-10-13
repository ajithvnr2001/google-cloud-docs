---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats/
title: Method: aggregateIssueStats \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.168180+00:00
---

# Method: aggregateIssueStats  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: aggregateIssueStats Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * IssueGroupStats
    * JSON representation
  * IssueStats
    * JSON representation
  * Try it!



v1beta.aggregateIssueStats provides database resource issues statistics.

### HTTP request

`POST https://databasecenter.googleapis.com/v1beta:aggregateIssueStats`

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
      "baselineDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `fullResourceName`, `resourceType`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info,'resourceName', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`signalTypeGroups[]` |  `object (`[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalTypeGroup)`)` Optional. Lists of signal types that are issues.  
`baselineDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date)`)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
### Response body

The response message containing one of more group of relevant health issues for database resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "issueGroupStats": [
        {
          object ([IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats#IssueGroupStats))
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
`issueGroupStats[]` |  `object (`[IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats#IssueGroupStats)`)` List of issue group stats where each group contains stats for resources having a particular combination of relevant issues.  
`totalResourcesCount` |  `integer` Total count of the resources filtered in based on the user given filter.  
`totalResourceGroupsCount` |  `integer` Total count of the resource filtered in based on the user given filter.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetHealthStats.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## IssueGroupStats

IssueGroupStats refers to stats for a particulare combination of relevant health issues of database resources.

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
          object ([IssueStats](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats#IssueStats))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Database resource level health card name. This will corresponds to one of the requested input group names.  
`resourceGroupsCount` |  `integer` Total count of the groups of resources returned by the filter that also have one or more resources for which any of the specified issues are applicable.  
`resourcesCount` |  `integer` Total count of resources returned by the filter for which any of the specified issues are applicable.  
`healthyResourceGroupsCount` |  `integer` The number of resource groups from the total groups as defined above that are healthy with respect to all of the specified issues.  
`healthyResourcesCount` |  `integer` The number of resources from the total defined above in field totalResourcesCount that are healthy with respect to all of the specified issues.  
`issueStats[]` |  `object (`[IssueStats](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats#IssueStats)`)` List of issues stats containing count of resources having particular issue category.  
  
## IssueStats

IssueStats holds stats for a particular signal category.

JSON representation  
---  
      
    
    {
      "signalType": enum ([SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)),
      "resourceCount": integer,
      "deltaDetails": {
        object ([DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DeltaDetails))
      },
      "issueSeverity": enum ([IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/IssueSeverity))
    }  
  
Fields  
---  
`signalType` |  `enum (`[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)`)` Type of signal which is an issue.  
`resourceCount` |  `integer` Number of resources having issues of a given type.  
`deltaDetails` |  `object (`[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DeltaDetails)`)` Optional. Delta counts and details of resources for which issue was raised or fixed.  
`issueSeverity` |  `enum (`[IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/IssueSeverity)`)` Severity of the issue.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
