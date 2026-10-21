---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService
title: Interface BackendService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:12.966386+00:00
---

# Interface BackendService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface BackendService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface BackendService

[BackendService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService) allows you to retrieve information about backend servers. Backend servers are long running addressable servers that can be used for applications that need to keep persistent state in ram between requests. 

This API is deprecated and has been replaced by [com.google.appengine.api.modules.ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService). Please update your code as soon as possible. See the modules documentation for more information: <https://developers.google.com/appengine/docs/java/modules/converting>

This API allows you to retrieve information about the backend handling the current request. It also allows you to to get the address of a specific backend instance in such a way that a local server is used during development and a production server is used in production.

## Static Fields 

### BACKEND_ID_ENV_ATTRIBUTE
    
    
    public static final String BACKEND_ID_ENV_ATTRIBUTE

Environment attribute key where the backend name is stored. See Also: [BackendService#getCurrentBackend()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService#com_google_appengine_api_backends_BackendService_getCurrentBackend__)

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### DEVAPPSERVER_PORTMAPPING_KEY
    
    
    public static final String DEVAPPSERVER_PORTMAPPING_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTANCE_ID_ENV_ATTRIBUTE
    
    
    public static final String INSTANCE_ID_ENV_ATTRIBUTE

Environment attribute key where the instance id is stored. See Also: [BackendService#getCurrentInstance()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService#com_google_appengine_api_backends_BackendService_getCurrentInstance__)

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_HEADER_BACKEND_REDIRECT
    
    
    public static final String REQUEST_HEADER_BACKEND_REDIRECT

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### REQUEST_HEADER_INSTANCE_REDIRECT
    
    
    public static final String REQUEST_HEADER_INSTANCE_REDIRECT

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Methods 

### getBackendAddress(String backend)
    
    
    public abstract String getBackendAddress(String backend)

Get the address of a specific backend in such a way that a local server is used during development and a production server is used in production.

**Parameter**  
---  
**Name** | **Description**  
`backend` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the backend  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The address of the backend  
  
### getBackendAddress(String backend, int instance)
    
    
    public abstract String getBackendAddress(String backend, int instance)

Get the address of a specific backend instance in such a way that a local instance is used during development and a production server instance is used in production.

**Parameters**  
---  
**Name** | **Description**  
`backend` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the backend  
`instance` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The instance id  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The address of the backend instance  
  
### getCurrentBackend()
    
    
    public abstract String getCurrentBackend()

Get the name of the backend handling the current request.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name of the backend or null if the request is not handled by a backend.  
  
### getCurrentInstance()
    
    
    public abstract int getCurrentInstance()

Get the instance handling the current request.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The instance id or -1 if the request is not handled by a backend.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
