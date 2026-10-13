---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest
title: Secret Manager v1beta1 API - Class UpdateSecretRequest (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:39.147378+00:00
---

# Secret Manager v1beta1 API - Class UpdateSecretRequest (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Secret Manager v1beta1 API - Class UpdateSecretRequest (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/3.0.0-beta06/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/2.0.0-beta05/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest)


    
    
    public sealed class UpdateSecretRequest : IMessage<UpdateSecretRequest>, IEquatable<UpdateSecretRequest>, IDeepCloneable<UpdateSecretRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Secret Manager v1beta1 API class UpdateSecretRequest.

Request message for [SecretManagerService.UpdateSecret][google.cloud.secrets.v1beta1.SecretManagerService.UpdateSecret].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateSecretRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecretManager.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1)

## Assembly

Google.Cloud.SecretManager.V1Beta1.dll

## Constructors 

### UpdateSecretRequest()
    
    
    public UpdateSecretRequest()

### UpdateSecretRequest(UpdateSecretRequest)
    
    
    public UpdateSecretRequest(UpdateSecretRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.UpdateSecretRequest)`  
  
  
## Properties 

### Secret
    
    
    public Secret Secret { get; set; }

Required. [Secret][google.cloud.secrets.v1beta1.Secret] with updated field values.

**Property Value**  
---  
**Type** | **Description**  
`[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.Secret)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. Specifies the fields to be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
