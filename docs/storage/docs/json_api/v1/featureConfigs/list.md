---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/list/
title: FeatureConfigs: list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:24.326486+00:00
---

# FeatureConfigs: list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  FeatureConfigs: list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of `FeatureConfig` resources in the specified project.

## Required permissions

To use this method, the authenticated user must have the `storage.featureConfigs.list` IAM permission.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/v2/projects/project/locations/global/featureConfigs

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`project` | `string` | The project ID or number for which to list feature configurations.  
**Query parameters**  
`filter` | `string` | _Optional._ A filter expression to apply to the results. Supports filtering by `type`. Example: `type="AUTO_ANNOTATE"`.  
`orderBy` | `string` | _Optional._ Sort order for the results.  
`pageSize` | `integer` | _Optional._ Maximum number of results to return in a single response. The service may return fewer than this value. If unspecified, at most 100 results are returned. The maximum value is 100; values above 100 are coerced to 100.  
`pageToken` | `string` | _Optional._ A page token received from a previous `list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `list` must match the call that provided the page token.  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a list of [FeatureConfig resources](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs#resource) in the following structure:
    
    
    {
      "featureConfigs": [
        [FeatureConfig resource](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs#resource)
      ],
      "nextPageToken": string
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
