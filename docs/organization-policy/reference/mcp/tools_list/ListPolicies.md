---
url: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies/
title: MCP Tools Reference: orgpolicy.googleapis.com \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:43.876052+00:00
---

# MCP Tools Reference: orgpolicy.googleapis.com  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  MCP Tools Reference: orgpolicy.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `ListPolicies`

Retrieves all explicit policies set on a particular resource. Useful for auditing what policies are directly applied.

The following code sample shows how to use `curl` to call the `ListPolicies` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://orgpolicy.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "ListPolicies",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The request sent to the `ListPolicies` method.

### ListPoliciesRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The target Google Cloud resource that parents the set of constraints and policies that will be returned from this call. Must be in one of the following forms:

  * `projects/{project_number}`
  * `projects/{project_id}`
  * `folders/{folder_number}`
  * `organizations/{organization_number}`

  
`pageSize` |  `integer` Size of the pages to be returned. This is not used, but the server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start using this field.  
  
## Output Schema

The response returned from the `ListPolicies` method. It will be empty if no policies are set on the resource.

### ListPoliciesResponse

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([Policy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.Policy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policies[]` |  `object (`[Policy](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.Policy)`)` All policies that exist on the resource. It will be empty if no policies are set.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start supplying a valid token.  
  
### Policy

JSON representation  
---  
      
    
    {
      "name": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec))
      },
      "alternate": {
        object ([AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.AlternatePolicySpec))
      },
      "dryRunSpec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint that this policy configures:

  * `projects/{project_number}/policies/{constraint_name}`
  * `folders/{folder_number}/policies/{constraint_name}`
  * `organizations/{organization_number}/policies/{constraint_name}`

For example, `projects/123/policies/compute.disableSerialPortAccess`.Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec)`)` Basic information about the organization policy.  
`alternate  
**(deprecated)**` |  `object (`[AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.AlternatePolicySpec)`)` This item is deprecated!Deprecated.  
`dryRunSpec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec)`)` Dry-run policy. Audit-only policy, can be used to monitor how the policy would have impacted the existing and future resources if it's enforced.  
`etag` |  `string` Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This entity tag (ETag) is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
  
### PolicySpec

JSON representation  
---  
      
    
    {
      "etag": string,
      "updateTime": string,
      "rules": [
        {
          object ([PolicyRule](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicyRule))
        }
      ],
      "inheritFromParent": boolean,
      "reset": boolean
    }  
  
Fields  
---  
`etag` |  `string` An opaque tag indicating the current version of the policySpec, used for concurrency control.This field is ignored if used in a `CreatePolicy` request.When the policy is returned from either a `GetPolicy` or a `ListPolicies` request, this entity tag (ETag) indicates the version of the current policySpec to use when executing a read-modify-write loop.When the policy is returned from a `GetEffectivePolicy` request, the ETag will be unset.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time stamp this was previously updated. This represents the last time a call to `CreatePolicy` or `UpdatePolicy` was made for that policy.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rules[]` |  `object (`[PolicyRule](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicyRule)`)` In policies for boolean constraints, the following requirements apply:

  * There must be exactly one policy rule where a condition is unset.
  * Boolean policy rules with conditions must set `enforced` to the opposite of the policy rule without a condition.
  * During policy evaluation, policy rules with conditions that are true for a target resource take precedence.

  
`inheritFromParent` |  `boolean` Determines the inheritance behavior for this policy.If `inherit_from_parent` is true, policy rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the new root for evaluation. This field can be set only for policies that configure list constraints.  
`reset` |  `boolean` Ignores policies set above this resource and restores the `constraint_default` enforcement behavior of the specific constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.  
  
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
  
### PolicyRule

JSON representation  
---  
      
    
    {
      "condition": {
        object ([Expr](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.Expr))
      },
      "parameters": {
        object
      },
    
      // Union field kind can be only one of the following:
      "values": {
        object ([StringValues](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.StringValues))
      },
      "allowAll": boolean,
      "denyAll": boolean,
      "enforce": boolean
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.Expr)`)` A condition that determines whether this rule is used to evaluate the policy.When set, the `google.type.Expr.expression` field must contain 1 to 10 subexpressions, joined by the `||` or `&&` operators. Each subexpression must use the `resource.matchTag()`, `resource.matchTagId()`, `resource.hasTagKey()`, or `resource.hasTagKeyId()` Common Expression Language (CEL) function.The `resource.matchTag()` function takes the following arguments:

  * `key_name`: the namespaced name of the tag key, with the organization ID and a slash (`/`) as a prefix; for example, `123456789012/environment`
  * `value_name`: the short name of the tag value

For example: `resource.matchTag('123456789012/environment, 'prod')`The `resource.matchTagId()` function takes the following arguments:

  * `key_id`: the permanent ID of the tag key; for example, `tagKeys/123456789012`
  * `value_id`: the permanent ID of the tag value; for example, `tagValues/567890123456`

For example: `resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')`The `resource.hasTagKey()` function takes the following argument:

  * `key_name`: the namespaced name of the tag key, with the organization ID and a slash (`/`) as a prefix; for example, `123456789012/environment`

For example: `resource.hasTagKey('123456789012/environment')`The `resource.hasTagKeyId()` function takes the following arguments:

  * `key_id`: the permanent ID of the tag key; for example, `tagKeys/123456789012`

For example: `resource.hasTagKeyId('tagKeys/123456789012')`  
`parameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Required for managed constraints if parameters are defined. Passes parameter values when policy enforcement is enabled. Ensure that parameter value types match those defined in the constraint definition. For example:
    
    
    {
      "allowedLocations" : ["us-east1", "us-west1"],
      "allowAll" : true
    }
      
  
Union field `kind`.`kind` can be only one of the following:  
`values` |  `object (`[StringValues](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.StringValues)`)` List of values to be used for this policy rule. This field can be set only in policies for list constraints.  
`allowAll` |  `boolean` Setting this to true means that all values are allowed. This field can be set only in policies for list constraints.  
`denyAll` |  `boolean` Setting this to true means that all values are denied. This field can be set only in policies for list constraints.  
`enforce` |  `boolean` If `true`, then the policy is enforced. If `false`, then any configuration is acceptable. This field can be set in policies for boolean constraints, custom constraints and managed constraints.  
  
### StringValues

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ]
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource.  
`deniedValues[]` |  `string` List of values denied at this resource.  
  
### Expr

JSON representation  
---  
      
    
    {
      "expression": string,
      "title": string,
      "description": string,
      "location": string
    }  
  
Fields  
---  
`expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### AlternatePolicySpec

JSON representation  
---  
      
    
    {
      "launch": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec))
      }
    }  
  
Fields  
---  
`launch` |  `string` Reference to the launch that will be used while audit logging and to control the launch. Set only in the alternate policy.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListPolicies#Output.Schema.PolicySpec)`)` Specify constraint for configurations of Google Cloud resources.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
