---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class
title: Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:19.076186+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a DataStoreConnectionSignals.

## Implements

[protos.google.cloud.dialogflow.cx.v3.IDataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.idatastoreconnectionsignals)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.cx.v3.IDataStoreConnectionSignals);

Constructs a new DataStoreConnectionSignals.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.idatastoreconnectionsignals)`   
Properties to set  
  
## Properties 

### answer
    
    
    public answer: string;

DataStoreConnectionSignals answer.

### answerGenerationModelCallSignals
    
    
    public answerGenerationModelCallSignals?: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.IAnswerGenerationModelCallSignals|null);

DataStoreConnectionSignals answerGenerationModelCallSignals.

### answerParts
    
    
    public answerParts: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.IAnswerPart[];

DataStoreConnectionSignals answerParts.

### citedSnippets
    
    
    public citedSnippets: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ICitedSnippet[];

DataStoreConnectionSignals citedSnippets.

### groundingSignals
    
    
    public groundingSignals?: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.IGroundingSignals|null);

DataStoreConnectionSignals groundingSignals.

### rewriterModelCallSignals
    
    
    public rewriterModelCallSignals?: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.IRewriterModelCallSignals|null);

DataStoreConnectionSignals rewriterModelCallSignals.

### rewrittenQuery
    
    
    public rewrittenQuery: string;

DataStoreConnectionSignals rewrittenQuery.

### safetySignals
    
    
    public safetySignals?: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals|null);

DataStoreConnectionSignals safetySignals.

### searchSnippets
    
    
    public searchSnippets: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISearchSnippet[];

DataStoreConnectionSignals searchSnippets.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.cx.v3.IDataStoreConnectionSignals): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals;

Creates a new DataStoreConnectionSignals instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.idatastoreconnectionsignals)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class)` | DataStoreConnectionSignals instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals;

Decodes a DataStoreConnectionSignals message from the specified reader or buffer.

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
`[DataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class)` | DataStoreConnectionSignals  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals;

Decodes a DataStoreConnectionSignals message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class)` | DataStoreConnectionSignals  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.cx.v3.IDataStoreConnectionSignals, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataStoreConnectionSignals message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.idatastoreconnectionsignals)`   
DataStoreConnectionSignals message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.cx.v3.IDataStoreConnectionSignals, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataStoreConnectionSignals message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.idatastoreconnectionsignals)`   
DataStoreConnectionSignals message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals;

Creates a DataStoreConnectionSignals message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class)` | DataStoreConnectionSignals  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataStoreConnectionSignals

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

Converts this DataStoreConnectionSignals to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataStoreConnectionSignals message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataStoreConnectionSignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals-class)`   
DataStoreConnectionSignals  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataStoreConnectionSignals message.

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
