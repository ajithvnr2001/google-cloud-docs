---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot/
title: Class QueryDocumentSnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.646899+00:00
---

# Class QueryDocumentSnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class QueryDocumentSnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A QueryDocumentSnapshot contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with [data()] or [get()] to get a specific field.

A QueryDocumentSnapshot offers the same API surface as a [DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot). Since query results contain only existing documents, the [exists] property will always be true and [data()] will never return 'undefined'.

QueryDocumentSnapshot DocumentSnapshot

## Inheritance

[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)<AppModelType, DbModelType> > QueryDocumentSnapshot

## Implements

FirebaseFirestore.QueryDocumentSnapshot<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Properties 

### createTime
    
    
    /** @override */
    get createTime(): Timestamp;

The time the document was created.

{Timestamp} QueryDocumentSnapshot#createTime

**Example**
    
    
    let query = firestore.collection('col');
    
    query.get().forEach(snapshot => {
      console.log(`Document created at '${snapshot.createTime.toDate()}'`);
    });
    

### updateTime
    
    
    /** @override */
    get updateTime(): Timestamp;

The time the document was last updated (at the time the snapshot was generated).

{Timestamp} QueryDocumentSnapshot#updateTime

**Example**
    
    
    let query = firestore.collection('col');
    
    query.get().forEach(snapshot => {
      console.log(`Document updated at '${snapshot.updateTime.toDate()}'`);
    });
    

## Methods 

### data()
    
    
    /** @override */
    data(): AppModelType;

Retrieves all fields in the document as an object.

**Returns**  
---  
**Type** | **Description**  
`AppModelType` | {T} An object containing all fields in the document.  
**Example**
    
    
    let query = firestore.collection('col');
    
    query.get().forEach(documentSnapshot => {
      let data = documentSnapshot.data();
      console.log(`Retrieved data: ${JSON.stringify(data)}`);
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
