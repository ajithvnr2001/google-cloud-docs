---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload
title: Class Payload.JsonPayload (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:03.120553+00:00
---

# Class Payload.JsonPayload (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Payload.JsonPayload (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class Payload.JsonPayload extends Payload<Struct>

A log entry's JSON payload.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload) > Payload.JsonPayload

## Inherited Members

[Payload.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload#com_google_cloud_logging_Payload_equals_java_lang_Object_)

[Payload.getData()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload#com_google_cloud_logging_Payload_getData__)

[Payload.getType()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload#com_google_cloud_logging_Payload_getType__)

[Payload.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload#com_google_cloud_logging_Payload_hashCode__)

[Payload.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload#com_google_cloud_logging_Payload_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### of(Struct data)
    
    
    public static Payload.JsonPayload of(Struct data)

Creates a log entry payload given its JSON data represented as a protobuf struct.

**Parameter**  
---  
**Name** | **Description**  
`data` | `[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Payload.JsonPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload)` |   
  
### of(Map<String,?> data)
    
    
    public static Payload.JsonPayload of(Map<String,?> data)

Creates a log entry payload given its JSON data represented as a map. The provided map is copied into a [Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html) object.

Notice that all numbers (int, long, float and double) are serialized as double values. Enums are serialized as strings.

Example usage of `JsonPayload`:
    
    
     List<Long> listValue = Arrays.asList(1L, 2L);
     Map<String, Object> innerMap = new HashMap<String, Object>();
     innerMap.put("booleanValue", true);
     innerMap.put("stringValue", "stringValue");
     Map<String, Object> jsonContent = new HashMap<String, Object>();
     jsonContent.put("listValue", listValue);
     jsonContent.put("integerValue", 42);
     jsonContent.put("doubleValue", 42.0);
     jsonContent.put("stringValue", "stringValue");
     jsonContent.put("mapValue", innerMap);
     JsonPayload payload = JsonPayload.of(jsonContent);
     

**Parameter**  
---  
**Name** | **Description**  
`data` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Payload.JsonPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload)` |   
  
## Methods 

### getDataAsMap()
    
    
    public Map<String,Object> getDataAsMap()

Returns the log entry's JSON data as an unmodifiable map.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
