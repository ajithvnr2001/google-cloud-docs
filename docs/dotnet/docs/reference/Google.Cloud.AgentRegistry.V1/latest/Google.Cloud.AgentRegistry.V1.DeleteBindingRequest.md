---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest
title: Agent Registry v1 API - Class DeleteBindingRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:48.565988+00:00
---

# Agent Registry v1 API - Class DeleteBindingRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Agent Registry v1 API - Class DeleteBindingRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class DeleteBindingRequest : IMessage<DeleteBindingRequest>, IEquatable<DeleteBindingRequest>, IDeepCloneable<DeleteBindingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Agent Registry v1 API class DeleteBindingRequest.

Message for deleting a Binding

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteBindingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AgentRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1)

## Assembly

Google.Cloud.AgentRegistry.V1.dll

## Constructors 

### DeleteBindingRequest()
    
    
    public DeleteBindingRequest()

### DeleteBindingRequest(DeleteBindingRequest)
    
    
    public DeleteBindingRequest(DeleteBindingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest)`  
  
  
## Properties 

### BindingName
    
    
    public BindingName BindingName { get; set; }

[BindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.BindingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.DeleteBindingRequest#Google_Cloud_AgentRegistry_V1_DeleteBindingRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.BindingName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
