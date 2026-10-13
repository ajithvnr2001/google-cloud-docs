---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition/
title: MCP Tools Reference: apihub.googleapis.com \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:47.313404+00:00
---

# MCP Tools Reference: apihub.googleapis.com  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  MCP Tools Reference: apihub.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_definition`

Get details about a definition in an API version.

The following sample demonstrate how to use `curl` to invoke the `get_definition` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://apihub.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_definition",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The `GetDefinition` method's request.

### GetDefinitionRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the definition to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/definitions/{definition}`  
  
## Output Schema

Represents a definition for example schema, request, response definitions contained in an API version. A definition is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, definition will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Also, within OpenAPI spec, only `schema` object is supported.

### Definition

JSON representation  
---  
      
    
    {
      "name": string,
      "spec": string,
      "type": enum ([Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition#Output.Schema.Type)),
      "createTime": string,
      "updateTime": string,
      "attributes": {
        string: {
          object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
        },
        ...
      },
    
      // Union field value can be only one of the following:
      "schema": {
        object ([Schema](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition#Output.Schema.Schema))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the definition.Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/definitions/{definition}`  
`spec` |  `string` Output only. The name of the spec from where the definition was parsed. Format is `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}`  
`type` |  `enum (`[Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition#Output.Schema.Type)`)` Output only. The type of the definition.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the definition was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the definition was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`))` Optional. The list of user defined attributes associated with the definition resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `value`.`value` can be only one of the following:  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/get_definition#Output.Schema.Schema)`)` Output only. The value of a schema definition.  
  
### Schema

JSON representation  
---  
      
    
    {
      "displayName": string,
      "rawValue": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The display name of the schema. This will map to the name of the schema in the spec.  
`rawValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The raw value of the schema definition corresponding to the schema name in the spec.A base64-encoded string.  
  
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
  
### AttributesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)`  
  
### AttributeValues

JSON representation  
---  
      
    
    {
      "attribute": string,
    
      // Union field Value can be only one of the following:
      "enumValues": {
        object ([EnumAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.EnumAttributeValues))
      },
      "stringValues": {
        object ([StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues))
      },
      "jsonValues": {
        object ([StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues))
      },
      "uriValues": {
        object ([StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues))
      }
      // End of list of possible types for union field Value.
    }  
  
Fields  
---  
`attribute` |  `string` Output only. The name of the attribute. Format: projects/{project}/locations/{location}/attributes/{attribute}  
Union field `Value`. The attribute values associated with the resource. `Value` can be only one of the following:  
`enumValues` |  `object (`[EnumAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.EnumAttributeValues)`)` The attribute values associated with a resource in case attribute data type is enum.  
`stringValues` |  `object (`[StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues)`)` The attribute values associated with a resource in case attribute data type is string.  
`jsonValues` |  `object (`[StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues)`)` The attribute values associated with a resource in case attribute data type is JSON.  
`uriValues` |  `object (`[StringAttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.StringAttributeValues)`)` The attribute values associated with a resource in case attribute data type is URL, URI or IP, like gs://bucket-name/object-name.  
  
### EnumAttributeValues

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([AllowedValue](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AllowedValue))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[AllowedValue](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AllowedValue)`)` Required. The attribute values in case attribute data type is enum.  
  
### AllowedValue

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "description": string,
      "immutable": boolean
    }  
  
Fields  
---  
`id` |  `string` Required. The ID of the allowed value. * If provided, the same will be used. The service will throw an error if the specified id is already used by another allowed value in the same attribute resource. * If not provided, a system generated id derived from the display name will be used. In this case, the service will handle conflict resolution by adding a system generated suffix in case of duplicates.This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`displayName` |  `string` Required. The display name of the allowed value.  
`description` |  `string` Optional. The detailed description of the allowed value.  
`immutable` |  `boolean` Optional. When set to true, the allowed value cannot be updated or deleted by the user. It can only be true for System defined attributes.  
  
### StringAttributeValues

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Required. The attribute values in case attribute data type is string or JSON.  
  
### Type

Enumeration of definition types.

Enums  
---  
`TYPE_UNSPECIFIED` | Definition type unspecified.  
`SCHEMA` | Definition type schema.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-25 UTC."],[],[]] 
