---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets/
title: Method: analyzeOrgPolicyGovernedAssets \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:03.696144+00:00
---

# Method: analyzeOrgPolicyGovernedAssets  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: analyzeOrgPolicyGovernedAssets Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * GovernedAsset
    * JSON representation
  * GovernedResource
    * JSON representation
  * GovernedIamPolicy
    * JSON representation
  * Try it!



Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope. This RPC supports custom constraints and the following canned constraints:

  * constraints/ainotebooks.accessMode
  * constraints/ainotebooks.disableFileDownloads
  * constraints/ainotebooks.disableRootAccess
  * constraints/ainotebooks.disableTerminal
  * constraints/ainotebooks.environmentOptions
  * constraints/ainotebooks.requireAutoUpgradeSchedule
  * constraints/ainotebooks.restrictVpcNetworks
  * constraints/compute.disableGuestAttributesAccess
  * constraints/compute.disableInstanceDataAccessApis
  * constraints/compute.disableNestedVirtualization
  * constraints/compute.disableSerialPortAccess
  * constraints/compute.disableSerialPortLogging
  * constraints/compute.disableVpcExternalIpv6
  * constraints/compute.requireOsLogin
  * constraints/compute.requireShieldedVm
  * constraints/compute.restrictLoadBalancerCreationForTypes
  * constraints/compute.restrictProtocolForwardingCreationForTypes
  * constraints/compute.restrictXpnProjectLienRemoval
  * constraints/compute.setNewProjectDefaultToZonalDNSOnly
  * constraints/compute.skipDefaultNetworkCreation
  * constraints/compute.trustedImageProjects
  * constraints/compute.vmCanIpForward
  * constraints/compute.vmExternalIpAccess
  * constraints/gcp.detailedAuditLoggingMode
  * constraints/gcp.resourceLocations
  * constraints/iam.allowedPolicyMemberDomains
  * constraints/iam.automaticIamGrantsForDefaultServiceAccounts
  * constraints/iam.disableServiceAccountCreation
  * constraints/iam.disableServiceAccountKeyCreation
  * constraints/iam.disableServiceAccountKeyUpload
  * constraints/iam.restrictCrossProjectServiceAccountLienRemoval
  * constraints/iam.serviceAccountKeyExpiryHours
  * constraints/resourcemanager.accessBoundaries
  * constraints/resourcemanager.allowedExportDestinations
  * constraints/sql.restrictAuthorizedNetworks
  * constraints/sql.restrictNoncompliantDiagnosticDataAccess
  * constraints/sql.restrictNoncompliantResourceCreation
  * constraints/sql.restrictPublicIp
  * constraints/storage.publicAccessPrevention
  * constraints/storage.restrictAuthTypes
  * constraints/storage.uniformBucketLevelAccess



This RPC only returns either resources of types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) or IAM policies.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{scope=*/*}:analyzeOrgPolicyGovernedAssets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies.

  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`
  * `cloudasset.assets.analyzeOrgPolicy`

  
  
### Query parameters

Parameters  
---  
`constraint` |  `string` Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint.  
`filter` |  `string` The expression to filter `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.governed_assets)`.For governed resources, filtering is currently available for bare literal values and the following fields: * governedResource.project * governedResource.folders * consolidatedPolicy.rules.enforce When filtering by `governedResource.project` or `consolidatedPolicy.rules.enforce`, the only supported operator is `=`. When filtering by `governedResource.folders`, the supported operators are `=` and `:`. For example, filtering by `governedResource.project="projects/12345678"` will return all the governed resources under "projects/12345678", including the project itself if applicable.For governed IAM policies, filtering is currently available for bare literal values and the following fields: * governedIamPolicy.project * governedIamPolicy.folders * consolidatedPolicy.rules.enforce When filtering by `governedIamPolicy.project` or `consolidatedPolicy.rules.enforce`, the only supported operator is `=`. When filtering by `governedIamPolicy.folders`, the supported operators are `=` and `:`. For example, filtering by `governedIamPolicy.folders:"folders/12345678"` will return all the governed IAM policies under "folders/001".  
`pageToken` |  `string` The pagination token to retrieve the next page.  
`pageSize` |  `integer` The maximum number of items to return per page. If unspecified, `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.governed_assets)` will contain 100 items with a maximum of 200.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[AssetService.AnalyzeOrgPolicyGovernedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "governedAssets": [
        {
          object ([GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset))
        }
      ],
      "constraint": {
        object ([AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint))
      },
      "nextPageToken": string
    }  
  
Fields  
---  
`governedAssets[]` |  `object (`[GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset)`)` The list of the analyzed governed assets.  
`constraint` |  `object (`[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicyConstraint)`)` The definition of the constraint in the request.  
`nextPageToken` |  `string` The page token to fetch the next page for `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.governed_assets)`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## GovernedAsset

Represents a Google Cloud asset(resource or IAM policy) governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.QUERY_PARAMETERS.constraint)`.

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
    
      // Union field governed_asset can be only one of the following:
      "governedResource": {
        object ([GovernedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedResource))
      },
      "governedIamPolicy": {
        object ([GovernedIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedIamPolicy))
      }
      // End of list of possible types for union field governed_asset.
    }  
  
Fields  
---  
`consolidatedPolicy` |  `object (`[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy)`)` The consolidated policy for the analyzed asset. The consolidated policy is computed by merging and evaluating `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.policy_bundle](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset.FIELDS.policy_bundle)`. The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).  
`policyBundle[]` |  `object (`[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy)`)` The ordered list of all organization policies from the `[consolidatedPolicy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#FIELDS.attached_resource)` to the scope specified in the request.If the constraint is defined with default policy, it will also appear in the list.  
Union field `governed_asset`.`governed_asset` can be only one of the following:  
`governedResource` |  `object (`[GovernedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedResource)`)` A Google Cloud resource governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.QUERY_PARAMETERS.constraint)`.  
`governedIamPolicy` |  `object (`[GovernedIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedIamPolicy)`)` An IAM policy governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.QUERY_PARAMETERS.constraint)`.  
  
## GovernedResource

The Google Cloud resources governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.QUERY_PARAMETERS.constraint)`.

JSON representation  
---  
      
    
    {
      "fullResourceName": string,
      "parent": string,
      "project": string,
      "folders": [
        string
      ],
      "organization": string,
      "assetType": string,
      "effectiveTags": [
        {
          object ([EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails))
        }
      ]
    }  
  
Fields  
---  
`fullResourceName` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the Google Cloud resource.  
`parent` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedResource.FIELDS.full_resource_name)`.  
`project` |  `string` The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project.  
`folders[]` |  `string` The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization.  
`assetType` |  `string` The asset type of the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedResource.FIELDS.full_resource_name)` Example: `cloudresourcemanager.googleapis.com/Project` See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types.  
`effectiveTags[]` |  `object (`[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails)`)` The effective tags on this resource.  
  
## GovernedIamPolicy

The IAM policies governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#body.QUERY_PARAMETERS.constraint)`.

JSON representation  
---  
      
    
    {
      "attachedResource": string,
      "policy": {
        object ([Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy))
      },
      "project": string,
      "folders": [
        string
      ],
      "organization": string,
      "assetType": string
    }  
  
Fields  
---  
`attachedResource` |  `string` The full resource name of the resource on which this IAM policy is set. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Policy)`)` The IAM policy directly set on the given resource.  
`project` |  `string` The project that this IAM policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the IAM policy belongs to a project.  
`folders[]` |  `string` The folder(s) that this IAM policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this IAM policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to an organization.  
`assetType` |  `string` The asset type of the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedIamPolicy.FIELDS.attached_resource)`. Example: `cloudresourcemanager.googleapis.com/Project` See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
