---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest
title: AlloyDB v1beta API - Class CreateSecondaryInstanceRequest (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:49.106573+00:00
---

# AlloyDB v1beta API - Class CreateSecondaryInstanceRequest (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class CreateSecondaryInstanceRequest (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class CreateSecondaryInstanceRequest : IMessage<CreateSecondaryInstanceRequest>, IEquatable<CreateSecondaryInstanceRequest>, IDeepCloneable<CreateSecondaryInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class CreateSecondaryInstanceRequest.

Message for creating a Secondary Instance

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateSecondaryInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### CreateSecondaryInstanceRequest()
    
    
    public CreateSecondaryInstanceRequest()

### CreateSecondaryInstanceRequest(CreateSecondaryInstanceRequest)
    
    
    public CreateSecondaryInstanceRequest(CreateSecondaryInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest)`  
  
  
## Properties 

### Instance
    
    
    public Instance Instance { get; set; }

Required. The resource being created

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` |   
  
### InstanceId
    
    
    public string InstanceId { get; set; }

Required. ID of the requesting object.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsClusterName
    
    
    public ClusterName ParentAsClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest#Google_Cloud_AlloyDb_V1Beta_CreateSecondaryInstanceRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
