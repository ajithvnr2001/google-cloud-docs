---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.json.GoogleJsonError.Details
title: Class GoogleJsonError.Details (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:31.914635+00:00
---

# Class GoogleJsonError.Details (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.json.GoogleJsonError.Details

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GoogleJsonError.Details (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public static class GoogleJsonError.Details extends GenericJson

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > java.util.AbstractMap > com.google.api.client.util.GenericData > com.google.api.client.json.GenericJson > GoogleJsonError.Details

## Inherited Members

com.google.api.client.json.GenericJson.clone()

com.google.api.client.json.GenericJson.getFactory()

com.google.api.client.json.GenericJson.set(java.lang.String,java.lang.Object)

com.google.api.client.json.GenericJson.setFactory(com.google.api.client.json.JsonFactory)

com.google.api.client.json.GenericJson.toPrettyString()

com.google.api.client.json.GenericJson.toString()

com.google.api.client.util.GenericData.entrySet()

com.google.api.client.util.GenericData.equals(java.lang.Object)

com.google.api.client.util.GenericData.get(java.lang.Object)

com.google.api.client.util.GenericData.getClassInfo()

com.google.api.client.util.GenericData.getUnknownKeys()

com.google.api.client.util.GenericData.hashCode()

com.google.api.client.util.GenericData.put(java.lang.String,java.lang.Object)

com.google.api.client.util.GenericData.putAll(java.util.Map<? extends java.lang.String,?>)

com.google.api.client.util.GenericData.remove(java.lang.Object)

com.google.api.client.util.GenericData.setUnknownKeys(java.util.Map<java.lang.String,java.lang.Object>)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

[AbstractMap.clear()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#clear--)

[AbstractMap.containsKey(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsKey-java.lang.Object-)

[AbstractMap.containsValue(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsValue-java.lang.Object-)

[AbstractMap.isEmpty()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#isEmpty--)

[AbstractMap.keySet()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#keySet--)

[AbstractMap.put(K,V)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#put-K-V-)

[AbstractMap.putAll(Map<? extends K,? extends V>)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#putAll-java.util.Map<?%20extends%20K-?%20extends%20V>-)

[AbstractMap.size()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#size--)

[AbstractMap.values()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#values--)

## Constructors 

### Details()
    
    
    public Details()

## Methods 

### getDetail()
    
    
    public String getDetail()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getParameterViolations()
    
    
    public List<GoogleJsonError.ParameterViolations> getParameterViolations()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ParameterViolations](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.json.GoogleJsonError.ParameterViolations)>` |   
  
### getReason()
    
    
    public String getReason()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getType()
    
    
    public String getType()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### setDetail(String detail)
    
    
    public void setDetail(String detail)

**Parameter**  
---  
**Name** | **Description**  
`detail` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setParameterViolations(List<GoogleJsonError.ParameterViolations> parameterViolations)
    
    
    public void setParameterViolations(List<GoogleJsonError.ParameterViolations> parameterViolations)

Sets parameterViolations list as immutable to prevent exposing mutable state.

**Parameter**  
---  
**Name** | **Description**  
`parameterViolations` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ParameterViolations](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.json.GoogleJsonError.ParameterViolations)>`  
  
  
### setReason(String reason)
    
    
    public void setReason(String reason)

**Parameter**  
---  
**Name** | **Description**  
`reason` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setType(String type)
    
    
    public void setType(String type)

**Parameter**  
---  
**Name** | **Description**  
`type` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
