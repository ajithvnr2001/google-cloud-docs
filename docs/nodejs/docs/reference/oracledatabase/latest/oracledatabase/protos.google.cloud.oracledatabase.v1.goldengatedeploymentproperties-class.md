---
url: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class
title: Class protos.google.cloud.oracledatabase.v1.GoldengateDeploymentProperties (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:29.485806+00:00
---

# Class protos.google.cloud.oracledatabase.v1.GoldengateDeploymentProperties (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.oracledatabase.v1.GoldengateDeploymentProperties (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.8.0  0.2.0  0.1.0 

Represents a GoldengateDeploymentProperties.

## Implements

[protos.google.cloud.oracledatabase.v1.IGoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengatedeploymentproperties)

## Package

[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.oracledatabase.v1.IGoldengateDeploymentProperties);

Constructs a new GoldengateDeploymentProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengatedeploymentproperties)`   
Properties to set  
  
## Properties 

### backupSchedule
    
    
    public backupSchedule?: (google.cloud.oracledatabase.v1.IGoldengateBackupSchedule|null);

GoldengateDeploymentProperties backupSchedule.

### category
    
    
    public category: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentCategory|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentCategory);

GoldengateDeploymentProperties category.

### cpuCoreCount
    
    
    public cpuCoreCount: number;

GoldengateDeploymentProperties cpuCoreCount.

### deploymentBackupId
    
    
    public deploymentBackupId: string;

GoldengateDeploymentProperties deploymentBackupId.

### deploymentDiagnosticData
    
    
    public deploymentDiagnosticData?: (google.cloud.oracledatabase.v1.IDeploymentDiagnosticData|null);

GoldengateDeploymentProperties deploymentDiagnosticData.

### deploymentRole
    
    
    public deploymentRole: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentRoleType|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentRoleType);

GoldengateDeploymentProperties deploymentRole.

### deploymentType
    
    
    public deploymentType: string;

GoldengateDeploymentProperties deploymentType.

### deploymentUrl
    
    
    public deploymentUrl: string;

GoldengateDeploymentProperties deploymentUrl.

### description
    
    
    public description: string;

GoldengateDeploymentProperties description.

### environmentType
    
    
    public environmentType: string;

GoldengateDeploymentProperties environmentType.

### fqdn
    
    
    public fqdn: string;

GoldengateDeploymentProperties fqdn.

### healthy
    
    
    public healthy: boolean;

GoldengateDeploymentProperties healthy.

### ingressIps
    
    
    public ingressIps: google.cloud.oracledatabase.v1.IIngressIp[];

GoldengateDeploymentProperties ingressIps.

### isAutoScalingEnabled
    
    
    public isAutoScalingEnabled: boolean;

GoldengateDeploymentProperties isAutoScalingEnabled.

### isLatestVersion
    
    
    public isLatestVersion: boolean;

GoldengateDeploymentProperties isLatestVersion.

### isPublic
    
    
    public isPublic: boolean;

GoldengateDeploymentProperties isPublic.

### isStorageUtilizationLimitExceeded
    
    
    public isStorageUtilizationLimitExceeded: boolean;

GoldengateDeploymentProperties isStorageUtilizationLimitExceeded.

### lastBackupScheduleTime
    
    
    public lastBackupScheduleTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties lastBackupScheduleTime.

### licenseModel
    
    
    public licenseModel: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.LicenseModel|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.LicenseModel);

GoldengateDeploymentProperties licenseModel.

### lifecycleDetails
    
    
    public lifecycleDetails: string;

GoldengateDeploymentProperties lifecycleDetails.

### lifecycleState
    
    
    public lifecycleState: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleState|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleState);

GoldengateDeploymentProperties lifecycleState.

### lifecycleSubState
    
    
    public lifecycleSubState: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleSubState|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleSubState);

GoldengateDeploymentProperties lifecycleSubState.

### loadBalancerId
    
    
    public loadBalancerId: string;

GoldengateDeploymentProperties loadBalancerId.

### loadBalancerSubnetId
    
    
    public loadBalancerSubnetId: string;

GoldengateDeploymentProperties loadBalancerSubnetId.

### locks
    
    
    public locks: google.cloud.oracledatabase.v1.IGoldengateDeploymentLock[];

GoldengateDeploymentProperties locks.

### maintenanceConfig
    
    
    public maintenanceConfig?: (google.cloud.oracledatabase.v1.IGoldengateMaintenanceConfig|null);

GoldengateDeploymentProperties maintenanceConfig.

### maintenanceWindow
    
    
    public maintenanceWindow?: (google.cloud.oracledatabase.v1.IGoldengateMaintenanceWindow|null);

GoldengateDeploymentProperties maintenanceWindow.

### nextBackupScheduleTime
    
    
    public nextBackupScheduleTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties nextBackupScheduleTime.

### nextMaintenanceActionType
    
    
    public nextMaintenanceActionType: (google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.NextMaintenanceActionType|keyof typeof google.cloud.oracledatabase.v1.GoldengateDeploymentProperties.NextMaintenanceActionType);

GoldengateDeploymentProperties nextMaintenanceActionType.

### nextMaintenanceDescription
    
    
    public nextMaintenanceDescription: string;

GoldengateDeploymentProperties nextMaintenanceDescription.

### nextMaintenanceTime
    
    
    public nextMaintenanceTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties nextMaintenanceTime.

### nsgIds
    
    
    public nsgIds: string[];

GoldengateDeploymentProperties nsgIds.

### ocid
    
    
    public ocid: string;

GoldengateDeploymentProperties ocid.

### oggData
    
    
    public oggData?: (google.cloud.oracledatabase.v1.IGoldengateOggDeployment|null);

GoldengateDeploymentProperties oggData.

### oggVersionSupportEndTime
    
    
    public oggVersionSupportEndTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties oggVersionSupportEndTime.

### placements
    
    
    public placements: google.cloud.oracledatabase.v1.IGoldengatePlacement[];

GoldengateDeploymentProperties placements.

### privateIpAddress
    
    
    public privateIpAddress: string;

GoldengateDeploymentProperties privateIpAddress.

### publicIpAddress
    
    
    public publicIpAddress: string;

GoldengateDeploymentProperties publicIpAddress.

### roleChangeTime
    
    
    public roleChangeTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties roleChangeTime.

### storageUtilizationBytes
    
    
    public storageUtilizationBytes: (number|Long|string);

GoldengateDeploymentProperties storageUtilizationBytes.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties updateTime.

### upgradeRequiredTime
    
    
    public upgradeRequiredTime?: (google.protobuf.ITimestamp|null);

GoldengateDeploymentProperties upgradeRequiredTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.oracledatabase.v1.IGoldengateDeploymentProperties): google.cloud.oracledatabase.v1.GoldengateDeploymentProperties;

Creates a new GoldengateDeploymentProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengatedeploymentproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class)` | GoldengateDeploymentProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.oracledatabase.v1.GoldengateDeploymentProperties;

Decodes a GoldengateDeploymentProperties message from the specified reader or buffer.

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
`[GoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class)` | GoldengateDeploymentProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.oracledatabase.v1.GoldengateDeploymentProperties;

Decodes a GoldengateDeploymentProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class)` | GoldengateDeploymentProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.oracledatabase.v1.IGoldengateDeploymentProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateDeploymentProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengatedeploymentproperties)`   
GoldengateDeploymentProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.oracledatabase.v1.IGoldengateDeploymentProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateDeploymentProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengatedeploymentproperties)`   
GoldengateDeploymentProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.oracledatabase.v1.GoldengateDeploymentProperties;

Creates a GoldengateDeploymentProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class)` | GoldengateDeploymentProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GoldengateDeploymentProperties

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

Converts this GoldengateDeploymentProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.oracledatabase.v1.GoldengateDeploymentProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GoldengateDeploymentProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GoldengateDeploymentProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengatedeploymentproperties-class)`   
GoldengateDeploymentProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GoldengateDeploymentProperties message.

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
