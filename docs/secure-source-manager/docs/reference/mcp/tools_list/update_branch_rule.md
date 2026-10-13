---
url: https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_branch_rule/
title: MCP Tools Reference: securesourcemanager.googleapis.com \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:47.585910+00:00
---

# MCP Tools Reference: securesourcemanager.googleapis.com  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/update_branch_rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-source-manager/docs/authentication)



Send feedback 

#  MCP Tools Reference: securesourcemanager.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_branch_rule`

Update a Secure Source Manager branch rule.

The following code sample shows how to use `curl` to call the `update_branch_rule` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://securesourcemanager.europe-west4.rep.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_branch_rule",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

UpdateBranchRuleRequest is the request to update a branchRule.

### UpdateBranchRuleRequest

JSON representation  
---  
      
    
    {
      "branchRule": {
        object ([BranchRule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule#Input.Schema.BranchRule))
      },
      "validateOnly": boolean,
      "updateMask": string
    }  
  
Fields  
---  
`branchRule` |  `object (`[BranchRule](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule#Input.Schema.BranchRule)`)`  
`validateOnly` |  `boolean` Optional. If set, validate the request and preview the review, but do not actually post it. (<https://google.aip.dev/163>, for declarative friendly)  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to specify the fields to be overwritten in the branchRule resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "*" means full replacement.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### BranchRule

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "includePattern": string,
      "disabled": boolean,
      "requirePullRequest": boolean,
      "minimumReviewsCount": integer,
      "minimumApprovalsCount": integer,
      "requireCodeOwnerApproval": boolean,
      "requireCommentsResolved": boolean,
      "allowStaleReviews": boolean,
      "requireLinearHistory": boolean,
      "requiredStatusChecks": [
        {
          object ([Check](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule#Input.Schema.Check))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. A unique identifier for a BranchRule. The name should be of the format: `projects/{project}/locations/{location}/repositories/{repository}/branchRules/{branch_rule}`  
`uid` |  `string` Output only. Unique identifier of the repository.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`includePattern` |  `string` Optional. The pattern of the branch that can match to this BranchRule. Specified as regex. .* for all branches. Examples: main, (main|release.*). Current MVP phase only support `.*` for wildcard.  
`disabled` |  `boolean` Optional. Determines if the branch rule is disabled or not.  
`requirePullRequest` |  `boolean` Optional. Determines if the branch rule requires a pull request or not.  
`minimumReviewsCount` |  `integer` Optional. The minimum number of reviews required for the branch rule to be matched.  
`minimumApprovalsCount` |  `integer` Optional. The minimum number of approvals required for the branch rule to be matched.  
`requireCodeOwnerApproval` |  `boolean` Optional. Determines if code owners must approve before merging to the branch.  
`requireCommentsResolved` |  `boolean` Optional. Determines if require comments resolved before merging to the branch.  
`allowStaleReviews` |  `boolean` Optional. Determines if allow stale reviews or approvals before merging to the branch.  
`requireLinearHistory` |  `boolean` Optional. Determines if require linear history before merging to the branch.  
`requiredStatusChecks[]` |  `object (`[Check](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/create_branch_rule#Input.Schema.Check)`)` Optional. List of required status checks before merging to the branch.  
  
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
  
### Check

JSON representation  
---  
      
    
    {
      "context": string
    }  
  
Fields  
---  
`context` |  `string` Required. The context of the check.  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
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
        object ([Status](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/close_pull_request#Output.Schema.Status))
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
`error` |  `object (`[Status](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp/tools_list/close_pull_request#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
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

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
