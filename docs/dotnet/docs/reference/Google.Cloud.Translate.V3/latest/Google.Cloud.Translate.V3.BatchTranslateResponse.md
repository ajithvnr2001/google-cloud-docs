---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse
title: Google Cloud Translation v3 API - Class BatchTranslateResponse (3.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:16.254497+00:00
---

# Google Cloud Translation v3 API - Class BatchTranslateResponse (3.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Translation v3 API - Class BatchTranslateResponse (3.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.11.0 (latest)  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BatchTranslateResponse : IMessage<BatchTranslateResponse>, IEquatable<BatchTranslateResponse>, IDeepCloneable<BatchTranslateResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Translation v3 API class BatchTranslateResponse.

Stored in the [google.longrunning.Operation.response][google.longrunning.Operation.response] field returned by BatchTranslateText if at least one sentence is translated successfully.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchTranslateResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchTranslateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchTranslateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchTranslateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Translate.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3)

## Assembly

Google.Cloud.Translate.V3.dll

## Constructors 

### BatchTranslateResponse()
    
    
    public BatchTranslateResponse()

### BatchTranslateResponse(BatchTranslateResponse)
    
    
    public BatchTranslateResponse(BatchTranslateResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchTranslateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.BatchTranslateResponse)`  
  
  
## Properties 

### EndTime
    
    
    public Timestamp EndTime { get; set; }

The time when the operation is finished and [google.longrunning.Operation.done][google.longrunning.Operation.done] is set to true.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### FailedCharacters
    
    
    public long FailedCharacters { get; set; }

Number of characters that have failed to process (Unicode codepoints).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### SubmitTime
    
    
    public Timestamp SubmitTime { get; set; }

Time when the operation was submitted.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### TotalCharacters
    
    
    public long TotalCharacters { get; set; }

Total number of characters (Unicode codepoints).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TranslatedCharacters
    
    
    public long TranslatedCharacters { get; set; }

Number of successfully translated characters (Unicode codepoints).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
