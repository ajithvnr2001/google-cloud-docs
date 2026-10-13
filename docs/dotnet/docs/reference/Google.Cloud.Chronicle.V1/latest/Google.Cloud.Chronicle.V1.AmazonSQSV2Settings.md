---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings
title: Chronicle v1 API - Class AmazonSQSV2Settings (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:37.364099+00:00
---

# Chronicle v1 API - Class AmazonSQSV2Settings (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class AmazonSQSV2Settings (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class AmazonSQSV2Settings : IMessage<AmazonSQSV2Settings>, IEquatable<AmazonSQSV2Settings>, IDeepCloneable<AmazonSQSV2Settings>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class AmazonSQSV2Settings.

AmazonSQSV2Settings is the settings proto for Omniflow SQS feeds.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AmazonSQSV2Settings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AmazonSQSV2Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AmazonSQSV2Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AmazonSQSV2Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### AmazonSQSV2Settings()
    
    
    public AmazonSQSV2Settings()

### AmazonSQSV2Settings(AmazonSQSV2Settings)
    
    
    public AmazonSQSV2Settings(AmazonSQSV2Settings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AmazonSQSV2Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AmazonSQSV2Settings)`  
  
  
## Properties 

### Authentication
    
    
    public SQSAuthV2 Authentication { get; set; }

Required. Authentication.

**Property Value**  
---  
**Type** | **Description**  
`[SQSAuthV2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.SQSAuthV2)` |   
  
### ChronicleServiceAccount
    
    
    public string ChronicleServiceAccount { get; set; }

Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IncludePrefixes
    
    
    public RepeatedField<string> IncludePrefixes { get; }

Optional. Optional list of object prefixes to include.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaxLookbackDays
    
    
    public int MaxLookbackDays { get; set; }

Optional. Maximum File Age to ingest in days.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Queue
    
    
    public string Queue { get; set; }

Required. Amazon Resource Name(ARN) of the queue.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### S3Uri
    
    
    public string S3Uri { get; set; }

Required. S3 URI.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceDeletionOption
    
    
    public SourceDeletionOptionV2 SourceDeletionOption { get; set; }

Optional. Source deletion option.

**Property Value**  
---  
**Type** | **Description**  
`[SourceDeletionOptionV2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.SourceDeletionOptionV2)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
