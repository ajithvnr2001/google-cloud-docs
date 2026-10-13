---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/OperationMetadata/
title: OperationMetadata \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:36.157427+00:00
---

# OperationMetadata  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



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
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the operation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the operation finished running.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`statusMessage` |  `string` Output only. Human-readable status of the operation, if any.  
`requestedCancellation` |  `boolean` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[Operation.error](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.operations#Operation.FIELDS.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.operations#Status.FIELDS.code)` of 1, corresponding to `Code.CANCELLED`.  
`apiVersion` |  `string` Output only. API version used to start the operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-11 UTC."],[],[]] 
