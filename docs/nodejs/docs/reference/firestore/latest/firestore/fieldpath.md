---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath/
title: Class FieldPath (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:34.748077+00:00
---

# Class FieldPath (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class FieldPath (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A dot-separated path for navigating sub-objects (e.g. nested maps) within a document.

## Inheritance

Path<[FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)> > FieldPath

## Implements

firestore.FieldPath

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(segments)
    
    
    constructor(...segments: string[]);

Constructs a Firestore Field Path.

**Parameter**  
---  
**Name** | **Description**  
`segments` |  `string[]`   
Sequence of field names that form this path.  
**Example**
    
    
    let query = firestore.collection('col');
    let fieldPath = new FieldPath('f.o.o', 'bar');
    
    query.where(fieldPath, '==', 42).get().then(snapshot => {
      snapshot.forEach(document => {
        console.log(`Document contains {'f.o.o' : {'bar' : 42}}`);
      });
    });
    

## Methods 

### documentId()
    
    
    static documentId(): FieldPath;

A special FieldPath value to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.

**Returns**  
---  
**Type** | **Description**  
`[FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)` | {FieldPath}  
  
### isEqual(other)
    
    
    isEqual(other: FieldPath): boolean;

Returns true if this `FieldPath` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `[FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `FieldPath` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
