---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries/
title: Method: timeSeries.exportTensorboardTimeSeries \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:22.826605+00:00
---

# Method: timeSeries.exportTensorboardTimeSeries  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: timeSeries.exportTensorboardTimeSeries Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tensorboards.experiments.runs.timeSeries.exportTensorboardTimeSeries

Exports a TensorboardTimeSeries' data. data is returned in paginated responses.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{tensorboardTimeSeries}:exportTensorboardTimeSeries`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`tensorboardTimeSeries` `string` Required. The resource name of the TensorboardTimeSeries to export data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{timeSeries}`

### Request body

The request body contains data with the following structure: | Fields  
  
`filter` `string` Exports the TensorboardTimeSeries' data that match the filter expression. | `pageSize` `integer` The maximum number of data points to return per page. The default pageSize is 1000. Values must be between 1 and 10000. Values above 10000 are coerced to 10000. | `pageToken` `string` A page token, received from a previous `[timeSeries.exportTensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries#google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[timeSeries.exportTensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries#google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData)` must match the call that provided the page token. | `orderBy` `string` Field to use to sort the TensorboardTimeSeries' data. By default, TensorboardTimeSeries' data is returned in a pseudo random order.

### Response body

Response message for `[TensorboardService.ExportTensorboardTimeSeriesData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries#google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData)`. If successful, the response body contains data with the following structure: | Fields  
  
`timeSeriesDataPoints[]` `object (`[TimeSeriesDataPoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesDataPoint)`)` The returned time series data points. | `nextPageToken` `string` A token, which can be sent as `[pageToken](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries#body.request_body.FIELDS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "timeSeriesDataPoints": [
        {
          object ([TimeSeriesDataPoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesDataPoint))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `tensorboardTimeSeries` resource:

  * `aiplatform.tensorboardTimeSeries.read`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
