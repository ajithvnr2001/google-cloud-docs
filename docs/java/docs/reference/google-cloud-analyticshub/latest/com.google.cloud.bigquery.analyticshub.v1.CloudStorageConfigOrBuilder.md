---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfigOrBuilder
title: Interface CloudStorageConfigOrBuilder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:21.325883+00:00
---

# Interface CloudStorageConfigOrBuilder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudStorageConfigOrBuilder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CloudStorageConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAvroConfig()
    
    
    public abstract CloudStorageConfig.AvroConfig getAvroConfig()

Optional. If set, message data will be written to Cloud Storage in Avro format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.AvroConfig avro_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.AvroConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.AvroConfig)` | The avroConfig.  
  
### getAvroConfigOrBuilder()
    
    
    public abstract CloudStorageConfig.AvroConfigOrBuilder getAvroConfigOrBuilder()

Optional. If set, message data will be written to Cloud Storage in Avro format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.AvroConfig avro_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.AvroConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.AvroConfigOrBuilder)` |   
  
### getBucket()
    
    
    public abstract String getBucket()

Required. User-provided name for the Cloud Storage bucket. The bucket must be created by the user. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements](https://cloud.google.com/storage/docs/buckets#naming).

`string bucket = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bucket.  
  
### getBucketBytes()
    
    
    public abstract ByteString getBucketBytes()

Required. User-provided name for the Cloud Storage bucket. The bucket must be created by the user. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements](https://cloud.google.com/storage/docs/buckets#naming).

`string bucket = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bucket.  
  
### getFilenameDatetimeFormat()
    
    
    public abstract String getFilenameDatetimeFormat()

Optional. User-provided format string specifying how to represent datetimes in Cloud Storage filenames. See the [datetime format guidance](https://cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_names).

`string filename_datetime_format = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filenameDatetimeFormat.  
  
### getFilenameDatetimeFormatBytes()
    
    
    public abstract ByteString getFilenameDatetimeFormatBytes()

Optional. User-provided format string specifying how to represent datetimes in Cloud Storage filenames. See the [datetime format guidance](https://cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_names).

`string filename_datetime_format = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filenameDatetimeFormat.  
  
### getFilenamePrefix()
    
    
    public abstract String getFilenamePrefix()

Optional. User-provided prefix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming).

`string filename_prefix = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filenamePrefix.  
  
### getFilenamePrefixBytes()
    
    
    public abstract ByteString getFilenamePrefixBytes()

Optional. User-provided prefix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming).

`string filename_prefix = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filenamePrefix.  
  
### getFilenameSuffix()
    
    
    public abstract String getFilenameSuffix()

Optional. User-provided suffix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming). Must not end in "/".

`string filename_suffix = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filenameSuffix.  
  
### getFilenameSuffixBytes()
    
    
    public abstract ByteString getFilenameSuffixBytes()

Optional. User-provided suffix for Cloud Storage filename. See the [object naming requirements](https://cloud.google.com/storage/docs/objects#naming). Must not end in "/".

`string filename_suffix = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filenameSuffix.  
  
### getMaxBytes()
    
    
    public abstract long getMaxBytes()

Optional. The maximum bytes that can be written to a Cloud Storage file before a new file is created. Min 1 KB, max 10 GiB. The max_bytes limit may be exceeded in cases where messages are larger than the limit.

`int64 max_bytes = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxBytes.  
  
### getMaxDuration()
    
    
    public abstract Duration getMaxDuration()

Optional. File batching settings. If no max_duration setting is specified, a max_duration of 5 minutes will be set by default. max_duration is required regardless of whether other file batching settings are specified.

The maximum duration that can elapse before a new Cloud Storage file is created. Min 1 minute, max 10 minutes, default 5 minutes. May not exceed the subscription's acknowledgement deadline.

`.google.protobuf.Duration max_duration = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maxDuration.  
  
### getMaxDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getMaxDurationOrBuilder()

Optional. File batching settings. If no max_duration setting is specified, a max_duration of 5 minutes will be set by default. max_duration is required regardless of whether other file batching settings are specified.

The maximum duration that can elapse before a new Cloud Storage file is created. Min 1 minute, max 10 minutes, default 5 minutes. May not exceed the subscription's acknowledgement deadline.

`.google.protobuf.Duration max_duration = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMaxMessages()
    
    
    public abstract long getMaxMessages()

Optional. The maximum number of messages that can be written to a Cloud Storage file before a new file is created. Min 1000 messages.

`int64 max_messages = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxMessages.  
  
### getOutputFormatCase()
    
    
    public abstract CloudStorageConfig.OutputFormatCase getOutputFormatCase()

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.OutputFormatCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.OutputFormatCase)` |   
  
### getServiceAccountEmail()
    
    
    public abstract String getServiceAccountEmail()

Optional. The service account to use to write to Cloud Storage. The subscription creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used.

`string service_account_email = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccountEmail.  
  
### getServiceAccountEmailBytes()
    
    
    public abstract ByteString getServiceAccountEmailBytes()

Optional. The service account to use to write to Cloud Storage. The subscription creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used.

`string service_account_email = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccountEmail.  
  
### getTextConfig()
    
    
    public abstract CloudStorageConfig.TextConfig getTextConfig()

Optional. If set, message data will be written to Cloud Storage in text format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.TextConfig text_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.TextConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.TextConfig)` | The textConfig.  
  
### getTextConfigOrBuilder()
    
    
    public abstract CloudStorageConfig.TextConfigOrBuilder getTextConfigOrBuilder()

Optional. If set, message data will be written to Cloud Storage in text format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.TextConfig text_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudStorageConfig.TextConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.TextConfigOrBuilder)` |   
  
### hasAvroConfig()
    
    
    public abstract boolean hasAvroConfig()

Optional. If set, message data will be written to Cloud Storage in Avro format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.AvroConfig avro_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroConfig field is set.  
  
### hasMaxDuration()
    
    
    public abstract boolean hasMaxDuration()

Optional. File batching settings. If no max_duration setting is specified, a max_duration of 5 minutes will be set by default. max_duration is required regardless of whether other file batching settings are specified.

The maximum duration that can elapse before a new Cloud Storage file is created. Min 1 minute, max 10 minutes, default 5 minutes. May not exceed the subscription's acknowledgement deadline.

`.google.protobuf.Duration max_duration = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxDuration field is set.  
  
### hasTextConfig()
    
    
    public abstract boolean hasTextConfig()

Optional. If set, message data will be written to Cloud Storage in text format.

` .google.cloud.bigquery.analyticshub.v1.CloudStorageConfig.TextConfig text_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
