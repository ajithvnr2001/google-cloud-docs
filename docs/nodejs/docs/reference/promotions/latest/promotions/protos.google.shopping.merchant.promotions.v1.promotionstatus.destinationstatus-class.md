---
url: https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class
title: Class protos.google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:58.144842+00:00
---

# Class protos.google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.6.0  0.2.1  0.1.0 

Represents a DestinationStatus.

## Implements

[protos.google.shopping.merchant.promotions.v1.PromotionStatus.IDestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.idestinationstatus)

## Package

[@google-shopping/promotions](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.promotions.v1.PromotionStatus.IDestinationStatus);

Constructs a new DestinationStatus.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.idestinationstatus)`   
Properties to set  
  
## Properties 

### reportingContext
    
    
    public reportingContext: (google.shopping.type.ReportingContext.ReportingContextEnum|keyof typeof google.shopping.type.ReportingContext.ReportingContextEnum);

DestinationStatus reportingContext.

### status
    
    
    public status: (google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus.State|keyof typeof google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus.State);

DestinationStatus status.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.promotions.v1.PromotionStatus.IDestinationStatus): google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus;

Creates a new DestinationStatus instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.idestinationstatus)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class)` | DestinationStatus instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus;

Decodes a DestinationStatus message from the specified reader or buffer.

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
`[DestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class)` | DestinationStatus  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus;

Decodes a DestinationStatus message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class)` | DestinationStatus  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.promotions.v1.PromotionStatus.IDestinationStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DestinationStatus message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.idestinationstatus)`   
DestinationStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.promotions.v1.PromotionStatus.IDestinationStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DestinationStatus message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.idestinationstatus)`   
DestinationStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus;

Creates a DestinationStatus message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class)` | DestinationStatus  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DestinationStatus

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

Converts this DestinationStatus to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.promotions.v1.PromotionStatus.DestinationStatus, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DestinationStatus message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DestinationStatus](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionstatus.destinationstatus-class)`   
DestinationStatus  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DestinationStatus message.

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
