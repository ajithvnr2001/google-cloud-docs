---
url: https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class
title: Class protos.google.shopping.merchant.issueresolution.v1beta.Callout (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:30.639817+00:00
---

# Class protos.google.shopping.merchant.issueresolution.v1beta.Callout (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.issueresolution.v1beta.Callout (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.4.0 

Represents a Callout.

## Implements

[protos.google.shopping.merchant.issueresolution.v1beta.ICallout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.icallout)

## Package

[@google-shopping/issueresolution](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.issueresolution.v1beta.ICallout);

Constructs a new Callout.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICallout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.icallout)`   
Properties to set  
  
## Properties 

### fullMessage
    
    
    public fullMessage?: (google.shopping.merchant.issueresolution.v1beta.ITextWithTooltip|null);

Callout fullMessage.

### styleHint
    
    
    public styleHint: (google.shopping.merchant.issueresolution.v1beta.Callout.CalloutStyleHint|keyof typeof google.shopping.merchant.issueresolution.v1beta.Callout.CalloutStyleHint);

Callout styleHint.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.issueresolution.v1beta.ICallout): google.shopping.merchant.issueresolution.v1beta.Callout;

Creates a new Callout instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICallout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.icallout)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Callout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class)` | Callout instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.issueresolution.v1beta.Callout;

Decodes a Callout message from the specified reader or buffer.

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
`[Callout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class)` | Callout  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.issueresolution.v1beta.Callout;

Decodes a Callout message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Callout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class)` | Callout  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.issueresolution.v1beta.ICallout, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Callout message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICallout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.icallout)`   
Callout message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.issueresolution.v1beta.ICallout, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Callout message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICallout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.icallout)`   
Callout message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.issueresolution.v1beta.Callout;

Creates a Callout message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Callout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class)` | Callout  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Callout

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

Converts this Callout to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.issueresolution.v1beta.Callout, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Callout message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Callout](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.callout-class)`   
Callout  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Callout message.

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
