---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies/
title: Method: analyzeOrgPolicies \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:03.620997+00:00
---

# Method: analyzeOrgPolicies  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: analyzeOrgPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * OrgPolicyResult
    * JSON representation
  * Try it!



Analyzes organization policies under a scope.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{scope=*/*}:analyzeOrgPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. The organization to scope the request. Only organization policies within the scope will be analyzed.

  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.analyzeOrgPolicy`

  
  
### Query parameters

Parameters  
---  
`constraint` |  `string` Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint.  
`filter` |  `string` The expression to filter `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#body.AnalyzeOrgPoliciesResponse.FIELDS.org_policy_results)`. Filtering is currently available for bare literal values and the following fields: * consolidatedPolicy.attached_resource * consolidatedPolicy.rules.enforceWhen filtering by a specific field, the only supported operator is `=`. For example, filtering by consolidatedPolicy.attached_resource="//cloudresourcemanager.googleapis.com/folders/001" will return all the Organization Policy results attached to "folders/001".  
`pageToken` |  `string` The pagination token to retrieve the next page.  
`pageSize` |  `integer` The maximum number of items to return per page. If unspecified, `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#body.AnalyzeOrgPoliciesResponse.FIELDS.org_policy_results)` will contain 20 items with a maximum of 200.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[AssetService.AnalyzeOrgPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "orgPolicyResults": [
        {
          object ([OrgPolicyResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#OrgPolicyResult))
        }
      ],
      "constraint": {
        object ([AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint))
      },
      "nextPageToken": string
    }  
  
Fields  
---  
`orgPolicyResults[]` |  `object (`[OrgPolicyResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#OrgPolicyResult)`)` The organization policies under the `[AnalyzeOrgPoliciesRequest.scope](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#body.PATH_PARAMETERS.scope)` with the `[AnalyzeOrgPoliciesRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#body.QUERY_PARAMETERS.constraint)`.  
`constraint` |  `object (`[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint)`)` The definition of the constraint in the request.  
`nextPageToken` |  `string` The page token to fetch the next page for `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#body.AnalyzeOrgPoliciesResponse.FIELDS.org_policy_results)`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## OrgPolicyResult

The organization policy result to the query.

JSON representation  
---  
      
    
    {
      "consolidatedPolicy": {
        object ([AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy))
      },
      "policyBundle": [
        {
          object ([AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy))
        }
      ],
      "project": string,
      "folders": [
        string
      ],
      "organization": string
    }  
  
Fields  
---  
`consolidatedPolicy` |  `object (`[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy)`)` The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating `[policyBundle](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies#OrgPolicyResult.FIELDS.policy_bundle)`. The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).  
`policyBundle[]` |  `object (`[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy)`)` The ordered list of all organization policies from the `[consolidatedPolicy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#FIELDS.attached_resource)`. to the scope specified in the request.If the constraint is defined with default policy, it will also appear in the list.  
`project` |  `string` The project that this consolidated policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the consolidated policy belongs to a project.  
`folders[]` |  `string` The folder(s) that this consolidated policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this consolidated policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
