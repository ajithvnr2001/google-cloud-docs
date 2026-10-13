---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ServiceConstants.Values
title: Enum ServiceConstants.Values (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:21.647194+00:00
---

# Enum ServiceConstants.Values (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ServiceConstants.Values

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum ServiceConstants.Values (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public enum ServiceConstants.Values extends Enum<ServiceConstants.Values> implements ProtocolMessageEnum

A collection of constant values meaningful to the Storage API.

Protobuf enum `google.storage.v2.ServiceConstants.Values`

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
`MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES` |  The maximum total bytes that can be populated into all bucket metadata fields. 20 KiB. `MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES = 20480;`  
`MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES_VALUE` |  The maximum total bytes that can be populated into all bucket metadata fields. 20 KiB. `MAX_BUCKET_METADATA_TOTAL_SIZE_BYTES = 20480;`  
`MAX_CUSTOM_METADATA_FIELD_NAME_BYTES` |  The maximum length field name that can be sent in a single custom metadata field. 1 KiB. `MAX_CUSTOM_METADATA_FIELD_NAME_BYTES = 1024;`  
`MAX_CUSTOM_METADATA_FIELD_NAME_BYTES_VALUE` |  The maximum length field name that can be sent in a single custom metadata field. 1 KiB. `MAX_CUSTOM_METADATA_FIELD_NAME_BYTES = 1024;`  
`MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES` |  The maximum length field value that can be sent in a single custom_metadata field. 4 KiB. `MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES = 4096;`  
`MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES_VALUE` |  The maximum length field value that can be sent in a single custom_metadata field. 4 KiB. `MAX_CUSTOM_METADATA_FIELD_VALUE_BYTES = 4096;`  
`MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES` |  The maximum total bytes that can be populated into all field names and values of the custom_metadata for one object. 8 KiB. `MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES = 8192;`  
`MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES_VALUE` |  The maximum total bytes that can be populated into all field names and values of the custom_metadata for one object. 8 KiB. `MAX_CUSTOM_METADATA_TOTAL_SIZE_BYTES = 8192;`  
`MAX_LABELS_ENTRIES_COUNT` |  The maximum number of key/value entries per bucket label. `MAX_LABELS_ENTRIES_COUNT = 64;`  
`MAX_LABELS_ENTRIES_COUNT_VALUE` |  The maximum number of key/value entries per bucket label. `MAX_LABELS_ENTRIES_COUNT = 64;`  
`MAX_LABELS_KEY_VALUE_BYTES` |  The maximum byte size of the key or value in a bucket label map. `MAX_LABELS_KEY_VALUE_BYTES = 128;`  
`MAX_LABELS_KEY_VALUE_BYTES_VALUE` |  The maximum byte size of the key or value in a bucket label map. `MAX_LABELS_KEY_VALUE_BYTES = 128;`  
`MAX_LABELS_KEY_VALUE_LENGTH` |  The maximum character length of the key or value in a bucket label map. `MAX_LABELS_KEY_VALUE_LENGTH = 63;`  
`MAX_LABELS_KEY_VALUE_LENGTH_VALUE` |  The maximum character length of the key or value in a bucket label map. `MAX_LABELS_KEY_VALUE_LENGTH = 63;`  
`MAX_LIFECYCLE_RULES_PER_BUCKET` |  The maximum number of LifecycleRules that can be registered for a given bucket. `MAX_LIFECYCLE_RULES_PER_BUCKET = 100;`  
`MAX_LIFECYCLE_RULES_PER_BUCKET_VALUE` |  The maximum number of LifecycleRules that can be registered for a given bucket. `MAX_LIFECYCLE_RULES_PER_BUCKET = 100;`  
`MAX_NOTIFICATION_CONFIGS_PER_BUCKET` |  The maximum number of NotificationConfigs that can be registered for a given bucket. `MAX_NOTIFICATION_CONFIGS_PER_BUCKET = 100;`  
`MAX_NOTIFICATION_CONFIGS_PER_BUCKET_VALUE` |  The maximum number of NotificationConfigs that can be registered for a given bucket. `MAX_NOTIFICATION_CONFIGS_PER_BUCKET = 100;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTES` |  The maximum number of custom attributes per NotificationConfigs. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTES = 5;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTES_VALUE` |  The maximum number of custom attributes per NotificationConfigs. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTES = 5;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH` |  The maximum length of a custom attribute key included in NotificationConfig. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH = 256;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH_VALUE` |  The maximum length of a custom attribute key included in NotificationConfig. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_KEY_LENGTH = 256;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH` |  The maximum length of a custom attribute value included in a NotificationConfig. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH = 1024;`  
`MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH_VALUE` |  The maximum length of a custom attribute value included in a NotificationConfig. `MAX_NOTIFICATION_CUSTOM_ATTRIBUTE_VALUE_LENGTH = 1024;`  
`MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST` |  The maximum number of object IDs that can be included in a DeleteObjectsRequest. `MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST = 1000;`  
`MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST_VALUE` |  The maximum number of object IDs that can be included in a DeleteObjectsRequest. `MAX_OBJECT_IDS_PER_DELETE_OBJECTS_REQUEST = 1000;`  
`MAX_OBJECT_SIZE_MB` |  The maximum size of an object in MB - whether written in a single stream or composed from multiple other objects. 5 TiB. `MAX_OBJECT_SIZE_MB = 5242880;`  
`MAX_OBJECT_SIZE_MB_VALUE` |  The maximum size of an object in MB - whether written in a single stream or composed from multiple other objects. 5 TiB. `MAX_OBJECT_SIZE_MB = 5242880;`  
`MAX_READ_CHUNK_BYTES` |  The maximum size chunk that can be returned in a single `ReadRequest`. 2 MiB. `MAX_READ_CHUNK_BYTES = 2097152;`  
`MAX_READ_CHUNK_BYTES_VALUE` |  The maximum size chunk that can be returned in a single `ReadRequest`. 2 MiB. `MAX_READ_CHUNK_BYTES = 2097152;`  
`MAX_WRITE_CHUNK_BYTES` |  The maximum size chunk that can be sent in a single WriteObjectRequest. 2 MiB. `MAX_WRITE_CHUNK_BYTES = 2097152;`  
`MAX_WRITE_CHUNK_BYTES_VALUE` |  The maximum size chunk that can be sent in a single WriteObjectRequest. 2 MiB. `MAX_WRITE_CHUNK_BYTES = 2097152;`  
`SPLIT_TOKEN_MAX_VALID_DAYS` |  The maximum number of days for which a token returned by the GetListObjectsSplitPoints RPC is valid. `SPLIT_TOKEN_MAX_VALID_DAYS = 14;`  
`SPLIT_TOKEN_MAX_VALID_DAYS_VALUE` |  The maximum number of days for which a token returned by the GetListObjectsSplitPoints RPC is valid. `SPLIT_TOKEN_MAX_VALID_DAYS = 14;`  
`UNRECOGNIZED` |   
`VALUES_UNSPECIFIED` |  Unused. Proto3 requires first enum to be 0. `VALUES_UNSPECIFIED = 0;`  
`VALUES_UNSPECIFIED_VALUE` |  Unused. Proto3 requires first enum to be 0. `VALUES_UNSPECIFIED = 0;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ServiceConstants.Values#com_google_storage_v2_ServiceConstants_Values_forNumber_int_) instead._  
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
