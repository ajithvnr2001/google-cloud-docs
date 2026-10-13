---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata
title: Infrastructure Manager v1 API - Class ProvisionDeploymentGroupOperationMetadata (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:17.882427+00:00
---

# Infrastructure Manager v1 API - Class ProvisionDeploymentGroupOperationMetadata (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class ProvisionDeploymentGroupOperationMetadata (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ProvisionDeploymentGroupOperationMetadata : IMessage<ProvisionDeploymentGroupOperationMetadata>, IEquatable<ProvisionDeploymentGroupOperationMetadata>, IDeepCloneable<ProvisionDeploymentGroupOperationMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Infrastructure Manager v1 API class ProvisionDeploymentGroupOperationMetadata.

Operation metadata for `ProvisionDeploymentGroup` and `DeprovisionDeploymentGroup` long-running operations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProvisionDeploymentGroupOperationMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### ProvisionDeploymentGroupOperationMetadata()
    
    
    public ProvisionDeploymentGroupOperationMetadata()

### ProvisionDeploymentGroupOperationMetadata(ProvisionDeploymentGroupOperationMetadata)
    
    
    public ProvisionDeploymentGroupOperationMetadata(ProvisionDeploymentGroupOperationMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata)`  
  
  
## Properties 

### DeploymentUnitProgresses
    
    
    public RepeatedField<DeploymentUnitProgress> DeploymentUnitProgresses { get; }

Output only. Progress information for each deployment unit within the operation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DeploymentUnitProgress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentUnitProgress)` |   
  
### Step
    
    
    public ProvisionDeploymentGroupOperationMetadata.Types.ProvisionDeploymentGroupStep Step { get; set; }

Output only. The current step of the deployment group operation.

**Property Value**  
---  
**Type** | **Description**  
`[ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata.Types)[ProvisionDeploymentGroupStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProvisionDeploymentGroupOperationMetadata.Types.ProvisionDeploymentGroupStep)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
