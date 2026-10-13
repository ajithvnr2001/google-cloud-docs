---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results/
title: MCP Tools Reference: cloudasset.googleapis.com \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:13.032282+00:00
---

# MCP Tools Reference: cloudasset.googleapis.com  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  MCP Tools Reference: cloudasset.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `export_iam_analysis_results`

Analyzes Google Cloud IAM policies asynchronously and exports the results to a BigQuery dataset or Google Cloud Storage bucket. Use this for large-scale analysis (for example, expanding resources or impersonation).

This tool requires the `analysis_query` parameter, which specifies the root container where policies are analyzed (`scope`) and offers optional selectors for resource names, principal identifiers, and applicable roles and permissions.

  * Folder and Organization scopes are _not_ supported; `scope` must be a project scope (for example, `projects/PROJECT_ID`).
  * When analyzing policies in a specific project (for example, 'in `PROJECT_ID`'), set `scope` to `projects/PROJECT_ID` and do _not_ set `resource_selector`.
  * Only set `resource_selector.full_resource_name` (for example, `//storage.googleapis.com/BUCKET_NAME`) when a request is made specifically for access to a particular resource within that scope.



This tool returns a long-running operation object containing an operation `name`. You must subsequently use the `get_iam_policy_analysis_status` tool with this `name` to poll the status until the `done` field is `true`.

The following code sample shows how to use `curl` to call the `export_iam_analysis_results` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudasset.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "export_iam_analysis_results",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

A request message for `AssetService.AnalyzeIamPolicyLongrunning`.

### AnalyzeIamPolicyLongrunningRequest

JSON representation  
---  
      
    
    {
      "analysisQuery": {
        object ([IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery))
      },
      "savedAnalysisQuery": string,
      "outputConfig": {
        object ([IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.IamPolicyAnalysisOutputConfig))
      }
    }  
  
Fields  
---  
`analysisQuery` |  `object (`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IamPolicyAnalysisQuery)`)` Required. The request query.  
`savedAnalysisQuery` |  `string` Optional. The name of a saved query, which must be in the format of `projects/project_number/savedQueries/saved_query_id`.  If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) doc.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`outputConfig` |  `object (`[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.IamPolicyAnalysisOutputConfig)`)` Required. Output configuration indicating where the results will be output to.  
  
### IamPolicyAnalysisQuery

JSON representation  
---  
      
    
    {
      "scope": string,
      "resourceSelector": {
        object ([ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector))
      },
      "identitySelector": {
        object ([IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector))
      },
      "accessSelector": {
        object ([AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector))
      },
      "options": {
        object ([Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options))
      },
      "conditionContext": {
        object ([ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext))
      }
    }  
  
Fields  
---  
`scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345").To know how to get a project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects).  
`resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.Options)`)` Optional. The query options.  
`conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Input.Schema.ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
  
### ResourceSelector

JSON representation  
---  
      
    
    {
      "fullResourceName": string
    }  
  
Fields  
---  
`fullResourceName` |  `string` Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).  
  
### IdentitySelector

JSON representation  
---  
      
    
    {
      "identity": string
    }  
  
Fields  
---  
`identity` |  `string` Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding).The examples of supported forms are: "user:[mike@example.com"](mailto:mike@example.com"), "group:[admins@example.com"](mailto:admins@example.com"), "domain:google.com", "serviceAccount:[my-project-id@appspot.gserviceaccount.com"](mailto:my-project-id@appspot.gserviceaccount.com").Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.  
  
### AccessSelector

JSON representation  
---  
      
    
    {
      "roles": [
        string
      ],
      "permissions": [
        string
      ]
    }  
  
Fields  
---  
`roles[]` |  `string` Optional. The roles to appear in result.  
`permissions[]` |  `string` Optional. The permissions to appear in result.  
  
### Options

JSON representation  
---  
      
    
    {
      "expandGroups": boolean,
      "expandRoles": boolean,
      "expandResources": boolean,
      "outputResourceEdges": boolean,
      "outputGroupEdges": boolean,
      "analyzeServiceAccountImpersonation": boolean
    }  
  
Fields  
---  
`expandGroups` |  `boolean` Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding.If `IamPolicyAnalysisQuery.identity_selector` is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set.If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][].Default is false.  
`expandRoles` |  `boolean` Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions.If `IamPolicyAnalysisQuery.access_selector` is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set.Default is false.  
`expandResources` |  `boolean` Optional. If true and `IamPolicyAnalysisQuery.resource_selector` is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy.For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P.If true and `IamPolicyAnalysisQuery.resource_selector` is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option.For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource.If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][].Default is false.  
`outputResourceEdges` |  `boolean` Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.  
`outputGroupEdges` |  `boolean` Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.  
`analyzeServiceAccountImpersonation` |  `boolean` Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use `AssetService.AnalyzeIamPolicyLongrunning` RPC instead.For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `AnalyzeIamPolicyResponse.service_account_impersonation_analysis`.Only the following permissions are considered in this analysis:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`

Default is false.  
  
### ConditionContext

JSON representation  
---  
      
    
    {
    
      // Union field TimeContext can be only one of the following:
      "accessTime": string
      // End of list of possible types for union field TimeContext.
    }  
  
Fields  
---  
Union field `TimeContext`. The IAM conditions time context. `TimeContext` can be only one of the following:  
`accessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### IamPolicyAnalysisOutputConfig

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.GcsDestination))
      },
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.BigQueryDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. IAM policy analysis export destination. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.GcsDestination)`)` Destination on Cloud Storage.  
`bigqueryDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.BigQueryDestination)`)` Destination on BigQuery.  
  
### GcsDestination

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the analysis result.  
  
### BigQueryDestination

JSON representation  
---  
      
    
    {
      "dataset": string,
      "tablePrefix": string,
      "partitionKey": enum ([PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.PartitionKey)),
      "writeDisposition": string
    }  
  
Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the analysis results should be exported. If this dataset does not exist, the export call will return an INVALID_ARGUMENT error.  
`tablePrefix` |  `string` Required. The prefix of the BigQuery tables to which the analysis results will be written. Tables will be created based on this table_prefix if not exist: * _analysis table will contain export operation's metadata. * _analysis_result will contain all the `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.IamPolicyAnalysisResult)`. When [partition_key] is specified, both tables will be partitioned based on the [partition_key].  
`partitionKey` |  `enum (`[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Input.Schema.PartitionKey)`)` The partition key for BigQuery partitioned table.  
`writeDisposition` |  `string` Optional. Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, an error is returned.

The default value is WRITE_APPEND. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Details are at <https://cloud.google.com/bigquery/docs/loading-data-local#appending_to_or_overwriting_a_table_using_a_local_file>.  
  
### PartitionKey

This enum determines the partition key column for the bigquery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. Tables won't be partitioned using this option.  
`REQUEST_TIME` | The time when the request is received. If specified as partition key, the result table(s) is partitioned by the RequestTime column, an additional timestamp column representing when the request was received.  
  
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
        object ([Status](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Output.Schema.Status))
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
`error` |  `object (`[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
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
`code` |  `integer` The status code, which should be an enum value of `[google.rpc.Code](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy#Output.Schema.Code)`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
