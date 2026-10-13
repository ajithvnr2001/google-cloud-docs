---
url: https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary
title: Class protos.google.cloud.storagebatchoperations.v1.ErrorSummary (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:14.936061+00:00
---

# Class protos.google.cloud.storagebatchoperations.v1.ErrorSummary (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.storagebatchoperations.v1.ErrorSummary (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.5.0 

Represents an ErrorSummary.

## Implements

[protos.google.cloud.storagebatchoperations.v1.IErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ierrorsummary)

## Package

[@google-cloud/storagebatchoperations](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.storagebatchoperations.v1.IErrorSummary);

Constructs a new ErrorSummary.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ierrorsummary)`   
Properties to set  
  
## Properties 

### errorCode
    
    
    public errorCode: (google.rpc.Code|keyof typeof google.rpc.Code);

ErrorSummary errorCode.

### errorCount
    
    
    public errorCount: (number|Long|string);

ErrorSummary errorCount.

### errorLogEntries
    
    
    public errorLogEntries: google.cloud.storagebatchoperations.v1.IErrorLogEntry[];

ErrorSummary errorLogEntries.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.storagebatchoperations.v1.IErrorSummary): google.cloud.storagebatchoperations.v1.ErrorSummary;

Creates a new ErrorSummary instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ierrorsummary)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary)` | ErrorSummary instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.storagebatchoperations.v1.ErrorSummary;

Decodes an ErrorSummary message from the specified reader or buffer.

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
`[ErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary)` | ErrorSummary  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.storagebatchoperations.v1.ErrorSummary;

Decodes an ErrorSummary message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary)` | ErrorSummary  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.storagebatchoperations.v1.IErrorSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ErrorSummary message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ierrorsummary)`   
ErrorSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.storagebatchoperations.v1.IErrorSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ErrorSummary message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ierrorsummary)`   
ErrorSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.storagebatchoperations.v1.ErrorSummary;

Creates an ErrorSummary message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary)` | ErrorSummary  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ErrorSummary

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

Converts this ErrorSummary to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.storagebatchoperations.v1.ErrorSummary, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ErrorSummary message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ErrorSummary](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.errorsummary)`   
ErrorSummary  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ErrorSummary message.

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
