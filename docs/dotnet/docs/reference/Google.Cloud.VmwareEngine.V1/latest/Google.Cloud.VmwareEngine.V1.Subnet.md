---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet
title: VMware Engine v1 API - Class Subnet (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:31.938943+00:00
---

# VMware Engine v1 API - Class Subnet (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VMware Engine v1 API - Class Subnet (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.6.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.5.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.4.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.3.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.2.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.1.0/Google.Cloud.VmwareEngine.V1.Subnet)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.0.0/Google.Cloud.VmwareEngine.V1.Subnet)


    
    
    public sealed class Subnet : IMessage<Subnet>, IEquatable<Subnet>, IDeepCloneable<Subnet>, IBufferMessage, IMessage

Reference documentation and code samples for the VMware Engine v1 API class Subnet.

Subnet in a private cloud. Either `management` subnets (such as vMotion) that are read-only, or `userDefined`, which can also be updated.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Subnet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Subnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Subnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Subnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VmwareEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1)

## Assembly

Google.Cloud.VmwareEngine.V1.dll

## Constructors 

### Subnet()
    
    
    public Subnet()

### Subnet(Subnet)
    
    
    public Subnet(Subnet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Subnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet)`  
  
  
## Properties 

### GatewayIp
    
    
    public string GatewayIp { get; set; }

The IP address of the gateway of this subnet. Must fall within the IP prefix defined above.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IpCidrRange
    
    
    public string IpCidrRange { get; set; }

The IP address range of the subnet in CIDR format '10.0.0.0/24'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name of this subnet. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public Subnet.Types.State State { get; set; }

Output only. The state of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet.Types.State)` |   
  
### SubnetName
    
    
    public SubnetName SubnetName { get; set; }

[SubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.SubnetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Subnet#Google_Cloud_VmwareEngine_V1_Subnet_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SubnetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.SubnetName)` |   
  
### Type
    
    
    public string Type { get; set; }

Output only. The type of the subnet. For example "management" or "userDefined".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VlanId
    
    
    public int VlanId { get; set; }

Output only. VLAN ID of the VLAN on which the subnet is configured

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
