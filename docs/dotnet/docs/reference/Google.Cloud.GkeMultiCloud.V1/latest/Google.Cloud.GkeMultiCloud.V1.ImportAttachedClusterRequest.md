---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest
title: Anthos Multi-Cloud v1 API - Class ImportAttachedClusterRequest (2.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:14.934841+00:00
---

# Anthos Multi-Cloud v1 API - Class ImportAttachedClusterRequest (2.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Anthos Multi-Cloud v1 API - Class ImportAttachedClusterRequest (2.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.0 (latest)  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0-beta01 
    
    
    public sealed class ImportAttachedClusterRequest : IMessage<ImportAttachedClusterRequest>, IEquatable<ImportAttachedClusterRequest>, IDeepCloneable<ImportAttachedClusterRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Anthos Multi-Cloud v1 API class ImportAttachedClusterRequest.

Request message for `AttachedClusters.ImportAttachedCluster` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportAttachedClusterRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeMultiCloud.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1)

## Assembly

Google.Cloud.GkeMultiCloud.V1.dll

## Constructors 

### ImportAttachedClusterRequest()
    
    
    public ImportAttachedClusterRequest()

### ImportAttachedClusterRequest(ImportAttachedClusterRequest)
    
    
    public ImportAttachedClusterRequest(ImportAttachedClusterRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportAttachedClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest)`  
  
  
## Properties 

### Distribution
    
    
    public string Distribution { get; set; }

Required. The Kubernetes distribution of the underlying attached cluster.

Supported values: ["eks", "aks", "generic"].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FleetMembership
    
    
    public string FleetMembership { get; set; }

Required. The name of the fleet membership resource to import.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent location where this [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster] resource will be created.

Location names are formatted as `projects/<project-id>/locations/<region>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.ImportAttachedClusterRequest#Google_Cloud_GkeMultiCloud_V1_ImportAttachedClusterRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### PlatformVersion
    
    
    public string PlatformVersion { get; set; }

Required. The platform version for the cluster (e.g. `1.19.0-gke.1000`).

You can list all supported versions on a given Google Cloud region by calling [GetAttachedServerConfig][google.cloud.gkemulticloud.v1.AttachedClusters.GetAttachedServerConfig].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProxyConfig
    
    
    public AttachedProxyConfig ProxyConfig { get; set; }

Optional. Proxy configuration for outbound HTTP(S) traffic.

**Property Value**  
---  
**Type** | **Description**  
`[AttachedProxyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeMultiCloud.V1/latest/Google.Cloud.GkeMultiCloud.V1.AttachedProxyConfig)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If set, only validate the request, but do not actually import the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
