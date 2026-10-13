---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ServiceLatency/
title: ServiceLatency \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:02.723800+00:00
---

# ServiceLatency  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ServiceLatency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  ServiceLatency Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InternalServiceLatency
    * JSON representation



Message to represent the latency of the service.

JSON representation  
---  
      
    
    {
      "internalServiceLatencies": [
        {
          object ([InternalServiceLatency](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ServiceLatency#InternalServiceLatency))
        }
      ]
    }  
  
Fields  
---  
`internalServiceLatencies[]` |  `object (`[InternalServiceLatency](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ServiceLatency#InternalServiceLatency)`)` A list of internal service latencies.  
  
## InternalServiceLatency

Message to represent the latency of an internal service.

JSON representation  
---  
      
    
    {
      "step": string,
      "latencyMs": number,
      "startTime": string,
      "completeTime": string
    }  
  
Fields  
---  
`step` |  `string` The name of the internal service.  
`latencyMs` |  `number` The latency of the internal service in milliseconds.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of the internal service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The completion time of the internal service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-29 UTC."],[],[]] 
