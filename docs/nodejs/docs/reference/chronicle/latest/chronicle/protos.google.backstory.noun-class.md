---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class
title: Class protos.google.backstory.Noun (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:22.889411+00:00
---

# Class protos.google.backstory.Noun (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.backstory.Noun (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a Noun.

## Implements

[protos.google.backstory.INoun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.inoun)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.backstory.INoun);

Constructs a new Noun.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INoun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.inoun)`   
Properties to set  
  
## Properties 

### administrativeDomain
    
    
    public administrativeDomain: string;

Noun administrativeDomain.

### application
    
    
    public application: string;

Noun application.

### artifact
    
    
    public artifact?: (google.backstory.IArtifact|null);

Noun artifact.

### asset
    
    
    public asset?: (google.backstory.IAsset|null);

Noun asset.

### assetId
    
    
    public assetId: string;

Noun assetId.

### browser
    
    
    public browser?: (google.backstory.IBrowser|null);

Noun browser.

### cloud
    
    
    public cloud?: (google.backstory.ICloud|null);

Noun cloud.

### domain
    
    
    public domain?: (google.backstory.IDomain|null);

Noun domain.

### email
    
    
    public email: string;

Noun email.

### file
    
    
    public file?: (google.backstory.IFile|null);

Noun file.

### group
    
    
    public group?: (google.backstory.IGroup|null);

Noun group.

### hostname
    
    
    public hostname: string;

Noun hostname.

### investigation
    
    
    public investigation?: (google.backstory.IInvestigation|null);

Noun investigation.

### ip
    
    
    public ip: string[];

Noun ip.

### ipGeoArtifact
    
    
    public ipGeoArtifact: google.backstory.IArtifact[];

Noun ipGeoArtifact.

### ipLocation
    
    
    public ipLocation: google.backstory.ILocation[];

Noun ipLocation.

### labels
    
    
    public labels: google.backstory.ILabel[];

Noun labels.

### location
    
    
    public location?: (google.backstory.ILocation|null);

Noun location.

### mac
    
    
    public mac: string[];

Noun mac.

### namespace
    
    
    public namespace: string;

Noun namespace.

### natIp
    
    
    public natIp: string[];

Noun natIp.

### natPort
    
    
    public natPort: number;

Noun natPort.

### network
    
    
    public network?: (google.backstory.INetwork|null);

Noun network.

### objectReference
    
    
    public objectReference?: (google.backstory.IId|null);

Noun objectReference.

### platform
    
    
    public platform: (google.backstory.Noun.Platform|keyof typeof google.backstory.Noun.Platform);

Noun platform.

### platformPatchLevel
    
    
    public platformPatchLevel: string;

Noun platformPatchLevel.

### platformVersion
    
    
    public platformVersion: string;

Noun platformVersion.

### port
    
    
    public port: number;

Noun port.

### process
    
    
    public process?: (google.backstory.IProcess|null);

Noun process.

### processAncestors
    
    
    public processAncestors: google.backstory.IProcess[];

Noun processAncestors.

### registry
    
    
    public registry?: (google.backstory.IRegistry|null);

Noun registry.

### resource
    
    
    public resource?: (google.backstory.IResource|null);

Noun resource.

### resourceAncestors
    
    
    public resourceAncestors: google.backstory.IResource[];

Noun resourceAncestors.

### securityResult
    
    
    public securityResult: google.backstory.ISecurityResult[];

Noun securityResult.

### url
    
    
    public url: string;

Noun url.

### urlMetadata
    
    
    public urlMetadata?: (google.backstory.IUrl|null);

Noun urlMetadata.

### user
    
    
    public user?: (google.backstory.IUser|null);

Noun user.

### userManagementChain
    
    
    public userManagementChain: google.backstory.IUser[];

Noun userManagementChain.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.backstory.INoun): google.backstory.Noun;

Creates a new Noun instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INoun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.inoun)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Noun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class)` | Noun instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.backstory.Noun;

Decodes a Noun message from the specified reader or buffer.

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
`[Noun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class)` | Noun  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.backstory.Noun;

Decodes a Noun message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Noun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class)` | Noun  
  
### encode(message, writer)
    
    
    public static encode(message: google.backstory.INoun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Noun message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INoun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.inoun)`   
Noun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.backstory.INoun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Noun message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INoun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.inoun)`   
Noun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.backstory.Noun;

Creates a Noun message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Noun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class)` | Noun  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Noun

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

Converts this Noun to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.backstory.Noun, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Noun message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Noun](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.noun-class)`   
Noun  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Noun message.

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
