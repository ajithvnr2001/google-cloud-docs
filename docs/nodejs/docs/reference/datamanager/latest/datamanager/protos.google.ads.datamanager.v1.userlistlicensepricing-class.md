---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class
title: Class protos.google.ads.datamanager.v1.UserListLicensePricing (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:42.320321+00:00
---

# Class protos.google.ads.datamanager.v1.UserListLicensePricing (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserListLicensePricing (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserListLicensePricing.

## Implements

[protos.google.ads.datamanager.v1.IUserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistlicensepricing)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IUserListLicensePricing);

Constructs a new UserListLicensePricing.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistlicensepricing)`   
Properties to set  
  
## Properties 

### buyerApprovalState
    
    
    public buyerApprovalState: (google.ads.datamanager.v1.UserListLicensePricing.UserListPricingBuyerApprovalState|keyof typeof google.ads.datamanager.v1.UserListLicensePricing.UserListPricingBuyerApprovalState);

UserListLicensePricing buyerApprovalState.

### costMicros
    
    
    public costMicros?: (number|Long|string|null);

UserListLicensePricing costMicros.

### costType
    
    
    public costType?: (google.ads.datamanager.v1.UserListLicensePricing.UserListPricingCostType|keyof typeof google.ads.datamanager.v1.UserListLicensePricing.UserListPricingCostType|null);

UserListLicensePricing costType.

### currencyCode
    
    
    public currencyCode?: (string|null);

UserListLicensePricing currencyCode.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

UserListLicensePricing endTime.

### maxCostMicros
    
    
    public maxCostMicros?: (number|Long|string|null);

UserListLicensePricing maxCostMicros.

### pricingActive
    
    
    public pricingActive: boolean;

UserListLicensePricing pricingActive.

### pricingId
    
    
    public pricingId: (number|Long|string);

UserListLicensePricing pricingId.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

UserListLicensePricing startTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IUserListLicensePricing): google.ads.datamanager.v1.UserListLicensePricing;

Creates a new UserListLicensePricing instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistlicensepricing)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class)` | UserListLicensePricing instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.UserListLicensePricing;

Decodes a UserListLicensePricing message from the specified reader or buffer.

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
`[UserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class)` | UserListLicensePricing  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.UserListLicensePricing;

Decodes a UserListLicensePricing message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class)` | UserListLicensePricing  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IUserListLicensePricing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserListLicensePricing message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistlicensepricing)`   
UserListLicensePricing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IUserListLicensePricing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserListLicensePricing message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistlicensepricing)`   
UserListLicensePricing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.UserListLicensePricing;

Creates a UserListLicensePricing message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class)` | UserListLicensePricing  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UserListLicensePricing

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

Converts this UserListLicensePricing to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.UserListLicensePricing, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a UserListLicensePricing message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UserListLicensePricing](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistlicensepricing-class)`   
UserListLicensePricing  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a UserListLicensePricing message.

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
