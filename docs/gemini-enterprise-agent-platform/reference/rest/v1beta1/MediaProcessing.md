---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/MediaProcessing/
title: MediaProcessing \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:34:54.227449+00:00
---

# MediaProcessing  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/MediaProcessing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  MediaProcessing Stay organized with collections  Save and categorize content based on your preferences. 

Fields  
  
`type` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`static` `object (`[StaticMediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/MediaProcessing#StaticMediaProcessing)`)` End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // type
      "static": {
        object ([StaticMediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/MediaProcessing#StaticMediaProcessing))
      }
      // Union type
    }  
  
## StaticMediaProcessing

Fields  
  
`startOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Segment start time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "10.5s". Must be non-negative.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `endOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Segment end time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "30s". Must be non-negative and greater than `startOffset` if `startOffset` is set.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `fps` `number` Optional. Video frame-rate sampling density. | JSON representation  
---  
      
    
    {
      "startOffset": string,
      "endOffset": string,
      "fps": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
