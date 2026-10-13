---
url: https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class
title: Class protos.google.cloud.domains.v1beta1.Registration (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:18.635544+00:00
---

# Class protos.google.cloud.domains.v1beta1.Registration (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.domains.v1beta1.Registration (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.1.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.8 

Represents a Registration.

## Implements

[protos.google.cloud.domains.v1beta1.IRegistration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.iregistration)

## Package

[@google-cloud/domains](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.domains.v1beta1.IRegistration);

Constructs a new Registration.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegistration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.iregistration)`   
Properties to set  
  
## Properties 

### contactSettings
    
    
    public contactSettings?: (google.cloud.domains.v1beta1.IContactSettings|null);

Registration contactSettings.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Registration createTime.

### dnsSettings
    
    
    public dnsSettings?: (google.cloud.domains.v1beta1.IDnsSettings|null);

Registration dnsSettings.

### domainName
    
    
    public domainName: string;

Registration domainName.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

Registration expireTime.

### issues
    
    
    public issues: google.cloud.domains.v1beta1.Registration.Issue[];

Registration issues.

### labels
    
    
    public labels: { [k: string]: string };

Registration labels.

### managementSettings
    
    
    public managementSettings?: (google.cloud.domains.v1beta1.IManagementSettings|null);

Registration managementSettings.

### name
    
    
    public name: string;

Registration name.

### pendingContactSettings
    
    
    public pendingContactSettings?: (google.cloud.domains.v1beta1.IContactSettings|null);

Registration pendingContactSettings.

### state
    
    
    public state: (google.cloud.domains.v1beta1.Registration.State|keyof typeof google.cloud.domains.v1beta1.Registration.State);

Registration state.

### supportedPrivacy
    
    
    public supportedPrivacy: google.cloud.domains.v1beta1.ContactPrivacy[];

Registration supportedPrivacy.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.domains.v1beta1.IRegistration): google.cloud.domains.v1beta1.Registration;

Creates a new Registration instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegistration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.iregistration)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class)` | Registration instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.domains.v1beta1.Registration;

Decodes a Registration message from the specified reader or buffer.

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
`[Registration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class)` | Registration  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.domains.v1beta1.Registration;

Decodes a Registration message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class)` | Registration  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.domains.v1beta1.IRegistration, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Registration message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegistration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.iregistration)`   
Registration message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.domains.v1beta1.IRegistration, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Registration message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegistration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.iregistration)`   
Registration message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.domains.v1beta1.Registration;

Creates a Registration message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Registration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class)` | Registration  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Registration

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

Converts this Registration to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.domains.v1beta1.Registration, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Registration message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Registration](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1beta1.registration-class)`   
Registration  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Registration message.

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
