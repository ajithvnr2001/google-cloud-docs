---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest
title: Vision AI v1 API - Class BatchRunProcessRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:58.692281+00:00
---

# Vision AI v1 API - Class BatchRunProcessRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class BatchRunProcessRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class BatchRunProcessRequest : IMessage<BatchRunProcessRequest>, IEquatable<BatchRunProcessRequest>, IDeepCloneable<BatchRunProcessRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class BatchRunProcessRequest.

Request message for running the processes in a batch.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchRunProcessRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### BatchRunProcessRequest()
    
    
    public BatchRunProcessRequest()

### BatchRunProcessRequest(BatchRunProcessRequest)
    
    
    public BatchRunProcessRequest(BatchRunProcessRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)`  
  
  
## Properties 

### BatchId
    
    
    public string BatchId { get; set; }

Output only. The batch ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Options
    
    
    public BatchRunProcessRequest.Types.BatchRunProcessOptions Options { get; set; }

Optional. Options for batch processes.

**Property Value**  
---  
**Type** | **Description**  
`[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest.Types)[BatchRunProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest.Types.BatchRunProcessOptions)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource shared by all processes being created.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsClusterName
    
    
    public ClusterName ParentAsClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClusterName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest#Google_Cloud_VisionAI_V1_BatchRunProcessRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClusterName)` |   
  
### Requests
    
    
    public RepeatedField<CreateProcessRequest> Requests { get; }

Required. The create process requests.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
