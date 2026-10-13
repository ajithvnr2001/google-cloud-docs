---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder
title: Class CloudDatastoreRemoteServiceConfig.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:23.936029+00:00
---

# Class CloudDatastoreRemoteServiceConfig.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class CloudDatastoreRemoteServiceConfig.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract static class CloudDatastoreRemoteServiceConfig.Builder

Builder for [CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudDatastoreRemoteServiceConfig.Builder

## Inherited Members

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

## Constructors 

### Builder()
    
    
    public Builder()

## Methods 

### accessToken(String accessToken)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder accessToken(String accessToken)

Sets the access token.

Cannot be combined with a call to [#useComputeEngineCredential(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_useComputeEngineCredential_boolean_) or [#useServiceAccountCredential(String, PrivateKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_useServiceAccountCredential_java_lang_String_java_security_PrivateKey_).

**Parameter**  
---  
**Name** | **Description**  
`accessToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### additionalAppIds(Set<CloudDatastoreRemoteServiceConfig.AppId> value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder additionalAppIds(Set<CloudDatastoreRemoteServiceConfig.AppId> value)

Provides a set of additional app IDs that may appear in [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) values in entities.

This is only required if the client will read entities containing [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) values that contain app IDs other than the one provided to [#appId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_appId_). Any such app IDs should be provided to this method.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[AppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.AppId)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### appId(CloudDatastoreRemoteServiceConfig.AppId value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder appId(CloudDatastoreRemoteServiceConfig.AppId value)

Sets the [AppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.AppId) of the Cloud Datastore instance to call. Required.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CloudDatastoreRemoteServiceConfig.AppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.AppId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### asyncStackTraceCaptureEnabled(boolean value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder asyncStackTraceCaptureEnabled(boolean value)

If set to true, stacktrace for async calls is captured and returned as part of error messages. There is overhead in capturing this stack trace and it is recommended to enable it primarily for debugging.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### build()
    
    
    public CloudDatastoreRemoteServiceConfig build()

**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig)` |   
  
### emulatorHost(String value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder emulatorHost(String value)

Instructs the client to connect to a locally-running Cloud Datastore Emulator and not to pass credentials.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### hostOverride(String value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder hostOverride(String value)

Overrides the host (e.g. `datastore.googleapis.com`) used to contact the Cloud Datastore API. To connect to the Cloud Datastore Emulator, use [#emulatorHost](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_emulatorHost_) instead.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### httpConnectTimeoutMillis(int value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder httpConnectTimeoutMillis(int value)

Sets the HTTP connect timeout in milliseconds.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### installApiProxyEnvironment(boolean value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder installApiProxyEnvironment(boolean value)

If set to true, a minimal Environment will be installed (if none is already installed).

If set to false, no attempt to install an environment will be made and the user must install it instead. At a minimum, such an environment must provide implementations for Environment#getAppId(), Environment#getAttributes(), and Environment#getRemainingMillis().

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### maxRetries(int value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder maxRetries(int value)

Sets the maximum number of retries for underlying HTTP connect exceptions.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### useComputeEngineCredential(boolean value)
    
    
    public abstract CloudDatastoreRemoteServiceConfig.Builder useComputeEngineCredential(boolean value)

If set to true, always use a Compute Engine credential instead of using the Application Default Credentials library to construct the credential.

Cannot be combined with a call to [#useServiceAccountCredential(String, PrivateKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_useServiceAccountCredential_java_lang_String_java_security_PrivateKey_) or [#accessToken(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_accessToken_java_lang_String_).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### useServiceAccountCredential(String serviceAccountId, PrivateKey privateKey)
    
    
    public CloudDatastoreRemoteServiceConfig.Builder useServiceAccountCredential(String serviceAccountId, PrivateKey privateKey)

Instructs the client to use a service account credential instead of using the Application Default Credentials library to construct the credential.

Cannot be combined with a call to [#useComputeEngineCredential(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_useComputeEngineCredential_boolean_) or [#accessToken(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_Builder_accessToken_java_lang_String_).

**Parameters**  
---  
**Name** | **Description**  
`serviceAccountId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`privateKey` | `[PrivateKey](https://docs.oracle.com/javase/8/docs/api/java/security/PrivateKey.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
