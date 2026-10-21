---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources/
title: Method: projects.locations.registryBooks.searchIpResources \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:13.655873+00:00
---

# Method: projects.locations.registryBooks.searchIpResources  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Method: projects.locations.registryBooks.searchIpResources Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SearchResourceType
  * Range
    * JSON representation
  * SearchIpResourcesResult
    * JSON representation
  * Try it!



Searches IP resources in a given RegistryBook.

### HTTP request

`POST https://cloudnumberregistry.googleapis.com/v1alpha/{name=projects/*/locations/*/registryBooks/*}:searchIpResources`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the RegistryBook to search in.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "query": string,
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string,
      "showUtilization": boolean,
      "searchResourceTypes": [
        enum ([SearchResourceType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#SearchResourceType))
      ]
    }  
  
Fields  
---  
`query` |  `string` Optional. Search query. This string filters resources in an AIP-160-like format. It has some limitations. You can only specify top level conjunctions or attribute level negations. Each restriction can only be used once except the attribute restriction.The available restrictions for Ranges are: - `realm`: The Realm name to search in. - `ip_address`: The IP address to search for within Ranges. - `ipVersion`: The IP version to filter by (e.g., "IPV4", "IPV6"). - `parentRange`: The parent Range of the Range to search for. - `attribute_text`: The attribute text to search for within Ranges. - `attribute`: The attribute key and value to filter by.The available restrictions for Realms are: - `ipVersion`: The IP version to search for. - `managementType`: The management type of the Realm (e.g., "CNR", "USER").Only one of attribute_text or multiple attribute filters can be specified. Examples: - `realm=test-realm` \- `realm=test-realm AND ip_address=10.0.0.0` \- `realm=test-realm AND ipVersion=IPV6` \- `realm=test-realm AND attribute_text=test` \- `ip_address=10.0.0.0 AND attribute:(key1=value1) AND attribute:(key2=value2)` \- `attribute_text=test AND parentRange=projects/123/locations/global/discoveredRanges/test-parent-range` \- `managementType=CNR`  
`orderBy` |  `string` Optional. Hint for how to order the results. Supported sort fields are: - `name`: Sort alphabetically by the resource name. - `createTime`: Sort by the creation timestamp of the resource. - `updateTime`: Sort by the last update timestamp of the resource.Supported directions are `asc` (ascending) and `desc` (descending). If unspecified, direction defaults to `asc`. Only sorting by a single field is supported.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`showUtilization` |  `boolean` Optional. Whether to show the utilization of the Ranges in the response.  
`searchResourceTypes[]` |  `enum (`[SearchResourceType](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#SearchResourceType)`)` Optional. The type of resources to search for. If not specified, the server will return Ranges.  
  
### Response body

Response message for the `[CloudNumberRegistry.SearchIpResources](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#google.cloud.numberregistry.v1alpha.CloudNumberRegistry.SearchIpResources)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ranges": [
        {
          object ([Range](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#Range))
        }
      ],
      "results": [
        {
          object ([SearchIpResourcesResult](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#SearchIpResourcesResult))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`ranges[]  
**(deprecated)**` |  `object (`[Range](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#Range)`)` This item is deprecated!Deprecated: Use results field instead. The list of Ranges matching the search query.  
`results[]` |  `object (`[SearchIpResourcesResult](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#SearchIpResourcesResult)`)` The list of results matching the search query.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudnumberregistry.registryBooks.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SearchResourceType

The type of resources to search for.

Enums  
---  
`SEARCH_RESOURCE_TYPE_UNSPECIFIED` | Unspecified search type.  
`RANGES` | Search for Ranges.  
`REALMS` | Search for Realms.  
  
## Range

Represents either a CustomRange or a DiscoveredRange.

JSON representation  
---  
      
    
    {
      "utilization": {
        object ([RangeUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization))
      },
    
      // Union field range can be only one of the following:
      "customRange": {
        object ([CustomRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges#CustomRange))
      },
      "discoveredRange": {
        object ([DiscoveredRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges#DiscoveredRange))
      }
      // End of list of possible types for union field range.
    }  
  
Fields  
---  
`utilization` |  `object (`[RangeUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/RangeUtilization)`)` The utilization of the Range.  
Union field `range`. The Range. `range` can be only one of the following:  
`customRange` |  `object (`[CustomRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges#CustomRange)`)` A CustomRange.  
`discoveredRange` |  `object (`[DiscoveredRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges#DiscoveredRange)`)` A DiscoveredRange.  
  
## SearchIpResourcesResult

A result matching the search query, which can be either a Range or a Realm.

JSON representation  
---  
      
    
    {
    
      // Union field result can be only one of the following:
      "range": {
        object ([Range](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#Range))
      },
      "realm": {
        object ([Realm](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#Realm))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
Union field `result`. Either a Range or a Realm matching the search query. `result` can be only one of the following:  
`range` |  `object (`[Range](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources#Range)`)` A Range matching the search query.  
`realm` |  `object (`[Realm](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms#Realm)`)` A Realm matching the search query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
