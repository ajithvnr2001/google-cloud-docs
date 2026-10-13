---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest
title: Cloud Life Sciences v2beta API - Class RunPipelineRequest (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:21.135980+00:00
---

# Cloud Life Sciences v2beta API - Class RunPipelineRequest (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Life Sciences v2beta API - Class RunPipelineRequest (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/2.0.0-beta06/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/1.0.0-beta02/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest)


    
    
    public sealed class RunPipelineRequest : IMessage<RunPipelineRequest>, IEquatable<RunPipelineRequest>, IDeepCloneable<RunPipelineRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Life Sciences v2beta API class RunPipelineRequest.

The arguments to the `RunPipeline` method. The requesting user must have the `iam.serviceAccounts.actAs` permission for the Cloud Life Sciences service account or the request will fail.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RunPipelineRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RunPipelineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RunPipelineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RunPipelineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.LifeSciences.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta)

## Assembly

Google.Cloud.LifeSciences.V2Beta.dll

## Constructors 

### RunPipelineRequest()
    
    
    public RunPipelineRequest()

### RunPipelineRequest(RunPipelineRequest)
    
    
    public RunPipelineRequest(RunPipelineRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RunPipelineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.RunPipelineRequest)`  
  
  
## Properties 

### Labels
    
    
    public MapField<string, string> Labels { get; }

User-defined labels to associate with the returned operation. These labels are not propagated to any Google Cloud Platform resources used by the operation, and can be modified at any time.

To associate labels with resources created while executing the operation, see the appropriate resource message (for example, `VirtualMachine`).

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

The project and location that this request should be executed against.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Pipeline
    
    
    public Pipeline Pipeline { get; set; }

Required. The description of the pipeline to run.

**Property Value**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LifeSciences.V2Beta/latest/Google.Cloud.LifeSciences.V2Beta.Pipeline)` |   
  
### PubSubTopic
    
    
    public string PubSubTopic { get; set; }

The name of an existing Pub/Sub topic. The server will publish messages to this topic whenever the status of the operation changes. The Life Sciences Service Agent account must have publisher permissions to the specified topic or notifications will not be sent.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
