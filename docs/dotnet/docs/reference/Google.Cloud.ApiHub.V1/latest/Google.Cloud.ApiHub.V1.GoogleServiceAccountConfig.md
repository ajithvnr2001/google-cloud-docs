---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig
title: API hub v1 API - Class GoogleServiceAccountConfig (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:50.935479+00:00
---

# API hub v1 API - Class GoogleServiceAccountConfig (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class GoogleServiceAccountConfig (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig)


    
    
    public sealed class GoogleServiceAccountConfig : IMessage<GoogleServiceAccountConfig>, IEquatable<GoogleServiceAccountConfig>, IDeepCloneable<GoogleServiceAccountConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class GoogleServiceAccountConfig.

Config for Google service account authentication.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GoogleServiceAccountConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GoogleServiceAccountConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GoogleServiceAccountConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GoogleServiceAccountConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### GoogleServiceAccountConfig()
    
    
    public GoogleServiceAccountConfig()

### GoogleServiceAccountConfig(GoogleServiceAccountConfig)
    
    
    public GoogleServiceAccountConfig(GoogleServiceAccountConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GoogleServiceAccountConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig)`  
  
  
## Properties 

### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

Required. The service account to be used for authenticating request.

The `iam.serviceAccounts.getAccessToken` permission should be granted on this service account to the impersonator service account.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountAsServiceAccountName
    
    
    public ServiceAccountName ServiceAccountAsServiceAccountName { get; set; }

[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ServiceAccountName)-typed view over the [ServiceAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GoogleServiceAccountConfig#Google_Cloud_ApiHub_V1_GoogleServiceAccountConfig_ServiceAccount) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ServiceAccountName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
