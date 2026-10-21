---
url: https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request/
title: MCP Tools Reference: cloudquotas.googleapis.com \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:26:29.644488+00:00
---

# MCP Tools Reference: cloudquotas.googleapis.com  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  MCP Tools Reference: cloudquotas.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_quota_increase_request`

Creates a new QuotaPreference that declares the desired value for a quota (initiating a Quota Increase Request). Expected request structure: 'quota_preference.name' (string, format: projects/{project}/locations/global/quotaPreferences/{id}), 'quota_preference.service' (string, e.g. compute.googleapis.com), 'quota_preference.quota_id' (string, e.g. CpusPerProjectPerRegion), 'quota_preference.quota_config.preferred_value' (int64), 'quota_preference.contact_email' (string), and 'quota_preference.justification' (string).

The following sample demonstrate how to use `curl` to invoke the `create_quota_increase_request` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://cloudquotas.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_quota_increase_request",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Message for updating a QuotaPreference

### UpdateQuotaPreferenceRequest

JSON representation  
---  
      
    
    {
      "updateMask": string,
      "quotaPreference": {
        object ([QuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaPreference))
      },
      "allowMissing": boolean,
      "validateOnly": boolean,
      "ignoreSafetyChecks": [
        enum ([QuotaSafetyCheck](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaSafetyCheck))
      ]
    }  
  
Fields  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`quotaPreference` |  `object (`[QuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaPreference)`)` Required. The resource being updated  
`allowMissing` |  `boolean` Optional. If set to true, and the quota preference is not found, a new one will be created. In this situation, `update_mask` is ignored.  
`validateOnly` |  `boolean` Optional. If set to true, validate the request, but do not actually update. Note that a request being valid does not mean that the request is guaranteed to be fulfilled.  
`ignoreSafetyChecks[]` |  `enum (`[QuotaSafetyCheck](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaSafetyCheck)`)` The list of quota safety checks to be ignored.  
  
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
  
### QuotaPreference

JSON representation  
---  
      
    
    {
      "name": string,
      "dimensions": {
        string: string,
        ...
      },
      "quotaConfig": {
        object ([QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaConfig))
      },
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "service": string,
      "quotaId": string,
      "reconciling": boolean,
      "justification": string,
      "contactEmail": string
    }  
  
Fields  
---  
`name` |  `string` Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`  
`dimensions` |  `map (key: string, value: string)` Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`quotaConfig` |  `object (`[QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaConfig)`)` Required. Preferred quota configuration.  
`etag` |  `string` Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`service` |  `string` Required. The name of the service to which the quota preference is applied.  
`quotaId` |  `string` Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`  
`reconciling` |  `boolean` Output only. Is the quota preference pending Google Cloud approval and fulfillment.  
`justification` |  `string` The reason / justification for this quota preference.  
`contactEmail` |  `string` Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.  
  
### DimensionsEntry

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
  
### QuotaConfig

JSON representation  
---  
      
    
    {
      "preferredValue": string,
      "stateDetail": string,
      "grantedValue": string,
      "traceId": string,
      "annotations": {
        string: string,
        ...
      },
      "requestOrigin": enum ([Origin](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.Origin))
    }  
  
Fields  
---  
`preferredValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The preferred value. Must be greater than or equal to -1. If set to -1, it means the value is "unlimited".  
`stateDetail` |  `string` Output only. Optional details about the state of this quota preference.  
`grantedValue` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Output only. Granted quota value.  
`traceId` |  `string` Output only. The trace id that the Google Cloud uses to provision the requested quota. This trace id may be used by the client to contact Cloud support to track the state of a quota preference request. The trace id is only produced for increase requests and is unique for each request. The quota decrease requests do not have a trace id.  
`annotations` |  `map (key: string, value: string)` Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`requestOrigin` |  `enum (`[Origin](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.Origin)`)` Output only. The origin of the quota preference request.  
  
### Int64Value

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The int64 value.  
  
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
  
### Origin

The enumeration of the origins of quota preference requests.

Enums  
---  
`ORIGIN_UNSPECIFIED` | The unspecified value.  
`CLOUD_CONSOLE` | Created through Cloud Console.  
`AUTO_ADJUSTER` | Generated by automatic quota adjustment.  
  
### QuotaSafetyCheck

Enumerations of quota safety checks.

Enums  
---  
`QUOTA_SAFETY_CHECK_UNSPECIFIED` | Unspecified quota safety check.  
`QUOTA_DECREASE_BELOW_USAGE` | Validates that a quota mutation would not cause the consumer's effective limit to be lower than the consumer's quota usage.  
`QUOTA_DECREASE_PERCENTAGE_TOO_HIGH` | Validates that a quota mutation would not cause the consumer's effective limit to decrease by more than 10 percent.  
  
## Output Schema

QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.

### QuotaPreference

JSON representation  
---  
      
    
    {
      "name": string,
      "dimensions": {
        string: string,
        ...
      },
      "quotaConfig": {
        object ([QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaConfig))
      },
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "service": string,
      "quotaId": string,
      "reconciling": boolean,
      "justification": string,
      "contactEmail": string
    }  
  
Fields  
---  
`name` |  `string` Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`  
`dimensions` |  `map (key: string, value: string)` Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`quotaConfig` |  `object (`[QuotaConfig](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.QuotaConfig)`)` Required. Preferred quota configuration.  
`etag` |  `string` Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`service` |  `string` Required. The name of the service to which the quota preference is applied.  
`quotaId` |  `string` Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`  
`reconciling` |  `boolean` Output only. Is the quota preference pending Google Cloud approval and fulfillment.  
`justification` |  `string` The reason / justification for this quota preference.  
`contactEmail` |  `string` Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.  
  
### DimensionsEntry

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
  
### QuotaConfig

JSON representation  
---  
      
    
    {
      "preferredValue": string,
      "stateDetail": string,
      "grantedValue": string,
      "traceId": string,
      "annotations": {
        string: string,
        ...
      },
      "requestOrigin": enum ([Origin](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.Origin))
    }  
  
Fields  
---  
`preferredValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The preferred value. Must be greater than or equal to -1. If set to -1, it means the value is "unlimited".  
`stateDetail` |  `string` Output only. Optional details about the state of this quota preference.  
`grantedValue` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Output only. Granted quota value.  
`traceId` |  `string` Output only. The trace id that the Google Cloud uses to provision the requested quota. This trace id may be used by the client to contact Cloud support to track the state of a quota preference request. The trace id is only produced for increase requests and is unique for each request. The quota decrease requests do not have a trace id.  
`annotations` |  `map (key: string, value: string)` Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`requestOrigin` |  `enum (`[Origin](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request#Input.Schema.Origin)`)` Output only. The origin of the quota preference request.  
  
### Int64Value

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The int64 value.  
  
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
  
### Origin

The enumeration of the origins of quota preference requests.

Enums  
---  
`ORIGIN_UNSPECIFIED` | The unspecified value.  
`CLOUD_CONSOLE` | Created through Cloud Console.  
`AUTO_ADJUSTER` | Generated by automatic quota adjustment.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
