---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery
title: Class LogQuery (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:42:31.876079+00:00
---

# Class LogQuery (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class LogQuery (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class LogQuery implements Cloneable, Serializable

Allows users to customize the behavior of [LogService#fetch(LogQuery)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService#com_google_appengine_api_log_LogService_fetch_com_google_appengine_api_log_LogQuery_). 

`startTime` is the earliest request completion or last-update time that results should be fetched for, in seconds since the Unix epoch. If `null` then no requests will be excluded for ending too long ago. 

`endTime` is the latest request completion or last-update time that results should be fetched for, in seconds since the Unix epoch. If `null` then no requests will be excluded for ending too recently. 

`offset` is a cursor into the log stream retrieved from a previously emitted [RequestLogs#getOffset](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs#com_google_appengine_api_log_RequestLogs_getOffset_). This iterator will begin returning logs immediately after the record from which the offset came. If `null`, the query will begin at `startTime`. 

`minLogLevel` is a [LogService.LogLevel](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService.LogLevel) which serves as a filter on the requests returned. Requests with no application logs at or above the specified level will be omitted. Works even if `includeAppLogs` is not True. 

`includeIncomplete` selects whether requests that have started but not yet finished should be included in the query. Defaults to False. 

`includeAppLogs` specifies whether or not to include application logs in the query results. Defaults to False. 

`majorVersionIds` specifies versions of the application's default module for which logs records should retrieved. 

`versions` specifies module versions of the application for which logs should be retrieved. 

`requestIds`, if not `empty()`, indicates that instead of a time-based scan, logs for the specified requests should be returned. See the Request IDs section of [ the Java Servlet Environment documentation](https://developers.google.com/appengine/docs/java/runtime#The_Environment) for how to retrieve these IDs at runtime. Malformed request IDs cause an exception and unrecognized request IDs are ignored. This option may not be combined with other filtering options such as startTime, endTime, offset, or minLogLevel. When `requestIds` is not `empty()`, `majorVersionIds` are ignored. Logs are returned in the order requested. 

`batchSize` specifies the internal batching strategy of the returned [Iterable < RequestLogs >](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html). Has no impact on the result of the query. 

Notes on usage:  
The recommended way to instantiate a `LogQuery` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.log.LogQuery.Builder.*;
    
     ...
    
     // All requests, including application logs.
     iter = logService.fetch(withIncludeAppLogs(true));
    
     // All requests ending in the past day (or still running) with an info log or higher.
     Calendar cal = Calendar.getInstance();
     cal.add(Calendar.DAY_OF_MONTH, -1);
     iter = logService.fetch(withEndTimeMillis(cal.time())
         .includeIncomplete(true).minimumLogLevel(LogService.INFO));
     

There are a couple of ways to configure [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) to limit [LogService#fetch(LogQuery)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService#com_google_appengine_api_log_LogService_fetch_com_google_appengine_api_log_LogQuery_) to only return log records for specific module versions. 

  1. **[#versions(List)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery#com_google_appengine_api_log_LogQuery_versions_java_util_List_com_google_appengine_api_log_LogQuery_Version__)(Builder#withVersions(List))** \- Includes designated module versions for the application. 
  2. **[#majorVersionIds(List)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery#com_google_appengine_api_log_LogQuery_majorVersionIds_java_util_List_java_lang_String__) (Builder#withMajorVersionIds(List))** \- Includes designated versions of the default module for the application. 

For a particular [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery) only one of these methods may be used. If neither is used, [LogService#fetch(LogQuery)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService#com_google_appengine_api_log_LogService_fetch_com_google_appengine_api_log_LogQuery_) results may include any module version.

It is not allowed to call both [#versions(List)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery#com_google_appengine_api_log_LogQuery_versions_java_util_List_com_google_appengine_api_log_LogQuery_Version__) (Builder#withVersions(List)) and [#requestIds(List)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery#com_google_appengine_api_log_LogQuery_requestIds_java_util_List_java_lang_String__)(Builder#withRequestIds(List) for the same [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogQuery

## Implements

[Cloneable](https://docs.oracle.com/javase/8/docs/api/java/lang/Cloneable.html), [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### LogQuery()
    
    
    public LogQuery()

## Methods 

### batchSize(int batchSize)
    
    
    public LogQuery batchSize(int batchSize)

Sets the batch size. Please read the class javadoc for an explanation of how batch size is used.

**Parameter**  
---  
**Name** | **Description**  
`batchSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The batch size to set. Must be greater than 0.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### clone()
    
    
    public LogQuery clone()

Makes a copy of a provided LogQuery.

**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | A new LogQuery whose fields are copied from the given LogQuery.  
**Overrides**

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

### endTimeMillis(long endTimeMillis)
    
    
    public LogQuery endTimeMillis(long endTimeMillis)

Sets the end time to a value in milliseconds. Please read the class javadoc for an explanation of how end time is used.

**Parameter**  
---  
**Name** | **Description**  
`endTimeMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The end time to set, in milliseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### endTimeUsec(long endTimeUsec)
    
    
    public LogQuery endTimeUsec(long endTimeUsec)

Sets the end time to a value in microseconds. Please read the class javadoc for an explanation of how end time is used.

**Parameter**  
---  
**Name** | **Description**  
`endTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The end time to set, in microseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### getBatchSize()
    
    
    public @Nullable Integer getBatchSize()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Integer.html)` | The batch size, or `null` if none was provided.  
  
### getEndTimeMillis()
    
    
    public @Nullable Long getEndTimeMillis()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Long](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Long.html)` | The end time in milliseconds, or `null` if none was provided.  
  
### getEndTimeUsec()
    
    
    public @Nullable Long getEndTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Long](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Long.html)` | The end time in microseconds, or `null` if none was provided.  
  
### getIncludeAppLogs()
    
    
    public Boolean getIncludeAppLogs()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` | Whether or not application logs should be returned.  
  
### getIncludeIncomplete()
    
    
    public Boolean getIncludeIncomplete()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` | Whether or not incomplete request logs should be returned.  
  
### getMajorVersionIds()
    
    
    public List<String> getMajorVersionIds()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | The list of major app versions that should be queried over, or an empty list if none were set.  
  
### getMinLogLevel()
    
    
    public LogService.@Nullable LogLevel getMinLogLevel()

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.log.LogService.@org.jspecify.annotations.Nullable LogLevel` | The minimum log level, or `null` if none was provided.  
  
### getOffset()
    
    
    public @Nullable String getOffset()

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` | The offset, or `null` if none was provided.  
  
### getRequestIds()
    
    
    public List<String> getRequestIds()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | The list of request ids that should be queried over, or `null` if none were set.  
  
### getStartTimeMillis()
    
    
    public @Nullable Long getStartTimeMillis()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Long](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Long.html)` | The start time in milliseconds, or `null` if none was provided.  
  
### getStartTimeUsec()
    
    
    public @Nullable Long getStartTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Long](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Long.html)` | The start time in microseconds, or `null` if none was provided.  
  
### getVersions()
    
    
    public List<LogQuery.Version> getVersions()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Version)>` | The list possibly empty list of module versions that should be queried over.  
  
### includeAppLogs(boolean includeAppLogs)
    
    
    public LogQuery includeAppLogs(boolean includeAppLogs)

Sets include application logs. Please read the class javadoc for an explanation of how include application logs is used.

**Parameter**  
---  
**Name** | **Description**  
`includeAppLogs` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The value to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### includeIncomplete(boolean includeIncomplete)
    
    
    public LogQuery includeIncomplete(boolean includeIncomplete)

Sets include incomplete. Please read the class javadoc for an explanation of how include incomplete is used.

**Parameter**  
---  
**Name** | **Description**  
`includeIncomplete` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The value to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### majorVersionIds(List<String> versionIds)
    
    
    public LogQuery majorVersionIds(List<String> versionIds)

Sets the major version identifiers to query. Please read the class javadoc for an explanation of how major versions are used.

**Parameter**  
---  
**Name** | **Description**  
`versionIds` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The major version identifier list to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### minLogLevel(LogService.LogLevel minLogLevel)
    
    
    public LogQuery minLogLevel(LogService.LogLevel minLogLevel)

Sets the minimum log level. Please read the class javadoc for an explanation of how minimum log level is used.

**Parameter**  
---  
**Name** | **Description**  
`minLogLevel` | `[LogService.LogLevel](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService.LogLevel)`  
The minimum log level to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### offset(String offset)
    
    
    public LogQuery offset(String offset)

Sets the offset. Please read the class javadoc for an explanation of how offset is used.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The offset to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### requestIds(List<String> requestIds)
    
    
    public LogQuery requestIds(List<String> requestIds)

Sets the list of request ids to query. See the class javadoc for an explanation of how request ids are used.

**Parameter**  
---  
**Name** | **Description**  
`requestIds` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The request id list to set.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### startTimeMillis(long startTimeMillis)
    
    
    public LogQuery startTimeMillis(long startTimeMillis)

Sets the start time to a value in milliseconds. Please read the class javadoc for an explanation of how start time is used.

**Parameter**  
---  
**Name** | **Description**  
`startTimeMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The start time to set, in milliseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### startTimeUsec(long startTimeUsec)
    
    
    public LogQuery startTimeUsec(long startTimeUsec)

Sets the start time to a value in microseconds. Please read the class javadoc for an explanation of how start time is used.

**Parameter**  
---  
**Name** | **Description**  
`startTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The start time to set, in microseconds.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
### versions(List<LogQuery.Version> versions)
    
    
    public LogQuery versions(List<LogQuery.Version> versions)

Restricts the query to log records for the specified module versions.

Please read the class javadoc for usage information.

**Parameter**  
---  
**Name** | **Description**  
`versions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Version)>`  
The list of module versions to query.  
**Returns**  
---  
**Type** | **Description**  
`[LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)` | `this` (for chaining)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
