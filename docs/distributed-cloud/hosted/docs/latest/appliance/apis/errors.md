---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/errors/
title: Google Distributed Cloud air-gapped appliance Errors \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:21.774483+00:00
---

# Google Distributed Cloud air-gapped appliance Errors  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Google Distributed Cloud air-gapped appliance Errors Stay organized with collections  Save and categorize content based on your preferences. 

This chapter provides an overview of the error model for Google Distributed Cloud air-gapped appliance (GDC) APIs. It also provides general guidance to developers on how to properly generate and handle errors.

GDC APIs use a simple protocol-agnostic error model, which allows us to offer a consistent experience across different APIs, different API protocols (such as gRPC or HTTP), and different error contexts (such as asynchronous, batch, or workflow errors).

## Error model

The error model for GDC APIs is logically defined by [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto), an instance of which is returned to the client when an API error occurs. The following code snippet shows the overall design of the error model:
    
    
    package google.rpc;
    
    // The `Status` type defines a logical error model that is suitable for
    // different programming environments, including REST APIs and RPC APIs.
    message Status {
      // A simple error code that can be easily handled by the client. The
      // actual error code is defined by `google.rpc.Code`.
      int32 code = 1;
    
      // A developer-facing human-readable error message in English. It should
      // both explain the error and offer an actionable resolution to it.
      string message = 2;
    
      // Additional error information that the client code can use to handle
      // the error, such as retry info or a help link.
      repeated google.protobuf.Any details = 3;
    }
    

Because most Google APIs use resource-oriented API design, the error handling follows the same design principle by using a small set of standard errors with a large number of resources. For example, instead of defining different kinds of "not found" errors, the server uses one standard `google.rpc.Code.NOT_FOUND` error code and tells the client which specific resource was not found. The smaller error space reduces the complexity of documentation, affords better idiomatic mappings in client libraries, and reduces client logic complexity while not restricting the inclusion of actionable information.

**Note:** When using gRPC, errors are included in the headers, and total headers in responses are limited to 8 KB (8,192 bytes). Ensure that errors do not exceed 1-2 KB in size.

### Error codes

GDC APIs **must** use the canonical error codes defined by [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). Individual APIs **must** avoid defining additional error codes, since developers are very unlikely to write logic to handle a large number of error codes. For reference, handling an average of three error codes per API call would mean most application logic would just be for error handling, which would not be a good developer experience.

### Error messages

The error message should help users **understand and resolve** the API error easily and quickly. In general, consider the following guidelines when writing error messages:

  * Do not assume the user is an expert user of your API. Users could be client developers, operations people, IT staff, or end-users of apps.
  * Do not assume the user knows anything about your service implementation or is familiar with the context of the errors (such as log analysis).
  * When possible, error messages should be constructed such that a technical user (but not necessarily a developer of your API) can respond to the error and correct it.
  * Keep the error message brief. If needed, provide a link where a confused reader can ask questions, give feedback, or get more information that doesn't cleanly fit in an error message. Otherwise, use the details field to expand.

**Warning:** Error messages are not part of the API surface. They are subject to changes without notice. Application code **must not** have a hard dependency on error messages.

### Error details

GDC APIs define a set of standard error payloads for error details, which you can find in [google/rpc/error_details.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto). These cover the most common needs for API errors, such as quota failure and invalid parameters. Like error codes, developers should use these standard payloads whenever possible.

Additional error detail types should only be introduced if they can assist application code to handle the errors. If the error information can only be handled by humans, rely on the error message content and let developers handle it manually rather than introducing additional error detail types.

Here are some example `error_details` payloads:

  * `ErrorInfo`: Provides structured error information that is both **stable** and **extensible**.
  * `RetryInfo`: Describes when clients can retry a failed request, may be returned on `Code.UNAVAILABLE` or `Code.ABORTED`
  * `QuotaFailure`: Describes how a quota check failed, may be returned on `Code.RESOURCE_EXHAUSTED`
  * `BadRequest`: Describes violations in a client request, may be returned on `Code.INVALID_ARGUMENT`



### Error info

`ErrorInfo` is a special kind of error payload. It provides **stable and extensible** error information that both humans and applications can depend on. Each `ErrorInfo` has three pieces of information: an error domain, an error reason, and a set of error metadata, such as this [example](https://translate.googleapis.com/language/translate/v2?key=invalid&q=hello&source=en&target=es&format=text&$.xgafv=2). For more information, see the [`ErrorInfo`](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto#L112) definition.

For GDC APIs, the primary error domain is `googleapis.com`, and the corresponding error reasons are defined by `google.api.ErrorReason` enum. For more information, see the [`google.api.ErrorReason`](https://github.com/googleapis/googleapis/blob/master/google/api/error_reason.proto) definition.

### Error localization

The `message` field in [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) is developer-facing and **must** be in English.

If a user-facing error message is needed, use [`google.rpc.LocalizedMessage`](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto) as your details field. While the message field in [`google.rpc.LocalizedMessage`](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto) can be localized, ensure that the message field in [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) is in English.

By default, the API service should use the authenticated user's locale or HTTP `Accept-Language` header or the `language_code` parameter in the request to determine the language for the localization.

## Error mapping

GDC APIs are accessible in different programming environments. Each environment typically has its own way of error handling. The following sections explain how the error model is mapped in commonly used environments.

### HTTP mapping

While proto3 messages have native JSON encoding, GDC API platform uses a different error schema for GDC JSON HTTP APIs for backward compatibility reasons.

Schema:
    
    
    // This message defines the error schema for GDC JSON HTTP APIs.
    message Error {
      // Deprecated. This message is only used by error format v1.
      message ErrorProto {}
      // This message has the same semantics as `google.rpc.Status`. It uses HTTP
      // status code instead of gRPC status code. It has extra fields `status` and
      // `errors` for backward compatibility with [GDC API Client
      // Libraries](https://developers.google.com/api-client-library).
      message Status {
        // The HTTP status code that corresponds to `google.rpc.Status.code`.
        int32 code = 1;
        // This corresponds to `google.rpc.Status.message`.
        string message = 2;
        // Deprecated. This field is only used by error format v1.
        repeated ErrorProto errors = 3;
        // This is the enum version for `google.rpc.Status.code`.
        google.rpc.Code status = 4;
        // This corresponds to `google.rpc.Status.details`.
        repeated google.protobuf.Any details = 5;
      }
      // The actual error payload. The nested message structure is for backward
      // compatibility with [GDC API Client
      // Libraries](https://developers.google.com/api-client-library). It also
      // makes the error more readable to developers.
      Status error = 1;
    }
    

Example ([link](https://translate.googleapis.com/language/translate/v2?key=invalid&q=hello&source=en&target=es&format=text&$.xgafv=2)):
    
    
    {
      "error": {
        "code": 400,
        "message": "API key not valid. Please pass a valid API key.",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "API_KEY_INVALID",
            "domain": "googleapis.com",
            "metadata": {
              "service": "translate.googleapis.com"
            }
          }
        ]
      }
    }
    

### gRPC mapping

Different RPC protocols map the error model differently. For [gRPC](http://grpc.io), the error model is natively supported by the generated code and the runtime library in each supported language. You can find out more in gRPC's API documentation. For example, see gRPC Java's [`io.grpc.Status`](https://grpc.github.io/grpc-java/javadoc/io/grpc/Status.html).

### Client library mapping

GDC client libraries may choose to surface errors differently per language to be consistent with established idioms. For example, the [google-cloud-go](https://github.com/GoogleCloudPlatform/google-cloud-go) library will return an error that implements the same interface as [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto), while [google-cloud-java](https://github.com/googleapis/google-cloud-java) will raise an Exception.

## Handle errors

This table lists all of the gRPC error codes defined in [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto) and a short description of their cause. To handle an error, you can check the description for the returned status code and modify your call accordingly.

HTTP | gRPC | Description  
---|---|---  
200 | `OK` | No error.  
400 | `INVALID_ARGUMENT` | Client specified an invalid argument. Check error message and error details for more information.  
400 | `FAILED_PRECONDITION` | Request cannot be executed in the current system state, such as deleting a non-empty directory.  
400 | `OUT_OF_RANGE` | Client specified an invalid range.  
401 | `UNAUTHENTICATED` | Request not authenticated due to missing, invalid, or expired OAuth token.  
403 | `PERMISSION_DENIED` | Client does not have sufficient permission. This can happen because the OAuth token does not have the right scopes, the client doesn't have permission, or the API has not been enabled.  
404 | `NOT_FOUND` | A specified resource is not found.  
409 | `ABORTED` | Concurrency conflict, such as read-modify-write conflict.  
409 | `ALREADY_EXISTS` | The resource that a client tried to create already exists.  
429 | `RESOURCE_EXHAUSTED` | Either out of resource quota or reaching rate limiting. The client should look for google.rpc.QuotaFailure error detail for more information.  
499 | `CANCELLED` | Request cancelled by the client.  
500 | `DATA_LOSS` | Unrecoverable data loss or data corruption. The client should report the error to the user.  
500 | `UNKNOWN` | Unknown server error. Typically a server bug.  
500 | `INTERNAL` | Internal server error. Typically a server bug.  
501 | `NOT_IMPLEMENTED` | API method not implemented by the server.  
502 | N/A | Network error occurred before reaching the server. Typically a network outage or misconfiguration.  
503 | `UNAVAILABLE` | Service unavailable. Typically the server is down.  
504 | `DEADLINE_EXCEEDED` | Request deadline exceeded. This will happen only if the caller sets a deadline that is shorter than the method's default deadline (i.e. requested deadline is not enough for the server to process the request) and the request did not finish within the deadline.  
**Warning:** GDC APIs may concurrently check multiple preconditions for an API request. Returning one error code does not imply other preconditions are satisfied. Application code **must not** depend on the ordering of precondition checks.

### Retry errors

Clients **may** retry on 503 UNAVAILABLE errors with exponential backoff. The minimum delay should be 1s unless it is documented otherwise. The default retry repetition should be once unless it is documented otherwise.

For 429 RESOURCE_EXHAUSTED errors, the client may retry at the higher level with minimum 30s delay. Such retries are only useful for long running background jobs.

For all other errors, retry may not be applicable. First ensure your request is idempotent, and see [`google.rpc.RetryInfo`](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto#L40) for guidance.

### Propagate errors

If your API service depends on other services, you should not blindly propagate errors from those services to your clients. When translating errors, we suggest the following:

  * Hide implementation details and confidential information.
  * Adjust the party responsible for the error. For example, a server that receives an `INVALID_ARGUMENT` error from another service should propagate an `INTERNAL` to its own caller.



### Reproduce errors

If you cannot resolve errors through analysis of logs and monitoring, you should try to reproduce the errors with a simple and repeatable test. You can use the test to collect more information for troubleshooting, which you can provide when contacting technical support.

We recommend you use [`oauth2l`](https://github.com/google/oauth2l) and [`curl -v`](https://curl.se/docs/manpage.html) and [System Parameters](https://docs.cloud.google.com/apis/docs/system-parameters) to reproduce errors with GDC APIs. Together they can reproduce almost all GDC API requests, and provide you verbose debug information. For more information, see the respective documentation pages for the API you are calling.

## Generate errors

If you are a server developer, you should generate errors with enough information to help client developers understand and resolve the problem. At the same time, you must be aware of the security and privacy of the user data, and avoid disclosing sensitive information in the error message and error details, since errors are often logged and may be accessible by others. For example, an error message like "Client IP address is not on allowlist 128.0.0.0/8" exposes information about the server-side policy, which may not be accessible to the user who has access to the logs.

To generate proper errors, you first need to be familiar with [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto) to choose the most suitable error code for each error condition. A server application may check multiple error conditions in parallel, and return the first one.

The following table lists each error code and an example of a good error message.

HTTP | gRPC | Example Error Message  
---|---|---  
400 | `INVALID_ARGUMENT` | Request field x.y.z is xxx, expected one of [yyy, zzz].  
400 | `FAILED_PRECONDITION` | Resource xxx is a non-empty directory, so it cannot be deleted.  
400 | `OUT_OF_RANGE` | Parameter 'age' is out of range [0, 125].  
401 | `UNAUTHENTICATED` | Invalid authentication credentials.  
403 | `PERMISSION_DENIED` | Permission 'xxx' denied on resource 'yyy'.  
404 | `NOT_FOUND` | Resource 'xxx' not found.  
409 | `ABORTED` | Couldn't acquire lock on resource 'xxx.  
409 | `ALREADY_EXISTS` | Resource 'xxx' already exists.  
429 | `RESOURCE_EXHAUSTED` | Quota limit 'xxx' exceeded.  
499 | `CANCELLED` | Request cancelled by the client.  
500 | `DATA_LOSS` | See note.  
500 | `UNKNOWN` | See note.  
500 | `INTERNAL` | See note.  
501 | `NOT_IMPLEMENTED` | Method 'xxx' not implemented.  
503 | `UNAVAILABLE` | See note.  
504 | `DEADLINE_EXCEEDED` | See note.  
**Note:** Since the client cannot fix the server error, it is not useful to generate additional error details. To avoid leaking sensitive information under error conditions, it is recommended not to generate any error message and only generate `google.rpc.DebugInfo` error details. The `DebugInfo` is specially designed only for server-side logging, and **must** not be sent to client.

### Error payloads

The `google.rpc` package defines a set of standard error payloads, which are preferred to custom error payloads. The following table lists each error code and its matching standard error payload, if applicable. We recommend advanced applications look for these error payloads in `google.rpc.Status` when they handle errors.

HTTP | gRPC | Recommended Error Detail  
---|---|---  
400 | `INVALID_ARGUMENT` | `google.rpc.BadRequest`  
400 | `FAILED_PRECONDITION` | `google.rpc.PreconditionFailure`  
400 | `OUT_OF_RANGE` | `google.rpc.BadRequest`  
401 | `UNAUTHENTICATED` | `google.rpc.ErrorInfo`  
403 | `PERMISSION_DENIED` | `google.rpc.ErrorInfo`  
404 | `NOT_FOUND` | `google.rpc.ResourceInfo`  
409 | `ABORTED` | `google.rpc.ErrorInfo`  
409 | `ALREADY_EXISTS` | `google.rpc.ResourceInfo`  
429 | `RESOURCE_EXHAUSTED` | `google.rpc.QuotaFailure`  
499 | `CANCELLED` |   
500 | `DATA_LOSS` | `google.rpc.DebugInfo`  
500 | `UNKNOWN` | `google.rpc.DebugInfo`  
500 | `INTERNAL` | `google.rpc.DebugInfo`  
501 | `NOT_IMPLEMENTED` |   
503 | `UNAVAILABLE` | `google.rpc.DebugInfo`  
504 | `DEADLINE_EXCEEDED` | `google.rpc.DebugInfo`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
