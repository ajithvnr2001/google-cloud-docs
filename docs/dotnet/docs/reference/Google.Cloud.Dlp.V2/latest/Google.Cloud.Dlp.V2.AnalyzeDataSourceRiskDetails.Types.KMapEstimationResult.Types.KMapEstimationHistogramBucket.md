---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket
title: Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:33.451862+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket : IMessage<AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket>, IEquatable<AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket>, IDeepCloneable<AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket.

A KMapEstimationHistogramBucket message with the following values: min_anonymity: 3 max_anonymity: 5 frequency: 42 means that there are 42 records whose quasi-identifier values correspond to 3, 4 or 5 people in the overlying population. An important particular case is when min_anonymity = max_anonymity = 1: the frequency field then corresponds to the number of uniquely identifiable records.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)[KMapEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)[KMapEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)[KMapEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### KMapEstimationHistogramBucket()
    
    
    public KMapEstimationHistogramBucket()

### KMapEstimationHistogramBucket(KMapEstimationHistogramBucket)
    
    
    public KMapEstimationHistogramBucket(AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)[KMapEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket)`  
  
  
## Properties 

### BucketSize
    
    
    public long BucketSize { get; set; }

Number of records within these anonymity bounds.

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
    
    
    public RepeatedField<AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationQuasiIdValues> BucketValues { get; }

Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)[KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)[KMapEstimationQuasiIdValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationQuasiIdValues)` |   
  
### MaxAnonymity
    
    
    public long MaxAnonymity { get; set; }

Always greater than or equal to min_anonymity.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### MinAnonymity
    
    
    public long MinAnonymity { get; set; }

Always positive.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
