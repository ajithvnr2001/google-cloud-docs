---
url: https://docs.cloud.google.com/docs/discovery/type-format/
title: Type and format \u00a0|\u00a0 Google APIs Discovery Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:48:51.259785+00:00
---

# Type and format  |  Google APIs Discovery Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/discovery/type-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Google APIs Discovery Service ](https://docs.cloud.google.com/docs/discovery)



#  Type and format Stay organized with collections  Save and categorize content based on your preferences. 

The `type` and `format` properties on parameters and schemas can be used to determine the data type of the property. The `type` property indicates the type of the property when its sent in JSON requests and responses (JSON supports a small set of data types, see [json.org](https://json.org) for details). The `format` property provides additional information about the underlying type. Properties will always have a `type` property, but some may also have a `format` property. 

For example, a 64-bit integer cannot be represented in JSON (since JavaScript and JSON support integers up to 2^53). Therefore, a 64-bit integer must be represented as a string in JSON requests/responses. So the `type` property will be set to "string", but the `format` property will be set to "int64" to indicate that it is a 64-bit integer. 

The JSON Schema spec already [defines a set of common values](https://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.23) for the `format` property. The Google APIs Discovery Service supports some of these values, and defines others as well. The full list of `type` and `format` values supported by Google APIs Discovery Service is summarized below. 

**Note:** The [client libraries](https://developers.google.com/api-client-library/) that we automatically generate from an API's discovery document sometimes use language-idiomatic types for these types and formats. For example: A 64-bit integer is represented as type `string` in JSON requests and responses, but our generated Java client library uses the Java `long` type. Type value | Format value | Meaning  
---|---|---  
`any` | `` |  The property may have any type. Defined by the [JSON Schema spec](https://tools.ietf.org/html/draft-zyp-json-schema-03).   
`any` | `google.protobuf.Value` |  The property has the JSON representation of the type of [google.protobuf.Value](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/struct.proto).   
`array` | `` |  A JavaScript array of values. The `items` property indicates the schema for the array values. Defined by the JSON Schema spec.   
`array` | `google.protobuf.ListValue` |  The property has the JSON representation of the type of [google.protobuf.ListValue](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/struct.proto).   
`boolean` | `` | A boolean value, either "true" or "false". Defined by the JSON Schema spec.  
`integer` | `int32` |  A 32-bit signed integer. It has a minimum value of -2,147,483,648 and a maximum value of 2,147,483,647 (inclusive).   
`integer` | `uint32` |  A 32-bit unsigned integer. It has a minimum value of 0 and a maximum value of 4,294,967,295 (inclusive).   
`number` | `double` | A double-precision 64-bit IEEE 754 floating point.  
`number` | `float` | A single-precision 32-bit IEEE 754 floating point.  
`object` | `` | A JavaScript object. Defined by the JSON Schema spec.  
`object` | `google.protobuf.Struct` |  The property has the JSON representation of the type of [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/struct.proto).   
`object` | `google.protobuf.Any` |  The property has the JSON representation of the type of [google.protobuf.Any](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/any.proto).   
`string` | `` | An arbitrary string. Defined by the JSON Schema spec.  
`string` | `byte` |  A padded, base64-encoded string of bytes, encoded with a URL and filename safe alphabet (sometimes referred to as "web-safe" or "base64url"). Defined by [RFC4648](https://tools.ietf.org/html/rfc4648).   
`string` | `date` | An RFC3339 date in the format YYYY-MM-DD. Defined in the JSON Schema spec.  
`string` | `date-time` |  An RFC3339 timestamp in UTC time. This in the format of yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS") is optional. Defined in the JSON Schema spec.   
`string` | `google-datetime` |  An RFC3339 timestamp in UTC time. This in the format of yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS") is optional.   
`string` | `google-duration` |  A string ends in the suffix "s" (indicating seconds) and is preceded by the number of seconds, with nanoseconds expressed as fractional seconds. The period is always used as the decimal point, not a comma.   
`string` | `google-fieldmask` |  A string where field names are separated by a comma. Field names are represented in lower-camel naming conventions.   
`string` | `int64` |  A 64-bit signed integer. It has a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807 (inclusive).   
`string` | `uint64` |  A 64-bit unsigned integer. It has a minimum value of 0 and a maximum value of (2^64)-1 (inclusive).   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
