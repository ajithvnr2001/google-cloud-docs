---
url: https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/AnnotateVideoProgress/
title: AnnotateVideoProgress \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:22.925927+00:00
---

# AnnotateVideoProgress  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/AnnotateVideoProgress/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/video-intelligence/docs/apis)



Send feedback 

#  AnnotateVideoProgress Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * VideoAnnotationProgress
    * JSON representation



Video annotation progress. Included in the `metadata` field of the `Operation` returned by the `operations.get` call of the `google::longrunning::Operations` service.

JSON representation  
---  
      
    
    {
      "annotationProgress": [
        {
          object ([VideoAnnotationProgress](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/AnnotateVideoProgress#VideoAnnotationProgress))
        }
      ]
    }  
  
Fields  
---  
`annotationProgress[]` |  `object (`[VideoAnnotationProgress](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/AnnotateVideoProgress#VideoAnnotationProgress)`)` Progress metadata for all videos specified in `AnnotateVideoRequest`.   
  
## VideoAnnotationProgress

Annotation progress for a single video.

JSON representation  
---  
      
    
    {
      "inputUri": string,
      "progressPercent": number,
      "startTime": string,
      "updateTime": string,
      "feature": enum ([Feature](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#Feature)),
      "segment": {
        object ([VideoSegment](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#VideoSegment))
      }
    }  
  
Fields  
---  
`inputUri` |  `string` Video file location in [Google Cloud Storage](https://cloud.google.com/storage/).   
`progressPercent` |  `number` Approximate percentage processed thus far. Guaranteed to be 100 when fully processed.   
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Time when the request was received.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Time of the most recent update.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`feature` |  `enum (`[Feature](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#Feature)`)` Specifies which feature is being tracked if the request contains more than one features.   
`segment` |  `object (`[VideoSegment](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#VideoSegment)`)` Specifies which segment is being tracked if the request contains more than one segments.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
