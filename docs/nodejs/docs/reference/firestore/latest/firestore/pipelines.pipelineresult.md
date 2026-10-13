---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelineresult
title: Class Pipelines.PipelineResult (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.290573+00:00
---

# Class Pipelines.PipelineResult (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelineresult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.PipelineResult (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A PipelineResult contains data read from a Firestore Pipeline. The data can be extracted with the `data()` or `get(String)` methods.

If the PipelineResult represents a non-document result, `ref` will return a undefined value.

## Implements

firestore.Pipelines.PipelineResult

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `PipelineResult` class.

## Properties 

### _createTime
    
    
    readonly _createTime: Timestamp | undefined;

### _executionTime
    
    
    readonly _executionTime: Timestamp | undefined;

### _updateTime
    
    
    readonly _updateTime: Timestamp | undefined;

### createTime
    
    
    get createTime(): Timestamp | undefined;

The time the document was created. Undefined if this result is not a document.

{Timestamp|undefined}

### id
    
    
    get id(): string | undefined;

The ID of the document for which this PipelineResult contains data, if it is a document; otherwise `undefined`.

{string}

### ref
    
    
    get ref(): DocumentReference | undefined;

The reference of the document, if it is a document; otherwise `undefined`.

### updateTime
    
    
    get updateTime(): Timestamp | undefined;

The time the document was last updated (at the time the snapshot was generated). Undefined if this result is not a document.

{Timestamp|undefined}

## Methods 

### data()
    
    
    data(): firestore.DocumentData;

Retrieves all fields in the result as an object.

**Returns**  
---  
**Type** | **Description**  
`firestore.DocumentData` | {T} An object containing all fields in the document.  
**Example**
    
    
    typescript
    let p = firestore.pipeline().collection('col');
    
    p.execute().then(results => {
      let data = results[0].data();
      console.log(`Retrieved data: ${JSON.stringify(data)}`);
    });
    

### get(fieldPath)
    
    
    get(fieldPath: string | FieldPath): any;

Retrieves the field specified by `field`.

**Parameter**  
---  
**Name** | **Description**  
`fieldPath` |  `string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
The field path (e.g. 'foo' or 'foo.bar') to a specific field.  
**Returns**  
---  
**Type** | **Description**  
`any` | {*} The data at the specified field location or undefined if no such field exists.  
**Example**
    
    
    typescript
    let p = firestore.pipeline().collection('col');
    
    p.execute().then(results => {
      let field = results[0].get('a.b');
      console.log(`Retrieved field value: ${field}`);
    });
    

### isEqual(other)
    
    
    isEqual(other: PipelineResult): boolean;

Returns true if the document's data and path in this `PipelineResult` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `[PipelineResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelineresult)`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `PipelineResult` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
