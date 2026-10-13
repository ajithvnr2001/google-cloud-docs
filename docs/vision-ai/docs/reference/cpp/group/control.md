---
url: https://docs.cloud.google.com/vision-ai/docs/reference/cpp/group/control/
title: Control \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:14.152754+00:00
---

# Control  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/cpp/group/control/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control

Constructs for controlling service resources. 

## Summary

### Functions  
  
---  
`CreateStream(const ServiceConnectionOptions & options, absl::string_view stream_id)` |  `absl::Status` Creates a new stream resource with id `stream_id`.   
`DeleteStream(const ServiceConnectionOptions & options, absl::string_view stream_id)` |  `absl::Status` Deletes the stream with id `stream_id`.   
  
## Functions

### CreateStream
    
    
    absl::Status CreateStream(
      const ServiceConnectionOptions & options,
      absl::string_view stream_id
    )

Creates a new stream resource with id `stream_id`. 

Details | Parameters |  |  `option` |  Connection options.   
---|---  
`stream_id` |  The id of the stream to connect to.   
**Returns** |  OK on success. Otherwise the error indicating the cause.   
  
### DeleteStream
    
    
    absl::Status DeleteStream(
      const ServiceConnectionOptions & options,
      absl::string_view stream_id
    )

Deletes the stream with id `stream_id`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
