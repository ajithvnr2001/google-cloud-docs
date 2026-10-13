---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.ParameterType
title: Enum ParameterType (0.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:15.941872+00:00
---

# Enum ParameterType (0.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.ParameterType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum ParameterType (0.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.103.0 (latest)  0.99.0  0.98.0  0.97.0  0.95.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.68.0  0.67.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.5.0 
    
    
    public enum ParameterType extends Enum<ParameterType> implements ProtocolMessageEnum

ParameterType specifies what kind of input we need for this parameter.

Protobuf enum `google.dataflow.v1beta3.ParameterType`

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
`BIGQUERY_TABLE` |  The parameter specifies a BigQuery table. `BIGQUERY_TABLE = 10;`  
`BIGQUERY_TABLE_VALUE` |  The parameter specifies a BigQuery table. `BIGQUERY_TABLE = 10;`  
`BOOLEAN` |  The parameter specifies a boolean input. `BOOLEAN = 17;`  
`BOOLEAN_VALUE` |  The parameter specifies a boolean input. `BOOLEAN = 17;`  
`DEFAULT` |  Default input type. `DEFAULT = 0;`  
`DEFAULT_VALUE` |  Default input type. `DEFAULT = 0;`  
`ENUM` |  The parameter specifies an enum input. `ENUM = 18;`  
`ENUM_VALUE` |  The parameter specifies an enum input. `ENUM = 18;`  
`GCS_READ_BUCKET` |  The parameter specifies a Cloud Storage Bucket to read from. `GCS_READ_BUCKET = 2;`  
`GCS_READ_BUCKET_VALUE` |  The parameter specifies a Cloud Storage Bucket to read from. `GCS_READ_BUCKET = 2;`  
`GCS_READ_FILE` |  The parameter specifies a Cloud Storage file path to read from. `GCS_READ_FILE = 4;`  
`GCS_READ_FILE_VALUE` |  The parameter specifies a Cloud Storage file path to read from. `GCS_READ_FILE = 4;`  
`GCS_READ_FOLDER` |  The parameter specifies a Cloud Storage folder path to read from. `GCS_READ_FOLDER = 6;`  
`GCS_READ_FOLDER_VALUE` |  The parameter specifies a Cloud Storage folder path to read from. `GCS_READ_FOLDER = 6;`  
`GCS_WRITE_BUCKET` |  The parameter specifies a Cloud Storage Bucket to write to. `GCS_WRITE_BUCKET = 3;`  
`GCS_WRITE_BUCKET_VALUE` |  The parameter specifies a Cloud Storage Bucket to write to. `GCS_WRITE_BUCKET = 3;`  
`GCS_WRITE_FILE` |  The parameter specifies a Cloud Storage file path to write to. `GCS_WRITE_FILE = 5;`  
`GCS_WRITE_FILE_VALUE` |  The parameter specifies a Cloud Storage file path to write to. `GCS_WRITE_FILE = 5;`  
`GCS_WRITE_FOLDER` |  The parameter specifies a Cloud Storage folder to write to. `GCS_WRITE_FOLDER = 7;`  
`GCS_WRITE_FOLDER_VALUE` |  The parameter specifies a Cloud Storage folder to write to. `GCS_WRITE_FOLDER = 7;`  
`JAVASCRIPT_UDF_FILE` |  The parameter specifies a JavaScript UDF in Cloud Storage. `JAVASCRIPT_UDF_FILE = 11;`  
`JAVASCRIPT_UDF_FILE_VALUE` |  The parameter specifies a JavaScript UDF in Cloud Storage. `JAVASCRIPT_UDF_FILE = 11;`  
`KAFKA_READ_TOPIC` |  The parameter specifies the fully-qualified name of an Apache Kafka topic. This can be either a Google Managed Kafka topic or a non-managed Kafka topic. `KAFKA_READ_TOPIC = 21;`  
`KAFKA_READ_TOPIC_VALUE` |  The parameter specifies the fully-qualified name of an Apache Kafka topic. This can be either a Google Managed Kafka topic or a non-managed Kafka topic. `KAFKA_READ_TOPIC = 21;`  
`KAFKA_TOPIC` |  Deprecated. Please use KAFKA_READ_TOPIC instead. `KAFKA_TOPIC = 20 [deprecated = true];`  
`KAFKA_TOPIC_VALUE` |  Deprecated. Please use KAFKA_READ_TOPIC instead. `KAFKA_TOPIC = 20 [deprecated = true];`  
`KAFKA_WRITE_TOPIC` |  The parameter specifies the fully-qualified name of an Apache Kafka topic. This can be an existing Google Managed Kafka topic, the name for a new Google Managed Kafka topic, or an existing non-managed Kafka topic. `KAFKA_WRITE_TOPIC = 22;`  
`KAFKA_WRITE_TOPIC_VALUE` |  The parameter specifies the fully-qualified name of an Apache Kafka topic. This can be an existing Google Managed Kafka topic, the name for a new Google Managed Kafka topic, or an existing non-managed Kafka topic. `KAFKA_WRITE_TOPIC = 22;`  
`KMS_KEY_NAME` |  The parameter specifies a KMS Key name. `KMS_KEY_NAME = 14;`  
`KMS_KEY_NAME_VALUE` |  The parameter specifies a KMS Key name. `KMS_KEY_NAME = 14;`  
`MACHINE_TYPE` |  The parameter specifies a Machine Type. `MACHINE_TYPE = 13;`  
`MACHINE_TYPE_VALUE` |  The parameter specifies a Machine Type. `MACHINE_TYPE = 13;`  
`NUMBER` |  The parameter specifies a number input. `NUMBER = 19;`  
`NUMBER_VALUE` |  The parameter specifies a number input. `NUMBER = 19;`  
`PUBSUB_SUBSCRIPTION` |  The parameter specifies a Pub/Sub Subscription. `PUBSUB_SUBSCRIPTION = 9;`  
`PUBSUB_SUBSCRIPTION_VALUE` |  The parameter specifies a Pub/Sub Subscription. `PUBSUB_SUBSCRIPTION = 9;`  
`PUBSUB_TOPIC` |  The parameter specifies a Pub/Sub Topic. `PUBSUB_TOPIC = 8;`  
`PUBSUB_TOPIC_VALUE` |  The parameter specifies a Pub/Sub Topic. `PUBSUB_TOPIC = 8;`  
`SERVICE_ACCOUNT` |  The parameter specifies a Service Account email. `SERVICE_ACCOUNT = 12;`  
`SERVICE_ACCOUNT_VALUE` |  The parameter specifies a Service Account email. `SERVICE_ACCOUNT = 12;`  
`TEXT` |  The parameter specifies generic text input. `TEXT = 1;`  
`TEXT_VALUE` |  The parameter specifies generic text input. `TEXT = 1;`  
`UNRECOGNIZED` |   
`WORKER_REGION` |  The parameter specifies a Worker Region. `WORKER_REGION = 15;`  
`WORKER_REGION_VALUE` |  The parameter specifies a Worker Region. `WORKER_REGION = 15;`  
`WORKER_ZONE` |  The parameter specifies a Worker Zone. `WORKER_ZONE = 16;`  
`WORKER_ZONE_VALUE` |  The parameter specifies a Worker Zone. `WORKER_ZONE = 16;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.ParameterType#com_google_dataflow_v1beta3_ParameterType_forNumber_int_) instead._  
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
