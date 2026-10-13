---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class
title: Class protos.google.shopping.merchant.lfp.v1beta.LfpStore (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:23.962552+00:00
---

# Class protos.google.shopping.merchant.lfp.v1beta.LfpStore (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.lfp.v1beta.LfpStore (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a LfpStore.

## Implements

[protos.google.shopping.merchant.lfp.v1beta.ILfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpstore)

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.lfp.v1beta.ILfpStore);

Constructs a new LfpStore.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpstore)`   
Properties to set  
  
## Properties 

### gcidCategory
    
    
    public gcidCategory: string[];

LfpStore gcidCategory.

### matchingState
    
    
    public matchingState: (google.shopping.merchant.lfp.v1beta.LfpStore.StoreMatchingState|keyof typeof google.shopping.merchant.lfp.v1beta.LfpStore.StoreMatchingState);

LfpStore matchingState.

### matchingStateHint
    
    
    public matchingStateHint?: (string|null);

LfpStore matchingStateHint.

### name
    
    
    public name: string;

LfpStore name.

### phoneNumber
    
    
    public phoneNumber?: (string|null);

LfpStore phoneNumber.

### placeId
    
    
    public placeId?: (string|null);

LfpStore placeId.

### storeAddress
    
    
    public storeAddress: string;

LfpStore storeAddress.

### storeCode
    
    
    public storeCode: string;

LfpStore storeCode.

### storeName
    
    
    public storeName?: (string|null);

LfpStore storeName.

### targetAccount
    
    
    public targetAccount: (number|Long|string);

LfpStore targetAccount.

### websiteUri
    
    
    public websiteUri?: (string|null);

LfpStore websiteUri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.lfp.v1beta.ILfpStore): google.shopping.merchant.lfp.v1beta.LfpStore;

Creates a new LfpStore instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpstore)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)` | LfpStore instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.lfp.v1beta.LfpStore;

Decodes a LfpStore message from the specified reader or buffer.

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
`[LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)` | LfpStore  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.lfp.v1beta.LfpStore;

Decodes a LfpStore message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)` | LfpStore  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.lfp.v1beta.ILfpStore, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LfpStore message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpstore)`   
LfpStore message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.lfp.v1beta.ILfpStore, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LfpStore message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilfpstore)`   
LfpStore message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.lfp.v1beta.LfpStore;

Creates a LfpStore message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)` | LfpStore  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LfpStore

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

Converts this LfpStore to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.lfp.v1beta.LfpStore, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LfpStore message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)`   
LfpStore  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LfpStore message.

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
