---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.VO2Max.MeasurementMethod
title: Enum VO2Max.MeasurementMethod (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:46.610231+00:00
---

# Enum VO2Max.MeasurementMethod (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.VO2Max.MeasurementMethod

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum VO2Max.MeasurementMethod (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public enum VO2Max.MeasurementMethod extends Enum<VO2Max.MeasurementMethod> implements ProtocolMessageEnum

Measurement method used to measure the VO2 max value.

Protobuf enum `google.devicesandservices.health.v4.VO2Max.MeasurementMethod`

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
`COOPER_TEST` |  Run as far as possible for 12 minutes. Distance correlated with age and gender translates to a VO2 max value. `COOPER_TEST = 3;`  
`COOPER_TEST_VALUE` |  Run as far as possible for 12 minutes. Distance correlated with age and gender translates to a VO2 max value. `COOPER_TEST = 3;`  
`FITBIT_RUN` |  Fitbit specific, measures VO2 max rate during a run. `FITBIT_RUN = 1;`  
`FITBIT_RUN_VALUE` |  Fitbit specific, measures VO2 max rate during a run. `FITBIT_RUN = 1;`  
`GOOGLE_DEMOGRAPHIC` |  Google specific, measures VO2 max rate for a user based on their demographic data. `GOOGLE_DEMOGRAPHIC = 2;`  
`GOOGLE_DEMOGRAPHIC_VALUE` |  Google specific, measures VO2 max rate for a user based on their demographic data. `GOOGLE_DEMOGRAPHIC = 2;`  
`HEART_RATE_RATIO` |  Maximum heart rate divided by the resting heart rate, with a multiplier applied. Does not require any exercise. `HEART_RATE_RATIO = 4;`  
`HEART_RATE_RATIO_VALUE` |  Maximum heart rate divided by the resting heart rate, with a multiplier applied. Does not require any exercise. `HEART_RATE_RATIO = 4;`  
`MAX_EXERCISE` |  Healthkit specific, measures VO2 max rate by monitoring exercise to the user’s physical limit. Similar to COOPER_TEST or MULTISTAGE_FITNESS_TEST. `MAX_EXERCISE = 8;`  
`MAX_EXERCISE_VALUE` |  Healthkit specific, measures VO2 max rate by monitoring exercise to the user’s physical limit. Similar to COOPER_TEST or MULTISTAGE_FITNESS_TEST. `MAX_EXERCISE = 8;`  
`MEASUREMENT_METHOD_UNSPECIFIED` |  Unspecified measurement method. `MEASUREMENT_METHOD_UNSPECIFIED = 0;`  
`MEASUREMENT_METHOD_UNSPECIFIED_VALUE` |  Unspecified measurement method. `MEASUREMENT_METHOD_UNSPECIFIED = 0;`  
`METABOLIC_CART` |  Measured by a medical device called metabolic cart. `METABOLIC_CART = 5;`  
`METABOLIC_CART_VALUE` |  Measured by a medical device called metabolic cart. `METABOLIC_CART = 5;`  
`MULTISTAGE_FITNESS_TEST` |  Continuous 20m back-and-forth runs with increasing difficulty, until exhaustion. `MULTISTAGE_FITNESS_TEST = 6;`  
`MULTISTAGE_FITNESS_TEST_VALUE` |  Continuous 20m back-and-forth runs with increasing difficulty, until exhaustion. `MULTISTAGE_FITNESS_TEST = 6;`  
`OTHER` |  Use when the method is not covered in this enum. `OTHER = 11;`  
`OTHER_VALUE` |  Use when the method is not covered in this enum. `OTHER = 11;`  
`PREDICTION_NON_EXERCISE` |  Healthkit specific, estimates VO2 max rate without any exercise. Similar to HEART_RATE_RATIO. `PREDICTION_NON_EXERCISE = 10;`  
`PREDICTION_NON_EXERCISE_VALUE` |  Healthkit specific, estimates VO2 max rate without any exercise. Similar to HEART_RATE_RATIO. `PREDICTION_NON_EXERCISE = 10;`  
`PREDICTION_SUB_MAX_EXERCISE` |  Healthkit specific, estimates VO2 max rate based on low-intensity exercise. Similar to ROCKPORT_FITNESS_TEST. `PREDICTION_SUB_MAX_EXERCISE = 9;`  
`PREDICTION_SUB_MAX_EXERCISE_VALUE` |  Healthkit specific, estimates VO2 max rate based on low-intensity exercise. Similar to ROCKPORT_FITNESS_TEST. `PREDICTION_SUB_MAX_EXERCISE = 9;`  
`ROCKPORT_FITNESS_TEST` |  Measured using walking exercise. `ROCKPORT_FITNESS_TEST = 7;`  
`ROCKPORT_FITNESS_TEST_VALUE` |  Measured using walking exercise. `ROCKPORT_FITNESS_TEST = 7;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.VO2Max.MeasurementMethod#com_google_devicesandservices_health_v4_VO2Max_MeasurementMethod_forNumber_int_) instead._  
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
