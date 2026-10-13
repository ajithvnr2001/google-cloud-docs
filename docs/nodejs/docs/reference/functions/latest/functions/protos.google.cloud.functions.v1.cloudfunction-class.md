---
url: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class
title: Class protos.google.cloud.functions.v1.CloudFunction (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:29.878547+00:00
---

# Class protos.google.cloud.functions.v1.CloudFunction (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.functions.v1.CloudFunction (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.6.0  3.3.0  3.1.0  2.4.1  2.3.1  2.2.3  1.2.0  1.1.9 

Represents a CloudFunction.

## Implements

[protos.google.cloud.functions.v1.ICloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.icloudfunction)

## Package

[@google-cloud/functions](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.functions.v1.ICloudFunction);

Constructs a new CloudFunction.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.icloudfunction)`   
Properties to set  
  
## Properties 

### automaticUpdatePolicy
    
    
    public automaticUpdatePolicy?: (google.cloud.functions.v1.CloudFunction.IAutomaticUpdatePolicy|null);

CloudFunction automaticUpdatePolicy.

### availableMemoryMb
    
    
    public availableMemoryMb: number;

CloudFunction availableMemoryMb.

### buildEnvironmentVariables
    
    
    public buildEnvironmentVariables: { [k: string]: string };

CloudFunction buildEnvironmentVariables.

### buildId
    
    
    public buildId: string;

CloudFunction buildId.

### buildName
    
    
    public buildName: string;

CloudFunction buildName.

### buildServiceAccount
    
    
    public buildServiceAccount: string;

CloudFunction buildServiceAccount.

### buildWorkerPool
    
    
    public buildWorkerPool: string;

CloudFunction buildWorkerPool.

### description
    
    
    public description: string;

CloudFunction description.

### dockerRegistry
    
    
    public dockerRegistry: (google.cloud.functions.v1.CloudFunction.DockerRegistry|keyof typeof google.cloud.functions.v1.CloudFunction.DockerRegistry);

CloudFunction dockerRegistry.

### dockerRepository
    
    
    public dockerRepository: string;

CloudFunction dockerRepository.

### entryPoint
    
    
    public entryPoint: string;

CloudFunction entryPoint.

### environmentVariables
    
    
    public environmentVariables: { [k: string]: string };

CloudFunction environmentVariables.

### eventTrigger
    
    
    public eventTrigger?: (google.cloud.functions.v1.IEventTrigger|null);

CloudFunction eventTrigger.

### httpsTrigger
    
    
    public httpsTrigger?: (google.cloud.functions.v1.IHttpsTrigger|null);

CloudFunction httpsTrigger.

### ingressSettings
    
    
    public ingressSettings: (google.cloud.functions.v1.CloudFunction.IngressSettings|keyof typeof google.cloud.functions.v1.CloudFunction.IngressSettings);

CloudFunction ingressSettings.

### kmsKeyName
    
    
    public kmsKeyName: string;

CloudFunction kmsKeyName.

### labels
    
    
    public labels: { [k: string]: string };

CloudFunction labels.

### maxInstances
    
    
    public maxInstances: number;

CloudFunction maxInstances.

### minInstances
    
    
    public minInstances: number;

CloudFunction minInstances.

### name
    
    
    public name: string;

CloudFunction name.

### network
    
    
    public network: string;

CloudFunction network.

### onDeployUpdatePolicy
    
    
    public onDeployUpdatePolicy?: (google.cloud.functions.v1.CloudFunction.IOnDeployUpdatePolicy|null);

CloudFunction onDeployUpdatePolicy.

### runtime
    
    
    public runtime: string;

CloudFunction runtime.

### runtimeUpdatePolicy
    
    
    public runtimeUpdatePolicy?: ("automaticUpdatePolicy"|"onDeployUpdatePolicy");

CloudFunction runtimeUpdatePolicy.

### secretEnvironmentVariables
    
    
    public secretEnvironmentVariables: google.cloud.functions.v1.ISecretEnvVar[];

CloudFunction secretEnvironmentVariables.

### secretVolumes
    
    
    public secretVolumes: google.cloud.functions.v1.ISecretVolume[];

CloudFunction secretVolumes.

### serviceAccountEmail
    
    
    public serviceAccountEmail: string;

CloudFunction serviceAccountEmail.

### sourceArchiveUrl
    
    
    public sourceArchiveUrl?: (string|null);

CloudFunction sourceArchiveUrl.

### sourceCode
    
    
    public sourceCode?: ("sourceArchiveUrl"|"sourceRepository"|"sourceUploadUrl");

CloudFunction sourceCode.

### sourceRepository
    
    
    public sourceRepository?: (google.cloud.functions.v1.ISourceRepository|null);

CloudFunction sourceRepository.

### sourceToken
    
    
    public sourceToken: string;

CloudFunction sourceToken.

### sourceUploadUrl
    
    
    public sourceUploadUrl?: (string|null);

CloudFunction sourceUploadUrl.

### status
    
    
    public status: (google.cloud.functions.v1.CloudFunctionStatus|keyof typeof google.cloud.functions.v1.CloudFunctionStatus);

CloudFunction status.

### timeout
    
    
    public timeout?: (google.protobuf.IDuration|null);

CloudFunction timeout.

### trigger
    
    
    public trigger?: ("httpsTrigger"|"eventTrigger");

CloudFunction trigger.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

CloudFunction updateTime.

### versionId
    
    
    public versionId: (number|Long|string);

CloudFunction versionId.

### vpcConnector
    
    
    public vpcConnector: string;

CloudFunction vpcConnector.

### vpcConnectorEgressSettings
    
    
    public vpcConnectorEgressSettings: (google.cloud.functions.v1.CloudFunction.VpcConnectorEgressSettings|keyof typeof google.cloud.functions.v1.CloudFunction.VpcConnectorEgressSettings);

CloudFunction vpcConnectorEgressSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.functions.v1.ICloudFunction): google.cloud.functions.v1.CloudFunction;

Creates a new CloudFunction instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.icloudfunction)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class)` | CloudFunction instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.functions.v1.CloudFunction;

Decodes a CloudFunction message from the specified reader or buffer.

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
`[CloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class)` | CloudFunction  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.functions.v1.CloudFunction;

Decodes a CloudFunction message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class)` | CloudFunction  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.functions.v1.ICloudFunction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudFunction message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.icloudfunction)`   
CloudFunction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.functions.v1.ICloudFunction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudFunction message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.icloudfunction)`   
CloudFunction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.functions.v1.CloudFunction;

Creates a CloudFunction message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class)` | CloudFunction  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CloudFunction

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

Converts this CloudFunction to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.functions.v1.CloudFunction, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CloudFunction message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CloudFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v1.cloudfunction-class)`   
CloudFunction  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CloudFunction message.

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
