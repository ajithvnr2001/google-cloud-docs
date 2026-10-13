---
url: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate
title: Class protos.google.cloud.run.v2.RevisionTemplate (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:59.513878+00:00
---

# Class protos.google.cloud.run.v2.RevisionTemplate (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.run.v2.RevisionTemplate (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.3.0  3.2.0  2.1.0  1.5.0  1.0.2  0.5.0  0.4.2  0.2.3 

Represents a RevisionTemplate.

## Implements

[protos.google.cloud.run.v2.IRevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.irevisiontemplate)

## Package

[@google-cloud/run](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.run.v2.IRevisionTemplate);

Constructs a new RevisionTemplate.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.irevisiontemplate)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

RevisionTemplate annotations.

### containers
    
    
    public containers: google.cloud.run.v2.IContainer[];

RevisionTemplate containers.

### encryptionKey
    
    
    public encryptionKey: string;

RevisionTemplate encryptionKey.

### encryptionKeyRevocationAction
    
    
    public encryptionKeyRevocationAction: (google.cloud.run.v2.EncryptionKeyRevocationAction|keyof typeof google.cloud.run.v2.EncryptionKeyRevocationAction);

RevisionTemplate encryptionKeyRevocationAction.

### encryptionKeyShutdownDuration
    
    
    public encryptionKeyShutdownDuration?: (google.protobuf.IDuration|null);

RevisionTemplate encryptionKeyShutdownDuration.

### executionEnvironment
    
    
    public executionEnvironment: (google.cloud.run.v2.ExecutionEnvironment|keyof typeof google.cloud.run.v2.ExecutionEnvironment);

RevisionTemplate executionEnvironment.

### gpuZonalRedundancyDisabled
    
    
    public gpuZonalRedundancyDisabled?: (boolean|null);

RevisionTemplate gpuZonalRedundancyDisabled.

### healthCheckDisabled
    
    
    public healthCheckDisabled: boolean;

RevisionTemplate healthCheckDisabled.

### labels
    
    
    public labels: { [k: string]: string };

RevisionTemplate labels.

### maxInstanceRequestConcurrency
    
    
    public maxInstanceRequestConcurrency: number;

RevisionTemplate maxInstanceRequestConcurrency.

### nodeSelector
    
    
    public nodeSelector?: (google.cloud.run.v2.INodeSelector|null);

RevisionTemplate nodeSelector.

### revision
    
    
    public revision: string;

RevisionTemplate revision.

### scaling
    
    
    public scaling?: (google.cloud.run.v2.IRevisionScaling|null);

RevisionTemplate scaling.

### serviceAccount
    
    
    public serviceAccount: string;

RevisionTemplate serviceAccount.

### serviceMesh
    
    
    public serviceMesh?: (google.cloud.run.v2.IServiceMesh|null);

RevisionTemplate serviceMesh.

### sessionAffinity
    
    
    public sessionAffinity: boolean;

RevisionTemplate sessionAffinity.

### timeout
    
    
    public timeout?: (google.protobuf.IDuration|null);

RevisionTemplate timeout.

### volumes
    
    
    public volumes: google.cloud.run.v2.IVolume[];

RevisionTemplate volumes.

### vpcAccess
    
    
    public vpcAccess?: (google.cloud.run.v2.IVpcAccess|null);

RevisionTemplate vpcAccess.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.run.v2.IRevisionTemplate): google.cloud.run.v2.RevisionTemplate;

Creates a new RevisionTemplate instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.irevisiontemplate)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate)` | RevisionTemplate instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.run.v2.RevisionTemplate;

Decodes a RevisionTemplate message from the specified reader or buffer.

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
`[RevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate)` | RevisionTemplate  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.run.v2.RevisionTemplate;

Decodes a RevisionTemplate message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate)` | RevisionTemplate  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.run.v2.IRevisionTemplate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RevisionTemplate message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.irevisiontemplate)`   
RevisionTemplate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.run.v2.IRevisionTemplate, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RevisionTemplate message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.irevisiontemplate)`   
RevisionTemplate message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.run.v2.RevisionTemplate;

Creates a RevisionTemplate message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate)` | RevisionTemplate  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RevisionTemplate

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

Converts this RevisionTemplate to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.run.v2.RevisionTemplate, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RevisionTemplate message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RevisionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.revisiontemplate)`   
RevisionTemplate  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RevisionTemplate message.

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
