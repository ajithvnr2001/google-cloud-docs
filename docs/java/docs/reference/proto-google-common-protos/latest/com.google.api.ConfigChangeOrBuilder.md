---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.ConfigChangeOrBuilder
title: Interface ConfigChangeOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:47.648768+00:00
---

# Interface ConfigChangeOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.ConfigChangeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConfigChangeOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public interface ConfigChangeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdvices(int index)
    
    
    public abstract Advice getAdvices(int index)

Collection of advice provided for this change, useful for determining the possible impact of this change.

`repeated .google.api.Advice advices = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Advice](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Advice)` |   
  
### getAdvicesCount()
    
    
    public abstract int getAdvicesCount()

Collection of advice provided for this change, useful for determining the possible impact of this change.

`repeated .google.api.Advice advices = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdvicesList()
    
    
    public abstract List<Advice> getAdvicesList()

Collection of advice provided for this change, useful for determining the possible impact of this change.

`repeated .google.api.Advice advices = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Advice](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Advice)>` |   
  
### getAdvicesOrBuilder(int index)
    
    
    public abstract AdviceOrBuilder getAdvicesOrBuilder(int index)

Collection of advice provided for this change, useful for determining the possible impact of this change.

`repeated .google.api.Advice advices = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdviceOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.AdviceOrBuilder)` |   
  
### getAdvicesOrBuilderList()
    
    
    public abstract List<? extends AdviceOrBuilder> getAdvicesOrBuilderList()

Collection of advice provided for this change, useful for determining the possible impact of this change.

`repeated .google.api.Advice advices = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.AdviceOrBuilder>` |   
  
### getChangeType()
    
    
    public abstract ChangeType getChangeType()

The type for this change, either ADDED, REMOVED, or MODIFIED.

`.google.api.ChangeType change_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeType](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.ChangeType)` | The changeType.  
  
### getChangeTypeValue()
    
    
    public abstract int getChangeTypeValue()

The type for this change, either ADDED, REMOVED, or MODIFIED.

`.google.api.ChangeType change_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for changeType.  
  
### getElement()
    
    
    public abstract String getElement()

Object hierarchy path to the change, with levels separated by a '.' character. For repeated fields, an applicable unique identifier field is used for the index (usually selector, name, or id). For maps, the term 'key' is used. If the field has no unique identifier, the numeric index is used. Examples:

  * visibility.rules[selector=="google.LibraryService.ListBooks"].restriction
  * quota.metric_rules[selector=="google"].metric_costs[key=="reads"].value
  * logging.producer_destinations[0]



`string element = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The element.  
  
### getElementBytes()
    
    
    public abstract ByteString getElementBytes()

Object hierarchy path to the change, with levels separated by a '.' character. For repeated fields, an applicable unique identifier field is used for the index (usually selector, name, or id). For maps, the term 'key' is used. If the field has no unique identifier, the numeric index is used. Examples:

  * visibility.rules[selector=="google.LibraryService.ListBooks"].restriction
  * quota.metric_rules[selector=="google"].metric_costs[key=="reads"].value
  * logging.producer_destinations[0]



`string element = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for element.  
  
### getNewValue()
    
    
    public abstract String getNewValue()

Value of the changed object in the new Service configuration, in JSON format. This field will not be populated if ChangeType == REMOVED.

`string new_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The newValue.  
  
### getNewValueBytes()
    
    
    public abstract ByteString getNewValueBytes()

Value of the changed object in the new Service configuration, in JSON format. This field will not be populated if ChangeType == REMOVED.

`string new_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for newValue.  
  
### getOldValue()
    
    
    public abstract String getOldValue()

Value of the changed object in the old Service configuration, in JSON format. This field will not be populated if ChangeType == ADDED.

`string old_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The oldValue.  
  
### getOldValueBytes()
    
    
    public abstract ByteString getOldValueBytes()

Value of the changed object in the old Service configuration, in JSON format. This field will not be populated if ChangeType == ADDED.

`string old_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for oldValue.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
