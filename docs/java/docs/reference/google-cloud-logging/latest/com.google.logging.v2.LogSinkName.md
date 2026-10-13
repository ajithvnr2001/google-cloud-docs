---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName
title: Class LogSinkName (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:32.259575+00:00
---

# Class LogSinkName (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LogSinkName (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class LogSinkName implements ResourceName

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogSinkName

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

### format(String project, String sink)
    
    
    public static String format(String project, String sink)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatBillingAccountSinkName(String billingAccount, String sink)
    
    
    public static String formatBillingAccountSinkName(String billingAccount, String sink)

**Parameters**  
---  
**Name** | **Description**  
`billingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatFolderSinkName(String folder, String sink)
    
    
    public static String formatFolderSinkName(String folder, String sink)

**Parameters**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatOrganizationSinkName(String organization, String sink)
    
    
    public static String formatOrganizationSinkName(String organization, String sink)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatProjectSinkName(String project, String sink)
    
    
    public static String formatProjectSinkName(String project, String sink)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
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
  
### newBillingAccountSinkBuilder()
    
    
    public static LogSinkName.BillingAccountSinkBuilder newBillingAccountSinkBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.BillingAccountSinkBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.BillingAccountSinkBuilder)` |   
  
### newBuilder()
    
    
    public static LogSinkName.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.Builder)` |   
  
### newFolderSinkBuilder()
    
    
    public static LogSinkName.FolderSinkBuilder newFolderSinkBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.FolderSinkBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.FolderSinkBuilder)` |   
  
### newOrganizationSinkBuilder()
    
    
    public static LogSinkName.OrganizationSinkBuilder newOrganizationSinkBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.OrganizationSinkBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.OrganizationSinkBuilder)` |   
  
### newProjectSinkBuilder()
    
    
    public static LogSinkName.Builder newProjectSinkBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.Builder)` |   
  
### of(String project, String sink)
    
    
    public static LogSinkName of(String project, String sink)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)` |   
  
### ofBillingAccountSinkName(String billingAccount, String sink)
    
    
    public static LogSinkName ofBillingAccountSinkName(String billingAccount, String sink)

**Parameters**  
---  
**Name** | **Description**  
`billingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)` |   
  
### ofFolderSinkName(String folder, String sink)
    
    
    public static LogSinkName ofFolderSinkName(String folder, String sink)

**Parameters**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)` |   
  
### ofOrganizationSinkName(String organization, String sink)
    
    
    public static LogSinkName ofOrganizationSinkName(String organization, String sink)

**Parameters**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)` |   
  
### ofProjectSinkName(String project, String sink)
    
    
    public static LogSinkName ofProjectSinkName(String project, String sink)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)` |   
  
### parse(String formattedString)
    
    
    public static @Nullable LogSinkName parse(String formattedString)

**Parameter**  
---  
**Name** | **Description**  
`formattedString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName` |   
  
### parseList(List<String> formattedStrings)
    
    
    public static List<LogSinkName> parseList(List<String> formattedStrings)

**Parameter**  
---  
**Name** | **Description**  
`formattedStrings` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogSinkName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName)>` |   
  
### toStringList(List<@Nullable LogSinkName> values)
    
    
    public static List<String> toStringList(List<@Nullable LogSinkName> values)

**Parameter**  
---  
**Name** | **Description**  
`values` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
## Constructors 

### LogSinkName() (deprecated)
    
    
    protected LogSinkName()

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

### getBillingAccount()
    
    
    public String getBillingAccount()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
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
  
### getSink()
    
    
    public String getSink()

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
    
    
    public LogSinkName.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LogSinkName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSinkName.Builder)` |   
  
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
