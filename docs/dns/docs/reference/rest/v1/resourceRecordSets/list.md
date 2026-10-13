---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list/
title: Method: resourceRecordSets.list \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:21.044049+00:00
---

# Method: resourceRecordSets.list  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Method: resourceRecordSets.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Enumerates ResourceRecordSets that you have created but not yet deleted.

### HTTP request

`GET https://dns.googleapis.com/dns/v1/projects/{project}/managedZones/{managedZone}/rrsets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Identifies the project addressed by this request.  
`managedZone` |  `string` Identifies the managed zone addressed by this request. Can be the managed zone name or ID.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer` Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.  
`pageToken` |  `string` Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.  
`name` |  `string` Specify a fully qualified domain name to view only those records. The `name` parameter is not supported and must be omitted when you use `filter`.  
`type` |  `string` Specify a record type to view only those records. You must also specify the `name` parameter. The `type` parameter is not supported and must be omitted when you use `filter`.  
`filter` |  `string` Specify a filter expression to view records that exactly match the specified domain. Both the `name` and `type` parameters are not supported and must be omitted when you use `filter`.Your `filter` expression must conform to [AIP-160](https://google.aip.dev/160) and you must specify a domain in the `name` field. Optionally, you can include the `type` field to filter records by type. You can also include the `has_suffix` function to view records that match by domain suffix. Examples:

  * `name`="example.com."
  * `name`="example.com." AND type="A"
  * `name`=`has_suffix`("example.com.")
  * `name`=`has_suffix`("example.com.") AND type="A"

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rrsets": [
        {
          object ([ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet))
        }
      ],
      "nextPageToken": string,
      "kind": string
    }  
  
Fields  
---  
`rrsets[]` |  `object (`[ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet)`)` The resource record set resources.  
`nextPageToken` |  `string` This field indicates that more results are available beyond the last page displayed. To fetch the results, make another list request and use this value as your page token. This lets you retrieve the complete contents of a very large collection one page at a time.However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You can't retrieve a consistent snapshot of a collection larger than the maximum page size.  
`kind` |  `string` Type of resource.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`
  * ` https://www.googleapis.com/auth/ndev.clouddns.readonly`
  * ` https://www.googleapis.com/auth/ndev.clouddns.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `project` resource:

  * `dns.resourceRecordSets.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
