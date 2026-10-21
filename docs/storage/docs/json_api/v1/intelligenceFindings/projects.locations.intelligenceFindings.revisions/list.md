---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings.revisions/list/
title: Method: projects.locations.intelligenceFindings.revisions.list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:22.310908+00:00
---

# Method: projects.locations.intelligenceFindings.revisions.list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.intelligenceFindings.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists all the revisions of an `[IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding)` resource.

## REST format
    
    
    GET /v2/{parent=projects/*/locations/*/intelligenceFindings/*}/revisions

## HTTP body

The HTTP request has no request body.

## Query parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the `IntelligenceFindingRevision` resource.   
Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`pageSize` |  `integer` Optional. The maximum number of `IntelligenceFindingRevision` resources to return. The maximum value is `100`; values above `100` will be coerced to `100`. The default value is `100`.   
`pageToken` |  `string` Optional. A page token, received from a previous `ListIntelligenceFindingRevisions` call. Provide this to retrieve the subsequent page.   
  
## Response

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "intelligenceFindingRevisions": [
        {
          object ([IntelligenceFindingRevision](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFindingRevision))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`intelligenceFindingRevisions[]` |  `object (`[IntelligenceFindingRevision](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFindingRevision)`)` The `IntelligenceFindingRevision` resources from the specified project.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page.  
  
## Authorization

Requires the following Google IAM permission on the specified resource:

  * `storage.buckets.viewIntelligenceDetails`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
