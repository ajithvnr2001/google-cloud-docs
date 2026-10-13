---
url: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class
title: Class protos.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:18.423571+00:00
---

# Class protos.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.3  0.7.2  0.6.2  0.5.0  0.1.0 

Represents a ManagedCertificate.

## Implements

[protos.google.cloud.certificatemanager.v1.Certificate.IManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.imanagedcertificate)

## Package

[@google-cloud/certificate-manager](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.certificatemanager.v1.Certificate.IManagedCertificate);

Constructs a new ManagedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.imanagedcertificate)`   
Properties to set  
  
## Properties 

### authorizationAttemptInfo
    
    
    public authorizationAttemptInfo: google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.IAuthorizationAttemptInfo[];

ManagedCertificate authorizationAttemptInfo.

### dnsAuthorizations
    
    
    public dnsAuthorizations: string[];

ManagedCertificate dnsAuthorizations.

### domains
    
    
    public domains: string[];

ManagedCertificate domains.

### issuanceConfig
    
    
    public issuanceConfig: string;

ManagedCertificate issuanceConfig.

### provisioningIssue
    
    
    public provisioningIssue?: (google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.IProvisioningIssue|null);

ManagedCertificate provisioningIssue.

### state
    
    
    public state: (google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State|keyof typeof google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State);

ManagedCertificate state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.certificatemanager.v1.Certificate.IManagedCertificate): google.cloud.certificatemanager.v1.Certificate.ManagedCertificate;

Creates a new ManagedCertificate instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.imanagedcertificate)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class)` | ManagedCertificate instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.certificatemanager.v1.Certificate.ManagedCertificate;

Decodes a ManagedCertificate message from the specified reader or buffer.

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
`[ManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class)` | ManagedCertificate  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.certificatemanager.v1.Certificate.ManagedCertificate;

Decodes a ManagedCertificate message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class)` | ManagedCertificate  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.certificatemanager.v1.Certificate.IManagedCertificate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagedCertificate message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.imanagedcertificate)`   
ManagedCertificate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.certificatemanager.v1.Certificate.IManagedCertificate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagedCertificate message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.imanagedcertificate)`   
ManagedCertificate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.certificatemanager.v1.Certificate.ManagedCertificate;

Creates a ManagedCertificate message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class)` | ManagedCertificate  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ManagedCertificate

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

Converts this ManagedCertificate to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.certificatemanager.v1.Certificate.ManagedCertificate, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ManagedCertificate message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ManagedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate.managedcertificate-class)`   
ManagedCertificate  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ManagedCertificate message.

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
