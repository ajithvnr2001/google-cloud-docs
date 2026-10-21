---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponseOrBuilder
title: Interface URLFetchServicePb.URLFetchResponseOrBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:09:41.322929+00:00
---

# Interface URLFetchServicePb.URLFetchResponseOrBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface URLFetchServicePb.URLFetchResponseOrBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface URLFetchServicePb.URLFetchResponseOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getApiBytesReceived()
    
    
    public abstract long getApiBytesReceived()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getApiBytesSent()
    
    
    public abstract long getApiBytesSent()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getApiCpuMilliseconds()
    
    
    public abstract long getApiCpuMilliseconds()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getContent()
    
    
    public abstract ByteString getContent()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getContentWasTruncated()
    
    
    public abstract boolean getContentWasTruncated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExternalBytesReceived()
    
    
    public abstract long getExternalBytesReceived()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExternalBytesSent()
    
    
    public abstract long getExternalBytesSent()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFinalUrl()
    
    
    public abstract String getFinalUrl()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getFinalUrlBytes()
    
    
    public abstract ByteString getFinalUrlBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getHeader(int arg0)
    
    
    public abstract URLFetchServicePb.URLFetchResponse.Header getHeader(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.Header)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<URLFetchServicePb.URLFetchResponse.Header> getHeaderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.Header)>` |   
  
### getHeaderOrBuilder(int arg0)
    
    
    public abstract URLFetchServicePb.URLFetchResponse.HeaderOrBuilder getHeaderOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.HeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends URLFetchServicePb.URLFetchResponse.HeaderOrBuilder> getHeaderOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.HeaderOrBuilder>` |   
  
### getStatusCode()
    
    
    public abstract int getStatusCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasApiBytesReceived()
    
    
    public abstract boolean hasApiBytesReceived()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasApiBytesSent()
    
    
    public abstract boolean hasApiBytesSent()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasApiCpuMilliseconds()
    
    
    public abstract boolean hasApiCpuMilliseconds()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasContent()
    
    
    public abstract boolean hasContent()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasContentWasTruncated()
    
    
    public abstract boolean hasContentWasTruncated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasExternalBytesReceived()
    
    
    public abstract boolean hasExternalBytesReceived()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasExternalBytesSent()
    
    
    public abstract boolean hasExternalBytesSent()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasFinalUrl()
    
    
    public abstract boolean hasFinalUrl()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasStatusCode()
    
    
    public abstract boolean hasStatusCode()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
