---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.Statistics
title: Google Cloud Spanner v1 API - Class SessionPool.Statistics (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:02.075987+00:00
---

# Google Cloud Spanner v1 API - Class SessionPool.Statistics (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.Statistics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class SessionPool.Statistics (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class SessionPool.Statistics

Reference documentation and code samples for the Google Cloud Spanner v1 API class SessionPool.Statistics.

A snapshot of statistics for a [SessionPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionPool.Statistics

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Properties 

### PerSegmentStatistics
    
    
    public IReadOnlyList<SessionPool.SessionPoolSegmentStatistics> PerSegmentStatistics { get; }

The statistics broken down by [SessionPool.SessionPoolSegmentKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentKey). This is never null, but may be empty.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[SessionPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool)[SessionPoolSegmentStatistics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentStatistics)` |   
  
### TotalActiveSessionCount
    
    
    public int TotalActiveSessionCount { get; }

The total of [ActiveSessionCount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentStatistics#Google_Cloud_Spanner_V1_SessionPool_SessionPoolSegmentStatistics_ActiveSessionCount) values across all databases in the pool.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TotalInFlightCreationCount
    
    
    public int TotalInFlightCreationCount { get; }

The total of [InFlightCreationCount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentStatistics#Google_Cloud_Spanner_V1_SessionPool_SessionPoolSegmentStatistics_InFlightCreationCount) values across all databases in the pool.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TotalPendingAcquisitionCount
    
    
    public int TotalPendingAcquisitionCount { get; }

The total of [PendingAcquisitionCount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentStatistics#Google_Cloud_Spanner_V1_SessionPool_SessionPoolSegmentStatistics_PendingAcquisitionCount) values across all databases in the pool.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TotalPoolCount
    
    
    public int TotalPoolCount { get; }

The total of [PoolCount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.SessionPoolSegmentStatistics#Google_Cloud_Spanner_V1_SessionPool_SessionPoolSegmentStatistics_PoolCount) values across all databases in the pool.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
