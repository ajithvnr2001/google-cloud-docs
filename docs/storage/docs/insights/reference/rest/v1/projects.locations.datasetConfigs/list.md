---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/list/
title: Method: projects.locations.datasetConfigs.list \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:36.980678+00:00
---

# Method: projects.locations.datasetConfigs.list  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.datasetConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the dataset configurations in a given project for a given location.

### HTTP request

`GET https://storageinsights.googleapis.com/v1/{parent=projects/*/locations/*}/datasetConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListDatasetConfigsRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. Server might return fewer items than requested. If unspecified, server picks an appropriate default.  
`pageToken` |  `string` A token identifying a page of results the server should return.  
`filter` |  `string` Filtering results  
`orderBy` |  `string` Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Response message for `[`datasetConfigs.list`](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/list#google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "datasetConfigs": [
        {
          object ([DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#DatasetConfig))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`datasetConfigs[]` |  `object (`[DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#DatasetConfig)`)` The list of `DatasetConfigs`  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `storageinsights.datasetConfigs.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
