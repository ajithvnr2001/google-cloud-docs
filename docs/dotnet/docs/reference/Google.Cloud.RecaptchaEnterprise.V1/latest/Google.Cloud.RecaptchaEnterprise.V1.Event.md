---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event
title: Google Cloud reCAPTCHA Enterprise v1 API - Class Event (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:23.826895+00:00
---

# Google Cloud reCAPTCHA Enterprise v1 API - Class Event (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1 API - Class Event (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class Event : IMessage<Event>, IEquatable<Event>, IDeepCloneable<Event>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1 API class Event.

The event being assessed.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Event

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1.dll

## Constructors 

### Event()
    
    
    public Event()

### Event(Event)
    
    
    public Event(Event other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event)`  
  
  
## Properties 

### ExpectedAction
    
    
    public string ExpectedAction { get; set; }

Optional. The expected action for this type of event. This should be the same action provided at token generation time on client-side platforms already integrated with recaptcha enterprise. Required for Universal keys.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Express
    
    
    public bool Express { get; set; }

Optional. Flag for a reCAPTCHA express request for an assessment without a token. If enabled, `site_key` must reference an Express site key.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### FirewallPolicyEvaluation
    
    
    public bool FirewallPolicyEvaluation { get; set; }

Optional. Flag for enabling firewall policy config assessment. If this flag is enabled, the firewall policy is evaluated and a suggested firewall action is returned in the response.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### FraudPrevention
    
    
    public Event.Types.FraudPrevention FraudPrevention { get; set; }

Optional. The Fraud Prevention setting for this assessment.

**Property Value**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event.Types)[FraudPrevention](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.Event.Types.FraudPrevention)` |   
  
### HashedAccountId
    
    
    [Obsolete]
    public ByteString HashedAccountId { get; set; }

Optional. Deprecated: use `user_info.account_id` instead. Unique stable hashed user identifier for the request. The identifier must be hashed using hmac-sha256 with stable secret.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### Headers
    
    
    public RepeatedField<string> Headers { get; }

Optional. HTTP header information about the request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Ja3
    
    
    public string Ja3 { get; set; }

Optional. JA3 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/salesforce/ja3>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Ja4
    
    
    public string Ja4 { get; set; }

Optional. JA4 fingerprint for SSL clients. To learn how to compute this fingerprint, please refer to <https://github.com/FoxIO-LLC/ja4>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestedUri
    
    
    public string RequestedUri { get; set; }

Optional. The URI resource the user requested that triggered an assessment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SiteKey
    
    
    public string SiteKey { get; set; }

Optional. The site key that was used to invoke reCAPTCHA Enterprise on your site and generate the token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Token
    
    
    public string Token { get; set; }

Optional. The user response token provided by the reCAPTCHA Enterprise client-side integration on your site.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TransactionData
    
    
    public TransactionData TransactionData { get; set; }

Optional. Data describing a payment transaction to be assessed. Sending this data enables reCAPTCHA Enterprise Fraud Prevention and the FraudPreventionAssessment component in the response.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.TransactionData)` |   
  
### UserAgent
    
    
    public string UserAgent { get; set; }

Optional. The user agent present in the request from the user's device related to this event.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UserInfo
    
    
    public UserInfo UserInfo { get; set; }

Optional. Information about the user that generates this event, when they can be identified. They are often identified through the use of an account for logged-in requests or login/registration requests, or by providing user identifiers for guest actions like checkout.

**Property Value**  
---  
**Type** | **Description**  
`[UserInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.UserInfo)` |   
  
### UserIpAddress
    
    
    public string UserIpAddress { get; set; }

Optional. The IP address in the request from the user's device related to this event.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WafTokenAssessment
    
    
    public bool WafTokenAssessment { get; set; }

Optional. Flag for running Web Application Firewall (WAF) token assessment. If enabled, the token must be specified, and have been created by a WAF-enabled key.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
