---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/predict/
title: MCP Tools Reference: aiplatform.googleapis.com \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:07:33.563649+00:00
---

# MCP Tools Reference: aiplatform.googleapis.com  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  MCP Tools Reference: aiplatform.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `predict`

Perform online predictions for a wide range of machine learning models. Use this to get real-time inference results from your deployed models on Agent Platform.

The following sample demonstrate how to use `curl` to invoke the `predict` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://aiplatform.googleapis.com/mcp/generate' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "predict",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for `PredictionService.Predict`.

### PredictRequest

JSON representation  
---  
      
    
    {
      "endpoint": string,
      "instances": [
        value
      ],
      "parameters": value,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`endpoint` |  `string` Required. The resource name of the publisher model or endpoint requested to serve the prediction. For Google models like Embedding or Veo, use the publisher model format. For tuned models or other models deployed to an Agent Platform endpoint, use the endpoint format.

  * Publisher model format: `projects/{project}/locations/{location}/publishers/google/models/{model}`
  * Endpoint format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

  
`instances[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behavior is as documented by that Model. The schema of each instance depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `TextEmbeddingPredictionInstance`
  * For a generative AI request to a Multimodal Embedding model, see `VisionEmbeddingModelInstance`
  * For a video generation request to a Veo model, see `VideoGenerationModelInstance`
  * For a traditional machine learning request to a deployed custom model, the schema of any single instance is defined by the model's `instanceSchemaUri`.

  
`parameters` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The parameters that govern the prediction. The schema of the parameters depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `TextEmbeddingPredictionParams`
  * For a generative AI request to a Multimodal Embedding model, see `VisionEmbeddingModelParams`
  * For a video generation request to a Veo model, see `VideoGenerationModelParams`
  * For a traditional machine learning request to a deployed custom model, the schema of the parameters is defined by the model's `parametersSchemaUri`.

  
`labels` |  `map (key: string, value: string)` Optional. The user labels for Imagen billing usage only. Only Imagen supports labels. For other use cases, it will be ignored.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
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
  
### LabelsEntry

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
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
## Output Schema

Response message for `PredictionService.Predict`.

### PredictResponse

JSON representation  
---  
      
    
    {
      "predictions": [
        value
      ],
      "deployedModelId": string,
      "model": string,
      "modelVersionId": string,
      "modelDisplayName": string,
      "metadata": value
    }  
  
Fields  
---  
`predictions[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The predictions that are the output of the predictions call. The schema of each prediction depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `TextEmbeddingPredictionResult`
  * For a generative AI request to a Multimodal Embedding model, see `VisionEmbeddingModelResult`
  * For a video generation request to a Veo model, see `VideoGenerationModelResult`
  * For a traditional machine learning request to a deployed custom model, the schema of each prediction is defined by the model's `predictionSchemaUri`.

  
`deployedModelId` |  `string` ID of the Endpoint's DeployedModel that served this prediction.  
`model` |  `string` Output only. The resource name of the Model which is deployed as the DeployedModel that this prediction hits.  
`modelVersionId` |  `string` Output only. The version ID of the Model which is deployed as the DeployedModel that this prediction hits.  
`modelDisplayName` |  `string` Output only. The `display name` of the Model which is deployed as the DeployedModel that this prediction hits.  
`metadata` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. Request-level metadata returned by the model. The metadata type will be dependent upon the model implementation.  
  
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
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
