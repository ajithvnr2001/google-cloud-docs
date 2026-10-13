---
url: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl
title: Class AuthorizationRequestUrl (1.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:12.667076+00:00
---

# Class AuthorizationRequestUrl (1.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthorizationRequestUrl (1.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.39.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.38.2 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.38.2/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.37.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.37.0/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.36.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.36.0/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.34.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.34.1/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.33.3 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.33.3/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)
  * [ 1.32.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.32.1/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)


    
    
    public class AuthorizationRequestUrl extends GenericUrl

OAuth 2.0 URL builder for an authorization web page to allow the end user to authorize the application to access their protected resources, as specified in [Authorization Endpoint](http://tools.ietf.org/html/rfc6749#section-3.1).

Sample usage for a web application:
    
    
     public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
     String url = new AuthorizationRequestUrl(
     "https://server.example.com/authorize", "s6BhdRkqt3", Arrays.asList("code")).setState("xyz")
     .setRedirectUri("https://client.example.com/rd").build();
     response.sendRedirect(url);
     }
     

Implementation is not thread-safe.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > java.util.AbstractMap > com.google.api.client.util.GenericData > com.google.api.client.http.GenericUrl > AuthorizationRequestUrl

## Inherited Members

com.google.api.client.http.GenericUrl.appendRawPath(java.lang.String)

com.google.api.client.http.GenericUrl.build()

com.google.api.client.http.GenericUrl.buildAuthority()

com.google.api.client.http.GenericUrl.buildRelativeUrl()

com.google.api.client.http.GenericUrl.clone()

com.google.api.client.http.GenericUrl.equals(java.lang.Object)

com.google.api.client.http.GenericUrl.getAll(java.lang.String)

com.google.api.client.http.GenericUrl.getFirst(java.lang.String)

com.google.api.client.http.GenericUrl.getFragment()

com.google.api.client.http.GenericUrl.getHost()

com.google.api.client.http.GenericUrl.getPathParts()

com.google.api.client.http.GenericUrl.getPort()

com.google.api.client.http.GenericUrl.getRawPath()

com.google.api.client.http.GenericUrl.getScheme()

com.google.api.client.http.GenericUrl.getUserInfo()

com.google.api.client.http.GenericUrl.hashCode()

com.google.api.client.http.GenericUrl.set(java.lang.String,java.lang.Object)

com.google.api.client.http.GenericUrl.setFragment(java.lang.String)

com.google.api.client.http.GenericUrl.setHost(java.lang.String)

com.google.api.client.http.GenericUrl.setPathParts(java.util.List<java.lang.String>)

com.google.api.client.http.GenericUrl.setPort(int)

com.google.api.client.http.GenericUrl.setRawPath(java.lang.String)

com.google.api.client.http.GenericUrl.setScheme(java.lang.String)

com.google.api.client.http.GenericUrl.setUserInfo(java.lang.String)

com.google.api.client.http.GenericUrl.toPathParts(java.lang.String)

com.google.api.client.http.GenericUrl.toPathParts(java.lang.String,boolean)

com.google.api.client.http.GenericUrl.toString()

com.google.api.client.http.GenericUrl.toURI()

com.google.api.client.http.GenericUrl.toURL()

com.google.api.client.http.GenericUrl.toURL(java.lang.String)

com.google.api.client.util.GenericData.entrySet()

com.google.api.client.util.GenericData.get(java.lang.Object)

com.google.api.client.util.GenericData.getClassInfo()

com.google.api.client.util.GenericData.getUnknownKeys()

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

### AuthorizationRequestUrl(String authorizationServerEncodedUrl, String clientId, Collection<String> responseTypes)
    
    
    public AuthorizationRequestUrl(String authorizationServerEncodedUrl, String clientId, Collection<String> responseTypes)

**Parameters**  
---  
**Name** | **Description**  
`authorizationServerEncodedUrl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
authorization server encoded URL  
`clientId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
client identifier  
`responseTypes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
[response type](http://tools.ietf.org/html/rfc6749#section-3.1.1), which must be `"code"` for requesting an authorization code, ` "token"` for requesting an access token (implicit grant), or a list of registered extension values to join with a space  
  
## Methods 

### clone()
    
    
    public AuthorizationRequestUrl clone()

**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
**Overrides**

com.google.api.client.http.GenericUrl.clone()

### getClientId()
    
    
    public final String getClientId()

Returns the client identifier.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRedirectUri()
    
    
    public final String getRedirectUri()

Returns the URI that the authorization server directs the resource owner's user-agent back to the client after a successful authorization grant (as specified in [Redirection Endpoint](http://tools.ietf.org/html/rfc6749#section-3.1.2)) or ` null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResponseTypes()
    
    
    public final String getResponseTypes()

Returns the [Response type](http://tools.ietf.org/html/rfc6749#section-3.1.1), which must be `"code"` for requesting an authorization code, `"token"` for requesting an access token (implicit grant), or space-separated registered extension values.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getScopes()
    
    
    public final String getScopes()

Returns the space-separated list of scopes (as specified in [Access Token Scope](http://tools.ietf.org/html/rfc6749#section-3.3)) or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getState()
    
    
    public final String getState()

Returns the state (an opaque value used by the client to maintain state between the request and callback, as mentioned in [Registration Requirements](http://tools.ietf.org/html/rfc6749#section-3.1.2.2)) or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### set(String fieldName, Object value)
    
    
    public AuthorizationRequestUrl set(String fieldName, Object value)

**Parameters**  
---  
**Name** | **Description**  
`fieldName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
**Overrides**

com.google.api.client.http.GenericUrl.set(java.lang.String,java.lang.Object)

### setClientId(String clientId)
    
    
    public AuthorizationRequestUrl setClientId(String clientId)

Sets the client identifier.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`clientId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
  
### setRedirectUri(String redirectUri)
    
    
    public AuthorizationRequestUrl setRedirectUri(String redirectUri)

Sets the URI that the authorization server directs the resource owner's user-agent back to the client after a successful authorization grant (as specified in [Redirection Endpoint](http://tools.ietf.org/html/rfc6749#section-3.1.2)) or ` null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`redirectUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
  
### setResponseTypes(Collection<String> responseTypes)
    
    
    public AuthorizationRequestUrl setResponseTypes(Collection<String> responseTypes)

Sets the [response type](http://tools.ietf.org/html/rfc6749#section-3.1.1), which must be `"code"` for requesting an authorization code, `"token"` for requesting an access token (implicit grant), or a list of registered extension values to join with a space.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`responseTypes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
  
### setScopes(Collection<String> scopes)
    
    
    public AuthorizationRequestUrl setScopes(Collection<String> scopes)

Sets the list of scopes (as specified in [Access Token Scope](http://tools.ietf.org/html/rfc6749#section-3.3)) or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
collection of scopes to be joined by a space separator (or a single value containing multiple space-separated scopes) or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
  
### setState(String state)
    
    
    public AuthorizationRequestUrl setState(String state)

Sets the state (an opaque value used by the client to maintain state between the request and callback, as mentioned in [Registration Requirements](http://tools.ietf.org/html/rfc6749#section-3.1.2.2)) or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`state` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationRequestUrl](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationRequestUrl)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
