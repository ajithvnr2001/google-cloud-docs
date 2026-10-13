---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent
title: Class protos.google.cloud.retail.v2beta.UserEvent (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:44.367227+00:00
---

# Class protos.google.cloud.retail.v2beta.UserEvent (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.UserEvent (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a UserEvent.

## Implements

[protos.google.cloud.retail.v2beta.IUserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iuserevent)

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.retail.v2beta.IUserEvent);

Constructs a new UserEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iuserevent)`   
Properties to set  
  
## Properties 

### attributes
    
    
    public attributes: { [k: string]: google.cloud.retail.v2beta.ICustomAttribute };

UserEvent attributes.

### attributionToken
    
    
    public attributionToken: string;

UserEvent attributionToken.

### cartId
    
    
    public cartId: string;

UserEvent cartId.

### completionDetail
    
    
    public completionDetail?: (google.cloud.retail.v2beta.ICompletionDetail|null);

UserEvent completionDetail.

### entity
    
    
    public entity: string;

UserEvent entity.

### eventTime
    
    
    public eventTime?: (google.protobuf.ITimestamp|null);

UserEvent eventTime.

### eventType
    
    
    public eventType: string;

UserEvent eventType.

### experimentIds
    
    
    public experimentIds: string[];

UserEvent experimentIds.

### filter
    
    
    public filter: string;

UserEvent filter.

### offset
    
    
    public offset: number;

UserEvent offset.

### orderBy
    
    
    public orderBy: string;

UserEvent orderBy.

### pageCategories
    
    
    public pageCategories: string[];

UserEvent pageCategories.

### pageViewId
    
    
    public pageViewId: string;

UserEvent pageViewId.

### productDetails
    
    
    public productDetails: google.cloud.retail.v2beta.IProductDetail[];

UserEvent productDetails.

### purchaseTransaction
    
    
    public purchaseTransaction?: (google.cloud.retail.v2beta.IPurchaseTransaction|null);

UserEvent purchaseTransaction.

### referrerUri
    
    
    public referrerUri: string;

UserEvent referrerUri.

### searchQuery
    
    
    public searchQuery: string;

UserEvent searchQuery.

### sessionId
    
    
    public sessionId: string;

UserEvent sessionId.

### uri
    
    
    public uri: string;

UserEvent uri.

### userInfo
    
    
    public userInfo?: (google.cloud.retail.v2beta.IUserInfo|null);

UserEvent userInfo.

### visitorId
    
    
    public visitorId: string;

UserEvent visitorId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.retail.v2beta.IUserEvent): google.cloud.retail.v2beta.UserEvent;

Creates a new UserEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iuserevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent)` | UserEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.retail.v2beta.UserEvent;

Decodes a UserEvent message from the specified reader or buffer.

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
`[UserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent)` | UserEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.retail.v2beta.UserEvent;

Decodes a UserEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent)` | UserEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.retail.v2beta.IUserEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iuserevent)`   
UserEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.retail.v2beta.IUserEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UserEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iuserevent)`   
UserEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.retail.v2beta.UserEvent;

Creates a UserEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent)` | UserEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UserEvent

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

Converts this UserEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.retail.v2beta.UserEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a UserEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UserEvent](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.userevent)`   
UserEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a UserEvent message.

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
