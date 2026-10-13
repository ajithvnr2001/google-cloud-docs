---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class
title: Class protos.google.cloud.kms.v1.SingleTenantHsmInstanceProposal (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:15.041662+00:00
---

# Class protos.google.cloud.kms.v1.SingleTenantHsmInstanceProposal (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.SingleTenantHsmInstanceProposal (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents a SingleTenantHsmInstanceProposal.

## Implements

[protos.google.cloud.kms.v1.ISingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.isingletenanthsminstanceproposal)

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.kms.v1.ISingleTenantHsmInstanceProposal);

Constructs a new SingleTenantHsmInstanceProposal.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.isingletenanthsminstanceproposal)`   
Properties to set  
  
## Properties 

### addQuorumMember
    
    
    public addQuorumMember?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IAddQuorumMember|null);

SingleTenantHsmInstanceProposal addQuorumMember.

### approvalParameters
    
    
    public approvalParameters?: ("quorumParameters"|"requiredActionQuorumParameters");

SingleTenantHsmInstanceProposal approvalParameters.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

SingleTenantHsmInstanceProposal createTime.

### deleteSingleTenantHsmInstance
    
    
    public deleteSingleTenantHsmInstance?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IDeleteSingleTenantHsmInstance|null);

SingleTenantHsmInstanceProposal deleteSingleTenantHsmInstance.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

SingleTenantHsmInstanceProposal deleteTime.

### disableSingleTenantHsmInstance
    
    
    public disableSingleTenantHsmInstance?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IDisableSingleTenantHsmInstance|null);

SingleTenantHsmInstanceProposal disableSingleTenantHsmInstance.

### enableSingleTenantHsmInstance
    
    
    public enableSingleTenantHsmInstance?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IEnableSingleTenantHsmInstance|null);

SingleTenantHsmInstanceProposal enableSingleTenantHsmInstance.

### expiration
    
    
    public expiration?: ("expireTime"|"ttl");

SingleTenantHsmInstanceProposal expiration.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

SingleTenantHsmInstanceProposal expireTime.

### failureReason
    
    
    public failureReason: string;

SingleTenantHsmInstanceProposal failureReason.

### name
    
    
    public name: string;

SingleTenantHsmInstanceProposal name.

### operation
    
    
    public operation?: ("registerTwoFactorAuthKeys"|"disableSingleTenantHsmInstance"|"enableSingleTenantHsmInstance"|"deleteSingleTenantHsmInstance"|"addQuorumMember"|"removeQuorumMember"|"refreshSingleTenantHsmInstance"|"upgradeKeyTrust");

SingleTenantHsmInstanceProposal operation.

### purgeTime
    
    
    public purgeTime?: (google.protobuf.ITimestamp|null);

SingleTenantHsmInstanceProposal purgeTime.

### quorumParameters
    
    
    public quorumParameters?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IQuorumParameters|null);

SingleTenantHsmInstanceProposal quorumParameters.

### refreshSingleTenantHsmInstance
    
    
    public refreshSingleTenantHsmInstance?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IRefreshSingleTenantHsmInstance|null);

SingleTenantHsmInstanceProposal refreshSingleTenantHsmInstance.

### registerTwoFactorAuthKeys
    
    
    public registerTwoFactorAuthKeys?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IRegisterTwoFactorAuthKeys|null);

SingleTenantHsmInstanceProposal registerTwoFactorAuthKeys.

### removeQuorumMember
    
    
    public removeQuorumMember?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IRemoveQuorumMember|null);

SingleTenantHsmInstanceProposal removeQuorumMember.

### requiredActionQuorumParameters
    
    
    public requiredActionQuorumParameters?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IRequiredActionQuorumParameters|null);

SingleTenantHsmInstanceProposal requiredActionQuorumParameters.

### state
    
    
    public state: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.State|keyof typeof google.cloud.kms.v1.SingleTenantHsmInstanceProposal.State);

SingleTenantHsmInstanceProposal state.

### ttl
    
    
    public ttl?: (google.protobuf.IDuration|null);

SingleTenantHsmInstanceProposal ttl.

### upgradeKeyTrust
    
    
    public upgradeKeyTrust?: (google.cloud.kms.v1.SingleTenantHsmInstanceProposal.IUpgradeKeyTrust|null);

SingleTenantHsmInstanceProposal upgradeKeyTrust.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.kms.v1.ISingleTenantHsmInstanceProposal): google.cloud.kms.v1.SingleTenantHsmInstanceProposal;

Creates a new SingleTenantHsmInstanceProposal instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.isingletenanthsminstanceproposal)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)` | SingleTenantHsmInstanceProposal instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.kms.v1.SingleTenantHsmInstanceProposal;

Decodes a SingleTenantHsmInstanceProposal message from the specified reader or buffer.

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
`[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)` | SingleTenantHsmInstanceProposal  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.kms.v1.SingleTenantHsmInstanceProposal;

Decodes a SingleTenantHsmInstanceProposal message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)` | SingleTenantHsmInstanceProposal  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.kms.v1.ISingleTenantHsmInstanceProposal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SingleTenantHsmInstanceProposal message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.isingletenanthsminstanceproposal)`   
SingleTenantHsmInstanceProposal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.kms.v1.ISingleTenantHsmInstanceProposal, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SingleTenantHsmInstanceProposal message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.isingletenanthsminstanceproposal)`   
SingleTenantHsmInstanceProposal message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.kms.v1.SingleTenantHsmInstanceProposal;

Creates a SingleTenantHsmInstanceProposal message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)` | SingleTenantHsmInstanceProposal  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SingleTenantHsmInstanceProposal

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

Converts this SingleTenantHsmInstanceProposal to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.kms.v1.SingleTenantHsmInstanceProposal, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SingleTenantHsmInstanceProposal message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.singletenanthsminstanceproposal-class)`   
SingleTenantHsmInstanceProposal  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SingleTenantHsmInstanceProposal message.

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
