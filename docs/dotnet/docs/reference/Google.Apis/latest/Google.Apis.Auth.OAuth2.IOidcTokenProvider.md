---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.IOidcTokenProvider
title: Interface IOidcTokenProvider (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:17.248711+00:00
---

# Interface IOidcTokenProvider (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.IOidcTokenProvider

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Interface IOidcTokenProvider (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Auth.OAuth2.IOidcTokenProvider)


    
    
    public interface IOidcTokenProvider

Represents an OIDC token provider.

## Namespace

[Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2)

## Assembly

Google.Apis.Auth.dll

## Methods 

### GetOidcTokenAsync(OidcTokenOptions, CancellationToken)
    
    
    Task<OidcToken> GetOidcTokenAsync(OidcTokenOptions options, CancellationToken cancellationToken = default)

Returns an OIDC token for the given options.

**Parameters**  
---  
**Name** | **Description**  
`options` | `[OidcTokenOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcTokenOptions)`  
The options to create the token from.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The cancellation token that may be used to cancel the request.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OidcToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcToken)` | The OIDC token.  
  
## Extension Method

[Utilities.ThrowIfNull<T>(T, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
