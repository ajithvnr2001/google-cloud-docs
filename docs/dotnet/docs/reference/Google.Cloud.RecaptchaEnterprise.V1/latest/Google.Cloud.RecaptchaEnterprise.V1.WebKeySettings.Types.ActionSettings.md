---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings
title: Google Cloud reCAPTCHA Enterprise v1 API - Class WebKeySettings.Types.ActionSettings (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:07.956214+00:00
---

# Google Cloud reCAPTCHA Enterprise v1 API - Class WebKeySettings.Types.ActionSettings (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1 API - Class WebKeySettings.Types.ActionSettings (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class WebKeySettings.Types.ActionSettings : IMessage<WebKeySettings.Types.ActionSettings>, IEquatable<WebKeySettings.Types.ActionSettings>, IDeepCloneable<WebKeySettings.Types.ActionSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1 API class WebKeySettings.Types.ActionSettings.

Per-action challenge settings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WebKeySettings.Types.ActionSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WebKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types)[ActionSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WebKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types)[ActionSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WebKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types)[ActionSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1.dll

## Constructors 

### ActionSettings()
    
    
    public ActionSettings()

### ActionSettings(ActionSettings)
    
    
    public ActionSettings(WebKeySettings.Types.ActionSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WebKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types)[ActionSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.WebKeySettings.Types.ActionSettings)`  
  
  
## Properties 

### ScoreThreshold
    
    
    public float ScoreThreshold { get; set; }

Required. A challenge is triggered if the end-user score is below that threshold. Value must be between 0 and 1 (inclusive).

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
