---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ResolutionStatus
title: Enum ResolutionStatus (0.220.0-beta) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:05.484205+00:00
---

# Enum ResolutionStatus (0.220.0-beta)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ResolutionStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum ResolutionStatus (0.220.0-beta) Stay organized with collections  Save and categorize content based on your preferences. 

0.220.0-beta (latest)  0.216.0-beta  0.215.0-beta  0.214.0-beta  0.212.0-beta  0.209.0-beta  0.208.0-beta  0.206.0-beta  0.204.0-beta  0.203.0-beta  0.202.0-beta  0.201.0-beta  0.199.0-beta  0.197.0-beta  0.196.0-beta  0.195.0-beta  0.194.0-beta  0.193.0-beta  0.191.0-beta  0.189.0-beta  0.188.0-beta  0.185.0-beta  0.184.0-beta  0.183.0-beta  0.181.0-beta  0.180.0-beta  0.179.0-beta  0.178.0-beta  0.177.0-beta  0.176.0-beta  0.175.0-beta  0.174.0-beta  0.173.0-beta  0.172.0-beta  0.170.0-beta  0.169.0-beta  0.168.0-beta  0.167.0-beta  0.166.0-beta  0.165.0-beta  0.164.0-beta  0.163.0-beta  0.162.0-beta  0.161.0-beta  0.160.0-beta  0.158.0-beta  0.157.0-beta  0.156.0-beta  0.155.0-beta  0.154.0-beta  0.153.0-beta  0.152.0-beta  0.151.0-beta  0.150.0-beta  0.149.0-beta  0.148.0-beta  0.145.0-beta  0.144.0-beta  0.143.0-beta  0.142.0-beta  0.141.0-beta  0.140.0-beta  0.139.0-beta  0.138.0-beta  0.137.0-beta  0.136.0-beta  0.135.0-beta  0.134.0-beta  0.133.0-beta  0.132.0-beta  0.130.0-beta  0.129.0-beta  0.128.0-beta  0.127.0-beta  0.126.0-beta  0.125.0-beta  0.124.15-beta  0.123.4-beta  0.122.23-beta 
    
    
    public enum ResolutionStatus extends Enum<ResolutionStatus> implements ProtocolMessageEnum

Resolution status of an error group.

Protobuf enum `google.devtools.clouderrorreporting.v1beta1.ResolutionStatus`

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
`ACKNOWLEDGED` |  Error Group manually acknowledged, it can have an issue link attached. `ACKNOWLEDGED = 2;`  
`ACKNOWLEDGED_VALUE` |  Error Group manually acknowledged, it can have an issue link attached. `ACKNOWLEDGED = 2;`  
`MUTED` |  The error group is muted and excluded by default on group stats requests. `MUTED = 4;`  
`MUTED_VALUE` |  The error group is muted and excluded by default on group stats requests. `MUTED = 4;`  
`OPEN` |  The error group is not being addressed. This is the default for new groups. It is also used for errors re-occurring after marked RESOLVED. `OPEN = 1;`  
`OPEN_VALUE` |  The error group is not being addressed. This is the default for new groups. It is also used for errors re-occurring after marked RESOLVED. `OPEN = 1;`  
`RESOLUTION_STATUS_UNSPECIFIED` |  Status is unknown. When left unspecified in requests, it is treated like OPEN. `RESOLUTION_STATUS_UNSPECIFIED = 0;`  
`RESOLUTION_STATUS_UNSPECIFIED_VALUE` |  Status is unknown. When left unspecified in requests, it is treated like OPEN. `RESOLUTION_STATUS_UNSPECIFIED = 0;`  
`RESOLVED` |  Error Group manually resolved, more events for this group are not expected to occur. `RESOLVED = 3;`  
`RESOLVED_VALUE` |  Error Group manually resolved, more events for this group are not expected to occur. `RESOLVED = 3;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ResolutionStatus#com_google_devtools_clouderrorreporting_v1beta1_ResolutionStatus_forNumber_int_) instead._  
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
