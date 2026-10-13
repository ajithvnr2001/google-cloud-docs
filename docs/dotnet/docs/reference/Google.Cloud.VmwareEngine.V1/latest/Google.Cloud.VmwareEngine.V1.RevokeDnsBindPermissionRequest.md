---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest
title: VMware Engine v1 API - Class RevokeDnsBindPermissionRequest (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:51.763456+00:00
---

# VMware Engine v1 API - Class RevokeDnsBindPermissionRequest (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VMware Engine v1 API - Class RevokeDnsBindPermissionRequest (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.6.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.5.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.4.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.3.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.2.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.1.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.0.0/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)


    
    
    public sealed class RevokeDnsBindPermissionRequest : IMessage<RevokeDnsBindPermissionRequest>, IEquatable<RevokeDnsBindPermissionRequest>, IDeepCloneable<RevokeDnsBindPermissionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the VMware Engine v1 API class RevokeDnsBindPermissionRequest.

Request message for [VmwareEngine.RevokeDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission]

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RevokeDnsBindPermissionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VmwareEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1)

## Assembly

Google.Cloud.VmwareEngine.V1.dll

## Constructors 

### RevokeDnsBindPermissionRequest()
    
    
    public RevokeDnsBindPermissionRequest()

### RevokeDnsBindPermissionRequest(RevokeDnsBindPermissionRequest)
    
    
    public RevokeDnsBindPermissionRequest(RevokeDnsBindPermissionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest)`  
  
  
## Properties 

### DnsBindPermissionName
    
    
    public DnsBindPermissionName DnsBindPermissionName { get; set; }

[DnsBindPermissionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.DnsBindPermissionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.RevokeDnsBindPermissionRequest#Google_Cloud_VmwareEngine_V1_RevokeDnsBindPermissionRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DnsBindPermissionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.DnsBindPermissionName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Principal
    
    
    public Principal Principal { get; set; }

Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project.

**Property Value**  
---  
**Type** | **Description**  
`[Principal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.Principal)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
