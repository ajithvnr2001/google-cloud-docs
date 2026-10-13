---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy
title: Network Services v1 API - Class ServiceLbPolicy (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:30.930326+00:00
---

# Network Services v1 API - Class ServiceLbPolicy (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1 API - Class ServiceLbPolicy (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ServiceLbPolicy : IMessage<ServiceLbPolicy>, IEquatable<ServiceLbPolicy>, IDeepCloneable<ServiceLbPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1 API class ServiceLbPolicy.

ServiceLbPolicy holds global load balancing and traffic distribution configuration that can be applied to a BackendService.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceLbPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1)

## Assembly

Google.Cloud.NetworkServices.V1.dll

## Constructors 

### ServiceLbPolicy()
    
    
    public ServiceLbPolicy()

### ServiceLbPolicy(ServiceLbPolicy)
    
    
    public ServiceLbPolicy(ServiceLbPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy)`  
  
  
## Properties 

### AutoCapacityDrain
    
    
    public ServiceLbPolicy.Types.AutoCapacityDrain AutoCapacityDrain { get; set; }

Optional. Configuration to automatically move traffic away for unhealthy IG/NEG for the associated Backend Service.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types)[AutoCapacityDrain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types.AutoCapacityDrain)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The timestamp when this resource was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. A free-text description of the resource. Max length 1024 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FailoverConfig
    
    
    public ServiceLbPolicy.Types.FailoverConfig FailoverConfig { get; set; }

Optional. Configuration related to health based failover.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types)[FailoverConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types.FailoverConfig)` |   
  
### IsolationConfig
    
    
    public ServiceLbPolicy.Types.IsolationConfig IsolationConfig { get; set; }

Optional. Configuration to provide isolation support for the associated Backend Service.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types)[IsolationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types.IsolationConfig)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Set of label tags associated with the ServiceLbPolicy resource.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LoadBalancingAlgorithm
    
    
    public ServiceLbPolicy.Types.LoadBalancingAlgorithm LoadBalancingAlgorithm { get; set; }

Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types)[LoadBalancingAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy.Types.LoadBalancingAlgorithm)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the ServiceLbPolicy resource. It matches pattern `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceLbPolicyName
    
    
    public ServiceLbPolicyName ServiceLbPolicyName { get; set; }

[ServiceLbPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicy#Google_Cloud_NetworkServices_V1_ServiceLbPolicy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceLbPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ServiceLbPolicyName)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The timestamp when this resource was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
