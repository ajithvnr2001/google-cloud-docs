---
url: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListCustomConstraints/
title: MCP Tools Reference: orgpolicy.googleapis.com \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:45.755082+00:00
---

# MCP Tools Reference: orgpolicy.googleapis.com  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListCustomConstraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  MCP Tools Reference: orgpolicy.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `ListCustomConstraints`

Lists all custom constraints defined for an organization.

The following code sample shows how to use `curl` to call the `ListCustomConstraints` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://orgpolicy.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "ListCustomConstraints",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The request sent to the `ListCustomConstraints` method.

### ListCustomConstraintsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The target Google Cloud resource that parents the set of custom constraints that will be returned from this call. Must be in one of the following forms:

  * `organizations/{organization_id}`

  
`pageSize` |  `integer` Size of the pages to be returned. This is not used, but the server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start using this field.  
  
## Output Schema

The response returned from the `ListCustomConstraints` method. It will be empty if no custom or managed constraints are set on the organization resource.

### ListCustomConstraintsResponse

JSON representation  
---  
      
    
    {
      "customConstraints": [
        {
          object ([CustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.CustomConstraint))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`customConstraints[]` |  `object (`[CustomConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.CustomConstraint)`)` All custom and managed constraints that exist on the organization resource. It will be empty if no custom constraints are set.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start supplying a valid token.  
  
### CustomConstraint

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.ActionType)),
      "displayName": string,
      "description": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Name of the constraint. This is unique within the organization. The name must be of the form:

  * `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms`The max length is 71 characters and the minimum length is 1. Note that the prefix `organizations/{organization_id}/customConstraints/custom.` is not counted.  
`resourceTypes[]` |  `string` Immutable. The resource instance type on which this policy applies. Format will be of the form : `<service name>/<type>` Example:

  * `compute.googleapis.com/Instance`.

  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.MethodType)`)` All the operations being applied for this constraint.  
`condition` |  `string` A Common Expression Language (CEL) condition which is used in the evaluation of the constraint. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")` or, `resource.management.auto_upgrade == true`The max length of the condition is 1000 characters.  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/CreateCustomConstraint#Input.Schema.ActionType)`)` Allow or deny type.  
`displayName` |  `string` One line display name for the UI. The max length of the display_name is 200 characters.  
`description` |  `string` Detailed information about this custom policy constraint. The max length of the description is 2000 characters.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` methods were called.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### MethodType

The operation for which this constraint will be applied. To apply this constraint only when creating new resources, set `method_types` to `CREATE` only. To apply this constraint when creating or updating resources, set `method_types` to `CREATE` and `UPDATE`.

`UPDATE` only custom constraints are not supported. Use `CREATE` or `CREATE, UPDATE`.

Enums  
---  
`METHOD_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`CREATE` | Constraint applied when creating the resource.  
`UPDATE` | Constraint applied when updating the resource.  
`DELETE` | Constraint applied when deleting the resource. Not supported.  
`REMOVE_GRANT` | Constraint applied when removing an IAM grant.  
`GOVERN_TAGS` | Constraint applied when enforcing forced tagging.  
  
### ActionType

Allow or deny type.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`ALLOW` | Allowed action type.  
`DENY` | Deny action type.  
  
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
