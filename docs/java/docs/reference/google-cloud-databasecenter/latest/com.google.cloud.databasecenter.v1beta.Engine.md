---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Engine
title: Enum Engine (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:53.378097+00:00
---

# Enum Engine (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Engine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Engine (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum Engine extends Enum<Engine> implements ProtocolMessageEnum

Engine refers to underlying database binary running in an instance.

Protobuf enum `google.cloud.databasecenter.v1beta.Engine`

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
`ENGINE_ADB_SERVERLESS_ORACLE` |  Oracle Autonomous DB Serverless engine. `ENGINE_ADB_SERVERLESS_ORACLE = 13;`  
`ENGINE_ADB_SERVERLESS_ORACLE_VALUE` |  Oracle Autonomous DB Serverless engine. `ENGINE_ADB_SERVERLESS_ORACLE = 13;`  
`ENGINE_EXADATA_ORACLE` |  Oracle Exadata engine. `ENGINE_EXADATA_ORACLE = 12;`  
`ENGINE_EXADATA_ORACLE_VALUE` |  Oracle Exadata engine. `ENGINE_EXADATA_ORACLE = 12;`  
`ENGINE_FIRESTORE_WITH_DATASTORE_MODE` |  Firestore with datastore mode. `ENGINE_FIRESTORE_WITH_DATASTORE_MODE = 11;`  
`ENGINE_FIRESTORE_WITH_DATASTORE_MODE_VALUE` |  Firestore with datastore mode. `ENGINE_FIRESTORE_WITH_DATASTORE_MODE = 11;`  
`ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE` |  Firestore with MongoDB compatibility. `ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE = 14;`  
`ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE_VALUE` |  Firestore with MongoDB compatibility. `ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE = 14;`  
`ENGINE_FIRESTORE_WITH_NATIVE_MODE` |  Firestore with native mode. `ENGINE_FIRESTORE_WITH_NATIVE_MODE = 10;`  
`ENGINE_FIRESTORE_WITH_NATIVE_MODE_VALUE` |  Firestore with native mode. `ENGINE_FIRESTORE_WITH_NATIVE_MODE = 10;`  
`ENGINE_MEMORYSTORE_FOR_REDIS` |  Memorystore with Redis dialect. `ENGINE_MEMORYSTORE_FOR_REDIS = 8;`  
`ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER` |  Memorystore with Redis cluster dialect. `ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER = 9;`  
`ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER_VALUE` |  Memorystore with Redis cluster dialect. `ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER = 9;`  
`ENGINE_MEMORYSTORE_FOR_REDIS_VALUE` |  Memorystore with Redis dialect. `ENGINE_MEMORYSTORE_FOR_REDIS = 8;`  
`ENGINE_MYSQL` |  MySQL binary running as an engine in the database instance. `ENGINE_MYSQL = 1;`  
`ENGINE_MYSQL_VALUE` |  MySQL binary running as an engine in the database instance. `ENGINE_MYSQL = 1;`  
`ENGINE_NATIVE` |  Native database binary running as engine in instance. `ENGINE_NATIVE = 4;`  
`ENGINE_NATIVE_VALUE` |  Native database binary running as engine in instance. `ENGINE_NATIVE = 4;`  
`ENGINE_OTHER` |  Other refers to rest of other database engine. This is to be when engine is known, but it is not present in this enum. `ENGINE_OTHER = 6;`  
`ENGINE_OTHER_VALUE` |  Other refers to rest of other database engine. This is to be when engine is known, but it is not present in this enum. `ENGINE_OTHER = 6;`  
`ENGINE_POSTGRES` |  Postgres binary running as engine in database instance. `ENGINE_POSTGRES = 2;`  
`ENGINE_POSTGRES_VALUE` |  Postgres binary running as engine in database instance. `ENGINE_POSTGRES = 2;`  
`ENGINE_SQL_SERVER` |  SQLServer binary running as engine in database instance. `ENGINE_SQL_SERVER = 3;`  
`ENGINE_SQL_SERVER_VALUE` |  SQLServer binary running as engine in database instance. `ENGINE_SQL_SERVER = 3;`  
`ENGINE_UNSPECIFIED` |  UNSPECIFIED means engine type is not known or available. `ENGINE_UNSPECIFIED = 0;`  
`ENGINE_UNSPECIFIED_VALUE` |  UNSPECIFIED means engine type is not known or available. `ENGINE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Engine#com_google_cloud_databasecenter_v1beta_Engine_forNumber_int_) instead._  
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
