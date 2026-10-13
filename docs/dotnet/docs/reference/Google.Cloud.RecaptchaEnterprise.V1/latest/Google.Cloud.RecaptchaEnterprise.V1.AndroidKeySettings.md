---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings
title: Google Cloud reCAPTCHA Enterprise v1 API - Class AndroidKeySettings (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:35.914403+00:00
---

# Google Cloud reCAPTCHA Enterprise v1 API - Class AndroidKeySettings (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1 API - Class AndroidKeySettings (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class AndroidKeySettings : IMessage<AndroidKeySettings>, IEquatable<AndroidKeySettings>, IDeepCloneable<AndroidKeySettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1 API class AndroidKeySettings.

Settings specific to keys that can be used by Android apps.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AndroidKeySettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AndroidKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AndroidKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AndroidKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1.dll

## Constructors 

### AndroidKeySettings()
    
    
    public AndroidKeySettings()

### AndroidKeySettings(AndroidKeySettings)
    
    
    public AndroidKeySettings(AndroidKeySettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AndroidKeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AndroidKeySettings)`  
  
  
## Properties 

### AllowAllPackageNames
    
    
    public bool AllowAllPackageNames { get; set; }

Optional. If set to true, allowed_package_names are not enforced.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AllowedPackageNames
    
    
    public RepeatedField<string> AllowedPackageNames { get; }

Optional. Android package names of apps allowed to use the key. Example: 'com.companyname.appname' Each key supports a maximum of 250 package names. To use a key on more apps, set `allow_all_package_names` to true. When this is set, you are responsible for validating the package name by checking the `token_properties.android_package_name` field in each assessment response against your list of allowed package names.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SupportNonGoogleAppStoreDistribution
    
    
    public bool SupportNonGoogleAppStoreDistribution { get; set; }

Optional. Set to true for keys that are used in an Android application that is available for download in app stores in addition to the Google Play Store.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
