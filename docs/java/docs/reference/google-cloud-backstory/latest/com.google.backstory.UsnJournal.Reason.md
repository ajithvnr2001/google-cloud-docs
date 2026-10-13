---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.UsnJournal.Reason
title: Enum UsnJournal.Reason (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:34.233515+00:00
---

# Enum UsnJournal.Reason (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.UsnJournal.Reason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum UsnJournal.Reason (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public enum UsnJournal.Reason extends Enum<UsnJournal.Reason> implements ProtocolMessageEnum

The reason for the USN journal entry.

Protobuf enum `google.backstory.UsnJournal.Reason`

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
`BASIC_INFO_CHANGE` |  Basic info change reason. `BASIC_INFO_CHANGE = 14;`  
`BASIC_INFO_CHANGE_VALUE` |  Basic info change reason. `BASIC_INFO_CHANGE = 14;`  
`CLOSE` |  Close reason. `CLOSE = 22;`  
`CLOSE_VALUE` |  Close reason. `CLOSE = 22;`  
`COMPRESSION_CHANGE` |  Compression change reason. `COMPRESSION_CHANGE = 16;`  
`COMPRESSION_CHANGE_VALUE` |  Compression change reason. `COMPRESSION_CHANGE = 16;`  
`DATA_EXTEND` |  Data extend reason. `DATA_EXTEND = 2;`  
`DATA_EXTEND_VALUE` |  Data extend reason. `DATA_EXTEND = 2;`  
`DATA_OVERWRITE` |  Data overwrite reason. `DATA_OVERWRITE = 1;`  
`DATA_OVERWRITE_VALUE` |  Data overwrite reason. `DATA_OVERWRITE = 1;`  
`DATA_TRUNCATION` |  Data truncation reason. `DATA_TRUNCATION = 3;`  
`DATA_TRUNCATION_VALUE` |  Data truncation reason. `DATA_TRUNCATION = 3;`  
`EA_CHANGE` |  EA change reason. `EA_CHANGE = 9;`  
`EA_CHANGE_VALUE` |  EA change reason. `EA_CHANGE = 9;`  
`ENCRYPTION_CHANGE` |  Encryption change reason. `ENCRYPTION_CHANGE = 17;`  
`ENCRYPTION_CHANGE_VALUE` |  Encryption change reason. `ENCRYPTION_CHANGE = 17;`  
`FILE_CREATE` |  File create reason. `FILE_CREATE = 7;`  
`FILE_CREATE_VALUE` |  File create reason. `FILE_CREATE = 7;`  
`FILE_DELETE` |  File delete reason. `FILE_DELETE = 8;`  
`FILE_DELETE_VALUE` |  File delete reason. `FILE_DELETE = 8;`  
`HARD_LINK_CHANGE` |  Hard link change reason. `HARD_LINK_CHANGE = 15;`  
`HARD_LINK_CHANGE_VALUE` |  Hard link change reason. `HARD_LINK_CHANGE = 15;`  
`INDEXABLE_CHANGE` |  Indexable change reason. `INDEXABLE_CHANGE = 13;`  
`INDEXABLE_CHANGE_VALUE` |  Indexable change reason. `INDEXABLE_CHANGE = 13;`  
`NAMED_DATA_EXTEND` |  Named data extend reason. `NAMED_DATA_EXTEND = 5;`  
`NAMED_DATA_EXTEND_VALUE` |  Named data extend reason. `NAMED_DATA_EXTEND = 5;`  
`NAMED_DATA_OVERWRITE` |  Named data overwrite reason. `NAMED_DATA_OVERWRITE = 4;`  
`NAMED_DATA_OVERWRITE_VALUE` |  Named data overwrite reason. `NAMED_DATA_OVERWRITE = 4;`  
`NAMED_DATA_TRUNCATION` |  Named data truncation reason. `NAMED_DATA_TRUNCATION = 6;`  
`NAMED_DATA_TRUNCATION_VALUE` |  Named data truncation reason. `NAMED_DATA_TRUNCATION = 6;`  
`OBJECT_ID_CHANGE` |  Object ID change reason. `OBJECT_ID_CHANGE = 18;`  
`OBJECT_ID_CHANGE_VALUE` |  Object ID change reason. `OBJECT_ID_CHANGE = 18;`  
`REASON_UNSPECIFIED` |  Unspecified reason. `REASON_UNSPECIFIED = 0;`  
`REASON_UNSPECIFIED_VALUE` |  Unspecified reason. `REASON_UNSPECIFIED = 0;`  
`RENAME_NEW_NAME` |  Rename new name reason. `RENAME_NEW_NAME = 12;`  
`RENAME_NEW_NAME_VALUE` |  Rename new name reason. `RENAME_NEW_NAME = 12;`  
`RENAME_OLD_NAME` |  Rename old name reason. `RENAME_OLD_NAME = 11;`  
`RENAME_OLD_NAME_VALUE` |  Rename old name reason. `RENAME_OLD_NAME = 11;`  
`REPARSE_POINT_CHANGE` |  Reparse point change reason. `REPARSE_POINT_CHANGE = 19;`  
`REPARSE_POINT_CHANGE_VALUE` |  Reparse point change reason. `REPARSE_POINT_CHANGE = 19;`  
`SECURITY_CHANGE` |  Security change reason. `SECURITY_CHANGE = 10;`  
`SECURITY_CHANGE_VALUE` |  Security change reason. `SECURITY_CHANGE = 10;`  
`STREAM_CHANGE` |  Stream change reason. `STREAM_CHANGE = 20;`  
`STREAM_CHANGE_VALUE` |  Stream change reason. `STREAM_CHANGE = 20;`  
`TRANSACTED_CHANGE` |  Transacted change reason. `TRANSACTED_CHANGE = 21;`  
`TRANSACTED_CHANGE_VALUE` |  Transacted change reason. `TRANSACTED_CHANGE = 21;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.UsnJournal.Reason#com_google_backstory_UsnJournal_Reason_forNumber_int_) instead._  
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
