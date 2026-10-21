---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService
title: Interface ModulesService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:07:46.006990+00:00
---

# Interface ModulesService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface ModulesService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface ModulesService

ModulesService allows the application to fetch information about its own module and version information. Additionally, the service has the ability to start, stop and change the number of instances associated with a module version.

## Methods 

### getCurrentInstanceId()
    
    
    public abstract String getCurrentInstanceId()

Get the id of the current instance.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | current instance id  
  
### getCurrentModule()
    
    
    public abstract String getCurrentModule()

Get the name of the current module. ("default" if modules are not enabled for this app)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the name of the module  
  
### getCurrentVersion()
    
    
    public abstract String getCurrentVersion()

Get the name of the current version.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the name of the version  
  
### getDefaultVersion(String module)
    
    
    public abstract String getDefaultVersion(String module)

Returns the name of the default version for the module.

**Parameter**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null for the current module  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getInstanceHostname(String module, String version, String instance)
    
    
    public abstract String getInstanceHostname(String module, String version, String instance)

Returns a host name to use for the given module, version and instance.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null to indicate the current module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version or null to indicate the current version  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the id of a particular instance to address  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the hostname of the given instance  
  
### getModules()
    
    
    public abstract Set<String> getModules()

Get the set of modules that are available to the application.

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | Set of modules available to the application  
  
### getNumInstances(String module, String version)
    
    
    public abstract int getNumInstances(String module, String version)

Returns the number of instances that are available to the given manual scaling module version.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null for the current module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version or null for the current version  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVersionHostname(String module, String version)
    
    
    public abstract String getVersionHostname(String module, String version)

Returns a host name to use for the given module and version.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null to indicate the current module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version or null to indicate the current version  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getVersions(String module)
    
    
    public abstract Set<String> getVersions(String module)

Returns the set of versions that are available to the given module.

**Parameter**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null for the current module  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### setNumInstances(String module, String version, long instances)
    
    
    public abstract void setNumInstances(String module, String version, long instances)

Set the number of instances that are available to the given manual scaling module version. Changing the number of instances is an asynchronous process so this may return before added instances begin serving or removed instances stop serving.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null for the current module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version or null for the current version  
`instances` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of instances to set  
  
### setNumInstancesAsync(String module, String version, long instances)
    
    
    public abstract Future<Void> setNumInstancesAsync(String module, String version, long instances)

Starts an asynchronous call to [#setNumInstances](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService#com_google_appengine_api_modules_ModulesService_setNumInstances_) and returns a [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) to obtain its eventual result. When the returned [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) yields a successful result [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService) will have successfully initiated the process of setting the number of instances. There may be some delay before added instances start serving or removed instances stop serving.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`instances` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### startVersion(String module, String version)
    
    
    public abstract void startVersion(String module, String version)

Starts the given manual scaling or basic scaling module version. Starting a version is an asynchronous process so this may return before the started version is serving. If the requested module version is already started this returns without error.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version  
  
### startVersionAsync(String module, String version)
    
    
    public abstract Future<Void> startVersionAsync(String module, String version)

Starts an asynchronous call to [#startVersion](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService#com_google_appengine_api_modules_ModulesService_startVersion_) and returns a [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) to obtain its eventual result. When the returned [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) yields a successful result [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService) will have successfully initiated the process of starting the requested version. There may be some delay before the version starts serving.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### stopVersion(String module, String version)
    
    
    public abstract void stopVersion(String module, String version)

Stops the given manual scaling or basic scaling module version. Stopping a version is an asynchronous process so this may return before the stopped version stops serving. If the requested module version is already stopped this returns without error.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the module or null for the current module  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the version or null for the current version  
  
### stopVersionAsync(String module, String version)
    
    
    public abstract Future<Void> stopVersionAsync(String module, String version)

Starts an asynchronous call to [#stopVersion](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService#com_google_appengine_api_modules_ModulesService_stopVersion_) and returns a [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) to obtain its eventual result. When the returned [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) yields a successful result [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService) will have successfully initiated the process of stopping the requested version. There may be some delay before the version stops serving.

**Parameters**  
---  
**Name** | **Description**  
`module` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`version` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
