---
url: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict
title: Class protos.google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:20.537144+00:00
---

# Class protos.google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  6.2.0  6.0.1  5.13.0  5.11.0  5.10.0  5.8.0  5.5.0  5.4.0  5.2.0  5.1.1  5.0.0  4.1.0  3.4.1  3.3.1  3.1.1  3.0.4  2.5.0  2.4.0  2.3.0  2.2.1  2.1.7 

Represents an AccountTakeoverVerdict.

## Implements

[protos.google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.iaccounttakeoververdict)

## Package

[@google-cloud/recaptcha-enterprise](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTakeoverVerdict);

Constructs a new AccountTakeoverVerdict.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.iaccounttakeoververdict)`   
Properties to set  
  
## Properties 

### risk
    
    
    public risk: number;

AccountTakeoverVerdict risk.

### riskReasons
    
    
    public riskReasons: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountRiskReason[];

AccountTakeoverVerdict riskReasons.

### trustReasons
    
    
    public trustReasons: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTrustReason[];

AccountTakeoverVerdict trustReasons.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTakeoverVerdict): google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict;

Creates a new AccountTakeoverVerdict instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.iaccounttakeoververdict)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict)` | AccountTakeoverVerdict instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict;

Decodes an AccountTakeoverVerdict message from the specified reader or buffer.

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
`[AccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict)` | AccountTakeoverVerdict  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict;

Decodes an AccountTakeoverVerdict message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict)` | AccountTakeoverVerdict  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTakeoverVerdict, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccountTakeoverVerdict message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.iaccounttakeoververdict)`   
AccountTakeoverVerdict message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.IAccountTakeoverVerdict, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccountTakeoverVerdict message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.iaccounttakeoververdict)`   
AccountTakeoverVerdict message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict;

Creates an AccountTakeoverVerdict message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict)` | AccountTakeoverVerdict  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AccountTakeoverVerdict

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

Converts this AccountTakeoverVerdict to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.recaptchaenterprise.v1.AccountDefenderAssessment.AccountTakeoverVerdict, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AccountTakeoverVerdict message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AccountTakeoverVerdict](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1.accountdefenderassessment.accounttakeoververdict)`   
AccountTakeoverVerdict  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AccountTakeoverVerdict message.

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
