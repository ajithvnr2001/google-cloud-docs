---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance.ObservabilityInstanceConfigOrBuilder
title: Interface Instance.ObservabilityInstanceConfigOrBuilder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:25.252816+00:00
---

# Interface Instance.ObservabilityInstanceConfigOrBuilder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance.ObservabilityInstanceConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Instance.ObservabilityInstanceConfigOrBuilder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Instance.ObservabilityInstanceConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAssistiveExperiencesEnabled()
    
    
    public abstract boolean getAssistiveExperiencesEnabled()

Whether assistive experiences are enabled for this AlloyDB instance.

`optional bool assistive_experiences_enabled = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The assistiveExperiencesEnabled.  
  
### getEnabled()
    
    
    public abstract boolean getEnabled()

Observability feature status for an instance. This flag is turned "off" by default.

`optional bool enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getMaxQueryStringLength()
    
    
    public abstract int getMaxQueryStringLength()

Query string length. The default value is 10k.

`optional int32 max_query_string_length = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxQueryStringLength.  
  
### getPreserveComments()
    
    
    public abstract boolean getPreserveComments()

Preserve comments in query string for an instance. This flag is turned "off" by default.

`optional bool preserve_comments = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preserveComments.  
  
### getQueryPlansPerMinute()
    
    
    public abstract int getQueryPlansPerMinute()

Number of query execution plans captured by Insights per minute for all queries combined. The default value is 200. Any integer between 0 to 200 is considered valid.

`optional int32 query_plans_per_minute = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The queryPlansPerMinute.  
  
### getRecordApplicationTags()
    
    
    public abstract boolean getRecordApplicationTags()

Record application tags for an instance. This flag is turned "off" by default.

`optional bool record_application_tags = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The recordApplicationTags.  
  
### getTrackActiveQueries()
    
    
    public abstract boolean getTrackActiveQueries()

Track actively running queries on the instance. If not set, this flag is "off" by default.

`optional bool track_active_queries = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The trackActiveQueries.  
  
### getTrackClientAddress()
    
    
    public abstract boolean getTrackClientAddress()

Track client address for an instance. If not set, default value is "off".

`optional bool track_client_address = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The trackClientAddress.  
  
### getTrackWaitEventTypes()
    
    
    public abstract boolean getTrackWaitEventTypes()

Output only. Track wait event types during query execution for an instance. This flag is turned "on" by default but tracking is enabled only after observability enabled flag is also turned on. This is read-only flag and only modifiable by internal API.

`optional bool track_wait_event_types = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The trackWaitEventTypes.  
  
### getTrackWaitEvents()
    
    
    public abstract boolean getTrackWaitEvents()

Track wait events during query execution for an instance. This flag is turned "on" by default but tracking is enabled only after observability enabled flag is also turned on.

`optional bool track_wait_events = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The trackWaitEvents.  
  
### hasAssistiveExperiencesEnabled()
    
    
    public abstract boolean hasAssistiveExperiencesEnabled()

Whether assistive experiences are enabled for this AlloyDB instance.

`optional bool assistive_experiences_enabled = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assistiveExperiencesEnabled field is set.  
  
### hasEnabled()
    
    
    public abstract boolean hasEnabled()

Observability feature status for an instance. This flag is turned "off" by default.

`optional bool enabled = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enabled field is set.  
  
### hasMaxQueryStringLength()
    
    
    public abstract boolean hasMaxQueryStringLength()

Query string length. The default value is 10k.

`optional int32 max_query_string_length = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxQueryStringLength field is set.  
  
### hasPreserveComments()
    
    
    public abstract boolean hasPreserveComments()

Preserve comments in query string for an instance. This flag is turned "off" by default.

`optional bool preserve_comments = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the preserveComments field is set.  
  
### hasQueryPlansPerMinute()
    
    
    public abstract boolean hasQueryPlansPerMinute()

Number of query execution plans captured by Insights per minute for all queries combined. The default value is 200. Any integer between 0 to 200 is considered valid.

`optional int32 query_plans_per_minute = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryPlansPerMinute field is set.  
  
### hasRecordApplicationTags()
    
    
    public abstract boolean hasRecordApplicationTags()

Record application tags for an instance. This flag is turned "off" by default.

`optional bool record_application_tags = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recordApplicationTags field is set.  
  
### hasTrackActiveQueries()
    
    
    public abstract boolean hasTrackActiveQueries()

Track actively running queries on the instance. If not set, this flag is "off" by default.

`optional bool track_active_queries = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trackActiveQueries field is set.  
  
### hasTrackClientAddress()
    
    
    public abstract boolean hasTrackClientAddress()

Track client address for an instance. If not set, default value is "off".

`optional bool track_client_address = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trackClientAddress field is set.  
  
### hasTrackWaitEventTypes()
    
    
    public abstract boolean hasTrackWaitEventTypes()

Output only. Track wait event types during query execution for an instance. This flag is turned "on" by default but tracking is enabled only after observability enabled flag is also turned on. This is read-only flag and only modifiable by internal API.

`optional bool track_wait_event_types = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trackWaitEventTypes field is set.  
  
### hasTrackWaitEvents()
    
    
    public abstract boolean hasTrackWaitEvents()

Track wait events during query execution for an instance. This flag is turned "on" by default but tracking is enabled only after observability enabled flag is also turned on.

`optional bool track_wait_events = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trackWaitEvents field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
