---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/Principal/
title: Principal \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:24.348366+00:00
---

# Principal  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/Principal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  Principal Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Users/Service accounts which have access for DNS binding on the intranet VPC corresponding to the consumer project. Principal can be a user or a service account. For example: For specifying user `user@example.com` use `{"user": "user@example.com"}` and for specifying service account `service-account@gserviceaccount.com` use `{"serviceAccount": "service-account@gserviceaccount.com"}`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "user": string,
      "serviceAccount": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The consumer provided user/service account which needs to be granted permission to DNS bind with the intranet VPC corresponding to the consumer project. Principal can be a user or a service account. For example: For specifying user `user@example.com` use `{"user": "user@example.com"}` and for specifying service account `service-account@gserviceaccount.com` use `{"serviceAccount": "service-account@gserviceaccount.com"}`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`user` |  `string` The user who needs to be granted permission.  
`serviceAccount` |  `string` The service account which needs to be granted the permission.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-11 UTC."],[],[]] 
