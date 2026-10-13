---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest
title: Identity and Access Management (IAM) v3beta API - Class UpdateAccessPolicyRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:39.550722+00:00
---

# Identity and Access Management (IAM) v3beta API - Class UpdateAccessPolicyRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class UpdateAccessPolicyRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class UpdateAccessPolicyRequest : IMessage<UpdateAccessPolicyRequest>, IEquatable<UpdateAccessPolicyRequest>, IDeepCloneable<UpdateAccessPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class UpdateAccessPolicyRequest.

Request message for UpdateAccessPolicy method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateAccessPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Constructors 

### UpdateAccessPolicyRequest()
    
    
    public UpdateAccessPolicyRequest()

### UpdateAccessPolicyRequest(UpdateAccessPolicyRequest)
    
    
    public UpdateAccessPolicyRequest(UpdateAccessPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.UpdateAccessPolicyRequest)`  
  
  
## Properties 

### AccessPolicy
    
    
    public AccessPolicy AccessPolicy { get; set; }

Required. The access policy to update.

The access policy's `name` field is used to identify the policy to update.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicy)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set, validate the request and preview the update, but do not actually post it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
