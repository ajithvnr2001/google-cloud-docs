---
url: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest
title: Class RefreshTokenRequest (1.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:00.556720+00:00
---

# Class RefreshTokenRequest (1.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RefreshTokenRequest (1.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.39.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.38.2 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.38.2/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.37.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.37.0/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.36.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.36.0/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.34.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.34.1/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.33.3 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.33.3/com.google.api.client.auth.oauth2.RefreshTokenRequest)
  * [ 1.32.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.32.1/com.google.api.client.auth.oauth2.RefreshTokenRequest)


    
    
    public class RefreshTokenRequest extends TokenRequest

OAuth 2.0 request to refresh an access token using a refresh token as specified in [Refreshing an Access Token](http://tools.ietf.org/html/rfc6749#section-6).

Use [Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.Credential) to access protected resources from the resource server using the TokenResponse returned by #execute(). On error, it will instead throw [TokenResponseException](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenResponseException).

Sample usage:
    
    
     static void refreshAccessToken() throws IOException {
     try {
     TokenResponse response =
     new RefreshTokenRequest(new NetHttpTransport(), new GsonFactory(), new GenericUrl(
     "https://server.example.com/token"), "tGzv3JOkF0XG5Qx2TlKWIA")
     .setClientAuthentication(
     new BasicAuthentication("s6BhdRkqt3", "7Fjfp0ZBr1KtDRbnfVdmIw")).execute();
     System.out.println("Access token: " + response.getAccessToken());
     } catch (TokenResponseException e) {
     if (e.getDetails() != null) {
     System.err.println("Error: " + e.getDetails().getError());
     if (e.getDetails().getErrorDescription() != null) {
     System.err.println(e.getDetails().getErrorDescription());
     }
     if (e.getDetails().getErrorUri() != null) {
     System.err.println(e.getDetails().getErrorUri());
     }
     } else {
     System.err.println(e.getMessage());
     }
     }
     }
     

Some OAuth 2.0 providers don't support BasicAuthentication but instead support [ClientParametersAuthentication](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.ClientParametersAuthentication). In the above sample code, simply replace the class name and it will work the same way.

Implementation is not thread-safe.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > java.util.AbstractMap > com.google.api.client.util.GenericData > [TokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest) > RefreshTokenRequest

## Inherited Members

[TokenRequest.execute()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_execute__)

[TokenRequest.executeUnparsed()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_executeUnparsed__)

[TokenRequest.getClientAuthentication()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getClientAuthentication__)

[TokenRequest.getGrantType()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getGrantType__)

[TokenRequest.getJsonFactory()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getJsonFactory__)

[TokenRequest.getRequestInitializer()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getRequestInitializer__)

[TokenRequest.getResponseClass()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getResponseClass__)

[TokenRequest.getScopes()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getScopes__)

[TokenRequest.getTokenServerUrl()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getTokenServerUrl__)

[TokenRequest.getTransport()](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_getTransport__)

[TokenRequest.set(String,Object)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_set_java_lang_String_java_lang_Object_)

[TokenRequest.setClientAuthentication(HttpExecuteInterceptor)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setClientAuthentication_com_google_api_client_http_HttpExecuteInterceptor_)

[TokenRequest.setGrantType(String)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setGrantType_java_lang_String_)

[TokenRequest.setRequestInitializer(HttpRequestInitializer)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setRequestInitializer_com_google_api_client_http_HttpRequestInitializer_)

[TokenRequest.setResponseClass(Class<? extends TokenResponse>)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setResponseClass_java_lang_Class___extends_com_google_api_client_auth_oauth2_TokenResponse__)

[TokenRequest.setScopes(Collection<String>)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setScopes_java_util_Collection_java_lang_String__)

[TokenRequest.setTokenServerUrl(GenericUrl)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setTokenServerUrl_com_google_api_client_http_GenericUrl_)

com.google.api.client.util.GenericData.clone()

com.google.api.client.util.GenericData.entrySet()

com.google.api.client.util.GenericData.equals(java.lang.Object)

com.google.api.client.util.GenericData.get(java.lang.Object)

com.google.api.client.util.GenericData.getClassInfo()

com.google.api.client.util.GenericData.getUnknownKeys()

com.google.api.client.util.GenericData.hashCode()

com.google.api.client.util.GenericData.put(java.lang.String,java.lang.Object)

com.google.api.client.util.GenericData.putAll(java.util.Map<? extends java.lang.String,?>)

com.google.api.client.util.GenericData.remove(java.lang.Object)

com.google.api.client.util.GenericData.setUnknownKeys(java.util.Map<java.lang.String,java.lang.Object>)

com.google.api.client.util.GenericData.toString()

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

[AbstractMap.clear()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#clear--)

[AbstractMap.containsKey(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsKey-java.lang.Object-)

[AbstractMap.containsValue(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsValue-java.lang.Object-)

[AbstractMap.isEmpty()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#isEmpty--)

[AbstractMap.keySet()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#keySet--)

[AbstractMap.put(K,V)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#put-K-V-)

[AbstractMap.putAll(Map<? extends K,? extends V>)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#putAll-java.util.Map<?%20extends%20K-?%20extends%20V>-)

[AbstractMap.size()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#size--)

[AbstractMap.values()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#values--)

## Constructors 

### RefreshTokenRequest(HttpTransport transport, JsonFactory jsonFactory, GenericUrl tokenServerUrl, String refreshToken)
    
    
    public RefreshTokenRequest(HttpTransport transport, JsonFactory jsonFactory, GenericUrl tokenServerUrl, String refreshToken)

**Parameters**  
---  
**Name** | **Description**  
`transport` | `com.google.api.client.http.HttpTransport`  
HTTP transport  
`jsonFactory` | `com.google.api.client.json.JsonFactory`  
JSON factory  
`tokenServerUrl` | `com.google.api.client.http.GenericUrl`  
token server URL  
`refreshToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
refresh token issued to the client  
  
## Methods 

### getRefreshToken()
    
    
    public final String getRefreshToken()

Returns the refresh token issued to the client.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### set(String fieldName, Object value)
    
    
    public RefreshTokenRequest set(String fieldName, Object value)

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.set(String fieldName, Object value)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_set_java_lang_String_java_lang_Object_)

### setClientAuthentication(HttpExecuteInterceptor clientAuthentication)
    
    
    public RefreshTokenRequest setClientAuthentication(HttpExecuteInterceptor clientAuthentication)

Sets the client authentication or `null` for none.

The recommended initializer by the specification is BasicAuthentication. All authorization servers must support that. A common alternative is [ClientParametersAuthentication](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.ClientParametersAuthentication). An alternative client authentication method may be provided that implements HttpRequestInitializer.

This HTTP request execute interceptor is guaranteed to be the last execute interceptor before the request is executed, and after any execute interceptor set by the #getRequestInitializer().

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`clientAuthentication` | `com.google.api.client.http.HttpExecuteInterceptor`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setClientAuthentication(HttpExecuteInterceptor clientAuthentication)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setClientAuthentication_com_google_api_client_http_HttpExecuteInterceptor_)

### setGrantType(String grantType)
    
    
    public RefreshTokenRequest setGrantType(String grantType)

Sets the grant type (`"authorization_code"`, `"password"`, ` "client_credentials"`, `"refresh_token"` or absolute URI of the extension grant type).

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`grantType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setGrantType(String grantType)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setGrantType_java_lang_String_)

### setRefreshToken(String refreshToken)
    
    
    public RefreshTokenRequest setRefreshToken(String refreshToken)

Sets the refresh token issued to the client.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`refreshToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
  
### setRequestInitializer(HttpRequestInitializer requestInitializer)
    
    
    public RefreshTokenRequest setRequestInitializer(HttpRequestInitializer requestInitializer)

Sets the HTTP request initializer or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`requestInitializer` | `com.google.api.client.http.HttpRequestInitializer`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setRequestInitializer(HttpRequestInitializer requestInitializer)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setRequestInitializer_com_google_api_client_http_HttpRequestInitializer_)

### setResponseClass(Class<? extends TokenResponse> responseClass)
    
    
    public RefreshTokenRequest setResponseClass(Class<? extends TokenResponse> responseClass)

Sets the TokenResponse class to allow specifying object parsing.

**Parameter**  
---  
**Name** | **Description**  
`responseClass` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends com.google.api.client.auth.oauth2.TokenResponse>`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setResponseClass(Class<? extends TokenResponse> responseClass)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setResponseClass_java_lang_Class___extends_com_google_api_client_auth_oauth2_TokenResponse__)

### setScopes(Collection<String> scopes)
    
    
    public RefreshTokenRequest setScopes(Collection<String> scopes)

Sets the list of scopes (as specified in [Access Token Scope](http://tools.ietf.org/html/rfc6749#section-3.3)) or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setScopes(Collection<String> scopes)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setScopes_java_util_Collection_java_lang_String__)

### setTokenServerUrl(GenericUrl tokenServerUrl)
    
    
    public RefreshTokenRequest setTokenServerUrl(GenericUrl tokenServerUrl)

Sets the token server URL.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`tokenServerUrl` | `com.google.api.client.http.GenericUrl`  
  
**Returns**  
---  
**Type** | **Description**  
`[RefreshTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.RefreshTokenRequest)` |   
**Overrides**

[TokenRequest.setTokenServerUrl(GenericUrl tokenServerUrl)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.TokenRequest#com_google_api_client_auth_oauth2_TokenRequest_setTokenServerUrl_com_google_api_client_http_GenericUrl_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
