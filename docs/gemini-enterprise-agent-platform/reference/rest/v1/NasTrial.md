---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial/
title: NasTrial \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:28:21.981527+00:00
---

# NasTrial  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  NasTrial Stay organized with collections  Save and categorize content based on your preferences. 

Represents a uCAIP NasJob trial.

Fields  
  
`id` `string` Output only. The identifier of the NasTrial assigned by the service. | `state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial#State)`)` Output only. The detailed state of the NasTrial. | `finalMeasurement` `object (`[Measurement](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement)`)` Output only. The final measurement containing the objective value. | `startTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the NasTrial was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `endTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time when the NasTrial's status changed to `SUCCEEDED` or `INFEASIBLE`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "id": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial#State)),
      "finalMeasurement": {
        object ([Measurement](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Measurement))
      },
      "startTime": string,
      "endTime": string
    }  
  
## State

Describes a NasTrial state.

Enums  
---  
`STATE_UNSPECIFIED` | The NasTrial state is unspecified.  
`REQUESTED` | Indicates that a specific NasTrial has been requested, but it has not yet been suggested by the service.  
`ACTIVE` | Indicates that the NasTrial has been suggested.  
`STOPPING` | Indicates that the NasTrial should stop according to the service.  
`SUCCEEDED` | Indicates that the NasTrial is completed successfully.  
`INFEASIBLE` | Indicates that the NasTrial should not be attempted again. The service will set a NasTrial to INFEASIBLE when it's done but missing the finalMeasurement.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
