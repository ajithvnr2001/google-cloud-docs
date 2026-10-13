---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet/
title: Method: effectiveIamPolicies.batchGet \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.851455+00:00
---

# Method: effectiveIamPolicies.batchGet  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: effectiveIamPolicies.batchGet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * EffectiveIamPolicy
    * JSON representation
  * PolicyInfo
    * JSON representation
  * Try it!



Gets effective IAM policies for a batch of resources.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{scope=*/*}/effectiveIamPolicies:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. Only IAM policies on or below the scope will be returned.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`

  
  
### Query parameters

Parameters  
---  
`names[]` |  `string` Required. The names refer to the [full_resource_names](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). A maximum of 20 resources' effective policies can be retrieved in a batch.  
  
### Request body

The request body must be empty.

### Response body

A response message for `[AssetService.BatchGetEffectiveIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policyResults": [
        {
          object ([EffectiveIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy))
        }
      ]
    }  
  
Fields  
---  
`policyResults[]` |  `object (`[EffectiveIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy)`)` The effective policies for a batch of resources. Note that the results order is the same as the order of `[BatchGetEffectiveIamPoliciesRequest.names](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#body.QUERY_PARAMETERS.names)`. When a resource does not have any effective IAM policies, its corresponding policy_result will contain empty `[EffectiveIamPolicy.policies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.policies)`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## EffectiveIamPolicy

The effective IAM policies on one resource.

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "policies": [
        {
          object ([PolicyInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo))
        }
      ]
    }  
  
Fields  
---  
`fullResourceName` |  `string` The [fullResourceName](https://cloud.google.com/asset-inventory/docs/resource-name-format) for which the `[policies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.policies)` are computed. This is one of the `[BatchGetEffectiveIamPoliciesRequest.names](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#body.QUERY_PARAMETERS.names)` the caller provides in the request.  
`policies[]` |  `object (`[PolicyInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo)`)` The effective policies for the `[fullResourceName](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.full_resource_name)`.These policies include the policy set on the `[fullResourceName](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.full_resource_name)` and those set on its parents and ancestors up to the `[BatchGetEffectiveIamPoliciesRequest.scope](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#body.PATH_PARAMETERS.scope)`. Note that these policies are not filtered according to the resource type of the `[fullResourceName](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.full_resource_name)`.These policies are hierarchically ordered by `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo.FIELDS.attached_resource)` starting from `[fullResourceName](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#EffectiveIamPolicy.FIELDS.full_resource_name)` itself to its parents and ancestors, such that policies[i]'s `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo.FIELDS.attached_resource)` is the child of policies[i+1]'s `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo.FIELDS.attached_resource)`, if policies[i+1] exists.  
  
## PolicyInfo

The IAM policy and its attached resource.

JSON representation  
---  
      
    
    {
      "attachedResource": string,
      "policy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy))
      }
    }  
  
Fields  
---  
`attachedResource` |  `string` The full resource name the `[policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo.FIELDS.policy)` is directly attached to.  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy)`)` The IAM policy that's directly attached to the `[attachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet#PolicyInfo.FIELDS.attached_resource)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
