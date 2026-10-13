---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest
title: Google Bigtable v2 API - Class ExecuteQueryRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:46.590707+00:00
---

# Google Bigtable v2 API - Class ExecuteQueryRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ExecuteQueryRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ExecuteQueryRequest : IMessage<ExecuteQueryRequest>, IEquatable<ExecuteQueryRequest>, IDeepCloneable<ExecuteQueryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ExecuteQueryRequest.

Request message for Bigtable.ExecuteQuery

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExecuteQueryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### ExecuteQueryRequest()
    
    
    public ExecuteQueryRequest()

### ExecuteQueryRequest(ExecuteQueryRequest)
    
    
    public ExecuteQueryRequest(ExecuteQueryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
  
  
## Properties 

### AppProfileId
    
    
    public string AppProfileId { get; set; }

Optional. This value specifies routing for replication. If not specified, the `default` application profile will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataFormatCase
    
    
    public ExecuteQueryRequest.DataFormatOneofCase DataFormatCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)[DataFormatOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest.DataFormatOneofCase)` |   
  
### InstanceName
    
    
    public string InstanceName { get; set; }

Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceNameAsInstanceName
    
    
    public InstanceName InstanceNameAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)-typed view over the [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest#Google_Cloud_Bigtable_V2_ExecuteQueryRequest_InstanceName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)` |   
  
### Params
    
    
    public MapField<string, Value> Params { get; }

Required. params contains string type keys and Bigtable type values that bind to placeholders in the query string. In query string, a parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`) in the query string.

For example, if `params["firstName"] = bytes_value: "foo" type {bytes_type {}}` then `@firstName` will be replaced with googlesql bytes value "foo" in the query string during query evaluation.

If `Value.kind` is not set, the value is treated as a NULL value of the given type. For example, if `params["firstName"] = type {string_type {}}` then `@firstName` will be replaced with googlesql null string.

If `query` is set, any empty `Value.type` in the map will be rejected with `INVALID_ARGUMENT`.

If `prepared_query` is set, any empty `Value.type` in the map will be inferred from the `param_types` in the `PrepareQueryRequest`. Any non-empty `Value.type` must match the corresponding `param_types` entry, or be rejected with `INVALID_ARGUMENT`.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Value)` |   
  
### PreparedQuery
    
    
    public ByteString PreparedQuery { get; set; }

A prepared query that was returned from `PrepareQueryResponse`.

Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.

Setting this field also places restrictions on several other fields:

  * `data_format` must be empty.
  * `validate_only` must be false.
  * `params` must match the `param_types` set in the `PrepareQueryRequest`.



**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ProtoFormat
    
    
    [Obsolete]
    public ProtoFormat ProtoFormat { get; set; }

Protocol buffer format as described by ProtoSchema and ProtoRows messages.

**Property Value**  
---  
**Type** | **Description**  
`[ProtoFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ProtoFormat)` |   
  
### Query
    
    
    [Obsolete]
    public string Query { get; set; }

Required. The query string.

Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResumeToken
    
    
    public ByteString ResumeToken { get; set; }

Optional. If this request is resuming a previously interrupted query execution, `resume_token` should be copied from the last PartialResultSet yielded before the interruption. Doing this enables the query execution to resume where the last one left off. The rest of the request parameters must exactly match the request that yielded this token. Otherwise the request will fail.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ViewParameters
    
    
    public MapField<string, Value> ViewParameters { get; }

Optional. This map provides the runtime values returned by the VIEW_PARAMETERS() function calls, typically used for user-level scoping of data based on identity.

The key is the name of the view parameter e.g. `user_id`, and the value is the parameter value e.g. `alice@example.com`.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Value)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
