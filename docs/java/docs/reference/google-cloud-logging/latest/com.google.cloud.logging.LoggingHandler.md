---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler
title: Class LoggingHandler (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:00.681332+00:00
---

# Class LoggingHandler (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LoggingHandler (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class LoggingHandler extends Handler

A logging handler that outputs logs generated with [java.util.logging.Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html) to Cloud Logging.

Java logging levels (see [java.util.logging.Level](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html)) are mapped to the following Google Cloud Logging severities:

Mapping of Java logging level to Cloud Logging severities Java Level | Cloud Logging Severity  
---|---  
SEVERE | ERROR  
WARNING | WARNING  
INFO | INFO  
CONFIG | INFO  
FINE | DEBUG  
FINER | DEBUG  
FINEST | DEBUG  
  
Original Java logging levels are added as labels (with `levelName` and ` levelValue` keys, respectively) to the corresponding Cloud Logging [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry). You can read entry labels using [LogEntry#getLabels()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry#com_google_logging_v2_LogEntry_getLabels__). To use logging levels that correspond to Cloud Logging severities you can use [LoggingLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingLevel).

**Configuration** : By default each `LoggingHandler` is initialized using the following `LogManager` configuration properties (that you can set in the ` logging.properties` file). If properties are not defined (or have invalid values) then the specified default values are used.

  * `com.google.cloud.logging.LoggingHandler.log` the log name (defaults to ` java.log`). 
  * `com.google.cloud.logging.LoggingHandler.level` specifies the default level for the handler (defaults to `Level.INFO`). 
  * `com.google.cloud.logging.LoggingHandler.filter` specifies the name of a Filter class to use (defaults to no filter). 
  * `com.google.cloud.logging.LoggingHandler.formatter` specifies the name of a Formatter class to use (defaults to SimpleFormatter). 
  * `com.google.cloud.logging.LoggingHandler.flushLevel` specifies the flush log level. When a log with this level is published, logs are transmitted to the Cloud Logging service (defaults to [LoggingLevel#ERROR](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingLevel#com_google_cloud_logging_LoggingLevel_ERROR)). 
  * `com.google.cloud.logging.LoggingHandler.enhancers` specifies a comma separated list of [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer) classes. This handler will call each enhancer list whenever it builds a [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry) instance (defaults to empty list). 
  * `com.google.cloud.logging.LoggingHandler.resourceType` the type name to use when creating the default MonitoredResource (defaults to auto-detected resource type, else "global"). 
  * `com.google.cloud.logging.Synchronicity` the synchronicity of the write method to use to write logs to the Cloud Logging service (defaults to [Synchronicity#ASYNC](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity#com_google_cloud_logging_Synchronicity_ASYNC)). 
  * `com.google.cloud.logging.LoggingHandler.autoPopulateMetadata` is a boolean flag that opts-out the population of the log entries metadata before the logs are sent to Cloud Logging (defaults to `true`). 
  * `com.google.cloud.logging.LoggingHandler.redirectToStdout` is a boolean flag that opts-in redirecting the output of the handler to STDOUT instead of ingesting logs to Cloud Logging using Logging API (defaults to `false`). Redirecting logs can be used in Google Cloud environments with installed logging agent to delegate log ingestions to the agent. Redirected logs are formatted as one line Json string following the structured logging guidelines. This flag is deprecated; use ` com.google.cloud.logging.LoggingHandler.logTarget` instead. 
  * `com.google.cloud.logging.LoggingHandler.logTarget` is an enumeration controlling log routing (defaults to `CLOUD_LOGGING`). If set to STDOUT or STDERR, logs will be printed to the corresponding stream in the Json format that can be parsed by the logging agent. If set to CLOUD_LOGGING, logs will be sent directly to the Google Cloud Logging API. 



To add a `LoggingHandler` to an existing [Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html) and be sure to avoid infinite recursion when logging, use the [#addHandler(Logger, LoggingHandler)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler#com_google_cloud_logging_LoggingHandler_addHandler_java_util_logging_Logger_com_google_cloud_logging_LoggingHandler_) method. Alternatively you can add the handler via `logging.properties`. For example using the following line:
    
    
     com.example.mypackage.handlers=com.google.cloud.logging.LoggingHandler
     

See Also: [Structured logging](https://cloud.google.com/logging/docs/structured-logging)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Handler](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html) > LoggingHandler

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

[Handler.close()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#close--)

[Handler.flush()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#flush--)

[Handler.getEncoding()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#getEncoding--)

[Handler.getErrorManager()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#getErrorManager--)

[Handler.getFilter()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#getFilter--)

[Handler.getFormatter()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#getFormatter--)

[Handler.getLevel()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#getLevel--)

[Handler.isLoggable(LogRecord)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#isLoggable-java.util.logging.LogRecord-)

[Handler.publish(LogRecord)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#publish-java.util.logging.LogRecord-)

[Handler.reportError(String,Exception,int)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#reportError-java.lang.String-java.lang.Exception-int-)

[Handler.setEncoding(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#setEncoding-java.lang.String-)

[Handler.setErrorManager(ErrorManager)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#setErrorManager-java.util.logging.ErrorManager-)

[Handler.setFilter(Filter)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#setFilter-java.util.logging.Filter-)

[Handler.setFormatter(Formatter)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#setFormatter-java.util.logging.Formatter-)

[Handler.setLevel(Level)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#setLevel-java.util.logging.Level-)

## Static Methods 

### addHandler(Logger logger, LoggingHandler handler)
    
    
    public static void addHandler(Logger logger, LoggingHandler handler)

Adds the provided `LoggingHandler` to `logger`. Use this method to register Cloud Logging handlers instead of Logger#addHandler(Handler) to avoid infinite recursion when logging.

**Parameters**  
---  
**Name** | **Description**  
`logger` | `[Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html)`  
  
`handler` | `[LoggingHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler)`  
  
  
## Constructors 

### LoggingHandler()
    
    
    public LoggingHandler()

Creates a handler that publishes messages to Cloud Logging.

### LoggingHandler(String log)
    
    
    public LoggingHandler(String log)

Creates a handler that publishes messages to Cloud Logging.

**Parameter**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the log to which log entries are written  
  
### LoggingHandler(String log, LoggingOptions options)
    
    
    public LoggingHandler(String log, LoggingOptions options)

Creates a handler that publishes messages to Cloud Logging.

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the log to which log entries are written  
`options` | `[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)`  
options for the Cloud Logging service  
  
### LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource)
    
    
    public LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource)

Creates a handler that publishes messages to Cloud Logging.

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the log to which log entries are written  
`options` | `[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)`  
options for the Cloud Logging service  
`monitoredResource` | `com.google.cloud.MonitoredResource`  
the monitored resource to which log entries refer. If it is null then a default resource is created based on the project ID and deployment environment.  
  
### LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource, List<LoggingEnhancer> enhancers)
    
    
    public LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource, List<LoggingEnhancer> enhancers)

Creates a handler that publishes messages to Cloud Logging.

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the log to which log entries are written  
`options` | `[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)`  
options for the Cloud Logging service  
`monitoredResource` | `com.google.cloud.MonitoredResource`  
the monitored resource to which log entries refer. If it is null then a default resource is created based on the project ID and deployment environment.  
`enhancers` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer)>`  
List of [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer) instances used to enhance any[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry) instances built by this handler.  
  
### LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource, List<LoggingEnhancer> enhancers, LogDestinationName destination)
    
    
    public LoggingHandler(String log, LoggingOptions options, MonitoredResource monitoredResource, List<LoggingEnhancer> enhancers, LogDestinationName destination)

Creates a handler that publishes messages to Cloud Logging. Auto-population of the logs metadata can be opted-out in `options` argument or in the configuration file. At least one flag [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions) or LoggingConfig has to be explicitly set to ` false` in order to opt out the metadata auto-population.

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the log to which log entries are written  
`options` | `[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)`  
options for the Cloud Logging service  
`monitoredResource` | `com.google.cloud.MonitoredResource`  
the monitored resource to which log entries refer. If it is null then a default resource is created based on the project ID and deployment environment.  
`enhancers` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer)>`  
List of [LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer) instances used to enhance any[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry) instances built by this handler.  
`destination` | `[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)`  
the log destination [LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName) (see 'logName' parameter in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>)  
  
## Methods 

### close()
    
    
    public synchronized void close()

Closes the handler and the associated [Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging) object.

**Overrides**

[Handler.close()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#close--)

### flush()
    
    
    public void flush()

**Overrides**

[Handler.flush()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#flush--)

### getAutoPopulateMetadata()
    
    
    public Boolean getAutoPopulateMetadata()

Gets the metadata auto population flag.

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getFlushLevel()
    
    
    public Level getFlushLevel()

Get the flush log level.

**Returns**  
---  
**Type** | **Description**  
`[Level](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html)` |   
  
### getLogTarget()
    
    
    public LoggingHandler.LogTarget getLogTarget()

**Returns**  
---  
**Type** | **Description**  
`[LoggingHandler.LogTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler.LogTarget)` |   
  
### getRedirectToStdout() (deprecated)
    
    
    public Boolean getRedirectToStdout()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getSynchronicity()
    
    
    public Synchronicity getSynchronicity()

Get the flush log level.

**Returns**  
---  
**Type** | **Description**  
`[Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity)` |   
  
### logEntryFor(LogRecord record)
    
    
    protected LogEntry.Builder logEntryFor(LogRecord record)

**Parameter**  
---  
**Name** | **Description**  
`record` | `[LogRecord](https://docs.oracle.com/javase/8/docs/api/java/util/logging/LogRecord.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder)` |   
  
### publish(LogRecord record)
    
    
    public void publish(LogRecord record)

**Parameter**  
---  
**Name** | **Description**  
`record` | `[LogRecord](https://docs.oracle.com/javase/8/docs/api/java/util/logging/LogRecord.html)`  
  
**Overrides**

[Handler.publish(LogRecord)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Handler.html#publish-java.util.logging.LogRecord-)

### setAutoPopulateMetadata(boolean value)
    
    
    public void setAutoPopulateMetadata(boolean value)

Sets the metadata auto population flag.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setFlushLevel(Level flushLevel)
    
    
    public void setFlushLevel(Level flushLevel)

Sets minimum logging level to log immediately and flush any pending writes.

**Parameter**  
---  
**Name** | **Description**  
`flushLevel` | `[Level](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html)`  
minimum log level to trigger flush  
  
### setLogTarget(LoggingHandler.LogTarget value)
    
    
    public void setLogTarget(LoggingHandler.LogTarget value)

Configure the destination for ingested logs. If set to STDOUT or STDERR, logs will be printed to the corresponding stream in the Json format that can be parsed by the logging agent. If set to CLOUD_LOGGING, logs will be sent directly to the Google Cloud Logging API.

This method is mutually exclusive with [#setRedirectToStdout(boolean)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler#com_google_cloud_logging_LoggingHandler_setRedirectToStdout_boolean_).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LoggingHandler.LogTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler.LogTarget)`  
  
  
### setRedirectToStdout(boolean value) (deprecated)
    
    
    public void setRedirectToStdout(boolean value)

**Deprecated.** _Use[#setLogTarget(LogTarget)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler#com_google_cloud_logging_LoggingHandler_setLogTarget_)._

Enable/disable redirection to STDOUT. If set to `true`, logs will be printed to STDOUT in the Json format that can be parsed by the logging agent. If set to `false`, logs will be ingested to Cloud Logging by calling Logging API.

This method is mutually exclusive with [#setLogTarget(LogTarget)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler#com_google_cloud_logging_LoggingHandler_setLogTarget_).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setSynchronicity(Synchronicity synchronicity)
    
    
    public void setSynchronicity(Synchronicity synchronicity)

Sets synchronicity of logging writes. By default, writes are asynchronous.

**Parameter**  
---  
**Name** | **Description**  
`synchronicity` | `[Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity)`  
[Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
