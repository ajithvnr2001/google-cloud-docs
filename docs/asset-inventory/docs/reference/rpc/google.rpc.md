---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc
title: Package google.rpc \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.774652+00:00
---

# Package google.rpc  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.rpc Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[BadRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.BadRequest)` (message)
  * `[BadRequest.FieldViolation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.BadRequest.FieldViolation)` (message)
  * `[Code](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Code)` (enum)
  * `[Help](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Help)` (message)
  * `[Help.Link](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Help.Link)` (message)
  * `[LocalizedMessage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.LocalizedMessage)` (message)
  * `[PreconditionFailure](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.PreconditionFailure)` (message)
  * `[PreconditionFailure.Violation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.PreconditionFailure.Violation)` (message)
  * `[QuotaFailure](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.QuotaFailure)` (message)
  * `[QuotaFailure.Violation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.QuotaFailure.Violation)` (message)
  * `[RequestInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.RequestInfo)` (message)
  * `[ResourceInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.ResourceInfo)` (message)
  * `[RetryInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.RetryInfo)` (message)
  * `[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Status)` (message)



## BadRequest

Describes violations in a client request. This error type focuses on the syntactic aspects of the request.

Fields  
---  
`field_violations[]` |  `[FieldViolation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.BadRequest.FieldViolation)` Describes all violations in a client request.  
  
## FieldViolation

A message type used to describe a single bad request field.

Fields  
---  
`field` |  `string` A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.Consider the following:
    
    
    message CreateContactRequest {
      message EmailAddress {
        enum Type {
          TYPE_UNSPECIFIED = 0;
          HOME = 1;
          WORK = 2;
        }
    
        optional string email = 1;
        repeated EmailType type = 2;
      }
    
      string full_name = 1;
      repeated EmailAddress email_addresses = 2;
    }
    

In this example, in proto `field` could take one of the following values:

  * `full_name` for a violation in the `full_name` value
  * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
  * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

  * `fullName` for a violation in the `fullName` value
  * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
  * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.

  
`description` |  `string` A description of why the request element is bad.  
`reason` |  `string` The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`localized_message` |  `[LocalizedMessage](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.LocalizedMessage)` Provides a localized error message for field-level errors that is safe to return to the API consumer.  
  
## Code

The canonical error codes for gRPC APIs.

Sometimes multiple error codes may apply. Services should return the most specific error code that applies. For example, prefer `OUT_OF_RANGE` over `FAILED_PRECONDITION` if both codes apply. Similarly prefer `NOT_FOUND` or `ALREADY_EXISTS` over `FAILED_PRECONDITION`.

Enums  
---  
`OK` | Not an error; returned on success.HTTP Mapping: 200 OK  
`CANCELLED` | The operation was cancelled, typically by the caller.HTTP Mapping: 499 Client Closed Request  
`UNKNOWN` | Unknown error. For example, this error may be returned when a `Status` value received from another address space belongs to an error space that is not known in this address space. Also errors raised by APIs that do not return enough error information may be converted to this error.HTTP Mapping: 500 Internal Server Error  
`INVALID_ARGUMENT` | The client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (e.g., a malformed file name).HTTP Mapping: 400 Bad Request  
`DEADLINE_EXCEEDED` | The deadline expired before the operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.HTTP Mapping: 504 Gateway Timeout  
`NOT_FOUND` | Some requested entity (e.g., file or directory) was not found.Note to server developers: if a request is denied for an entire class of users, such as gradual feature rollout or undocumented allowlist, `NOT_FOUND` may be used. If a request is denied for some users within a class of users, such as user-based access control, `PERMISSION_DENIED` must be used.HTTP Mapping: 404 Not Found  
`ALREADY_EXISTS` | The entity that a client attempted to create (e.g., file or directory) already exists.HTTP Mapping: 409 Conflict  
`PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. `PERMISSION_DENIED` must not be used for rejections caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for those errors). `PERMISSION_DENIED` must not be used if the caller can not be identified (use `UNAUTHENTICATED` instead for those errors). This error code does not imply the request is valid or the requested entity exists or satisfies other pre-conditions.HTTP Mapping: 403 Forbidden  
`UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation.HTTP Mapping: 401 Unauthorized  
`RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.HTTP Mapping: 429 Too Many Requests  
`FAILED_PRECONDITION` | The operation was rejected because the system is not in a state required for the operation's execution. For example, the directory to be deleted is non-empty, an rmdir operation is applied to a non-directory, etc.Service implementors can use the following guidelines to decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use `UNAVAILABLE` if the client can retry just the failing call. (b) Use `ABORTED` if the client should retry at a higher level. For example, when a client-specified test-and-set fails, indicating the client should restart a read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client should not retry until the system state has been explicitly fixed. For example, if an "rmdir" fails because the directory is non-empty, `FAILED_PRECONDITION` should be returned since the client should not retry unless the files are deleted from the directory.HTTP Mapping: 400 Bad Request  
`ABORTED` | The operation was aborted, typically due to a concurrency issue such as a sequencer check failure or transaction abort.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 409 Conflict  
`OUT_OF_RANGE` | The operation was attempted past the valid range. E.g., seeking or reading past end-of-file.Unlike `INVALID_ARGUMENT`, this error indicates a problem that may be fixed if the system state changes. For example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to read at an offset that is not in the range [0,2^32-1], but it will generate `OUT_OF_RANGE` if asked to read from an offset past the current file size.There is a fair bit of overlap between `FAILED_PRECONDITION` and `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error) when it applies so that callers who are iterating through a space can easily look for an `OUT_OF_RANGE` error to detect when they are done.HTTP Mapping: 400 Bad Request  
`UNIMPLEMENTED` | The operation is not implemented or is not supported/enabled in this service.HTTP Mapping: 501 Not Implemented  
`INTERNAL` | Internal errors. This means that some invariants expected by the underlying system have been broken. This error code is reserved for serious errors.HTTP Mapping: 500 Internal Server Error  
`UNAVAILABLE` | The service is currently unavailable. This is most likely a transient condition, which can be corrected by retrying with a backoff. Note that it is not always safe to retry non-idempotent operations.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 503 Service Unavailable  
`DATA_LOSS` | Unrecoverable data loss or corruption.HTTP Mapping: 500 Internal Server Error  
  
## Help

Provides links to documentation or for performing an out of band action.

For example, if a quota check failed with an error indicating the calling project hasn't enabled the accessed service, this can contain a URL pointing directly to the right place in the developer console to flip the bit.

Fields  
---  
`links[]` |  `[Link](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Help.Link)` URL(s) pointing to additional information on handling the current error.  
  
## Link

Describes a URL link.

Fields  
---  
`description` |  `string` Describes what the link offers.  
`url` |  `string` The URL of the link.  
  
## LocalizedMessage

Provides a localized error message that is safe to return to the user which can be attached to an RPC error.

Fields  
---  
`locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`message` |  `string` The localized error message in the above locale.  
  
## PreconditionFailure

Describes what preconditions have failed.

For example, if an RPC failed because it required the Terms of Service to be acknowledged, it could list the terms of service violation in the PreconditionFailure message.

Fields  
---  
`violations[]` |  `[Violation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.PreconditionFailure.Violation)` Describes all precondition violations.  
  
## Violation

A message type used to describe a single precondition failure.

Fields  
---  
`type` |  `string` The type of PreconditionFailure. We recommend using a service-specific enum type to define the supported precondition violation subjects. For example, "TOS" for "Terms of Service violation".  
`subject` |  `string` The subject, relative to the type, that failed. For example, "google.com/cloud" relative to the "TOS" type would indicate which terms of service is being referenced.  
`description` |  `string` A description of how the precondition failed. Developers can use this description to understand how to fix the failure.For example: "Terms of service not accepted".  
  
## QuotaFailure

Describes how a quota check failed.

For example if a daily limit was exceeded for the calling project, a service could respond with a QuotaFailure detail containing the project id and the description of the quota limit that was exceeded. If the calling project hasn't enabled the service in the developer console, then a service could respond with the project id and set `service_disabled` to true.

Also see RetryInfo and Help types for other details about handling a quota failure.

Fields  
---  
`violations[]` |  `[Violation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.QuotaFailure.Violation)` Describes all quota violations.  
  
## Violation

A message type used to describe a single quota violation. For example, a daily quota or a custom quota that was exceeded.

Fields  
---  
`subject` |  `string` The subject on which the quota check failed. For example, "clientip:" or "project:".  
`description` |  `string` A description of how the quota check failed. Clients can use this description to find more about the quota configuration in the service's public documentation, or find the relevant quota limit to adjust through developer console.For example: "Service disabled" or "Daily Limit for read operations exceeded".  
`api_service` |  `string` The API Service from which the `QuotaFailure.Violation` orginates. In some cases, Quota issues originate from an API Service other than the one that was called. In other words, a dependency of the called API Service could be the cause of the `QuotaFailure`, and this field would have the dependency API service name.For example, if the called API is Kubernetes Engine API (container.googleapis.com), and a quota violation occurs in the Kubernetes Engine API itself, this field would be "container.googleapis.com". On the other hand, if the quota violation occurs when the Kubernetes Engine API creates VMs in the Compute Engine API (compute.googleapis.com), this field would be "compute.googleapis.com".  
`quota_metric` |  `string` The metric of the violated quota. A quota metric is a named counter to measure usage, such as API requests or CPUs. When an activity occurs in a service, such as Virtual Machine allocation, one or more quota metrics may be affected.For example, "compute.googleapis.com/cpus_per_vm_family", "storage.googleapis.com/internet_egress_bandwidth".  
`quota_id` |  `string` The id of the violated quota. Also know as "limit name", this is the unique identifier of a quota in the context of an API service.For example, "CPUS-PER-VM-FAMILY-per-project-region".  
`quota_dimensions` |  `map<string, string>` The dimensions of the violated quota. Every non-global quota is enforced on a set of dimensions. While quota metric defines what to count, the dimensions specify for what aspects the counter should be increased.For example, the quota "CPUs per region per VM family" enforces a limit on the metric "compute.googleapis.com/cpus_per_vm_family" on dimensions "region" and "vm_family". And if the violation occurred in region "us-central1" and for VM family "n1", the quota_dimensions would be,{ "region": "us-central1", "vm_family": "n1", }When a quota is enforced globally, the quota_dimensions would always be empty.  
`quota_value` |  `int64` The enforced quota value at the time of the `QuotaFailure`.For example, if the enforced quota value at the time of the `QuotaFailure` on the number of CPUs is "10", then the value of this field would reflect this quantity.  
`future_quota_value` |  `int64` The new quota value being rolled out at the time of the violation. At the completion of the rollout, this value will be enforced in place of quota_value. If no rollout is in progress at the time of the violation, this field is not set.For example, if at the time of the violation a rollout is in progress changing the number of CPUs quota from 10 to 20, 20 would be the value of this field.  
  
## RequestInfo

Contains metadata about the request that clients can attach when filing a bug or providing other forms of feedback.

Fields  
---  
`request_id` |  `string` An opaque string that should only be interpreted by the service generating it. For example, it can be used to identify requests in the service's logs.  
`serving_data` |  `string` Any data that was used to serve this request. For example, an encrypted stack trace that can be sent back to the service provider for debugging.  
  
## ResourceInfo

Describes the resource that is being accessed.

Fields  
---  
`resource_type` |  `string` A name for the type of resource being accessed, e.g. "sql table", "cloud storage bucket", "file", "Google calendar"; or the type URL of the resource: e.g. "type.googleapis.com/google.pubsub.v1.Topic".  
`resource_name` |  `string` The name of the resource being accessed. For example, a shared calendar name: "example.com[_4fghdhgsrgh@group.calendar.google.com"](mailto:_4fghdhgsrgh@group.calendar.google.com"), if the current error is `[google.rpc.Code.PERMISSION_DENIED](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.PERMISSION_DENIED)`.  
`owner` |  `string` The owner of the resource (optional). For example, "user:" or "project:".  
`description` |  `string` Describes what error is encountered when accessing this resource. For example, updating a cloud project may require the `writer` permission on the developer console project.  
  
## RetryInfo

Describes when the clients can retry a failed request. Clients could ignore the recommendation here or retry when this information is missing from error responses.

It's always recommended that clients should use exponential backoff when retrying.

Clients should wait until `retry_delay` amount of time has passed since receiving the error response before retrying. If retrying requests also fail, clients should use an exponential backoff scheme to gradually increase the delay between retries based on `retry_delay`, until either a maximum number of retries have been reached or a maximum retry delay cap has been reached.

Fields  
---  
`retry_delay` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Clients should wait at least this long between retrying the same request.  
  
## Status

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details.

You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).

Fields  
---  
`code` |  `int32` The status code, which should be an enum value of `[google.rpc.Code](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Code)`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `[google.rpc.Status.details](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Status.FIELDS.repeated.google.protobuf.Any.google.rpc.Status.details)` field, or localized by the client.  
`details[]` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` A list of messages that carry the error details. There is a common set of message types for APIs to use.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
