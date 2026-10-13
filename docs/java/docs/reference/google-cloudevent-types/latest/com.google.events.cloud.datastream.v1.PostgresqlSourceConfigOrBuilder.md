---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlSourceConfigOrBuilder
title: Interface PostgresqlSourceConfigOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:04.697249+00:00
---

# Interface PostgresqlSourceConfigOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlSourceConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PostgresqlSourceConfigOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlSourceConfigOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.datastream.v1.PostgresqlSourceConfigOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.datastream.v1.PostgresqlSourceConfigOrBuilder)


    
    
    public interface PostgresqlSourceConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExcludeObjects()
    
    
    public abstract PostgresqlRdbms getExcludeObjects()

PostgreSQL objects to exclude from the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlRdbms](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlRdbms)` | The excludeObjects.  
  
### getExcludeObjectsOrBuilder()
    
    
    public abstract PostgresqlRdbmsOrBuilder getExcludeObjectsOrBuilder()

PostgreSQL objects to exclude from the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlRdbmsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlRdbmsOrBuilder)` |   
  
### getIncludeObjects()
    
    
    public abstract PostgresqlRdbms getIncludeObjects()

PostgreSQL objects to include in the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlRdbms](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlRdbms)` | The includeObjects.  
  
### getIncludeObjectsOrBuilder()
    
    
    public abstract PostgresqlRdbmsOrBuilder getIncludeObjectsOrBuilder()

PostgreSQL objects to include in the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlRdbmsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PostgresqlRdbmsOrBuilder)` |   
  
### getPublication()
    
    
    public abstract String getPublication()

Required. The name of the publication that includes the set of all tables that are defined in the stream's include_objects.

`string publication = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The publication.  
  
### getPublicationBytes()
    
    
    public abstract ByteString getPublicationBytes()

Required. The name of the publication that includes the set of all tables that are defined in the stream's include_objects.

`string publication = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for publication.  
  
### getReplicationSlot()
    
    
    public abstract String getReplicationSlot()

Required. Immutable. The name of the logical replication slot that's configured with the pgoutput plugin.

`string replication_slot = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The replicationSlot.  
  
### getReplicationSlotBytes()
    
    
    public abstract ByteString getReplicationSlotBytes()

Required. Immutable. The name of the logical replication slot that's configured with the pgoutput plugin.

`string replication_slot = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for replicationSlot.  
  
### hasExcludeObjects()
    
    
    public abstract boolean hasExcludeObjects()

PostgreSQL objects to exclude from the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms exclude_objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the excludeObjects field is set.  
  
### hasIncludeObjects()
    
    
    public abstract boolean hasIncludeObjects()

PostgreSQL objects to include in the stream.

`.google.events.cloud.datastream.v1.PostgresqlRdbms include_objects = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the includeObjects field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
