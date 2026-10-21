---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log
title: Package com.google.appengine.api.log (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:52:33.411968+00:00
---

# Package com.google.appengine.api.log (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.log (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides access to request logs and application logs. See Also: [com.google.appengine.api.log.LogService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService)

## Classes 

### [AppLogLine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.AppLogLine)

An AppLogLine contains all the information for a single application log. Specifically, this information is: (1) the time at which the logged event occurred, (2) the level that the event was logged at, and (3) the message associated with this event. AppLogLines may be inserted by the user via logging frameworks, or by App Engine itself if we wish to alert the user that certain events have occurred.

### [ILogServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.ILogServiceFactoryProvider)

Factory provider for [ILogServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.ILogServiceFactory).

**Note:** This class is not intended for end users.

### [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery)

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

### [LogQuery.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Builder)

Contains static creation methods for [LogQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery).

### [LogQuery.Version](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQuery.Version)

Specifies a version of a module.

### [LogQueryResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQueryResult)

An object that is the result of performing a LogService.fetch() operation. LogQueryResults contain the logs from the user's query. Users of this service should use the [LogQueryResult#iterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogQueryResult#com_google_appengine_api_log_LogQueryResult_iterator_) provided by this class to retrieve their results.

### [LogServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogServiceFactory)

Creates [LogService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService) implementations.

### [RequestLogs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs)

RequestLogs contain all the log information for a single request. This includes the request log as well as any application logs (which may correspond to logging statements in the user's code or messages we have inserted to alert them to certain conditions we have noticed). Additionally, we include information about this request outside of those logs, such as how long the request took, the IP of the user performing the request, and so on.

## Interfaces 

### [ILogServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.ILogServiceFactory)

Creates [LogService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService) implementations.

### [LogService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService)

`LogService` allows callers to request the logs for an application using supplied filters. Logs are returned in an `Iterable` that yields [RequestLogs](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs), which contain request-level information and optionally [AppLogLine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.AppLogLine) objects containing the application logs from the request.

## Enums 

### [LogService.LogLevel](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogService.LogLevel)

## Exceptions 

### [InvalidRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.InvalidRequestException)

Log errors caused by an invalid request due either to an out of range option or an unsupported combination of options. The exception detail will typically provide more specific information about the error.

### [LogServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.LogServiceException)

Log errors apart from InvalidRequestException. These errors will generally benefit from retrying the operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
