---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings/summarize/
title: Method: projects.locations.intelligenceFindings.summarize \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:22.175583+00:00
---

# Method: projects.locations.intelligenceFindings.summarize  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings/summarize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.intelligenceFindings.summarize Stay organized with collections  Save and categorize content based on your preferences. 

Summarizes intelligence findings for an organization, a folder, or a project.

## REST format
    
    
    GET /v2/{parent=projects/PROJECT_ID/locations/LOCATION}/intelligenceFindings:summarize
    
    
    GET /v2/{parent=folders/FOLDER_ID/locations/LOCATION}/intelligenceFindings:summarize
    
    
    GET /v2/{parent=organizations/ORGANIZATION_ID/locations/LOCATION}/intelligenceFindings:summarize

## HTTP body

The HTTP request has no request body.

## Query parameters

Parameters  
---  
`parent` |  `string` Required. The scope for which to summarize the findings.  
Format: 

  * `organizations/ORGANIZATION_ID/locations/LOCATION`
  * `folders/FOLDER_ID/locations/LOCATION`
  * `projects/PROJECT_ID/locations/LOCATION`

  
`resourceScope` |  `enum (`ResourceScope`)` Optional. Determines the granularity of the findings when the `parent` is an organization or folder. 

  * `PARENT` (or not set): The API returns a single summary for each insight type, aggregated across the entire `parent` scope.
  * `PROJECT`: The API returns a separate summary for each insight type for every project within the `parent` scope.

The only supported values are `PARENT` and `PROJECT`. If you don't specify a value, the API defaults to the `PARENT` behavior.   
`filter` |  `string` Optional. The filter expression, following AIP-160. Supports filtering by FindingType.   
`pageSize` |  `integer` Optional. The maximum number of findings to return. The maximum value is `100`; values above `100` are coerced to `100`. The default value is `100`.   
`pageToken` |  `string` Optional. A page token, received from a previous `SummarizeIntelligenceFindings` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `SummarizeIntelligenceFindings` must match the call that provided the page token.   
  
## ResourceScope

Describes the available resource scopes for summarizing findings.

Enums  
---  
`RESOURCE_SCOPE_UNSPECIFIED` | The default behavior. Defaults to `PARENT` behavior.  
`PARENT` | The API aggregates summaries at the level of the `parent` resource.  
`PROJECT` | The API breaks down summaries by each project within the `parent` scope.  
  
## Response

If the request is successful, the response body contains the following data structure:

JSON representation  
---  
      
    
    {
      "findingSummaries": [
        {
          object ([FindingSummary](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/FindingSummary))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`findingSummaries[]` |  `object (`[FindingSummary](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/FindingSummary)`)` The list of `FindingSummary` summaries.  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `pageToken` field in the subsequent call to `SummarizeIntelligenceFindings`.  
  
## Authorization

Requires the following Google IAM permission on the specified resource:

  * `storage.buckets.viewIntelligenceDetails`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
