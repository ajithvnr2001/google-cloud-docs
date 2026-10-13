---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest
title: Anthos Multi-Cloud v1 API - Class UpdateAttachedClusterRequest (2.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:45.307969+00:00
---

# Anthos Multi-Cloud v1 API - Class UpdateAttachedClusterRequest (2.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Anthos Multi-Cloud v1 API - Class UpdateAttachedClusterRequest (2.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 
    
    
    public sealed class UpdateAttachedClusterRequest : IMessage<UpdateAttachedClusterRequest>, IEquatable<UpdateAttachedClusterRequest>, IDeepCloneable<UpdateAttachedClusterRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Anthos Multi-Cloud v1 API class UpdateAttachedClusterRequest.

Request message for `AttachedClusters.UpdateAttachedCluster` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateAttachedClusterRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeMultiCloud.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1)

## Assembly

Google.Cloud.GkeMultiCloud.V1.dll

## Constructors 

### UpdateAttachedClusterRequest()
    
    
    public UpdateAttachedClusterRequest()

### UpdateAttachedClusterRequest(UpdateAttachedClusterRequest)
    
    
    public UpdateAttachedClusterRequest(UpdateAttachedClusterRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.UpdateAttachedClusterRequest)`  
  
  
## Properties 

### AttachedCluster
    
    
    public AttachedCluster AttachedCluster { get; set; }

Required. The [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster] resource to update.

**Property Value**  
---  
**Type** | **Description**  
`[AttachedCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AttachedCluster)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field can only include these fields from [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]:

  * `annotations`.
  * `authorization.admin_groups`.
  * `authorization.admin_users`.
  * `binary_authorization.evaluation_mode`.
  * `description`.
  * `logging_config.component_config.enable_components`.
  * `monitoring_config.managed_prometheus_config.enabled`.
  * `platform_version`.
  * `proxy_config.kubernetes_secret.name`.
  * `proxy_config.kubernetes_secret.namespace`.
  * `security_posture_config.vulnerability_mode`
  * `monitoring_config.cloud_monitoring_config.enabled`



**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If set, only validate the request, but do not actually update the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
