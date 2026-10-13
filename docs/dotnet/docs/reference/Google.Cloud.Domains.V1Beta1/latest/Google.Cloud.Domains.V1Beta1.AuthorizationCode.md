---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode
title: Cloud Domains v1beta1 API - Class AuthorizationCode (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:20.142405+00:00
---

# Cloud Domains v1beta1 API - Class AuthorizationCode (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1beta1 API - Class AuthorizationCode (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/2.0.0-beta05/Google.Cloud.Domains.V1Beta1.AuthorizationCode)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/1.0.0-beta04/Google.Cloud.Domains.V1Beta1.AuthorizationCode)


    
    
    public sealed class AuthorizationCode : IMessage<AuthorizationCode>, IEquatable<AuthorizationCode>, IDeepCloneable<AuthorizationCode>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1beta1 API class AuthorizationCode.

Defines an authorization code.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AuthorizationCode

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AuthorizationCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AuthorizationCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AuthorizationCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1)

## Assembly

Google.Cloud.Domains.V1Beta1.dll

## Constructors 

### AuthorizationCode()
    
    
    public AuthorizationCode()

### AuthorizationCode(AuthorizationCode)
    
    
    public AuthorizationCode(AuthorizationCode other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AuthorizationCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.AuthorizationCode)`  
  
  
## Properties 

### Code
    
    
    public string Code { get; set; }

The Authorization Code in ASCII. It can be used to transfer the domain to or from another registrar.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
