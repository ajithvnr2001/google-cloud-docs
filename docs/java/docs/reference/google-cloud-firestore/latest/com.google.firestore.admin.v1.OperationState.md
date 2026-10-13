---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.OperationState
title: Enum OperationState (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:36.575138+00:00
---

# Enum OperationState (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.OperationState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum OperationState (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public enum OperationState extends Enum<OperationState> implements ProtocolMessageEnum

Describes the state of the operation.

Protobuf enum `google.firestore.admin.v1.OperationState`

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
`CANCELLED` |  Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation. `CANCELLED = 7;`  
`CANCELLED_VALUE` |  Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation. `CANCELLED = 7;`  
`CANCELLING` |  Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation. `CANCELLING = 3;`  
`CANCELLING_VALUE` |  Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation. `CANCELLING = 3;`  
`FAILED` |  Request has finished being processed, but encountered an error. `FAILED = 6;`  
`FAILED_VALUE` |  Request has finished being processed, but encountered an error. `FAILED = 6;`  
`FINALIZING` |  Request has been processed and is in its finalization stage. `FINALIZING = 4;`  
`FINALIZING_VALUE` |  Request has been processed and is in its finalization stage. `FINALIZING = 4;`  
`INITIALIZING` |  Request is being prepared for processing. `INITIALIZING = 1;`  
`INITIALIZING_VALUE` |  Request is being prepared for processing. `INITIALIZING = 1;`  
`OPERATION_STATE_UNSPECIFIED` |  Unspecified. `OPERATION_STATE_UNSPECIFIED = 0;`  
`OPERATION_STATE_UNSPECIFIED_VALUE` |  Unspecified. `OPERATION_STATE_UNSPECIFIED = 0;`  
`PROCESSING` |  Request is actively being processed. `PROCESSING = 2;`  
`PROCESSING_VALUE` |  Request is actively being processed. `PROCESSING = 2;`  
`SUCCESSFUL` |  Request has completed successfully. `SUCCESSFUL = 5;`  
`SUCCESSFUL_VALUE` |  Request has completed successfully. `SUCCESSFUL = 5;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.OperationState#com_google_firestore_admin_v1_OperationState_forNumber_int_) instead._  
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
