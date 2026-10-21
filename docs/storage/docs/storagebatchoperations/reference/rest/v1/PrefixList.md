---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList/
title: PrefixList \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:15:15.928434+00:00
---

# PrefixList  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PrefixList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  PrefixList Stay organized with collections  Save and categorize content based on your preferences. 

Describes prefixes of objects to be transformed.

JSON representation  
---  
      
    
    {
      "includedObjectPrefixes": [
        string
      ]
    }  
  
Fields  
---  
`includedObjectPrefixes[]` |  `string` Optional. Specify one or more object prefixes. For example:

  * To match one object, use a single prefix, `prefix1`.
  * To match multiple objects, use comma-separated prefixes, `prefix1, prefix2`.
  * To match all objects, use an empty prefix, `''`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
