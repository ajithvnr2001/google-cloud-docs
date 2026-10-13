---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse
title: Parameter Manager v1 API - Class RenderParameterVersionResponse (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:07.126123+00:00
---

# Parameter Manager v1 API - Class RenderParameterVersionResponse (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Parameter Manager v1 API - Class RenderParameterVersionResponse (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class RenderParameterVersionResponse : IMessage<RenderParameterVersionResponse>, IEquatable<RenderParameterVersionResponse>, IDeepCloneable<RenderParameterVersionResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Parameter Manager v1 API class RenderParameterVersionResponse.

Message describing RenderParameterVersionResponse resource

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RenderParameterVersionResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1)

## Assembly

Google.Cloud.ParameterManager.V1.dll

## Constructors 

### RenderParameterVersionResponse()
    
    
    public RenderParameterVersionResponse()

### RenderParameterVersionResponse(RenderParameterVersionResponse)
    
    
    public RenderParameterVersionResponse(RenderParameterVersionResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse)`  
  
  
## Properties 

### ParameterVersion
    
    
    public string ParameterVersion { get; set; }

Output only. Resource identifier of a ParameterVersion in the format `projects/*/locations/*/parameters/*/versions/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParameterVersionAsParameterVersionName
    
    
    public ParameterVersionName ParameterVersionAsParameterVersionName { get; set; }

[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)-typed view over the [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse#Google_Cloud_ParameterManager_V1_RenderParameterVersionResponse_ParameterVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)` |   
  
### Payload
    
    
    public ParameterVersionPayload Payload { get; set; }

Payload content of a ParameterVersion resource.

**Property Value**  
---  
**Type** | **Description**  
`[ParameterVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionPayload)` |   
  
### RenderedPayload
    
    
    public ByteString RenderedPayload { get; set; }

Output only. Server generated rendered version of the user provided payload data (ParameterVersionPayload) which has substitutions of all (if any) references to a SecretManager SecretVersion resources. This substitution only works for a Parameter which is in JSON or YAML format.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
