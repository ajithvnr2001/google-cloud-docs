---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement/
title: Measurement \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:10:36.493294+00:00
---

# Measurement  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Measurement Stay organized with collections  Save and categorize content based on your preferences. 

A message representing a Measurement of a Trial. A Measurement contains the Metrics got by executing a Trial using suggested hyperparameter values.

Fields  
  
`elapsedDuration` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. time that the Trial has been running at the point of this Measurement.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `stepCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of steps the machine learning model has been trained for. Must be non-negative. | `metrics[]` `object (`[Metric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement#Metric)`)` Output only. A list of metrics got by evaluating the objective functions using suggested Parameter values. | JSON representation  
---  
      
    
    {
      "elapsedDuration": string,
      "stepCount": string,
      "metrics": [
        {
          object ([Metric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement#Metric))
        }
      ]
    }  
  
## Metric

A message representing a metric in the measurement.

Fields  
  
`metricId` `string` Output only. The id of the Metric. The Metric should be defined in `[StudySpec's Metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/StudySpec#FIELDS.metrics)`. | `value` `number` Output only. The value for this metric. | JSON representation  
---  
      
    
    {
      "metricId": string,
      "value": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
