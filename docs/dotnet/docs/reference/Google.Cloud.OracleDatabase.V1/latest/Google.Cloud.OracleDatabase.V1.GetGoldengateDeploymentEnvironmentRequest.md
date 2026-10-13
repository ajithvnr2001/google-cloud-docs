---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest
title: Oracle Database@Google Cloud v1 API - Class GetGoldengateDeploymentEnvironmentRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:30.874038+00:00
---

# Oracle Database@Google Cloud v1 API - Class GetGoldengateDeploymentEnvironmentRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class GetGoldengateDeploymentEnvironmentRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GetGoldengateDeploymentEnvironmentRequest : IMessage<GetGoldengateDeploymentEnvironmentRequest>, IEquatable<GetGoldengateDeploymentEnvironmentRequest>, IDeepCloneable<GetGoldengateDeploymentEnvironmentRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class GetGoldengateDeploymentEnvironmentRequest.

Message for getting a GoldengateDeploymentEnvironment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetGoldengateDeploymentEnvironmentRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetGoldengateDeploymentEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetGoldengateDeploymentEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetGoldengateDeploymentEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### GetGoldengateDeploymentEnvironmentRequest()
    
    
    public GetGoldengateDeploymentEnvironmentRequest()

### GetGoldengateDeploymentEnvironmentRequest(GetGoldengateDeploymentEnvironmentRequest)
    
    
    public GetGoldengateDeploymentEnvironmentRequest(GetGoldengateDeploymentEnvironmentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetGoldengateDeploymentEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest)`  
  
  
## Properties 

### GoldengateDeploymentEnvironmentName
    
    
    public GoldengateDeploymentEnvironmentName GoldengateDeploymentEnvironmentName { get; set; }

[GoldengateDeploymentEnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironmentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GetGoldengateDeploymentEnvironmentRequest#Google_Cloud_OracleDatabase_V1_GetGoldengateDeploymentEnvironmentRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[GoldengateDeploymentEnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironmentName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Name of the resource with the format: projects/{project}/locations/{location}/goldengateDeploymentEnvironments/{goldengate_deployment_environment}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
