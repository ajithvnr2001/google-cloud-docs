---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigtableConfig.State
title: Enum BigtableConfig.State (1.157.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:45.300796+00:00
---

# Enum BigtableConfig.State (1.157.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigtableConfig.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum BigtableConfig.State (1.157.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.157.0 (latest)  1.153.0  1.152.0  1.151.0  1.150.1  1.149.0  1.148.0  1.147.0  1.145.0  1.143.1  1.142.0  1.141.5  1.140.2  1.139.4  1.138.0  1.137.1  1.136.1  1.135.0  1.134.2  1.133.1  1.132.2  1.131.0  1.130.0  1.129.6  1.127.3  1.126.6  1.125.13  1.123.18  1.122.2  1.121.1  1.120.24  1.119.1  1.118.0  1.117.0  1.116.4  1.115.5 
    
    
    public enum BigtableConfig.State extends Enum<BigtableConfig.State> implements ProtocolMessageEnum

Possible states for a Bigtable subscription. Note: more states could be added in the future. Please code accordingly.

Protobuf enum `google.pubsub.v1.BigtableConfig.State`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ACTIVE` |  The subscription can actively send messages to Bigtable. `ACTIVE = 1;`  
`ACTIVE_VALUE` |  The subscription can actively send messages to Bigtable. `ACTIVE = 1;`  
`APP_PROFILE_MISCONFIGURED` |  Unused in the current implementation. Placeholder for future use. `APP_PROFILE_MISCONFIGURED = 3;`  
`APP_PROFILE_MISCONFIGURED_VALUE` |  Unused in the current implementation. Placeholder for future use. `APP_PROFILE_MISCONFIGURED = 3;`  
`IN_TRANSIT_LOCATION_RESTRICTION` |  Cannot write to the destination because enforce_in_transit is set to true and the destination locations are not in the allowed regions. `IN_TRANSIT_LOCATION_RESTRICTION = 6;`  
`IN_TRANSIT_LOCATION_RESTRICTION_VALUE` |  Cannot write to the destination because enforce_in_transit is set to true and the destination locations are not in the allowed regions. `IN_TRANSIT_LOCATION_RESTRICTION = 6;`  
`NOT_FOUND` |  Unused in the current implementation. Placeholder for future use. `NOT_FOUND = 2;`  
`NOT_FOUND_VALUE` |  Unused in the current implementation. Placeholder for future use. `NOT_FOUND = 2;`  
`PERMISSION_DENIED` |  Cannot write to Bigtable because of permission denied errors. This can happen if:

  * The Bigtable instance, table, or app profile does not exist.
  * The Pub/Sub service agent has not been granted the [appropriate Bigtable IAM permission bigtable.tables.mutateRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/{$universe.dns_names.final_documentation_domain}/bigtable/docs/access-control#permissions)
  * The bigtable.googleapis.com API is not enabled for the project ([instructions](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/{$universe.dns_names.final_documentation_domain}/service-usage/docs/enable-disable))

`PERMISSION_DENIED = 4;`  
`PERMISSION_DENIED_VALUE` |  Cannot write to Bigtable because of permission denied errors. This can happen if:

  * The Bigtable instance, table, or app profile does not exist.
  * The Pub/Sub service agent has not been granted the [appropriate Bigtable IAM permission bigtable.tables.mutateRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/{$universe.dns_names.final_documentation_domain}/bigtable/docs/access-control#permissions)
  * The bigtable.googleapis.com API is not enabled for the project ([instructions](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/{$universe.dns_names.final_documentation_domain}/service-usage/docs/enable-disable))

`PERMISSION_DENIED = 4;`  
`SCHEMA_MISMATCH` |  Cannot write to Bigtable because of a missing column family (`data`), or if there is no structured row key for the subscription name + message ID, if because the app profile is not configured for single-cluster routing. `SCHEMA_MISMATCH = 5;`  
`SCHEMA_MISMATCH_VALUE` |  Cannot write to Bigtable because of a missing column family (`data`), or if there is no structured row key for the subscription name + message ID, if because the app profile is not configured for single-cluster routing. `SCHEMA_MISMATCH = 5;`  
`STATE_UNSPECIFIED` |  Default value. This value is unused. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  Default value. This value is unused. `STATE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`VERTEX_AI_LOCATION_RESTRICTION` |  Cannot write to Bigtable because the table is not in the same location as where Vertex AI models used in `message_transform`s are deployed. `VERTEX_AI_LOCATION_RESTRICTION = 7;`  
`VERTEX_AI_LOCATION_RESTRICTION_VALUE` |  Cannot write to Bigtable because the table is not in the same location as where Vertex AI models used in `message_transform`s are deployed. `VERTEX_AI_LOCATION_RESTRICTION = 7;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.BigtableConfig.State#com_google_pubsub_v1_BigtableConfig_State_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
