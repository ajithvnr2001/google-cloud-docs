---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName
title: Class DiscoveredResourcesTopologyName (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:21.629553+00:00
---

# Class DiscoveredResourcesTopologyName (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DiscoveredResourcesTopologyName (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class DiscoveredResourcesTopologyName implements ResourceName

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DiscoveredResourcesTopologyName

## Implements

com.google.api.resourcenames.ResourceName

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### format(String project, String location)
    
    
    public static String format(String project, String location)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### isParsableFrom(String formattedString)
    
    
    public static boolean isParsableFrom(String formattedString)

**Parameter**  
---  
**Name** | **Description**  
`formattedString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### newBuilder()
    
    
    public static DiscoveredResourcesTopologyName.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveredResourcesTopologyName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName.Builder)` |   
  
### of(String project, String location)
    
    
    public static DiscoveredResourcesTopologyName of(String project, String location)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredResourcesTopologyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName)` |   
  
### parse(String formattedString)
    
    
    public static @Nullable DiscoveredResourcesTopologyName parse(String formattedString)

**Parameter**  
---  
**Name** | **Description**  
`formattedString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName` |   
  
### parseList(List<String> formattedStrings)
    
    
    public static List<DiscoveredResourcesTopologyName> parseList(List<String> formattedStrings)

**Parameter**  
---  
**Name** | **Description**  
`formattedStrings` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DiscoveredResourcesTopologyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName)>` |   
  
### toStringList(List<@Nullable DiscoveredResourcesTopologyName> values)
    
    
    public static List<String> toStringList(List<@Nullable DiscoveredResourcesTopologyName> values)

**Parameter**  
---  
**Name** | **Description**  
`values` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<@org.jspecify.annotations.Nullable com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
## Constructors 

### DiscoveredResourcesTopologyName() (deprecated)
    
    
    protected DiscoveredResourcesTopologyName()

## Methods 

### equals(@Nullable Object o)
    
    
    public boolean equals(@Nullable Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `@org.jspecify.annotations.Nullable java.lang.Object`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getFieldValue(String fieldName)
    
    
    public String getFieldValue(String fieldName)

**Parameter**  
---  
**Name** | **Description**  
`fieldName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getFieldValuesMap()
    
    
    public Map<String,String> getFieldValuesMap()

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLocation()
    
    
    public String getLocation()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getProject()
    
    
    public String getProject()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toBuilder()
    
    
    public DiscoveredResourcesTopologyName.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[DiscoveredResourcesTopologyName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apptopology/latest/com.google.cloud.apptopology.v1.DiscoveredResourcesTopologyName.Builder)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
