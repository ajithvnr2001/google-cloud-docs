---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity
title: Class protos.google.cloud.chronicle.v1.FindingsRefinementActivity (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:38.115857+00:00
---

# Class protos.google.cloud.chronicle.v1.FindingsRefinementActivity (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.FindingsRefinementActivity (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a FindingsRefinementActivity.

## Implements

[protos.google.cloud.chronicle.v1.IFindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifindingsrefinementactivity)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IFindingsRefinementActivity);

Constructs a new FindingsRefinementActivity.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifindingsrefinementactivity)`   
Properties to set  
  
## Properties 

### Activity
    
    
    public Activity?: "detectionExclusionActivity";

FindingsRefinementActivity Activity.

### detectionExclusionActivity
    
    
    public detectionExclusionActivity?: (google.cloud.chronicle.v1.IDetectionExclusionActivity|null);

FindingsRefinementActivity detectionExclusionActivity.

### findingsRefinement
    
    
    public findingsRefinement: string;

FindingsRefinementActivity findingsRefinement.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IFindingsRefinementActivity): google.cloud.chronicle.v1.FindingsRefinementActivity;

Creates a new FindingsRefinementActivity instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifindingsrefinementactivity)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity)` | FindingsRefinementActivity instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.FindingsRefinementActivity;

Decodes a FindingsRefinementActivity message from the specified reader or buffer.

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
`[FindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity)` | FindingsRefinementActivity  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.FindingsRefinementActivity;

Decodes a FindingsRefinementActivity message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity)` | FindingsRefinementActivity  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IFindingsRefinementActivity, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FindingsRefinementActivity message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifindingsrefinementactivity)`   
FindingsRefinementActivity message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IFindingsRefinementActivity, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FindingsRefinementActivity message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifindingsrefinementactivity)`   
FindingsRefinementActivity message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.FindingsRefinementActivity;

Creates a FindingsRefinementActivity message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity)` | FindingsRefinementActivity  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FindingsRefinementActivity

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

Converts this FindingsRefinementActivity to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.FindingsRefinementActivity, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FindingsRefinementActivity message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FindingsRefinementActivity](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementactivity)`   
FindingsRefinementActivity  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FindingsRefinementActivity message.

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
