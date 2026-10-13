---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse
title: Telco Automation v1 API - Class ComputeDeploymentStatusResponse (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:37.463327+00:00
---

# Telco Automation v1 API - Class ComputeDeploymentStatusResponse (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Telco Automation v1 API - Class ComputeDeploymentStatusResponse (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/1.2.0/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/1.1.0/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/1.0.0/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse)


    
    
    public sealed class ComputeDeploymentStatusResponse : IMessage<ComputeDeploymentStatusResponse>, IEquatable<ComputeDeploymentStatusResponse>, IDeepCloneable<ComputeDeploymentStatusResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Telco Automation v1 API class ComputeDeploymentStatusResponse.

Response object for `ComputeDeploymentStatus`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComputeDeploymentStatusResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TelcoAutomation.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1)

## Assembly

Google.Cloud.TelcoAutomation.V1.dll

## Constructors 

### ComputeDeploymentStatusResponse()
    
    
    public ComputeDeploymentStatusResponse()

### ComputeDeploymentStatusResponse(ComputeDeploymentStatusResponse)
    
    
    public ComputeDeploymentStatusResponse(ComputeDeploymentStatusResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ComputeDeploymentStatusResponse)`  
  
  
## Properties 

### AggregatedStatus
    
    
    public Status AggregatedStatus { get; set; }

Output only. Aggregated status of a deployment.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.Status)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the deployment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceStatuses
    
    
    public RepeatedField<ResourceStatus> ResourceStatuses { get; }

Output only. Resource level status details in deployments.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ResourceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TelcoAutomation.V1/latest/Google.Cloud.TelcoAutomation.V1.ResourceStatus)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
