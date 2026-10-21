---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequestOrBuilder
title: Interface URLFetchServicePb.URLFetchRequestOrBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:04:07.132871+00:00
---

# Interface URLFetchServicePb.URLFetchRequestOrBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface URLFetchServicePb.URLFetchRequestOrBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface URLFetchServicePb.URLFetchRequestOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getDeadline()
    
    
    public abstract double getDeadline()

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFollowRedirects()
    
    
    public abstract boolean getFollowRedirects()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeader(int arg0)
    
    
    public abstract URLFetchServicePb.URLFetchRequest.Header getHeader(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.Header)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<URLFetchServicePb.URLFetchRequest.Header> getHeaderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.Header)>` |   
  
### getHeaderOrBuilder(int arg0)
    
    
    public abstract URLFetchServicePb.URLFetchRequest.HeaderOrBuilder getHeaderOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.HeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends URLFetchServicePb.URLFetchRequest.HeaderOrBuilder> getHeaderOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.HeaderOrBuilder>` |   
  
### getMethod()
    
    
    public abstract URLFetchServicePb.URLFetchRequest.RequestMethod getMethod()

**Returns**  
---  
**Type** | **Description**  
`[RequestMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.RequestMethod)` |   
  
### getMustValidateServerCertificate()
    
    
    public abstract boolean getMustValidateServerCertificate()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPayload()
    
    
    public abstract ByteString getPayload()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getUrl()
    
    
    public abstract String getUrl()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUrlBytes()
    
    
    public abstract ByteString getUrlBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### hasDeadline()
    
    
    public abstract boolean hasDeadline()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasFollowRedirects()
    
    
    public abstract boolean hasFollowRedirects()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMethod()
    
    
    public abstract boolean hasMethod()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMustValidateServerCertificate()
    
    
    public abstract boolean hasMustValidateServerCertificate()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasPayload()
    
    
    public abstract boolean hasPayload()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasUrl()
    
    
    public abstract boolean hasUrl()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
