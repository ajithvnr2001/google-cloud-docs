---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/OperationMetadataV1Beta/
title: OperationMetadataV1Beta \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:40.139096+00:00
---

# OperationMetadataV1Beta  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/OperationMetadataV1Beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)



Send feedback 

#  OperationMetadataV1Beta Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata for the given `[google.longrunning.Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

JSON representation  
---  
      
    
    {
      "method": string,
      "insertTime": string,
      "endTime": string,
      "user": string,
      "target": string,
      "ephemeralMessage": string,
      "warning": [
        string
      ],
    }  
  
Fields  
---  
`method` |  `string` API method that initiated this operation. Example: `google.appengine.v1beta.Versions.CreateVersion`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`insertTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Time that this operation was created.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Time that this operation completed.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`user` |  `string` User who requested this operation.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`target` |  `string` Name of the resource that this operation is acting on. Example: `apps/myapp/services/default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`ephemeralMessage` |  `string` Ephemeral message that may change every time the operation is polled.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`warning[]` |  `string` Durable messages that persist on every operation poll.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
