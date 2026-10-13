---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference
title: Class protos.google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:13.524561+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a BigtableDatabaseReference.

## Implements

[protos.google.cloud.geminidataanalytics.v1alpha.IBigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ibigtabledatabasereference)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1alpha.IBigtableDatabaseReference);

Constructs a new BigtableDatabaseReference.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ibigtabledatabasereference)`   
Properties to set  
  
## Properties 

### databaseTableReferences
    
    
    public databaseTableReferences: google.cloud.geminidataanalytics.v1alpha.IDatabaseTableReference[];

BigtableDatabaseReference databaseTableReferences.

### instanceId
    
    
    public instanceId: string;

BigtableDatabaseReference instanceId.

### projectId
    
    
    public projectId: string;

BigtableDatabaseReference projectId.

### tableIds
    
    
    public tableIds: string[];

BigtableDatabaseReference tableIds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1alpha.IBigtableDatabaseReference): google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference;

Creates a new BigtableDatabaseReference instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ibigtabledatabasereference)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference)` | BigtableDatabaseReference instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference;

Decodes a BigtableDatabaseReference message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[BigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference)` | BigtableDatabaseReference  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference;

Decodes a BigtableDatabaseReference message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference)` | BigtableDatabaseReference  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1alpha.IBigtableDatabaseReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigtableDatabaseReference message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ibigtabledatabasereference)`   
BigtableDatabaseReference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1alpha.IBigtableDatabaseReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigtableDatabaseReference message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ibigtabledatabasereference)`   
BigtableDatabaseReference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference;

Creates a BigtableDatabaseReference message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference)` | BigtableDatabaseReference  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BigtableDatabaseReference

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this BigtableDatabaseReference to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1alpha.BigtableDatabaseReference, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BigtableDatabaseReference message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BigtableDatabaseReference](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.bigtabledatabasereference)`   
BigtableDatabaseReference  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BigtableDatabaseReference message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
