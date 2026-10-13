---
url: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class
title: Class protos.google.cloud.functions.v2beta.ServiceConfig (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:46.713208+00:00
---

# Class protos.google.cloud.functions.v2beta.ServiceConfig (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.functions.v2beta.ServiceConfig (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.6.0  3.3.0  3.1.0  2.4.1  2.3.1  2.2.3  1.2.0  1.1.9 

Represents a ServiceConfig.

## Implements

[protos.google.cloud.functions.v2beta.IServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.iserviceconfig)

## Package

[@google-cloud/functions](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.functions.v2beta.IServiceConfig);

Constructs a new ServiceConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.iserviceconfig)`   
Properties to set  
  
## Properties 

### allTrafficOnLatestRevision
    
    
    public allTrafficOnLatestRevision: boolean;

ServiceConfig allTrafficOnLatestRevision.

### availableCpu
    
    
    public availableCpu: string;

ServiceConfig availableCpu.

### availableMemory
    
    
    public availableMemory: string;

ServiceConfig availableMemory.

### binaryAuthorizationPolicy
    
    
    public binaryAuthorizationPolicy: string;

ServiceConfig binaryAuthorizationPolicy.

### environmentVariables
    
    
    public environmentVariables: { [k: string]: string };

ServiceConfig environmentVariables.

### ingressSettings
    
    
    public ingressSettings: (google.cloud.functions.v2beta.ServiceConfig.IngressSettings|keyof typeof google.cloud.functions.v2beta.ServiceConfig.IngressSettings);

ServiceConfig ingressSettings.

### maxInstanceCount
    
    
    public maxInstanceCount: number;

ServiceConfig maxInstanceCount.

### maxInstanceRequestConcurrency
    
    
    public maxInstanceRequestConcurrency: number;

ServiceConfig maxInstanceRequestConcurrency.

### minInstanceCount
    
    
    public minInstanceCount: number;

ServiceConfig minInstanceCount.

### revision
    
    
    public revision: string;

ServiceConfig revision.

### secretEnvironmentVariables
    
    
    public secretEnvironmentVariables: google.cloud.functions.v2beta.ISecretEnvVar[];

ServiceConfig secretEnvironmentVariables.

### secretVolumes
    
    
    public secretVolumes: google.cloud.functions.v2beta.ISecretVolume[];

ServiceConfig secretVolumes.

### securityLevel
    
    
    public securityLevel: (google.cloud.functions.v2beta.ServiceConfig.SecurityLevel|keyof typeof google.cloud.functions.v2beta.ServiceConfig.SecurityLevel);

ServiceConfig securityLevel.

### service
    
    
    public service: string;

ServiceConfig service.

### serviceAccountEmail
    
    
    public serviceAccountEmail: string;

ServiceConfig serviceAccountEmail.

### timeoutSeconds
    
    
    public timeoutSeconds: number;

ServiceConfig timeoutSeconds.

### uri
    
    
    public uri: string;

ServiceConfig uri.

### vpcConnector
    
    
    public vpcConnector: string;

ServiceConfig vpcConnector.

### vpcConnectorEgressSettings
    
    
    public vpcConnectorEgressSettings: (google.cloud.functions.v2beta.ServiceConfig.VpcConnectorEgressSettings|keyof typeof google.cloud.functions.v2beta.ServiceConfig.VpcConnectorEgressSettings);

ServiceConfig vpcConnectorEgressSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.functions.v2beta.IServiceConfig): google.cloud.functions.v2beta.ServiceConfig;

Creates a new ServiceConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.iserviceconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class)` | ServiceConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.functions.v2beta.ServiceConfig;

Decodes a ServiceConfig message from the specified reader or buffer.

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
`[ServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class)` | ServiceConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.functions.v2beta.ServiceConfig;

Decodes a ServiceConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class)` | ServiceConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.functions.v2beta.IServiceConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ServiceConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.iserviceconfig)`   
ServiceConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.functions.v2beta.IServiceConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ServiceConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.iserviceconfig)`   
ServiceConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.functions.v2beta.ServiceConfig;

Creates a ServiceConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class)` | ServiceConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ServiceConfig

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

Converts this ServiceConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.functions.v2beta.ServiceConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ServiceConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ServiceConfig](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2beta.serviceconfig-class)`   
ServiceConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ServiceConfig message.

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
