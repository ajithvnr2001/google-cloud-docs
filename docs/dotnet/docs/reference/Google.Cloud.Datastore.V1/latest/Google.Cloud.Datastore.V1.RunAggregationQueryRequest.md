---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest
title: Google Cloud Datastore v1 API - Class RunAggregationQueryRequest (5.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:05.231388+00:00
---

# Google Cloud Datastore v1 API - Class RunAggregationQueryRequest (5.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Datastore v1 API - Class RunAggregationQueryRequest (5.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class RunAggregationQueryRequest : IMessage<RunAggregationQueryRequest>, IEquatable<RunAggregationQueryRequest>, IDeepCloneable<RunAggregationQueryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Datastore v1 API class RunAggregationQueryRequest.

The request for [Datastore.RunAggregationQuery][google.datastore.v1.Datastore.RunAggregationQuery].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RunAggregationQueryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RunAggregationQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RunAggregationQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RunAggregationQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1)

## Assembly

Google.Cloud.Datastore.V1.dll

## Constructors 

### RunAggregationQueryRequest()
    
    
    public RunAggregationQueryRequest()

### RunAggregationQueryRequest(RunAggregationQueryRequest)
    
    
    public RunAggregationQueryRequest(RunAggregationQueryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RunAggregationQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest)`  
  
  
## Properties 

### AggregationQuery
    
    
    public AggregationQuery AggregationQuery { get; set; }

The query to run.

**Property Value**  
---  
**Type** | **Description**  
`[AggregationQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AggregationQuery)` |   
  
### DatabaseId
    
    
    public string DatabaseId { get; set; }

The ID of the database against which to make the request.

'(default)' is not allowed; please use empty string '' to refer the default database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExplainOptions
    
    
    public ExplainOptions ExplainOptions { get; set; }

Optional. Explain options for the query. If set, additional query statistics will be returned. If not, only query results will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[ExplainOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.ExplainOptions)` |   
  
### GqlQuery
    
    
    public GqlQuery GqlQuery { get; set; }

The GQL query to run. This query must be an aggregation query.

**Property Value**  
---  
**Type** | **Description**  
`[GqlQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.GqlQuery)` |   
  
### PartitionId
    
    
    public PartitionId PartitionId { get; set; }

Entities are partitioned into subsets, identified by a partition ID. Queries are scoped to a single partition. This partition ID is normalized with the standard default context partition ID.

**Property Value**  
---  
**Type** | **Description**  
`[PartitionId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PartitionId)` |   
  
### ProjectId
    
    
    public string ProjectId { get; set; }

Required. The ID of the project against which to make the request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QueryTypeCase
    
    
    public RunAggregationQueryRequest.QueryTypeOneofCase QueryTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RunAggregationQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest)[QueryTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunAggregationQueryRequest.QueryTypeOneofCase)` |   
  
### ReadOptions
    
    
    public ReadOptions ReadOptions { get; set; }

The options for this query.

**Property Value**  
---  
**Type** | **Description**  
`[ReadOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.ReadOptions)` |   
  
### RequestOptions
    
    
    public RequestOptions RequestOptions { get; set; }

Optional. The options for this request.

**Property Value**  
---  
**Type** | **Description**  
`[RequestOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RequestOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
