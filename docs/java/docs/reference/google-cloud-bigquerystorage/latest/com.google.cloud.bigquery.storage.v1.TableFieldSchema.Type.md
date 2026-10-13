---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.Type
title: Enum TableFieldSchema.Type (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:45.758425+00:00
---

# Enum TableFieldSchema.Type (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum TableFieldSchema.Type (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public enum TableFieldSchema.Type extends Enum<TableFieldSchema.Type> implements ProtocolMessageEnum

Protobuf enum `google.cloud.bigquery.storage.v1.TableFieldSchema.Type`

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
`BIGNUMERIC` |  BigNumeric value `BIGNUMERIC = 13;`  
`BIGNUMERIC_VALUE` |  BigNumeric value `BIGNUMERIC = 13;`  
`BOOL` |  2-valued `BOOL = 6;`  
`BOOL_VALUE` |  2-valued `BOOL = 6;`  
`BYTES` |  64K, Binary `BYTES = 5;`  
`BYTES_VALUE` |  64K, Binary `BYTES = 5;`  
`DATE` |  Civil date - Year, Month, Day `DATE = 8;`  
`DATETIME` |  Combination of civil date and civil time `DATETIME = 10;`  
`DATETIME_VALUE` |  Combination of civil date and civil time `DATETIME = 10;`  
`DATE_VALUE` |  Civil date - Year, Month, Day `DATE = 8;`  
`DOUBLE` |  64-bit IEEE floating point `DOUBLE = 3;`  
`DOUBLE_VALUE` |  64-bit IEEE floating point `DOUBLE = 3;`  
`GEOGRAPHY` |  Geography object `GEOGRAPHY = 11;`  
`GEOGRAPHY_VALUE` |  Geography object `GEOGRAPHY = 11;`  
`INT64` |  64-bit signed `INT64 = 2;`  
`INT64_VALUE` |  64-bit signed `INT64 = 2;`  
`INTERVAL` |  Interval `INTERVAL = 14;`  
`INTERVAL_VALUE` |  Interval `INTERVAL = 14;`  
`JSON` |  JSON, String `JSON = 15;`  
`JSON_VALUE` |  JSON, String `JSON = 15;`  
`NUMERIC` |  Numeric value `NUMERIC = 12;`  
`NUMERIC_VALUE` |  Numeric value `NUMERIC = 12;`  
`RANGE` |  RANGE `RANGE = 16;`  
`RANGE_VALUE` |  RANGE `RANGE = 16;`  
`STRING` |  64K, UTF8 `STRING = 1;`  
`STRING_VALUE` |  64K, UTF8 `STRING = 1;`  
`STRUCT` |  Aggregate type `STRUCT = 4;`  
`STRUCT_VALUE` |  Aggregate type `STRUCT = 4;`  
`TIME` |  Civil time - Hour, Minute, Second, Microseconds `TIME = 9;`  
`TIMESTAMP` |  64-bit signed usec since UTC epoch `TIMESTAMP = 7;`  
`TIMESTAMP_VALUE` |  64-bit signed usec since UTC epoch `TIMESTAMP = 7;`  
`TIME_VALUE` |  Civil time - Hour, Minute, Second, Microseconds `TIME = 9;`  
`TYPE_UNSPECIFIED` |  Illegal value `TYPE_UNSPECIFIED = 0;`  
`TYPE_UNSPECIFIED_VALUE` |  Illegal value `TYPE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableFieldSchema.Type#com_google_cloud_bigquery_storage_v1_TableFieldSchema_Type_forNumber_int_) instead._  
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
