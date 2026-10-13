---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SMBSettings
title: Enum SMBSettings (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:09.475081+00:00
---

# Enum SMBSettings (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SMBSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum SMBSettings (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum SMBSettings extends Enum<SMBSettings> implements ProtocolMessageEnum

SMBSettings Modifies the behaviour of a SMB volume.

Protobuf enum `google.cloud.netapp.v1.SMBSettings`

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
`ACCESS_BASED_ENUMERATION` |  SMB setting to access volume based on enumerartion `ACCESS_BASED_ENUMERATION = 8;`  
`ACCESS_BASED_ENUMERATION_VALUE` |  SMB setting to access volume based on enumerartion `ACCESS_BASED_ENUMERATION = 8;`  
`BROWSABLE` |  SMB setting browsable `BROWSABLE = 2;`  
`BROWSABLE_VALUE` |  SMB setting browsable `BROWSABLE = 2;`  
`CHANGE_NOTIFY` |  SMB setting notify change `CHANGE_NOTIFY = 3;`  
`CHANGE_NOTIFY_VALUE` |  SMB setting notify change `CHANGE_NOTIFY = 3;`  
`CONTINUOUSLY_AVAILABLE` |  Continuously available enumeration `CONTINUOUSLY_AVAILABLE = 9;`  
`CONTINUOUSLY_AVAILABLE_VALUE` |  Continuously available enumeration `CONTINUOUSLY_AVAILABLE = 9;`  
`ENCRYPT_DATA` |  SMB setting encrypt data `ENCRYPT_DATA = 1;`  
`ENCRYPT_DATA_VALUE` |  SMB setting encrypt data `ENCRYPT_DATA = 1;`  
`NON_BROWSABLE` |  SMB setting not to notify change `NON_BROWSABLE = 4;`  
`NON_BROWSABLE_VALUE` |  SMB setting not to notify change `NON_BROWSABLE = 4;`  
`OPLOCKS` |  SMB setting oplocks `OPLOCKS = 5;`  
`OPLOCKS_VALUE` |  SMB setting oplocks `OPLOCKS = 5;`  
`SHOW_PREVIOUS_VERSIONS` |  SMB setting to show previous versions `SHOW_PREVIOUS_VERSIONS = 7;`  
`SHOW_PREVIOUS_VERSIONS_VALUE` |  SMB setting to show previous versions `SHOW_PREVIOUS_VERSIONS = 7;`  
`SHOW_SNAPSHOT` |  SMB setting to show snapshots `SHOW_SNAPSHOT = 6;`  
`SHOW_SNAPSHOT_VALUE` |  SMB setting to show snapshots `SHOW_SNAPSHOT = 6;`  
`SMB_SETTINGS_UNSPECIFIED` |  Unspecified default option `SMB_SETTINGS_UNSPECIFIED = 0;`  
`SMB_SETTINGS_UNSPECIFIED_VALUE` |  Unspecified default option `SMB_SETTINGS_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SMBSettings#com_google_cloud_netapp_v1_SMBSettings_forNumber_int_) instead._  
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
