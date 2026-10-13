---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextRequestOrBuilder
title: Interface LookupContextRequestOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:51.525496+00:00
---

# Interface LookupContextRequestOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LookupContextRequestOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public interface LookupContextRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsOptions(String key)
    
    
    public abstract boolean containsOptions(String key)

Optional. Allows to configure the context.

Supported options:

  * `format` \- The format of the context (one of `yaml`, `xml`, `json`, default is `yaml`).
  * `context_budget` \- If provided, the output will be intelligently truncated on a best-effort basis to contain approximately the desired amount of characters. There is no guarantee to achieve the specific amount.



`map<string, string> options = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getContext()
    
    
    public abstract String getContext()

Optional. The text representing contextual information for which metadata context is being requested.

`string context = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The context.  
  
### getContextBytes()
    
    
    public abstract ByteString getContextBytes()

Optional. The text representing contextual information for which metadata context is being requested.

`string context = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for context.  
  
### getName()
    
    
    public abstract String getName()

Required. The project to which the request should be attributed in the following form: `projects/{project}/locations/{location}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The project to which the request should be attributed in the following form: `projects/{project}/locations/{location}`.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOptions() (deprecated)
    
    
    public abstract Map<String,String> getOptions()

Use [#getOptionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextRequestOrBuilder#com_google_cloud_dataplex_v1_LookupContextRequestOrBuilder_getOptionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getOptionsCount()
    
    
    public abstract int getOptionsCount()

Optional. Allows to configure the context.

Supported options:

  * `format` \- The format of the context (one of `yaml`, `xml`, `json`, default is `yaml`).
  * `context_budget` \- If provided, the output will be intelligently truncated on a best-effort basis to contain approximately the desired amount of characters. There is no guarantee to achieve the specific amount.



`map<string, string> options = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOptionsMap()
    
    
    public abstract Map<String,String> getOptionsMap()

Optional. Allows to configure the context.

Supported options:

  * `format` \- The format of the context (one of `yaml`, `xml`, `json`, default is `yaml`).
  * `context_budget` \- If provided, the output will be intelligently truncated on a best-effort basis to contain approximately the desired amount of characters. There is no guarantee to achieve the specific amount.



`map<string, string> options = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getOptionsOrDefault(String key, String defaultValue)
    
    
    public abstract String getOptionsOrDefault(String key, String defaultValue)

Optional. Allows to configure the context.

Supported options:

  * `format` \- The format of the context (one of `yaml`, `xml`, `json`, default is `yaml`).
  * `context_budget` \- If provided, the output will be intelligently truncated on a best-effort basis to contain approximately the desired amount of characters. There is no guarantee to achieve the specific amount.



`map<string, string> options = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOptionsOrThrow(String key)
    
    
    public abstract String getOptionsOrThrow(String key)

Optional. Allows to configure the context.

Supported options:

  * `format` \- The format of the context (one of `yaml`, `xml`, `json`, default is `yaml`).
  * `context_budget` \- If provided, the output will be intelligently truncated on a best-effort basis to contain approximately the desired amount of characters. There is no guarantee to achieve the specific amount.



`map<string, string> options = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResources(int index)
    
    
    public abstract String getResources(int index)

Required. The entry names to look up the context for. The maximum number of resources for a request is limited to 10.

## Examples:

`projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`

` repeated string resources = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resources at the given index.  
  
### getResourcesBytes(int index)
    
    
    public abstract ByteString getResourcesBytes(int index)

Required. The entry names to look up the context for. The maximum number of resources for a request is limited to 10.

## Examples:

`projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`

` repeated string resources = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the resources at the given index.  
  
### getResourcesCount()
    
    
    public abstract int getResourcesCount()

Required. The entry names to look up the context for. The maximum number of resources for a request is limited to 10.

## Examples:

`projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`

` repeated string resources = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of resources.  
  
### getResourcesList()
    
    
    public abstract List<String> getResourcesList()

Required. The entry names to look up the context for. The maximum number of resources for a request is limited to 10.

## Examples:

`projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`

` repeated string resources = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the resources.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
