---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/list_apis/
title: MCP Tools Reference: apihub.googleapis.com \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:38.107191+00:00
---

# MCP Tools Reference: apihub.googleapis.com  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/list_apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  MCP Tools Reference: apihub.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_apis`

List API resources in the API hub.

The following sample demonstrate how to use `curl` to invoke the `list_apis` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://apihub.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_apis",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The `ListApis` method's request.

### ListApisRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of API resources. Format: `projects/{project}/locations/{location}`  
`filter` |  `string` Optional. An expression that filters the list of ApiResources.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>`, `:` or `=`. Filters are not case sensitive.The following fields in the `ApiResource` are eligible for filtering:

  * `owner.email` \- The email of the team which owns the ApiResource. Allowed comparison operators: `=`.
  * `create_time` \- The time at which the ApiResource was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and `<`.
  * `display_name` \- The display name of the ApiResource. Allowed comparison operators: `=`.
  * `target_user.enum_values.values.id` \- The allowed value id of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `target_user.enum_values.values.display_name` \- The allowed value display name of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `team.enum_values.values.id` \- The allowed value id of the team attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `team.enum_values.values.display_name` \- The allowed value display name of the team attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `business_unit.enum_values.values.id` \- The allowed value id of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `business_unit.enum_values.values.display_name` \- The allowed value display name of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `maturity_level.enum_values.values.id` \- The allowed value id of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `maturity_level.enum_values.values.display_name` \- The allowed value display name of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `api_style.enum_values.values.id` \- The allowed value id of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `api_style.enum_values.values.display_name` \- The allowed value display name of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`.
  * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` \- The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name.
  * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name`
  * The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name.
  * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` \- The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name.
  * `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` \- The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name.

A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"api-1\"` is equivalent to `name = \"projects/test-project-id/locations/test-location-id/apis/api-1\"` provided the parent is `projects/test-project-id/locations/test-location-id`.Another supported filter function is `plugins(source_metadata)`. This function filters for resources that are associated with a specific plugin. For example, `plugins(source_metadata) : "projects/test-project-id/locations/test-location-id/plugins/test-plugin-id"` will return resources sourced from the given plugin.Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API.Here are a few examples:

  * `owner.email = \"apihub@google.com\"` \- - The owner team email is [_apihub@google.com_](mailto:_apihub@google.com_).
  * `owner.email = \"apihub@google.com\" AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"` \- The owner team email is [_apihub@google.com_](mailto:_apihub@google.com_) and the api was created before _2021-08-15 14:50:00 UTC_ and after _2021-08-10 12:00:00 UTC_.
  * `owner.email = \"apihub@google.com\" OR team.enum_values.values.id: apihub-team-id` \- The filter string specifies the APIs where the owner team email is [_apihub@google.com_](mailto:_apihub@google.com_) or the id of the allowed value associated with the team attribute is _apihub-team-id_.
  * `owner.email = \"apihub@google.com\" OR team.enum_values.values.display_name: ApiHub Team` \- The filter string specifies the APIs where the owner team email is [_apihub@google.com_](mailto:_apihub@google.com_) or the display name of the allowed value associated with the team attribute is `ApiHub Team`.
  * `owner.email = \"apihub@google.com\" AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test_enum_id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/1765\0f90-4a29-5431-b3d0-d5532da3764c.string_values.values: test_string_value` \- The filter string specifies the APIs where the owner team email is [_apihub@google.com_](mailto:_apihub@google.com_) and the id of the allowed value associated with the user defined attribute of type enum is _test_enum_id_ and the value of the user defined attribute of type string is _test_..

  
`pageSize` |  `integer` Optional. The maximum number of API resources to return. The service may return fewer than this value. If unspecified, at most 50 Apis will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page.When paginating, all other parameters (except page_size) provided to `ListApis` must match the call that provided the page token.  
  
## Output Schema

The `ListApis` method's response.

### ListApisResponse

JSON representation  
---  
      
    
    {
      "apis": [
        {
          object ([Api](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Api))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`apis[]` |  `object (`[Api](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Api)`)` The API resources present in the API hub.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Api

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "documentation": {
        object ([Documentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Documentation))
      },
      "owner": {
        object ([Owner](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Owner))
      },
      "versions": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "targetUser": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "team": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "businessUnit": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "maturityLevel": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "attributes": {
        string: {
          object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
        },
        ...
      },
      "apiStyle": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "selectedVersion": string,
      "apiRequirements": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "fingerprint": string,
      "sourceMetadata": [
        {
          object ([SourceMetadata](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.SourceMetadata))
        }
      ],
      "apiFunctionalRequirements": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      },
      "apiTechnicalRequirements": {
        object ([AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the API resource in the API Hub.Format: `projects/{project}/locations/{location}/apis/{api}`  
`displayName` |  `string` Required. The display name of the API resource.  
`description` |  `string` Optional. The description of the API resource.  
`documentation` |  `object (`[Documentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Documentation)`)` Optional. The documentation for the API resource.  
`owner` |  `object (`[Owner](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.Owner)`)` Optional. Owner details for the API resource.  
`versions[]` |  `string` Output only. The list of versions present in an API resource. Note: An API resource can be associated with more than 1 version. Format is `projects/{project}/locations/{location}/apis/{api}/versions/{version}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the API resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the API resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targetUser` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The target users for the API. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-target-user` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.  
`team` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The team owning the API. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-team` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.  
`businessUnit` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The business unit owning the API. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-business-unit` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.  
`maturityLevel` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The maturity level of the API. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-maturity-level` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.  
`attributes` |  `map (key: string, value: object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`))` Optional. The list of user defined attributes associated with the API resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`apiStyle` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The style of the API. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-api-style` attribute. The number of values for this attribute will be based on the cardinality of the attribute. The same can be retrieved via GetAttribute API. All values should be from the list of allowed values defined for the attribute.  
`selectedVersion` |  `string` Optional. The selected version for an API resource. This can be used when special handling is needed on client side for particular version of the API. Format is `projects/{project}/locations/{location}/apis/{api}/versions/{version}`  
`apiRequirements` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The api requirement doc associated with the API resource. Carinality is 1 for this attribute. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-api-requirements` attribute. The value of the attribute should be a proper URI, and in case of Cloud Storage URI, it should point to a Cloud Storage object, not a directory.  
`fingerprint` |  `string` Optional. Fingerprint of the API resource. This must be unique for each API resource. It can neither be unset nor be updated to an existing fingerprint of another API resource.  
`sourceMetadata[]` |  `object (`[SourceMetadata](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.SourceMetadata)`)` Output only. The list of sources and metadata from the sources of the API resource.  
`apiFunctionalRequirements` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The api functional requirements associated with the API resource. Carinality is 1 for this attribute. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-api-functional-requirements` attribute. The value of the attribute should be a proper URI, and in case of Cloud Storage URI, it should point to a Cloud Storage object, not a directory.  
`apiTechnicalRequirements` |  `object (`[AttributeValues](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.AttributeValues)`)` Optional. The api technical requirements associated with the API resource. Carinality is 1 for this attribute. This maps to the following system defined attribute: `projects/{project}/locations/{location}/attributes/system-api-technical-requirements` attribute. The value of the attribute should be a proper URI, and in case of Cloud Storage URI, it should point to a Cloud Storage object, not a directory.  
  
### Documentation

JSON representation  
---  
      
    
    {
      "externalUri": string
    }  
  
Fields  
---  
`externalUri` |  `string` Optional. The uri of the externally hosted documentation.  
  
### Owner

JSON representation  
---  
      
    
    {
      "displayName": string,
      "email": string
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The name of the owner.  
`email` |  `string` Required. The email of the owner.  
  
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
  
### SourceMetadata

JSON representation  
---  
      
    
    {
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.SourceType)),
      "originalResourceId": string,
      "originalResourceCreateTime": string,
      "originalResourceUpdateTime": string,
    
      // Union field source can be only one of the following:
      "pluginInstanceActionSource": {
        object ([PluginInstanceActionSource](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.PluginInstanceActionSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.SourceType)`)` Output only. The type of the source.  
`originalResourceId` |  `string` Output only. The unique identifier of the resource at the source.  
`originalResourceCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the resource was created at the source.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`originalResourceUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the resource was last updated at the source.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `source`. The source of the resource. `source` can be only one of the following:  
`pluginInstanceActionSource` |  `object (`[PluginInstanceActionSource](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp/tools_list/create_api#Input.Schema.PluginInstanceActionSource)`)` Output only. The source of the resource is a plugin instance action.  
  
### PluginInstanceActionSource

JSON representation  
---  
      
    
    {
      "pluginInstance": string,
      "actionId": string
    }  
  
Fields  
---  
`pluginInstance` |  `string` Output only. The resource name of the source plugin instance. Format is `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionId` |  `string` Output only. The id of the plugin instance action.  
  
### SourceType

The possible types of the source.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Source type not specified.  
`PLUGIN` | Source type plugin.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-25 UTC."],[],[]] 
