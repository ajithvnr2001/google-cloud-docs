---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest
title: Google Bigtable v2 API - Class PrepareQueryRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:58.102827+00:00
---

# Google Bigtable v2 API - Class PrepareQueryRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class PrepareQueryRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class PrepareQueryRequest : IMessage<PrepareQueryRequest>, IEquatable<PrepareQueryRequest>, IDeepCloneable<PrepareQueryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class PrepareQueryRequest.

Request message for Bigtable.PrepareQuery

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PrepareQueryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### PrepareQueryRequest()
    
    
    public PrepareQueryRequest()

### PrepareQueryRequest(PrepareQueryRequest)
    
    
    public PrepareQueryRequest(PrepareQueryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
  
  
## Properties 

### AppProfileId
    
    
    public string AppProfileId { get; set; }

Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataFormatCase
    
    
    public PrepareQueryRequest.DataFormatOneofCase DataFormatCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)[DataFormatOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest.DataFormatOneofCase)` |   
  
### InstanceName
    
    
    public string InstanceName { get; set; }

Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceNameAsInstanceName
    
    
    public InstanceName InstanceNameAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)-typed view over the [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest#Google_Cloud_Bigtable_V2_PrepareQueryRequest_InstanceName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)` |   
  
### ParamTypes
    
    
    public MapField<string, Type> ParamTypes { get; }

Required. `param_types` is a map of parameter identifier strings to their `Type`s.

In query string, a parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`) in the query string.

For example, if param_types["firstName"] = Bytes then @firstName will be a query parameter of type Bytes. The specific `Value` to be used for the query execution must be sent in `ExecuteQueryRequest` in the `params` map.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Type)` |   
  
### ProtoFormat
    
    
    public ProtoFormat ProtoFormat { get; set; }

Protocol buffer format as described by ProtoSchema and ProtoRows messages.

**Property Value**  
---  
**Type** | **Description**  
`[ProtoFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ProtoFormat)` |   
  
### Query
    
    
    public string Query { get; set; }

Required. The query string.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
