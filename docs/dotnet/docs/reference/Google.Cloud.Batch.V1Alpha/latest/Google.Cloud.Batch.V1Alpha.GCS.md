---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS
title: Batch v1alpha API - Class GCS (1.0.0-alpha35) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:06.384489+00:00
---

# Batch v1alpha API - Class GCS (1.0.0-alpha35)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Batch v1alpha API - Class GCS (1.0.0-alpha35) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha35 (latest)  1.0.0-alpha34 
    
    
    public sealed class GCS : IMessage<GCS>, IEquatable<GCS>, IDeepCloneable<GCS>, IBufferMessage, IMessage

Reference documentation and code samples for the Batch v1alpha API class GCS.

Represents a Google Cloud Storage volume.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GCS

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GCS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GCS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GCS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Batch.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha)

## Assembly

Google.Cloud.Batch.V1Alpha.dll

## Constructors 

### GCS()
    
    
    public GCS()

### GCS(GCS)
    
    
    public GCS(GCS other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GCS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.GCS)`  
  
  
## Properties 

### RemotePath
    
    
    public string RemotePath { get; set; }

Remote path, either a bucket name or a subdirectory of a bucket, e.g.: bucket_name, bucket_name/subdirectory/

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
