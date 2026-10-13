---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings
title: Chronicle v1 API - Class CustomAPISettings (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:55.095733+00:00
---

# Chronicle v1 API - Class CustomAPISettings (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CustomAPISettings (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CustomAPISettings : IMessage<CustomAPISettings>, IEquatable<CustomAPISettings>, IDeepCloneable<CustomAPISettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CustomAPISettings.

Settings required by Feeds of Custom API (Codeless). Supports fetching data from third-party APIs with configurable pagination, authentication, and response parsing.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomAPISettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomAPISettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomAPISettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomAPISettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### CustomAPISettings()
    
    
    public CustomAPISettings()

### CustomAPISettings(CustomAPISettings)
    
    
    public CustomAPISettings(CustomAPISettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomAPISettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings)`  
  
  
## Properties 

### AuthenticationCase
    
    
    public CustomAPISettings.AuthenticationOneofCase AuthenticationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPISettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings)[AuthenticationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPISettings.AuthenticationOneofCase)` |   
  
### BaseUrl
    
    
    public string BaseUrl { get; set; }

Required. Enter the primary web address of the third-party API (e.g., <https://api.vendor.com>).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BasicAuth
    
    
    public UsernameSecretAuth BasicAuth { get; set; }

Authenticate using Username/Password credentials.

**Property Value**  
---  
**Type** | **Description**  
`[UsernameSecretAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UsernameSecretAuth)` |   
  
### HeaderAuth
    
    
    public CustomAPIHeaderAuth HeaderAuth { get; set; }

Authenticate using custom API Keys injected into request headers.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPIHeaderAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIHeaderAuth)` |   
  
### NoAuth
    
    
    public CustomAPINoAuth NoAuth { get; set; }

Authenticate without credentials or secrets.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPINoAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPINoAuth)` |   
  
### OauthClientCredentials
    
    
    public OAuthClientCredentials OauthClientCredentials { get; set; }

Authenticate using OAuth 2.0 Client Credentials Grant flow.

**Property Value**  
---  
**Type** | **Description**  
`[OAuthClientCredentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.OAuthClientCredentials)` |   
  
### PollingFrequency
    
    
    public int PollingFrequency { get; set; }

Optional. Specify how often the platform checks the API for new data in minutes (default is 15 minutes).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PrimaryRequest
    
    
    public CustomAPITransferNode PrimaryRequest { get; set; }

Required. Configure the initial API call used to fetch the main list of logs or events.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPITransferNode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPITransferNode)` |   
  
### QueryAuth
    
    
    public CustomAPIQueryAuth QueryAuth { get; set; }

Authenticate using custom API Keys injected into URL query parameters.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPIQueryAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIQueryAuth)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
