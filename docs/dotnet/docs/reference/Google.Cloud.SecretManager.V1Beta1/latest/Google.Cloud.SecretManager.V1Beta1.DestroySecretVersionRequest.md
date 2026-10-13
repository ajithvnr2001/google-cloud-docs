---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest
title: Secret Manager v1beta1 API - Class DestroySecretVersionRequest (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:27.509591+00:00
---

# Secret Manager v1beta1 API - Class DestroySecretVersionRequest (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Secret Manager v1beta1 API - Class DestroySecretVersionRequest (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/3.0.0-beta06/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/2.0.0-beta05/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest)


    
    
    public sealed class DestroySecretVersionRequest : IMessage<DestroySecretVersionRequest>, IEquatable<DestroySecretVersionRequest>, IDeepCloneable<DestroySecretVersionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Secret Manager v1beta1 API class DestroySecretVersionRequest.

Request message for [SecretManagerService.DestroySecretVersion][google.cloud.secrets.v1beta1.SecretManagerService.DestroySecretVersion].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DestroySecretVersionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DestroySecretVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DestroySecretVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DestroySecretVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecretManager.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1)

## Assembly

Google.Cloud.SecretManager.V1Beta1.dll

## Constructors 

### DestroySecretVersionRequest()
    
    
    public DestroySecretVersionRequest()

### DestroySecretVersionRequest(DestroySecretVersionRequest)
    
    
    public DestroySecretVersionRequest(DestroySecretVersionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DestroySecretVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The resource name of the [SecretVersion][google.cloud.secrets.v1beta1.SecretVersion] to destroy in the format `projects/*/secrets/*/versions/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecretVersionName
    
    
    public SecretVersionName SecretVersionName { get; set; }

[SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretVersionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.DestroySecretVersionRequest#Google_Cloud_SecretManager_V1Beta1_DestroySecretVersionRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1Beta1/latest/Google.Cloud.SecretManager.V1Beta1.SecretVersionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
