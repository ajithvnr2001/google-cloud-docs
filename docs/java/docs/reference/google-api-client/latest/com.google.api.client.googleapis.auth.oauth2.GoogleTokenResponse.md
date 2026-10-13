---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse
title: Class GoogleTokenResponse (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:52.651502+00:00
---

# Class GoogleTokenResponse (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GoogleTokenResponse (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public class GoogleTokenResponse extends TokenResponse

Google OAuth 2.0 JSON model for a successful access token response as specified in [Successful Response](http://tools.ietf.org/html/rfc6749#section-5.1), including an ID token as specified in [OpenID Connect Session Management 1.0](http://openid.net/specs/openid-connect-session-1_0.html).

This response object is the result of [GoogleAuthorizationCodeTokenRequest#execute()](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeTokenRequest#com_google_api_client_googleapis_auth_oauth2_GoogleAuthorizationCodeTokenRequest_execute__) and [GoogleRefreshTokenRequest#execute()](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleRefreshTokenRequest#com_google_api_client_googleapis_auth_oauth2_GoogleRefreshTokenRequest_execute__). Use [#parseIdToken()](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse#com_google_api_client_googleapis_auth_oauth2_GoogleTokenResponse_parseIdToken__) to parse the [GoogleIdToken](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken) and then call [GoogleIdTokenVerifier#verify(GoogleIdToken)](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier#com_google_api_client_googleapis_auth_oauth2_GoogleIdTokenVerifier_verify_com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_).

Implementation is not thread-safe.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > java.util.AbstractMap > com.google.api.client.util.GenericData > com.google.api.client.json.GenericJson > com.google.api.client.auth.oauth2.TokenResponse > GoogleTokenResponse

## Inherited Members

com.google.api.client.auth.oauth2.TokenResponse.clone()

com.google.api.client.auth.oauth2.TokenResponse.getAccessToken()

com.google.api.client.auth.oauth2.TokenResponse.getExpiresInSeconds()

com.google.api.client.auth.oauth2.TokenResponse.getRefreshToken()

com.google.api.client.auth.oauth2.TokenResponse.getScope()

com.google.api.client.auth.oauth2.TokenResponse.getTokenType()

com.google.api.client.auth.oauth2.TokenResponse.set(java.lang.String,java.lang.Object)

com.google.api.client.auth.oauth2.TokenResponse.setAccessToken(java.lang.String)

com.google.api.client.auth.oauth2.TokenResponse.setExpiresInSeconds(java.lang.Long)

com.google.api.client.auth.oauth2.TokenResponse.setRefreshToken(java.lang.String)

com.google.api.client.auth.oauth2.TokenResponse.setScope(java.lang.String)

com.google.api.client.auth.oauth2.TokenResponse.setTokenType(java.lang.String)

com.google.api.client.json.GenericJson.getFactory()

com.google.api.client.json.GenericJson.setFactory(com.google.api.client.json.JsonFactory)

com.google.api.client.json.GenericJson.toPrettyString()

com.google.api.client.json.GenericJson.toString()

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

### GoogleTokenResponse()
    
    
    public GoogleTokenResponse()

## Methods 

### clone()
    
    
    public GoogleTokenResponse clone()

**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.clone()

### getIdToken()
    
    
    public final String getIdToken()

Beta   
Returns the ID token.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### parseIdToken()
    
    
    public GoogleIdToken parseIdToken()

Beta   
Parses using [GoogleIdToken#parse(JsonFactory, String)](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken#com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_parse_com_google_api_client_json_JsonFactory_java_lang_String_) based on the JSON factory and [ID token](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse#com_google_api_client_googleapis_auth_oauth2_GoogleTokenResponse_getIdToken__).

**Returns**  
---  
**Type** | **Description**  
`[GoogleIdToken](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### set(String fieldName, Object value)
    
    
    public GoogleTokenResponse set(String fieldName, Object value)

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.set(java.lang.String,java.lang.Object)

### setAccessToken(String accessToken)
    
    
    public GoogleTokenResponse setAccessToken(String accessToken)

**Parameter**  
---  
**Name** | **Description**  
`accessToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.setAccessToken(java.lang.String)

### setExpiresInSeconds(Long expiresIn)
    
    
    public GoogleTokenResponse setExpiresInSeconds(Long expiresIn)

**Parameter**  
---  
**Name** | **Description**  
`expiresIn` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.setExpiresInSeconds(java.lang.Long)

### setIdToken(String idToken)
    
    
    public GoogleTokenResponse setIdToken(String idToken)

Beta   
Sets the ID token.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`idToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
  
### setRefreshToken(String refreshToken)
    
    
    public GoogleTokenResponse setRefreshToken(String refreshToken)

**Parameter**  
---  
**Name** | **Description**  
`refreshToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.setRefreshToken(java.lang.String)

### setScope(String scope)
    
    
    public GoogleTokenResponse setScope(String scope)

**Parameter**  
---  
**Name** | **Description**  
`scope` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.setScope(java.lang.String)

### setTokenType(String tokenType)
    
    
    public GoogleTokenResponse setTokenType(String tokenType)

**Parameter**  
---  
**Name** | **Description**  
`tokenType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse)` |   
**Overrides**

com.google.api.client.auth.oauth2.TokenResponse.setTokenType(java.lang.String)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
