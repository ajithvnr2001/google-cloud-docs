---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder
title: Interface ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:09.462776+00:00
---

# Interface ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder)


    
    
    public static interface ProcessorIOSpec.InstanceResourceInputBindingSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfigTypeUri()
    
    
    public abstract String getConfigTypeUri()

The configuration proto that includes the Googleapis resources. I.e. type.googleapis.com/google.cloud.vision.v1.StreamWithAnnotation

`string config_type_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The configTypeUri.  
  
### getConfigTypeUriBytes()
    
    
    public abstract ByteString getConfigTypeUriBytes()

The configuration proto that includes the Googleapis resources. I.e. type.googleapis.com/google.cloud.vision.v1.StreamWithAnnotation

`string config_type_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for configTypeUri.  
  
### getName()
    
    
    public abstract String getName()

Name of the input binding, unique within the processor.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the input binding, unique within the processor.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResourceTypeCase()
    
    
    public abstract ProcessorIOSpec.InstanceResourceInputBindingSpec.ResourceTypeCase getResourceTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[ProcessorIOSpec.InstanceResourceInputBindingSpec.ResourceTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.ProcessorIOSpec.InstanceResourceInputBindingSpec.ResourceTypeCase)` |   
  
### getResourceTypeUri()
    
    
    public abstract String getResourceTypeUri()

The direct type url of Googleapis resource. i.e. type.googleapis.com/google.cloud.vision.v1.Asset

`string resource_type_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceTypeUri.  
  
### getResourceTypeUriBytes()
    
    
    public abstract ByteString getResourceTypeUriBytes()

The direct type url of Googleapis resource. i.e. type.googleapis.com/google.cloud.vision.v1.Asset

`string resource_type_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceTypeUri.  
  
### hasConfigTypeUri()
    
    
    public abstract boolean hasConfigTypeUri()

The configuration proto that includes the Googleapis resources. I.e. type.googleapis.com/google.cloud.vision.v1.StreamWithAnnotation

`string config_type_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the configTypeUri field is set.  
  
### hasResourceTypeUri()
    
    
    public abstract boolean hasResourceTypeUri()

The direct type url of Googleapis resource. i.e. type.googleapis.com/google.cloud.vision.v1.Asset

`string resource_type_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resourceTypeUri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
