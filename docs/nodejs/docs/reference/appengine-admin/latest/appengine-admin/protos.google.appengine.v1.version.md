---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version
title: Class protos.google.appengine.v1.Version (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:35.093502+00:00
---

# Class protos.google.appengine.v1.Version (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.Version (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a Version.

## Implements

[protos.google.appengine.v1.IVersion](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iversion)

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.appengine.v1.IVersion);

Constructs a new Version.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iversion)`   
Properties to set  
  
## Properties 

### apiConfig
    
    
    public apiConfig?: (google.appengine.v1.IApiConfigHandler|null);

Version apiConfig.

### appEngineApis
    
    
    public appEngineApis: boolean;

Version appEngineApis.

### automaticScaling
    
    
    public automaticScaling?: (google.appengine.v1.IAutomaticScaling|null);

Version automaticScaling.

### basicScaling
    
    
    public basicScaling?: (google.appengine.v1.IBasicScaling|null);

Version basicScaling.

### betaSettings
    
    
    public betaSettings: { [k: string]: string };

Version betaSettings.

### buildEnvVariables
    
    
    public buildEnvVariables: { [k: string]: string };

Version buildEnvVariables.

### createdBy
    
    
    public createdBy: string;

Version createdBy.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Version createTime.

### defaultExpiration
    
    
    public defaultExpiration?: (google.protobuf.IDuration|null);

Version defaultExpiration.

### deployment
    
    
    public deployment?: (google.appengine.v1.IDeployment|null);

Version deployment.

### diskUsageBytes
    
    
    public diskUsageBytes: (number|Long|string);

Version diskUsageBytes.

### endpointsApiService
    
    
    public endpointsApiService?: (google.appengine.v1.IEndpointsApiService|null);

Version endpointsApiService.

### entrypoint
    
    
    public entrypoint?: (google.appengine.v1.IEntrypoint|null);

Version entrypoint.

### env
    
    
    public env: string;

Version env.

### envVariables
    
    
    public envVariables: { [k: string]: string };

Version envVariables.

### errorHandlers
    
    
    public errorHandlers: google.appengine.v1.IErrorHandler[];

Version errorHandlers.

### handlers
    
    
    public handlers: google.appengine.v1.IUrlMap[];

Version handlers.

### healthCheck
    
    
    public healthCheck?: (google.appengine.v1.IHealthCheck|null);

Version healthCheck.

### id
    
    
    public id: string;

Version id.

### inboundServices
    
    
    public inboundServices: google.appengine.v1.InboundServiceType[];

Version inboundServices.

### instanceClass
    
    
    public instanceClass: string;

Version instanceClass.

### libraries
    
    
    public libraries: google.appengine.v1.ILibrary[];

Version libraries.

### livenessCheck
    
    
    public livenessCheck?: (google.appengine.v1.ILivenessCheck|null);

Version livenessCheck.

### manualScaling
    
    
    public manualScaling?: (google.appengine.v1.IManualScaling|null);

Version manualScaling.

### name
    
    
    public name: string;

Version name.

### network
    
    
    public network?: (google.appengine.v1.INetwork|null);

Version network.

### nobuildFilesRegex
    
    
    public nobuildFilesRegex: string;

Version nobuildFilesRegex.

### readinessCheck
    
    
    public readinessCheck?: (google.appengine.v1.IReadinessCheck|null);

Version readinessCheck.

### resources
    
    
    public resources?: (google.appengine.v1.IResources|null);

Version resources.

### runtime
    
    
    public runtime: string;

Version runtime.

### runtimeApiVersion
    
    
    public runtimeApiVersion: string;

Version runtimeApiVersion.

### runtimeChannel
    
    
    public runtimeChannel: string;

Version runtimeChannel.

### runtimeMainExecutablePath
    
    
    public runtimeMainExecutablePath: string;

Version runtimeMainExecutablePath.

### scaling
    
    
    public scaling?: ("automaticScaling"|"basicScaling"|"manualScaling");

Version scaling.

### serviceAccount
    
    
    public serviceAccount: string;

Version serviceAccount.

### servingStatus
    
    
    public servingStatus: (google.appengine.v1.ServingStatus|keyof typeof google.appengine.v1.ServingStatus);

Version servingStatus.

### threadsafe
    
    
    public threadsafe: boolean;

Version threadsafe.

### versionUrl
    
    
    public versionUrl: string;

Version versionUrl.

### vm
    
    
    public vm: boolean;

Version vm.

### vpcAccessConnector
    
    
    public vpcAccessConnector?: (google.appengine.v1.IVpcAccessConnector|null);

Version vpcAccessConnector.

### zones
    
    
    public zones: string[];

Version zones.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.appengine.v1.IVersion): google.appengine.v1.Version;

Creates a new Version instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iversion)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)` | Version instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.appengine.v1.Version;

Decodes a Version message from the specified reader or buffer.

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
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)` | Version  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.appengine.v1.Version;

Decodes a Version message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)` | Version  
  
### encode(message, writer)
    
    
    public static encode(message: google.appengine.v1.IVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Version message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iversion)`   
Version message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.appengine.v1.IVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Version message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iversion)`   
Version message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.appengine.v1.Version;

Creates a Version message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)` | Version  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Version

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

Converts this Version to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.appengine.v1.Version, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Version message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)`   
Version  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Version message.

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
