---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.PropertyFilterOrBuilder
title: Interface PropertyFilterOrBuilder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:35.075338+00:00
---

# Interface PropertyFilterOrBuilder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.PropertyFilterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PropertyFilterOrBuilder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public interface PropertyFilterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getOp()
    
    
    public abstract PropertyFilter.Operator getOp()

The operator to filter by.

`.google.datastore.v1.PropertyFilter.Operator op = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyFilter.Operator](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.PropertyFilter.Operator)` | The op.  
  
### getOpValue()
    
    
    public abstract int getOpValue()

The operator to filter by.

`.google.datastore.v1.PropertyFilter.Operator op = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for op.  
  
### getProperty()
    
    
    public abstract PropertyReference getProperty()

The property to filter by.

`.google.datastore.v1.PropertyReference property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.PropertyReference)` | The property.  
  
### getPropertyOrBuilder()
    
    
    public abstract PropertyReferenceOrBuilder getPropertyOrBuilder()

The property to filter by.

`.google.datastore.v1.PropertyReference property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.PropertyReferenceOrBuilder)` |   
  
### getValue()
    
    
    public abstract Value getValue()

The value to compare the property to.

`.google.datastore.v1.Value value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.Value)` | The value.  
  
### getValueOrBuilder()
    
    
    public abstract ValueOrBuilder getValueOrBuilder()

The value to compare the property to.

`.google.datastore.v1.Value value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.ValueOrBuilder)` |   
  
### hasProperty()
    
    
    public abstract boolean hasProperty()

The property to filter by.

`.google.datastore.v1.PropertyReference property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the property field is set.  
  
### hasValue()
    
    
    public abstract boolean hasValue()

The value to compare the property to.

`.google.datastore.v1.Value value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the value field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
