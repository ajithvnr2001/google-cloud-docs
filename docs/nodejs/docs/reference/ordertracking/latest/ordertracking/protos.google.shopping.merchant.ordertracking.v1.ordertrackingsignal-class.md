---
url: https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class
title: Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignal (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:36.256483+00:00
---

# Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignal (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignal (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.4.0 

Represents an OrderTrackingSignal.

## Implements

[protos.google.shopping.merchant.ordertracking.v1.IOrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.iordertrackingsignal)

## Package

[@google-shopping/ordertracking](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.ordertracking.v1.IOrderTrackingSignal);

Constructs a new OrderTrackingSignal.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.iordertrackingsignal)`   
Properties to set  
  
## Properties 

### customerShippingFee
    
    
    public customerShippingFee?: (google.shopping.type.IPrice|null);

OrderTrackingSignal customerShippingFee.

### deliveryPostalCode
    
    
    public deliveryPostalCode: string;

OrderTrackingSignal deliveryPostalCode.

### deliveryRegionCode
    
    
    public deliveryRegionCode: string;

OrderTrackingSignal deliveryRegionCode.

### lineItems
    
    
    public lineItems: google.shopping.merchant.ordertracking.v1.OrderTrackingSignal.ILineItemDetails[];

OrderTrackingSignal lineItems.

### merchantId
    
    
    public merchantId: (number|Long|string);

OrderTrackingSignal merchantId.

### orderCreatedTime
    
    
    public orderCreatedTime?: (google.type.IDateTime|null);

OrderTrackingSignal orderCreatedTime.

### orderId
    
    
    public orderId: string;

OrderTrackingSignal orderId.

### orderTrackingSignalId
    
    
    public orderTrackingSignalId: (number|Long|string);

OrderTrackingSignal orderTrackingSignalId.

### shipmentLineItemMapping
    
    
    public shipmentLineItemMapping: google.shopping.merchant.ordertracking.v1.OrderTrackingSignal.IShipmentLineItemMapping[];

OrderTrackingSignal shipmentLineItemMapping.

### shippingInfo
    
    
    public shippingInfo: google.shopping.merchant.ordertracking.v1.OrderTrackingSignal.IShippingInfo[];

OrderTrackingSignal shippingInfo.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.ordertracking.v1.IOrderTrackingSignal): google.shopping.merchant.ordertracking.v1.OrderTrackingSignal;

Creates a new OrderTrackingSignal instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.iordertrackingsignal)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)` | OrderTrackingSignal instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.ordertracking.v1.OrderTrackingSignal;

Decodes an OrderTrackingSignal message from the specified reader or buffer.

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
`[OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)` | OrderTrackingSignal  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.ordertracking.v1.OrderTrackingSignal;

Decodes an OrderTrackingSignal message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)` | OrderTrackingSignal  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.ordertracking.v1.IOrderTrackingSignal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OrderTrackingSignal message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.iordertrackingsignal)`   
OrderTrackingSignal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.ordertracking.v1.IOrderTrackingSignal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OrderTrackingSignal message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.iordertrackingsignal)`   
OrderTrackingSignal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.ordertracking.v1.OrderTrackingSignal;

Creates an OrderTrackingSignal message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)` | OrderTrackingSignal  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OrderTrackingSignal

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

Converts this OrderTrackingSignal to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.ordertracking.v1.OrderTrackingSignal, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OrderTrackingSignal message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)`   
OrderTrackingSignal  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OrderTrackingSignal message.

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
