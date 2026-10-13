---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class
title: Class protos.google.cloud.deploy.v1.AutomationRun (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:27.931521+00:00
---

# Class protos.google.cloud.deploy.v1.AutomationRun (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.AutomationRun (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents an AutomationRun.

## Implements

[protos.google.cloud.deploy.v1.IAutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iautomationrun)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IAutomationRun);

Constructs a new AutomationRun.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iautomationrun)`   
Properties to set  
  
## Properties 

### advanceRolloutOperation
    
    
    public advanceRolloutOperation?: (google.cloud.deploy.v1.IAdvanceRolloutOperation|null);

AutomationRun advanceRolloutOperation.

### automationId
    
    
    public automationId: string;

AutomationRun automationId.

### automationSnapshot
    
    
    public automationSnapshot?: (google.cloud.deploy.v1.IAutomation|null);

AutomationRun automationSnapshot.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AutomationRun createTime.

### etag
    
    
    public etag: string;

AutomationRun etag.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

AutomationRun expireTime.

### name
    
    
    public name: string;

AutomationRun name.

### operation
    
    
    public operation?: ("promoteReleaseOperation"|"advanceRolloutOperation"|"repairRolloutOperation"|"timedPromoteReleaseOperation");

AutomationRun operation.

### policyViolation
    
    
    public policyViolation?: (google.cloud.deploy.v1.IPolicyViolation|null);

AutomationRun policyViolation.

### promoteReleaseOperation
    
    
    public promoteReleaseOperation?: (google.cloud.deploy.v1.IPromoteReleaseOperation|null);

AutomationRun promoteReleaseOperation.

### repairRolloutOperation
    
    
    public repairRolloutOperation?: (google.cloud.deploy.v1.IRepairRolloutOperation|null);

AutomationRun repairRolloutOperation.

### ruleId
    
    
    public ruleId: string;

AutomationRun ruleId.

### serviceAccount
    
    
    public serviceAccount: string;

AutomationRun serviceAccount.

### state
    
    
    public state: (google.cloud.deploy.v1.AutomationRun.State|keyof typeof google.cloud.deploy.v1.AutomationRun.State);

AutomationRun state.

### stateDescription
    
    
    public stateDescription: string;

AutomationRun stateDescription.

### targetId
    
    
    public targetId: string;

AutomationRun targetId.

### timedPromoteReleaseOperation
    
    
    public timedPromoteReleaseOperation?: (google.cloud.deploy.v1.ITimedPromoteReleaseOperation|null);

AutomationRun timedPromoteReleaseOperation.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AutomationRun updateTime.

### waitUntilTime
    
    
    public waitUntilTime?: (google.protobuf.ITimestamp|null);

AutomationRun waitUntilTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IAutomationRun): google.cloud.deploy.v1.AutomationRun;

Creates a new AutomationRun instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iautomationrun)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)` | AutomationRun instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.AutomationRun;

Decodes an AutomationRun message from the specified reader or buffer.

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
`[AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)` | AutomationRun  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.AutomationRun;

Decodes an AutomationRun message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)` | AutomationRun  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IAutomationRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AutomationRun message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iautomationrun)`   
AutomationRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IAutomationRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AutomationRun message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iautomationrun)`   
AutomationRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.AutomationRun;

Creates an AutomationRun message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)` | AutomationRun  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AutomationRun

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

Converts this AutomationRun to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.AutomationRun, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AutomationRun message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AutomationRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.automationrun-class)`   
AutomationRun  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AutomationRun message.

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
