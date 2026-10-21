---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelResult/
title: VisionEmbeddingModelResult \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:53:22.403152+00:00
---

# VisionEmbeddingModelResult  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VisionEmbeddingModelResult Stay organized with collections  Save and categorize content based on your preferences. 

The prediction result for a large vision model embedding request. An embedding is a vectorized representation of data such as image, text or video. The embeddings produced by this model can be used for tasks such as image retrieval, similarity comparison, and classification. The embedding vectors have 1024 dimensions.

Fields  
  
`imageEmbedding` `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` The embedding generated from the input image. This field is populated if the prediction request contained an image. | `textEmbedding` `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` The embedding generated from the input text. This field is populated if the prediction request contained text. | `videoEmbeddings[]` `object (`[VideoEmbedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelResult#VideoEmbedding)`)` The embeddings generated from the input video. This field is populated if the prediction request contained a video. The video is divided into 1-second segments, and an embedding is generated for each segment. | JSON representation  
---  
      
    
    {
      "imageEmbedding": array,
      "textEmbedding": array,
      "videoEmbeddings": [
        {
          object ([VideoEmbedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelResult#VideoEmbedding))
        }
      ]
    }  
  
## VideoEmbedding

Contains embedding data for a specific time segment of a video.

Fields  
  
`startOffsetSec` `integer` The start time of the video segment that this embedding represents, measured in seconds from the beginning of the video. | `endOffsetSec` `integer` The end time of the video segment that this embedding represents, measured in seconds from the beginning of the video. | `embedding` `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` The 1024-dimension embedding vector for this video segment. | JSON representation  
---  
      
    
    {
      "startOffsetSec": integer,
      "endOffsetSec": integer,
      "embedding": array
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
