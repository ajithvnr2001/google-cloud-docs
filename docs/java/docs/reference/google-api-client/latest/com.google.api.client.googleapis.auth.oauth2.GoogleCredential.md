---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential
title: Class GoogleCredential (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:13.238378+00:00
---

# Class GoogleCredential (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GoogleCredential (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public class GoogleCredential extends Credential

**Deprecated.** _Please use[ google-auth-library](https://github.com/googleapis/google-auth-library-java) for handling Application Default Credentials and other non-OAuth2 based authentication._

Thread-safe Google-specific implementation of the OAuth 2.0 helper for accessing protected resources using an access token, as well as optionally refreshing the access token when it expires using a refresh token.

There are three modes supported: access token only, refresh token flow, and service account flow (with or without impersonating a user).

If all you have is an access token, you simply pass the TokenResponse to the credential using Builder#setFromTokenResponse(TokenResponse). Google credential uses BearerToken#authorizationHeaderAccessMethod() as the access method. Sample usage:
    
    
     public static GoogleCredential createCredentialWithAccessTokenOnly(TokenResponse tokenResponse) {
       return new GoogleCredential().setFromTokenResponse(tokenResponse);
     }
     

If you have a refresh token, it is similar to the case of access token only, but you additionally need to pass the credential the client secrets using Builder#setClientSecrets(GoogleClientSecrets) or Builder#setClientSecrets(String, String). Google credential uses [GoogleOAuthConstants#TOKEN_SERVER_URL](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleOAuthConstants#com_google_api_client_googleapis_auth_oauth2_GoogleOAuthConstants_TOKEN_SERVER_URL) as the token server URL, and ClientParametersAuthentication with the client ID and secret as the client authentication. Sample usage:
    
    
     public static GoogleCredential createCredentialWithRefreshToken(
         HttpTransport transport, JsonFactory jsonFactory,
         GoogleClientSecrets clientSecrets, TokenResponse tokenResponse) {
      return new GoogleCredential.Builder().setTransport(transport)
                            .setJsonFactory(jsonFactory)
                            .setClientSecrets(clientSecrets)
                            .build()
                            .setFromTokenResponse(tokenResponse);
     }
     

The [service account flow](https://developers.google.com/accounts/docs/OAuth2ServiceAccount) is used when you want to access data owned by your client application. You download the private key in a `.p12` file from the Google APIs Console. Use Builder#setServiceAccountId(String), Builder#setServiceAccountPrivateKeyFromP12File(File), and Builder#setServiceAccountScopes(Collection). Sample usage:
    
    
     public static GoogleCredential createCredentialForServiceAccount(HttpTransport transport,
         JsonFactory jsonFactory,
         String serviceAccountId, Collection<String> serviceAccountScopes, File p12File)
         throws GeneralSecurityException, IOException {
       return new GoogleCredential.Builder().setTransport(transport).setJsonFactory(jsonFactory)
           .setServiceAccountId(serviceAccountId).setServiceAccountScopes(serviceAccountScopes)
           .setServiceAccountPrivateKeyFromP12File(p12File).build();
     }
     

You can also use the service account flow to impersonate a user in a domain that you own. This is very similar to the service account flow above, but you additionally call Builder#setServiceAccountUser(String). Sample usage:
    
    
     public static GoogleCredential createCredentialForServiceAccountImpersonateUser
         (HttpTransport transport, JsonFactory jsonFactory, String serviceAccountId,
          Collection<String> serviceAccountScopes, File p12File,
          String serviceAccountUser) throws GeneralSecurityException, IOException {
       return new GoogleCredential.Builder()
           .setTransport(transport)
           .setJsonFactory(jsonFactory)
           .setServiceAccountId(serviceAccountId)
           .setServiceAccountScopes(serviceAccountScopes)
           .setServiceAccountPrivateKeyFromP12File(p12File)
           .setServiceAccountUser(serviceAccountUser)
           .build();
     }
     

If you need to persist the access token in a data store, use DataStoreFactory and Builder#addRefreshListener(CredentialRefreshListener) with DataStoreCredentialRefreshListener.

If you have a custom request initializer, request execute interceptor, or unsuccessful response handler, take a look at the sample usage for HttpExecuteInterceptor and HttpUnsuccessfulResponseHandler, which are interfaces that this class also implements.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.api.client.auth.oauth2.Credential > GoogleCredential

## Inherited Members

com.google.api.client.auth.oauth2.Credential.executeRefreshToken()

com.google.api.client.auth.oauth2.Credential.getAccessToken()

com.google.api.client.auth.oauth2.Credential.getClientAuthentication()

com.google.api.client.auth.oauth2.Credential.getClock()

com.google.api.client.auth.oauth2.Credential.getExpirationTimeMilliseconds()

com.google.api.client.auth.oauth2.Credential.getExpiresInSeconds()

com.google.api.client.auth.oauth2.Credential.getJsonFactory()

com.google.api.client.auth.oauth2.Credential.getMethod()

com.google.api.client.auth.oauth2.Credential.getRefreshListeners()

com.google.api.client.auth.oauth2.Credential.getRefreshToken()

com.google.api.client.auth.oauth2.Credential.getRequestInitializer()

com.google.api.client.auth.oauth2.Credential.getTokenServerEncodedUrl()

com.google.api.client.auth.oauth2.Credential.getTransport()

com.google.api.client.auth.oauth2.Credential.handleResponse(com.google.api.client.http.HttpRequest,com.google.api.client.http.HttpResponse,boolean)

com.google.api.client.auth.oauth2.Credential.initialize(com.google.api.client.http.HttpRequest)

com.google.api.client.auth.oauth2.Credential.intercept(com.google.api.client.http.HttpRequest)

com.google.api.client.auth.oauth2.Credential.refreshToken()

com.google.api.client.auth.oauth2.Credential.setAccessToken(java.lang.String)

com.google.api.client.auth.oauth2.Credential.setExpirationTimeMilliseconds(java.lang.Long)

com.google.api.client.auth.oauth2.Credential.setExpiresInSeconds(java.lang.Long)

com.google.api.client.auth.oauth2.Credential.setFromTokenResponse(com.google.api.client.auth.oauth2.TokenResponse)

com.google.api.client.auth.oauth2.Credential.setRefreshToken(java.lang.String)

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

### fromStream(InputStream credentialStream) (deprecated)
    
    
    public static GoogleCredential fromStream(InputStream credentialStream)

**Deprecated.** _This method is being deprecated because of a potential security risk. Please use {@link[GoogleCredentials](https://cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials) instead._

Beta   


Important: This method does not validate the credential configuration. A security risk holds when a credential configuration is accepted from a source that is not under your control and used without validation on your side.

If you are loading your credential configuration from an untrusted source and have not mitigated the risks (e.g. by validating the configuration yourself), make these changes as soon as possible to prevent security risks to your environment.

Regardless of the method used, it is always your responsibility to validate configurations received from external sources.

See the {@link [documentation](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials)} for more details.

Returns a credential defined by a Json file.

**Parameter**  
---  
**Name** | **Description**  
`credentialStream` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
the stream with the credential definition.  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` | the credential defined by the credentialStream.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created from the stream.  
  
### fromStream(InputStream credentialStream, HttpTransport transport, JsonFactory jsonFactory) (deprecated)
    
    
    public static GoogleCredential fromStream(InputStream credentialStream, HttpTransport transport, JsonFactory jsonFactory)

**Deprecated.** _This method is being deprecated because of a potential security risk. Please use {@link[GoogleCredentials](https://cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials) instead._

Beta   


Important: This method does not validate the credential configuration. A security risk holds when a credential configuration is accepted from a source that is not under your control and used without validation on your side.

If you are loading your credential configuration from an untrusted source and have not mitigated the risks (e.g. by validating the configuration yourself), make these changes as soon as possible to prevent security risks to your environment.

Regardless of the method used, it is always your responsibility to validate configurations received from external sources.

See the {@link [documentation](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials)} for more details.

Returns a credential defined by a Json file.

**Parameters**  
---  
**Name** | **Description**  
`credentialStream` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
the stream with the credential definition.  
`transport` | `com.google.api.client.http.HttpTransport`  
  
`jsonFactory` | `com.google.api.client.json.JsonFactory`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` | the credential defined by the credentialStream.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created from the stream.  
  
### getApplicationDefault() (deprecated)
    
    
    public static GoogleCredential getApplicationDefault()

Beta   
Returns the Application Default Credentials.

Returns the Application Default Credentials which are credentials that identify and authorize the whole application. This is the built-in service account if running on Google Compute Engine or the credentials file from the path in the environment variable GOOGLE_APPLICATION_CREDENTIALS.

**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` | the credential instance.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created in the current environment.  
  
### getApplicationDefault(HttpTransport transport, JsonFactory jsonFactory) (deprecated)
    
    
    public static GoogleCredential getApplicationDefault(HttpTransport transport, JsonFactory jsonFactory)

Beta   
Returns the Application Default Credentials.

Returns the Application Default Credentials which are credentials that identify and authorize the whole application. This is the built-in service account if running on Google Compute Engine or the credentials file from the path in the environment variable GOOGLE_APPLICATION_CREDENTIALS.

**Parameters**  
---  
**Name** | **Description**  
`transport` | `com.google.api.client.http.HttpTransport`  
the transport for Http calls.  
`jsonFactory` | `com.google.api.client.json.JsonFactory`  
the factory for Json parsing and formatting.  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` | the credential instance.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the credential cannot be created in the current environment.  
  
## Constructors 

### GoogleCredential() (deprecated)
    
    
    public GoogleCredential()

Constructor with the ability to access protected resources, but not refresh tokens.

To use with the ability to refresh tokens, use Builder.

### GoogleCredential(GoogleCredential.Builder builder) (deprecated)
    
    
    protected GoogleCredential(GoogleCredential.Builder builder)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[GoogleCredential.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder)`  
Google credential builder  
  
## Methods 

### createDelegated(String user) (deprecated)
    
    
    public GoogleCredential createDelegated(String user)

Beta   
For service accounts that need to delegate to a specific user, create a copy of the credential with the specified user.

**Parameter**  
---  
**Name** | **Description**  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
  
### createScoped(Collection<String> scopes) (deprecated)
    
    
    public GoogleCredential createScoped(Collection<String> scopes)

Beta   
For credentials that require scopes, creates a copy of the credential with the specified scopes.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
  
### createScopedRequired() (deprecated)
    
    
    public boolean createScopedRequired()

Beta   
Indicates whether the credential requires scopes to be specified by calling createScoped before use.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### executeRefreshToken() (deprecated)
    
    
    protected TokenResponse executeRefreshToken()

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.auth.oauth2.TokenResponse` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.executeRefreshToken()

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getServiceAccountId() (deprecated)
    
    
    public final String getServiceAccountId()

Returns the service account ID (typically an e-mail address) or `null` if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServiceAccountPrivateKey() (deprecated)
    
    
    public final PrivateKey getServiceAccountPrivateKey()

Returns the private key to use with the service account flow or `null` if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[PrivateKey](https://docs.oracle.com/javase/8/docs/api/java/security/PrivateKey.html)` |   
  
### getServiceAccountPrivateKeyId() (deprecated)
    
    
    public final String getServiceAccountPrivateKeyId()

Beta   
Returns the ID of the private key to use with the service account flow or `null` if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServiceAccountProjectId() (deprecated)
    
    
    public final String getServiceAccountProjectId()

Returns the service account Project ID or `null` if not present, either because this is not using the service account flow, or is using an older version of the service account configuration.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServiceAccountScopes() (deprecated)
    
    
    public final Collection<String> getServiceAccountScopes()

Returns a collection of OAuth scopes to use with the service account flow or `null` if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getServiceAccountScopesAsString() (deprecated)
    
    
    public final String getServiceAccountScopesAsString()

Returns the space-separated OAuth scopes to use with the service account flow or `null` if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServiceAccountUser() (deprecated)
    
    
    public final String getServiceAccountUser()

Returns the email address of the user the application is trying to impersonate in the service account flow or `null` for none or if not using the service account flow.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### setAccessToken(String accessToken) (deprecated)
    
    
    public GoogleCredential setAccessToken(String accessToken)

**Parameter**  
---  
**Name** | **Description**  
`accessToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.setAccessToken(java.lang.String)

### setExpirationTimeMilliseconds(Long expirationTimeMilliseconds) (deprecated)
    
    
    public GoogleCredential setExpirationTimeMilliseconds(Long expirationTimeMilliseconds)

**Parameter**  
---  
**Name** | **Description**  
`expirationTimeMilliseconds` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.setExpirationTimeMilliseconds(java.lang.Long)

### setExpiresInSeconds(Long expiresIn) (deprecated)
    
    
    public GoogleCredential setExpiresInSeconds(Long expiresIn)

**Parameter**  
---  
**Name** | **Description**  
`expiresIn` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.setExpiresInSeconds(java.lang.Long)

### setFromTokenResponse(TokenResponse tokenResponse) (deprecated)
    
    
    public GoogleCredential setFromTokenResponse(TokenResponse tokenResponse)

**Parameter**  
---  
**Name** | **Description**  
`tokenResponse` | `com.google.api.client.auth.oauth2.TokenResponse`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.setFromTokenResponse(com.google.api.client.auth.oauth2.TokenResponse)

### setRefreshToken(String refreshToken) (deprecated)
    
    
    public GoogleCredential setRefreshToken(String refreshToken)

**Parameter**  
---  
**Name** | **Description**  
`refreshToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential)` |   
**Overrides**

com.google.api.client.auth.oauth2.Credential.setRefreshToken(java.lang.String)

### toBuilder() (deprecated)
    
    
    public GoogleCredential.Builder toBuilder()

Beta   
Create a builder from this credential.

**Returns**  
---  
**Type** | **Description**  
`[GoogleCredential.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
