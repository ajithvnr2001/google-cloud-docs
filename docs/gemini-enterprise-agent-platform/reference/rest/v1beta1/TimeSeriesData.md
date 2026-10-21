---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesData/
title: TimeSeriesData \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:13:23.588121+00:00
---

# TimeSeriesData  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TimeSeriesData Stay organized with collections  Save and categorize content based on your preferences. 

All the data stored in a TensorboardTimeSeries.

Fields  
  
`tensorboardTimeSeriesId` `string` Required. The id of the TensorboardTimeSeries, which will become the final component of the TensorboardTimeSeries' resource name | `valueType` `enum (`[ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries#ValueType)`)` Required. Immutable. The value type of this time series. All the values in this time series data must match this value type. | `values[]` `object (`[TimeSeriesDataPoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesDataPoint)`)` Required. data points in this time series. | JSON representation  
---  
      
    
    {
      "tensorboardTimeSeriesId": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tensorboards.experiments.runs.timeSeries#ValueType)),
      "values": [
        {
          object ([TimeSeriesDataPoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TimeSeriesDataPoint))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
