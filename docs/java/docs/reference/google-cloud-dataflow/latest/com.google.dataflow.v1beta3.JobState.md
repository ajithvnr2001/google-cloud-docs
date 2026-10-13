---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobState
title: Enum JobState (0.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:25.529432+00:00
---

# Enum JobState (0.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum JobState (0.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.103.0 (latest)  0.99.0  0.98.0  0.97.0  0.95.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.68.0  0.67.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.5.0 
    
    
    public enum JobState extends Enum<JobState> implements ProtocolMessageEnum

Describes the overall state of a google.dataflow.v1beta3.Job.

Protobuf enum `google.dataflow.v1beta3.JobState`

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
`JOB_STATE_CANCELLED` |  `JOB_STATE_CANCELLED` indicates that the job has been explicitly cancelled. This is a terminal job state. This state may only be set via a Cloud Dataflow `UpdateJob` call, and only if the job has not yet reached another terminal state. `JOB_STATE_CANCELLED = 5;`  
`JOB_STATE_CANCELLED_VALUE` |  `JOB_STATE_CANCELLED` indicates that the job has been explicitly cancelled. This is a terminal job state. This state may only be set via a Cloud Dataflow `UpdateJob` call, and only if the job has not yet reached another terminal state. `JOB_STATE_CANCELLED = 5;`  
`JOB_STATE_CANCELLING` |  `JOB_STATE_CANCELLING` indicates that the job has been explicitly cancelled and is in the process of stopping. Jobs that are cancelling may only transition to `JOB_STATE_CANCELLED` or `JOB_STATE_FAILED`. `JOB_STATE_CANCELLING = 10;`  
`JOB_STATE_CANCELLING_VALUE` |  `JOB_STATE_CANCELLING` indicates that the job has been explicitly cancelled and is in the process of stopping. Jobs that are cancelling may only transition to `JOB_STATE_CANCELLED` or `JOB_STATE_FAILED`. `JOB_STATE_CANCELLING = 10;`  
`JOB_STATE_DONE` |  `JOB_STATE_DONE` indicates that the job has successfully completed. This is a terminal job state. This state may be set by the Cloud Dataflow service, as a transition from `JOB_STATE_RUNNING`. It may also be set via a Cloud Dataflow `UpdateJob` call, if the job has not yet reached a terminal state. `JOB_STATE_DONE = 3;`  
`JOB_STATE_DONE_VALUE` |  `JOB_STATE_DONE` indicates that the job has successfully completed. This is a terminal job state. This state may be set by the Cloud Dataflow service, as a transition from `JOB_STATE_RUNNING`. It may also be set via a Cloud Dataflow `UpdateJob` call, if the job has not yet reached a terminal state. `JOB_STATE_DONE = 3;`  
`JOB_STATE_DRAINED` |  `JOB_STATE_DRAINED` indicates that the job has been drained. A drained job terminated by stopping pulling from its input sources and processing any data that remained in-flight when draining was requested. This state is a terminal state, may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_DRAINING`. `JOB_STATE_DRAINED = 8;`  
`JOB_STATE_DRAINED_VALUE` |  `JOB_STATE_DRAINED` indicates that the job has been drained. A drained job terminated by stopping pulling from its input sources and processing any data that remained in-flight when draining was requested. This state is a terminal state, may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_DRAINING`. `JOB_STATE_DRAINED = 8;`  
`JOB_STATE_DRAINING` |  `JOB_STATE_DRAINING` indicates that the job is in the process of draining. A draining job has stopped pulling from its input sources and is processing any data that remains in-flight. This state may be set via a Cloud Dataflow `UpdateJob` call, but only as a transition from `JOB_STATE_RUNNING`. Jobs that are draining may only transition to `JOB_STATE_DRAINED`, `JOB_STATE_CANCELLED`, or `JOB_STATE_FAILED`. `JOB_STATE_DRAINING = 7;`  
`JOB_STATE_DRAINING_VALUE` |  `JOB_STATE_DRAINING` indicates that the job is in the process of draining. A draining job has stopped pulling from its input sources and is processing any data that remains in-flight. This state may be set via a Cloud Dataflow `UpdateJob` call, but only as a transition from `JOB_STATE_RUNNING`. Jobs that are draining may only transition to `JOB_STATE_DRAINED`, `JOB_STATE_CANCELLED`, or `JOB_STATE_FAILED`. `JOB_STATE_DRAINING = 7;`  
`JOB_STATE_FAILED` |  `JOB_STATE_FAILED` indicates that the job has failed. This is a terminal job state. This state may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_RUNNING`. `JOB_STATE_FAILED = 4;`  
`JOB_STATE_FAILED_VALUE` |  `JOB_STATE_FAILED` indicates that the job has failed. This is a terminal job state. This state may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_RUNNING`. `JOB_STATE_FAILED = 4;`  
`JOB_STATE_PAUSED` |  `JOB_STATE_PAUSED` is not implemented yet. `JOB_STATE_PAUSED = 14;`  
`JOB_STATE_PAUSED_VALUE` |  `JOB_STATE_PAUSED` is not implemented yet. `JOB_STATE_PAUSED = 14;`  
`JOB_STATE_PAUSING` |  `JOB_STATE_PAUSING` is not implemented yet. `JOB_STATE_PAUSING = 13;`  
`JOB_STATE_PAUSING_VALUE` |  `JOB_STATE_PAUSING` is not implemented yet. `JOB_STATE_PAUSING = 13;`  
`JOB_STATE_PENDING` |  `JOB_STATE_PENDING` indicates that the job has been created but is not yet running. Jobs that are pending may only transition to `JOB_STATE_RUNNING`, or `JOB_STATE_FAILED`. `JOB_STATE_PENDING = 9;`  
`JOB_STATE_PENDING_VALUE` |  `JOB_STATE_PENDING` indicates that the job has been created but is not yet running. Jobs that are pending may only transition to `JOB_STATE_RUNNING`, or `JOB_STATE_FAILED`. `JOB_STATE_PENDING = 9;`  
`JOB_STATE_QUEUED` |  `JOB_STATE_QUEUED` indicates that the job has been created but is being delayed until launch. Jobs that are queued may only transition to `JOB_STATE_PENDING` or `JOB_STATE_CANCELLED`. `JOB_STATE_QUEUED = 11;`  
`JOB_STATE_QUEUED_VALUE` |  `JOB_STATE_QUEUED` indicates that the job has been created but is being delayed until launch. Jobs that are queued may only transition to `JOB_STATE_PENDING` or `JOB_STATE_CANCELLED`. `JOB_STATE_QUEUED = 11;`  
`JOB_STATE_RESOURCE_CLEANING_UP` |  `JOB_STATE_RESOURCE_CLEANING_UP` indicates that the batch job's associated resources are currently being cleaned up after a successful run. Currently, this is an opt-in feature, please reach out to Cloud support team if you are interested. `JOB_STATE_RESOURCE_CLEANING_UP = 12;`  
`JOB_STATE_RESOURCE_CLEANING_UP_VALUE` |  `JOB_STATE_RESOURCE_CLEANING_UP` indicates that the batch job's associated resources are currently being cleaned up after a successful run. Currently, this is an opt-in feature, please reach out to Cloud support team if you are interested. `JOB_STATE_RESOURCE_CLEANING_UP = 12;`  
`JOB_STATE_RUNNING` |  `JOB_STATE_RUNNING` indicates that the job is currently running. `JOB_STATE_RUNNING = 2;`  
`JOB_STATE_RUNNING_VALUE` |  `JOB_STATE_RUNNING` indicates that the job is currently running. `JOB_STATE_RUNNING = 2;`  
`JOB_STATE_STOPPED` |  `JOB_STATE_STOPPED` indicates that the job has not yet started to run. `JOB_STATE_STOPPED = 1;`  
`JOB_STATE_STOPPED_VALUE` |  `JOB_STATE_STOPPED` indicates that the job has not yet started to run. `JOB_STATE_STOPPED = 1;`  
`JOB_STATE_UNKNOWN` |  The job's run state isn't specified. `JOB_STATE_UNKNOWN = 0;`  
`JOB_STATE_UNKNOWN_VALUE` |  The job's run state isn't specified. `JOB_STATE_UNKNOWN = 0;`  
`JOB_STATE_UPDATED` |  `JOB_STATE_UPDATED` indicates that the job was successfully updated, meaning that this job was stopped and another job was started, inheriting state from this one. This is a terminal job state. This state may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_RUNNING`. `JOB_STATE_UPDATED = 6;`  
`JOB_STATE_UPDATED_VALUE` |  `JOB_STATE_UPDATED` indicates that the job was successfully updated, meaning that this job was stopped and another job was started, inheriting state from this one. This is a terminal job state. This state may only be set by the Cloud Dataflow service, and only as a transition from `JOB_STATE_RUNNING`. `JOB_STATE_UPDATED = 6;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobState#com_google_dataflow_v1beta3_JobState_forNumber_int_) instead._  
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
