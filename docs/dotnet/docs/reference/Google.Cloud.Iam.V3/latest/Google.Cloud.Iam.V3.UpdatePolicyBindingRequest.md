---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest
title: Identity and Access Management (IAM) v3 API - Class UpdatePolicyBindingRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:34.349056+00:00
---

# Identity and Access Management (IAM) v3 API - Class UpdatePolicyBindingRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3 API - Class UpdatePolicyBindingRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class UpdatePolicyBindingRequest : IMessage<UpdatePolicyBindingRequest>, IEquatable<UpdatePolicyBindingRequest>, IDeepCloneable<UpdatePolicyBindingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3 API class UpdatePolicyBindingRequest.

Request message for UpdatePolicyBinding method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdatePolicyBindingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3)

## Assembly

Google.Cloud.Iam.V3.dll

## Constructors 

### UpdatePolicyBindingRequest()
    
    
    public UpdatePolicyBindingRequest()

### UpdatePolicyBindingRequest(UpdatePolicyBindingRequest)
    
    
    public UpdatePolicyBindingRequest(UpdatePolicyBindingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdatePolicyBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.UpdatePolicyBindingRequest)`  
  
  
## Properties 

### PolicyBinding
    
    
    public PolicyBinding PolicyBinding { get; set; }

Required. The policy binding to update.

The policy binding's `name` field is used to identify the policy binding to update.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PolicyBinding)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. The list of fields to update

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set, validate the request and preview the update, but do not actually post it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-08 UTC."],[],[]] 
