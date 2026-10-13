---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig
title: Gemini Enterprise for Customer Experience v1beta API - Class EndUserAuthConfig (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:15.344282+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class EndUserAuthConfig (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class EndUserAuthConfig (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class EndUserAuthConfig : IMessage<EndUserAuthConfig>, IEquatable<EndUserAuthConfig>, IDeepCloneable<EndUserAuthConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class EndUserAuthConfig.

End-user authentication configuration used for Connection calls. The field values must be the names of context variables in the format `$context.variables.<name_of_variable>`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EndUserAuthConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### EndUserAuthConfig()
    
    
    public EndUserAuthConfig()

### EndUserAuthConfig(EndUserAuthConfig)
    
    
    public EndUserAuthConfig(EndUserAuthConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig)`  
  
  
## Properties 

### AuthConfigCase
    
    
    public EndUserAuthConfig.AuthConfigOneofCase AuthConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig)[AuthConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.AuthConfigOneofCase)` |   
  
### Oauth2AuthCodeConfig
    
    
    public EndUserAuthConfig.Types.Oauth2AuthCodeConfig Oauth2AuthCodeConfig { get; set; }

Oauth 2.0 Authorization Code authentication.

**Property Value**  
---  
**Type** | **Description**  
`[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types)[Oauth2AuthCodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types.Oauth2AuthCodeConfig)` |   
  
### Oauth2JwtBearerConfig
    
    
    public EndUserAuthConfig.Types.Oauth2JwtBearerConfig Oauth2JwtBearerConfig { get; set; }

JWT Profile Oauth 2.0 Authorization Grant authentication.

**Property Value**  
---  
**Type** | **Description**  
`[EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types)[Oauth2JwtBearerConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types.Oauth2JwtBearerConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
