---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class
title: Class protos.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:06.546172+00:00
---

# Class protos.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents an ImportDocumentsRequest.

## Implements

[protos.google.cloud.discoveryengine.v1alpha.IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iimportdocumentsrequest)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1alpha.IImportDocumentsRequest);

Constructs a new ImportDocumentsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iimportdocumentsrequest)`   
Properties to set  
  
## Properties 

### alloyDbSource
    
    
    public alloyDbSource?: (google.cloud.discoveryengine.v1alpha.IAlloyDbSource|null);

ImportDocumentsRequest alloyDbSource.

### autoGenerateIds
    
    
    public autoGenerateIds: boolean;

ImportDocumentsRequest autoGenerateIds.

### bigquerySource
    
    
    public bigquerySource?: (google.cloud.discoveryengine.v1alpha.IBigQuerySource|null);

ImportDocumentsRequest bigquerySource.

### bigtableSource
    
    
    public bigtableSource?: (google.cloud.discoveryengine.v1alpha.IBigtableSource|null);

ImportDocumentsRequest bigtableSource.

### cloudSqlSource
    
    
    public cloudSqlSource?: (google.cloud.discoveryengine.v1alpha.ICloudSqlSource|null);

ImportDocumentsRequest cloudSqlSource.

### errorConfig
    
    
    public errorConfig?: (google.cloud.discoveryengine.v1alpha.IImportErrorConfig|null);

ImportDocumentsRequest errorConfig.

### fhirStoreSource
    
    
    public fhirStoreSource?: (google.cloud.discoveryengine.v1alpha.IFhirStoreSource|null);

ImportDocumentsRequest fhirStoreSource.

### firestoreSource
    
    
    public firestoreSource?: (google.cloud.discoveryengine.v1alpha.IFirestoreSource|null);

ImportDocumentsRequest firestoreSource.

### gcsSource
    
    
    public gcsSource?: (google.cloud.discoveryengine.v1alpha.IGcsSource|null);

ImportDocumentsRequest gcsSource.

### idField
    
    
    public idField: string;

ImportDocumentsRequest idField.

### inlineSource
    
    
    public inlineSource?: (google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.IInlineSource|null);

ImportDocumentsRequest inlineSource.

### parent
    
    
    public parent: string;

ImportDocumentsRequest parent.

### reconciliationMode
    
    
    public reconciliationMode: (google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.ReconciliationMode|keyof typeof google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.ReconciliationMode);

ImportDocumentsRequest reconciliationMode.

### source
    
    
    public source?: ("inlineSource"|"gcsSource"|"bigquerySource"|"fhirStoreSource"|"spannerSource"|"cloudSqlSource"|"firestoreSource"|"alloyDbSource"|"bigtableSource");

ImportDocumentsRequest source.

### spannerSource
    
    
    public spannerSource?: (google.cloud.discoveryengine.v1alpha.ISpannerSource|null);

ImportDocumentsRequest spannerSource.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

ImportDocumentsRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1alpha.IImportDocumentsRequest): google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest;

Creates a new ImportDocumentsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iimportdocumentsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class)` | ImportDocumentsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest;

Decodes an ImportDocumentsRequest message from the specified reader or buffer.

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
`[ImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class)` | ImportDocumentsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest;

Decodes an ImportDocumentsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class)` | ImportDocumentsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1alpha.IImportDocumentsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportDocumentsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iimportdocumentsrequest)`   
ImportDocumentsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1alpha.IImportDocumentsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportDocumentsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iimportdocumentsrequest)`   
ImportDocumentsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest;

Creates an ImportDocumentsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class)` | ImportDocumentsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImportDocumentsRequest

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

Converts this ImportDocumentsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImportDocumentsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImportDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.importdocumentsrequest-class)`   
ImportDocumentsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImportDocumentsRequest message.

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
