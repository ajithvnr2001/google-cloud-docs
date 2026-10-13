---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest
title: DataStream v1alpha1 API - Class CreateStreamRequest (2.0.0-alpha06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:54.204123+00:00
---

# DataStream v1alpha1 API - Class CreateStreamRequest (2.0.0-alpha06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1alpha1 API - Class CreateStreamRequest (2.0.0-alpha06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest)
  * [ 2.0.0-alpha05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/2.0.0-alpha05/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/1.0.0-beta02/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest)


    
    
    public sealed class CreateStreamRequest : IMessage<CreateStreamRequest>, IEquatable<CreateStreamRequest>, IDeepCloneable<CreateStreamRequest>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateStreamRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1)

## Assembly

Google.Cloud.Datastream.V1Alpha1.dll

## Constructors 

### CreateStreamRequest()
    
    
    public CreateStreamRequest()

### CreateStreamRequest(CreateStreamRequest)
    
    
    public CreateStreamRequest(CreateStreamRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest)`  
  
  
## Properties 

### Force
    
    
    public bool Force { get; set; }

Optional. Create the stream without validating it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent that owns the collection of streams.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.CreateStreamRequest#Google_Cloud_Datastream_V1Alpha1_CreateStreamRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Stream
    
    
    public Stream Stream { get; set; }

Required. The stream resource to create.

**Property Value**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.Stream)` |   
  
### StreamId
    
    
    public string StreamId { get; set; }

Required. The stream identifier.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. Only validate the stream, but do not create any resources. The default is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
