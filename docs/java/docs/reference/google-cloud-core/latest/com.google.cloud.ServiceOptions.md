---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions
title: Class ServiceOptions<ServiceT,OptionsT> (2.77.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:51.801219+00:00
---

# Class ServiceOptions<ServiceT,OptionsT> (2.77.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ServiceOptions<ServiceT,OptionsT> (2.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.77.0 (latest)  2.73.0  2.72.0  2.71.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.1  2.63.1  2.62.2  2.61.0  2.60.3  2.59.0  2.58.2  2.57.0  2.56.0  2.55.0  2.53.1  2.52.0  2.51.0  2.50.0  2.49.1  2.48.0  2.47.0  2.45.0  2.44.1  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.1  2.37.0  2.36.1  2.35.0  2.33.0  2.32.0  2.31.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.1  2.23.0  2.22.1  2.21.1  2.20.1  2.13.0  2.12.0  2.11.0  2.9.4  2.8.27  2.7.1  2.6.1  2.5.11  2.4.0  2.3.5 
    
    
    public abstract class ServiceOptions<ServiceT,OptionsT> implements Serializable

Abstract class representing service options.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ServiceOptions<ServiceT,OptionsT>

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

## Type Parameters  
  
---  
**Name** | **Description**  
`ServiceT` |   
`OptionsT` |   
  
## Static Fields 

### CREDENTIAL_ENV_NAME
    
    
    public static final String CREDENTIAL_ENV_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### <T>getFromServiceLoader(Class<? extends T> clazz, T defaultInstance)
    
    
    public static T <T>getFromServiceLoader(Class<? extends T> clazz, T defaultInstance)

**Internal Only** : This feature is not stable for application use.

**Parameters**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends T>`  
  
`defaultInstance` | `T`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### <T>newInstance(String className)
    
    
    public static T <T>newInstance(String className)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`className` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
`[ClassNotFoundException](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassNotFoundException.html)` |   
  
### getAppEngineAppId()
    
    
    public static String getAppEngineAppId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAppEngineProjectId()
    
    
    protected static String getAppEngineProjectId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAppEngineProjectIdFromAppId()
    
    
    protected static String getAppEngineProjectIdFromAppId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultProjectId()
    
    
    public static String getDefaultProjectId()

Returns the default project ID, or `null` if no default project ID could be found. This method returns the first available project ID among the following sources:

  1. The project ID specified by the GOOGLE_CLOUD_PROJECT environment variable 
  2. The App Engine project ID 
  3. The project ID specified in the JSON credentials file pointed by the ` GOOGLE_APPLICATION_CREDENTIALS` environment variable 
  4. The Google Cloud SDK project ID 
  5. The Compute Engine project ID 



**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultRetrySettings()
    
    
    public static RetrySettings getDefaultRetrySettings()

**Returns**  
---  
**Type** | **Description**  
`[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)` |   
  
### getGoogApiClientLibName()
    
    
    public static String getGoogApiClientLibName()

Returns the library's name used by x-goog-api-client header as a string.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGoogleCloudProjectId()
    
    
    protected static String getGoogleCloudProjectId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLibraryName()
    
    
    public static String getLibraryName()

Returns the library's name, `gcloud-java`, as a string.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getNoRetrySettings()
    
    
    public static RetrySettings getNoRetrySettings()

**Returns**  
---  
**Type** | **Description**  
`[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)` |   
  
### getServiceAccountProjectId()
    
    
    protected static String getServiceAccountProjectId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Constructors 

### ServiceOptions(Class<? extends ServiceFactory<ServiceT,OptionsT>> serviceFactoryClass, Class<? extends ServiceRpcFactory<OptionsT>> rpcFactoryClass, ServiceOptions.Builder<ServiceT,OptionsT,?> builder, ServiceDefaults<ServiceT,OptionsT> serviceDefaults)
    
    
    protected ServiceOptions(Class<? extends ServiceFactory<ServiceT,OptionsT>> serviceFactoryClass, Class<? extends ServiceRpcFactory<OptionsT>> rpcFactoryClass, ServiceOptions.Builder<ServiceT,OptionsT,?> builder, ServiceDefaults<ServiceT,OptionsT> serviceDefaults)

**Internal Only** : This feature is not stable for application use.

_This class should only be extended within google-cloud-java_

**Parameters**  
---  
**Name** | **Description**  
`serviceFactoryClass` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends com.google.cloud.ServiceFactory<ServiceT,OptionsT>>`  
  
`rpcFactoryClass` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends com.google.cloud.spi.ServiceRpcFactory<OptionsT>>`  
  
`builder` | `[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.Builder)<ServiceT,OptionsT,?>`  
  
`serviceDefaults` | `[ServiceDefaults](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceDefaults)<ServiceT,OptionsT>`  
  
  
## Fields 

### clientLibToken
    
    
    protected final String clientLibToken

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### credentials
    
    
    protected Credentials credentials

**Field Value**  
---  
**Type** | **Description**  
`com.google.auth.Credentials` |   
  
## Methods 

### <B>toBuilder()
    
    
    public abstract B <B>toBuilder()

**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### baseEquals(ServiceOptions<?,?> other)
    
    
    protected boolean baseEquals(ServiceOptions<?,?> other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions)<?,?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### baseHashCode()
    
    
    protected int baseHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### defaultRetrySettings()
    
    
    protected RetrySettings defaultRetrySettings()

Some services may have different backoff requirements listed in their SLAs. Be sure to override this method in options subclasses when the service's backoff requirement differs from the default parameters listed in [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).

**Returns**  
---  
**Type** | **Description**  
`[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)` |   
  
### getApiTracerFactory()
    
    
    public ApiTracerFactory getApiTracerFactory()

**Returns**  
---  
**Type** | **Description**  
`[ApiTracerFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.tracing.ApiTracerFactory.html)` |   
  
### getApplicationName()
    
    
    public String getApplicationName()

Returns the application's name as a string in the format `gcloud-java/[version]`, optionally prepended with externally supplied User-Agent header value (via setting custom header provider).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getClientLibToken()
    
    
    public String getClientLibToken()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getClock()
    
    
    public ApiClock getClock()

Returns the service's clock. Default time source uses System#currentTimeMillis() to get current time.

**Returns**  
---  
**Type** | **Description**  
`[ApiClock](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiClock.html)` |   
  
### getCredentials()
    
    
    public Credentials getCredentials()

Returns the authentication credentials.

**Returns**  
---  
**Type** | **Description**  
`com.google.auth.Credentials` |   
  
### getDefaultHost()
    
    
    protected String getDefaultHost()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultProject()
    
    
    protected String getDefaultProject()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHost()
    
    
    public String getHost()

Returns the service host.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLibraryVersion()
    
    
    public String getLibraryVersion()

Returns the library's version as a string.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMergedHeaderProvider(HeaderProvider internalHeaderProvider)
    
    
    public final HeaderProvider getMergedHeaderProvider(HeaderProvider internalHeaderProvider)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`internalHeaderProvider` | `[HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html)` |   
  
### getProjectId()
    
    
    public String getProjectId()

Returns the project ID. Return value can be null (for services that don't require a project ID).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getQuotaProjectId()
    
    
    public String getQuotaProjectId()

Returns the quotaProjectId that specifies the project used for quota and billing purposes.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResolvedApiaryHost(String serviceName)
    
    
    public String getResolvedApiaryHost(String serviceName)

**Internal Only** : This feature is not stable for application use.

Returns a host value to be used for BigQuery and Storage Apiary Wrapped Libraries. To be removed in the future when Apiary clients can resolve their endpoints. Returns the host to be used as the rootUrl.

The resolved host will be in `https://{serviceName}.{resolvedUniverseDomain}/` format. The resolvedUniverseDomain will be set to `googleapis.com` if universeDomain is null.

The host value is set to DEFAULT_HOST if the user didn't configure a host. Returns the host value the user set, otherwise constructs the host for the user. See Also: [rootUrl](https://github.com/googleapis/google-api-java-client/blob/76765d5f9689be9d266a7d62fa6ffb4cabf701f5/google-api-client/src/main/java/com/google/api/client/googleapis/services/AbstractGoogleClient.java#L49)

**Parameter**  
---  
**Name** | **Description**  
`serviceName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResolvedHost(String serviceName)
    
    
    public String getResolvedHost(String serviceName)

**Internal Only** : This feature is not stable for application use.

Returns the resolved host for the Service to connect to Google Cloud

The resolved host will be in `https://{serviceName}.{resolvedUniverseDomain}` format. The resolvedUniverseDomain will be set to `googleapis.com` if universeDomain is null. The format is similar to the DEFAULT_HOST value in java-core. See Also: [DEFAULT_HOST](https://github.com/googleapis/google-cloud-java/blob/e50b96b70826f173e6d23278fea96c2af9b6e817/sdk-platform-java/java-core/google-cloud-core/src/main/java/com/google/cloud/ServiceOptions.java#L86)

**Parameter**  
---  
**Name** | **Description**  
`serviceName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRetrySettings()
    
    
    public RetrySettings getRetrySettings()

Returns configuration parameters for request retries.

**Returns**  
---  
**Type** | **Description**  
`[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html)` |   
  
### getRpc()
    
    
    public ServiceRpc getRpc()

Returns a Service RPC object for the current service. For instance, when using Google Cloud Storage, it returns a StorageRpc object.

**Returns**  
---  
**Type** | **Description**  
`[ServiceRpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceRpc)` |   
  
### getScopedCredentials()
    
    
    public Credentials getScopedCredentials()

Returns the authentication credentials. If required, credentials are scoped.

**Returns**  
---  
**Type** | **Description**  
`com.google.auth.Credentials` |   
  
### getScopes()
    
    
    protected abstract Set<String> getScopes()

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getService()
    
    
    public ServiceT getService()

Returns a Service object for the current service. For instance, when using Google Cloud Storage, it returns a Storage object.

**Returns**  
---  
**Type** | **Description**  
`ServiceT` |   
  
### getTransportOptions()
    
    
    public TransportOptions getTransportOptions()

Returns the transport-specific options for this service.

**Returns**  
---  
**Type** | **Description**  
`[TransportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.TransportOptions)` |   
  
### getUniverseDomain()
    
    
    public String getUniverseDomain()

Universe Domain is the domain for Google Cloud Services. A Google Cloud endpoint follows the format of `{ServiceName}.{UniverseDomain}`. For example, speech.googleapis.com would have a Universe Domain value of `googleapis.com` and cloudasset.test.com would have a Universe Domain of `test.com`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The universe domain value set in the Builder's setter. This is not the resolved Universe Domain  
  
### getUseJwtAccessWithScope()
    
    
    public boolean getUseJwtAccessWithScope()

Returns true when self-signed JWT with scopes are used for service account credentials.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true when self-signed JWT with scopes are used  
  
### getUserAgent()
    
    
    public final String getUserAgent()

**Internal Only** : This feature is not stable for application use.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasValidUniverseDomain()
    
    
    public boolean hasValidUniverseDomain()

**Internal Only** : This feature is not stable for application use.

Validates that Credentials' Universe Domain matches the resolved Universe Domain. Currently, this is only intended for BigQuery and Storage Apiary Wrapped Libraries.

This validation call should be made prior to any RPC invocation. This call is used to gate the RPC invocation if there is no valid universe domain.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### projectIdRequired()
    
    
    protected boolean projectIdRequired()

Returns whether a service requires a project ID. This method may be overridden in service-specific Options objects.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if a project ID is required to use the service, false if not  
  
### shouldRefreshRpc(ServiceRpc cachedRpc)
    
    
    protected boolean shouldRefreshRpc(ServiceRpc cachedRpc)

**Parameter**  
---  
**Name** | **Description**  
`cachedRpc` | `[ServiceRpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceRpc)`  
The currently cached service object  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if the currently cached service object should be refreshed.  
  
### shouldRefreshService(ServiceT cachedService)
    
    
    protected boolean shouldRefreshService(ServiceT cachedService)

**Parameter**  
---  
**Name** | **Description**  
`cachedService` | `ServiceT`  
The currently cached service object  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if the currently cached service object should be refreshed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
