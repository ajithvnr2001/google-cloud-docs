---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig
title: Class CloudDatastoreRemoteServiceConfig (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:50.441369+00:00
---

# Class CloudDatastoreRemoteServiceConfig (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class CloudDatastoreRemoteServiceConfig (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class CloudDatastoreRemoteServiceConfig

User-configurable global properties of Cloud Datastore.

Code not running in App Engine Standard can use the Cloud Datastore API by making a single call to [#setConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_setConfig_) before accessing any other classes from [com.google.appengine.api](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api). For example:
    
    
     public static void main(Strings[] args) {
       CloudDatastoreRemoteServiceConfig config = CloudDatastoreRemoteServiceConfig.builder()
           .appId(AppId.create(Location.US_CENTRAL, "my-project-id"))
           .build();
       CloudDatastoreRemoteServiceConfig.setConfig(config);
       DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
       ...
     }
     

Outside of tests, the config should not be cleared once it has been set. In tests, the config can be cleared by calling [#clear](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_clear_):
    
    
     {@literal @}Before
     public void before() {
       CloudDatastoreRemoteServiceConfig config = CloudDatastoreRemoteServiceConfig.builder()
           .appId(AppId.create(Location.US_CENTRAL, "my-project-id"))
           .emulatorHost(...)
           .build();
       CloudDatastoreRemoteServiceConfig.setConfig(config);
     }
    
     {@literal @}After
     public void after() {
       CloudDatastoreRemoteServiceConfig.clear();
     }
     

By default, this configuration uses [application-default credentials](https://developers.google.com/identity/protocols/application-default-credentials).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudDatastoreRemoteServiceConfig

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

## Static Methods 

### builder()
    
    
    public static CloudDatastoreRemoteServiceConfig.Builder builder()

Returns a [CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder).

**Returns**  
---  
**Type** | **Description**  
`[CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)` |   
  
### clear()
    
    
    public static void clear()

Clears the [CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig) instance (if one has been set) as well as the [ApiProxy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy)'s EnvironmentFactory and the Environment for the current thread.

This method should only be called in tests.

### setConfig(CloudDatastoreRemoteServiceConfig config)
    
    
    public static void setConfig(CloudDatastoreRemoteServiceConfig config)

Sets the [CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig) instance.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig)`  
  
  
## Constructors 

### CloudDatastoreRemoteServiceConfig()
    
    
    public CloudDatastoreRemoteServiceConfig()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
