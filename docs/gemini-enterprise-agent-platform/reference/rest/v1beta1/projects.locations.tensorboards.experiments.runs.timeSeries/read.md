---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/read/
title: Method: timeSeries.read \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:21.658823+00:00
---

# Method: timeSeries.read  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: timeSeries.read Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tensorboards.experiments.runs.timeSeries.read

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing maxDataPoints, which can't be greater than 10k.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{tensorboardTimeSeries}:read`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`tensorboardTimeSeries` `string` Required. The resource name of the TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{timeSeries}`

### Query parameters

| `maxDataPoints` `integer` The maximum number of TensorboardTimeSeries' data to return.This value should be a positive integer. This value can be set to -1 to return all data. | `filter` `string` Reads the TensorboardTimeSeries' data that match the filter expression.

### Request body

The request body must be empty.

### Response body

Response message for `[TensorboardService.ReadTensorboardTimeSeriesData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/read#google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardTimeSeriesData)`. If successful, the response body contains data with the following structure: | Fields  
  
`timeSeriesData` `object (`[TimeSeriesData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesData)`)` The returned time series data. | JSON representation  
---  
      
    
    {
      "timeSeriesData": {
        object ([TimeSeriesData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesData))
      }
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `tensorboardTimeSeries` resource:

  * `aiplatform.tensorboardTimeSeries.read`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
