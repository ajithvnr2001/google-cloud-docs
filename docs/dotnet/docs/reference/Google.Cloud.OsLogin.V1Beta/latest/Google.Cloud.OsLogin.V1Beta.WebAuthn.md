---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn
title: Google Cloud OS Login v1beta API - Class WebAuthn (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:38.223765+00:00
---

# Google Cloud OS Login v1beta API - Class WebAuthn (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Login v1beta API - Class WebAuthn (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/3.0.0-beta09/Google.Cloud.OsLogin.V1Beta.WebAuthn)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/2.0.0-beta05/Google.Cloud.OsLogin.V1Beta.WebAuthn)


    
    
    public sealed class WebAuthn : IMessage<WebAuthn>, IEquatable<WebAuthn>, IDeepCloneable<WebAuthn>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud OS Login v1beta API class WebAuthn.

Security key information specific to the Web Authentication protocol.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WebAuthn

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WebAuthn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WebAuthn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WebAuthn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OsLogin.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta)

## Assembly

Google.Cloud.OsLogin.V1Beta.dll

## Constructors 

### WebAuthn()
    
    
    public WebAuthn()

### WebAuthn(WebAuthn)
    
    
    public WebAuthn(WebAuthn other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WebAuthn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.WebAuthn)`  
  
  
## Properties 

### RpId
    
    
    public string RpId { get; set; }

Relying party ID for Web Authentication.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
