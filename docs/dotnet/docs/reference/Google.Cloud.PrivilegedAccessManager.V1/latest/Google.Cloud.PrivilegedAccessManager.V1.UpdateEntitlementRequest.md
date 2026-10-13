---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest
title: Privileged Access Manager v1 API - Class UpdateEntitlementRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:26.861179+00:00
---

# Privileged Access Manager v1 API - Class UpdateEntitlementRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Privileged Access Manager v1 API - Class UpdateEntitlementRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.1.0/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.0.0/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest)


    
    
    public sealed class UpdateEntitlementRequest : IMessage<UpdateEntitlementRequest>, IEquatable<UpdateEntitlementRequest>, IDeepCloneable<UpdateEntitlementRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Privileged Access Manager v1 API class UpdateEntitlementRequest.

Message for updating an entitlement.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateEntitlementRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PrivilegedAccessManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1)

## Assembly

Google.Cloud.PrivilegedAccessManager.V1.dll

## Constructors 

### UpdateEntitlementRequest()
    
    
    public UpdateEntitlementRequest()

### UpdateEntitlementRequest(UpdateEntitlementRequest)
    
    
    public UpdateEntitlementRequest(UpdateEntitlementRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.UpdateEntitlementRequest)`  
  
  
## Properties 

### Entitlement
    
    
    public Entitlement Entitlement { get; set; }

Required. The entitlement resource that is updated.

**Property Value**  
---  
**Type** | **Description**  
`[Entitlement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.Entitlement)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The list of fields to update. A field is overwritten if, and only if, it is in the mask. Any immutable fields set in the mask are ignored by the server. Repeated fields and map fields are only allowed in the last position of a `paths` string and overwrite the existing values. Hence an update to a repeated field or a map should contain the entire list of values. The fields specified in the update_mask are relative to the resource and not to the request. (e.g. `MaxRequestDuration`; _not_ `entitlement.MaxRequestDuration`) A value of '*' for this field refers to full replacement of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
