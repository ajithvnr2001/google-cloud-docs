---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/Shared.Types/OperationMetadata/
title: OperationMetadata \u00a0|\u00a0 Sovereign Controls by Partners guides for partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:30:04.896069+00:00
---

# OperationMetadata  |  Sovereign Controls by Partners guides for partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/Shared.Types/OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners)
  * [ Sovereign Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/guides)
  * [ Reference ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest)



Send feedback 

#  OperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents the metadata of the long-running operation.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "endTime": string,
      "target": string,
      "verb": string,
      "statusMessage": string,
      "requestedCancellation": boolean,
      "apiVersion": string
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the operation was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the operation finished running.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`statusMessage` |  `string` Output only. Human-readable status of the operation, if any.  
`requestedCancellation` |  `boolean` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have [Operation.error][] value with a `google.rpc.Status.code` of 1, corresponding to `Code.CANCELLED`.  
`apiVersion` |  `string` Output only. API version used to start the operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
