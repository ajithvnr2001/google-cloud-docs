---
url: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis
title: Class protos.google.maps.solar.v1.FinancialAnalysis (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:20:32.717040+00:00
---

# Class protos.google.maps.solar.v1.FinancialAnalysis (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.solar.v1.FinancialAnalysis (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.1.0 

Represents a FinancialAnalysis.

## Implements

[protos.google.maps.solar.v1.IFinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifinancialanalysis)

## Package

[@googlemaps/solar](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.solar.v1.IFinancialAnalysis);

Constructs a new FinancialAnalysis.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifinancialanalysis)`   
Properties to set  
  
## Properties 

### averageKwhPerMonth
    
    
    public averageKwhPerMonth: number;

FinancialAnalysis averageKwhPerMonth.

### cashPurchaseSavings
    
    
    public cashPurchaseSavings?: (google.maps.solar.v1.ICashPurchaseSavings|null);

FinancialAnalysis cashPurchaseSavings.

### defaultBill
    
    
    public defaultBill: boolean;

FinancialAnalysis defaultBill.

### financedPurchaseSavings
    
    
    public financedPurchaseSavings?: (google.maps.solar.v1.IFinancedPurchaseSavings|null);

FinancialAnalysis financedPurchaseSavings.

### financialDetails
    
    
    public financialDetails?: (google.maps.solar.v1.IFinancialDetails|null);

FinancialAnalysis financialDetails.

### leasingSavings
    
    
    public leasingSavings?: (google.maps.solar.v1.ILeasingSavings|null);

FinancialAnalysis leasingSavings.

### monthlyBill
    
    
    public monthlyBill?: (google.type.IMoney|null);

FinancialAnalysis monthlyBill.

### panelConfigIndex
    
    
    public panelConfigIndex?: (number|null);

FinancialAnalysis panelConfigIndex.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.solar.v1.IFinancialAnalysis): google.maps.solar.v1.FinancialAnalysis;

Creates a new FinancialAnalysis instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifinancialanalysis)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis)` | FinancialAnalysis instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.solar.v1.FinancialAnalysis;

Decodes a FinancialAnalysis message from the specified reader or buffer.

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
`[FinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis)` | FinancialAnalysis  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.solar.v1.FinancialAnalysis;

Decodes a FinancialAnalysis message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis)` | FinancialAnalysis  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.solar.v1.IFinancialAnalysis, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FinancialAnalysis message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifinancialanalysis)`   
FinancialAnalysis message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.solar.v1.IFinancialAnalysis, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FinancialAnalysis message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifinancialanalysis)`   
FinancialAnalysis message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.solar.v1.FinancialAnalysis;

Creates a FinancialAnalysis message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis)` | FinancialAnalysis  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FinancialAnalysis

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

Converts this FinancialAnalysis to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.solar.v1.FinancialAnalysis, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FinancialAnalysis message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FinancialAnalysis](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.financialanalysis)`   
FinancialAnalysis  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FinancialAnalysis message.

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
