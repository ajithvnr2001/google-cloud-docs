---
url: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class
title: Class protos.google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:14.435640+00:00
---

# Class protos.google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.8.0  0.2.0  0.1.0 

Represents a GoldengateRedisConnectionProperties.

## Implements

[protos.google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateredisconnectionproperties)

## Package

[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties);

Constructs a new GoldengateRedisConnectionProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateredisconnectionproperties)`   
Properties to set  
  
## Properties 

### authenticationType
    
    
    public authenticationType: (google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties.RedisAuthenticationType|keyof typeof google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties.RedisAuthenticationType);

GoldengateRedisConnectionProperties authenticationType.

### connectionPasswordOptions
    
    
    public connectionPasswordOptions?: ("password"|"passwordSecretVersion");

GoldengateRedisConnectionProperties connectionPasswordOptions.

### keyStoreFile
    
    
    public keyStoreFile: string;

GoldengateRedisConnectionProperties keyStoreFile.

### keyStorePassword
    
    
    public keyStorePassword?: (string|null);

GoldengateRedisConnectionProperties keyStorePassword.

### keyStorePasswordOptions
    
    
    public keyStorePasswordOptions?: ("keyStorePassword"|"keyStorePasswordSecretVersion");

GoldengateRedisConnectionProperties keyStorePasswordOptions.

### keyStorePasswordSecretVersion
    
    
    public keyStorePasswordSecretVersion?: (string|null);

GoldengateRedisConnectionProperties keyStorePasswordSecretVersion.

### password
    
    
    public password?: (string|null);

GoldengateRedisConnectionProperties password.

### passwordSecretVersion
    
    
    public passwordSecretVersion?: (string|null);

GoldengateRedisConnectionProperties passwordSecretVersion.

### redisClusterId
    
    
    public redisClusterId: string;

GoldengateRedisConnectionProperties redisClusterId.

### securityProtocol
    
    
    public securityProtocol: (google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties.RedisSecurityProtocol|keyof typeof google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties.RedisSecurityProtocol);

GoldengateRedisConnectionProperties securityProtocol.

### servers
    
    
    public servers: string;

GoldengateRedisConnectionProperties servers.

### technologyType
    
    
    public technologyType: string;

GoldengateRedisConnectionProperties technologyType.

### trustStoreFile
    
    
    public trustStoreFile: string;

GoldengateRedisConnectionProperties trustStoreFile.

### trustStorePassword
    
    
    public trustStorePassword?: (string|null);

GoldengateRedisConnectionProperties trustStorePassword.

### trustStorePasswordOptions
    
    
    public trustStorePasswordOptions?: ("trustStorePassword"|"trustStorePasswordSecretVersion");

GoldengateRedisConnectionProperties trustStorePasswordOptions.

### trustStorePasswordSecretVersion
    
    
    public trustStorePasswordSecretVersion?: (string|null);

GoldengateRedisConnectionProperties trustStorePasswordSecretVersion.

### username
    
    
    public username: string;

GoldengateRedisConnectionProperties username.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties): google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties;

Creates a new GoldengateRedisConnectionProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateredisconnectionproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class)` | GoldengateRedisConnectionProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties;

Decodes a GoldengateRedisConnectionProperties message from the specified reader or buffer.

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
`[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class)` | GoldengateRedisConnectionProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties;

Decodes a GoldengateRedisConnectionProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class)` | GoldengateRedisConnectionProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateRedisConnectionProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateredisconnectionproperties)`   
GoldengateRedisConnectionProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateRedisConnectionProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateredisconnectionproperties)`   
GoldengateRedisConnectionProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties;

Creates a GoldengateRedisConnectionProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class)` | GoldengateRedisConnectionProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GoldengateRedisConnectionProperties

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

Converts this GoldengateRedisConnectionProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.oracledatabase.v1.GoldengateRedisConnectionProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GoldengateRedisConnectionProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateredisconnectionproperties-class)`   
GoldengateRedisConnectionProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GoldengateRedisConnectionProperties message.

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
