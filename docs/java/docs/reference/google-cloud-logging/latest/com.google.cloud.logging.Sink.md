---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink
title: Class Sink (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:03.863093+00:00
---

# Class Sink (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Sink (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class Sink extends SinkInfo

Cloud Logging sinks can be used to control the export of your logs. Each sink specifies the export of a set of log entries to a certain destination. A sink consists of a name, unique to the project, a filter for choosing the log entries to export and a destination for the log entries.

Sink destination can either be a Google Cloud Storage bucket (see [SinkInfo.Destination.BucketDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.BucketDestination), a Google Cloud BigQuery dataset (see [SinkInfo.Destination.DatasetDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.DatasetDestination)) or a Google CloudPub/Sub topic (see [SinkInfo.Destination.TopicDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.TopicDestination)).

`Sink` adds a layer of service-related functionality over [SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo). Objects of this class are immutable. To get a `Sink` object with the most recent information use [#reload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink#com_google_cloud_logging_Sink_reload_) or [#reloadAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink#com_google_cloud_logging_Sink_reloadAsync_). See Also: [About Sinks](https://cloud.google.com/logging/docs/api/tasks/exporting-logs#about_sinks)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo) > Sink

## Inherited Members

[SinkInfo.<T>getDestination()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo__T_getDestination__)

[SinkInfo.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_equals_java_lang_Object_)

[SinkInfo.getFilter()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_getFilter__)

[SinkInfo.getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_getName__)

[SinkInfo.getVersionFormat()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_getVersionFormat__)

[SinkInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_hashCode__)

[SinkInfo.newBuilder(String,SinkInfo.Destination)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_newBuilder_java_lang_String_com_google_cloud_logging_SinkInfo_Destination_)

[SinkInfo.of(String,SinkInfo.Destination)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_of_java_lang_String_com_google_cloud_logging_SinkInfo_Destination_)

[SinkInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_toBuilder__)

[SinkInfo.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### delete()
    
    
    public boolean delete()

Deletes this sink.

Example of deleting the sink.
    
    
     boolean deleted = sink.delete();
     if (deleted) {
       // the sink was deleted
     } else {
       // the sink was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the sink was deleted, `false` if it was not found  
  
### deleteAsync()
    
    
    public ApiFuture<Boolean> deleteAsync()

Sends a request for deleting this sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the sink was deleted, `false` if it was not found.

Example of asynchronously deleting the sink.
    
    
     ApiFuture<Boolean> future = sink.deleteAsync();
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the sink was deleted
     } else {
       // the sink was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### equals(Object obj)
    
    
    public final boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[SinkInfo.equals(Object obj)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_equals_java_lang_Object_)

### getLogging()
    
    
    public Logging getLogging()

Returns the sinks's `Logging` object used to issue requests.

**Returns**  
---  
**Type** | **Description**  
`[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging)` |   
  
### hashCode()
    
    
    public final int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[SinkInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_hashCode__)

### reload()
    
    
    public Sink reload()

Fetches current sink's latest information. Returns `null` if the sink does not exist.

Example of getting the sink's latest information.
    
    
     Sink latestSink = sink.reload();
     if (latestSink == null) {
       // the sink was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)` | a `Sink` object with latest information or `null` if not found  
  
### reloadAsync()
    
    
    public ApiFuture<Sink> reloadAsync()

Sends a request to fetch current sink's latest information. This method returns a ` ApiFuture` object to consume the result. ApiFuture#get() returns a `Sink` object with latest information or `null` if not found.

Example of asynchronously getting the sink's latest information.
    
    
     ApiFuture<Sink> future = sink.reloadAsync();
     // ...
     Sink latestSink = future.get();
     if (latestSink == null) {
       // the sink was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
### toBuilder()
    
    
    public Sink.Builder toBuilder()

Returns a builder for this `SinkInfo` object.

**Returns**  
---  
**Type** | **Description**  
`[Sink.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink.Builder)` |   
**Overrides**

[SinkInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo#com_google_cloud_logging_SinkInfo_toBuilder__)

### update()
    
    
    public Sink update()

Updates current sink. If the sink does not exist, it is created.

Example of updating the sink's information.
    
    
     Sink updatedSink = sink.toBuilder()
         .setFilter("severity<=error") .build()="" .update();="">

**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)` | a `Sink` object with updated information  
  
### updateAsync()
    
    
    public ApiFuture<Sink> updateAsync()

Sends a request to update current sink. If the sink does not exist, it is created. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a `Sink` object with updated information.

Example of asynchronously updating the sink's information.
    
    
     ApiFuture<Sink> future = sink.toBuilder()
         .setFilter("severity<=error") .build()="" .updateasync();="" ...="" sink="" updatedsink="future.get();">

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
