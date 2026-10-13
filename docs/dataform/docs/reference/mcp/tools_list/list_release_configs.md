---
url: https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs/
title: MCP Tools Reference: dataform.googleapis.com \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:09.385379+00:00
---

# MCP Tools Reference: dataform.googleapis.com  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  MCP Tools Reference: dataform.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_release_configs`

List the release configurations in a given Dataform repository.

The `parent` parameter value must be in the format `projects/{project_id}/locations/{location}/repositories/{repository}`.

The following code sample shows how to use `curl` to call the `list_release_configs` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://dataform.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_release_configs",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

`ListReleaseConfigs` request message.

### ListReleaseConfigsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The repository in which to list release configs. Must be in the format `projects/*/locations/*/repositories/*`.  
`pageSize` |  `integer` Optional. Maximum number of release configs to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.  
`pageToken` |  `string` Optional. Page token received from a previous `ListReleaseConfigs` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListReleaseConfigs`, with the exception of `page_size`, must match the call that provided the page token.  
  
## Output Schema

`ListReleaseConfigs` response message.

### ListReleaseConfigsResponse

JSON representation  
---  
      
    
    {
      "releaseConfigs": [
        {
          object ([ReleaseConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.ReleaseConfig))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`releaseConfigs[]` |  `object (`[ReleaseConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.ReleaseConfig)`)` List of release configs.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations which could not be reached.  
  
### ReleaseConfig

JSON representation  
---  
      
    
    {
      "name": string,
      "gitCommitish": string,
      "codeCompilationConfig": {
        object ([CodeCompilationConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.CodeCompilationConfig))
      },
      "cronSchedule": string,
      "timeZone": string,
      "recentScheduledReleaseRecords": [
        {
          object ([ScheduledReleaseRecord](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.ScheduledReleaseRecord))
        }
      ],
      "releaseCompilationResult": string,
      "disabled": boolean,
    
      // Union field _internal_metadata can be only one of the following:
      "internalMetadata": string
      // End of list of possible types for union field _internal_metadata.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The release config's name.  
`gitCommitish` |  `string` Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` \- a tag: `tag1` \- a branch name: `branch1`  
`codeCompilationConfig` |  `object (`[CodeCompilationConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.CodeCompilationConfig)`)` Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.  
`cronSchedule` |  `string` Optional. Optional schedule (in cron format) for automatic creation of compilation results.  
`timeZone` |  `string` Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is `UTC`.  
`recentScheduledReleaseRecords[]` |  `object (`[ScheduledReleaseRecord](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.ScheduledReleaseRecord)`)` Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.  
`releaseCompilationResult` |  `string` Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`disabled` |  `boolean` Optional. Disables automatic creation of compilation results.  
Union field `_internal_metadata`.`_internal_metadata` can be only one of the following:  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
### CodeCompilationConfig

JSON representation  
---  
      
    
    {
      "defaultDatabase": string,
      "defaultSchema": string,
      "defaultLocation": string,
      "assertionSchema": string,
      "vars": {
        string: string,
        ...
      },
      "databaseSuffix": string,
      "schemaSuffix": string,
      "tablePrefix": string,
      "builtinAssertionNamePrefix": string,
      "defaultNotebookRuntimeOptions": {
        object ([NotebookRuntimeOptions](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.NotebookRuntimeOptions))
      },
      "pipelineConfig": {
        object ([PipelineConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.PipelineConfig))
      }
    }  
  
Fields  
---  
`defaultDatabase` |  `string` Optional. The default database (Google Cloud project ID).  
`defaultSchema` |  `string` Optional. The default schema (BigQuery dataset ID).  
`defaultLocation` |  `string` Optional. The default BigQuery location to use. Defaults to "US". See the BigQuery docs for a full list of locations: <https://cloud.google.com/bigquery/docs/locations>.  
`assertionSchema` |  `string` Optional. The default schema (BigQuery dataset ID) for assertions.  
`vars` |  `map (key: string, value: string)` Optional. User-defined variables that are made available to project code during compilation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`databaseSuffix` |  `string` Optional. The suffix that should be appended to all database (Google Cloud project ID) names.  
`schemaSuffix` |  `string` Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names.  
`tablePrefix` |  `string` Optional. The prefix that should be prepended to all table names.  
`builtinAssertionNamePrefix` |  `string` Optional. The prefix to prepend to built-in assertion names.  
`defaultNotebookRuntimeOptions` |  `object (`[NotebookRuntimeOptions](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.NotebookRuntimeOptions)`)` Optional. The default notebook runtime options.  
`pipelineConfig` |  `object (`[PipelineConfig](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.PipelineConfig)`)` Optional. The pipeline options which defines the pipeline type and path within the Git repository.  
  
### VarsEntry

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
  
### NotebookRuntimeOptions

JSON representation  
---  
      
    
    {
      "aiPlatformNotebookRuntimeTemplate": string,
    
      // Union field execution_sink can be only one of the following:
      "gcsOutputBucket": string
      // End of list of possible types for union field execution_sink.
    
      // Union field repository_snapshot_storage can be only one of the following:
      "gcsRepositorySnapshotDestination": {
        object ([GcsRepositorySnapshotDestination](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.GcsRepositorySnapshotDestination))
      }
      // End of list of possible types for union field repository_snapshot_storage.
    }  
  
Fields  
---  
`aiPlatformNotebookRuntimeTemplate` |  `string` Optional. The resource name of the [Colab runtime template](https://cloud.google.com/colab/docs/runtimes), from which a runtime is created for notebook executions. If not specified, a runtime is created with Colab's default specifications.  
Union field `execution_sink`. The location to store the notebook execution result. `execution_sink` can be only one of the following:  
`gcsOutputBucket` |  `string` Optional. The Google Cloud Storage location to upload the result to. Format: `gs://bucket-name`.  
Union field `repository_snapshot_storage`. The destination of the snapshot of repository files to be available for read-only access inside a notebook runtime `repository_snapshot_storage` can be only one of the following:  
`gcsRepositorySnapshotDestination` |  `object (`[GcsRepositorySnapshotDestination](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.GcsRepositorySnapshotDestination)`)` Optional. The Google Cloud Storage destination to upload the snapshot to. For empty URI it defaults to the provided gcs_output_bucket. Format: `gs://bucket-name/path/`.  
  
### GcsRepositorySnapshotDestination

JSON representation  
---  
      
    
    {
      "repositorySnapshotUri": string
    }  
  
Fields  
---  
`repositorySnapshotUri` |  `string` Optional. The Google Cloud Storage destination to upload the repository snapshot to. Format: `gs://bucket-name/path/`.  
  
### PipelineConfig

JSON representation  
---  
      
    
    {
      "pipelineType": enum ([PipelineType](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.PipelineType)),
      "path": string
    }  
  
Fields  
---  
`pipelineType` |  `enum (`[PipelineType](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_release_configs#Output.Schema.PipelineType)`)` Required. The type of the pipeline.  
`path` |  `string` Required. The relative path within the Git repository where the pipeline is defined. For example, for a Dataform pipeline, it is a path to the folder where `workflow_settings.yaml` or `dataform.json` is located.  
  
### ScheduledReleaseRecord

JSON representation  
---  
      
    
    {
      "releaseTime": string,
    
      // Union field result can be only one of the following:
      "compilationResult": string,
      "errorStatus": {
        object ([Status](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_workflow_configs#Output.Schema.Status))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`releaseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of this release attempt.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `result`. The result of this release attempt. `result` can be only one of the following:  
`compilationResult` |  `string` The name of the created compilation result, if one was successfully created. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.  
`errorStatus` |  `object (`[Status](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/list_workflow_configs#Output.Schema.Status)`)` The error status encountered upon this attempt to create the compilation result, if the attempt was unsuccessful.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
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
  
### PipelineType

The type of the pipeline. This may be extended in the future. In case of UNSPECIFIED, the error will be thrown.

Enums  
---  
`PIPELINE_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`DATAFORM` | Regular Dataform pipeline.  
`SQL` | SQL single file asset.  
`NOTEBOOK` | Notebook single file asset.  
  
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

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
