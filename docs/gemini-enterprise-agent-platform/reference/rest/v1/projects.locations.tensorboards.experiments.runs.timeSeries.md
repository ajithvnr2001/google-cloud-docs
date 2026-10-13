---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries
title: REST Resource: projects.locations.tensorboards.experiments.runs.timeSeries \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:05.628298+00:00
---

# REST Resource: projects.locations.tensorboards.experiments.runs.timeSeries  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.tensorboards.experiments.runs.timeSeries Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: TensorboardTimeSeries

TensorboardTimeSeries maps to times series produced in training runs

Fields  
  
`name` `string` Output only. name of the TensorboardTimeSeries. | `displayName` `string` Required. user provided name of this TensorboardTimeSeries. This value should be unique among all TensorboardTimeSeries resources belonging to the same TensorboardRun resource (parent resource). | `description` `string` description of this TensorboardTimeSeries. | `valueType` `enum (`[ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#ValueType)`)` Required. Immutable. type of TensorboardTimeSeries value. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this TensorboardTimeSeries was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this TensorboardTimeSeries was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `etag` `string` Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. | `pluginName` `string` Immutable. name of the plugin this time series pertain to. Such as Scalar, Tensor, blob | `pluginData` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` data of the current plugin, with the size limited to 65KB.A base64-encoded string. | `metadata` `object (`[Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#Metadata)`)` Output only. Scalar, Tensor, or blob metadata for this TensorboardTimeSeries. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#ValueType)),
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "pluginName": string,
      "pluginData": string,
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#Metadata))
      }
    }  
  
## ValueType

An enum representing the value type of a TensorboardTimeSeries.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | The value type is unspecified.  
`SCALAR` | Used for TensorboardTimeSeries that is a list of scalars. E.g. accuracy of a model over epochs/time.  
`TENSOR` | Used for TensorboardTimeSeries that is a list of tensors. E.g. histograms of weights of layer in a model over epoch/time.  
`BLOB_SEQUENCE` | Used for TensorboardTimeSeries that is a list of blob sequences. E.g. set of sample images with labels over epochs/time.  
  
## Metadata

Describes metadata for a TensorboardTimeSeries.

Fields  
  
`maxStep` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Max step index of all data points within a TensorboardTimeSeries. | `maxWallTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Max wall clock timestamp of all data points within a TensorboardTimeSeries.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `maxBlobSequenceLength` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The largest blob sequence length (number of blobs) of all data points in this time series, if its ValueType is BLOB_SEQUENCE. | JSON representation  
---  
      
    
    {
      "maxStep": string,
      "maxWallTime": string,
      "maxBlobSequenceLength": string
    }  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/create)`

|  Creates a TensorboardTimeSeries.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/delete)`

|  Deletes a TensorboardTimeSeries.  
  
### `[exportTensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/exportTensorboardTimeSeries)`

|  Exports a TensorboardTimeSeries' data.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/get)`

|  Gets a TensorboardTimeSeries.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/list)`

|  Lists TensorboardTimeSeries in a Location.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/patch)`

|  Updates a TensorboardTimeSeries.  
  
### `[read](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/read)`

|  Reads a TensorboardTimeSeries' data.  
  
### `[readBlobData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/readBlobData)`

|  Gets bytes of TensorboardBlobs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
