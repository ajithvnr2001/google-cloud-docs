---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings/get/
title: Method: projects.locations.intelligenceFindings.get \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:21.880998+00:00
---

# Method: projects.locations.intelligenceFindings.get  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/projects.locations.intelligenceFindings/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.intelligenceFindings.get Stay organized with collections  Save and categorize content based on your preferences. 

Gets a specific `[IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding)` resource.

## REST format
    
    
    GET /v2/{name=projects/project/locations/location/intelligenceFindings/intelligence_finding}

## HTTP body

The HTTP request has no request body.

## Query parameters

Parameters  
---  
`name` |  `string` Required. The name of the `IntelligenceFinding` resource.  
Format: `projects/project/locations/location/intelligenceFindings/intelligence_finding`  
  
## Response

If successful, the response body contains an instance of `[IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding)` resource.

## Authorization

Requires the following Google IAM permission on the specified resource:

  * `storage.buckets.viewIntelligenceDetails`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
