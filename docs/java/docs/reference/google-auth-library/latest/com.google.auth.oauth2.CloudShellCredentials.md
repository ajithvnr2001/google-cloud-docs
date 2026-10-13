---
url: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CloudShellCredentials
title: Class CloudShellCredentials (1.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:13.395401+00:00
---

# Class CloudShellCredentials (1.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CloudShellCredentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudShellCredentials (1.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.54.0 (latest)  1.50.0  1.49.0  1.48.0  1.46.0  1.43.0  1.42.1  1.41.0  1.40.0  1.39.1  1.38.0  1.37.1  1.36.0  1.35.0  1.34.0  1.33.1  1.32.1  1.31.0  1.30.1  1.29.1-SNAPSHOT  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.20.0  1.19.0  1.18.0  1.7.0  1.6.1  1.4.0  1.3.0 
    
    
    public class CloudShellCredentials extends GoogleCredentials

OAuth2 credentials representing the built-in service account for Google Cloud Shell.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials) > [OAuth2Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials) > [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials) > CloudShellCredentials

## Inherited Members

[Credentials.blockingGetToCallback(URI,RequestMetadataCallback)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_blockingGetToCallback_java_net_URI_com_google_auth_RequestMetadataCallback_)

[Credentials.getMetricsCredentialType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getMetricsCredentialType__)

[Credentials.getRequestMetadata()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getRequestMetadata__)

[GoogleCredentials.create(AccessToken)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_create_com_google_auth_oauth2_AccessToken_)

[GoogleCredentials.create(String,AccessToken)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_create_java_lang_String_com_google_auth_oauth2_AccessToken_)

[GoogleCredentials.createDelegated(String)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createDelegated_java_lang_String_)

[GoogleCredentials.createScoped(String)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScoped_java_lang_String____)

[GoogleCredentials.createScoped(Collection<String>)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScoped_java_util_Collection_java_lang_String__)

[GoogleCredentials.createScoped(Collection<String>,Collection<String>)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScoped_java_util_Collection_java_lang_String__java_util_Collection_java_lang_String__)

[GoogleCredentials.createScopedRequired()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScopedRequired__)

[GoogleCredentials.createWithCustomRetryStrategy(boolean)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createWithCustomRetryStrategy_boolean_)

[GoogleCredentials.createWithQuotaProject(String)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createWithQuotaProject_java_lang_String_)

[GoogleCredentials.equals(@Nullable Object)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_equals__org_jspecify_annotations_Nullable_java_lang_Object_)

[GoogleCredentials.fromStream(InputStream)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_fromStream_java_io_InputStream_)

[GoogleCredentials.fromStream(InputStream,HttpTransportFactory)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_fromStream_java_io_InputStream_com_google_auth_http_HttpTransportFactory_)

[GoogleCredentials.getAdditionalHeaders()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getAdditionalHeaders__)

[GoogleCredentials.getApplicationDefault()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)

[GoogleCredentials.getApplicationDefault(HttpTransportFactory)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault_com_google_auth_http_HttpTransportFactory_)

[GoogleCredentials.getCredentialInfo()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getCredentialInfo__)

[GoogleCredentials.getProjectId()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getProjectId__)

[GoogleCredentials.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getQuotaProjectId__)

[GoogleCredentials.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getUniverseDomain__)

[GoogleCredentials.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_hashCode__)

[GoogleCredentials.isExplicitUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_isExplicitUniverseDomain__)

[GoogleCredentials.newBuilder()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_newBuilder__)

[GoogleCredentials.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toBuilder__)

[GoogleCredentials.toString()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toString__)

[GoogleCredentials.toStringHelper()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toStringHelper__)

[OAuth2Credentials.<T>getFromServiceLoader(Class<? extends T>,T)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials__T_getFromServiceLoader_java_lang_Class___extends_T__T_)

[OAuth2Credentials.addChangeListener(OAuth2Credentials.CredentialsChangedListener)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_addChangeListener_com_google_auth_oauth2_OAuth2Credentials_CredentialsChangedListener_)

[OAuth2Credentials.getAccessToken()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getAccessToken__)

[OAuth2Credentials.getAuthenticationType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getAuthenticationType__)

[OAuth2Credentials.getRequestMetadata(@Nullable URI)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getRequestMetadata__org_jspecify_annotations_Nullable_java_net_URI_)

[OAuth2Credentials.getRequestMetadata(URI,Executor,RequestMetadataCallback)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getRequestMetadata_java_net_URI_java_util_concurrent_Executor_com_google_auth_RequestMetadataCallback_)

[OAuth2Credentials.getRequestMetadataInternal()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_getRequestMetadataInternal__)

[OAuth2Credentials.hasRequestMetadata()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_hasRequestMetadata__)

[OAuth2Credentials.hasRequestMetadataOnly()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_hasRequestMetadataOnly__)

[OAuth2Credentials.newInstance(String)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_newInstance_java_lang_String_)

[OAuth2Credentials.refresh()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_refresh__)

[OAuth2Credentials.refreshAccessToken()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_refreshAccessToken__)

[OAuth2Credentials.refreshIfExpired()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_refreshIfExpired__)

[OAuth2Credentials.removeChangeListener(OAuth2Credentials.CredentialsChangedListener)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_removeChangeListener_com_google_auth_oauth2_OAuth2Credentials_CredentialsChangedListener_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### GET_AUTH_TOKEN_REQUEST
    
    
    protected static final String GET_AUTH_TOKEN_REQUEST

The Cloud Shell back authorization channel uses serialized Javascript Protobuffers, preceded by the message length and a new line character. However, the request message has no content, so a token request consists of an empty JsPb, and its 2 character length prefix.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### GET_AUTH_TOKEN_REQUEST_BYTES
    
    
    protected static final byte[] GET_AUTH_TOKEN_REQUEST_BYTES

**Field Value**  
---  
**Type** | **Description**  
`byte[]` |   
  
## Static Methods 

### create(int authPort)
    
    
    public static CloudShellCredentials create(int authPort)

**Parameter**  
---  
**Name** | **Description**  
`authPort` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudShellCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CloudShellCredentials)` |   
  
### newBuilder()
    
    
    public static CloudShellCredentials.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[CloudShellCredentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CloudShellCredentials.Builder)` |   
  
## Methods 

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

[GoogleCredentials.equals(@Nullable Object obj)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_equals__org_jspecify_annotations_Nullable_java_lang_Object_)

### getAuthPort()
    
    
    protected int getAuthPort()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GoogleCredentials.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_hashCode__)

### refreshAccessToken()
    
    
    public AccessToken refreshAccessToken()

Method to refresh the access token according to the specific type of credentials.

Throws IllegalStateException if not overridden since direct use of OAuth2Credentials is only for temporary or non-refreshing access tokens.

**Returns**  
---  
**Type** | **Description**  
`[AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken)` |   
**Overrides**

[OAuth2Credentials.refreshAccessToken()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials#com_google_auth_oauth2_OAuth2Credentials_refreshAccessToken__)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### toBuilder()
    
    
    public CloudShellCredentials.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[CloudShellCredentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CloudShellCredentials.Builder)` |   
**Overrides**

[GoogleCredentials.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toBuilder__)

### toString()
    
    
    public String toString()

Returns a string representation of this credential, including request metadata and access token.

**Security Warning:** The output of this method includes the request metadata which contains the raw Bearer access token, and the raw access token value. Do not log this output in production environments as it may expose sensitive credentials.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[GoogleCredentials.toString()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toString__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
