---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest
title: Google Cloud Vision v1 API - Class AsyncBatchAnnotateFilesRequest (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:58.967581+00:00
---

# Google Cloud Vision v1 API - Class AsyncBatchAnnotateFilesRequest (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class AsyncBatchAnnotateFilesRequest (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)


    
    
    public sealed class AsyncBatchAnnotateFilesRequest : IMessage<AsyncBatchAnnotateFilesRequest>, IEquatable<AsyncBatchAnnotateFilesRequest>, IDeepCloneable<AsyncBatchAnnotateFilesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class AsyncBatchAnnotateFilesRequest.

Multiple async file annotation requests are batched into a single service call.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AsyncBatchAnnotateFilesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### AsyncBatchAnnotateFilesRequest()
    
    
    public AsyncBatchAnnotateFilesRequest()

### AsyncBatchAnnotateFilesRequest(AsyncBatchAnnotateFilesRequest)
    
    
    public AsyncBatchAnnotateFilesRequest(AsyncBatchAnnotateFilesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncBatchAnnotateFilesRequest)`  
  
  
## Properties 

### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Optional. Target project and location to make a call.

Format: `projects/{project-id}/locations/{location-id}`.

If no parent is specified, a region will be chosen automatically.

Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.

Example: `projects/project-A/locations/eu`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Requests
    
    
    public RepeatedField<AsyncAnnotateFileRequest> Requests { get; }

Required. Individual async file annotation requests for this batch.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AsyncAnnotateFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AsyncAnnotateFileRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
