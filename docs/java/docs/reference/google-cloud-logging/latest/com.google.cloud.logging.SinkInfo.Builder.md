---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder
title: Class SinkInfo.Builder (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:04.383495+00:00
---

# Class SinkInfo.Builder (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SinkInfo.Builder (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public abstract static class SinkInfo.Builder

A builder for `SinkInfo` objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SinkInfo.Builder

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

### Builder()
    
    
    public Builder()

## Methods 

### build()
    
    
    public abstract SinkInfo build()

Creates a `SinkInfo` object for this builder.

**Returns**  
---  
**Type** | **Description**  
`[SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo)` |   
  
### setDestination(SinkInfo.Destination destination)
    
    
    public abstract SinkInfo.Builder setDestination(SinkInfo.Destination destination)

Sets the export destination. Use a Destination.BucketDestination object to create a sink that exports logs to a Google Cloud Storage bucket. Use a Destination.DatasetDestination object to create a sink that exports logs to a Google Cloud BigQuery dataset. Use a Destination.TopicDestination object to create a sink that exports logs to a Google Cloud Pub/Sub topic. See Also: [ Exporting Logs](https://cloud.google.com/logging/docs/api/tasks/exporting-logs#about_sinks)

**Parameter**  
---  
**Name** | **Description**  
`destination` | `[SinkInfo.Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SinkInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder)` |   
  
### setFilter(String filter)
    
    
    public abstract SinkInfo.Builder setFilter(String filter)

Sets an advanced logs filter. Only log entries matching that filter are exported. The filter must be consistent with the log entry format specified with #setVersionFormat(VersionFormat), regardless of the format of the log entry that was originally written to Cloud Logging. Example (V2 format): ` logName=projects/my-projectid/logs/syslog AND severity>=ERROR`. See Also: [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters)

**Parameter**  
---  
**Name** | **Description**  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SinkInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder)` |   
  
### setName(String name)
    
    
    public abstract SinkInfo.Builder setName(String name)

Sets the name of the sink. Example: `my-severe-errors-to-pubsub`. Sink identifiers are limited to 1000 characters and can include only the following characters: `A-Z`, ` a-z`, `0-9`, and the special characters `_-.`.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SinkInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder)` |   
  
### setVersionFormat(SinkInfo.VersionFormat versionFormat)
    
    
    public abstract SinkInfo.Builder setVersionFormat(SinkInfo.VersionFormat versionFormat)

Sets the log entry version to use for this sink's exported log entries. This version does not have to correspond to the version of the log entry when it was written to Google Cloud Logging.

**Parameter**  
---  
**Name** | **Description**  
`versionFormat` | `[SinkInfo.VersionFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.VersionFormat)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SinkInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
