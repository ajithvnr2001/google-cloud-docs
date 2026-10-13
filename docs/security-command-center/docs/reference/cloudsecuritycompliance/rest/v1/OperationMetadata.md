---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/OperationMetadata/
title: OperationMetadata \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:36.625556+00:00
---

# OperationMetadata  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  OperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The metadata for the long-running operation.

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
`target` |  `string` Output only. The server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. The name of the verb that was executed by the operation.  
`statusMessage` |  `string` Output only. The human-readable status of the operation, if any.  
`requestedCancellation` |  `boolean` Output only. Identifies whether the user has requested that the operation be cancelled. If an operation was cancelled successfully, then the field `[google.longrunning.Operation.error](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/folders.locations.operationDetails#Operation.FIELDS.error)` contains the value `[google.rpc.Code.CANCELLED](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Code#ENUM_VALUES.CANCELLED)`.  
`apiVersion` |  `string` Output only. The API version that was used to start the operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-07 UTC."],[],[]] 
