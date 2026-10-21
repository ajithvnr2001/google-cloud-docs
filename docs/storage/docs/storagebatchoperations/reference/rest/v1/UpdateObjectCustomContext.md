---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext/
title: UpdateObjectCustomContext \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:44:52.942004+00:00
---

# UpdateObjectCustomContext  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  UpdateObjectCustomContext Stay organized with collections  Save and categorize content based on your preferences. 

Describes options to update object custom contexts.

JSON representation  
---  
      
    
    {
    
      // Union field action can be only one of the following:
      "customContextUpdates": {
        object ([CustomContextUpdates](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext#CustomContextUpdates))
      },
      "clearAll": boolean
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `action`. One of the actions must be set. `action` can be only one of the following:  
`customContextUpdates` |  `object (`[CustomContextUpdates](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext#CustomContextUpdates)`)` A collection of updates to apply to specific custom contexts. Use this to add, update or delete individual contexts by key.  
`clearAll` |  `boolean` If set, must be set to true and all existing object custom contexts are deleted.  
  
## CustomContextUpdates

Describes a collection of updates to apply to custom contexts identified by key.

JSON representation  
---  
      
    
    {
      "updates": {
        string: {
          object ([ObjectCustomContextPayload](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext#ObjectCustomContextPayload))
        },
        ...
      },
      "keysToClear": [
        string
      ]
    }  
  
Fields  
---  
`updates` |  `map (key: string, value: object (`[ObjectCustomContextPayload](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/UpdateObjectCustomContext#ObjectCustomContextPayload)`))` Optional. Insert or update the existing custom contexts.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`keysToClear[]` |  `string` Optional. Custom contexts to clear by key. A key can't be present in both `updates` and `keysToClear`.  
  
## ObjectCustomContextPayload

Describes the payload of a user-defined object custom context.

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` The value of the object custom context. If set, `value` can't be an empty string because it is a required field in custom context. If unset, `value` is ignored and no changes are made to the `value` field of the custom context payload.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
