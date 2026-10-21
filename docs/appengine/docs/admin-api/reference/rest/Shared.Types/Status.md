---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/Status/
title: Status \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:56:15.675068+00:00
---

# Status  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/Status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)



Send feedback 

#  Status Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). The error model is designed to be:

  * Simple to use and understand for most users
  * Flexible enough to meet unexpected needs



### Overview

The `Status` message contains three pieces of data: error code, error message, and error details. The error code should be an enum value of `[google.rpc.Code](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/Code)`, but it may accept additional error codes if needed. The error message should be a developer-facing English message that helps developers _understand_ and _resolve_ the error. If a localized user-facing error message is needed, put the localized message in the error details or localize it in the client. The optional error details may contain arbitrary information about the error. There is a predefined set of error detail types in the package `google.rpc` which can be used for common error conditions.

### Language mapping

The `Status` message is the logical representation of the error model, but it is not necessarily the actual wire format. When the `Status` message is exposed in different client libraries and different wire protocols, it can be mapped differently. For example, it will likely be mapped to some exceptions in Java, but more likely mapped to some error codes in C.

### Other uses

The error model and the `Status` message can be used in a variety of environments, either with or without APIs, to provide a consistent developer experience across different environments.

Example uses of this error model include:

  * Partial errors. If a service needs to return partial errors to the client, it may embed the `Status` in the normal response to indicate the partial errors.

  * Workflow errors. A typical workflow has multiple steps. Each step may have a `Status` message for error reporting purpose.

  * Batch operations. If a client uses batch request and batch response, the `Status` message should be used directly inside batch response, one for each error sub-response.

  * Asynchronous operations. If an API call embeds asynchronous operation results in its response, the status of those operations should be represented directly using the `Status` message.

  * Logging. If some API errors are stored in logs, the message `Status` could be used directly after any stripping needed for security/privacy reasons.


JSON representation  
---  
      
    
    {
      "code": number,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ],
    }  
  
Fields  
---  
`code` |  `number` The status code, which should be an enum value of `[google.rpc.Code](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/Code)`.   
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `[google.rpc.Status.details](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/Status#FIELDS.details)` field, or localized by the client.   
`details[]` |  `object` A list of messages that carry the error details. There will be a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
