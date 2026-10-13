---
url: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials
title: Class ImpersonatedCredentials (1.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:57.146294+00:00
---

# Class ImpersonatedCredentials (1.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ImpersonatedCredentials (1.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.54.0 (latest)  1.50.0  1.49.0  1.48.0  1.46.0  1.43.0  1.42.1  1.41.0  1.40.0  1.39.1  1.38.0  1.37.1  1.36.0  1.35.0  1.34.0  1.33.1  1.32.1  1.31.0  1.30.1  1.29.1-SNAPSHOT  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.20.0  1.19.0  1.18.0  1.7.0  1.6.1  1.4.0  1.3.0 
    
    
    public class ImpersonatedCredentials extends GoogleCredentials implements ServiceAccountSigner, IdTokenProvider

ImpersonatedCredentials allowing credentials issued to a user or service account to impersonate another. The source project using ImpersonatedCredentials must enable the "IAMCredentials" API. Also, the target service account must grant the originating principal the "Service Account Token Creator" IAM role.

Usage:

String credPath = "/path/to/svc_account.json"; ServiceAccountCredentials sourceCredentials = ServiceAccountCredentials .fromStream(new FileInputStream(credPath)); sourceCredentials = (ServiceAccountCredentials) sourceCredentials .createScoped(Arrays.asList("<https://www.googleapis.com/auth/iam>"));

ImpersonatedCredentials targetCredentials = ImpersonatedCredentials.create(sourceCredentials, "impersonated-account@project.iam.gserviceaccount.com", null, Arrays.asList("<https://www.googleapis.com/auth/devstorage.read_only>"), 300);

Storage storage_service = StorageOptions.newBuilder().setProjectId("project-id") .setCredentials(targetCredentials).build().getService();

for (Bucket b : storage_service.list().iterateAll()) System.out.println(b);

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials) > [OAuth2Credentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials) > [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials) > ImpersonatedCredentials

## Implements

[ServiceAccountSigner](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.ServiceAccountSigner), [IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider)

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

## Static Methods 

### create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime)
    
    
    public static ImpersonatedCredentials create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime)

**Parameters**  
---  
**Name** | **Description**  
`sourceCredentials` | `[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)`  
the source credential used to acquire the impersonated credentials. It should be either a user account credential or a service account credential.  
`targetPrincipal` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the service account to impersonate  
`delegates` | `@org.jspecify.annotations.Nullable java.util.List<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the chained list of delegates required to grant the final access_token. If set, the sequence of identities must have "Service Account Token Creator" capability granted to the preceding identity. For example, if set to [serviceAccountB, serviceAccountC], the sourceCredential must have the Token Creator role on serviceAccountB. serviceAccountB must have the Token Creator on serviceAccountC. Finally, C must have Token Creator on target_principal. If left unset, sourceCredential must have that role on targetPrincipal.  
`scopes` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
scopes to request during the authorization grant  
`lifetime` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
number of seconds the delegated credential should be valid. By default this value should be at most 3600. However, you can follow [these instructions](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) to set up the service account and extend the maximum lifetime to 43200 (12 hours). <https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth> If the given lifetime is 0, default value 3600 will be used instead when creating the credentials.  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | new credentials  
  
### create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory)
    
    
    public static ImpersonatedCredentials create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory)

**Parameters**  
---  
**Name** | **Description**  
`sourceCredentials` | `[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)`  
the source credential used to acquire the impersonated credentials. It should be either a user account credential or a service account credential.  
`targetPrincipal` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the service account to impersonate  
`delegates` | `@org.jspecify.annotations.Nullable java.util.List<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the chained list of delegates required to grant the final access_token. If set, the sequence of identities must have "Service Account Token Creator" capability granted to the preceding identity. For example, if set to [serviceAccountB, serviceAccountC], the sourceCredential must have the Token Creator role on serviceAccountB. serviceAccountB must have the Token Creator on serviceAccountC. Finally, C must have Token Creator on target_principal. If unset, sourceCredential must have that role on targetPrincipal.  
`scopes` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
scopes to request during the authorization grant  
`lifetime` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
number of seconds the delegated credential should be valid. By default this value should be at most 3600. However, you can follow [these instructions](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) to set up the service account and extend the maximum lifetime to 43200 (12 hours). If the given lifetime is 0, default value 3600 will be used instead when creating the credentials.  
`transportFactory` | `[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)`  
HTTP transport factory that creates the transport used to get access tokens  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | new credentials  
  
### create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory, @Nullable String quotaProjectId)
    
    
    public static ImpersonatedCredentials create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory, @Nullable String quotaProjectId)

**Parameters**  
---  
**Name** | **Description**  
`sourceCredentials` | `[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)`  
the source credential used to acquire the impersonated credentials. It should be either a user account credential or a service account credential.  
`targetPrincipal` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the service account to impersonate  
`delegates` | `@org.jspecify.annotations.Nullable java.util.List<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the chained list of delegates required to grant the final access_token. If set, the sequence of identities must have "Service Account Token Creator" capability granted to the preceding identity. For example, if set to [serviceAccountB, serviceAccountC], the sourceCredential must have the Token Creator role on serviceAccountB. serviceAccountB must have the Token Creator on serviceAccountC. Finally, C must have Token Creator on target_principal. If unset, sourceCredential must have that role on targetPrincipal.  
`scopes` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
scopes to request during the authorization grant  
`lifetime` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
number of seconds the delegated credential should be valid. By default this value should be at most 3600. However, you can follow [these instructions](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) to set up the service account and extend the maximum lifetime to 43200 (12 hours). If the given lifetime is 0, default value 3600 will be used instead when creating the credentials.  
`transportFactory` | `[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)`  
HTTP transport factory that creates the transport used to get access tokens.  
`quotaProjectId` | `@org.jspecify.annotations.Nullable java.lang.String`  
the project used for quota and billing purposes. Should be null unless the caller wants to use a project different from the one that owns the impersonated credential for billing/quota purposes.  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | new credentials  
  
### create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory, @Nullable String quotaProjectId, @Nullable String iamEndpointOverride)
    
    
    public static ImpersonatedCredentials create(GoogleCredentials sourceCredentials, String targetPrincipal, @Nullable List<String> delegates, List<String> scopes, int lifetime, HttpTransportFactory transportFactory, @Nullable String quotaProjectId, @Nullable String iamEndpointOverride)

**Parameters**  
---  
**Name** | **Description**  
`sourceCredentials` | `[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)`  
the source credential used to acquire the impersonated credentials. It should be either a user account credential or a service account credential.  
`targetPrincipal` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the service account to impersonate  
`delegates` | `@org.jspecify.annotations.Nullable java.util.List<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the chained list of delegates required to grant the final access_token. If set, the sequence of identities must have "Service Account Token Creator" capability granted to the preceding identity. For example, if set to [serviceAccountB, serviceAccountC], the sourceCredential must have the Token Creator role on serviceAccountB. serviceAccountB must have the Token Creator on serviceAccountC. Finally, C must have Token Creator on target_principal. If unset, sourceCredential must have that role on targetPrincipal.  
`scopes` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
scopes to request during the authorization grant  
`lifetime` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
number of seconds the delegated credential should be valid. By default this value should be at most 3600. However, you can follow [these instructions](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) to set up the service account and extend the maximum lifetime to 43200 (12 hours). If the given lifetime is 0, default value 3600 will be used instead when creating the credentials.  
`transportFactory` | `[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)`  
HTTP transport factory that creates the transport used to get access tokens.  
`quotaProjectId` | `@org.jspecify.annotations.Nullable java.lang.String`  
the project used for quota and billing purposes. Should be null unless the caller wants to use a project different from the one that owns the impersonated credential for billing/quota purposes.  
`iamEndpointOverride` | `@org.jspecify.annotations.Nullable java.lang.String`  
The full IAM endpoint override with the target_principal embedded. This is useful when supporting impersonation with regional endpoints.  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | new credentials  
  
### fromStream(InputStream credentialsStream)
    
    
    public static ImpersonatedCredentials fromStream(InputStream credentialsStream)

Returns credentials defined by a ImpersonatedCredential key file in JSON format from the Google Developers Console.

Important: If you accept a credential configuration (credential JSON/File/Stream) from an external source for authentication to Google Cloud Platform, you must validate it before providing it to any Google API or library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to {@see [documentation](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials)}.

**Parameter**  
---  
**Name** | **Description**  
`credentialsStream` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
the stream with the credential definition.  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | the credential defined by the credentialsStream.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created from the stream.  
  
### fromStream(InputStream credentialsStream, HttpTransportFactory transportFactory)
    
    
    public static ImpersonatedCredentials fromStream(InputStream credentialsStream, HttpTransportFactory transportFactory)

Returns credentials defined by a ImpersonatedCredential key file in JSON format from the Google Developers Console.

Important: If you accept a credential configuration (credential JSON/File/Stream) from an external source for authentication to Google Cloud Platform, you must validate it before providing it to any Google API or library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to {@see [documentation](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials)}.

**Parameters**  
---  
**Name** | **Description**  
`credentialsStream` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
the stream with the credential definition.  
`transportFactory` | `[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)`  
HTTP transport factory, creates the transport used to get access tokens.  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | the credential defined by the credentialsStream.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created from the stream.  
  
### newBuilder()
    
    
    public static ImpersonatedCredentials.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials.Builder)` |   
  
## Methods 

### createScoped(Collection<String> scopes)
    
    
    public GoogleCredentials createScoped(Collection<String> scopes)

If the credentials support scopes, creates a copy of the identity with the specified scopes, invalidates the existing scoped access token; otherwise, return the same instance.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)` |   
**Overrides**

[GoogleCredentials.createScoped(Collection<String> scopes)](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScoped_java_util_Collection_java_lang_String__)

### createScopedRequired()
    
    
    public boolean createScopedRequired()

Indicates whether the credentials require scopes to be specified via a call to [GoogleCredentials#createScoped](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScoped_) before use.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GoogleCredentials.createScopedRequired()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_createScopedRequired__)

### createWithCustomCalendar(Calendar calendar)
    
    
    public ImpersonatedCredentials createWithCustomCalendar(Calendar calendar)

**Obsolete**

_This method is obsolete and will be removed in a future release._

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is marked obsolete. There is no alternative to setting a custom calendar for the Credential.

Clones the impersonated credentials with a new calendar.

**Parameter**  
---  
**Name** | **Description**  
`calendar` | `[Calendar](https://docs.oracle.com/javase/8/docs/api/java/util/Calendar.html)`  
the calendar that will be used by the new ImpersonatedCredentials instance when parsing the received expiration time of the refreshed access token  
**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials)` | the cloned impersonated credentials with the given custom calendar  
  
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

### getAccount()
    
    
    public String getAccount()

Returns the email field of the serviceAccount that is being impersonated.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | email address of the impersonated service account  
  
### getMetricsCredentialType()
    
    
    public CredentialTypeForMetrics getMetricsCredentialType()

Gets the credential type used for internal metrics header.

The default is `CredentialTypeForMetrics.DO_NOT_SEND`. For a credential that is established to track for metrics, this default should be overridden.

**Returns**  
---  
**Type** | **Description**  
`[CredentialTypeForMetrics](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.CredentialTypeForMetrics)` |   
**Overrides**

[Credentials.getMetricsCredentialType()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Credentials#com_google_auth_Credentials_getMetricsCredentialType__)

### getSourceCredentials()
    
    
    public GoogleCredentials getSourceCredentials()

**Returns**  
---  
**Type** | **Description**  
`[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials)` |   
  
### getUniverseDomain()
    
    
    public String getUniverseDomain()

Gets the universe domain for the credential.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the universe domain from source credentials  
**Overrides**

[GoogleCredentials.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_getUniverseDomain__)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GoogleCredentials.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_hashCode__)

### idTokenWithAudience(String targetAudience, @Nullable List<IdTokenProvider.Option> options)
    
    
    public IdToken idTokenWithAudience(String targetAudience, @Nullable List<IdTokenProvider.Option> options)

Returns an IdToken for the current Credential.

**Parameters**  
---  
**Name** | **Description**  
`targetAudience` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the audience field for the issued ID token  
`options` | `@org.jspecify.annotations.Nullable java.util.List<[Option](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option)>`  
credential specific options for for the token. For example, an ID token for an ImpersonatedCredentials can return the email address within the token claims if "ImpersonatedCredentials.INCLUDE_EMAIL" is provided as a list option.  
Only one option value is supported: "ImpersonatedCredentials.INCLUDE_EMAIL" If no options are set, the default excludes the "includeEmail" attribute in the API request.  
**Returns**  
---  
**Type** | **Description**  
`[IdToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdToken)` | IdToken object which includes the raw id_token, expiration, and audience  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the attempt to get an ID token failed  
  
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
  
### setTransportFactory(HttpTransportFactory httpTransportFactory)
    
    
    public void setTransportFactory(HttpTransportFactory httpTransportFactory)

**Parameter**  
---  
**Name** | **Description**  
`httpTransportFactory` | `[HttpTransportFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpTransportFactory)`  
  
  
### sign(byte[] toSign)
    
    
    public byte[] sign(byte[] toSign)

Signs the provided bytes using the private key associated with the impersonated service account See Also: [Blob Signing](https://cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/signBlob)

**Parameter**  
---  
**Name** | **Description**  
`toSign` | `byte[]`  
bytes to sign  
**Returns**  
---  
**Type** | **Description**  
`byte[]` | signed bytes  
  
### toBuilder()
    
    
    public ImpersonatedCredentials.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ImpersonatedCredentials.Builder](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ImpersonatedCredentials.Builder)` |   
**Overrides**

[GoogleCredentials.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials#com_google_auth_oauth2_GoogleCredentials_toBuilder__)

### toString()
    
    
    public String toString()

Returns a string representation of this credential.

**Security Warning:** The output of this method includes the source credentials which may recursively contain sensitive fields such as access tokens. Do not log this output in production environments as it may expose sensitive credentials.

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
