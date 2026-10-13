---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateTagHoldRequestOrBuilder
title: Interface CreateTagHoldRequestOrBuilder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:41.897716+00:00
---

# Interface CreateTagHoldRequestOrBuilder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateTagHoldRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateTagHoldRequestOrBuilder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.97.0  1.96.0  1.95.0  1.93.0  1.90.0  1.89.0  1.87.0  1.85.0  1.84.0  1.82.0  1.80.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.72.0  1.70.0  1.69.0  1.66.0  1.65.0  1.64.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.6  1.4.0  1.3.2  1.2.12 
    
    
    public interface CreateTagHoldRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getTagHold()
    
    
    public abstract TagHold getTagHold()

Required. The TagHold to be created.

` .google.cloud.resourcemanager.v3.TagHold tag_hold = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TagHold](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.TagHold)` | The tagHold.  
  
### getTagHoldOrBuilder()
    
    
    public abstract TagHoldOrBuilder getTagHoldOrBuilder()

Required. The TagHold to be created.

` .google.cloud.resourcemanager.v3.TagHold tag_hold = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TagHoldOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.TagHoldOrBuilder)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action.

`bool validate_only = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasTagHold()
    
    
    public abstract boolean hasTagHold()

Required. The TagHold to be created.

` .google.cloud.resourcemanager.v3.TagHold tag_hold = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tagHold field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
