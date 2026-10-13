---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class
title: Class protos.google.cloud.aiplatform.v1beta1.FeatureView (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:49.294122+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.FeatureView (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.FeatureView (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a FeatureView.

## Implements

[protos.google.cloud.aiplatform.v1beta1.IFeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeatureview)

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.aiplatform.v1beta1.IFeatureView);

Constructs a new FeatureView.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeatureview)`   
Properties to set  
  
## Properties 

### bigQuerySource
    
    
    public bigQuerySource?: (google.cloud.aiplatform.v1beta1.FeatureView.IBigQuerySource|null);

FeatureView bigQuerySource.

### bigtableMetadata
    
    
    public bigtableMetadata?: (google.cloud.aiplatform.v1beta1.FeatureView.IBigtableMetadata|null);

FeatureView bigtableMetadata.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

FeatureView createTime.

### etag
    
    
    public etag: string;

FeatureView etag.

### featureRegistrySource
    
    
    public featureRegistrySource?: (google.cloud.aiplatform.v1beta1.FeatureView.IFeatureRegistrySource|null);

FeatureView featureRegistrySource.

### indexConfig
    
    
    public indexConfig?: (google.cloud.aiplatform.v1beta1.FeatureView.IIndexConfig|null);

FeatureView indexConfig.

### labels
    
    
    public labels: { [k: string]: string };

FeatureView labels.

### name
    
    
    public name: string;

FeatureView name.

### optimizedConfig
    
    
    public optimizedConfig?: (google.cloud.aiplatform.v1beta1.FeatureView.IOptimizedConfig|null);

FeatureView optimizedConfig.

### satisfiesPzi
    
    
    public satisfiesPzi: boolean;

FeatureView satisfiesPzi.

### satisfiesPzs
    
    
    public satisfiesPzs: boolean;

FeatureView satisfiesPzs.

### serviceAccountEmail
    
    
    public serviceAccountEmail: string;

FeatureView serviceAccountEmail.

### serviceAgentType
    
    
    public serviceAgentType: (google.cloud.aiplatform.v1beta1.FeatureView.ServiceAgentType|keyof typeof google.cloud.aiplatform.v1beta1.FeatureView.ServiceAgentType);

FeatureView serviceAgentType.

### source
    
    
    public source?: ("bigQuerySource"|"featureRegistrySource"|"vertexRagSource");

FeatureView source.

### syncConfig
    
    
    public syncConfig?: (google.cloud.aiplatform.v1beta1.FeatureView.ISyncConfig|null);

FeatureView syncConfig.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

FeatureView updateTime.

### vectorSearchConfig
    
    
    public vectorSearchConfig?: (google.cloud.aiplatform.v1beta1.FeatureView.IVectorSearchConfig|null);

FeatureView vectorSearchConfig.

### vertexRagSource
    
    
    public vertexRagSource?: (google.cloud.aiplatform.v1beta1.FeatureView.IVertexRagSource|null);

FeatureView vertexRagSource.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.aiplatform.v1beta1.IFeatureView): google.cloud.aiplatform.v1beta1.FeatureView;

Creates a new FeatureView instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeatureview)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)` | FeatureView instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.aiplatform.v1beta1.FeatureView;

Decodes a FeatureView message from the specified reader or buffer.

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
`[FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)` | FeatureView  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.aiplatform.v1beta1.FeatureView;

Decodes a FeatureView message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)` | FeatureView  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.aiplatform.v1beta1.IFeatureView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureView message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeatureview)`   
FeatureView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.aiplatform.v1beta1.IFeatureView, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FeatureView message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeatureview)`   
FeatureView message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.aiplatform.v1beta1.FeatureView;

Creates a FeatureView message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)` | FeatureView  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FeatureView

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

Converts this FeatureView to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.aiplatform.v1beta1.FeatureView, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FeatureView message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)`   
FeatureView  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FeatureView message.

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
