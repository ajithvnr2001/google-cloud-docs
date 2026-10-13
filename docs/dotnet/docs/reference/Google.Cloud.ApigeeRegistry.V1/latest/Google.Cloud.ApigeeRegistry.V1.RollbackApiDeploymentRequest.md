---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest
title: Apigee Registry v1 API - Class RollbackApiDeploymentRequest (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:20.997177+00:00
---

# Apigee Registry v1 API - Class RollbackApiDeploymentRequest (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Apigee Registry v1 API - Class RollbackApiDeploymentRequest (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class RollbackApiDeploymentRequest : IMessage<RollbackApiDeploymentRequest>, IEquatable<RollbackApiDeploymentRequest>, IDeepCloneable<RollbackApiDeploymentRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Apigee Registry v1 API class RollbackApiDeploymentRequest.

Request message for RollbackApiDeployment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RollbackApiDeploymentRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RollbackApiDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RollbackApiDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RollbackApiDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApigeeRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1)

## Assembly

Google.Cloud.ApigeeRegistry.V1.dll

## Constructors 

### RollbackApiDeploymentRequest()
    
    
    public RollbackApiDeploymentRequest()

### RollbackApiDeploymentRequest(RollbackApiDeploymentRequest)
    
    
    public RollbackApiDeploymentRequest(RollbackApiDeploymentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RollbackApiDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest)`  
  
  
## Properties 

### ApiDeploymentName
    
    
    public ApiDeploymentName ApiDeploymentName { get; set; }

[ApiDeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.ApiDeploymentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.RollbackApiDeploymentRequest#Google_Cloud_ApigeeRegistry_V1_RollbackApiDeploymentRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ApiDeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeRegistry.V1/latest/Google.Cloud.ApigeeRegistry.V1.ApiDeploymentName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The deployment being rolled back.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RevisionId
    
    
    public string RevisionId { get; set; }

Required. The revision ID to roll back to. It must be a revision of the same deployment.

Example: `c7cfa2a8`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
