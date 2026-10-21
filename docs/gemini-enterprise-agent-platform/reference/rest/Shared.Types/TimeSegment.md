---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TimeSegment/
title: TimeSegment \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:47:15.446909+00:00
---

# TimeSegment  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TimeSegment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TimeSegment Stay organized with collections  Save and categorize content based on your preferences. 

A time period inside of a DataItem that has a time dimension (e.g. video).

Fields  
  
`startTimeOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Start of the time segment (inclusive), represented as the duration since the start of the DataItem.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `endTimeOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` End of the time segment (exclusive), represented as the duration since the start of the DataItem.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | JSON representation  
---  
      
    
    {
      "startTimeOffset": string,
      "endTimeOffset": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
