---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Builder
title: Class LogQuery.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:53:53.239916+00:00
---

# Class LogQuery.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class LogQuery.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class LogQuery.Builder

Contains static creation methods for [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogQuery.Builder

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

### withBatchSize(int batchSize)
    
    
    public static LogQuery withBatchSize(int batchSize)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given batch size. Shorthand for `LogQuery.Builder.withDefaults().batchSize(batchSize);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how batch size is used.

**Parameter**  
---  
**Name** | **Description**  
`batchSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the batch size to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withDefaults()
    
    
    public static LogQuery withDefaults()

Helper method for creating a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) instance with default values. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of the defaults.

**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` |   
  
### withEndTimeMillis(long endTimeMillis)
    
    
    public static LogQuery withEndTimeMillis(long endTimeMillis)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given end time. Shorthand for ` LogQuery.Builder.withDefaults().endTimeMillis(endTimeMillis);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how end time is used.

**Parameter**  
---  
**Name** | **Description**  
`endTimeMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the end time to use, in milliseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withEndTimeUsec(long endTimeUsec)
    
    
    public static LogQuery withEndTimeUsec(long endTimeUsec)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given end time. Shorthand for `LogQuery.Builder.withDefaults().endTimeUsec(endTimeUsec);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how end time is used.

**Parameter**  
---  
**Name** | **Description**  
`endTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the start time to use, in microseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withIncludeAppLogs(boolean includeAppLogs)
    
    
    public static LogQuery withIncludeAppLogs(boolean includeAppLogs)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with include application logs set. Shorthand for `LogQuery.Builder.withDefaults().includeAppLogs(includeAppLogs);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of the include application logs setting.

**Parameter**  
---  
**Name** | **Description**  
`includeAppLogs` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the inclusion value to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withIncludeIncomplete(boolean includeIncomplete)
    
    
    public static LogQuery withIncludeIncomplete(boolean includeIncomplete)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given include incomplete setting. Shorthand for `LogQuery.Builder.withDefaults().includeIncomplete(includeIncomplete);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how include incomplete is used.

**Parameter**  
---  
**Name** | **Description**  
`includeIncomplete` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the inclusion value to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withMajorVersionIds(List<String> versionIds)
    
    
    public static LogQuery withMajorVersionIds(List<String> versionIds)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given major version IDs. Shorthand for `LogQuery.Builder.withDefaults().majorVersionIds(versionIds);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how the list of major version ids is used.

**Parameter**  
---  
**Name** | **Description**  
`versionIds` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the major version id list to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withMinLogLevel(LogService.LogLevel minLogLevel)
    
    
    public static LogQuery withMinLogLevel(LogService.LogLevel minLogLevel)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given minimum log level. Shorthand for `LogQuery.Builder.withDefaults().minLogLevel(minLogLevel);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how minimum log level is used.

**Parameter**  
---  
**Name** | **Description**  
`minLogLevel` | `[LogService.LogLevel](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService.LogLevel)`  
the minimum log level to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withOffset(String offset)
    
    
    public static LogQuery withOffset(String offset)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given offset. Shorthand for `LogQuery.Builder.withDefaults().offset(offset);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how offsets are used.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the offset to use.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withRequestIds(List<String> requestIds)
    
    
    public static LogQuery withRequestIds(List<String> requestIds)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given request IDs. Shorthand for `LogQuery.Builder.withDefaults().requestIds(requestIds);`. See the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how the list of request ids is used.

**Parameter**  
---  
**Name** | **Description**  
`requestIds` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the request id list to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withStartTimeMillis(long startTimeMillis)
    
    
    public static LogQuery withStartTimeMillis(long startTimeMillis)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given start time. Shorthand for `LogQuery.Builder.withDefaults().startTimeMillis(startTimeMillis);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how start time is used.

**Parameter**  
---  
**Name** | **Description**  
`startTimeMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the start time to use, in milliseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withStartTimeUsec(long startTimeUsec)
    
    
    public static LogQuery withStartTimeUsec(long startTimeUsec)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given start time. Shorthand for `LogQuery.Builder.withDefaults().startTimeUsec(startTimeUsec);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for an explanation of how start time is used.

**Parameter**  
---  
**Name** | **Description**  
`startTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the start time to use, in microseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
### withVersions(List<LogQuery.Version> versions)
    
    
    public static LogQuery withVersions(List<LogQuery.Version> versions)

Create a [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) with the given [Version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Version) values. Shorthand for `LogQuery.Builder.withDefaults().versions(versions);`. Please read the [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) class javadoc for usage information.

**Parameter**  
---  
**Name** | **Description**  
`versions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Version)>`  
the list to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | The newly created LogQuery instance.  
  
## Constructors 

### Builder()
    
    
    public Builder()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
