---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HierarchyConfig/
title: HierarchyConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:27:24.561829+00:00
---

# HierarchyConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HierarchyConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  HierarchyConfig Stay organized with collections  Save and categorize content based on your preferences. 

Configuration that defines the hierarchical relationship of time series and parameters for hierarchical forecasting strategies.

Fields  
  
`groupColumns[]` `string` A list of time series attribute column names that define the time series hierarchy. Only one level of hierarchy is supported, ex. 'region' for a hierarchy of stores or 'department' for a hierarchy of products. If multiple columns are specified, time series will be grouped by their combined values, ex. ('blue', 'large') for 'color' and 'size', up to 5 columns are accepted. If no group columns are specified, all time series are considered to be part of the same group. | `groupTotalWeight` `number` The weight of the loss for predictions aggregated over time series in the same group. | `temporalTotalWeight` `number` The weight of the loss for predictions aggregated over the horizon for a single time series. | `groupTemporalTotalWeight` `number` The weight of the loss for predictions aggregated over both the horizon and time series in the same hierarchy group. | JSON representation  
---  
      
    
    {
      "groupColumns": [
        string
      ],
      "groupTotalWeight": number,
      "temporalTotalWeight": number,
      "groupTemporalTotalWeight": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
