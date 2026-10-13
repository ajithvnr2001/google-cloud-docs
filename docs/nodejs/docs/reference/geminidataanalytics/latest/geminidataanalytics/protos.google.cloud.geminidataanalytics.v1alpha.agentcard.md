---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard
title: Class protos.google.cloud.geminidataanalytics.v1alpha.AgentCard (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:52.451617+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1alpha.AgentCard (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1alpha.AgentCard (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents an AgentCard.

## Implements

[protos.google.cloud.geminidataanalytics.v1alpha.IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.iagentcard)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1alpha.IAgentCard);

Constructs a new AgentCard.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.iagentcard)`   
Properties to set  
  
## Properties 

### additionalInterfaces
    
    
    public additionalInterfaces: google.cloud.geminidataanalytics.v1alpha.IAgentInterface[];

AgentCard additionalInterfaces.

### capabilities
    
    
    public capabilities?: (google.cloud.geminidataanalytics.v1alpha.IAgentCapabilities|null);

AgentCard capabilities.

### defaultInputModes
    
    
    public defaultInputModes: string[];

AgentCard defaultInputModes.

### defaultOutputModes
    
    
    public defaultOutputModes: string[];

AgentCard defaultOutputModes.

### description
    
    
    public description: string;

AgentCard description.

### documentationUrl
    
    
    public documentationUrl: string;

AgentCard documentationUrl.

### iconUrl
    
    
    public iconUrl: string;

AgentCard iconUrl.

### name
    
    
    public name: string;

AgentCard name.

### preferredTransport
    
    
    public preferredTransport: string;

AgentCard preferredTransport.

### protocolVersion
    
    
    public protocolVersion: string;

AgentCard protocolVersion.

### provider
    
    
    public provider?: (google.cloud.geminidataanalytics.v1alpha.IAgentProvider|null);

AgentCard provider.

### security
    
    
    public security: google.cloud.geminidataanalytics.v1alpha.ISecurity[];

AgentCard security.

### securitySchemes
    
    
    public securitySchemes: { [k: string]: google.cloud.geminidataanalytics.v1alpha.ISecurityScheme };

AgentCard securitySchemes.

### signatures
    
    
    public signatures: google.cloud.geminidataanalytics.v1alpha.IAgentCardSignature[];

AgentCard signatures.

### skills
    
    
    public skills: google.cloud.geminidataanalytics.v1alpha.IAgentSkill[];

AgentCard skills.

### supportsAuthenticatedExtendedCard
    
    
    public supportsAuthenticatedExtendedCard: boolean;

AgentCard supportsAuthenticatedExtendedCard.

### url
    
    
    public url: string;

AgentCard url.

### version
    
    
    public version: string;

AgentCard version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1alpha.IAgentCard): google.cloud.geminidataanalytics.v1alpha.AgentCard;

Creates a new AgentCard instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.iagentcard)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard)` | AgentCard instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1alpha.AgentCard;

Decodes an AgentCard message from the specified reader or buffer.

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
`[AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard)` | AgentCard  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1alpha.AgentCard;

Decodes an AgentCard message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard)` | AgentCard  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1alpha.IAgentCard, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AgentCard message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.iagentcard)`   
AgentCard message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1alpha.IAgentCard, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AgentCard message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.iagentcard)`   
AgentCard message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1alpha.AgentCard;

Creates an AgentCard message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard)` | AgentCard  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AgentCard

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

Converts this AgentCard to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1alpha.AgentCard, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AgentCard message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.agentcard)`   
AgentCard  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AgentCard message.

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
