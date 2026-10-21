---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.datasetVersions/list/
title: Method: datasetVersions.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:10:32.244799+00:00
---

# Method: datasetVersions.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.datasetVersions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: datasetVersions.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.datasetVersions.list

Lists DatasetVersions in a Dataset.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/datasetVersions`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Dataset to list DatasetVersions from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

### Query parameters

| `filter` `string` Optional. The standard list filter. | `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. | `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. | `orderBy` `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

### Request body

The request body must be empty.

### Response body

Response message for `[DatasetService.ListDatasetVersions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.datasetVersions/list#google.cloud.aiplatform.v1beta1.DatasetService.ListDatasetVersions)`. If successful, the response body contains data with the following structure: | Fields  
  
`datasetVersions[]` `object (`[DatasetVersion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.datasetVersions#DatasetVersion)`)` A list of DatasetVersions that matches the specified filter in the request. | `nextPageToken` `string` The standard List next-page token. | JSON representation  
---  
      
    
    {
      "datasetVersions": [
        {
          object ([DatasetVersion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.datasetVersions#DatasetVersion))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
