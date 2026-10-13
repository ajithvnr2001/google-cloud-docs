---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig
title: Gemini Enterprise for Customer Experience v1 API - Class OmnichannelIntegrationConfig.Types.WhatsappConfig (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:12.474156+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class OmnichannelIntegrationConfig.Types.WhatsappConfig (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class OmnichannelIntegrationConfig.Types.WhatsappConfig (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class OmnichannelIntegrationConfig.Types.WhatsappConfig : IMessage<OmnichannelIntegrationConfig.Types.WhatsappConfig>, IEquatable<OmnichannelIntegrationConfig.Types.WhatsappConfig>, IDeepCloneable<OmnichannelIntegrationConfig.Types.WhatsappConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class OmnichannelIntegrationConfig.Types.WhatsappConfig.

How Omnichannel should receive/reply events from WhatsApp.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OmnichannelIntegrationConfig.Types.WhatsappConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OmnichannelIntegrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types)[WhatsappConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OmnichannelIntegrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types)[WhatsappConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OmnichannelIntegrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types)[WhatsappConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### WhatsappConfig()
    
    
    public WhatsappConfig()

### WhatsappConfig(WhatsappConfig)
    
    
    public WhatsappConfig(OmnichannelIntegrationConfig.Types.WhatsappConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OmnichannelIntegrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types)[WhatsappConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.OmnichannelIntegrationConfig.Types.WhatsappConfig)`  
  
  
## Properties 

### MetaBusinessPortfolioId
    
    
    public string MetaBusinessPortfolioId { get; set; }

The Meta Business Portfolio (MBP) ID. <https://www.facebook.com/business/help/1710077379203657>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PhoneNumber
    
    
    public string PhoneNumber { get; set; }

The phone number used for sending/receiving messages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PhoneNumberId
    
    
    public string PhoneNumberId { get; set; }

The Phone Number ID associated with the WhatsApp Business Account.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WebhookVerifyToken
    
    
    public string WebhookVerifyToken { get; set; }

The verify token configured in the Meta App Dashboard for webhook verification.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WhatsappBusinessAccountId
    
    
    public string WhatsappBusinessAccountId { get; set; }

The customer's WhatsApp Business Account (WABA) ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WhatsappBusinessToken
    
    
    public string WhatsappBusinessToken { get; set; }

The access token for authenticating API calls to the WhatsApp Cloud API. <https://developers.facebook.com/docs/whatsapp/business-management-api/get-started/#business-integration-system-user-access-tokens>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
