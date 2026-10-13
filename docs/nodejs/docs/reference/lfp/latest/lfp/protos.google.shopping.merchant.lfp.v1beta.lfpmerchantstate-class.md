---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class
title: Class protos.google.shopping.merchant.lfp.v1beta.LfpMerchantState (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:23.326621+00:00
---

# Class protos.google.shopping.merchant.lfp.v1beta.LfpMerchantState (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.lfp.v1beta.LfpMerchantState (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a LfpMerchantState.

## Implements

[protos.google.shopping.merchant.lfp.v1beta.ILfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpmerchantstate)

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.lfp.v1beta.ILfpMerchantState);

Constructs a new LfpMerchantState.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpmerchantstate)`   
Properties to set  
  
## Properties 

### countrySettings
    
    
    public countrySettings: google.shopping.merchant.lfp.v1beta.LfpMerchantState.ICountrySettings[];

LfpMerchantState countrySettings.

### inventoryStats
    
    
    public inventoryStats?: (google.shopping.merchant.lfp.v1beta.LfpMerchantState.IInventoryStats|null);

LfpMerchantState inventoryStats.

### linkedGbps
    
    
    public linkedGbps: (number|Long|string);

LfpMerchantState linkedGbps.

### name
    
    
    public name: string;

LfpMerchantState name.

### storeStates
    
    
    public storeStates: google.shopping.merchant.lfp.v1beta.LfpMerchantState.ILfpStoreState[];

LfpMerchantState storeStates.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.lfp.v1beta.ILfpMerchantState): google.shopping.merchant.lfp.v1beta.LfpMerchantState;

Creates a new LfpMerchantState instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpmerchantstate)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class)` | LfpMerchantState instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.lfp.v1beta.LfpMerchantState;

Decodes a LfpMerchantState message from the specified reader or buffer.

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
`[LfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class)` | LfpMerchantState  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.lfp.v1beta.LfpMerchantState;

Decodes a LfpMerchantState message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class)` | LfpMerchantState  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.lfp.v1beta.ILfpMerchantState, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LfpMerchantState message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpmerchantstate)`   
LfpMerchantState message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.lfp.v1beta.ILfpMerchantState, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LfpMerchantState message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpmerchantstate)`   
LfpMerchantState message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.lfp.v1beta.LfpMerchantState;

Creates a LfpMerchantState message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class)` | LfpMerchantState  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LfpMerchantState

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

Converts this LfpMerchantState to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.lfp.v1beta.LfpMerchantState, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LfpMerchantState message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LfpMerchantState](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpmerchantstate-class)`   
LfpMerchantState  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LfpMerchantState message.

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
