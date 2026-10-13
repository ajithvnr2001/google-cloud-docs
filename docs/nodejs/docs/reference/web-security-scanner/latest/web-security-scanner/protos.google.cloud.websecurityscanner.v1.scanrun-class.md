---
url: https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class
title: Class protos.google.cloud.websecurityscanner.v1.ScanRun (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:52.592249+00:00
---

# Class protos.google.cloud.websecurityscanner.v1.ScanRun (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.websecurityscanner.v1.ScanRun (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.1.5  1.1.1  1.0.7 

Represents a ScanRun.

## Implements

[protos.google.cloud.websecurityscanner.v1.IScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.iscanrun)

## Package

[@google-cloud/web-security-scanner](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.websecurityscanner.v1.IScanRun);

Constructs a new ScanRun.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.iscanrun)`   
Properties to set  
  
## Properties 

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

ScanRun endTime.

### errorTrace
    
    
    public errorTrace?: (google.cloud.websecurityscanner.v1.IScanRunErrorTrace|null);

ScanRun errorTrace.

### executionState
    
    
    public executionState: (google.cloud.websecurityscanner.v1.ScanRun.ExecutionState|keyof typeof google.cloud.websecurityscanner.v1.ScanRun.ExecutionState);

ScanRun executionState.

### hasVulnerabilities
    
    
    public hasVulnerabilities: boolean;

ScanRun hasVulnerabilities.

### name
    
    
    public name: string;

ScanRun name.

### progressPercent
    
    
    public progressPercent: number;

ScanRun progressPercent.

### resultState
    
    
    public resultState: (google.cloud.websecurityscanner.v1.ScanRun.ResultState|keyof typeof google.cloud.websecurityscanner.v1.ScanRun.ResultState);

ScanRun resultState.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

ScanRun startTime.

### urlsCrawledCount
    
    
    public urlsCrawledCount: (number|Long|string);

ScanRun urlsCrawledCount.

### urlsTestedCount
    
    
    public urlsTestedCount: (number|Long|string);

ScanRun urlsTestedCount.

### warningTraces
    
    
    public warningTraces: google.cloud.websecurityscanner.v1.IScanRunWarningTrace[];

ScanRun warningTraces.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.websecurityscanner.v1.IScanRun): google.cloud.websecurityscanner.v1.ScanRun;

Creates a new ScanRun instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.iscanrun)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class)` | ScanRun instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.websecurityscanner.v1.ScanRun;

Decodes a ScanRun message from the specified reader or buffer.

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
`[ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class)` | ScanRun  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.websecurityscanner.v1.ScanRun;

Decodes a ScanRun message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class)` | ScanRun  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.websecurityscanner.v1.IScanRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ScanRun message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.iscanrun)`   
ScanRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.websecurityscanner.v1.IScanRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ScanRun message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.iscanrun)`   
ScanRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.websecurityscanner.v1.ScanRun;

Creates a ScanRun message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class)` | ScanRun  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ScanRun

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

Converts this ScanRun to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.websecurityscanner.v1.ScanRun, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ScanRun message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1.scanrun-class)`   
ScanRun  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ScanRun message.

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
