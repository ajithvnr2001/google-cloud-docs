---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot
title: Google Cloud reCAPTCHA Enterprise v1 API - Class Bot (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:42.251258+00:00
---

# Google Cloud reCAPTCHA Enterprise v1 API - Class Bot (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1 API - Class Bot (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class Bot : IMessage<Bot>, IEquatable<Bot>, IDeepCloneable<Bot>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1 API class Bot.

Bot information and metadata.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Bot

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Bot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Bot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Bot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1.dll

## Constructors 

### Bot()
    
    
    public Bot()

### Bot(Bot)
    
    
    public Bot(Bot other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Bot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot)`  
  
  
## Properties 

### BotType
    
    
    public Bot.Types.BotType BotType { get; set; }

Optional. Enumerated field representing the type of bot.

**Property Value**  
---  
**Type** | **Description**  
`[Bot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot.Types)[BotType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Bot.Types.BotType)` |   
  
### Name
    
    
    public string Name { get; set; }

Optional. Enumerated string value that indicates the identity of the bot, formatted in kebab-case. Current example values include the following:

  * google-agent - AI_AGENT
  * browser-base - AI_AGENT
  * chat-gpt - AI_AGENT
  * aws-bedrock - AI_AGENT
  * cybaa-bot - AI_AGENT
  * cloudflare - AI_AGENT
  * payhawk - AI_AGENT
  * duck-duck-go - SEARCH_INDEXER
  * mediaboard - CONTENT_SCRAPER
  * marker-io - AI_AGENT
  * broadcom - AI_AGENT
  * anchor-browser - AI_AGENT
  * shopify - AI_AGENT
  * stackscope - CONTENT_SCRAPER
  * manus - AI_AGENT
  * kernel-sh - AI_AGENT
  * zvelo - SEARCH_INDEXER



Ensure that your applications can handle identifier values not explicitly listed here. Deprecated values might take some time to stop showing up in responses. New values can be pushed so this list should be taken as non exhaustive.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
