---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags
title: REST Resource: projects.locations.flags \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:03.550248+00:00
---

# REST Resource: projects.locations.flags  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.flags Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Flag
    * JSON representation
    * FlagValueType
    * ValueType
    * FlagVariant
      * JSON representation
    * State
  * Methods



## Resource: Flag

Represents a single Flag.

JSON representation  
---  
      
    
    {
      "name": string,
      "key": string,
      "valueType": enum ([FlagValueType](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.FlagValueType)),
      "flagValueType": enum ([ValueType](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.ValueType)),
      "evaluationSpec": {
        object ([EvaluationSpec](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec))
      },
      "unitKind": string,
      "description": string,
      "variants": [
        {
          object ([FlagVariant](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.FlagVariant))
        }
      ],
      "flagSet": string,
      "state": enum ([State](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.State)),
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      },
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/flags/{flagId}"  
`key` |  `string` Required. Immutable. Flag key used in runtime evaluation APIs (OpenFeature). Max length: 256 bytes.  
`valueType  
**(deprecated)**` |  `enum (`[FlagValueType](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.FlagValueType)`)` This item is deprecated!Optional. Immutable. Deprecated: Use `flagValueType` instead. Flag value type.  
`flagValueType` |  `enum (`[ValueType](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.ValueType)`)` Optional. Immutable. Flag value type.  
`evaluationSpec` |  `object (`[EvaluationSpec](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec)`)` Optional. Specification of how the flag value should be evaluated.If a bool flag is created without an evaluationSpec specified, two default variants, "Enabled" (with boolValue = true) and "Disabled" (with boolValue = false), are created by default, and "Disabled" is set as the defaultTarget.  
`unitKind` |  `string` Required. Immutable. `[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#UnitKind)` that can consume this flag.  
`description` |  `string` Optional. Description of the flag. Max length: 500 bytes.  
`variants[]` |  `object (`[FlagVariant](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.FlagVariant)`)` Optional. A list of variants.  
`flagSet` |  `string` Optional. Flag set this flag belongs to.  
`state` |  `enum (`[State](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag.State)`)` Optional. Current state of the flag.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### FlagValueType

Enums  
---  
`FLAG_VALUE_TYPE_UNSPECIFIED` |   
`FLAG_VALUE_TYPE_BOOL` | Boolean flag value type.  
`FLAG_VALUE_TYPE_INT` | Integer flag value type.  
`FLAG_VALUE_TYPE_STRING` | String flag value type.  
`FLAG_VALUE_TYPE_DOUBLE` | Double flag type.  
  
### ValueType

Flag value type.

Enums  
---  
`FLAG_VALUE_TYPE_UNSPECIFIED` | Unspecified flag value type.  
`FLAG_VALUE_TYPE_BOOLEAN` | Boolean flag value type.  
`FLAG_VALUE_TYPE_INTEGER` | Integer flag value type.  
`FLAG_VALUE_TYPE_STRING` | String flag value type.  
`FLAG_VALUE_TYPE_DOUBLE` | Double flag value type.  
  
### FlagVariant

Variant is an identifier for a value (name assigned to a value).

JSON representation  
---  
      
    
    {
      "id": string,
      "trackingId": string,
      "description": string,
    
      // Union field value can be only one of the following:
      "booleanValue": boolean,
      "integerValue": string,
      "stringValue": string,
      "doubleValue": number
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`id` |  `string` Required. Variant ID. Max length: 128 bytes.  
`trackingId` |  `string` Optional. trackingId is unique depending on name and value of the variant within the scope of the service. It is typically generated by the server and must not be changed. trackingId is used to uniquely identify and track variants.  
`description` |  `string` Optional. A human-readable description of what this variant does or represents.  
Union field `value`. value is a single flag value for the variant. `value` can be only one of the following:  
`booleanValue` |  `boolean` Optional. Boolean variant value.  
`integerValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Integer variant value.  
`stringValue` |  `string` Optional. String variant value.  
`doubleValue` |  `number` Optional. Double variant value.  
  
### State

State defines the state of the flag.

Enums  
---  
`FLAG_STATE_UNSPECIFIED` | Flag state is unspecified.  
`FLAG_STATE_IN_DEVELOPMENT` | Flag is in development state.  
`FLAG_STATE_ACTIVE` | Flag is in active state.  
`FLAG_STATE_SUNSETTING` | Flag is in deprecated state.  
`FLAG_STATE_CLEANUP` | Flag is in cleanup state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/create)`

|  Create a new flag.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/delete)`

|  Delete a single flag.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/get)`

|  Retrieve a single flag.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/list)`

|  Retrieve a collection of flags.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/patch)`

|  Update a single flag.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
