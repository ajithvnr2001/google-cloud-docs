---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove/
title: Method: analyzeMove \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:03.069461+00:00
---

# Method: analyzeMove  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: analyzeMove Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * AnalysisView
  * MoveAnalysis
    * JSON representation
  * MoveAnalysisResult
    * JSON representation
  * MoveImpact
    * JSON representation
  * Try it!



Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user's permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{resource=*/*}:analyzeMove`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345").  
  
### Query parameters

Parameters  
---  
`destinationParent` |  `string` Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified destination parent. This can only be a folder number (such as "folders/123") or an organization number (such as "organizations/123").  
`view` |  `enum (`[AnalysisView](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#AnalysisView)`)` Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL.  
  
### Request body

The request body must be empty.

### Response body

The response message for resource move analysis.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "moveAnalysis": [
        {
          object ([MoveAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveAnalysis))
        }
      ]
    }  
  
Fields  
---  
`moveAnalysis[]` |  `object (`[MoveAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveAnalysis)`)` The list of analyses returned from performing the intended resource move analysis. The analysis is grouped by different Google Cloud services.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AnalysisView

View enum for supporting partial analysis responses.

Enums  
---  
`ANALYSIS_VIEW_UNSPECIFIED` | The default/unset value. The API will default to the FULL view.  
`FULL` | Full analysis including all level of impacts of the specified resource move.  
`BASIC` | Basic analysis only including blockers which will prevent the specified resource move at runtime.  
  
## MoveAnalysis

A message to group the analysis information.

JSON representation  
---  
      
    
    {
      "displayName": string,
    
      // Union field result can be only one of the following:
      "analysis": {
        object ([MoveAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveAnalysisResult))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation#Status))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`displayName` |  `string` The user friendly display name of the analysis. E.g. IAM, organization policy etc.  
Union field `result`.`result` can be only one of the following:  
`analysis` |  `object (`[MoveAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveAnalysisResult)`)` Analysis result of moving the target resource.  
`error` |  `object (`[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation#Status)`)` Description of error encountered when performing the analysis.  
  
## MoveAnalysisResult

An analysis result including blockers and warnings.

JSON representation  
---  
      
    
    {
      "blockers": [
        {
          object ([MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveImpact))
        }
      ],
      "warnings": [
        {
          object ([MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveImpact))
        }
      ]
    }  
  
Fields  
---  
`blockers[]` |  `object (`[MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveImpact)`)` Blocking information that would prevent the target resource from moving to the specified destination at runtime.  
`warnings[]` |  `object (`[MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove#MoveImpact)`)` Warning information indicating that moving the target resource to the specified destination might be unsafe. This can include important policy information and configuration changes, but will not block moves at runtime.  
  
## MoveImpact

A message to group impacts of moving the target resource.

JSON representation  
---  
      
    
    {
      "detail": string
    }  
  
Fields  
---  
`detail` |  `string` User friendly impact detail in a free form message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
