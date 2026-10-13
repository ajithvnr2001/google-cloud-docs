---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove/
title: Method: organizations.locations.workloads.analyzeWorkloadMove \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:26.160974+00:00
---

# Method: organizations.locations.workloads.analyzeWorkloadMove  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.analyzeWorkloadMove Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AssetMoveAnalysis
    * JSON representation
  * MoveAnalysisGroup
    * JSON representation
  * MoveAnalysisResult
    * JSON representation
  * MoveImpact
    * JSON representation



Analyzes a hypothetical move of a source resource to a target workload to surface compliance risks. The analysis is best effort and is not guaranteed to be exhaustive.

### HTTP request

`GET https://{endpoint}/v1beta1/{target=organizations/*/locations/*/workloads/*}:analyzeWorkloadMove`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`target` |  `string` Required. The resource ID of the folder-based destination workload. This workload is where the source resource will hypothetically be moved to. Specify the workload's relative resource name, formatted as: "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}" For example: "organizations/123/locations/us-east1/workloads/assured-workload-2"  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Page size. If a value is not specified, the default value of 10 is used. The maximum value is 50.  
`pageToken` |  `string` Optional. The page token from the previous response. It needs to be passed in the second and following requests.  
`assetTypes[]` |  `string` Optional. List of asset types to be analyzed, including and under the source resource. If empty, all assets are analyzed. The complete list of asset types is available [here](https://cloud.google.com/asset-inventory/docs/supported-asset-types).  
Union parameter `sourceResource`. The resource type to be moved to the destination workload. `sourceResource` can be only one of the following:  
`project` |  `string` The source type is a project. Specify the project's relative resource name, formatted as either a project number or a project ID: "projects/{PROJECT_NUMBER}" or "projects/{PROJECT_ID}" For example: "projects/951040570662" when specifying a project number, or "projects/my-project-123" when specifying a project ID.  
  
### Request body

The request body must be empty.

### Response body

Response containing the analysis results for the hypothetical resource move.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "assetMoveAnalyses": [
        {
          object ([AssetMoveAnalysis](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#AssetMoveAnalysis))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`assetMoveAnalyses[]` |  `object (`[AssetMoveAnalysis](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#AssetMoveAnalysis)`)` List of analysis results for each asset in scope.  
`nextPageToken` |  `string` The next page token. Is empty if the last page is reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `target` resource:

  * `assuredworkloads.workload.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AssetMoveAnalysis

Represents move analysis results for an asset.

JSON representation  
---  
      
    
    {
      "asset": string,
      "assetType": string,
      "analysisGroups": [
        {
          object ([MoveAnalysisGroup](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveAnalysisGroup))
        }
      ]
    }  
  
Fields  
---  
`asset` |  `string` The full resource name of the asset being analyzed. Example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1  
`assetType` |  `string` Type of the asset being analyzed. Possible values will be among the ones listed [here](https://cloud.google.com/asset-inventory/docs/supported-asset-types).  
`analysisGroups[]` |  `object (`[MoveAnalysisGroup](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveAnalysisGroup)`)` List of eligible analyses performed for the asset.  
  
## MoveAnalysisGroup

Represents a logical group of checks performed for an asset. If successful, the group contains the analysis result, otherwise it contains an error with the failure reason.

JSON representation  
---  
      
    
    {
      "displayName": string,
    
      // Union field result can be only one of the following:
      "analysisResult": {
        object ([MoveAnalysisResult](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveAnalysisResult))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`displayName` |  `string` Name of the analysis group.  
Union field `result`.`result` can be only one of the following:  
`analysisResult` |  `object (`[MoveAnalysisResult](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveAnalysisResult)`)` Result of a successful analysis.  
`error` |  `object (`[Status](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Error details for a failed analysis.  
  
## MoveAnalysisResult

Represents the successful move analysis results for a group.

JSON representation  
---  
      
    
    {
      "warnings": [
        {
          object ([MoveImpact](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveImpact))
        }
      ],
      "blockers": [
        {
          object ([MoveImpact](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveImpact))
        }
      ]
    }  
  
Fields  
---  
`warnings[]` |  `object (`[MoveImpact](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveImpact)`)` List of warnings. These are risks that may or may not result in compliance violations.  
`blockers[]` |  `object (`[MoveImpact](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove#MoveImpact)`)` List of blockers. If not resolved, these will result in compliance violations in the target.  
  
## MoveImpact

Represents the impact of moving the asset to the target.

JSON representation  
---  
      
    
    {
      "detail": string
    }  
  
Fields  
---  
`detail` |  `string` Explanation of the impact.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
