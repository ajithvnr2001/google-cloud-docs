---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class
title: Class protos.google.cloud.ces.v1.Agent (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:50.917532+00:00
---

# Class protos.google.cloud.ces.v1.Agent (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.Agent (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an Agent.

## Implements

[protos.google.cloud.ces.v1.IAgent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iagent)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IAgent);

Constructs a new Agent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iagent)`   
Properties to set  
  
## Properties 

### afterAgentCallbacks
    
    
    public afterAgentCallbacks: google.cloud.ces.v1.ICallback[];

Agent afterAgentCallbacks.

### afterModelCallbacks
    
    
    public afterModelCallbacks: google.cloud.ces.v1.ICallback[];

Agent afterModelCallbacks.

### afterToolCallbacks
    
    
    public afterToolCallbacks: google.cloud.ces.v1.ICallback[];

Agent afterToolCallbacks.

### agentType
    
    
    public agentType?: ("llmAgent"|"remoteDialogflowAgent");

Agent agentType.

### beforeAgentCallbacks
    
    
    public beforeAgentCallbacks: google.cloud.ces.v1.ICallback[];

Agent beforeAgentCallbacks.

### beforeModelCallbacks
    
    
    public beforeModelCallbacks: google.cloud.ces.v1.ICallback[];

Agent beforeModelCallbacks.

### beforeToolCallbacks
    
    
    public beforeToolCallbacks: google.cloud.ces.v1.ICallback[];

Agent beforeToolCallbacks.

### childAgents
    
    
    public childAgents: string[];

Agent childAgents.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Agent createTime.

### description
    
    
    public description: string;

Agent description.

### displayName
    
    
    public displayName: string;

Agent displayName.

### etag
    
    
    public etag: string;

Agent etag.

### generatedSummary
    
    
    public generatedSummary: string;

Agent generatedSummary.

### guardrails
    
    
    public guardrails: string[];

Agent guardrails.

### instruction
    
    
    public instruction: string;

Agent instruction.

### llmAgent
    
    
    public llmAgent?: (google.cloud.ces.v1.Agent.ILlmAgent|null);

Agent llmAgent.

### modelSettings
    
    
    public modelSettings?: (google.cloud.ces.v1.IModelSettings|null);

Agent modelSettings.

### name
    
    
    public name: string;

Agent name.

### remoteDialogflowAgent
    
    
    public remoteDialogflowAgent?: (google.cloud.ces.v1.Agent.IRemoteDialogflowAgent|null);

Agent remoteDialogflowAgent.

### tools
    
    
    public tools: string[];

Agent tools.

### toolsets
    
    
    public toolsets: google.cloud.ces.v1.Agent.IAgentToolset[];

Agent toolsets.

### transferRules
    
    
    public transferRules: google.cloud.ces.v1.ITransferRule[];

Agent transferRules.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Agent updateTime.

### validationErrors
    
    
    public validationErrors: string[];

Agent validationErrors.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IAgent): google.cloud.ces.v1.Agent;

Creates a new Agent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iagent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)` | Agent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.Agent;

Decodes an Agent message from the specified reader or buffer.

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
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)` | Agent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.Agent;

Decodes an Agent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)` | Agent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Agent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iagent)`   
Agent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Agent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iagent)`   
Agent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.Agent;

Creates an Agent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)` | Agent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Agent

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

Converts this Agent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.Agent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Agent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)`   
Agent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Agent message.

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
