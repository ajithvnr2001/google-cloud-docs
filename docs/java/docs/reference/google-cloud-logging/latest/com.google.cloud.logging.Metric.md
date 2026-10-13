---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric
title: Class Metric (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:01.702056+00:00
---

# Class Metric (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Metric (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class Metric extends MetricInfo

Cloud Logging metrics describe logs-based metric. The value of the metric is the number of log entries that match a logs filter (see #getFilter()).

`Metric` adds a layer of service-related functionality over [MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo). Objects of this class are immutable. To get a `Metric` object with the most recent information use [#reload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric#com_google_cloud_logging_Metric_reload_) or [#reloadAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric#com_google_cloud_logging_Metric_reloadAsync_). See Also: [Logs-based Metrics ](https://cloud.google.com/logging/docs/view/logs_based_metrics)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo) > Metric

## Inherited Members

[MetricInfo.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_equals_java_lang_Object_)

[MetricInfo.getDescription()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_getDescription__)

[MetricInfo.getFilter()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_getFilter__)

[MetricInfo.getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_getName__)

[MetricInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_hashCode__)

[MetricInfo.newBuilder(String,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_newBuilder_java_lang_String_java_lang_String_)

[MetricInfo.of(String,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_of_java_lang_String_java_lang_String_)

[MetricInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_toBuilder__)

[MetricInfo.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_toString__)

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

Deletes this metric.

Example of deleting the metric.
    
    
     boolean deleted = metric.delete();
     if (deleted) {
       // the metric was deleted
     } else {
       // the metric was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the metric was deleted, `false` if it was not found  
  
### deleteAsync()
    
    
    public ApiFuture<Boolean> deleteAsync()

Sends a request for deleting this metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the metric was deleted, `false` if it was not found.

Example of asynchronously deleting the metric.
    
    
     ApiFuture<Boolean> future = metric.deleteAsync();
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the metric was deleted
     } else {
       // the metric was not found
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

[MetricInfo.equals(Object obj)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_equals_java_lang_Object_)

### getLogging()
    
    
    public Logging getLogging()

Returns the metrics's `Logging` object used to issue requests.

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

[MetricInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_hashCode__)

### reload()
    
    
    public Metric reload()

Fetches current metric's latest information. Returns `null` if the metric does not exist.

Example of getting the metric's latest information.
    
    
     Metric latestMetric = metric.reload();
     if (latestMetric == null) {
       // the metric was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)` | a `Metric` object with latest information or `null` if not found  
  
### reloadAsync()
    
    
    public ApiFuture<Metric> reloadAsync()

Sends a request to fetch current metric's latest information. This method returns a ` ApiFuture` object to consume the result. ApiFuture#get() returns a `Metric` object with latest information or `null` if not found.

Example of asynchronously getting the metric's latest information.
    
    
     ApiFuture<Metric> future = metric.reloadAsync();
     // ...
     Metric latestMetric = future.get();
     if (latestMetric == null) {
       // the metric was not found
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
### toBuilder()
    
    
    public Metric.Builder toBuilder()

Returns a builder for this `MetricInfo` object.

**Returns**  
---  
**Type** | **Description**  
`[Metric.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric.Builder)` |   
**Overrides**

[MetricInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo#com_google_cloud_logging_MetricInfo_toBuilder__)

### update()
    
    
    public Metric update()

Updates current metric. If the metric does not exist, it is created.

Example of updating the metric's information.
    
    
     Metric updatedMetric = metric.toBuilder()
         .setDescription("A more detailed description")
         .build()
         .update();
     

**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)` | a `Metric` object with updated information  
  
### updateAsync()
    
    
    public ApiFuture<Metric> updateAsync()

Sends a request to update current metric. If the metric does not exist, it is created. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a `Metric` object with updated information.

Example of asynchronously updating the metric's information.
    
    
     ApiFuture<Metric> future = metric.toBuilder()
         .setDescription("A more detailed description")
         .build()
         .updateAsync();
     // ...
     Metric updatedMetric = future.get();
     

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
