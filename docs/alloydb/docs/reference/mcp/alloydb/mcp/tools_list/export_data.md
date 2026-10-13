---
url: https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data/
title: MCP Tools Reference: alloydb \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:41.688065+00:00
---

# MCP Tools Reference: alloydb  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Reference ](https://docs.cloud.google.com/alloydb/docs/reference/rest)



Send feedback 

#  MCP Tools Reference: alloydb Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `export_data`

Exports data from an AlloyDB cluster to a file in Google Cloud Storage.

**_Requirements_**

  * The cluster and primary instance must exist and be in a READY state.
  * The Google Cloud Storage bucket must exist.
  * The AlloyDB service account must have the `storage.objectAdmin` IAM role to write to the bucket. The AlloyDB service account is in the format of service-{project_number}@gcp-sa-alloydb.iam.gserviceaccount.com. {project_number} is a valid base-10 encoded positive integer.



**_Usage_**

  1. Call `export_data` to export data from a cluster to a Cloud Storage bucket.
  2. This will return a long-running operation that indicates the progress of the export. The time taken for the operation to complete depends on the size of data being exported.
  3. You can poll the status of the operation using the `get_operation` tool.



The following sample demonstrate how to use `curl` to invoke the `export_data` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://alloydb.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "export_data",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Export cluster request.

### ExportClusterRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "database": string,
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.GcsDestination))
      }
      // End of list of possible types for union field destination.
    
      // Union field export_options can be only one of the following:
      "csvExportOptions": {
        object ([CsvExportOptions](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.CsvExportOptions))
      },
      "sqlExportOptions": {
        object ([SqlExportOptions](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.SqlExportOptions))
      }
      // End of list of possible types for union field export_options.
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the cluster.  
`database` |  `string` Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
Union field `destination`. Oneof field to support other destinations in future. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.GcsDestination)`)` Required. Option to export data to cloud storage.  
Union field `export_options`. Required field to specify export file type and options. `export_options` can be only one of the following:  
`csvExportOptions` |  `object (`[CsvExportOptions](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.CsvExportOptions)`)` Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` |  `object (`[SqlExportOptions](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/export_data#Input.Schema.SqlExportOptions)`)` Options for exporting data in SQL format. Required field to be set for SQL file type.  
  
### GcsDestination

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form `gs://bucketName/fileName`.  
  
### CsvExportOptions

JSON representation  
---  
      
    
    {
      "selectQuery": string,
      "fieldDelimiter": string,
      "quoteCharacter": string,
      "escapeCharacter": string
    }  
  
Fields  
---  
`selectQuery` |  `string` Required. The SELECT query used to extract the data.  
`fieldDelimiter` |  `string` Optional. Specifies the character that separates columns within each row (line) of the file. The default is comma. The value of this argument has to be a character in Hex ASCII Code.  
`quoteCharacter` |  `string` Optional. Specifies the quoting character to be used when a data value is quoted. The default is double-quote. The value of this argument has to be a character in Hex ASCII Code.  
`escapeCharacter` |  `string` Optional. Specifies the character that should appear before a data character that needs to be escaped. The default is the same as quote character. The value of this argument has to be a character in Hex ASCII Code.  
  
### SqlExportOptions

JSON representation  
---  
      
    
    {
      "tables": [
        string
      ],
    
      // Union field _schema_only can be only one of the following:
      "schemaOnly": boolean
      // End of list of possible types for union field _schema_only.
    
      // Union field _clean_target_objects can be only one of the following:
      "cleanTargetObjects": boolean
      // End of list of possible types for union field _clean_target_objects.
    
      // Union field _if_exist_target_objects can be only one of the following:
      "ifExistTargetObjects": boolean
      // End of list of possible types for union field _if_exist_target_objects.
    }  
  
Fields  
---  
`tables[]` |  `string` Optional. Tables to export from.  
Union field `_schema_only`.`_schema_only` can be only one of the following:  
`schemaOnly` |  `boolean` Optional. If true, only export the schema.  
Union field `_clean_target_objects`.`_clean_target_objects` can be only one of the following:  
`cleanTargetObjects` |  `boolean` Optional. If true, output commands to DROP all the dumped database objects prior to outputting the commands for creating them.  
Union field `_if_exist_target_objects`.`_if_exist_target_objects` can be only one of the following:  
`ifExistTargetObjects` |  `boolean` Optional. If true, use DROP ... IF EXISTS commands to check for the object's existence before dropping it in clean_target_objects mode.  
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_cluster#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_cluster#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
