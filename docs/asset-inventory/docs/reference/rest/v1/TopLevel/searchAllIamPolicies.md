---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies/
title: Method: searchAllIamPolicies \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.120379+00:00
---

# Method: searchAllIamPolicies  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: searchAllIamPolicies Stay organized with collections  Save and categorize content based on your preferences. 

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



Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllIamPolicies` permission on the desired scope, otherwise the request will be rejected.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{scope=*/*}:searchAllIamPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllIamPolicies`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllIamPolicies`

  
  
### Query parameters

Parameters  
---  
`query` |  `string` Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified `scope`. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure).Examples:

  * `policy:amy@gmail.com` to find IAM policy bindings that specify user "amy@gmail.com".
  * `policy:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
  * `policy:comp*` to find IAM policy bindings that contain "comp" as a prefix of any word in the binding.
  * `policy.role.permissions:storage.buckets.update` to find IAM policy bindings that specify a role containing "storage.buckets.update" permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
  * `policy.role.permissions:upd*` to find IAM policy bindings that specify a role containing "upd" as a prefix of any word in the role permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
  * `resource:organizations/123456` to find IAM policy bindings that are set on "organizations/123456".
  * `resource=//cloudresourcemanager.googleapis.com/projects/myproject` to find IAM policy bindings that are set on the project named "myproject".
  * `Important` to find IAM policy bindings that contain "Important" as a word in any of the searchable fields (except for the included permissions).
  * `resource:(instance1 OR instance2) policy:amy` to find IAM policy bindings that are set on resources "instance1" or "instance2" and also specify user "amy".
  * `roles:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
  * `memberTypes:user` to find IAM policy bindings that contain the principal type "user".

  
`pageSize` |  `integer` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `nextPageToken` is returned.  
`pageToken` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters must be identical to those in the previous call.  
`assetTypes[]` |  `string` Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types)Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots IAM policies attached to asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots IAM policies attached to asset type ends with "Instance".
  * ".*Instance.*" snapshots IAM policies attached to asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.  
`orderBy` |  `string` Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "assetType DESC, resource". Only singular primitive fields in the response are sortable: * resource * assetType * project All the other fields such as repeated fields (e.g., `folders`) and non-primitive fields (e.g., `policy`) are not supported.  
  
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
          object ([IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#IamPolicySearchResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `object (`[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#IamPolicySearchResult)`)` A list of IAM policies that match the search query. Related information such as the associated resource is returned along with the policy.  
`nextPageToken` |  `string` Set if there are more results than those appearing in this response; to get the next set of results, call this method again, using this value as the `pageToken`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## IamPolicySearchResult

A result of IAM Policy search, containing information of an IAM policy.

JSON representation  
---  
      
    
    {
      "resource": string,
      "assetType": string,
      "project": string,
      "folders": [
        string
      ],
      "organization": string,
      "policy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy))
      },
      "explanation": {
        object ([Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#Explanation))
      }
    }  
  
Fields  
---  
`resource` |  `string` The full resource name of the resource associated with this IAM policy. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.To search against the `resource`:

  * use a field query. Example: `resource:organizations/123`

  
`assetType` |  `string` The type of the resource associated with this IAM policy. Example: `compute.googleapis.com/Disk`.To search against the `assetType`:

  * specify the `assetTypes` field in your search request.

  
`project` |  `string` The project that the associated Google Cloud resource belongs to, in the form of projects/{PROJECT_NUMBER}. If an IAM policy is set on a resource (like VM instance, Cloud Storage bucket), the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, this field will be empty.To search against the `project`:

  * specify the `scope` field as this project in your search request.

  
`folders[]` |  `string` The folder(s) that the IAM policy belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs to one or more folders.To search against `folders`:

  * use a field query. Example: `folders:(123 OR 456)`
  * use a free text query. Example: `123`
  * specify the `scope` field as this folder in your search request.

  
`organization` |  `string` The organization that the IAM policy belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs to an organization.To search against `organization`:

  * use a field query. Example: `organization:123`
  * use a free text query. Example: `123`
  * specify the `scope` field as this organization in your search request.

  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy)`)` The IAM policy directly set on the given resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constrain on policies (e.g., an empty query), this contains all the bindings.To search against the `policy` bindings:

  * use a field query: 
    * query by the policy contained members. Example: `policy:amy@gmail.com`
    * query by the policy contained roles. Example: `policy:roles/compute.admin`
    * query by the policy contained roles' included permissions. Example: `policy.role.permissions:compute.instances.create`

  
`explanation` |  `object (`[Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#Explanation)`)` Explanation about the IAM policy search result. It contains additional information to explain why the search result matches the query.  
  
## Explanation

Explanation about the IAM policy search result.

JSON representation  
---  
      
    
    {
      "matchedPermissions": {
        string: {
          object ([Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#Permissions))
        },
        ...
      }
    }  
  
Fields  
---  
`matchedPermissions` |  `map (key: string, value: object (`[Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies#Permissions)`))` The map from roles to their included permissions that match the permission query (i.e., a query containing `policy.role.permissions:`). Example: if query `policy.role.permissions:compute.disk.get` matches a policy binding that contains owner role, the matchedPermissions will be `{"roles/owner": ["compute.disk.get"]}`. The roles can also be found in the returned `policy` bindings. Note that the map is populated only for requests with permission queries.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Permissions

IAM permissions

JSON representation  
---  
      
    
    {
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`permissions[]` |  `string` A list of permissions. A sample permission string: `compute.disk.get`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
