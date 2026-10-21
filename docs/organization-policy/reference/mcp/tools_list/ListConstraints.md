---
url: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints/
title: MCP Tools Reference: orgpolicy.googleapis.com \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:43.989599+00:00
---

# MCP Tools Reference: orgpolicy.googleapis.com  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  MCP Tools Reference: orgpolicy.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `ListConstraints`

Lists constraints that can be applied to a specific resource (project, folder, or organization). Use this to discover what constraints are available to enforce.

The following code sample shows how to use `curl` to call the `ListConstraints` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://orgpolicy.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "ListConstraints",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The request sent to the `ListConstraints` method.

### ListConstraintsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The Google Cloud resource that parents the constraint. Must be in one of the following forms:

  * `projects/{project_number}`
  * `projects/{project_id}`
  * `folders/{folder_number}`
  * `organizations/{organization_number}`

  
`pageSize` |  `integer` Size of the pages to be returned. This is not used, but the server may at any point start using this field to limit page size.  
`pageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start using this field.  
  
## Output Schema

The response returned from the `ListConstraints` method.

### ListConstraintsResponse

JSON representation  
---  
      
    
    {
      "constraints": [
        {
          object ([Constraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Constraint))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`constraints[]` |  `object (`[Constraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Constraint)`)` The collection of constraints that are available on the targeted resource.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used.  
  
### Constraint

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "constraintDefault": enum ([ConstraintDefault](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ConstraintDefault)),
      "supportsDryRun": boolean,
      "equivalentConstraint": string,
      "supportsSimulation": boolean,
    
      // Union field constraint_type can be only one of the following:
      "listConstraint": {
        object ([ListConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ListConstraint))
      },
      "booleanConstraint": {
        object ([BooleanConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.BooleanConstraint))
      }
      // End of list of possible types for union field constraint_type.
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the constraint. Must be in one of the following forms:

  * `projects/{project_number}/constraints/{constraint_name}`
  * `folders/{folder_number}/constraints/{constraint_name}`
  * `organizations/{organization_number}/constraints/{constraint_name}`

For example, "/projects/123/constraints/compute.disableSerialPortAccess".  
`displayName` |  `string` The human readable name.Mutable.  
`description` |  `string` Detailed description of what this constraint controls as well as how and where it is enforced.Mutable.  
`constraintDefault` |  `enum (`[ConstraintDefault](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ConstraintDefault)`)` The evaluation behavior of this constraint in the absence of a policy.  
`supportsDryRun` |  `boolean` Shows if dry run is supported for this constraint or not.  
`equivalentConstraint` |  `string` Defines the equivalent constraint name, if it exists. Managed constraints can have an equivalent legacy managed constraint, and legacy managed constraints can have an equivalent managed constraint. For example, "constraints/iam.disableServiceAccountKeyUpload" is equivalent to "constraints/iam.managed.disableServiceAccountKeyUpload".  
`supportsSimulation` |  `boolean` Shows if simulation is supported for this constraint or not.  
Union field `constraint_type`. The type of restrictions for this `Constraint`.Immutable after creation. `constraint_type` can be only one of the following:  
`listConstraint` |  `object (`[ListConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ListConstraint)`)` Defines this constraint as being a list constraint.  
`booleanConstraint` |  `object (`[BooleanConstraint](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.BooleanConstraint)`)` Defines this constraint as being a boolean constraint.  
  
### ListConstraint

JSON representation  
---  
      
    
    {
      "supportsIn": boolean,
      "supportsUnder": boolean
    }  
  
Fields  
---  
`supportsIn` |  `boolean` Indicates whether values grouped into categories can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"in:Python"` would match any value in the 'Python' group.  
`supportsUnder` |  `boolean` Indicates whether subtrees of the Resource Manager resource hierarchy can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"under:folders/123"` would match any resource under the 'folders/123' folder.  
  
### BooleanConstraint

JSON representation  
---  
      
    
    {
      "customConstraintDefinition": {
        object ([CustomConstraintDefinition](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.CustomConstraintDefinition))
      }
    }  
  
Fields  
---  
`customConstraintDefinition` |  `object (`[CustomConstraintDefinition](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.CustomConstraintDefinition)`)` Custom constraint definition. Defines this as a managed constraint.  
  
### CustomConstraintDefinition

JSON representation  
---  
      
    
    {
      "resourceTypes": [
        string
      ],
      "methodTypes": [
        enum ([MethodType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.MethodType))
      ],
      "condition": string,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ActionType)),
      "parameters": {
        string: {
          object ([Parameter](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Parameter))
        },
        ...
      }
    }  
  
Fields  
---  
`resourceTypes[]` |  `string` The resource instance type that this policy applies to, in the format `<service name>/<type>`. Example:

  * `compute.googleapis.com/Instance`.

  
`methodTypes[]` |  `enum (`[MethodType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.MethodType)`)` All the operations being applied for this constraint.  
`condition` |  `string` Org policy condition/expression. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")` or, `resource.management.auto_upgrade == true`The max length of the condition is 1000 characters.  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.ActionType)`)` Allow or deny type.  
`parameters` |  `map (key: string, value: object (`[Parameter](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Parameter)`))` Stores the structure of `[`Parameters`](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Parameter)` used by the constraint condition. The key of `map` represents the name of the parameter.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### ParametersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Parameter](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Parameter))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Parameter](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Parameter)`)`  
  
### Parameter

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Type)),
      "defaultValue": value,
      "validValuesExpr": string,
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Metadata))
      },
      "item": enum ([Type](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Type)`)` Type of the parameter.  
`defaultValue` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Sets the value of the parameter in an assignment if no value is given.  
`validValuesExpr` |  `string` Provides a CEL expression to specify the acceptable parameter values during assignment. For example, parameterName in ("parameterValue1", "parameterValue2").  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Metadata)`)` Defines subproperties primarily used by the UI to display user-friendly information.  
`item` |  `enum (`[Type](https://docs.cloud.google.com/organization-policy/reference/mcp/tools_list/ListConstraints#Output.Schema.Type)`)` Determines the parameter's value structure. For example, `LIST<STRING>` can be specified by defining `type: LIST`, and `item: STRING`.  
  
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
  
### Metadata

JSON representation  
---  
      
    
    {
      "description": string
    }  
  
Fields  
---  
`description` |  `string` Detailed description of what this `parameter` is and its use. Mutable.  
  
### ConstraintDefault

Specifies the default behavior in the absence of any policy for the constraint. This must not be `CONSTRAINT_DEFAULT_UNSPECIFIED`.

Immutable after creation.

Enums  
---  
`CONSTRAINT_DEFAULT_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if set.  
`ALLOW` | Indicate that all values are allowed for list constraints. Indicate that enforcement is off for boolean constraints.  
`DENY` | Indicate that all values are denied for list constraints. Indicate that enforcement is on for boolean constraints.  
  
### MethodType

The operation for which this constraint will be applied. To apply this constraint only when creating new resources, set `method_types` to `CREATE` only. To apply this constraint when creating or updating resources, set `method_types` to `CREATE` and `UPDATE`.

`UPDATE`-only custom constraints are not supported. Use `CREATE` or `CREATE, UPDATE`.

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
  
### Type

All valid types of parameter.

Enums  
---  
`TYPE_UNSPECIFIED` | This is only used for distinguishing unset values, and results in an error if used.  
`LIST` | List parameter type.  
`STRING` | String parameter type.  
`BOOLEAN` | Boolean parameter type.  
  
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
