---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc
title: Namespace Google.Rpc (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:04.555741+00:00
---

# Namespace Google.Rpc (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Namespace Google.Rpc (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Rpc)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Rpc)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Rpc)



## Classes 

### [BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)

Describes violations in a client request. This error type focuses on the syntactic aspects of the request.

### [BadRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)

Container for nested types declared in the BadRequest message type.

### [BadRequest.Types.FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)

A message type used to describe a single bad request field.

### [CodeReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.CodeReflection)

Holder for reflection information generated from google/rpc/code.proto

### [DebugInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.DebugInfo)

Describes additional debugging info.

### [ErrorDetailsReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.ErrorDetailsReflection)

Holder for reflection information generated from google/rpc/error_details.proto

### [ErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.ErrorInfo)

Describes the cause of the error with structured details.

Example of an error when contacting the "pubsub.googleapis.com" API when it is not enabled:
    
    
    { "reason": "API_DISABLED"
      "domain": "googleapis.com"
      "metadata": {
        "resource": "projects/123",
        "service": "pubsub.googleapis.com"
      }
    }
    

This response indicates that the pubsub.googleapis.com API is not enabled.

Example of an error that is returned when attempting to create a Spanner instance in a region that is out of stock:
    
    
    { "reason": "STOCKOUT"
      "domain": "spanner.googleapis.com",
      "metadata": {
        "availableRegions": "us-central1,us-east2"
      }
    }
    

### [Help](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Help)

Provides links to documentation or for performing an out of band action.

For example, if a quota check failed with an error indicating the calling project hasn't enabled the accessed service, this can contain a URL pointing directly to the right place in the developer console to flip the bit.

### [Help.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Help.Types)

Container for nested types declared in the Help message type.

### [Help.Types.Link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Help.Types.Link)

Describes a URL link.

### [HttpHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.HttpHeader)

Represents an HTTP header.

### [HttpReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.HttpReflection)

Holder for reflection information generated from google/rpc/http.proto

### [HttpRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.HttpRequest)

Represents an HTTP request.

### [HttpResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.HttpResponse)

Represents an HTTP response.

### [LocalizedMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.LocalizedMessage)

Provides a localized error message that is safe to return to the user which can be attached to an RPC error.

### [PreconditionFailure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.PreconditionFailure)

Describes what preconditions have failed.

For example, if an RPC failed because it required the Terms of Service to be acknowledged, it could list the terms of service violation in the PreconditionFailure message.

### [PreconditionFailure.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.PreconditionFailure.Types)

Container for nested types declared in the PreconditionFailure message type.

### [PreconditionFailure.Types.Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.PreconditionFailure.Types.Violation)

A message type used to describe a single precondition failure.

### [QuotaFailure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.QuotaFailure)

Describes how a quota check failed.

For example if a daily limit was exceeded for the calling project, a service could respond with a QuotaFailure detail containing the project id and the description of the quota limit that was exceeded. If the calling project hasn't enabled the service in the developer console, then a service could respond with the project id and set `service_disabled` to true.

Also see RetryInfo and Help types for other details about handling a quota failure.

### [QuotaFailure.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.QuotaFailure.Types)

Container for nested types declared in the QuotaFailure message type.

### [QuotaFailure.Types.Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.QuotaFailure.Types.Violation)

A message type used to describe a single quota violation. For example, a daily quota or a custom quota that was exceeded.

### [RequestInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.RequestInfo)

Contains metadata about the request that clients can attach when filing a bug or providing other forms of feedback.

### [ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.ResourceInfo)

Describes the resource that is being accessed.

### [RetryInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.RetryInfo)

Describes when the clients can retry a failed request. Clients could ignore the recommendation here or retry when this information is missing from error responses.

It's always recommended that clients should use exponential backoff when retrying.

Clients should wait until `retry_delay` amount of time has passed since receiving the error response before retrying. If retrying requests also fail, clients should use an exponential backoff scheme to gradually increase the delay between retries based on `retry_delay`, until either a maximum number of retries have been reached or a maximum retry delay cap has been reached.

### [StandardErrorTypeRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.StandardErrorTypeRegistry)

Registry of the [ standard set of error types](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto) defined in the richer error model developed and used by Google. These can be sepcified in the [Details](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status#Google_Rpc_Status_Details).

### [Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status)

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details.

You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).

### [StatusReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.StatusReflection)

Holder for reflection information generated from google/rpc/status.proto

## Enums 

### [Code](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Code)

The canonical error codes for gRPC APIs.

Sometimes multiple error codes may apply. Services should return the most specific error code that applies. For example, prefer `OUT_OF_RANGE` over `FAILED_PRECONDITION` if both codes apply. Similarly prefer `NOT_FOUND` or `ALREADY_EXISTS` over `FAILED_PRECONDITION`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
