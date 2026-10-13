---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings
title: Class protos.google.cloud.chronicle.v1.AmazonSQSV2Settings (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:50:52.911952+00:00
---

# Class protos.google.cloud.chronicle.v1.AmazonSQSV2Settings (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.AmazonSQSV2Settings (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents an AmazonSQSV2Settings.

## Implements

[protos.google.cloud.chronicle.v1.IAmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iamazonsqsv2settings)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IAmazonSQSV2Settings);

Constructs a new AmazonSQSV2Settings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iamazonsqsv2settings)`   
Properties to set  
  
## Properties 

### authentication
    
    
    public authentication?: (google.cloud.chronicle.v1.ISQSAuthV2|null);

AmazonSQSV2Settings authentication.

### chronicleServiceAccount
    
    
    public chronicleServiceAccount: string;

AmazonSQSV2Settings chronicleServiceAccount.

### includePrefixes
    
    
    public includePrefixes: string[];

AmazonSQSV2Settings includePrefixes.

### maxLookbackDays
    
    
    public maxLookbackDays: number;

AmazonSQSV2Settings maxLookbackDays.

### queue
    
    
    public queue: string;

AmazonSQSV2Settings queue.

### s3Uri
    
    
    public s3Uri: string;

AmazonSQSV2Settings s3Uri.

### sourceDeletionOption
    
    
    public sourceDeletionOption: (google.cloud.chronicle.v1.SourceDeletionOptionV2|keyof typeof google.cloud.chronicle.v1.SourceDeletionOptionV2);

AmazonSQSV2Settings sourceDeletionOption.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IAmazonSQSV2Settings): google.cloud.chronicle.v1.AmazonSQSV2Settings;

Creates a new AmazonSQSV2Settings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iamazonsqsv2settings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings)` | AmazonSQSV2Settings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.AmazonSQSV2Settings;

Decodes an AmazonSQSV2Settings message from the specified reader or buffer.

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
`[AmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings)` | AmazonSQSV2Settings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.AmazonSQSV2Settings;

Decodes an AmazonSQSV2Settings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings)` | AmazonSQSV2Settings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IAmazonSQSV2Settings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AmazonSQSV2Settings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iamazonsqsv2settings)`   
AmazonSQSV2Settings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IAmazonSQSV2Settings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AmazonSQSV2Settings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iamazonsqsv2settings)`   
AmazonSQSV2Settings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.AmazonSQSV2Settings;

Creates an AmazonSQSV2Settings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings)` | AmazonSQSV2Settings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AmazonSQSV2Settings

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

Converts this AmazonSQSV2Settings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.AmazonSQSV2Settings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AmazonSQSV2Settings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AmazonSQSV2Settings](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.amazonsqsv2settings)`   
AmazonSQSV2Settings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AmazonSQSV2Settings message.

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
