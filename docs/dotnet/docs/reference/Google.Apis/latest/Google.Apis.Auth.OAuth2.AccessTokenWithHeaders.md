---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders
title: Class AccessTokenWithHeaders (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:55.908750+00:00
---

# Class AccessTokenWithHeaders (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class AccessTokenWithHeaders (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders)


    
    
    public sealed class AccessTokenWithHeaders

Represents an access token that can be used to authorize a request. The token might be accompanied by extra information that should be sent in the form of headers.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AccessTokenWithHeaders

## Inherited Members

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2)

## Assembly

Google.Apis.Auth.dll

## Constructors 

### AccessTokenWithHeaders(string, IReadOnlyDictionary<string, IReadOnlyList<string>>)
    
    
    public AccessTokenWithHeaders(string token, IReadOnlyDictionary<string, IReadOnlyList<string>> headers)

Constructs an [AccessTokenWithHeaders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.AccessTokenWithHeaders) based on a given token and headers.

**Parameters**  
---  
**Name** | **Description**  
`token` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token to build this instance for. May be null.  
`headers` | `[IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The collection of headers that may accompany the token. May be null.  
  
## Properties 

### AccessToken
    
    
    public string AccessToken { get; }

An access token that can be used to authorize a request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Headers
    
    
    public IReadOnlyDictionary<string, IReadOnlyList<string>> Headers { get; }

Extra headers, if any, that should be included in the request.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### AddHeaders(HttpRequestHeaders)
    
    
    public void AddHeaders(HttpRequestHeaders requestHeaders)

Adds the headers in this object to the given header collection.

**Parameter**  
---  
**Name** | **Description**  
`requestHeaders` | `[HttpRequestHeaders](https://learn.microsoft.com/dotnet/api/system.net.http.headers.httprequestheaders)`  
The header collection to add the headers to.  
  
### AddHeaders(HttpRequestMessage)
    
    
    public void AddHeaders(HttpRequestMessage request)

Adds the headers in this object to the given request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[HttpRequestMessage](https://learn.microsoft.com/dotnet/api/system.net.http.httprequestmessage)`  
The request to add the headers to.  
  
## Extension Method

[Utilities.ThrowIfNull<T>(T, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
