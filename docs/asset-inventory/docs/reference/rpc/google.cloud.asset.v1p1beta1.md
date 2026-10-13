---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1
title: Package google.cloud.asset.v1p1beta1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:09.900227+00:00
---

# Package google.cloud.asset.v1p1beta1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.cloud.asset.v1p1beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.AssetService)` (interface)
  * `[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.IamPolicySearchResult)` (message)
  * `[IamPolicySearchResult.Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation)` (message)
  * `[Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.Permissions)` (message)
  * `[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllIamPoliciesRequest)` (message)
  * `[SearchAllIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllIamPoliciesResponse)` (message)
  * `[SearchAllResourcesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllResourcesRequest)` (message)
  * `[SearchAllResourcesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllResourcesResponse)` (message)
  * `[StandardResourceMetadata](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.StandardResourceMetadata)` (message)



## AssetService

Asset service definition.

SearchAllIamPolicies  
---  
` rpc SearchAllIamPolicies(`[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllIamPoliciesRequest)`) returns (`[SearchAllIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllIamPoliciesResponse)`) ` Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the IAM policies within a scope, even if they don't have `.getIamPolicy` permission of all the IAM policies. Callers should have `cloudasset.assets.searchAllIamPolicies` permission on the requested scope, otherwise the request will be rejected.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SearchAllResources  
---  
` rpc SearchAllResources(`[SearchAllResourcesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllResourcesRequest)`) returns (`[SearchAllResourcesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.SearchAllResourcesResponse)`) ` Searches all the resources within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the resources within a scope, even if they don't have `.get` permission of all the resources. Callers should have `cloudasset.assets.searchAllResources` permission on the requested scope, otherwise the request will be rejected.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## IamPolicySearchResult

The result for an IAM policy search.

Fields  
---  
`resource` |  `string` The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource associated with this IAM policy.  
`project` |  `string` The project that the associated Google Cloud resource belongs to, in the form of `projects/{project_number}`. If an IAM policy is set on a resource -- such as a Compute Engine instance or a Cloud Storage bucket -- the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, the project field will be empty.  
`policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` The IAM policy attached to the specified resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constraint on policies (e.g. an empty query), this contains all the bindings.  
`explanation` |  `[Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation)` Explanation about the IAM policy search result. It contains additional information that explains why the search result matches the query.  
  
## Explanation

Explanation about the IAM policy search result.

Fields  
---  
`matched_permissions` |  `map<string, `[Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.Permissions)`>` The map from roles to their included permission matching the permission query (e.g. containing `policy.role.permissions:`). Example role string: "roles/compute.instanceAdmin". The roles can also be found in the returned `policy` bindings. Note that the map is populated only if requesting with a permission query.  
  
## Permissions

IAM permissions.

Fields  
---  
`permissions[]` |  `string` A list of permissions. Example permission string: "compute.disk.get".  
  
## SearchAllIamPoliciesRequest

Search all IAM policies request.

Fields  
---  
`scope` |  `string` Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be:

  * Organization number (such as "organizations/123")
  * Folder number (such as "folders/1234")
  * Project number (such as "projects/12345")
  * Project ID (such as "projects/abc")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllIamPolicies`

  
`query` |  `string` Optional. The query statement. Examples:

  * "policy:[myuser@mydomain.com](mailto:myuser@mydomain.com)"
  * "policy:([myuser@mydomain.com](mailto:myuser@mydomain.com) viewer)"

  
`page_size` |  `int32` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.  
`page_token` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters must be identical to those in the previous call.  
  
## SearchAllIamPoliciesResponse

Search all IAM policies response.

Fields  
---  
`results[]` |  `[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.IamPolicySearchResult)` A list of IAM policies that match the search query. Related information such as the associated resource is returned along with the policy.  
`next_page_token` |  `string` Set if there are more results than those appearing in this response; to get the next set of results, call this method again, using this value as the `page_token`.  
  
## SearchAllResourcesRequest

Search all resources request.

Fields  
---  
`scope` |  `string` Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be:

  * Organization number (such as "organizations/123")
  * Folder number (such as "folders/1234")
  * Project number (such as "projects/12345")
  * Project ID (such as "projects/abc")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`

  
`query` |  `string` Optional. The query statement.  
`asset_types[]` |  `string` Optional. A list of asset types that this request searches for. If empty, it will search all the supported asset types.  
`page_size` |  `int32` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.  
`page_token` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
`order_by` |  `string` Optional. A comma separated list of fields specifying the sorting order of the results. The default order is ascending. Add `DESC` after the field name to indicate descending order. Redundant space characters are ignored. For example, `location DESC , name`.  
  
## SearchAllResourcesResponse

Search all resources response.

Fields  
---  
`results[]` |  `[StandardResourceMetadata](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.StandardResourceMetadata)` A list of resource that match the search query.  
`next_page_token` |  `string` If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
  
## StandardResourceMetadata

The standard metadata of a cloud resource.

Fields  
---  
`name` |  `string` The full resource name. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of this resource. For example: "compute.googleapis.com/Disk".  
`project` |  `string` The project that this resource belongs to, in the form of `projects/{project_number}`.  
`display_name` |  `string` The display name of this resource.  
`description` |  `string` One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes.  
`additional_attributes[]` |  `string` Additional searchable attributes of this resource. Informational only. The exact set of attributes is subject to change. For example: project id, DNS name etc.  
`location` |  `string` Location can be "global", regional like "us-east1", or zonal like "us-west1-b".  
`labels` |  `map<string, string>` Labels associated with this resource. See [Labelling and grouping Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information.  
`network_tags[]` |  `string` Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See [Labelling Google Cloud resources](lhttps://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
