---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense
title: Class protos.google.ads.datamanager.v1.UserListGlobalLicense (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:41.488466+00:00
---

# Class protos.google.ads.datamanager.v1.UserListGlobalLicense (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserListGlobalLicense (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserListGlobalLicense.

## Implements

[protos.google.ads.datamanager.v1.IUserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistgloballicense)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IUserListGlobalLicense);

Constructs a new UserListGlobalLicense.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistgloballicense)`   
Properties to set  
  
## Properties 

### historicalPricings
    
    
    public historicalPricings: google.ads.datamanager.v1.IUserListLicensePricing[];

UserListGlobalLicense historicalPricings.

### licenseType
    
    
    public licenseType?: (google.ads.datamanager.v1.UserListGlobalLicenseType|keyof typeof google.ads.datamanager.v1.UserListGlobalLicenseType|null);

UserListGlobalLicense licenseType.

### metrics
    
    
    public metrics?: (google.ads.datamanager.v1.IUserListLicenseMetrics|null);

UserListGlobalLicense metrics.

### name
    
    
    public name: string;

UserListGlobalLicense name.

### pricing
    
    
    public pricing?: (google.ads.datamanager.v1.IUserListLicensePricing|null);

UserListGlobalLicense pricing.

### status
    
    
    public status?: (google.ads.datamanager.v1.UserListLicenseStatus|keyof typeof google.ads.datamanager.v1.UserListLicenseStatus|null);

UserListGlobalLicense status.

### userListDisplayName
    
    
    public userListDisplayName: string;

UserListGlobalLicense userListDisplayName.

### userListId
    
    
    public userListId?: (number|Long|string|null);

UserListGlobalLicense userListId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IUserListGlobalLicense): google.ads.datamanager.v1.UserListGlobalLicense;

Creates a new UserListGlobalLicense instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistgloballicense)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)` | UserListGlobalLicense instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.UserListGlobalLicense;

Decodes a UserListGlobalLicense message from the specified reader or buffer.

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
`[UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)` | UserListGlobalLicense  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.UserListGlobalLicense;

Decodes a UserListGlobalLicense message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)` | UserListGlobalLicense  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IUserListGlobalLicense, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserListGlobalLicense message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistgloballicense)`   
UserListGlobalLicense message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IUserListGlobalLicense, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserListGlobalLicense message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlistgloballicense)`   
UserListGlobalLicense message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.UserListGlobalLicense;

Creates a UserListGlobalLicense message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)` | UserListGlobalLicense  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UserListGlobalLicense

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

Converts this UserListGlobalLicense to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.UserListGlobalLicense, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a UserListGlobalLicense message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UserListGlobalLicense](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlistgloballicense)`   
UserListGlobalLicense  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a UserListGlobalLicense message.

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
