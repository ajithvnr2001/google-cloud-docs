---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError.StorageErrorCode
title: Enum StorageError.StorageErrorCode (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:45.263262+00:00
---

# Enum StorageError.StorageErrorCode (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError.StorageErrorCode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum StorageError.StorageErrorCode (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public enum StorageError.StorageErrorCode extends Enum<StorageError.StorageErrorCode> implements ProtocolMessageEnum

Error code for `StorageError`.

Protobuf enum `google.cloud.bigquery.storage.v1.StorageError.StorageErrorCode`

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
`CMEK_ENCRYPTION_ERROR` |  There is an encryption error while using customer-managed encryption key. `CMEK_ENCRYPTION_ERROR = 12;`  
`CMEK_ENCRYPTION_ERROR_VALUE` |  There is an encryption error while using customer-managed encryption key. `CMEK_ENCRYPTION_ERROR = 12;`  
`CMEK_NOT_PROVIDED` |  Customer-managed encryption key (CMEK) not provided for CMEK-enabled data. `CMEK_NOT_PROVIDED = 10;`  
`CMEK_NOT_PROVIDED_VALUE` |  Customer-managed encryption key (CMEK) not provided for CMEK-enabled data. `CMEK_NOT_PROVIDED = 10;`  
`INVALID_CMEK_PROVIDED` |  Customer-managed encryption key (CMEK) was incorrectly provided. `INVALID_CMEK_PROVIDED = 11;`  
`INVALID_CMEK_PROVIDED_VALUE` |  Customer-managed encryption key (CMEK) was incorrectly provided. `INVALID_CMEK_PROVIDED = 11;`  
`INVALID_STREAM_STATE` |  Invalid Stream state. For example, you try to commit a stream that is not finalized or is garbaged. `INVALID_STREAM_STATE = 5;`  
`INVALID_STREAM_STATE_VALUE` |  Invalid Stream state. For example, you try to commit a stream that is not finalized or is garbaged. `INVALID_STREAM_STATE = 5;`  
`INVALID_STREAM_TYPE` |  Invalid Stream type. For example, you try to commit a stream that is not pending. `INVALID_STREAM_TYPE = 4;`  
`INVALID_STREAM_TYPE_VALUE` |  Invalid Stream type. For example, you try to commit a stream that is not pending. `INVALID_STREAM_TYPE = 4;`  
`KMS_PERMISSION_DENIED` |  Permission denied while using customer-managed encryption key. `KMS_PERMISSION_DENIED = 14;`  
`KMS_PERMISSION_DENIED_VALUE` |  Permission denied while using customer-managed encryption key. `KMS_PERMISSION_DENIED = 14;`  
`KMS_SERVICE_ERROR` |  Key Management Service (KMS) service returned an error, which can be retried. `KMS_SERVICE_ERROR = 13;`  
`KMS_SERVICE_ERROR_VALUE` |  Key Management Service (KMS) service returned an error, which can be retried. `KMS_SERVICE_ERROR = 13;`  
`OFFSET_ALREADY_EXISTS` |  Offset already exists. `OFFSET_ALREADY_EXISTS = 8;`  
`OFFSET_ALREADY_EXISTS_VALUE` |  Offset already exists. `OFFSET_ALREADY_EXISTS = 8;`  
`OFFSET_OUT_OF_RANGE` |  Offset out of range. `OFFSET_OUT_OF_RANGE = 9;`  
`OFFSET_OUT_OF_RANGE_VALUE` |  Offset out of range. `OFFSET_OUT_OF_RANGE = 9;`  
`SCHEMA_MISMATCH_EXTRA_FIELDS` |  There is a schema mismatch and it is caused by user schema has extra field than bigquery schema. `SCHEMA_MISMATCH_EXTRA_FIELDS = 7;`  
`SCHEMA_MISMATCH_EXTRA_FIELDS_VALUE` |  There is a schema mismatch and it is caused by user schema has extra field than bigquery schema. `SCHEMA_MISMATCH_EXTRA_FIELDS = 7;`  
`STORAGE_ERROR_CODE_UNSPECIFIED` |  Default error. `STORAGE_ERROR_CODE_UNSPECIFIED = 0;`  
`STORAGE_ERROR_CODE_UNSPECIFIED_VALUE` |  Default error. `STORAGE_ERROR_CODE_UNSPECIFIED = 0;`  
`STREAM_ALREADY_COMMITTED` |  Stream is already committed. `STREAM_ALREADY_COMMITTED = 2;`  
`STREAM_ALREADY_COMMITTED_VALUE` |  Stream is already committed. `STREAM_ALREADY_COMMITTED = 2;`  
`STREAM_FINALIZED` |  Stream is finalized. `STREAM_FINALIZED = 6;`  
`STREAM_FINALIZED_VALUE` |  Stream is finalized. `STREAM_FINALIZED = 6;`  
`STREAM_NOT_FOUND` |  Stream is not found. `STREAM_NOT_FOUND = 3;`  
`STREAM_NOT_FOUND_VALUE` |  Stream is not found. `STREAM_NOT_FOUND = 3;`  
`TABLE_NOT_FOUND` |  Table is not found in the system. `TABLE_NOT_FOUND = 1;`  
`TABLE_NOT_FOUND_VALUE` |  Table is not found in the system. `TABLE_NOT_FOUND = 1;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError.StorageErrorCode#com_google_cloud_bigquery_storage_v1_StorageError_StorageErrorCode_forNumber_int_) instead._  
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
