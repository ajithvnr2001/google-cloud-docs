---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig
title: Vertex AI v1beta1 API - Class AuthConfig.Types.OauthConfig (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:32.308080+00:00
---

# Vertex AI v1beta1 API - Class AuthConfig.Types.OauthConfig (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AuthConfig.Types.OauthConfig (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AuthConfig.Types.OauthConfig : IMessage<AuthConfig.Types.OauthConfig>, IEquatable<AuthConfig.Types.OauthConfig>, IDeepCloneable<AuthConfig.Types.OauthConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AuthConfig.Types.OauthConfig.

Config for user oauth.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AuthConfig.Types.OauthConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types)[OauthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types)[OauthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types)[OauthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### OauthConfig()
    
    
    public OauthConfig()

### OauthConfig(OauthConfig)
    
    
    public OauthConfig(AuthConfig.Types.OauthConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types)[OauthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig)`  
  
  
## Properties 

### AccessToken
    
    
    public string AccessToken { get; set; }

Access token for extension endpoint. Only used to propagate token from [[ExecuteExtensionRequest.runtime_auth_config]] at request time.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAccessToken
    
    
    public bool HasAccessToken { get; }

Gets whether the "access_token" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasServiceAccount
    
    
    public bool HasServiceAccount { get; }

Gets whether the "service_account" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### OauthConfigCase
    
    
    public AuthConfig.Types.OauthConfig.OauthConfigOneofCase OauthConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types)[OauthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig)[OauthConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AuthConfig.Types.OauthConfig.OauthConfigOneofCase)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

The service account used to generate access tokens for executing the Extension.

  * If the service account is specified, the `iam.serviceAccounts.getAccessToken` permission should be granted to Vertex AI Extension Service Agent (<https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents>) on the provided service account.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
