---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRate.HeartRateMetadata.SensorLocation
title: Enum HeartRate.HeartRateMetadata.SensorLocation (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:10.967522+00:00
---

# Enum HeartRate.HeartRateMetadata.SensorLocation (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRate.HeartRateMetadata.SensorLocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum HeartRate.HeartRateMetadata.SensorLocation (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public enum HeartRate.HeartRateMetadata.SensorLocation extends Enum<HeartRate.HeartRateMetadata.SensorLocation> implements ProtocolMessageEnum

The location of the sensor that measured the heart rate.

Protobuf enum ` google.devicesandservices.health.v4.HeartRate.HeartRateMetadata.SensorLocation`

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
`CHEST` |  Chest sensor. `CHEST = 1;`  
`CHEST_VALUE` |  Chest sensor. `CHEST = 1;`  
`EAR_LOBE` |  Ear lobe sensor. `EAR_LOBE = 5;`  
`EAR_LOBE_VALUE` |  Ear lobe sensor. `EAR_LOBE = 5;`  
`FINGER` |  Finger sensor. `FINGER = 3;`  
`FINGER_VALUE` |  Finger sensor. `FINGER = 3;`  
`FOOT` |  Foot sensor. `FOOT = 6;`  
`FOOT_VALUE` |  Foot sensor. `FOOT = 6;`  
`HAND` |  Hand sensor. `HAND = 4;`  
`HAND_VALUE` |  Hand sensor. `HAND = 4;`  
`SENSOR_LOCATION_UNSPECIFIED` |  The default value when no data is available. `SENSOR_LOCATION_UNSPECIFIED = 0;`  
`SENSOR_LOCATION_UNSPECIFIED_VALUE` |  The default value when no data is available. `SENSOR_LOCATION_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`WRIST` |  Wrist sensor. `WRIST = 2;`  
`WRIST_VALUE` |  Wrist sensor. `WRIST = 2;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.HeartRate.HeartRateMetadata.SensorLocation#com_google_devicesandservices_health_v4_HeartRate_HeartRateMetadata_SensorLocation_forNumber_int_) instead._  
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
