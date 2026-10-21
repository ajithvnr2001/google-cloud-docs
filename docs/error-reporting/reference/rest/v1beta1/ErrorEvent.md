---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorEvent/
title: ErrorEvent \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:41.226541+00:00
---

# ErrorEvent  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  ErrorEvent Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



An error event which is returned by the Error Reporting system.

JSON representation  
---  
      
    
    {
      "eventTime": string,
      "serviceContext": {
        object ([ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext))
      },
      "message": string,
      "context": {
        object ([ErrorContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext))
      }
    }  
  
Fields  
---  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the event occurred as provided in the error report. If the report did not contain a timestamp, the time the error was received by the Error Reporting system is used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceContext` |  `object (`[ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext)`)` The `ServiceContext` for which this error was reported.  
`message` |  `string` The stack trace that was reported or logged by the service.  
`context` |  `object (`[ErrorContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext)`)` Data about the context in which the error occurred.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-12 UTC."],[],[]] 
