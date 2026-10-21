---
url: https://docs.cloud.google.com/apis/design/errors/
title: AIP-193: Errors
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:59.306562+00:00
---

# AIP-193: Errors

> Source: https://docs.cloud.google.com/apis/design/errors/

  * AIPs by Scope
  * [General](https://docs.cloud.google.com/general)
  * [Google Cloud Platform](https://docs.cloud.google.com/cloud)
  * [Auth](https://docs.cloud.google.com/auth)
  * [Client libraries](https://docs.cloud.google.com/client-libraries)
  * [Workspace](https://docs.cloud.google.com/apps)
  * [Actions on Google](https://docs.cloud.google.com/aog)
  * AIPs
  * [ 1 AIP Purpose and Guidelines ](https://docs.cloud.google.com/1)
  * [ 2 AIP Numbering ](https://docs.cloud.google.com/2)
  * [ 3 AIP Versioning ](https://docs.cloud.google.com/3)
  * [ 8 AIP Style and Guidance ](https://docs.cloud.google.com/8)
  * [ 9 Glossary ](https://docs.cloud.google.com/9)
  * [ 100 API Design Review FAQ ](https://docs.cloud.google.com/100)
  * [ 111 Planes ](https://docs.cloud.google.com/111)
  * [ 121 Resource-oriented design ](https://docs.cloud.google.com/121)
  * [ 122 Resource names ](https://docs.cloud.google.com/122)
  * [ 123 Resource types ](https://docs.cloud.google.com/123)
  * [ 124 Resource association ](https://docs.cloud.google.com/124)
  * [ 126 Enumerations ](https://docs.cloud.google.com/126)
  * [ 127 HTTP and gRPC Transcoding ](https://docs.cloud.google.com/127)
  * [ 128 Declarative-friendly interfaces ](https://docs.cloud.google.com/128)
  * [ 129 Server-Modified Values and Defaults ](https://docs.cloud.google.com/129)
  * [ 130 Methods ](https://docs.cloud.google.com/130)
  * [ 131 Standard methods: Get ](https://docs.cloud.google.com/131)
  * [ 132 Standard methods: List ](https://docs.cloud.google.com/132)
  * [ 133 Standard methods: Create ](https://docs.cloud.google.com/133)
  * [ 134 Standard methods: Update ](https://docs.cloud.google.com/134)
  * [ 135 Standard methods: Delete ](https://docs.cloud.google.com/135)
  * [ 136 Custom methods ](https://docs.cloud.google.com/136)
  * [ 140 Field names ](https://docs.cloud.google.com/140)
  * [ 141 Quantities ](https://docs.cloud.google.com/141)
  * [ 142 Time and duration ](https://docs.cloud.google.com/142)
  * [ 143 Standardized codes ](https://docs.cloud.google.com/143)
  * [ 144 Repeated fields ](https://docs.cloud.google.com/144)
  * [ 145 Ranges ](https://docs.cloud.google.com/145)
  * [ 146 Generic fields ](https://docs.cloud.google.com/146)
  * [ 147 Sensitive fields ](https://docs.cloud.google.com/147)
  * [ 148 Standard fields ](https://docs.cloud.google.com/148)
  * [ 149 Unset field values ](https://docs.cloud.google.com/149)
  * [ 151 Long-running operations ](https://docs.cloud.google.com/151)
  * [ 152 Jobs ](https://docs.cloud.google.com/152)
  * [ 153 Import and export ](https://docs.cloud.google.com/153)
  * [ 154 Resource freshness validation ](https://docs.cloud.google.com/154)
  * [ 155 Request identification ](https://docs.cloud.google.com/155)
  * [ 156 Singleton resources ](https://docs.cloud.google.com/156)
  * [ 157 Partial responses ](https://docs.cloud.google.com/157)
  * [ 158 Pagination ](https://docs.cloud.google.com/158)
  * [ 159 Reading across collections ](https://docs.cloud.google.com/159)
  * [ 160 Filtering ](https://docs.cloud.google.com/160)
  * [ 161 Field masks ](https://docs.cloud.google.com/161)
  * [ 162 Resource Revisions ](https://docs.cloud.google.com/162)
  * [ 163 Change validation ](https://docs.cloud.google.com/163)
  * [ 164 Soft delete ](https://docs.cloud.google.com/164)
  * [ 165 Criteria-based delete ](https://docs.cloud.google.com/165)
  * [ 180 Backwards compatibility ](https://docs.cloud.google.com/180)
  * [ 181 Stability levels ](https://docs.cloud.google.com/181)
  * [ 182 External software dependencies ](https://docs.cloud.google.com/182)
  * [ 184 API version identifiers ](https://docs.cloud.google.com/184)
  * [ 185 API Versioning ](https://docs.cloud.google.com/185)
  * [ 190 Naming conventions ](https://docs.cloud.google.com/190)
  * [ 191 File and directory structure ](https://docs.cloud.google.com/191)
  * [ 192 Documentation ](https://docs.cloud.google.com/192)
  * [ 193 Errors ](https://docs.cloud.google.com/193)
  * [ 194 Automatic retry configuration ](https://docs.cloud.google.com/194)
  * [ 200 Precedent ](https://docs.cloud.google.com/200)
  * [ 202 Fields ](https://docs.cloud.google.com/202)
  * [ 203 Field behavior documentation ](https://docs.cloud.google.com/203)
  * [ 205 Beta-blocking changes ](https://docs.cloud.google.com/205)
  * [ 210 Unicode ](https://docs.cloud.google.com/210)
  * [ 211 Authorization checks ](https://docs.cloud.google.com/211)
  * [ 213 Common components ](https://docs.cloud.google.com/213)
  * [ 214 Resource expiration ](https://docs.cloud.google.com/214)
  * [ 215 API-specific protos ](https://docs.cloud.google.com/215)
  * [ 216 States ](https://docs.cloud.google.com/216)
  * [ 217 Unreachable resources ](https://docs.cloud.google.com/217)
  * [ 231 Batch methods: Get ](https://docs.cloud.google.com/231)
  * [ 233 Batch methods: Create ](https://docs.cloud.google.com/233)
  * [ 234 Batch methods: Update ](https://docs.cloud.google.com/234)
  * [ 235 Batch methods: Delete ](https://docs.cloud.google.com/235)
  * [ 236 Policy preview ](https://docs.cloud.google.com/236)

Errors  
---  
Number| 193  
Permalink| [google.aip.dev/193](https://google.aip.dev/193)  
State| Approved  
Created| 2019-07-26  
Updated| 2019-07-26  
  
Contents

  * Guidance
    * Status.message
    * Status.code
    * Status.details
    * Error messages
    * Partial errors
    * Permission Denied
  * HTTP/1.1+JSON representation
  * Rationale
    * Requiring ErrorInfo
    * Including LocalizedMessage
    * Updating Status.message
  * Further reading
  * Changelog



  * [File Bug](https://github.com/aip-dev/google.aip.dev/issues/)
  * [View source](https://github.com/aip-dev/google.aip.dev/blob/master/aip/general/0193.md)
  * [Edit this page](https://github.com/aip-dev/google.aip.dev/edit/master/aip/general/0193.md)



  1. [ API Improvement Proposals ](https://docs.cloud.google.com/)
  2. [ General AIPs ](https://docs.cloud.google.com/general)
  3. Errors 



#### AIP-193

# Errors

Effective error communication is an important part of designing simple and intuitive APIs. Services returning standardized error responses enable API clients to construct centralized common error handling logic. This common logic simplifies API client applications and eliminates the need for cumbersome custom error handling code.

## Guidance

Services **must** return a [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) message when an API error occurs, and **must** use the canonical error codes defined in [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). More information about the particular codes is available in the [gRPC status code documentation](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md).

Error messages **should** help a reasonably technical user _understand_ and _resolve_ the issue, and **should not** assume that the user is an expert in your particular API. Additionally, error messages **must not** assume that the user will know anything about its underlying implementation.

Error messages **should** be brief but actionable. Any extra information **should** be provided in the `details` field. If even more information is necessary, you **should** provide a link where a reader can get more information or ask questions to help resolve the issue. It is also important to [set the right tone](https://developers.google.com/tech-writing/error-messages/set-tone) when writing messages.

The following sections describe the fields of `google.rpc.Status`.

### Status.message

The `message` field is a developer-facing, human-readable "debug message" which **should** be in English. (Localized messages are expressed using a `LocalizedMessage` within the `details` field. See `LocalizedMessage` for more details.) Any dynamic aspects of the message **must** be included as metadata within the `ErrorInfo` that appears in `details`.

The message is considered a problem description. It is intended for developers to understand the problem and is more detailed than [`ErrorInfo.reason`](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto#L57), discussed later.

Messages **should** use simple descriptive language that is easy to understand (without technical jargon) to clearly state the problem that results in an error, and offer an actionable resolution to it.

For pre-existing (brownfield) APIs which have previously returned errors without machine-readable identifiers, the value of `message` **must** remain the same for any given error. For more information, see Changing Error Messages.

### Status.code

The `code` field is the status code, which **must** be the numeric value of one of the elements of the [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto) enum.

For example, the value `5` is the numeric value of the `NOT_FOUND` enum element.

### Status.details

The `details` field allows messages with additional error information to be included in the error response, each packed in a `google.protobuf.Any` message.

Google defines a set of [standard detail payloads](https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto) for error details, which cover most common needs for API errors. Services **should** use these standard detail payloads when feasible.

Each type of detail payload **must** be included at most once. For example, there **must not** be more than one [`BadRequest`](https://github.com/googleapis/googleapis/blob/477a59d764428136ba1d857a9633c0d231de6efa/google/rpc/error_details.proto#L168-L218) message in the `details`, but there **may** be a `BadRequest` and a [`PreconditionFailure`](https://github.com/googleapis/googleapis/blob/6f3fcc058ff29989f6d3a71557a44b5e81b897bd/google/rpc/error_details.proto#L139-L166).

All error responses **must** include an `ErrorInfo` within `details`. This provides machine-readable identifiers so that users can write code against specific aspects of the error.

The following sections describe the most common standard detail payloads.

#### ErrorInfo

The [`ErrorInfo`](https://github.com/googleapis/googleapis/blob/6f3fcc058ff29989f6d3a71557a44b5e81b897bd/google/rpc/error_details.proto#L27-L76) message is the primary way to send a machine-readable identifier. Contextual information **should** be included in `metadata` in `ErrorInfo` and **must** be included if it appears within an error message.

The `reason` field is a short snake_case description of the cause of the error. Error reasons are unique within a particular domain of errors. The reason **must** be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`. (This is UPPER_SNAKE_CASE, without leading or trailing underscores, and without leading digits.)

The reason **should** be terse, but meaningful enough for a human reader to understand what the reason refers to.

Good examples:

  * `CPU_AVAILABILITY`
  * `NO_STOCK`
  * `CHECKED_OUT`
  * `AVAILABILITY_ERROR`



Bad examples:

  * `THE_BOOK_YOU_WANT_IS_NOT_AVAILABLE` (overly verbose)
  * `ERROR` (too general)



The `domain` field is the logical grouping to which the `reason` belongs. The domain **must** be a globally unique value, and is typically the name of the service that generated the error, e.g. `pubsub.googleapis.com`.

The (reason, domain) pair form a machine-readable way of identifying a particular error. Services **must** use the same (reason, domain) pair for the same error, and **must not** use the same (reason, domain) pair for logically different errors. The decision about whether two errors are "the same" or not is not always clear, but **should** generally be considered in terms of the expected action a client might take to resolve them.

The `metadata` field is a map of key/value pairs providing additional dynamic information as context. Each key within `metadata` **must** be at most 64 characters long, and conform to the regular expression `[a-z][a-zA-Z0-9-_]+`.

Any request-specific information which contributes to the `Status.message` or `LocalizedMessage.message` messages **must** be represented within `metadata`. This practice is critical so that machine actors do not need to parse error messages to extract information.

For example consider the following message:

> An <e2-medium> VM instance with <local-ssd=3,nvidia-t4=2> is currently unavailable in the <us-east1-a> zone. Consider trying your request in the <us-central1-f,us-central1-c> zone(s), which currently has/have capacity to accommodate your request. Alternatively, you can try your request again with a different VM hardware configuration or at a later time. For more information, see the troubleshooting documentation.

The `ErrorInfo.metadata` map for the same error could be:

  * `"zone": "us-east1-a"`
  * `"vmType": "e2-medium"`
  * `"attachment": "local-ssd=3,nvidia-t4=2"`
  * `"zonesWithCapacity": "us-central1-f,us-central1-c"`



Additional contextual information that does not appear in an error message **may** also be included in `metadata` to allow programmatic use by the client.

The metadata included for any given (reason,domain) pair can evolve over time:

  * New keys **may** be included
  * All keys that have been included **must** continue to be included (but may have empty values)



In other words, once a user has observed a given key for a (reason, domain) pair, the service **must** allow them to rely on it continuing to be present in the future.

The set of keys provided in each (reason, domain) pair is independent from other pairs, but services **should** aim for consistent key naming. For example, two error reasons within the same domain should not use metadata keys of `vmType` and `virtualMachineType`.

#### LocalizedMessage

[`google.rpc.LocalizedMessage`](https://github.com/googleapis/googleapis/blob/e9897ed945336e2dc967b439ac7b4be6d2c62640/google/rpc/error_details.proto#L275-L285) is used to provide an error message which **should** be localized to a user-specified locale where possible.

If the `Status.message` field has a sub-optimal value which cannot be changed due to the constraints in the Changing Error Messages section, `LocalizedMessage` **may** be used to provide a better error message even when no user-specified locale is available.

Regardless of how the locale for the message was determined, both the `locale` and `message` fields **must** be populated.

The `locale` field specifies the locale of the message, following [IETF bcp47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) (Tags for Identifying Languages). Example values: `"en-US"`, `"fr-CH"`, `"es-MX"`.

The `message` field contains the localized text itself. This **should** include a brief description of the error and a call to action to resolve the error. The message **should** include contextual information to make the message as specific as possible. Any contextual information in the message **must** be included in `ErrorInfo.metadata`. See `ErrorInfo` for more details of how contextual information may be included in a message and the corresponding metadata.

The `LocalizedMessage` payload **should** contain the complete resolution to the error. If more information is needed than can reasonably fit in this payload, then additional resolution information **must** be provided in a `Help` payload. See the Help section for guidance.

#### Help

When other textual error messages (in `Status.message` or `LocalizedMessage.message`) don't provide the user sufficient context or actionable next steps, or if there are multiple points of failure that need to be considered in troubleshooting, a link to supplemental troubleshooting documentation **must** be provided in the `Help` payload.

Provide this information in addition to a clear problem definition and actionable resolution, not as an alternative to them. The linked documentation **must** clearly relate to the error. If a single page contains information about multiple errors, the `ErrorInfo.reason` value **must** be used to narrow down the relevant information.

The `description` field is a textual description of the linked information. This **must** be suitable to display to a user as text for a hyperlink. This **must** be plain text (not HTML, Markdown etc).

Example `description` value: `"Troubleshooting documentation for STOCKOUT errors"`

The `url` field is the URL to link to. This **must** be an absolute URL, including scheme.

Example `url` value: `"https://cloud.google.com/compute/docs/resource-error"`

For publicly-documented services, even those with access controls on actual usage, the linked content **must** be accessible without authentication.

For privately-documented services, the linked content **may** require authentication.

### Error messages

Textual error messages can be present in both `Status.message` and `LocalizedMessage.message` fields. Messages **should** be succinct but actionable, with request-specific information (such as a resource name or region) providing precise details where appropriate. Any request-specific details **must** be present in `ErrorInfo.metadata`.

#### Changing error messages

Changing the content of `Status.message` over time must be done carefully, to avoid breaking clients who have previously had to rely on the message for all information. See the rationale section for more details.

For a given RPC:

  * If the RPC has _always_ returned `ErrorInfo` with machine-readable information, the content of `Status.message` **may** change over time. (For example, the API producer may provide a clearer explanation, or more request-specific information.)
  * Otherwise, the content of `Status.message` **must** be stable, providing the same text with the same request-specific information. Instead of changing `Status.message`, the API **should** include a `LocalizedMessage` within `Status.details`.



Even if an RPC has always returned `ErrorInfo`, the API **may** keep the existing `Status.message` stable and add a `LocalizedMessage` within `Status.details`.

The content of `LocalizedMessage.details` **may** change over time.

### Partial errors

APIs **should not** support partial errors. Partial errors add significant complexity for users, because they usually sidestep the use of error codes, or move those error codes into the response message, where the user **must** write specialized error handling logic to address the problem.

However, occasionally partial errors are necessary, particularly in bulk operations where it would be hostile to users to fail an entire large request because of a problem with a single entry.

Methods that require partial errors **should** use [long-running operations](https://docs.cloud.google.com/151), and the method **should** put partial failure information in the metadata message. The errors themselves **must** still be represented with a [`google.rpc.Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) object.

### Permission Denied

If the user does not have permission to access the resource or parent, regardless of whether or not it exists, the service **must** error with `PERMISSION_DENIED` (HTTP 403). Permission **must** be checked prior to checking if the resource or parent exists.

If the user does have proper permission, but the requested resource or parent does not exist, the service **must** error with `NOT_FOUND` (HTTP 404).

## HTTP/1.1+JSON representation

When clients use HTTP/1.1 as per [AIP-127](https://docs.cloud.google.com/127), the error information is returned in the body of the response, as a JSON object. For backward compatibility reasons, this does not map precisely to `google.rpc.Status`, but contains the same core information. The schema is defined in the following proto:
    
    
    message Error {
      message Status {
        // The HTTP status code that corresponds to `google.rpc.Status.code`.
        int32 code = 1;
        // This corresponds to `google.rpc.Status.message`.
        string message = 2;
        // This is the enum version for `google.rpc.Status.code`.
        google.rpc.Code status = 4;
        // This corresponds to `google.rpc.Status.details`.
        repeated google.protobuf.Any details = 5;
      }
    
      Status error = 1;
    }
    

The most important difference is that the `code` field in the JSON is an HTTP status code, _not_ the direct value of `google.rpc.Status.code`. For example, a `google.rpc.Status` message with a `code` value of 5 would be mapped to an object including the following code-related fields (as well as the message, details etc):
    
    
    {
      "error": {
        "code": 404,          // The HTTP status code for "not found"
        "status": "NOT_FOUND" // The name in google.rpc.Code for value 5
      }
    }
    

The following JSON shows a fully populated HTTP/1.1+JSON representation of an error response.
    
    
    {
      "error": {
        "code": 429,
        "message": "The zone 'us-east1-a' does not have enough resources available to fulfill the request. Try a different zone, or try again later.",
        "status": "RESOURCE_EXHAUSTED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "RESOURCE_AVAILABILITY",
            "domain": "compute.googleapis.com",
            "metadata": {
              "zone": "us-east1-a",
              "vmType": "e2-medium",
              "attachment": "local-ssd=3,nvidia-t4=2",
              "zonesWithCapacity": "us-central1-f,us-central1-c"
            }
          },
          {
            "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
            "locale": "en-US",
            "message": "An <e2-medium> VM instance with <local-ssd=3,nvidia-t4=2> is currently unavailable in the <us-east1-a> zone. Consider trying your request in the <us-central1-f,us-central1-c> zone(s), which currently has/have capacity to accommodate your request. Alternatively, you can try your request again with a different VM hardware configuration or at a later time. For more information, see the troubleshooting documentation."
          },
          {
            "@type": "type.googleapis.com/google.rpc.Help",
            "links": [
              {
                "description": "Additional information on this error",
                "url": "https://cloud.google.com/compute/docs/resource-error"
              }
            ]
          }
        ]
      }
    }
    

## Rationale

### Requiring ErrorInfo

`ErrorInfo` is required because it further identifies an error. With only approximately twenty [available values](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto) for `Status.status`, it is difficult to disambiguate one error from another across an entire [API Service](https://cloud.google.com/apis/design/glossary#api_service).

Also, error messages often contain dynamic segments that express variable information, so there needs to be machine-readable component of _every_ error response that enables clients to use such information programmatically.

### Including LocalizedMessage

`LocalizedMessage` was selected as the location to present alternate error messages. While `LocalizedMessage` **may** use a locale specified in the request, a service **may** provide a `LocalizedMessage` even without a user-specified locale, typically to provide a better error message in situations where `Status.message` cannot be changed. Where the locale is not specified by the user, it **should** be `en-US` (US English).

A service **may** include `LocalizedMessage` even when the same message is provided in `Status.message` and when localization into a user-specified locale is not supported. Reasons for this include:

  * An intention to support user-specified localization in the near future, allowing clients to consistently use `LocalizedMessage` and not change their error-reporting code when the functionality is introduced.
  * Consistency across all RPCs within a service: if some RPCs include `LocalizedMessage` and some only use `Status.message` for error messages, clients have to be aware of which RPCs will do what, or implement a fall-back mechanism. Providing `LocalizedMessage` on all RPCs allows simple and consistent client code to be written.



### Updating Status.message

If a client has ever observed an error with `Status.message` populated (which it always will be) but without `ErrorInfo`, the developer of that client may well have had to resort to parsing `Status.message` in order to find out information beyond just what `Status.code` conveys. That information may be found by matching specific text (e.g. "Connection closed with unknown cause") or by parsing the message to find out metadata values (e.g. a region with insufficient resources). At that point, `Status.message` is implicitly part of the API contract, so **must not** be updated - that would be a breaking change. This is one reason for introducing `LocalizedMessage` into the `Status.details`.

RPCs which have **always** included `ErrorInfo` are in a better position: the contract is then more about the stability of `ErrorInfo` for any given error. The reason and domain need to be consistent over time, and the metadata provided for any given (reason,domain) can only be expanded. It's still possible that clients could be parsing `Status.message` instead of using `ErrorInfo`, but they will always have had a more robust option available to them.

## Further reading

  * For which error codes to retry, see [AIP-194](https://docs.cloud.google.com/194).
  * For how to retry errors in client libraries, see [AIP-4221](https://docs.cloud.google.com/4221).



## Changelog

  * **2024-10-18** : Rewrite/restructure for clarity.
  * **2024-01-10** : Incorporate guidance for writing effective messages.
  * **2023-05-17** : Change the recommended language for `Status.message` to be the service's native language rather than English.
  * **2023-05-17** : Specify requirements for changing error messages.
  * **2023-05-10** : Require [`ErrorInfo`](https://github.com/googleapis/googleapis/blob/6f3fcc058ff29989f6d3a71557a44b5e81b897bd/google/rpc/error_details.proto#L27-L76) for all error responses.
  * **2023-05-04** : Require uniqueness by message type for error details.
  * **2022-11-04** : Added guidance around PERMISSION_DENIED errors previously found in other AIPs.
  * **2022-08-12** : Reworded/Simplified intro to add clarity to the intent.
  * **2020-01-22** : Added a reference to the [`ErrorInfo`](https://github.com/googleapis/googleapis/blob/6f3fcc058ff29989f6d3a71557a44b5e81b897bd/google/rpc/error_details.proto#L27-L76) message.
  * **2019-10-14** : Added guidance restricting error message mutability to if there is a machine-readable identifier present.
  * **2019-09-23** : Added guidance about error message strings being able to change.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see [content licensing](https://docs.cloud.google.com/licensing).
