---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AudioResponseFormat/
title: AudioResponseFormat \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:38:06.477367+00:00
---

# AudioResponseFormat  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AudioResponseFormat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  AudioResponseFormat Stay organized with collections  Save and categorize content based on your preferences. 

Configuration for audio-specific output formatting.

Fields  
  
`delivery` `enum (`[DeliveryMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/DeliveryMode)`)` Optional. Delivery mode for the generated content. | `mimeType` `enum (`[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MimeType)`)` Optional. The MIME type of the audio output. | `sampleRate` `integer` Optional. Sample rate for the generated audio in Hertz. | `bitRate` `integer` Optional. Bit rate in bits per second (bps). Only applicable for compressed formats (MP3, Opus). | JSON representation  
---  
      
    
    {
      "delivery": enum ([DeliveryMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/DeliveryMode)),
      "mimeType": enum ([MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MimeType)),
      "sampleRate": integer,
      "bitRate": integer
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
