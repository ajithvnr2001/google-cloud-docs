---
url: https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_create_key/
title: MCP Tools Reference: apikeys.googleapis.com \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:41.291209+00:00
---

# MCP Tools Reference: apikeys.googleapis.com  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_create_key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Reference ](https://docs.cloud.google.com/api-keys/docs/apis)



Send feedback 

#  MCP Tools Reference: apikeys.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `apikeys_create_key`

Creates a new API key in the specified project. You can optionally specify restrictions.

The following code sample shows how to use `curl` to call the `apikeys_create_key` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://apikeys.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "apikeys_create_key",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `CreateKey` method.

### CreateKeyRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "key": {
        object ([Key](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.Key))
      },
      "keyId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The project in which the API key is created. The parent field must be in format of "projects//locations/global".  
`key` |  `object (`[Key](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.Key)`)` Required. The API key fields to set at creation time. You can configure only the `display_name`, `restrictions`, and `annotations` fields.  
`keyId` |  `string` User specified key id (optional). If specified, it will become the final component of the key resource name.The id must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the id must match the regular expression: `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.The id must NOT be a UUID-like string.  
  
### Key

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "displayName": string,
      "keyString": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "annotations": {
        string: string,
        ...
      },
      "restrictions": {
        object ([Restrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.Restrictions))
      },
      "etag": string,
      "serviceAccountEmail": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the key. The `name` has the form: `projects/<PROJECT_NUMBER>/locations/global/keys/<KEY_ID>`. For example: `projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2`NOTE: Key is a global resource; hence the only supported value for location is `global`.  
`uid` |  `string` Output only. Unique id in UUID4 format.  
`displayName` |  `string` Human-readable display name of this key that you can modify. The maximum length is 63 characters.  
`keyString` |  `string` Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. A timestamp identifying the time this key was originally created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. A timestamp identifying the time this key was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. A timestamp when this key was deleted. If the resource is not deleted, this must be empty.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`restrictions` |  `object (`[Restrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.Restrictions)`)` Key restrictions.  
`etag` |  `string` A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. See <https://google.aip.dev/154>.  
`serviceAccountEmail` |  `string` Optional. The email address of [the service account](https://cloud.google.com/iam/docs/service-accounts) the key is bound to.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### AnnotationsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Restrictions

JSON representation  
---  
      
    
    {
      "apiTargets": [
        {
          object ([ApiTarget](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.ApiTarget))
        }
      ],
    
      // Union field client_restrictions can be only one of the following:
      "browserKeyRestrictions": {
        object ([BrowserKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.BrowserKeyRestrictions))
      },
      "serverKeyRestrictions": {
        object ([ServerKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.ServerKeyRestrictions))
      },
      "androidKeyRestrictions": {
        object ([AndroidKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.AndroidKeyRestrictions))
      },
      "iosKeyRestrictions": {
        object ([IosKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.IosKeyRestrictions))
      }
      // End of list of possible types for union field client_restrictions.
    }  
  
Fields  
---  
`apiTargets[]` |  `object (`[ApiTarget](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.ApiTarget)`)` A restriction for a specific service and optionally one or more specific methods. Requests are allowed if they match any of these restrictions. If no restrictions are specified, all targets are allowed.  
Union field `client_restrictions`. The websites, IP addresses, Android apps, or iOS apps (the clients) that are allowed to use the key. You can specify only one type of client restrictions per key. `client_restrictions` can be only one of the following:  
`browserKeyRestrictions` |  `object (`[BrowserKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.BrowserKeyRestrictions)`)` The HTTP referrers (websites) that are allowed to use the key.  
`serverKeyRestrictions` |  `object (`[ServerKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.ServerKeyRestrictions)`)` The IP addresses of callers that are allowed to use the key.  
`androidKeyRestrictions` |  `object (`[AndroidKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.AndroidKeyRestrictions)`)` The Android apps that are allowed to use the key.  
`iosKeyRestrictions` |  `object (`[IosKeyRestrictions](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.IosKeyRestrictions)`)` The iOS apps that are allowed to use the key.  
  
### BrowserKeyRestrictions

JSON representation  
---  
      
    
    {
      "allowedReferrers": [
        string
      ]
    }  
  
Fields  
---  
`allowedReferrers[]` |  `string` A list of regular expressions for the referrer URLs that are allowed to make API calls with this key.  
  
### ServerKeyRestrictions

JSON representation  
---  
      
    
    {
      "allowedIps": [
        string
      ]
    }  
  
Fields  
---  
`allowedIps[]` |  `string` A list of the caller IP addresses that are allowed to make API calls with this key.  
  
### AndroidKeyRestrictions

JSON representation  
---  
      
    
    {
      "allowedApplications": [
        {
          object ([AndroidApplication](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.AndroidApplication))
        }
      ]
    }  
  
Fields  
---  
`allowedApplications[]` |  `object (`[AndroidApplication](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_list_keys#Output.Schema.AndroidApplication)`)` A list of Android applications that are allowed to make API calls with this key.  
  
### AndroidApplication

JSON representation  
---  
      
    
    {
      "sha1Fingerprint": string,
      "packageName": string
    }  
  
Fields  
---  
`sha1Fingerprint` |  `string` The SHA1 fingerprint of the application. For example, both sha1 formats are acceptable : DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09 or DA39A3EE5E6B4B0D3255BFEF95601890AFD80709. Output format is the latter.  
`packageName` |  `string` The package name of the application.  
  
### IosKeyRestrictions

JSON representation  
---  
      
    
    {
      "allowedBundleIds": [
        string
      ]
    }  
  
Fields  
---  
`allowedBundleIds[]` |  `string` A list of bundle IDs that are allowed when making API calls with this key.  
  
### ApiTarget

JSON representation  
---  
      
    
    {
      "service": string,
      "methods": [
        string
      ]
    }  
  
Fields  
---  
`service` |  `string` The service for this restriction. It should be the canonical service name, for example: `translate.googleapis.com`. You can use [`gcloud services list`](https://cloud.google.com/sdk/gcloud/reference/services/list) to get a list of services that are enabled in the project.  
`methods[]` |  `string` Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (*) can be used as the last symbol. Valid examples: `google.cloud.translate.v2.TranslateService.GetSupportedLanguage` `TranslateText` `Get*` `translate.googleapis.com.Get*`  
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_create_key#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/api-keys/docs/reference/mcp/tools_list/apikeys_create_key#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
