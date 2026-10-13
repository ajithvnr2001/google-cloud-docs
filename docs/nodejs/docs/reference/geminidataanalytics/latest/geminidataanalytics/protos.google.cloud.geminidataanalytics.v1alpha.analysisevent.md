---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent
title: Class protos.google.cloud.geminidataanalytics.v1alpha.AnalysisEvent (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:55.201102+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1alpha.AnalysisEvent (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1alpha.AnalysisEvent (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents an AnalysisEvent.

## Implements

[protos.google.cloud.geminidataanalytics.v1alpha.IAnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ianalysisevent)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1alpha.IAnalysisEvent);

Constructs a new AnalysisEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ianalysisevent)`   
Properties to set  
  
## Properties 

### code
    
    
    public code?: (string|null);

AnalysisEvent code.

### coderInstruction
    
    
    public coderInstruction?: (string|null);

AnalysisEvent coderInstruction.

### error
    
    
    public error?: (string|null);

AnalysisEvent error.

### executionError
    
    
    public executionError?: (string|null);

AnalysisEvent executionError.

### executionOutput
    
    
    public executionOutput?: (string|null);

AnalysisEvent executionOutput.

### kind
    
    
    public kind?: ("plannerReasoning"|"coderInstruction"|"code"|"executionOutput"|"executionError"|"resultVegaChartJson"|"resultNaturalLanguage"|"resultCsvData"|"resultReferenceData"|"error");

AnalysisEvent kind.

### plannerReasoning
    
    
    public plannerReasoning?: (string|null);

AnalysisEvent plannerReasoning.

### resultCsvData
    
    
    public resultCsvData?: (string|null);

AnalysisEvent resultCsvData.

### resultNaturalLanguage
    
    
    public resultNaturalLanguage?: (string|null);

AnalysisEvent resultNaturalLanguage.

### resultReferenceData
    
    
    public resultReferenceData?: (string|null);

AnalysisEvent resultReferenceData.

### resultVegaChartJson
    
    
    public resultVegaChartJson?: (string|null);

AnalysisEvent resultVegaChartJson.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1alpha.IAnalysisEvent): google.cloud.geminidataanalytics.v1alpha.AnalysisEvent;

Creates a new AnalysisEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ianalysisevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent)` | AnalysisEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1alpha.AnalysisEvent;

Decodes an AnalysisEvent message from the specified reader or buffer.

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
`[AnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent)` | AnalysisEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1alpha.AnalysisEvent;

Decodes an AnalysisEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent)` | AnalysisEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1alpha.IAnalysisEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalysisEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ianalysisevent)`   
AnalysisEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1alpha.IAnalysisEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalysisEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ianalysisevent)`   
AnalysisEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1alpha.AnalysisEvent;

Creates an AnalysisEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent)` | AnalysisEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnalysisEvent

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

Converts this AnalysisEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1alpha.AnalysisEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnalysisEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnalysisEvent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.analysisevent)`   
AnalysisEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnalysisEvent message.

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
