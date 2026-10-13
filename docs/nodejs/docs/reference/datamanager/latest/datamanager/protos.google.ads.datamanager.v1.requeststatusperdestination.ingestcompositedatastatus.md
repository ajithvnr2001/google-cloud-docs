---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus
title: Class protos.google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:28.398191+00:00
---

# Class protos.google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an IngestCompositeDataStatus.

## Implements

[protos.google.ads.datamanager.v1.RequestStatusPerDestination.IIngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.iingestcompositedatastatus)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.RequestStatusPerDestination.IIngestCompositeDataStatus);

Constructs a new IngestCompositeDataStatus.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.iingestcompositedatastatus)`   
Properties to set  
  
## Properties 

### dataTypeCounts
    
    
    public dataTypeCounts: google.ads.datamanager.v1.RequestStatusPerDestination.IDataTypeCount[];

IngestCompositeDataStatus dataTypeCounts.

### recordCount
    
    
    public recordCount: (number|Long|string);

IngestCompositeDataStatus recordCount.

### uploadMatchRateRange
    
    
    public uploadMatchRateRange: (google.ads.datamanager.v1.MatchRateRange|keyof typeof google.ads.datamanager.v1.MatchRateRange);

IngestCompositeDataStatus uploadMatchRateRange.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.RequestStatusPerDestination.IIngestCompositeDataStatus): google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus;

Creates a new IngestCompositeDataStatus instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.iingestcompositedatastatus)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus)` | IngestCompositeDataStatus instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus;

Decodes an IngestCompositeDataStatus message from the specified reader or buffer.

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
`[IngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus)` | IngestCompositeDataStatus  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus;

Decodes an IngestCompositeDataStatus message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus)` | IngestCompositeDataStatus  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.RequestStatusPerDestination.IIngestCompositeDataStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IngestCompositeDataStatus message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.iingestcompositedatastatus)`   
IngestCompositeDataStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.RequestStatusPerDestination.IIngestCompositeDataStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IngestCompositeDataStatus message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.iingestcompositedatastatus)`   
IngestCompositeDataStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus;

Creates an IngestCompositeDataStatus message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus)` | IngestCompositeDataStatus  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IngestCompositeDataStatus

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

Converts this IngestCompositeDataStatus to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.RequestStatusPerDestination.IngestCompositeDataStatus, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IngestCompositeDataStatus message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IngestCompositeDataStatus](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.requeststatusperdestination.ingestcompositedatastatus)`   
IngestCompositeDataStatus  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IngestCompositeDataStatus message.

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
