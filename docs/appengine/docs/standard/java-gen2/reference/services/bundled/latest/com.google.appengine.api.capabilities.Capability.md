---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability
title: Class Capability (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:40.019689+00:00
---

# Class Capability (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Capability (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class Capability

A capability represents a particular feature or set of features available on the App Engine platform.

To check the availability of a particular capability, use the [CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService) API.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Capability

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

## Static Fields 

### BLOBSTORE (deprecated)
    
    
    public static final Capability BLOBSTORE

**Deprecated.** _This service will always be reported as being available._

Availability of BlobstoreService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### DATASTORE (deprecated)
    
    
    public static final Capability DATASTORE

**Deprecated.** _This service will always be reported as being available. If_

Availability of the datastore.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### DATASTORE_WRITE
    
    
    public static final Capability DATASTORE_WRITE

Availability of datastore writes.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### IMAGES
    
    
    public static final Capability IMAGES

Availability of the ImagesService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### MAIL
    
    
    public static final Capability MAIL

Availability of theMailService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### MEMCACHE
    
    
    public static final Capability MEMCACHE

Availability ofMemcacheService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### PROSPECTIVE_SEARCH
    
    
    public static final Capability PROSPECTIVE_SEARCH

Availability of the ProspectiveSearchService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### TASKQUEUE
    
    
    public static final Capability TASKQUEUE

Availability of TaskQueueService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### URL_FETCH
    
    
    public static final Capability URL_FETCH

Availability of the URLFetchService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
### XMPP
    
    
    public static final Capability XMPP

Availability of the XMPPService.

**Field Value**  
---  
**Type** | **Description**  
`[Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)` |   
  
## Constructors 

### Capability(String packageName)
    
    
    public Capability(String packageName)

Creates a new instance of a Capability.

**Parameter**  
---  
**Name** | **Description**  
`packageName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the package associated with this capability.  
  
### Capability(String packageName, String name)
    
    
    public Capability(String packageName, String name)

Creates a new instance of a Capability.

**Parameters**  
---  
**Name** | **Description**  
`packageName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the package associated with this capability.  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the capability.  
  
## Methods 

### equals(Object x)
    
    
    public boolean equals(Object x)

**Parameter**  
---  
**Name** | **Description**  
`x` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getName()
    
    
    public String getName()

Returns the name associated with this capability.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the name associated with this capability.  
  
### getPackageName()
    
    
    public String getPackageName()

Returns the package name associated with this capability.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the package name associated with this capability.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
