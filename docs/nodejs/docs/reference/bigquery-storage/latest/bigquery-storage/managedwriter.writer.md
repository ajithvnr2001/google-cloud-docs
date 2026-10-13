---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/managedwriter.writer
title: Class managedwriter.Writer (5.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:23.457191+00:00
---

# Class managedwriter.Writer (5.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/managedwriter.writer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class managedwriter.Writer (5.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.2 (latest)  5.1.1  4.10.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.1  4.1.0  4.0.0  3.4.0  3.2.0  3.1.1  2.8.0  2.7.0  2.6.2  2.5.4  2.3.0 

A BigQuery Storage API Writer that can be used to write data into BigQuery Table using the Storage API.

managedwriter

## Package

[@google-cloud/bigquery-storage](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/overview.html)

## Constructors 

### (constructor)(params)
    
    
    constructor(params: WriterOptions);

Creates a new Writer instance.

**Parameter**  
---  
**Name** | **Description**  
`params` |  `WriterOptions`   
The parameters for the Writer. See WriterOptions docs for more information.  
  
## Methods 

### appendRows(rows, offsetValue)
    
    
    appendRows(rows: ProtoData['rows'], offsetValue?: IInt64Value['value']): PendingWrite;

Schedules the writing of rows at given offset.

**Parameters**  
---  
**Name** | **Description**  
`rows` |  `ProtoData['rows']`   
the rows in serialized format to write to BigQuery.  
`offsetValue` |  `IInt64Value_2['value']`   
the offset of the first row.  
**Returns**  
---  
**Type** | **Description**  
`PendingWrite` | {managedwriter.PendingWrite} The pending write  
  
### close()
    
    
    close(): void;

**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setDefaultMissingValueInterpretation(defaultMissingValueInterpretation)
    
    
    setDefaultMissingValueInterpretation(defaultMissingValueInterpretation: MissingValueInterpretation): void;

Update how missing values are interpreted for the given stream.

**Parameter**  
---  
**Name** | **Description**  
`defaultMissingValueInterpretation` |  `MissingValueInterpretation`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMissingValueInterpretations(missingValueInterpretations)
    
    
    setMissingValueInterpretations(missingValueInterpretations: MissingValueInterpretationMap): void;

Update how missing values are interpreted for individual columns.

**Parameter**  
---  
**Name** | **Description**  
`missingValueInterpretations` |  `MissingValueInterpretationMap`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setProtoDescriptor(protoDescriptor)
    
    
    setProtoDescriptor(protoDescriptor: IDescriptorProto): void;

Update the proto descriptor for the Writer. Internally a reconnection event is gonna happen to apply the new proto descriptor.

**Parameter**  
---  
**Name** | **Description**  
`protoDescriptor` |  `IDescriptorProto`   
The proto descriptor.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### traceId()
    
    
    traceId(): string;

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
