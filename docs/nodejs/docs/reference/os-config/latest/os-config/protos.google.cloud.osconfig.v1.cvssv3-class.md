---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class
title: Class protos.google.cloud.osconfig.v1.CVSSv3 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:30.643953+00:00
---

# Class protos.google.cloud.osconfig.v1.CVSSv3 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.osconfig.v1.CVSSv3 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

Represents a CVSSv3.

## Implements

[protos.google.cloud.osconfig.v1.ICVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.icvssv3)

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.osconfig.v1.ICVSSv3);

Constructs a new CVSSv3.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.icvssv3)`   
Properties to set  
  
## Properties 

### attackComplexity
    
    
    public attackComplexity: (google.cloud.osconfig.v1.CVSSv3.AttackComplexity|keyof typeof google.cloud.osconfig.v1.CVSSv3.AttackComplexity);

CVSSv3 attackComplexity.

### attackVector
    
    
    public attackVector: (google.cloud.osconfig.v1.CVSSv3.AttackVector|keyof typeof google.cloud.osconfig.v1.CVSSv3.AttackVector);

CVSSv3 attackVector.

### availabilityImpact
    
    
    public availabilityImpact: (google.cloud.osconfig.v1.CVSSv3.Impact|keyof typeof google.cloud.osconfig.v1.CVSSv3.Impact);

CVSSv3 availabilityImpact.

### baseScore
    
    
    public baseScore: number;

CVSSv3 baseScore.

### confidentialityImpact
    
    
    public confidentialityImpact: (google.cloud.osconfig.v1.CVSSv3.Impact|keyof typeof google.cloud.osconfig.v1.CVSSv3.Impact);

CVSSv3 confidentialityImpact.

### exploitabilityScore
    
    
    public exploitabilityScore: number;

CVSSv3 exploitabilityScore.

### impactScore
    
    
    public impactScore: number;

CVSSv3 impactScore.

### integrityImpact
    
    
    public integrityImpact: (google.cloud.osconfig.v1.CVSSv3.Impact|keyof typeof google.cloud.osconfig.v1.CVSSv3.Impact);

CVSSv3 integrityImpact.

### privilegesRequired
    
    
    public privilegesRequired: (google.cloud.osconfig.v1.CVSSv3.PrivilegesRequired|keyof typeof google.cloud.osconfig.v1.CVSSv3.PrivilegesRequired);

CVSSv3 privilegesRequired.

### scope
    
    
    public scope: (google.cloud.osconfig.v1.CVSSv3.Scope|keyof typeof google.cloud.osconfig.v1.CVSSv3.Scope);

CVSSv3 scope.

### userInteraction
    
    
    public userInteraction: (google.cloud.osconfig.v1.CVSSv3.UserInteraction|keyof typeof google.cloud.osconfig.v1.CVSSv3.UserInteraction);

CVSSv3 userInteraction.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.osconfig.v1.ICVSSv3): google.cloud.osconfig.v1.CVSSv3;

Creates a new CVSSv3 instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.icvssv3)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class)` | CVSSv3 instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.osconfig.v1.CVSSv3;

Decodes a CVSSv3 message from the specified reader or buffer.

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
`[CVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class)` | CVSSv3  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.osconfig.v1.CVSSv3;

Decodes a CVSSv3 message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class)` | CVSSv3  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.osconfig.v1.ICVSSv3, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CVSSv3 message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.icvssv3)`   
CVSSv3 message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.osconfig.v1.ICVSSv3, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CVSSv3 message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.icvssv3)`   
CVSSv3 message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.osconfig.v1.CVSSv3;

Creates a CVSSv3 message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class)` | CVSSv3  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CVSSv3

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

Converts this CVSSv3 to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.osconfig.v1.CVSSv3, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CVSSv3 message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CVSSv3](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.cvssv3-class)`   
CVSSv3  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CVSSv3 message.

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
