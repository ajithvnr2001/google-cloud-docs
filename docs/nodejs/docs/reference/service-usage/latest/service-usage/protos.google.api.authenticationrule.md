---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule
title: Class protos.google.api.AuthenticationRule (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:11.552656+00:00
---

# Class protos.google.api.AuthenticationRule (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.AuthenticationRule (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.3.0  2.2.2  2.1.2  1.2.1  1.1.4 

Represents an AuthenticationRule.

## Implements

[protos.google.api.IAuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthenticationrule)

## Package

[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IAuthenticationRule);

Constructs a new AuthenticationRule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthenticationrule)`   
Properties to set  
  
## Properties 

### allowWithoutCredential
    
    
    public allowWithoutCredential: boolean;

AuthenticationRule allowWithoutCredential.

### oauth
    
    
    public oauth?: (google.api.IOAuthRequirements|null);

AuthenticationRule oauth.

### requirements
    
    
    public requirements: google.api.IAuthRequirement[];

AuthenticationRule requirements.

### selector
    
    
    public selector: string;

AuthenticationRule selector.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IAuthenticationRule): google.api.AuthenticationRule;

Creates a new AuthenticationRule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthenticationrule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule)` | AuthenticationRule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.AuthenticationRule;

Decodes an AuthenticationRule message from the specified reader or buffer.

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
`[AuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule)` | AuthenticationRule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.AuthenticationRule;

Decodes an AuthenticationRule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule)` | AuthenticationRule  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IAuthenticationRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthenticationRule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthenticationrule)`   
AuthenticationRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IAuthenticationRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthenticationRule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthenticationrule)`   
AuthenticationRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.AuthenticationRule;

Creates an AuthenticationRule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule)` | AuthenticationRule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AuthenticationRule

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

Converts this AuthenticationRule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.AuthenticationRule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AuthenticationRule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AuthenticationRule](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authenticationrule)`   
AuthenticationRule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AuthenticationRule message.

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
