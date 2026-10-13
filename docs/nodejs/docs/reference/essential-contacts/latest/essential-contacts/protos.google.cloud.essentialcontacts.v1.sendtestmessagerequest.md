---
url: https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest
title: Class protos.google.cloud.essentialcontacts.v1.SendTestMessageRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:25.195636+00:00
---

# Class protos.google.cloud.essentialcontacts.v1.SendTestMessageRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.essentialcontacts.v1.SendTestMessageRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.2.0  3.0.0  2.1.2  2.0.2  1.1.1  1.0.6 

Represents a SendTestMessageRequest.

## Implements

[protos.google.cloud.essentialcontacts.v1.ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)

## Package

[@google-cloud/essential-contacts](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.essentialcontacts.v1.ISendTestMessageRequest);

Constructs a new SendTestMessageRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
Properties to set  
  
## Properties 

### contacts
    
    
    public contacts: string[];

SendTestMessageRequest contacts.

### notificationCategory
    
    
    public notificationCategory: (google.cloud.essentialcontacts.v1.NotificationCategory|keyof typeof google.cloud.essentialcontacts.v1.NotificationCategory);

SendTestMessageRequest notificationCategory.

### resource
    
    
    public resource: string;

SendTestMessageRequest resource.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.essentialcontacts.v1.ISendTestMessageRequest): google.cloud.essentialcontacts.v1.SendTestMessageRequest;

Creates a new SendTestMessageRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest)` | SendTestMessageRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.essentialcontacts.v1.SendTestMessageRequest;

Decodes a SendTestMessageRequest message from the specified reader or buffer.

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
`[SendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest)` | SendTestMessageRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.essentialcontacts.v1.SendTestMessageRequest;

Decodes a SendTestMessageRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest)` | SendTestMessageRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.essentialcontacts.v1.ISendTestMessageRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SendTestMessageRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
SendTestMessageRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.essentialcontacts.v1.ISendTestMessageRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SendTestMessageRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
SendTestMessageRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.essentialcontacts.v1.SendTestMessageRequest;

Creates a SendTestMessageRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest)` | SendTestMessageRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SendTestMessageRequest

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

Converts this SendTestMessageRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.essentialcontacts.v1.SendTestMessageRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SendTestMessageRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.sendtestmessagerequest)`   
SendTestMessageRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SendTestMessageRequest message.

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
