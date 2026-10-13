---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference
title: Cloud Security Compliance v1 API - Class CloudControlDeploymentReference (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:30.503811+00:00
---

# Cloud Security Compliance v1 API - Class CloudControlDeploymentReference (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Security Compliance v1 API - Class CloudControlDeploymentReference (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta05 (latest)  1.0.0-beta04 
    
    
    public sealed class CloudControlDeploymentReference : IMessage<CloudControlDeploymentReference>, IEquatable<CloudControlDeploymentReference>, IDeepCloneable<CloudControlDeploymentReference>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Security Compliance v1 API class CloudControlDeploymentReference.

The reference to a cloud control deployment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudControlDeploymentReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudControlDeploymentReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudControlDeploymentReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudControlDeploymentReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudSecurityCompliance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1)

## Assembly

Google.Cloud.CloudSecurityCompliance.V1.dll

## Constructors 

### CloudControlDeploymentReference()
    
    
    public CloudControlDeploymentReference()

### CloudControlDeploymentReference(CloudControlDeploymentReference)
    
    
    public CloudControlDeploymentReference(CloudControlDeploymentReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudControlDeploymentReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference)`  
  
  
## Properties 

### CloudControlDeployment
    
    
    public string CloudControlDeployment { get; set; }

Output only. The name of the CloudControlDeployment. The format is `organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}` or `projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}`. The only supported location is `global`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CloudControlDeploymentAsCloudControlDeploymentName
    
    
    public CloudControlDeploymentName CloudControlDeploymentAsCloudControlDeploymentName { get; set; }

[CloudControlDeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentName)-typed view over the [CloudControlDeployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentReference#Google_Cloud_CloudSecurityCompliance_V1_CloudControlDeploymentReference_CloudControlDeployment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CloudControlDeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudSecurityCompliance.V1/latest/Google.Cloud.CloudSecurityCompliance.V1.CloudControlDeploymentName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
