---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold/
title: PutObjectHold \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:16.737328+00:00
---

# PutObjectHold  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  PutObjectHold Stay organized with collections  Save and categorize content based on your preferences. 

Describes options to update object hold.

JSON representation  
---  
      
    
    {
      "temporaryHold": enum ([HoldStatus](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold#HoldStatus)),
      "eventBasedHold": enum ([HoldStatus](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold#HoldStatus))
    }  
  
Fields  
---  
`temporaryHold` |  `enum (`[HoldStatus](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold#HoldStatus)`)` Required. Updates object temporary holds state. When object temporary hold is set, object can't be deleted or replaced.  
`eventBasedHold` |  `enum (`[HoldStatus](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutObjectHold#HoldStatus)`)` Required. Updates object event based holds state. When object event based hold is set, object can't be deleted or replaced. Resets object's time in the bucket for the purposes of the retention period.  
  
## HoldStatus

Describes the status of the hold.

Enums  
---  
`HOLD_STATUS_UNSPECIFIED` | Default value, Object hold status isn't changed.  
`SET` | Places the hold.  
`UNSET` | Releases the hold.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
