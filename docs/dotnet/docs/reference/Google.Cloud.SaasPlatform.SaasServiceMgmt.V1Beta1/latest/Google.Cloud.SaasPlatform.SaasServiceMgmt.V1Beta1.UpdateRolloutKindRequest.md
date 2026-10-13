---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest
title: SaaS Runtime v1beta1 API - Class UpdateRolloutKindRequest (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:37.964771+00:00
---

# SaaS Runtime v1beta1 API - Class UpdateRolloutKindRequest (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  SaaS Runtime v1beta1 API - Class UpdateRolloutKindRequest (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class UpdateRolloutKindRequest : IMessage<UpdateRolloutKindRequest>, IEquatable<UpdateRolloutKindRequest>, IDeepCloneable<UpdateRolloutKindRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the SaaS Runtime v1beta1 API class UpdateRolloutKindRequest.

The request structure for the UpdateRolloutKind method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateRolloutKindRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateRolloutKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateRolloutKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateRolloutKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1)

## Assembly

Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.dll

## Constructors 

### UpdateRolloutKindRequest()
    
    
    public UpdateRolloutKindRequest()

### UpdateRolloutKindRequest(UpdateRolloutKindRequest)
    
    
    public UpdateRolloutKindRequest(UpdateRolloutKindRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateRolloutKindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.UpdateRolloutKindRequest)`  
  
  
## Properties 

### RequestId
    
    
    public string RequestId { get; set; }

An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RolloutKind
    
    
    public RolloutKind RolloutKind { get; set; }

Required. The desired state for the rollout kind.

**Property Value**  
---  
**Type** | **Description**  
`[RolloutKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.RolloutKind)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Field mask is used to specify the fields to be overwritten in the RolloutKind resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.

If the user does not provide a mask then all fields in the RolloutKind will be overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
