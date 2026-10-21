---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContextFilter/
title: ServiceContextFilter \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:41.315015+00:00
---

# ServiceContextFilter  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContextFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  ServiceContextFilter Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Specifies criteria for filtering a subset of service contexts. The fields in the filter correspond to the fields in `ServiceContext`. Only exact, case-sensitive matches are supported. If a field is unset or empty, it matches arbitrary values.

JSON representation  
---  
      
    
    {
      "service": string,
      "version": string,
      "resourceType": string
    }  
  
Fields  
---  
`service` |  `string` Optional. The exact value to match against [`ServiceContext.service`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.service).  
`version` |  `string` Optional. The exact value to match against [`ServiceContext.version`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.version).  
`resourceType` |  `string` Optional. The exact value to match against [`ServiceContext.resource_type`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext#FIELDS.resource_type).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
