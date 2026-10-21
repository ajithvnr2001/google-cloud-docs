---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFindingRevision/
title: IntelligenceFindingRevision \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:59.618005+00:00
---

# IntelligenceFindingRevision  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFindingRevision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IntelligenceFindingRevision Stay organized with collections  Save and categorize content based on your preferences. 

An `IntelligenceFindingRevision` represents a specific revision of an `[IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding)` resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshot": {
        object ([IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding))
      },
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of `IntelligenceFindingRevision`.  
Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`snapshot` |  `object (`[IntelligenceFinding](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding)`)` Output only. The snapshot of the `IntelligenceFinding` at the time the revision was created. This field contains the full finding details as they existed for the revision.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the revision was created.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
