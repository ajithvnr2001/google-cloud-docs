---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryType
title: Enum EntryType (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:11.903919+00:00
---

# Enum EntryType (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum EntryType (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public enum EntryType extends Enum<EntryType> implements ProtocolMessageEnum

Metadata automatically ingested from Google Cloud resources like BigQuery tables or Pub/Sub topics always uses enum values from `EntryType` as the type of entry.

Other sources of metadata like Hive or Oracle databases can identify the type by either using one of the enum values from `EntryType` (for example, `FILESET` for a Cloud Storage fileset) or specifying a custom value using the `Entry` field `user_specified_type`. For more information, see [Surface files from Cloud Storage with fileset entries](https://docs.cloud.google.com/data-catalog/docs/how-to/filesets) or [Create custom entries for your data sources](https://docs.cloud.google.com/data-catalog/docs/how-to/custom-entries).

Protobuf enum `google.cloud.datacatalog.v1.EntryType`

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
`CLUSTER` |  A group of servers that work together. For example, a Kafka cluster. `CLUSTER = 6;`  
`CLUSTER_VALUE` |  A group of servers that work together. For example, a Kafka cluster. `CLUSTER = 6;`  
`DASHBOARD` |  A Dashboard, for example from Looker. `DASHBOARD = 16;`  
`DASHBOARD_VALUE` |  A Dashboard, for example from Looker. `DASHBOARD = 16;`  
`DATABASE` |  A database. `DATABASE = 7;`  
`DATABASE_SCHEMA` |  Schema within a relational database. `DATABASE_SCHEMA = 15;`  
`DATABASE_SCHEMA_VALUE` |  Schema within a relational database. `DATABASE_SCHEMA = 15;`  
`DATABASE_VALUE` |  A database. `DATABASE = 7;`  
`DATA_SOURCE_CONNECTION` |  Connection to a data source. For example, a BigQuery connection. `DATA_SOURCE_CONNECTION = 8;`  
`DATA_SOURCE_CONNECTION_VALUE` |  Connection to a data source. For example, a BigQuery connection. `DATA_SOURCE_CONNECTION = 8;`  
`DATA_STREAM` |  An entry type for streaming entries. For example, a Pub/Sub topic. `DATA_STREAM = 3;`  
`DATA_STREAM_VALUE` |  An entry type for streaming entries. For example, a Pub/Sub topic. `DATA_STREAM = 3;`  
`ENTRY_TYPE_UNSPECIFIED` |  Default unknown type. `ENTRY_TYPE_UNSPECIFIED = 0;`  
`ENTRY_TYPE_UNSPECIFIED_VALUE` |  Default unknown type. `ENTRY_TYPE_UNSPECIFIED = 0;`  
`EXPLORE` |  A Looker Explore. For more information, see [Looker Explore API](https://developers.looker.com/api/explorer/4.0/methods/LookmlModel/lookml_model_explore). `EXPLORE = 17;`  
`EXPLORE_VALUE` |  A Looker Explore. For more information, see [Looker Explore API](https://developers.looker.com/api/explorer/4.0/methods/LookmlModel/lookml_model_explore). `EXPLORE = 17;`  
`FEATURE_GROUP` |  Feature Group resource in Vertex AI Feature Store. `FEATURE_GROUP = 21;`  
`FEATURE_GROUP_VALUE` |  Feature Group resource in Vertex AI Feature Store. `FEATURE_GROUP = 21;`  
`FEATURE_ONLINE_STORE` |  Feature Online Store resource in Vertex AI Feature Store. `FEATURE_ONLINE_STORE = 19;`  
`FEATURE_ONLINE_STORE_VALUE` |  Feature Online Store resource in Vertex AI Feature Store. `FEATURE_ONLINE_STORE = 19;`  
`FEATURE_VIEW` |  Feature View resource in Vertex AI Feature Store. `FEATURE_VIEW = 20;`  
`FEATURE_VIEW_VALUE` |  Feature View resource in Vertex AI Feature Store. `FEATURE_VIEW = 20;`  
`FILESET` |  An entry type for a set of files or objects. For example, a Cloud Storage fileset. `FILESET = 4;`  
`FILESET_VALUE` |  An entry type for a set of files or objects. For example, a Cloud Storage fileset. `FILESET = 4;`  
`LAKE` |  A Dataplex lake. `LAKE = 10;`  
`LAKE_VALUE` |  A Dataplex lake. `LAKE = 10;`  
`LOOK` |  A Looker Look. For more information, see [Looker Look API](https://developers.looker.com/api/explorer/4.0/methods/Look). `LOOK = 18;`  
`LOOK_VALUE` |  A Looker Look. For more information, see [Looker Look API](https://developers.looker.com/api/explorer/4.0/methods/Look). `LOOK = 18;`  
`MODEL` |  The type of models. For more information, see [Supported models in BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#supported_models). `MODEL = 5;`  
`MODEL_VALUE` |  The type of models. For more information, see [Supported models in BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#supported_models). `MODEL = 5;`  
`ROUTINE` |  Routine, for example, a BigQuery routine. `ROUTINE = 9;`  
`ROUTINE_VALUE` |  Routine, for example, a BigQuery routine. `ROUTINE = 9;`  
`SERVICE` |  A service, for example, a Dataproc Metastore service. `SERVICE = 14;`  
`SERVICE_VALUE` |  A service, for example, a Dataproc Metastore service. `SERVICE = 14;`  
`TABLE` |  The entry type that has a GoogleSQL schema, including logical views. `TABLE = 2;`  
`TABLE_VALUE` |  The entry type that has a GoogleSQL schema, including logical views. `TABLE = 2;`  
`UNRECOGNIZED` |   
`ZONE` |  A Dataplex zone. `ZONE = 11;`  
`ZONE_VALUE` |  A Dataplex zone. `ZONE = 11;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryType#com_google_cloud_datacatalog_v1_EntryType_forNumber_int_) instead._  
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

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
