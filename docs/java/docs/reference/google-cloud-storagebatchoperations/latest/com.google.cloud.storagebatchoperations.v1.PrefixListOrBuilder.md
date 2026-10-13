---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.PrefixListOrBuilder
title: Interface PrefixListOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:19.587019+00:00
---

# Interface PrefixListOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.PrefixListOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PrefixListOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface PrefixListOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIncludedObjectPrefixes(int index)
    
    
    public abstract String getIncludedObjectPrefixes(int index)

Optional. Include prefixes of the objects to be transformed.

  * Supports full object name
  * Supports prefix of the object name
  * Wildcards are not supported
  * Supports empty string for all objects in a bucket.



`repeated string included_object_prefixes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The includedObjectPrefixes at the given index.  
  
### getIncludedObjectPrefixesBytes(int index)
    
    
    public abstract ByteString getIncludedObjectPrefixesBytes(int index)

Optional. Include prefixes of the objects to be transformed.

  * Supports full object name
  * Supports prefix of the object name
  * Wildcards are not supported
  * Supports empty string for all objects in a bucket.



`repeated string included_object_prefixes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the includedObjectPrefixes at the given index.  
  
### getIncludedObjectPrefixesCount()
    
    
    public abstract int getIncludedObjectPrefixesCount()

Optional. Include prefixes of the objects to be transformed.

  * Supports full object name
  * Supports prefix of the object name
  * Wildcards are not supported
  * Supports empty string for all objects in a bucket.



`repeated string included_object_prefixes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of includedObjectPrefixes.  
  
### getIncludedObjectPrefixesList()
    
    
    public abstract List<String> getIncludedObjectPrefixesList()

Optional. Include prefixes of the objects to be transformed.

  * Supports full object name
  * Supports prefix of the object name
  * Wildcards are not supported
  * Supports empty string for all objects in a bucket.



`repeated string included_object_prefixes = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the includedObjectPrefixes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
