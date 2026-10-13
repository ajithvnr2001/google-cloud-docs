---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ImpersonatedCredential
title: Class ImpersonatedCredential (1.73.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:38.603559+00:00
---

# Class ImpersonatedCredential (1.73.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ImpersonatedCredential

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class ImpersonatedCredential (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.73.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.69.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.69.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.68.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.68.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.60.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.60.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.59.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.59.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.55.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.55.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)
  * [ 1.50.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/1.50.0/Google.Apis.Auth.OAuth2.ImpersonatedCredential)


    
    
    public sealed class ImpersonatedCredential : ServiceCredential, IHttpUnsuccessfulResponseHandler, IOidcTokenProvider, ICredential, IConfigurableHttpClientInitializer, ITokenAccessWithHeaders, ITokenAccess, IHttpExecuteInterceptor, IBlobSigner

Allows a service account or user credential to impersonate a service account. See <https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials> and <https://cloud.google.com/iam/docs/impersonating-service-accounts> for more information.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential) > ImpersonatedCredential

## Implements

[IHttpUnsuccessfulResponseHandler](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.IHttpUnsuccessfulResponseHandler), [IOidcTokenProvider](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.IOidcTokenProvider), [ICredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ICredential), [IConfigurableHttpClientInitializer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.IConfigurableHttpClientInitializer), [ITokenAccessWithHeaders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ITokenAccessWithHeaders), [ITokenAccess](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ITokenAccess), [IHttpExecuteInterceptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Http.IHttpExecuteInterceptor), [IBlobSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.IBlobSigner)

## Inherited Members

[ServiceCredential.TokenServerUrl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_TokenServerUrl)

[ServiceCredential.Clock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_Clock)

[ServiceCredential.AccessMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_AccessMethod)

[ServiceCredential.HttpClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_HttpClient)

[ServiceCredential.Scopes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_Scopes)

[ServiceCredential.Token](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_Token)

[ServiceCredential.QuotaProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_QuotaProject)

[ServiceCredential.Initialize(ConfigurableHttpClient)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_Initialize_Google_Apis_Http_ConfigurableHttpClient_)

[ServiceCredential.InterceptAsync(HttpRequestMessage, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_InterceptAsync_System_Net_Http_HttpRequestMessage_System_Threading_CancellationToken_)

[ServiceCredential.HandleResponseAsync(HandleUnsuccessfulResponseArgs)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_HandleResponseAsync_Google_Apis_Http_HandleUnsuccessfulResponseArgs_)

[ServiceCredential.GetAccessTokenForRequestAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_GetAccessTokenForRequestAsync_System_String_System_Threading_CancellationToken_)

[ServiceCredential.GetAccessTokenWithHeadersForRequestAsync(string, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_GetAccessTokenWithHeadersForRequestAsync_System_String_System_Threading_CancellationToken_)

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

## Remarks

This credential type does not validate the credential configuration. A security risk occurs when a credential configuration configured with malicious urls is used. You should validate credential configurations provided by untrusted sources. See [ Security requirements when using credential configurations from an external source ](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials) for more details.

## Properties 

### DelegateAccounts
    
    
    public IEnumerable<string> DelegateAccounts { get; }

Gets the chained list of delegate service accounts. May be empty.

**Property Value**  
---  
**Type** | **Description**  
`[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Lifetime
    
    
    public TimeSpan Lifetime { get; }

Gets the lifetime of the delegated credential. This is how long the delegated credential should be valid from the time of the first request made with this credential.

**Property Value**  
---  
**Type** | **Description**  
`[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)` |   
  
### SourceCredential
    
    
    public GoogleCredential SourceCredential { get; }

Gets the source credential used to acquire the impersonated credentials.

**Property Value**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential)` |   
  
### TargetPrincipal
    
    
    public string TargetPrincipal { get; }

Gets the service account to impersonate.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetOidcTokenAsync(OidcTokenOptions, CancellationToken)
    
    
    public Task<OidcToken> GetOidcTokenAsync(OidcTokenOptions options, CancellationToken cancellationToken = default)

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
  
### RequestAccessTokenAsync(CancellationToken)
    
    
    public override Task<bool> RequestAccessTokenAsync(CancellationToken taskCancellationToken)

Requests a new token.

**Parameter**  
---  
**Name** | **Description**  
`taskCancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
Cancellation token to cancel operation.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if a new token was received successfully.  
**Overrides**

[ServiceCredential.RequestAccessTokenAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.ServiceCredential#Google_Apis_Auth_OAuth2_ServiceCredential_RequestAccessTokenAsync_System_Threading_CancellationToken_)

### SignBlobAsync(byte[], CancellationToken)
    
    
    public Task<string> SignBlobAsync(byte[] blob, CancellationToken cancellationToken = default)

Signs the provided blob using the private key associated with the impersonated service account.

**Parameters**  
---  
**Name** | **Description**  
`blob` | `System.Byte`  
The blob to sign.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
Cancellation token to cancel operation.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` | The base64 encoded signature.  
**Exceptions**  
---  
**Type** | **Description**  
`[HttpRequestException](https://learn.microsoft.com/dotnet/api/system.net.http.httprequestexception)` | When signing request fails.  
`Newtonsoft.Json.JsonException` | When signing response is not a valid JSON.  
  
### ToGoogleCredential()
    
    
    public GoogleCredential ToGoogleCredential()

Creates a [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential) from this credential.

**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential)` |   
  
## Extension Method

[Utilities.ThrowIfNull<T>(T, string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Util.Utilities#Google_Apis_Util_Utilities_ThrowIfNull__1___0_System_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
