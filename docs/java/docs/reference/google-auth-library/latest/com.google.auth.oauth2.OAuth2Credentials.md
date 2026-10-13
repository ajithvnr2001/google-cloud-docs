---
url: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials
title: Class OAuth2Credentials (1.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:02.115970+00:00
---

# Class OAuth2Credentials (1.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OAuth2Credentials (1.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.54.0 (latest)  1.50.0  1.49.0  1.48.0  1.46.0  1.43.0  1.42.1  1.41.0  1.40.0  1.39.1  1.38.0  1.37.1  1.36.0  1.35.0  1.34.0  1.33.1  1.32.1  1.31.0  1.30.1  1.29.1-SNAPSHOT  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.20.0  1.19.0  1.18.0  1.7.0  1.6.1  1.4.0  1.3.0 
    
    
    public class OAuth2Credentials extends Credentials

Base type for Credentials using OAuth2.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials) > OAuth2Credentials

## Inherited Members

[Credentials.blockingGetToCallback(URI,RequestMetadataCallback)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_blockingGetToCallback_java_net_URI_com_google_auth_RequestMetadataCallback_)

[Credentials.getAuthenticationType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getAuthenticationType__)

[Credentials.getMetricsCredentialType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getMetricsCredentialType__)

[Credentials.getRequestMetadata()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata__)

[Credentials.getRequestMetadata(@Nullable URI)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata__org_jspecify_annotations_Nullable_java_net_URI_)

[Credentials.getRequestMetadata(URI,Executor,RequestMetadataCallback)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata_java_net_URI_java_util_concurrent_Executor_com_google_auth_RequestMetadataCallback_)

[Credentials.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getUniverseDomain__)

[Credentials.hasRequestMetadata()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_hasRequestMetadata__)

[Credentials.hasRequestMetadataOnly()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_hasRequestMetadataOnly__)

[Credentials.refresh()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_refresh__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### <T>getFromServiceLoader(Class<? extends T> clazz, T defaultInstance)
    
    
    public static T <T>getFromServiceLoader(Class<? extends T> clazz, T defaultInstance)

Returns the first service provider from the given service loader.

**Parameters**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends T>`  
The class of the service provider to load.  
`defaultInstance` | `T`  
The default instance to return if no service providers are found.  
**Returns**  
---  
**Type** | **Description**  
`T` | The first service provider from the service loader, or the `defaultInstance` if no service providers are found.  
  
### create(AccessToken accessToken)
    
    
    public static OAuth2Credentials create(AccessToken accessToken)

Returns the credentials instance from the given access token.

**Parameter**  
---  
**Name** | **Description**  
`accessToken` | `[AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken)`  
the access token  
**Returns**  
---  
**Type** | **Description**  
`[OAuth2Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials)` | the credentials instance  
  
### newBuilder()
    
    
    public static OAuth2Credentials.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[OAuth2Credentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials.Builder)` |   
  
### newInstance(String className)
    
    
    protected static HttpTransportFactory newInstance(String className)

Best-effort safe mechanism to attempt to instantiate an [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory) from a class name.

This method attempts to avoid Arbitrary Code Execution (ACE) vulnerabilities by:

  1. Checking if the class name matches the default or ServiceLoader-provided factory, and returning that instance if so. 
  2. If not, loading the class using reflection without running static initializers. 
  3. Verifying that the loaded class is assignable to [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory). 
  4. Only after verification, instantiating the class using its default constructor. 



**Parameter**  
---  
**Name** | **Description**  
`className` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The fully qualified name of the class to instantiate.  
**Returns**  
---  
**Type** | **Description**  
`[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)` | An instance of [HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory).  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | If the class cannot be loaded, is the wrong type, or cannot be instantiated.  
`[ClassNotFoundException](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassNotFoundException.html)` | If the class cannot be loaded, is the wrong type, or cannot be instantiated.  
  
## Constructors 

### OAuth2Credentials()
    
    
    protected OAuth2Credentials()

Default constructor.

### OAuth2Credentials(@Nullable AccessToken accessToken)
    
    
    protected OAuth2Credentials(@Nullable AccessToken accessToken)

Constructor with explicit access token.

**Parameter**  
---  
**Name** | **Description**  
`accessToken` | `@org.jspecify.annotations.Nullable com.google.auth.oauth2.AccessToken`  
initial or temporary access token  
  
### OAuth2Credentials(@Nullable AccessToken accessToken, Duration refreshMargin, Duration expirationMargin)
    
    
    protected OAuth2Credentials(@Nullable AccessToken accessToken, Duration refreshMargin, Duration expirationMargin)

**Parameters**  
---  
**Name** | **Description**  
`accessToken` | `@org.jspecify.annotations.Nullable com.google.auth.oauth2.AccessToken`  
  
`refreshMargin` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
`expirationMargin` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
  
## Methods 

### addChangeListener(OAuth2Credentials.CredentialsChangedListener listener)
    
    
    public final void addChangeListener(OAuth2Credentials.CredentialsChangedListener listener)

Adds a listener that is notified when the Credentials data changes.

This is called when token content changes, such as when the access token is refreshed. This is typically used by code caching the access token.

**Parameter**  
---  
**Name** | **Description**  
`listener` | `[OAuth2Credentials.CredentialsChangedListener](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials.CredentialsChangedListener)`  
the listener to be added  
  
### equals(@Nullable Object obj)
    
    
    public boolean equals(@Nullable Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `@org.jspecify.annotations.Nullable java.lang.Object`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAccessToken()
    
    
    public final @Nullable AccessToken getAccessToken()

Returns the cached access token.

If not set, you should call [#refresh()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_refresh__) to fetch and cache an access token.

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.auth.oauth2.AccessToken` | The cached access token.  
  
### getAdditionalHeaders()
    
    
    protected Map<String,List<String>> getAdditionalHeaders()

Provide additional headers to return as request metadata.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` | additional headers  
  
### getAuthenticationType()
    
    
    public String getAuthenticationType()

A constant string name describing the authentication technology.

E.g. “OAuth2”, “SSL”. For use by the transport layer to determine whether it supports the type of authentication in the case where [Credentials#hasRequestMetadataOnly](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_hasRequestMetadataOnly_) is false. Also serves as a debugging helper.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Credentials.getAuthenticationType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getAuthenticationType__)

### getRequestMetadata(@Nullable URI uri)
    
    
    public Map<String,List<String>> getRequestMetadata(@Nullable URI uri)

Provide the request metadata by ensuring there is a current access token and providing it as an authorization bearer token.

**Parameter**  
---  
**Name** | **Description**  
`uri` | `@org.jspecify.annotations.Nullable java.net.URI`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
**Overrides**

[Credentials.getRequestMetadata(@Nullable URI uri)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata__org_jspecify_annotations_Nullable_java_net_URI_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getRequestMetadata(URI uri, Executor executor, RequestMetadataCallback callback)
    
    
    public void getRequestMetadata(URI uri, Executor executor, RequestMetadataCallback callback)

Get the current request metadata without blocking.

This should be called by the transport layer on each request, and the data should be populated in headers or other context. The implementation can either call the callback inline or asynchronously. Either way it should **never block** in this method. The executor is provided for tasks that may block.

The default implementation will just call [#getRequestMetadata(URI)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getRequestMetadata_) then the callback from the given executor.

The convention for handling binary data is for the key in the returned map to end with `"-bin"` and for the corresponding values to be base64 encoded.

**Parameters**  
---  
**Name** | **Description**  
`uri` | `[URI](https://docs.oracle.com/javase/8/docs/api/java/net/URI.html)`  
  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
  
`callback` | `[RequestMetadataCallback](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.RequestMetadataCallback)`  
  
**Overrides**

[Credentials.getRequestMetadata(URI uri, Executor executor, RequestMetadataCallback callback)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata_java_net_URI_java_util_concurrent_Executor_com_google_auth_RequestMetadataCallback_)

### getRequestMetadataInternal()
    
    
    protected @Nullable Map<String,List<String>> getRequestMetadataInternal()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable java.util.Map<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
  
### hasRequestMetadata()
    
    
    public boolean hasRequestMetadata()

Whether the credentials have metadata entries that should be added to each request.

This should be called by the transport layer to see if [Credentials#getRequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata_) should be used for each request.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Credentials.hasRequestMetadata()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_hasRequestMetadata__)

### hasRequestMetadataOnly()
    
    
    public boolean hasRequestMetadataOnly()

Indicates whether or not the Auth mechanism works purely by including request metadata.

This is meant for the transport layer. If this is true a transport does not need to take actions other than including the request metadata. If this is false, a transport must specifically know about the authentication technology to support it, and should fail to accept the credentials otherwise.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Credentials.hasRequestMetadataOnly()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_hasRequestMetadataOnly__)

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### refresh()
    
    
    public void refresh()

Request a new token regardless of the current token state. If the current token is not expired, it will still be returned during the refresh.

**Overrides**

[Credentials.refresh()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_refresh__)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### refreshAccessToken()
    
    
    public AccessToken refreshAccessToken()

Method to refresh the access token according to the specific type of credentials.

Throws IllegalStateException if not overridden since direct use of OAuth2Credentials is only for temporary or non-refreshing access tokens.

**Returns**  
---  
**Type** | **Description**  
`[AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken)` | never  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | always. OAuth2Credentials does not support refreshing the access token. An instance with a new access token or a derived type that supports refreshing should be used instead.  
  
### refreshIfExpired()
    
    
    public void refreshIfExpired()

Refresh these credentials only if they have expired or are expiring imminently.

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | during token refresh.  
  
### removeChangeListener(OAuth2Credentials.CredentialsChangedListener listener)
    
    
    public final void removeChangeListener(OAuth2Credentials.CredentialsChangedListener listener)

Removes a listener that was added previously.

**Parameter**  
---  
**Name** | **Description**  
`listener` | `[OAuth2Credentials.CredentialsChangedListener](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials.CredentialsChangedListener)`  
The listener to be removed.  
  
### toBuilder()
    
    
    public OAuth2Credentials.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[OAuth2Credentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials.Builder)` |   
  
### toString()
    
    
    public String toString()

Returns a string representation of this credential, including request metadata and access token.

**Security Warning:** The output of this method includes the request metadata which contains the raw Bearer access token, and the raw access token value. Do not log this output in production environments as it may expose sensitive credentials.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
