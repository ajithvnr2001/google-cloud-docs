---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptionsOrBuilder
title: Interface TransactionOptionsOrBuilder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:32.020645+00:00
---

# Interface TransactionOptionsOrBuilder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransactionOptionsOrBuilder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public interface TransactionOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getModeCase()
    
    
    public abstract TransactionOptions.ModeCase getModeCase()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ModeCase)` |   
  
### getReadOnly()
    
    
    public abstract TransactionOptions.ReadOnly getReadOnly()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly)` | The readOnly.  
  
### getReadOnlyOrBuilder()
    
    
    public abstract TransactionOptions.ReadOnlyOrBuilder getReadOnlyOrBuilder()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnlyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnlyOrBuilder)` |   
  
### getReadWrite()
    
    
    public abstract TransactionOptions.ReadWrite getReadWrite()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWrite](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite)` | The readWrite.  
  
### getReadWriteOrBuilder()
    
    
    public abstract TransactionOptions.ReadWriteOrBuilder getReadWriteOrBuilder()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWriteOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWriteOrBuilder)` |   
  
### hasReadOnly()
    
    
    public abstract boolean hasReadOnly()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readOnly field is set.  
  
### hasReadWrite()
    
    
    public abstract boolean hasReadWrite()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readWrite field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
