---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters/
title: Counters \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:11:30.849026+00:00
---

# Counters  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/Counters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Counters Stay organized with collections  Save and categorize content based on your preferences. 

Describes details about the progress of the job.

JSON representation  
---  
      
    
    {
      "totalObjectCount": string,
      "succeededObjectCount": string,
      "failedObjectCount": string,
      "totalBytesFound": string,
      "objectCustomContextsCreated": string,
      "objectCustomContextsDeleted": string,
      "objectCustomContextsUpdated": string,
      "totalBytesTransformed": string
    }  
  
Fields  
---  
`totalObjectCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of objects listed.  
`succeededObjectCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of objects completed.  
`failedObjectCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of objects that failed due to user errors or service errors.  
`totalBytesFound` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of bytes found from source. This field is only populated for jobs with a prefix list object configuration.  
`objectCustomContextsCreated` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of object custom contexts created. This field is only populated for jobs with the UpdateObjectCustomContext transformation.  
`objectCustomContextsDeleted` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of object custom contexts deleted. This field is only populated for jobs with the UpdateObjectCustomContext transformation.  
`objectCustomContextsUpdated` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of object custom contexts updated. This counter tracks custom contexts where the key already existed, but the payload was modified. This field is only populated for jobs with the UpdateObjectCustomContext transformation.  
`totalBytesTransformed` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of bytes affected by the transformation. For example, this counts bytes deleted for `DeleteObject` operations and bytes rewritten for `RewriteObject` operations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
