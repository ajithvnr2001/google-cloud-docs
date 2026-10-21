---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.quota.QuotaService
title: Interface QuotaService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:02.882314+00:00
---

# Interface QuotaService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.quota.QuotaService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface QuotaService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface QuotaService

The `QuotaService` provides measurement of API and CPU usage during requests.

## Methods 

### convertCpuSecondsToMegacycles(double cpuSeconds)
    
    
    public abstract long convertCpuSecondsToMegacycles(double cpuSeconds)

Expresses a value in megaCycles as its approximate equivalent of CPU seconds on a theoretical 1.2 GHz CPU.

**Parameter**  
---  
**Name** | **Description**  
`cpuSeconds` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the value, in cpu seconds, to convert.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a long representing the megacycles the input CPU-seconds value converts to.  
  
### convertMegacyclesToCpuSeconds(long megaCycles)
    
    
    public abstract double convertMegacyclesToCpuSeconds(long megaCycles)

Expresses a value in megaCycles as its approximate equivalent of CPU seconds on a theoretical 1.2 GHz CPU.

**Parameter**  
---  
**Name** | **Description**  
`megaCycles` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the value, in megacycles, to convert.  
**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a double representing the CPU-seconds the input megacycle value converts to.  
  
### getApiTimeInMegaCycles() (deprecated)
    
    
    public abstract long getApiTimeInMegaCycles()

**Deprecated.** _This value is no longer meaningful._

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the overall amount spent in API cycles, as returned by the system. Returns 0 if the feature is not supported.  
  
### getCpuTimeInMegaCycles()
    
    
    public abstract long getCpuTimeInMegaCycles()

Measures the duration that the current request has spent so far processing the request within the App Engine sandbox. Note that time spent in API calls will not be added to this value. 

The unit the duration is measured is Megacycles. If all instructions were to be executed sequentially on a standard 1.2 GHz 64-bit x86 CPU, 1200 megacycles would equate to one second physical time elapsed.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the overall amount spent in CPU cycles, as returned by the system. Returns 0 if the feature is not supported.  
  
### supports(QuotaService.DataType type)
    
    
    public abstract boolean supports(QuotaService.DataType type)

Tests if the QuotaService can provide a certain kind of data at this point in time. Depending on the underlying app server implementation and what state it is in, a QuotaService might not always have access to all categories of data. For example, the dev-appserver might not be able to measure the megacycles of api calls. Trying to access that data would lead to an IllegalStateException, which would then need to be handled. To make it easier to prevent this, it is possible to ask the service if a particular kind of data is supported.

**Parameter**  
---  
**Name** | **Description**  
`type` | `[QuotaService.DataType](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.quota.QuotaService.DataType)`  
the type of data in question.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if the QuotaService can provide such data at this time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
