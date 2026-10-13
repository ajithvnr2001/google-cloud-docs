---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.MigratingVm.State
title: Enum MigratingVm.State (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:10.656189+00:00
---

# Enum MigratingVm.State (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.MigratingVm.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum MigratingVm.State (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public enum MigratingVm.State extends Enum<MigratingVm.State> implements ProtocolMessageEnum

The possible values of the state/health of source VM.

Protobuf enum `google.cloud.vmmigration.v1.MigratingVm.State`

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
`ACTIVE` |  The replication is active, and it's running or scheduled to run. `ACTIVE = 4;`  
`ACTIVE_VALUE` |  The replication is active, and it's running or scheduled to run. `ACTIVE = 4;`  
`CUTOVER` |  The source VM was stopped and replicated. The replication is currently paused. `CUTOVER = 8;`  
`CUTOVER_VALUE` |  The source VM was stopped and replicated. The replication is currently paused. `CUTOVER = 8;`  
`CUTTING_OVER` |  The source VM is being turned off, and a final replication is currently running. `CUTTING_OVER = 7;`  
`CUTTING_OVER_VALUE` |  The source VM is being turned off, and a final replication is currently running. `CUTTING_OVER = 7;`  
`ERROR` |  The replication process encountered an unrecoverable error and was aborted. `ERROR = 13;`  
`ERROR_VALUE` |  The replication process encountered an unrecoverable error and was aborted. `ERROR = 13;`  
`EXPIRED` |  The migrating VM has passed its expiration date. It might be possible to bring it back to "Active" state by updating the TTL field. For more information, see the documentation. `EXPIRED = 14;`  
`EXPIRED_VALUE` |  The migrating VM has passed its expiration date. It might be possible to bring it back to "Active" state by updating the TTL field. For more information, see the documentation. `EXPIRED = 14;`  
`FINALIZED` |  The replication process is done. The migrating VM is finalized and no longer consumes billable resources. `FINALIZED = 12;`  
`FINALIZED_EXPIRED` |  The migrating VM's has been finalized and migration resources have been removed. `FINALIZED_EXPIRED = 17;`  
`FINALIZED_EXPIRED_VALUE` |  The migrating VM's has been finalized and migration resources have been removed. `FINALIZED_EXPIRED = 17;`  
`FINALIZED_VALUE` |  The replication process is done. The migrating VM is finalized and no longer consumes billable resources. `FINALIZED = 12;`  
`FINALIZING` |  The migrating VM is being finalized and migration resources are being removed. `FINALIZING = 11;`  
`FINALIZING_VALUE` |  The migrating VM is being finalized and migration resources are being removed. `FINALIZING = 11;`  
`FINAL_SYNC` |  A cutover job is active and replication cycle is running the final sync. `FINAL_SYNC = 9;`  
`FINAL_SYNC_VALUE` |  A cutover job is active and replication cycle is running the final sync. `FINAL_SYNC = 9;`  
`FIRST_SYNC` |  Migration is going through the first sync cycle. `FIRST_SYNC = 3;`  
`FIRST_SYNC_VALUE` |  Migration is going through the first sync cycle. `FIRST_SYNC = 3;`  
`PAUSED` |  The replication was paused by the user and no cycles are scheduled to run. `PAUSED = 10;`  
`PAUSED_VALUE` |  The replication was paused by the user and no cycles are scheduled to run. `PAUSED = 10;`  
`PENDING` |  The VM in the source is being verified. `PENDING = 1;`  
`PENDING_VALUE` |  The VM in the source is being verified. `PENDING = 1;`  
`READY` |  The source VM was verified, and it's ready to start replication. `READY = 2;`  
`READY_VALUE` |  The source VM was verified, and it's ready to start replication. `READY = 2;`  
`STATE_UNSPECIFIED` |  The state was not sampled by the health checks yet. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  The state was not sampled by the health checks yet. `STATE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.MigratingVm.State#com_google_cloud_vmmigration_v1_MigratingVm_State_forNumber_int_) instead._  
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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
