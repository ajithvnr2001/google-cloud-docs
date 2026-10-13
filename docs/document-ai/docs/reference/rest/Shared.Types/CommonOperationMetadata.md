---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/CommonOperationMetadata/
title: CommonOperationMetadata \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:22.920926+00:00
---

# CommonOperationMetadata  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/CommonOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  CommonOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

The common metadata for long running operations.

JSON representation  
---  
      
    
    {
      "state": enum (State),
      "stateMessage": string,
      "resource": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`state` |  `enum (`State`)` The state of the operation.  
`stateMessage` |  `string` A message providing more details about the current state of processing.  
`resource` |  `string` A related resource to this operation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The creation time of the operation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last update time of the operation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
