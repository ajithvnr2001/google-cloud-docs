---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata
title: Google Cloud Translation v3 API - Class DeleteGlossaryMetadata (3.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:43.682790+00:00
---

# Google Cloud Translation v3 API - Class DeleteGlossaryMetadata (3.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Translation v3 API - Class DeleteGlossaryMetadata (3.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.11.0 (latest)  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class DeleteGlossaryMetadata : IMessage<DeleteGlossaryMetadata>, IEquatable<DeleteGlossaryMetadata>, IDeepCloneable<DeleteGlossaryMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Translation v3 API class DeleteGlossaryMetadata.

Stored in the [google.longrunning.Operation.metadata][google.longrunning.Operation.metadata] field returned by DeleteGlossary.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteGlossaryMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteGlossaryMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteGlossaryMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteGlossaryMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Translate.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3)

## Assembly

Google.Cloud.Translate.V3.dll

## Constructors 

### DeleteGlossaryMetadata()
    
    
    public DeleteGlossaryMetadata()

### DeleteGlossaryMetadata(DeleteGlossaryMetadata)
    
    
    public DeleteGlossaryMetadata(DeleteGlossaryMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteGlossaryMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

The name of the glossary that is being deleted.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public DeleteGlossaryMetadata.Types.State State { get; set; }

The current state of the glossary deletion operation.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteGlossaryMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translate.V3/latest/Google.Cloud.Translate.V3.DeleteGlossaryMetadata.Types.State)` |   
  
### SubmitTime
    
    
    public Timestamp SubmitTime { get; set; }

The time when the operation was submitted to the server.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
