---
url: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class
title: Class protos.grafeas.v1.DiscoveryOccurrence (7.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:23.666919+00:00
---

# Class protos.grafeas.v1.DiscoveryOccurrence (7.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.grafeas.v1.DiscoveryOccurrence (7.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.1 (latest)  6.0.1  5.5.0  4.5.0  4.2.2  4.1.2  3.6.1  3.5.0  3.4.6 

Represents a DiscoveryOccurrence.

## Implements

[protos.grafeas.v1.IDiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.idiscoveryoccurrence)

## Package

[@google-cloud/grafeas](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: grafeas.v1.IDiscoveryOccurrence);

Constructs a new DiscoveryOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.idiscoveryoccurrence)`   
Properties to set  
  
## Properties 

### analysisCompleted
    
    
    public analysisCompleted?: (grafeas.v1.DiscoveryOccurrence.IAnalysisCompleted|null);

DiscoveryOccurrence analysisCompleted.

### analysisError
    
    
    public analysisError: google.rpc.IStatus[];

DiscoveryOccurrence analysisError.

### analysisStatus
    
    
    public analysisStatus: (grafeas.v1.DiscoveryOccurrence.AnalysisStatus|keyof typeof grafeas.v1.DiscoveryOccurrence.AnalysisStatus);

DiscoveryOccurrence analysisStatus.

### analysisStatusError
    
    
    public analysisStatusError?: (google.rpc.IStatus|null);

DiscoveryOccurrence analysisStatusError.

### archiveTime
    
    
    public archiveTime?: (google.protobuf.ITimestamp|null);

DiscoveryOccurrence archiveTime.

### continuousAnalysis
    
    
    public continuousAnalysis: (grafeas.v1.DiscoveryOccurrence.ContinuousAnalysis|keyof typeof grafeas.v1.DiscoveryOccurrence.ContinuousAnalysis);

DiscoveryOccurrence continuousAnalysis.

### cpe
    
    
    public cpe: string;

DiscoveryOccurrence cpe.

### files
    
    
    public files: grafeas.v1.DiscoveryOccurrence.IFile[];

DiscoveryOccurrence files.

### lastScanTime
    
    
    public lastScanTime?: (google.protobuf.ITimestamp|null);

DiscoveryOccurrence lastScanTime.

### lastVulnerabilityUpdateTime
    
    
    public lastVulnerabilityUpdateTime?: (google.protobuf.ITimestamp|null);

DiscoveryOccurrence lastVulnerabilityUpdateTime.

### sbomStatus
    
    
    public sbomStatus?: (grafeas.v1.DiscoveryOccurrence.ISBOMStatus|null);

DiscoveryOccurrence sbomStatus.

### vulnerabilityAttestation
    
    
    public vulnerabilityAttestation?: (grafeas.v1.DiscoveryOccurrence.IVulnerabilityAttestation|null);

DiscoveryOccurrence vulnerabilityAttestation.

## Methods 

### create(properties)
    
    
    public static create(properties?: grafeas.v1.IDiscoveryOccurrence): grafeas.v1.DiscoveryOccurrence;

Creates a new DiscoveryOccurrence instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.idiscoveryoccurrence)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class)` | DiscoveryOccurrence instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): grafeas.v1.DiscoveryOccurrence;

Decodes a DiscoveryOccurrence message from the specified reader or buffer.

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
`[DiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class)` | DiscoveryOccurrence  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): grafeas.v1.DiscoveryOccurrence;

Decodes a DiscoveryOccurrence message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class)` | DiscoveryOccurrence  
  
### encode(message, writer)
    
    
    public static encode(message: grafeas.v1.IDiscoveryOccurrence, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiscoveryOccurrence message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.idiscoveryoccurrence)`   
DiscoveryOccurrence message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: grafeas.v1.IDiscoveryOccurrence, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiscoveryOccurrence message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.idiscoveryoccurrence)`   
DiscoveryOccurrence message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): grafeas.v1.DiscoveryOccurrence;

Creates a DiscoveryOccurrence message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class)` | DiscoveryOccurrence  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DiscoveryOccurrence

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

Converts this DiscoveryOccurrence to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: grafeas.v1.DiscoveryOccurrence, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DiscoveryOccurrence message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DiscoveryOccurrence](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.discoveryoccurrence-class)`   
DiscoveryOccurrence  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DiscoveryOccurrence message.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
