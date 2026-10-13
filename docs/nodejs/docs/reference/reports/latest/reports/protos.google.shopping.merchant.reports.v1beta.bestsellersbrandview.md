---
url: https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview
title: Class protos.google.shopping.merchant.reports.v1beta.BestSellersBrandView (0.17.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:32.201380+00:00
---

# Class protos.google.shopping.merchant.reports.v1beta.BestSellersBrandView (0.17.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.reports.v1beta.BestSellersBrandView (0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.16.0  0.14.0  0.9.0  0.8.1  0.7.0  0.5.0  0.4.0 

Represents a BestSellersBrandView.

## Implements

[protos.google.shopping.merchant.reports.v1beta.IBestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.ibestsellersbrandview)

## Package

[@google-shopping/reports](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.reports.v1beta.IBestSellersBrandView);

Constructs a new BestSellersBrandView.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.ibestsellersbrandview)`   
Properties to set  
  
## Properties 

### brand
    
    
    public brand?: (string|null);

BestSellersBrandView brand.

### previousRank
    
    
    public previousRank?: (number|Long|string|null);

BestSellersBrandView previousRank.

### previousRelativeDemand
    
    
    public previousRelativeDemand?: (google.shopping.merchant.reports.v1beta.RelativeDemand.RelativeDemandEnum|keyof typeof google.shopping.merchant.reports.v1beta.RelativeDemand.RelativeDemandEnum|null);

BestSellersBrandView previousRelativeDemand.

### rank
    
    
    public rank?: (number|Long|string|null);

BestSellersBrandView rank.

### relativeDemand
    
    
    public relativeDemand?: (google.shopping.merchant.reports.v1beta.RelativeDemand.RelativeDemandEnum|keyof typeof google.shopping.merchant.reports.v1beta.RelativeDemand.RelativeDemandEnum|null);

BestSellersBrandView relativeDemand.

### relativeDemandChange
    
    
    public relativeDemandChange?: (google.shopping.merchant.reports.v1beta.RelativeDemandChangeType.RelativeDemandChangeTypeEnum|keyof typeof google.shopping.merchant.reports.v1beta.RelativeDemandChangeType.RelativeDemandChangeTypeEnum|null);

BestSellersBrandView relativeDemandChange.

### reportCategoryId
    
    
    public reportCategoryId?: (number|Long|string|null);

BestSellersBrandView reportCategoryId.

### reportCountryCode
    
    
    public reportCountryCode?: (string|null);

BestSellersBrandView reportCountryCode.

### reportDate
    
    
    public reportDate?: (google.type.IDate|null);

BestSellersBrandView reportDate.

### reportGranularity
    
    
    public reportGranularity?: (google.shopping.merchant.reports.v1beta.ReportGranularity.ReportGranularityEnum|keyof typeof google.shopping.merchant.reports.v1beta.ReportGranularity.ReportGranularityEnum|null);

BestSellersBrandView reportGranularity.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.reports.v1beta.IBestSellersBrandView): google.shopping.merchant.reports.v1beta.BestSellersBrandView;

Creates a new BestSellersBrandView instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.ibestsellersbrandview)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview)` | BestSellersBrandView instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.reports.v1beta.BestSellersBrandView;

Decodes a BestSellersBrandView message from the specified reader or buffer.

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
`[BestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview)` | BestSellersBrandView  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.reports.v1beta.BestSellersBrandView;

Decodes a BestSellersBrandView message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview)` | BestSellersBrandView  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.reports.v1beta.IBestSellersBrandView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BestSellersBrandView message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.ibestsellersbrandview)`   
BestSellersBrandView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.reports.v1beta.IBestSellersBrandView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BestSellersBrandView message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.ibestsellersbrandview)`   
BestSellersBrandView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.reports.v1beta.BestSellersBrandView;

Creates a BestSellersBrandView message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview)` | BestSellersBrandView  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BestSellersBrandView

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

Converts this BestSellersBrandView to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.reports.v1beta.BestSellersBrandView, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BestSellersBrandView message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BestSellersBrandView](https://docs.cloud.google.com/nodejs/docs/reference/reports/latest/reports/protos.google.shopping.merchant.reports.v1beta.bestsellersbrandview)`   
BestSellersBrandView  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BestSellersBrandView message.

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
