---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class
title: Class protos.google.ads.datamanager.v1.UserList (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:41.325498+00:00
---

# Class protos.google.ads.datamanager.v1.UserList (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.UserList (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a UserList.

## Implements

[protos.google.ads.datamanager.v1.IUserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlist)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IUserList);

Constructs a new UserList.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlist)`   
Properties to set  
  
## Properties 

### accessReason
    
    
    public accessReason: (google.ads.datamanager.v1.UserList.AccessReason|keyof typeof google.ads.datamanager.v1.UserList.AccessReason);

UserList accessReason.

### accountAccessStatus
    
    
    public accountAccessStatus?: (google.ads.datamanager.v1.UserList.AccessStatus|keyof typeof google.ads.datamanager.v1.UserList.AccessStatus|null);

UserList accountAccessStatus.

### closingReason
    
    
    public closingReason?: (google.ads.datamanager.v1.UserList.ClosingReason|keyof typeof google.ads.datamanager.v1.UserList.ClosingReason|null);

UserList closingReason.

### description
    
    
    public description?: (string|null);

UserList description.

### displayName
    
    
    public displayName?: (string|null);

UserList displayName.

### id
    
    
    public id: (number|Long|string);

UserList id.

### ingestedUserListInfo
    
    
    public ingestedUserListInfo?: (google.ads.datamanager.v1.IIngestedUserListInfo|null);

UserList ingestedUserListInfo.

### integrationCode
    
    
    public integrationCode?: (string|null);

UserList integrationCode.

### membershipDuration
    
    
    public membershipDuration?: (google.protobuf.IDuration|null);

UserList membershipDuration.

### membershipStatus
    
    
    public membershipStatus?: (google.ads.datamanager.v1.UserList.MembershipStatus|keyof typeof google.ads.datamanager.v1.UserList.MembershipStatus|null);

UserList membershipStatus.

### name
    
    
    public name: string;

UserList name.

### readOnly
    
    
    public readOnly: boolean;

UserList readOnly.

### sizeInfo
    
    
    public sizeInfo?: (google.ads.datamanager.v1.ISizeInfo|null);

UserList sizeInfo.

### targetNetworkInfo
    
    
    public targetNetworkInfo?: (google.ads.datamanager.v1.ITargetNetworkInfo|null);

UserList targetNetworkInfo.

### userListInfo
    
    
    public userListInfo?: "ingestedUserListInfo";

UserList userListInfo.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IUserList): google.ads.datamanager.v1.UserList;

Creates a new UserList instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlist)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)` | UserList instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.UserList;

Decodes a UserList message from the specified reader or buffer.

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
`[UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)` | UserList  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.UserList;

Decodes a UserList message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)` | UserList  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IUserList, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserList message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlist)`   
UserList message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IUserList, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserList message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iuserlist)`   
UserList message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.UserList;

Creates a UserList message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)` | UserList  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UserList

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

Converts this UserList to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.UserList, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a UserList message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UserList](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.userlist-class)`   
UserList  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a UserList message.

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
