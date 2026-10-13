---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class
title: Class protos.google.cloud.ces.v1.App (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:54.732309+00:00
---

# Class protos.google.cloud.ces.v1.App (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.App (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an App.

## Implements

[protos.google.cloud.ces.v1.IApp](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapp)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IApp);

Constructs a new App.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApp](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapp)`   
Properties to set  
  
## Properties 

### audioProcessingConfig
    
    
    public audioProcessingConfig?: (google.cloud.ces.v1.IAudioProcessingConfig|null);

App audioProcessingConfig.

### clientCertificateSettings
    
    
    public clientCertificateSettings?: (google.cloud.ces.v1.IClientCertificateSettings|null);

App clientCertificateSettings.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

App createTime.

### dataStoreSettings
    
    
    public dataStoreSettings?: (google.cloud.ces.v1.IDataStoreSettings|null);

App dataStoreSettings.

### defaultChannelProfile
    
    
    public defaultChannelProfile?: (google.cloud.ces.v1.IChannelProfile|null);

App defaultChannelProfile.

### deploymentCount
    
    
    public deploymentCount: number;

App deploymentCount.

### description
    
    
    public description: string;

App description.

### displayName
    
    
    public displayName: string;

App displayName.

### errorHandlingSettings
    
    
    public errorHandlingSettings?: (google.cloud.ces.v1.IErrorHandlingSettings|null);

App errorHandlingSettings.

### etag
    
    
    public etag: string;

App etag.

### evaluationMetricsThresholds
    
    
    public evaluationMetricsThresholds?: (google.cloud.ces.v1.IEvaluationMetricsThresholds|null);

App evaluationMetricsThresholds.

### globalInstruction
    
    
    public globalInstruction: string;

App globalInstruction.

### guardrails
    
    
    public guardrails: string[];

App guardrails.

### languageSettings
    
    
    public languageSettings?: (google.cloud.ces.v1.ILanguageSettings|null);

App languageSettings.

### locked
    
    
    public locked: boolean;

App locked.

### loggingSettings
    
    
    public loggingSettings?: (google.cloud.ces.v1.ILoggingSettings|null);

App loggingSettings.

### metadata
    
    
    public metadata: { [k: string]: string };

App metadata.

### modelSettings
    
    
    public modelSettings?: (google.cloud.ces.v1.IModelSettings|null);

App modelSettings.

### name
    
    
    public name: string;

App name.

### pinned
    
    
    public pinned: boolean;

App pinned.

### predefinedVariableDeclarations
    
    
    public predefinedVariableDeclarations: google.cloud.ces.v1.App.IVariableDeclaration[];

App predefinedVariableDeclarations.

### rootAgent
    
    
    public rootAgent: string;

App rootAgent.

### timeZoneSettings
    
    
    public timeZoneSettings?: (google.cloud.ces.v1.ITimeZoneSettings|null);

App timeZoneSettings.

### toolExecutionMode
    
    
    public toolExecutionMode: (google.cloud.ces.v1.App.ToolExecutionMode|keyof typeof google.cloud.ces.v1.App.ToolExecutionMode);

App toolExecutionMode.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

App updateTime.

### validationErrors
    
    
    public validationErrors: string[];

App validationErrors.

### variableDeclarations
    
    
    public variableDeclarations: google.cloud.ces.v1.App.IVariableDeclaration[];

App variableDeclarations.

### vpcScSettings
    
    
    public vpcScSettings?: (google.cloud.ces.v1.IVpcScSettings|null);

App vpcScSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IApp): google.cloud.ces.v1.App;

Creates a new App instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApp](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapp)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)` | App instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.App;

Decodes an App message from the specified reader or buffer.

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
`[App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)` | App  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.App;

Decodes an App message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)` | App  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IApp, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified App message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApp](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapp)`   
App message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IApp, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified App message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApp](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapp)`   
App message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.App;

Creates an App message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)` | App  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for App

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

Converts this App to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.App, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an App message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)`   
App  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an App message.

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
