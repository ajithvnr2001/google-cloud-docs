---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs
title: Class RequestLogs (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:44:52.588319+00:00
---

# Class RequestLogs (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.RequestLogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class RequestLogs (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class RequestLogs implements Serializable

RequestLogs contain all the log information for a single request. This includes the request log as well as any application logs (which may correspond to logging statements in the user's code or messages we have inserted to alert them to certain conditions we have noticed). Additionally, we include information about this request outside of those logs, such as how long the request took, the IP of the user performing the request, and so on.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RequestLogs

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

## Constructors 

### RequestLogs()
    
    
    public RequestLogs()

Default, zero-argument constructor for RequestLogs.

### RequestLogs(LogServicePb.RequestLog requestLog, String offset)
    
    
    protected RequestLogs(LogServicePb.RequestLog requestLog, String offset)

Constructs a new (external-facing) RequestLogs from an (internal-facing) RequestLog. We scrub out any fields that the Protocol Buffer specification for RequestLog names as Google-only fields.

**Parameters**  
---  
**Name** | **Description**  
`requestLog` | `com.google.apphosting.api.logservice.LogServicePb.RequestLog`  
The RequestLog returned by a Log Read RPC call.  
`offset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A String containing an encoded offset from the RequestLog.  
  
## Methods 

### equals(@Nullable Object obj)
    
    
    public boolean equals(@Nullable Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getApiMcycles() (deprecated)
    
    
    public long getApiMcycles()

**Deprecated.** _This value is no longer meaningful._

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The number of machine cycles spent in API calls while processing this request.  
  
### getAppEngineRelease()
    
    
    public String getAppEngineRelease()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | App Engine Release, e.g. "1.7.5", or the empty string.  
  
### getAppId()
    
    
    public String getAppId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The application ID that handled this request.  
  
### getAppLogLines()
    
    
    public List<AppLogLine> getAppLogLines()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AppLogLine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.AppLogLine)>` | A list of application logs associated with this request.  
  
### getCombined()
    
    
    public String getCombined()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The Apache-format combined log entry for this request. While the information in this field can be constructed from the rest of this message, we include this method for convenience.  
  
### getCost()
    
    
    public double getCost()

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimated cost of this request, in dollars.  
  
### getEndTimeUsec()
    
    
    public long getEndTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The time at which the request was known to end processing, in microseconds since the Unix epoch.  
  
### getHost()
    
    
    public String getHost()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The Internet host and port number of the resource being requested.  
  
### getHttpVersion()
    
    
    public String getHttpVersion()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The HTTP version of this request.  
  
### getInstanceKey()
    
    
    public String getInstanceKey()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | Mostly-unique identifier for the instance that handled the request, or the empty string.  
  
### getIp()
    
    
    public String getIp()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The origin IP address of this request. App Engine uses an origin IP address from the 0.0.0.0/8 range when the request is to a web hook. Some examples of web hooks are task queues, cron jobs and warming requests.  
  
### getLatencyUsec()
    
    
    public long getLatencyUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The time required to process this request in microseconds.  
  
### getMcycles()
    
    
    public long getMcycles()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The number of machine cycles used to process this request.  
  
### getMethod()
    
    
    public String getMethod()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The request's method (e.g., GET, PUT, POST).  
  
### getModuleId()
    
    
    public String getModuleId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The module of the application that handled this request.  
  
### getNickname()
    
    
    public String getNickname()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nickname of the user that made the request. An empty string is returned if the user is not logged in.  
  
### getOffset()
    
    
    public String getOffset()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A Base64-encoded offset that may be used with a subsequent LogQuery to continue reading logs at the point in time immediately following this request.  
  
### getPendingTimeUsec()
    
    
    public long getPendingTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The time, in microseconds, that this request spent in the pending request queue, if it was pending at all.  
  
### getReferrer()
    
    
    public String getReferrer()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referrer URL of this request.  
  
### getReplicaIndex()
    
    
    public int getReplicaIndex()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backend replica that handled the request, or -1 if not serviced by a backend.  
  
### getRequestId()
    
    
    public String getRequestId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A globally unique identifier for a request, based on the request's starting time.  
  
### getResource()
    
    
    public String getResource()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resource path on the server requested by the client. Contains only the path component of the request URL.  
  
### getResponseSize()
    
    
    public long getResponseSize()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The size (in bytes) sent back to the client by this request.  
  
### getStartTimeUsec()
    
    
    public long getStartTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The time at which this request was known to have begun processing, in microseconds since the Unix epoch.  
  
### getStatus()
    
    
    public int getStatus()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The HTTP response status of this request.  
  
### getTaskName()
    
    
    public String getTaskName()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The request's task name, if this request was generated via the Task Queue API.  
  
### getTaskQueueName()
    
    
    public String getTaskQueueName()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The request's queue name, if this request was generated via the Task Queue API.  
  
### getUrlMapEntry()
    
    
    public String getUrlMapEntry()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The file or class within the URL mapping used for this request. Useful for tracking down the source code which was responsible for managing the request, especially for multiply mapped handlers.  
  
### getUserAgent()
    
    
    public String getUserAgent()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The user agent used to make this request.  
  
### getVersionId()
    
    
    public String getVersionId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version of the application that handled this request.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isFinished()
    
    
    public boolean isFinished()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether or not this request has been finished. If not, this request is still active.  
  
### isLoadingRequest()
    
    
    public boolean isLoadingRequest()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether or not this request was a loading request.  
  
### setApiMcycles(long apiMcycles)
    
    
    public void setApiMcycles(long apiMcycles)

**Parameter**  
---  
**Name** | **Description**  
`apiMcycles` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setAppEngineRelease(String appEngineRelease)
    
    
    public void setAppEngineRelease(String appEngineRelease)

**Parameter**  
---  
**Name** | **Description**  
`appEngineRelease` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setAppId(String appId)
    
    
    public void setAppId(String appId)

**Parameter**  
---  
**Name** | **Description**  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setAppLogLines(List<AppLogLine> appLogLines)
    
    
    public void setAppLogLines(List<AppLogLine> appLogLines)

**Parameter**  
---  
**Name** | **Description**  
`appLogLines` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AppLogLine](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.log.AppLogLine)>`  
  
  
### setCombined(String combined)
    
    
    public void setCombined(String combined)

**Parameter**  
---  
**Name** | **Description**  
`combined` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setCost(double cost)
    
    
    public void setCost(double cost)

**Parameter**  
---  
**Name** | **Description**  
`cost` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setEndTimeUsec(long endTimeUsec)
    
    
    public void setEndTimeUsec(long endTimeUsec)

**Parameter**  
---  
**Name** | **Description**  
`endTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setFinished(boolean finished)
    
    
    public void setFinished(boolean finished)

**Parameter**  
---  
**Name** | **Description**  
`finished` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setHost(String host)
    
    
    public void setHost(String host)

**Parameter**  
---  
**Name** | **Description**  
`host` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setHttpVersion(String httpVersion)
    
    
    public void setHttpVersion(String httpVersion)

**Parameter**  
---  
**Name** | **Description**  
`httpVersion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setInstanceKey(String instanceKey)
    
    
    public void setInstanceKey(String instanceKey)

**Parameter**  
---  
**Name** | **Description**  
`instanceKey` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setIp(String ip)
    
    
    public void setIp(String ip)

**Parameter**  
---  
**Name** | **Description**  
`ip` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setLatency(long latency)
    
    
    public void setLatency(long latency)

**Parameter**  
---  
**Name** | **Description**  
`latency` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setMcycles(long mcycles)
    
    
    public void setMcycles(long mcycles)

**Parameter**  
---  
**Name** | **Description**  
`mcycles` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setMethod(String method)
    
    
    public void setMethod(String method)

**Parameter**  
---  
**Name** | **Description**  
`method` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setModuleId(String moduleId)
    
    
    public void setModuleId(String moduleId)

**Parameter**  
---  
**Name** | **Description**  
`moduleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setNickname(String nickname)
    
    
    public void setNickname(String nickname)

**Parameter**  
---  
**Name** | **Description**  
`nickname` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setOffset(String offset)
    
    
    public void setOffset(String offset)

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setPendingTime(long pendingTime)
    
    
    public void setPendingTime(long pendingTime)

**Parameter**  
---  
**Name** | **Description**  
`pendingTime` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setReferrer(String referrer)
    
    
    public void setReferrer(String referrer)

**Parameter**  
---  
**Name** | **Description**  
`referrer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setReplicaIndex(int replicaIndex)
    
    
    public void setReplicaIndex(int replicaIndex)

**Parameter**  
---  
**Name** | **Description**  
`replicaIndex` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setRequestId(String requestId)
    
    
    public void setRequestId(String requestId)

**Parameter**  
---  
**Name** | **Description**  
`requestId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setResource(String resource)
    
    
    public void setResource(String resource)

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setResponseSize(long responseSize)
    
    
    public void setResponseSize(long responseSize)

**Parameter**  
---  
**Name** | **Description**  
`responseSize` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setStartTimeUsec(long startTimeUsec)
    
    
    public void setStartTimeUsec(long startTimeUsec)

**Parameter**  
---  
**Name** | **Description**  
`startTimeUsec` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setStatus(int status)
    
    
    public void setStatus(int status)

**Parameter**  
---  
**Name** | **Description**  
`status` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### setTaskName(String taskName)
    
    
    public void setTaskName(String taskName)

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setTaskQueueName(String taskQueueName)
    
    
    public void setTaskQueueName(String taskQueueName)

**Parameter**  
---  
**Name** | **Description**  
`taskQueueName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setUrlMapEntry(String urlMapEntry)
    
    
    public void setUrlMapEntry(String urlMapEntry)

**Parameter**  
---  
**Name** | **Description**  
`urlMapEntry` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setUserAgent(String userAgent)
    
    
    public void setUserAgent(String userAgent)

**Parameter**  
---  
**Name** | **Description**  
`userAgent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setVersionId(String versionId)
    
    
    public void setVersionId(String versionId)

**Parameter**  
---  
**Name** | **Description**  
`versionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setWasLoadingRequest(boolean wasLoadingRequest)
    
    
    public void setWasLoadingRequest(boolean wasLoadingRequest)

**Parameter**  
---  
**Name** | **Description**  
`wasLoadingRequest` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
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
