---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/NotificationType/
title: NotificationType \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:59.104475+00:00
---

# NotificationType  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/NotificationType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  NotificationType Stay organized with collections  Save and categorize content based on your preferences. 

Enumeration of the possible notification types for requests from Scotty.

Enums  
---  
`START` | Such requests signals the start of a request containing media upload. Only the media field(s) in the inserted/updated resource are set.The response should either return an error or succeed. On success, responses don't need to contain anything.  
`PROGRESS` | Such requests signals that the upload has progressed and that the backend might want to access the media file specified in relevant fields in the resource. Only the media field(s) in the inserted/updated resource are set.The response should either return an error or succeed. On success, responses don't need to contain anything.  
`END` | Such requests signals the end of a request containing media upload. END should be handled just like normal Insert/Upload requests, that is, they should process the request and return a complete resource in the response.Pointers to media data (a GFS path usually) appear in the relevant fields in the inserted/updated resource. See gdata.Media in data.proto.  
`RESPONSE_SENT` | Such requests occur after an END and signal that the response has been sent back to the client. RESPONSE_SENT is only sent to the backend if it is configured to receive them.The response does not need to contain anything.  
`ERROR` | Such requests indicate that an error occurred while processing the request. ERROR is only sent to the backend if it is configured to receive them. It is not guaranteed that all errors will result in this notification to the backend, even if the backend requests them.Since these requests are just for informational purposes, the response does not need to contain anything.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
