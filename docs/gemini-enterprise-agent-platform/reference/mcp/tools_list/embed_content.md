---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content/
title: MCP Tools Reference: aiplatform.googleapis.com \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:37:21.736001+00:00
---

# MCP Tools Reference: aiplatform.googleapis.com  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  MCP Tools Reference: aiplatform.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `embed_content`

Converts text or multimodal input into a high-dimensional vector representation (embedding), which is essential for tasks like semantic search, clustering, and Retrieval-Augmented Generation (RAG).

The following sample demonstrate how to use `curl` to invoke the `embed_content` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://aiplatform.googleapis.com/mcp/generate' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "embed_content",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for `PredictionService.EmbedContent`.

### EmbedContentRequest

JSON representation  
---  
      
    
    {
    
      // Union field _model can be only one of the following:
      "model": string
      // End of list of possible types for union field _model.
    
      // Union field _content can be only one of the following:
      "content": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Content))
      }
      // End of list of possible types for union field _content.
    
      // Union field _title can be only one of the following:
      "title": string
      // End of list of possible types for union field _title.
    
      // Union field _task_type can be only one of the following:
      "taskType": enum ([EmbeddingTaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbeddingTaskType))
      // End of list of possible types for union field _task_type.
    
      // Union field _output_dimensionality can be only one of the following:
      "outputDimensionality": integer
      // End of list of possible types for union field _output_dimensionality.
    
      // Union field _auto_truncate can be only one of the following:
      "autoTruncate": boolean
      // End of list of possible types for union field _auto_truncate.
    
      // Union field _embed_content_config can be only one of the following:
      "embedContentConfig": {
        object ([EmbedContentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbedContentConfig))
      }
      // End of list of possible types for union field _embed_content_config.
    }  
  
Fields  
---  
Union field `_model`.`_model` can be only one of the following:  
`model` |  `string` Required. The name of the publisher model requested to serve the prediction. Format: `projects/{project}/locations/{location}/publishers/*/models/*`  
Union field `_content`.`_content` can be only one of the following:  
`content` |  `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Content)`)` Required. The content to be embedded.  
Union field `_title`.`_title` can be only one of the following:  
`title  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Please use EmbedContentConfig.title instead. The title for the text.  
Union field `_task_type`.`_task_type` can be only one of the following:  
`taskType  
**(deprecated)**` |  `enum (`[EmbeddingTaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbeddingTaskType)`)` This item is deprecated!Optional. Deprecated: Please use EmbedContentConfig.task_type instead. The task type of the embedding.  
Union field `_output_dimensionality`.`_output_dimensionality` can be only one of the following:  
`outputDimensionality  
**(deprecated)**` |  `integer` This item is deprecated!Optional. Deprecated: Please use EmbedContentConfig.output_dimensionality instead. Reduced dimension for the output embedding. If set, excessive values in the output embedding are truncated from the end.  
Union field `_auto_truncate`.`_auto_truncate` can be only one of the following:  
`autoTruncate  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: Please use EmbedContentConfig.auto_truncate instead. Whether to silently truncate the input content if it's longer than the maximum sequence length.  
Union field `_embed_content_config`.`_embed_content_config` can be only one of the following:  
`embedContentConfig` |  `object (`[EmbedContentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbedContentConfig)`)` Optional. Configuration for the EmbedContent request.  
  
### Content

JSON representation  
---  
      
    
    {
      "role": string,
      "parts": [
        {
          object ([Part](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Part))
        }
      ]
    }  
  
Fields  
---  
`role` |  `string` Optional. The producer of the content. Must be either 'user' or 'model'.If not set, the service will default to 'user'.  
`parts[]` |  `object (`[Part](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Part)`)` Required. A list of `Part` objects that make up a single message. Parts of a message can have different MIME types.A `Content` message must have at least one `Part`.  
  
### Part

JSON representation  
---  
      
    
    {
      "thought": boolean,
      "thoughtSignature": string,
      "mediaResolution": {
        object ([MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.MediaResolution))
      },
      "audioTranscription": {
        object ([AudioTranscription](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.AudioTranscription))
      },
    
      // Union field data can be only one of the following:
      "text": string,
      "inlineData": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Blob))
      },
      "fileData": {
        object ([FileData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FileData))
      },
      "functionCall": {
        object ([FunctionCall](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionCall))
      },
      "functionResponse": {
        object ([FunctionResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponse))
      },
      "executableCode": {
        object ([ExecutableCode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.ExecutableCode))
      },
      "codeExecutionResult": {
        object ([CodeExecutionResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.CodeExecutionResult))
      }
      // End of list of possible types for union field data.
    
      // Union field metadata can be only one of the following:
      "videoMetadata": {
        object ([VideoMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.VideoMetadata))
      }
      // End of list of possible types for union field metadata.
    }  
  
Fields  
---  
`thought` |  `boolean` Optional. Indicates whether the `part` represents the model's thought process or reasoning.  
`thoughtSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. An opaque signature for the thought so it can be reused in subsequent requests.A base64-encoded string.  
`mediaResolution` |  `object (`[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.MediaResolution)`)` per part media resolution. Media resolution for the input media.  
`audioTranscription` |  `object (`[AudioTranscription](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.AudioTranscription)`)` Optional. Audio (input or output) transcription. This is only set when this Part contains audio data.  
Union field `data`.`data` can be only one of the following:  
`text` |  `string` Optional. The text content of the part. When sent from the VSCode Gemini Code Assist extension, references to @mentioned items will be converted to markdown boldface text. For example `@my-repo` will be converted to and sent as `**my-repo**` by the IDE agent.  
`inlineData` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Blob)`)` Optional. The inline data content of the part. This can be used to include images, audio, or video in a request.  
`fileData` |  `object (`[FileData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FileData)`)` Optional. The URI-based data of the part. This can be used to include files from Google Cloud Storage.  
`functionCall` |  `object (`[FunctionCall](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionCall)`)` Optional. A predicted function call returned from the model. This contains the name of the function to call and the arguments to pass to the function.  
`functionResponse` |  `object (`[FunctionResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponse)`)` Optional. The result of a function call. This is used to provide the model with the result of a function call that it predicted.  
`executableCode` |  `object (`[ExecutableCode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.ExecutableCode)`)` Optional. Code generated by the model that is intended to be executed.  
`codeExecutionResult` |  `object (`[CodeExecutionResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.CodeExecutionResult)`)` Optional. The result of executing the `ExecutableCode`.  
Union field `metadata`.`metadata` can be only one of the following:  
`videoMetadata` |  `object (`[VideoMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.VideoMetadata)`)` Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.  
  
### Blob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "displayName": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The raw bytes of the data.A base64-encoded string.  
`displayName` |  `string` Optional. The display name of the blob. Used to provide a label or filename to distinguish blobs.This field is only returned in `PromptMessage` for prompt management. It is used in the Gemini calls only when server-side tools (`code_execution`, `google_search`, and `url_context`) are enabled.  
  
### FileData

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "fileUri": string,
      "displayName": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`fileUri` |  `string` Required. The URI of the file in Google Cloud Storage.  
`displayName` |  `string` Optional. The display name of the file. Used to provide a label or filename to distinguish files.This field is only returned in `PromptMessage` for prompt management. It is used in the Gemini calls only when server side tools (`code_execution`, `google_search`, and `url_context`) are enabled.  
  
### FunctionCall

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "args": {
        object
      },
      "partialArgs": [
        {
          object ([PartialArg](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.PartialArg))
        }
      ],
      "willContinue": boolean
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique id of the function call. If populated, the client to execute the `function_call` and return the response with the matching `id`.  
`name` |  `string` Optional. The name of the function to call. Matches `FunctionDeclaration.name`.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The function parameters and values in JSON object format. See `FunctionDeclaration.parameters` for parameter details.  
`partialArgs[]` |  `object (`[PartialArg](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.PartialArg)`)` Optional. The partial argument value of the function call. If provided, represents the arguments/fields that are streamed incrementally.  
`willContinue` |  `boolean` Optional. Whether this is the last part of the FunctionCall. If true, another partial message for the current FunctionCall is expected to follow.  
  
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
  
### PartialArg

JSON representation  
---  
      
    
    {
      "jsonPath": string,
      "willContinue": boolean,
    
      // Union field delta can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean
      // End of list of possible types for union field delta.
    }  
  
Fields  
---  
`jsonPath` |  `string` Required. A JSON Path (RFC 9535) to the argument being streamed. <https://datatracker.ietf.org/doc/html/rfc9535>. e.g. "$.foo.bar[0].data".  
`willContinue` |  `boolean` Optional. Whether this is not the last part of the same json_path. If true, another PartialArg message for the current json_path is expected to follow.  
Union field `delta`. The delta of field value being streamed. `delta` can be only one of the following:  
`nullValue` |  `null` Optional. Represents a null value.  
`numberValue` |  `number` Optional. Represents a double value.  
`stringValue` |  `string` Optional. Represents a string value.  
`boolValue` |  `boolean` Optional. Represents a boolean value.  
  
### FunctionResponse

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "response": {
        object
      },
      "parts": [
        {
          object ([FunctionResponsePart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponsePart))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Optional. The id of the function call this response is for. Populated by the client to match the corresponding function call `id`.  
`name` |  `string` Required. The name of the function to call. Matches `FunctionDeclaration.name` and `FunctionCall.name`.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The function response in JSON object format. Use "output" key to specify function output and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as function output.  
`parts[]` |  `object (`[FunctionResponsePart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponsePart)`)` Optional. Ordered `Parts` that constitute a function response. Parts may have different IANA MIME types.  
  
### FunctionResponsePart

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "inlineData": {
        object ([FunctionResponseBlob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponseBlob))
      },
      "fileData": {
        object ([FunctionResponseFileData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponseFileData))
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. The data of the function response part. `data` can be only one of the following:  
`inlineData` |  `object (`[FunctionResponseBlob](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponseBlob)`)` Inline media bytes.  
`fileData` |  `object (`[FunctionResponseFileData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.FunctionResponseFileData)`)` URI based data.  
  
### FunctionResponseBlob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "displayName": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes.A base64-encoded string.  
`displayName` |  `string` Optional. Display name of the blob.Used to provide a label or filename to distinguish blobs.This field is only returned in PromptMessage for prompt management. It is currently used in the Gemini GenerateContent calls only when server side tools (code_execution, google_search, and url_context) are enabled.  
  
### FunctionResponseFileData

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "fileUri": string,
      "displayName": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`fileUri` |  `string` Required. URI.  
`displayName` |  `string` Optional. Display name of the file data.Used to provide a label or filename to distinguish file datas.This field is only returned in PromptMessage for prompt management. It is currently used in the Gemini GenerateContent calls only when server side tools (code_execution, google_search, and url_context) are enabled.  
  
### ExecutableCode

JSON representation  
---  
      
    
    {
      "language": enum ([Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Language)),
      "code": string,
    
      // Union field _id can be only one of the following:
      "id": string
      // End of list of possible types for union field _id.
    }  
  
Fields  
---  
`language` |  `enum (`[Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Language)`)` Required. Programming language of the `code`.  
`code` |  `string` Required. The code to be executed.  
Union field `_id`.`_id` can be only one of the following:  
`id` |  `string` Optional. Unique identifier of the `ExecutableCode` part. The server returns the `CodeExecutionResult` with the matching `id`.  
  
### CodeExecutionResult

JSON representation  
---  
      
    
    {
      "outcome": enum ([Outcome](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Outcome)),
      "output": string,
    
      // Union field _id can be only one of the following:
      "id": string
      // End of list of possible types for union field _id.
    }  
  
Fields  
---  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Outcome)`)` Required. Outcome of the code execution.  
`output` |  `string` Optional. Contains stdout when code execution is successful, stderr or other description otherwise.  
Union field `_id`.`_id` can be only one of the following:  
`id` |  `string` Optional. The identifier of the `ExecutableCode` part this result is for. Only populated if the corresponding `ExecutableCode` has an id.  
  
### VideoMetadata

JSON representation  
---  
      
    
    {
      "startOffset": string,
      "endOffset": string,
      "fps": number
    }  
  
Fields  
---  
`startOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The start offset of the video.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`endOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The end offset of the video.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`fps` |  `number` Optional. The frame rate of the video sent to the model. If not specified, the default value is 1.0. The valid range is (0.0, 24.0].  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### MediaResolution

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "level": enum ([Level](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Level))
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`.`value` can be only one of the following:  
`level` |  `enum (`[Level](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.Level)`)` The tokenization quality used for given media.  
  
### AudioTranscription

JSON representation  
---  
      
    
    {
      "text": string,
      "speakerLabel": string,
      "words": [
        {
          object ([WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.WordInfo))
        }
      ]
    }  
  
Fields  
---  
`text` |  `string` Required. The transcription text of this audio segment.  
`speakerLabel` |  `string` Optional. A label identifying the speaker of this audio segment (e.g. "spk_1", "spk_2"). Present when diarization is set.  
`words[]` |  `object (`[WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/evaluate_instances#Input.Schema.WordInfo)`)` Optional. Detailed word-level transcriptions and timing details. Present when word_timestamp is set.  
  
### WordInfo

JSON representation  
---  
      
    
    {
      "word": string,
      "startOffset": string,
      "endOffset": string
    }  
  
Fields  
---  
`word` |  `string` Required. Transcript of the word.  
`startOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Start offset in time of the word relative to the start of the audio.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`endOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. End offset in time of the word relative to the start of the audio.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### EmbedContentConfig

JSON representation  
---  
      
    
    {
    
      // Union field _title can be only one of the following:
      "title": string
      // End of list of possible types for union field _title.
    
      // Union field _task_type can be only one of the following:
      "taskType": enum ([EmbeddingTaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbeddingTaskType))
      // End of list of possible types for union field _task_type.
    
      // Union field _auto_truncate can be only one of the following:
      "autoTruncate": boolean
      // End of list of possible types for union field _auto_truncate.
    
      // Union field _output_dimensionality can be only one of the following:
      "outputDimensionality": integer
      // End of list of possible types for union field _output_dimensionality.
    
      // Union field _document_ocr can be only one of the following:
      "documentOcr": boolean
      // End of list of possible types for union field _document_ocr.
    
      // Union field _audio_track_extraction can be only one of the following:
      "audioTrackExtraction": boolean
      // End of list of possible types for union field _audio_track_extraction.
    }  
  
Fields  
---  
Union field `_title`.`_title` can be only one of the following:  
`title` |  `string` Optional. The title for the text.Only applicable to text-only embedding models.  
Union field `_task_type`.`_task_type` can be only one of the following:  
`taskType` |  `enum (`[EmbeddingTaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Input.Schema.EmbeddingTaskType)`)` Optional. The task type of the embedding.Only applicable to text-only embedding models.  
Union field `_auto_truncate`.`_auto_truncate` can be only one of the following:  
`autoTruncate` |  `boolean` Optional. Whether to silently truncate the input content if it's longer than the maximum sequence length.Only applicable to text-only embedding models.  
Union field `_output_dimensionality`.`_output_dimensionality` can be only one of the following:  
`outputDimensionality` |  `integer` Optional. Reduced dimension for the output embedding. If set, excessive values in the output embedding are truncated from the end.  
Union field `_document_ocr`.`_document_ocr` can be only one of the following:  
`documentOcr` |  `boolean` Optional. Whether to enable OCR for document content.  
Union field `_audio_track_extraction`.`_audio_track_extraction` can be only one of the following:  
`audioTrackExtraction` |  `boolean` Optional. Whether to extract audio from video content.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Language

Supported programming languages for the generated code.

Enums  
---  
`LANGUAGE_UNSPECIFIED` | Unspecified language. This value should not be used.  
`PYTHON` | Python >= 3.10, with numpy and simpy available.  
  
### Outcome

Enumeration of possible outcomes of the code execution.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Unspecified status. This value should not be used.  
`OUTCOME_OK` | Code execution completed successfully. `output` contains the stdout, if any.  
`OUTCOME_FAILED` | Code execution failed. `output` contains the stderr and stdout, if any.  
`OUTCOME_DEADLINE_EXCEEDED` | Code execution ran for too long, and was cancelled. There may or may not be a partial `output` present.  
  
### Level

The media resolution level.

Enums  
---  
`MEDIA_RESOLUTION_UNSPECIFIED` | Media resolution has not been set.  
`MEDIA_RESOLUTION_LOW` | Media resolution set to low.  
`MEDIA_RESOLUTION_MEDIUM` | Media resolution set to medium.  
`MEDIA_RESOLUTION_HIGH` | Media resolution set to high.  
`MEDIA_RESOLUTION_ULTRA_HIGH` | Media resolution set to ultra high. This is for image only.  
  
### EmbeddingTaskType

Represents a downstream task the embeddings will be used for.

Enums  
---  
`UNSPECIFIED` | Unset value, which will default to one of the other enum values.  
`RETRIEVAL_QUERY` | Specifies the given text is a query in a search/retrieval setting.  
`RETRIEVAL_DOCUMENT` | Specifies the given text is a document from the corpus being searched.  
`SEMANTIC_SIMILARITY` | Specifies the given text will be used for STS.  
`CLASSIFICATION` | Specifies that the given text will be classified.  
`CLUSTERING` | Specifies that the embeddings will be used for clustering.  
`QUESTION_ANSWERING` | Specifies that the embeddings will be used for question answering.  
`FACT_VERIFICATION` | Specifies that the embeddings will be used for fact verification.  
`CODE_RETRIEVAL_QUERY` | Specifies that the embeddings will be used for code retrieval.  
  
## Output Schema

Response message for `PredictionService.EmbedContent`.

### EmbedContentResponse

JSON representation  
---  
      
    
    {
      "embedding": {
        object ([Embedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.Embedding))
      },
      "usageMetadata": {
        object ([UsageMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.UsageMetadata))
      },
      "truncated": boolean
    }  
  
Fields  
---  
`embedding` |  `object (`[Embedding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.Embedding)`)` The embedding generated from the input content.  
`usageMetadata` |  `object (`[UsageMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.UsageMetadata)`)` Usage metadata about the response(s).  
`truncated` |  `boolean` Whether the input content was truncated before generating the embedding.  
  
### Embedding

JSON representation  
---  
      
    
    {
      "values": [
        number
      ]
    }  
  
Fields  
---  
`values[]` |  `number` Embedding vector values.  
  
### UsageMetadata

JSON representation  
---  
      
    
    {
      "promptTokenCount": integer,
      "candidatesTokenCount": integer,
      "totalTokenCount": integer,
      "toolUsePromptTokenCount": integer,
      "thoughtsTokenCount": integer,
      "cachedContentTokenCount": integer,
      "promptTokensDetails": [
        {
          object ([ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount))
        }
      ],
      "cacheTokensDetails": [
        {
          object ([ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount))
        }
      ],
      "candidatesTokensDetails": [
        {
          object ([ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount))
        }
      ],
      "toolUsePromptTokensDetails": [
        {
          object ([ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount))
        }
      ],
      "trafficType": enum ([TrafficType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.TrafficType))
    }  
  
Fields  
---  
`promptTokenCount` |  `integer` The total number of tokens in the prompt. This includes any text, images, or other media provided in the request. When `cached_content` is set, this also includes the number of tokens in the cached content.  
`candidatesTokenCount` |  `integer` The total number of tokens in the generated candidates.  
`totalTokenCount` |  `integer` The total number of tokens for the entire request. This is the sum of `prompt_token_count`, `candidates_token_count`, `tool_use_prompt_token_count`, and `thoughts_token_count`.  
`toolUsePromptTokenCount` |  `integer` Output only. The number of tokens in the results from tool executions, which are provided back to the model as input, if applicable.  
`thoughtsTokenCount` |  `integer` Output only. The number of tokens that were part of the model's generated "thoughts" output, if applicable.  
`cachedContentTokenCount` |  `integer` Output only. The number of tokens in the cached content that was used for this request.  
`promptTokensDetails[]` |  `object (`[ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount)`)` Output only. A detailed breakdown of the token count for each modality in the prompt.  
`cacheTokensDetails[]` |  `object (`[ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount)`)` Output only. A detailed breakdown of the token count for each modality in the cached content.  
`candidatesTokensDetails[]` |  `object (`[ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount)`)` Output only. A detailed breakdown of the token count for each modality in the generated candidates.  
`toolUsePromptTokensDetails[]` |  `object (`[ModalityTokenCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.ModalityTokenCount)`)` Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.  
`trafficType` |  `enum (`[TrafficType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/embed_content#Output.Schema.TrafficType)`)` Output only. The traffic type for this request.  
  
### ModalityTokenCount

JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.Modality)),
      "tokenCount": integer
    }  
  
Fields  
---  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/generate_content#Output.Schema.Modality)`)` The modality that this token count applies to.  
`tokenCount` |  `integer` The number of tokens counted for this modality.  
  
### Modality

The modality of a `Part` of a `Content` message. A modality is the type of media, such as an image or a video. It is used to categorize the content of a `Part` for token counting purposes.

Enums  
---  
`MODALITY_UNSPECIFIED` | When a modality is not specified, it is treated as `TEXT`.  
`TEXT` | The `Part` contains plain text.  
`IMAGE` | The `Part` contains an image.  
`VIDEO` | The `Part` contains a video.  
`AUDIO` | The `Part` contains audio.  
`DOCUMENT` | The `Part` contains a document, such as a PDF.  
  
### TrafficType

The type of traffic that this request was processed with, indicating which quota gets consumed.

Enums  
---  
`TRAFFIC_TYPE_UNSPECIFIED` | Unspecified request traffic type.  
`ON_DEMAND` | Type for Pay-As-You-Go traffic.  
`ON_DEMAND_PRIORITY` | Type for Priority Pay-As-You-Go traffic.  
`ON_DEMAND_FLEX` | Type for Flex traffic.  
`PROVISIONED_THROUGHPUT` | Type for Provisioned Throughput traffic.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
