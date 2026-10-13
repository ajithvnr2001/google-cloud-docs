---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/InterceptLocation/
title: InterceptLocation \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:44.628781+00:00
---

# InterceptLocation  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/InterceptLocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  InterceptLocation Stay organized with collections  Save and categorize content based on your preferences. 

Details about intercept in a specific cloud location.

JSON representation  
---  
      
    
    {
      "location": string,
      "state": enum ([State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/InterceptLocation#State))
    }  
  
Fields  
---  
`location` |  `string` Output only. The cloud location, e.g. "us-central1-a" or "asia-south1".  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/InterceptLocation#State)`)` Output only. The current state of the association in this location.  
  
## State

The current state of a resource in the location.

Enums  
---  
`STATE_UNSPECIFIED` | State not set (this is not a valid state).  
`ACTIVE` | The resource is ready and in sync in the location.  
`OUT_OF_SYNC` | The resource is out of sync in the location. In most cases, this is a result of a transient issue within the system (e.g. an inaccessible location) and the system is expected to recover automatically.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
