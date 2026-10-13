---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest
title: Infrastructure Manager v1 API - Class DeleteStatefileRequest (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:24.958742+00:00
---

# Infrastructure Manager v1 API - Class DeleteStatefileRequest (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class DeleteStatefileRequest (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DeleteStatefileRequest : IMessage<DeleteStatefileRequest>, IEquatable<DeleteStatefileRequest>, IDeepCloneable<DeleteStatefileRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Infrastructure Manager v1 API class DeleteStatefileRequest.

A request to delete a state file passed to a 'DeleteStatefile' call.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteStatefileRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### DeleteStatefileRequest()
    
    
    public DeleteStatefileRequest()

### DeleteStatefileRequest(DeleteStatefileRequest)
    
    
    public DeleteStatefileRequest(DeleteStatefileRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteStatefileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest)`  
  
  
## Properties 

### DeploymentName
    
    
    public DeploymentName DeploymentName { get; set; }

[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeleteStatefileRequest#Google_Cloud_Config_V1_DeleteStatefileRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentName)` |   
  
### LockId
    
    
    public long LockId { get; set; }

Required. Lock ID of the lock file to verify that the user who is deleting the state file previously locked the Deployment.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
