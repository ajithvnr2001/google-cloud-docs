---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest
title: Class protos.google.cloud.networkmanagement.v1.ConnectivityTest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:15.441131+00:00
---

# Class protos.google.cloud.networkmanagement.v1.ConnectivityTest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.ConnectivityTest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents a ConnectivityTest.

## Implements

[protos.google.cloud.networkmanagement.v1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iconnectivitytest)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IConnectivityTest);

Constructs a new ConnectivityTest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iconnectivitytest)`   
Properties to set  
  
## Properties 

### bypassFirewallChecks
    
    
    public bypassFirewallChecks: boolean;

ConnectivityTest bypassFirewallChecks.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ConnectivityTest createTime.

### description
    
    
    public description: string;

ConnectivityTest description.

### destination
    
    
    public destination?: (google.cloud.networkmanagement.v1.IEndpoint|null);

ConnectivityTest destination.

### displayName
    
    
    public displayName: string;

ConnectivityTest displayName.

### labels
    
    
    public labels: { [k: string]: string };

ConnectivityTest labels.

### name
    
    
    public name: string;

ConnectivityTest name.

### probingDetails
    
    
    public probingDetails?: (google.cloud.networkmanagement.v1.IProbingDetails|null);

ConnectivityTest probingDetails.

### protocol
    
    
    public protocol: string;

ConnectivityTest protocol.

### reachabilityDetails
    
    
    public reachabilityDetails?: (google.cloud.networkmanagement.v1.IReachabilityDetails|null);

ConnectivityTest reachabilityDetails.

### relatedProjects
    
    
    public relatedProjects: string[];

ConnectivityTest relatedProjects.

### returnReachabilityDetails
    
    
    public returnReachabilityDetails?: (google.cloud.networkmanagement.v1.IReachabilityDetails|null);

ConnectivityTest returnReachabilityDetails.

### roundTrip
    
    
    public roundTrip: boolean;

ConnectivityTest roundTrip.

### source
    
    
    public source?: (google.cloud.networkmanagement.v1.IEndpoint|null);

ConnectivityTest source.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

ConnectivityTest updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IConnectivityTest): google.cloud.networkmanagement.v1.ConnectivityTest;

Creates a new ConnectivityTest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iconnectivitytest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest)` | ConnectivityTest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.ConnectivityTest;

Decodes a ConnectivityTest message from the specified reader or buffer.

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
`[ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest)` | ConnectivityTest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.ConnectivityTest;

Decodes a ConnectivityTest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest)` | ConnectivityTest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IConnectivityTest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConnectivityTest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iconnectivitytest)`   
ConnectivityTest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IConnectivityTest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConnectivityTest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iconnectivitytest)`   
ConnectivityTest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.ConnectivityTest;

Creates a ConnectivityTest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest)` | ConnectivityTest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConnectivityTest

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

Converts this ConnectivityTest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.ConnectivityTest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConnectivityTest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.connectivitytest)`   
ConnectivityTest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConnectivityTest message.

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
