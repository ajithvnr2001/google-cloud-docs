---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll/
title: Method: iamPolicies.searchAll \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:06.036108+00:00
---

# Method: iamPolicies.searchAll  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: iamPolicies.searchAll Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IamPolicySearchResult
    * JSON representation
  * Explanation
    * JSON representation
  * Permissions
    * JSON representation
  * Try it!



Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the IAM policies within a scope, even if they don't have `.getIamPolicy` permission of all the IAM policies. Callers should have `cloudasset.assets.searchAllIamPolicies` permission on the requested scope, otherwise the request will be rejected.

### HTTP request

`GET https://cloudasset.googleapis.com/v1p1beta1/{scope=*/*}/iamPolicies:searchAll`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be:

  * Organization number (such as "organizations/123")
  * Folder number (such as "folders/1234")
  * Project number (such as "projects/12345")
  * Project ID (such as "projects/abc")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllIamPolicies`

  
  
### Query parameters

Parameters  
---  
`query` |  `string` Optional. The query statement. Examples:

  * "policy:[myuser@mydomain.com](mailto:myuser@mydomain.com)"
  * "policy:([myuser@mydomain.com](mailto:myuser@mydomain.com) viewer)"

  
`pageSize` |  `integer` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `nextPageToken` is returned.  
`pageToken` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters must be identical to those in the previous call.  
  
### Request body

The request body must be empty.

### Response body

Search all IAM policies response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#IamPolicySearchResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `object (`[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#IamPolicySearchResult)`)` A list of IAM policies that match the search query. Related information such as the associated resource is returned along with the policy.  
`nextPageToken` |  `string` Set if there are more results than those appearing in this response; to get the next set of results, call this method again, using this value as the `pageToken`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## IamPolicySearchResult

The result for an IAM policy search.

JSON representation  
---  
      
    
    {
      "resource": string,
      "project": string,
      "policy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy))
      },
      "explanation": {
        object ([Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#Explanation))
      }
    }  
  
Fields  
---  
`resource` |  `string` The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource associated with this IAM policy.  
`project` |  `string` The project that the associated Google Cloud resource belongs to, in the form of `projects/{projectNumber}`. If an IAM policy is set on a resource -- such as a Compute Engine instance or a Cloud Storage bucket -- the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, the project field will be empty.  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy)`)` The IAM policy attached to the specified resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constraint on policies (e.g. an empty query), this contains all the bindings.  
`explanation` |  `object (`[Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#Explanation)`)` Explanation about the IAM policy search result. It contains additional information that explains why the search result matches the query.  
  
## Explanation

Explanation about the IAM policy search result.

JSON representation  
---  
      
    
    {
      "matchedPermissions": {
        string: {
          object ([Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#Permissions))
        },
        ...
      }
    }  
  
Fields  
---  
`matchedPermissions` |  `map (key: string, value: object (`[Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll#Permissions)`))` The map from roles to their included permission matching the permission query (e.g. containing `policy.role.permissions:`). Example role string: "roles/compute.instanceAdmin". The roles can also be found in the returned `policy` bindings. Note that the map is populated only if requesting with a permission query.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Permissions

IAM permissions.

JSON representation  
---  
      
    
    {
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`permissions[]` |  `string` A list of permissions. Example permission string: "compute.disk.get".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
