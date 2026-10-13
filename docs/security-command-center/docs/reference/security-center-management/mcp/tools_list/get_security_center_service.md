---
url: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/get_security_center_service/
title: MCP Tools Reference: securitycentermanagement.googleapis.com \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:19.316178+00:00
---

# MCP Tools Reference: securitycentermanagement.googleapis.com  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/get_security_center_service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  MCP Tools Reference: securitycentermanagement.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_security_center_service`

Get service settings for the specified Security Command Center service

The following code sample shows how to use `curl` to call the `get_security_center_service` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://securitycentermanagement.googleapis.com/mcp/manage-services' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_security_center_service",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `SecurityCenterManagement.GetSecurityCenterService`.

### GetSecurityCenterServiceRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "showEligibleModulesOnly": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. The Security Command Center service to retrieve, in one of the following formats:

  * organizations/{organization}/locations/{location}/securityCenterServices/{service}
  * folders/{folder}/locations/{location}/securityCenterServices/{service}
  * projects/{project}/locations/{location}/securityCenterServices/{service}
  * projects/{project}/locations/{location}/clusters/{cluster}/securityCenterServices/{service}

The following values are valid for `{service}`:

  * `container-threat-detection`
  * `event-threat-detection`
  * `security-health-analytics`
  * `vm-threat-detection`
  * `web-security-scanner`
  * `vm-threat-detection-aws`
  * `cloud-run-threat-detection`
  * `external-exposure`
  * `vm-manager`
  * `ec2-vulnerability-assessment`
  * `gce-vulnerability-assessment`
  * `azure-vulnerability-assessment`
  * `notebook-security-scanner`
  * `artifact-analysis`
  * `agent-engine-threat-detection`

  
`showEligibleModulesOnly` |  `boolean` Optional. Indicates whether to show only modules that are available in your Security Command Center service tier. By default, all modules are shown.  
  
## Output Schema

Represents a particular Security Command Center service. This includes settings information such as top-level enablement in addition to individual module settings. Service settings can be configured at the organization, folder, or project level. Service settings at the organization or folder level are inherited by those in descendant folders and projects.

### SecurityCenterService

JSON representation  
---  
      
    
    {
      "name": string,
      "intendedEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)),
      "effectiveEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)),
      "modules": {
        string: {
          object ([ModuleSettings](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.ModuleSettings))
        },
        ...
      },
      "updateTime": string,
      "serviceConfig": {
        object
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the service, in one of the following formats:

  * `organizations/{organization}/locations/{location}/securityCenterServices/{service}`
  * `folders/{folder}/locations/{location}/securityCenterServices/{service}`
  * `projects/{project}/locations/{location}/securityCenterServices/{service}`
  * `projects/{project}/locations/{location}/clusters/{cluster}/securityCenterServices/{service}`

The following values are valid for `{service}`:

  * `container-threat-detection`
  * `event-threat-detection`
  * `security-health-analytics`
  * `vm-threat-detection`
  * `web-security-scanner`
  * `vm-threat-detection-aws`
  * `cloud-run-threat-detection`
  * `external-exposure`
  * `vm-manager`
  * `ec2-vulnerability-assessment`
  * `gce-vulnerability-assessment`
  * `azure-vulnerability-assessment`
  * `notebook-security-scanner`
  * `artifact-analysis`
  * `agent-engine-threat-detection`

  
`intendedEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)`)` Optional. The intended enablement state for the service at its level of the resource hierarchy. A `DISABLED` state will override all module enablement states to `DISABLED`.  
`effectiveEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)`)` Output only. The effective enablement state for the service at its level of the resource hierarchy. If the intended state is set to `INHERITED`, the effective state will be inherited from the enablement state of an ancestor. This state may differ from the intended enablement state due to billing eligibility or onboarding status.  
`modules` |  `map (key: string, value: object (`[ModuleSettings](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.ModuleSettings)`))` Optional. The module configurations, including the enablement state for the service's modules. The absence of a module in the map implies that its configuration is inherited from its parents.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the service was last updated. This could be due to an explicit user update or due to a side effect of another system change, such as billing subscription expiry.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional service-specific configuration. Not all services will utilize this field.  
  
### ModulesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([ModuleSettings](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.ModuleSettings))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[ModuleSettings](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.ModuleSettings)`)`  
  
### ModuleSettings

JSON representation  
---  
      
    
    {
      "intendedEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)),
      "effectiveEnablementState": enum ([EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState))
    }  
  
Fields  
---  
`intendedEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)`)` Optional. The intended enablement state for the module at its level of the resource hierarchy.  
`effectiveEnablementState` |  `enum (`[EnablementState](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp/tools_list/list_security_center_services#Output.Schema.EnablementState)`)` Output only. The effective enablement state for the module at its level of the resource hierarchy. If the intended state is set to `INHERITED`, the effective state will be inherited from the enablement state of an ancestor. This state may differ from the intended enablement state due to billing eligibility or onboarding status.  
  
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
  
### EnablementState

Represents the possible enablement states for a service or module.

Enums  
---  
`ENABLEMENT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`INHERITED` | State is inherited from the parent resource. Valid as an intended enablement state, but not as an effective enablement state.  
`ENABLED` | State is enabled.  
`DISABLED` | State is disabled.  
`INGEST_ONLY` | Security Command Center is configured to ingest findings from this service, but not to enable this service. This state indicates that Security Command Center is misconfigured. You can't set this state yourself.  
  
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

Last updated 2026-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
