---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot
title: Class protos.google.dataflow.v1beta3.Snapshot (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:05.493884+00:00
---

# Class protos.google.dataflow.v1beta3.Snapshot (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.dataflow.v1beta3.Snapshot (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.0.2  2.1.2  2.0.1  1.2.0  1.1.0  1.0.2 

Represents a Snapshot.

## Implements

[protos.google.dataflow.v1beta3.ISnapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isnapshot)

## Package

[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.dataflow.v1beta3.ISnapshot);

Constructs a new Snapshot.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISnapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isnapshot)`   
Properties to set  
  
## Properties 

### creationTime
    
    
    public creationTime?: (google.protobuf.ITimestamp|null);

Snapshot creationTime.

### description
    
    
    public description: string;

Snapshot description.

### diskSizeBytes
    
    
    public diskSizeBytes: (number|Long|string);

Snapshot diskSizeBytes.

### id
    
    
    public id: string;

Snapshot id.

### projectId
    
    
    public projectId: string;

Snapshot projectId.

### pubsubMetadata
    
    
    public pubsubMetadata: google.dataflow.v1beta3.IPubsubSnapshotMetadata[];

Snapshot pubsubMetadata.

### region
    
    
    public region: string;

Snapshot region.

### sourceJobId
    
    
    public sourceJobId: string;

Snapshot sourceJobId.

### state
    
    
    public state: (google.dataflow.v1beta3.SnapshotState|keyof typeof google.dataflow.v1beta3.SnapshotState);

Snapshot state.

### ttl
    
    
    public ttl?: (google.protobuf.IDuration|null);

Snapshot ttl.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.dataflow.v1beta3.ISnapshot): google.dataflow.v1beta3.Snapshot;

Creates a new Snapshot instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISnapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isnapshot)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot)` | Snapshot instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.dataflow.v1beta3.Snapshot;

Decodes a Snapshot message from the specified reader or buffer.

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
`[Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot)` | Snapshot  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.dataflow.v1beta3.Snapshot;

Decodes a Snapshot message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot)` | Snapshot  
  
### encode(message, writer)
    
    
    public static encode(message: google.dataflow.v1beta3.ISnapshot, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Snapshot message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISnapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isnapshot)`   
Snapshot message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.dataflow.v1beta3.ISnapshot, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Snapshot message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISnapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.isnapshot)`   
Snapshot message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.dataflow.v1beta3.Snapshot;

Creates a Snapshot message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot)` | Snapshot  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Snapshot

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

Converts this Snapshot to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.dataflow.v1beta3.Snapshot, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Snapshot message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.snapshot)`   
Snapshot  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Snapshot message.

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
