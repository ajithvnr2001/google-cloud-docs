---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName
title: Class FindingName (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:27.428744+00:00
---

# Class FindingName (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FindingName (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public class FindingName implements ResourceName

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FindingName

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

### format(String organization, String source, String finding)
    
    
    public static String format(String organization, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatFolderSourceFindingName(String folder, String source, String finding)
    
    
    public static String formatFolderSourceFindingName(String folder, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatOrganizationSourceFindingName(String organization, String source, String finding)
    
    
    public static String formatOrganizationSourceFindingName(String organization, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatProjectSourceFindingName(String project, String source, String finding)
    
    
    public static String formatProjectSourceFindingName(String project, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
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
    
    
    public static FindingName.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[FindingName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName.Builder)` |   
  
### newFolderSourceFindingBuilder()
    
    
    public static FindingName.FolderSourceFindingBuilder newFolderSourceFindingBuilder()

**Returns**  
---  
**Type** | **Description**  
`[FindingName.FolderSourceFindingBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName.FolderSourceFindingBuilder)` |   
  
### newOrganizationSourceFindingBuilder()
    
    
    public static FindingName.Builder newOrganizationSourceFindingBuilder()

**Returns**  
---  
**Type** | **Description**  
`[FindingName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName.Builder)` |   
  
### newProjectSourceFindingBuilder()
    
    
    public static FindingName.ProjectSourceFindingBuilder newProjectSourceFindingBuilder()

**Returns**  
---  
**Type** | **Description**  
`[FindingName.ProjectSourceFindingBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName.ProjectSourceFindingBuilder)` |   
  
### of(String organization, String source, String finding)
    
    
    public static FindingName of(String organization, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName)` |   
  
### ofFolderSourceFindingName(String folder, String source, String finding)
    
    
    public static FindingName ofFolderSourceFindingName(String folder, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName)` |   
  
### ofOrganizationSourceFindingName(String organization, String source, String finding)
    
    
    public static FindingName ofOrganizationSourceFindingName(String organization, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName)` |   
  
### ofProjectSourceFindingName(String project, String source, String finding)
    
    
    public static FindingName ofProjectSourceFindingName(String project, String source, String finding)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`source` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`finding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName)` |   
  
### parse(String formattedString)
    
    
    public static @Nullable FindingName parse(String formattedString)

**Parameter**  
---  
**Name** | **Description**  
`formattedString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v1.FindingName` |   
  
### parseList(List<String> formattedStrings)
    
    
    public static List<FindingName> parseList(List<String> formattedStrings)

**Parameter**  
---  
**Name** | **Description**  
`formattedStrings` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName)>` |   
  
### toStringList(List<@Nullable FindingName> values)
    
    
    public static List<String> toStringList(List<@Nullable FindingName> values)

**Parameter**  
---  
**Name** | **Description**  
`values` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<@org.jspecify.annotations.Nullable com.google.cloud.securitycenter.v1.FindingName>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
## Constructors 

### FindingName() (deprecated)
    
    
    protected FindingName()

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
  
### getFinding()
    
    
    public String getFinding()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getFolder()
    
    
    public String getFolder()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOrganization()
    
    
    public String getOrganization()

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
  
### getSource()
    
    
    public String getSource()

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
    
    
    public FindingName.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[FindingName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.FindingName.Builder)` |   
  
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
