---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class
title: Class protos.google.cloud.redis.v1.Instance (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:19.259248+00:00
---

# Class protos.google.cloud.redis.v1.Instance (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.v1.Instance (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.0  5.1.0  5.0.1  3.3.0  3.2.2  3.1.5  2.4.0  2.3.1  2.2.6 

Represents an Instance.

## Implements

[protos.google.cloud.redis.v1.IInstance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance)

## Package

[@google-cloud/redis](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.redis.v1.IInstance);

Constructs a new Instance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance)`   
Properties to set  
  
## Properties 

### alternativeLocationId
    
    
    public alternativeLocationId: string;

Instance alternativeLocationId.

### authEnabled
    
    
    public authEnabled: boolean;

Instance authEnabled.

### authorizedNetwork
    
    
    public authorizedNetwork: string;

Instance authorizedNetwork.

### availableMaintenanceVersions
    
    
    public availableMaintenanceVersions: string[];

Instance availableMaintenanceVersions.

### connectMode
    
    
    public connectMode: (google.cloud.redis.v1.Instance.ConnectMode|keyof typeof google.cloud.redis.v1.Instance.ConnectMode);

Instance connectMode.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Instance createTime.

### currentLocationId
    
    
    public currentLocationId: string;

Instance currentLocationId.

### customerManagedKey
    
    
    public customerManagedKey: string;

Instance customerManagedKey.

### displayName
    
    
    public displayName: string;

Instance displayName.

### host
    
    
    public host: string;

Instance host.

### labels
    
    
    public labels: { [k: string]: string };

Instance labels.

### locationId
    
    
    public locationId: string;

Instance locationId.

### maintenancePolicy
    
    
    public maintenancePolicy?: (google.cloud.redis.v1.IMaintenancePolicy|null);

Instance maintenancePolicy.

### maintenanceSchedule
    
    
    public maintenanceSchedule?: (google.cloud.redis.v1.IMaintenanceSchedule|null);

Instance maintenanceSchedule.

### maintenanceVersion
    
    
    public maintenanceVersion: string;

Instance maintenanceVersion.

### memorySizeGb
    
    
    public memorySizeGb: number;

Instance memorySizeGb.

### name
    
    
    public name: string;

Instance name.

### nodes
    
    
    public nodes: google.cloud.redis.v1.INodeInfo[];

Instance nodes.

### persistenceConfig
    
    
    public persistenceConfig?: (google.cloud.redis.v1.IPersistenceConfig|null);

Instance persistenceConfig.

### persistenceIamIdentity
    
    
    public persistenceIamIdentity: string;

Instance persistenceIamIdentity.

### port
    
    
    public port: number;

Instance port.

### readEndpoint
    
    
    public readEndpoint: string;

Instance readEndpoint.

### readEndpointPort
    
    
    public readEndpointPort: number;

Instance readEndpointPort.

### readReplicasMode
    
    
    public readReplicasMode: (google.cloud.redis.v1.Instance.ReadReplicasMode|keyof typeof google.cloud.redis.v1.Instance.ReadReplicasMode);

Instance readReplicasMode.

### redisConfigs
    
    
    public redisConfigs: { [k: string]: string };

Instance redisConfigs.

### redisVersion
    
    
    public redisVersion: string;

Instance redisVersion.

### replicaCount
    
    
    public replicaCount: number;

Instance replicaCount.

### reservedIpRange
    
    
    public reservedIpRange: string;

Instance reservedIpRange.

### secondaryIpRange
    
    
    public secondaryIpRange: string;

Instance secondaryIpRange.

### serverCaCerts
    
    
    public serverCaCerts: google.cloud.redis.v1.ITlsCertificate[];

Instance serverCaCerts.

### state
    
    
    public state: (google.cloud.redis.v1.Instance.State|keyof typeof google.cloud.redis.v1.Instance.State);

Instance state.

### statusMessage
    
    
    public statusMessage: string;

Instance statusMessage.

### suspensionReasons
    
    
    public suspensionReasons: google.cloud.redis.v1.Instance.SuspensionReason[];

Instance suspensionReasons.

### tier
    
    
    public tier: (google.cloud.redis.v1.Instance.Tier|keyof typeof google.cloud.redis.v1.Instance.Tier);

Instance tier.

### transitEncryptionMode
    
    
    public transitEncryptionMode: (google.cloud.redis.v1.Instance.TransitEncryptionMode|keyof typeof google.cloud.redis.v1.Instance.TransitEncryptionMode);

Instance transitEncryptionMode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.redis.v1.IInstance): google.cloud.redis.v1.Instance;

Creates a new Instance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)` | Instance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.redis.v1.Instance;

Decodes an Instance message from the specified reader or buffer.

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
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)` | Instance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.redis.v1.Instance;

Decodes an Instance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)` | Instance  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.redis.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.redis.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.redis.v1.Instance;

Creates an Instance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)` | Instance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Instance

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

Converts this Instance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.redis.v1.Instance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Instance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Instance](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.instance-class)`   
Instance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Instance message.

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
