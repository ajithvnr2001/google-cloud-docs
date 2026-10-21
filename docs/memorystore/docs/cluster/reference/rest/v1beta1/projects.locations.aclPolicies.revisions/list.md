---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions/list/
title: Method: projects.locations.aclPolicies.revisions.list \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:41.887026+00:00
---

# Method: projects.locations.aclPolicies.revisions.list  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Method: projects.locations.aclPolicies.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all ACL policy revisions in a given ACL policy.

### HTTP request

`GET https://redis.googleapis.com/v1beta1/{parent=projects/*/locations/*/aclPolicies/*}/revisions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the ACL policy to list revisions for. Format: "projects/{projectId}/locations/{locationId}/aclPolicies/{aclPolicyId}"  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return.  
`pageToken` |  `string` Optional. The `nextPageToken` value returned from a previous `revisions.list` request, if any.  
  
### Request body

The request body must be empty.

### Response body

Response for `revisions.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "aclPolicyRevisions": [
        {
          object ([AclPolicyRevision](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions#AclPolicyRevision))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`aclPolicyRevisions[]` |  `object (`[AclPolicyRevision](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions#AclPolicyRevision)`)` A list of ACL policy revisions.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/redis.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
