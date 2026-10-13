---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest
title: DataStream v1 API - Class GetStreamRequest (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:29.551822+00:00
---

# DataStream v1 API - Class GetStreamRequest (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class GetStreamRequest (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.GetStreamRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.GetStreamRequest)


    
    
    public sealed class GetStreamRequest : IMessage<GetStreamRequest>, IEquatable<GetStreamRequest>, IDeepCloneable<GetStreamRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1 API class GetStreamRequest.

Request message for getting a stream.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetStreamRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Constructors 

### GetStreamRequest()
    
    
    public GetStreamRequest()

### GetStreamRequest(GetStreamRequest)
    
    
    public GetStreamRequest(GetStreamRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the stream resource to get.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StreamName
    
    
    public StreamName StreamName { get; set; }

[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest#Google_Cloud_Datastream_V1_GetStreamRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
