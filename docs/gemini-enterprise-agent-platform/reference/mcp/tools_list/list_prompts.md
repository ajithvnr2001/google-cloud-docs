---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/list_prompts/
title: MCP Tools Reference: aiplatform.googleapis.com \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:57:05.834216+00:00
---

# MCP Tools Reference: aiplatform.googleapis.com  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/list_prompts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  MCP Tools Reference: aiplatform.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_prompts`

Lists all managed prompts in a location. Use this to browse existing prompts or map a user-friendly display_name to a technical resource name. CRITICAL: For {region}, use the region specified in the current context window. If no region is specified, prompt the user to provide one. Do not use 'global'.

The following sample demonstrate how to use `curl` to invoke the `list_prompts` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://aiplatform.googleapis.com/mcp/generate' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_prompts",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for `DatasetService.ListDatasets`.

### ListDatasetsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "pageSize": integer,
      "pageToken": string,
      "readMask": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The name of the Dataset's parent resource. Format: `projects/{project}/locations/{location}`  
`filter` |  `string` An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

  * `display_name`: supports = and !=
  * `metadata_schema_uri`: supports = and !=
  * `labels` supports general map functions that is: 
    * `labels.key=value` \- key:value equality
    * `labels.key:* or labels:key - key existence
    * A key including a space must be quoted. `labels."a key"`.

Some examples:

  * `displayName="myDisplayName"`
  * `labels.myKey="myValue"`

  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
`readMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

  * `display_name`
  * `create_time`
  * `update_time`

  
  
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
  
## Output Schema

Response message for `DatasetService.ListDatasets`.

### ListDatasetsResponse

JSON representation  
---  
      
    
    {
      "datasets": [
        {
          object ([Dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_prompt#Input.Schema.Dataset))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`datasets[]` |  `object (`[Dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_prompt#Input.Schema.Dataset)`)` A list of Datasets that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
### Dataset

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "metadataSchemaUri": string,
      "metadata": value,
      "dataItemCount": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "savedQueries": [
        {
          object ([SavedQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_prompt#Input.Schema.SavedQuery))
        }
      ],
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_endpoint#Input.Schema.EncryptionSpec))
      },
      "metadataArtifact": string,
      "modelReference": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`displayName` |  `string` Required. The user-defined name of the Dataset. The name can be up to 128 characters long and can consist of any UTF-8 characters.  
`description` |  `string` The description of the Dataset.  
`metadataSchemaUri` |  `string` Required. Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/.  
`metadata` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. Additional information about the Dataset.  
`dataItemCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of DataItems in this Dataset. Only apply for non-structured Dataset.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this Dataset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this Dataset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.  
`labels` |  `map (key: string, value: string)` The labels with user-defined metadata to organize your Datasets.Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded).See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Dataset:

  * "aiplatform.googleapis.com/dataset_metadata_schema": output only, its value is the `metadata_schema's` title.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`savedQueries[]` |  `object (`[SavedQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_prompt#Input.Schema.SavedQuery)`)` All SavedQueries belong to the Dataset will be returned in List/Get Dataset response. The annotation_specs field will not be populated except for UI cases which will only use `annotation_spec_count`. In CreateDataset request, a SavedQuery is created together if this field is set, up to one SavedQuery can be set in CreateDatasetRequest. The SavedQuery should not contain any AnnotationSpec.  
`encryptionSpec` |  `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/mcp/tools_list/create_endpoint#Input.Schema.EncryptionSpec)`)` Customer-managed encryption key spec for a Dataset. If set, this Dataset and all sub-resources of this Dataset will be secured by this key.  
`metadataArtifact` |  `string` Output only. The resource name of the Artifact that was created in MetadataStore when creating the Dataset. The Artifact resource name pattern is `projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}`.  
`modelReference` |  `string` Optional. Reference to the public base model last used by the dataset. Only set for prompt datasets.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
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
  
### SavedQuery

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "metadata": value,
      "createTime": string,
      "updateTime": string,
      "annotationFilter": string,
      "problemType": string,
      "annotationSpecCount": integer,
      "etag": string,
      "supportAutomlTraining": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of the SavedQuery.  
`displayName` |  `string` Required. The user-defined name of the SavedQuery. The name can be up to 128 characters long and can consist of any UTF-8 characters.  
`metadata` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Some additional information about the SavedQuery.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this SavedQuery was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when SavedQuery was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotationFilter` |  `string` Output only. Filters on the Annotations in the dataset.  
`problemType` |  `string` Required. Problem type of the SavedQuery. Allowed values:

  * IMAGE_CLASSIFICATION_SINGLE_LABEL
  * IMAGE_CLASSIFICATION_MULTI_LABEL
  * IMAGE_BOUNDING_POLY
  * IMAGE_BOUNDING_BOX
  * TEXT_CLASSIFICATION_SINGLE_LABEL
  * TEXT_CLASSIFICATION_MULTI_LABEL
  * TEXT_EXTRACTION
  * TEXT_SENTIMENT
  * VIDEO_CLASSIFICATION
  * VIDEO_OBJECT_TRACKING

  
`annotationSpecCount` |  `integer` Output only. Number of AnnotationSpecs in the context of the SavedQuery.  
`etag` |  `string` Used to perform a consistent read-modify-write update. If not set, a blind "overwrite" update happens.  
`supportAutomlTraining` |  `boolean` Output only. If the Annotations belonging to the SavedQuery can be used for AutoML training.  
  
### EncryptionSpec

JSON representation  
---  
      
    
    {
      "kmsKeyName": string
    }  
  
Fields  
---  
`kmsKeyName` |  `string` Required. Resource name of the Cloud KMS key used to protect the resource.The Cloud KMS key must be in the same region as the resource. It must have the format `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
