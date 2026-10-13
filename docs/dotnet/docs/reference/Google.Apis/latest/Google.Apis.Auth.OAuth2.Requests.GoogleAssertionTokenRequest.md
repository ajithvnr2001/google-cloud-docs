---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest
title: Class GoogleAssertionTokenRequest (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:56.704916+00:00
---

# Class GoogleAssertionTokenRequest (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class GoogleAssertionTokenRequest (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Auth.OAuth2.Requests.GoogleAssertionTokenRequest)


    
    
    public class GoogleAssertionTokenRequest : TokenRequest

Service account assertion token request as specified in <https://developers.google.com/accounts/docs/OAuth2ServiceAccount#makingrequest>.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [TokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequest) > GoogleAssertionTokenRequest

## Inherited Members

[TokenRequest.Scope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequest#Google_Apis_Auth_OAuth2_Requests_TokenRequest_Scope)

[TokenRequest.GrantType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequest#Google_Apis_Auth_OAuth2_Requests_TokenRequest_GrantType)

[TokenRequest.ClientId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequest#Google_Apis_Auth_OAuth2_Requests_TokenRequest_ClientId)

[TokenRequest.ClientSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequest#Google_Apis_Auth_OAuth2_Requests_TokenRequest_ClientSecret)

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Apis.Auth.OAuth2.Requests](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests)

## Assembly

Google.Apis.Auth.dll

## Constructors 

### GoogleAssertionTokenRequest()
    
    
    public GoogleAssertionTokenRequest()

Constructs a new refresh code token request and sets grant_type to `urn:ietf:params:oauth:grant-type:jwt-bearer`.

## Properties 

### Assertion
    
    
    [RequestParameter("assertion")]
    public string Assertion { get; set; }

Gets or sets the JWT (including signature).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Extension Methods

[Utilities.ThrowIfNull<T>(T, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

[TokenRequestExtenstions.ExecuteAsync(TokenRequest, HttpClient, string, CancellationToken, IClock)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.Requests.TokenRequestExtenstions#Google_Apis_Auth_OAuth2_Requests_TokenRequestExtenstions_ExecuteAsync_Google_Apis_Auth_OAuth2_Requests_TokenRequest_System_Net_Http_HttpClient_System_String_System_Threading_CancellationToken_Google_Apis_Util_IClock_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
