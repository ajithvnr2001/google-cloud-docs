---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName
title: Class McpToolName (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:30.855161+00:00
---

# Class McpToolName (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class McpToolName (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public class McpToolName implements ResourceName

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > McpToolName

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

### format(String project, String location, String apiNamespace, String mcpServer, String mcpTool)
    
    
    public static String format(String project, String location, String apiNamespace, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`apiNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatProjectLocationApiNamespaceMcpServerMcpToolName(String project, String location, String apiNamespace, String mcpServer, String mcpTool)
    
    
    public static String formatProjectLocationApiNamespaceMcpServerMcpToolName(String project, String location, String apiNamespace, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`apiNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### formatProjectLocationMcpServerMcpToolName(String project, String location, String mcpServer, String mcpTool)
    
    
    public static String formatProjectLocationMcpServerMcpToolName(String project, String location, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
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
    
    
    public static McpToolName.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[McpToolName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName.Builder)` |   
  
### newProjectLocationApiNamespaceMcpServerMcpToolBuilder()
    
    
    public static McpToolName.Builder newProjectLocationApiNamespaceMcpServerMcpToolBuilder()

**Returns**  
---  
**Type** | **Description**  
`[McpToolName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName.Builder)` |   
  
### newProjectLocationMcpServerMcpToolBuilder()
    
    
    public static McpToolName.ProjectLocationMcpServerMcpToolBuilder newProjectLocationMcpServerMcpToolBuilder()

**Returns**  
---  
**Type** | **Description**  
`[McpToolName.ProjectLocationMcpServerMcpToolBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName.ProjectLocationMcpServerMcpToolBuilder)` |   
  
### of(String project, String location, String apiNamespace, String mcpServer, String mcpTool)
    
    
    public static McpToolName of(String project, String location, String apiNamespace, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`apiNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpToolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName)` |   
  
### ofProjectLocationApiNamespaceMcpServerMcpToolName(String project, String location, String apiNamespace, String mcpServer, String mcpTool)
    
    
    public static McpToolName ofProjectLocationApiNamespaceMcpServerMcpToolName(String project, String location, String apiNamespace, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`apiNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpToolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName)` |   
  
### ofProjectLocationMcpServerMcpToolName(String project, String location, String mcpServer, String mcpTool)
    
    
    public static McpToolName ofProjectLocationMcpServerMcpToolName(String project, String location, String mcpServer, String mcpTool)

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`location` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpServer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`mcpTool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpToolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName)` |   
  
### parse(String formattedString)
    
    
    public static @Nullable McpToolName parse(String formattedString)

**Parameter**  
---  
**Name** | **Description**  
`formattedString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1beta.McpToolName` |   
  
### parseList(List<String> formattedStrings)
    
    
    public static List<McpToolName> parseList(List<String> formattedStrings)

**Parameter**  
---  
**Name** | **Description**  
`formattedStrings` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[McpToolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName)>` |   
  
### toStringList(List<@Nullable McpToolName> values)
    
    
    public static List<String> toStringList(List<@Nullable McpToolName> values)

**Parameter**  
---  
**Name** | **Description**  
`values` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1beta.McpToolName>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
## Constructors 

### McpToolName() (deprecated)
    
    
    protected McpToolName()

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

### getApiNamespace()
    
    
    public String getApiNamespace()

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
  
### getLocation()
    
    
    public String getLocation()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMcpServer()
    
    
    public String getMcpServer()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMcpTool()
    
    
    public String getMcpTool()

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
    
    
    public McpToolName.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[McpToolName.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1beta.McpToolName.Builder)` |   
  
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

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
