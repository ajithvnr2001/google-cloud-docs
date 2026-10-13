---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken
title: Memorystore v1 API - Class AuthToken (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:04.260151+00:00
---

# Memorystore v1 API - Class AuthToken (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1 API - Class AuthToken (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta09 
    
    
    public sealed class AuthToken : IMessage<AuthToken>, IEquatable<AuthToken>, IDeepCloneable<AuthToken>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1 API class AuthToken.

Auth token for the instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AuthToken

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1)

## Assembly

Google.Cloud.Memorystore.V1.dll

## Constructors 

### AuthToken()
    
    
    public AuthToken()

### AuthToken(AuthToken)
    
    
    public AuthToken(AuthToken other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken)`  
  
  
## Properties 

### AuthTokenName
    
    
    public AuthTokenName AuthTokenName { get; set; }

[AuthTokenName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthTokenName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken#Google_Cloud_Memorystore_V1_AuthToken_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AuthTokenName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthTokenName)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time of the auth token.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the auth token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public AuthToken.Types.State State { get; set; }

Output only. The state of the auth token.

**Property Value**  
---  
**Type** | **Description**  
`[AuthToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.AuthToken.Types.State)` |   
  
### Token
    
    
    public string Token { get; set; }

Output only. The auth token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
