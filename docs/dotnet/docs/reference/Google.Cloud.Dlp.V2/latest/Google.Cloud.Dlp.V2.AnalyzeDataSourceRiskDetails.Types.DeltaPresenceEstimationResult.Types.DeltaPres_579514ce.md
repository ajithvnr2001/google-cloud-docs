---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket
title: Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:31.911266+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket : IMessage<AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket>, IEquatable<AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket>, IDeepCloneable<AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket.

A DeltaPresenceEstimationHistogramBucket message with the following values: min_probability: 0.1 max_probability: 0.2 frequency: 42 means that there are 42 records for which δ is in [0.1, 0.2). An important particular case is when min_probability = max_probability = 1: then, every individual who shares this quasi-identifier combination is in the dataset.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)[DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)[DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)[DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### DeltaPresenceEstimationHistogramBucket()
    
    
    public DeltaPresenceEstimationHistogramBucket()

### DeltaPresenceEstimationHistogramBucket(DeltaPresenceEstimationHistogramBucket)
    
    
    public DeltaPresenceEstimationHistogramBucket(AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)[DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket)`  
  
  
## Properties 

### BucketSize
    
    
    public long BucketSize { get; set; }

Number of records within these probability bounds.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BucketValueCount
    
    
    public long BucketValueCount { get; set; }

Total number of distinct quasi-identifier tuple values in this bucket.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BucketValues
    
    
    public RepeatedField<AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationQuasiIdValues> BucketValues { get; }

Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)[DeltaPresenceEstimationQuasiIdValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationQuasiIdValues)` |   
  
### MaxProbability
    
    
    public double MaxProbability { get; set; }

Always greater than or equal to min_probability.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### MinProbability
    
    
    public double MinProbability { get; set; }

Between 0 and 1.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
