---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate
title: Class protos.google.appengine.v1.AuthorizedCertificate (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:29.358694+00:00
---

# Class protos.google.appengine.v1.AuthorizedCertificate (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.AuthorizedCertificate (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents an AuthorizedCertificate.

## Implements

[protos.google.appengine.v1.IAuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iauthorizedcertificate)

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.appengine.v1.IAuthorizedCertificate);

Constructs a new AuthorizedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iauthorizedcertificate)`   
Properties to set  
  
## Properties 

### certificateRawData
    
    
    public certificateRawData?: (google.appengine.v1.ICertificateRawData|null);

AuthorizedCertificate certificateRawData.

### displayName
    
    
    public displayName: string;

AuthorizedCertificate displayName.

### domainMappingsCount
    
    
    public domainMappingsCount: number;

AuthorizedCertificate domainMappingsCount.

### domainNames
    
    
    public domainNames: string[];

AuthorizedCertificate domainNames.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

AuthorizedCertificate expireTime.

### id
    
    
    public id: string;

AuthorizedCertificate id.

### managedCertificate
    
    
    public managedCertificate?: (google.appengine.v1.IManagedCertificate|null);

AuthorizedCertificate managedCertificate.

### name
    
    
    public name: string;

AuthorizedCertificate name.

### visibleDomainMappings
    
    
    public visibleDomainMappings: string[];

AuthorizedCertificate visibleDomainMappings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.appengine.v1.IAuthorizedCertificate): google.appengine.v1.AuthorizedCertificate;

Creates a new AuthorizedCertificate instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iauthorizedcertificate)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)` | AuthorizedCertificate instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.appengine.v1.AuthorizedCertificate;

Decodes an AuthorizedCertificate message from the specified reader or buffer.

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
`[AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)` | AuthorizedCertificate  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.appengine.v1.AuthorizedCertificate;

Decodes an AuthorizedCertificate message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)` | AuthorizedCertificate  
  
### encode(message, writer)
    
    
    public static encode(message: google.appengine.v1.IAuthorizedCertificate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthorizedCertificate message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iauthorizedcertificate)`   
AuthorizedCertificate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.appengine.v1.IAuthorizedCertificate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthorizedCertificate message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iauthorizedcertificate)`   
AuthorizedCertificate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.appengine.v1.AuthorizedCertificate;

Creates an AuthorizedCertificate message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)` | AuthorizedCertificate  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AuthorizedCertificate

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

Converts this AuthorizedCertificate to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.appengine.v1.AuthorizedCertificate, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AuthorizedCertificate message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)`   
AuthorizedCertificate  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AuthorizedCertificate message.

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
