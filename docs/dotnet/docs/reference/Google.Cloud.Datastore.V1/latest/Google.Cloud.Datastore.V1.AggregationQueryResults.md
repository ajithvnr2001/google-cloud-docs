---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AggregationQueryResults
title: Google Cloud Datastore v1 API - Class AggregationQueryResults (5.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:01.815523+00:00
---

# Google Cloud Datastore v1 API - Class AggregationQueryResults (5.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AggregationQueryResults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Datastore v1 API - Class AggregationQueryResults (5.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AggregationQueryResults

Reference documentation and code samples for the Google Cloud Datastore v1 API class AggregationQueryResults.

Represents the result of an [AggregationQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AggregationQuery).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregationQueryResults

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1)

## Assembly

Google.Cloud.Datastore.V1.dll

## Properties 

### this[string]
    
    
    public Value this[string alias] { get; }

Returns the result of the aggregation function that is assigned to the given alias. Will be null if was not specified in the original query.

**Parameter**  
---  
**Name** | **Description**  
`alias` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The alias of the aggregation function that was provided in the aggregation query. If not provided, Datastore will pick a default name following the format `property_<incremental_id++>`. For example: `text` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT_UP_TO(4) OVER ( ... ); ```
    
    
     becomes:
     ```text
     ```
     AGGREGATE
       COUNT_UP_TO(1) AS count_up_to_1,
       COUNT_UP_TO(2) AS property_1,
       COUNT_UP_TO(3) AS count_up_to_3,
       COUNT_UP_TO(4) AS property_2
     OVER (
       ...
     );
      
  
**Property Value**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Value)` | The result of the aggregation function corresponding to the given alias.  
  
### Metrics
    
    
    public ExplainMetrics Metrics { get; }

The information about planning and execution (if any) of the query. This will be null if no analysis was requested.

**Property Value**  
---  
**Type** | **Description**  
`[ExplainMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.ExplainMetrics)` |   
  
### MoreResults
    
    
    public QueryResultBatch.Types.MoreResultsType MoreResults { get; }

The condition that caused the query to complete, indicating whether more results are available beyond the query limit or end cursor, or whether the data has been exhausted.

**Property Value**  
---  
**Type** | **Description**  
`[QueryResultBatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.QueryResultBatch)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.QueryResultBatch.Types)[MoreResultsType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.QueryResultBatch.Types.MoreResultsType)` |   
  
### ReadTime
    
    
    public Timestamp ReadTime { get; }

The time at which the snapshot was read. This will be null if the query was only planned, and not executed.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
