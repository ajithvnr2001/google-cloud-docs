---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequestOrBuilder
title: Interface ReadRowsRequestOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:03.470520+00:00
---

# Interface ReadRowsRequestOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadRowsRequestOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface ReadRowsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArrowSerializationOptions()
    
    
    public abstract ArrowSerializationOptions getArrowSerializationOptions()

Optional. Options specific to the Apache Arrow output format.

This feature is not yet available.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSerializationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSerializationOptions)` | The arrowSerializationOptions.  
  
### getArrowSerializationOptionsOrBuilder()
    
    
    public abstract ArrowSerializationOptionsOrBuilder getArrowSerializationOptionsOrBuilder()

Optional. Options specific to the Apache Arrow output format.

This feature is not yet available.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSerializationOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSerializationOptionsOrBuilder)` |   
  
### getOffset()
    
    
    public abstract long getOffset()

The offset requested must be less than the last row read from Read. Requesting a larger offset is undefined. If not specified, start reading from offset zero.

`int64 offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The offset.  
  
### getOutputFormatSerializationOptionsCase()
    
    
    public abstract ReadRowsRequest.OutputFormatSerializationOptionsCase getOutputFormatSerializationOptionsCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsRequest.OutputFormatSerializationOptionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.OutputFormatSerializationOptionsCase)` |   
  
### getReadStream()
    
    
    public abstract String getReadStream()

Required. Stream to read rows from.

` string read_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The readStream.  
  
### getReadStreamBytes()
    
    
    public abstract ByteString getReadStreamBytes()

Required. Stream to read rows from.

` string read_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for readStream.  
  
### hasArrowSerializationOptions()
    
    
    public abstract boolean hasArrowSerializationOptions()

Optional. Options specific to the Apache Arrow output format.

This feature is not yet available.

` .google.cloud.bigquery.storage.v1.ArrowSerializationOptions arrow_serialization_options = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowSerializationOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
