---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class
title: Class protos.google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:43.585422+00:00
---

# Class protos.google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

Represents a Principal.

## Implements

[protos.google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IPrincipal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.iprincipal)

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IPrincipal);

Constructs a new Principal.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPrincipal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.iprincipal)`   
Properties to set  
  
## Properties 

### principal
    
    
    public principal?: (google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IStringMatch|null);

Principal principal.

### principalSelector
    
    
    public principalSelector: (google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal.PrincipalSelector|keyof typeof google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal.PrincipalSelector);

Principal principalSelector.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IPrincipal): google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal;

Creates a new Principal instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPrincipal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.iprincipal)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Principal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class)` | Principal instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal;

Decodes a Principal message from the specified reader or buffer.

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
`[Principal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class)` | Principal  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal;

Decodes a Principal message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Principal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class)` | Principal  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IPrincipal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Principal message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPrincipal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.iprincipal)`   
Principal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.IPrincipal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Principal message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPrincipal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.iprincipal)`   
Principal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal;

Creates a Principal message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Principal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class)` | Principal  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Principal

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

Converts this Principal to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networksecurity.v1alpha1.AuthzPolicy.AuthzRule.Principal, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Principal message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Principal](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.authzpolicy.authzrule.principal-class)`   
Principal  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Principal message.

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
