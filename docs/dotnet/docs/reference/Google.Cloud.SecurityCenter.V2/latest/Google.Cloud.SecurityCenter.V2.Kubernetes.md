---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes
title: Security Command Center v2 API - Class Kubernetes (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:29.014206+00:00
---

# Security Command Center v2 API - Class Kubernetes (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class Kubernetes (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Kubernetes : IMessage<Kubernetes>, IEquatable<Kubernetes>, IDeepCloneable<Kubernetes>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class Kubernetes.

Kubernetes-related attributes.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Kubernetes

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### Kubernetes()
    
    
    public Kubernetes()

### Kubernetes(Kubernetes)
    
    
    public Kubernetes(Kubernetes other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)`  
  
  
## Properties 

### AccessReviews
    
    
    public RepeatedField<Kubernetes.Types.AccessReview> AccessReviews { get; }

Provides information on any Kubernetes access reviews (privilege checks) relevant to the finding.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[AccessReview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.AccessReview)` |   
  
### Bindings
    
    
    public RepeatedField<Kubernetes.Types.Binding> Bindings { get; }

Provides Kubernetes role binding information for findings that involve [RoleBindings or ClusterRoleBindings](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.Binding)` |   
  
### NodePools
    
    
    public RepeatedField<Kubernetes.Types.NodePool> NodePools { get; }

GKE [node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) associated with the finding. This field contains node pool information for each node, when it is available.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[NodePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.NodePool)` |   
  
### Nodes
    
    
    public RepeatedField<Kubernetes.Types.Node> Nodes { get; }

Provides Kubernetes [node](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) information.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[Node](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.Node)` |   
  
### Objects
    
    
    public RepeatedField<Kubernetes.Types.Object> Objects { get; }

Kubernetes objects related to the finding.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[Object](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.Object)` |   
  
### Pods
    
    
    public RepeatedField<Kubernetes.Types.Pod> Pods { get; }

Kubernetes [Pods](https://cloud.google.com/kubernetes-engine/docs/concepts/pod) associated with the finding. This field contains Pod records for each container that is owned by a Pod.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[Pod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.Pod)` |   
  
### Roles
    
    
    public RepeatedField<Kubernetes.Types.Role> Roles { get; }

Provides Kubernetes role information for findings that involve [Roles or ClusterRoles](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Kubernetes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types)[Role](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.Kubernetes.Types.Role)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
