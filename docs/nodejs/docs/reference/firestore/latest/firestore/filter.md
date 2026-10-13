---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter/
title: Class Filter (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:35.243145+00:00
---

# Class Filter (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Filter (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A `Filter` represents a restriction on one or more field values and can be used to refine the results of a [Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query). `Filters`s are created by invoking , , or and can then be passed to to create a new [Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) instance that also contains this `Filter`.

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Methods 

### and(filters)
    
    
    static and(...filters: Filter[]): Filter;

Creates and returns a new [Filter][Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter) that is a conjunction of the given [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s. A conjunction filter includes a document if it satisfies all of the given [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s.

The returned Filter can be applied to [Query.where()], [Filter.or()], or [Filter.and()]. When applied to a [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) it requires that documents must satisfy one of the provided [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s.

**Parameter**  
---  
**Name** | **Description**  
`filters` |  `[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)[]`   
Optional. The [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s for AND operation. These must be created with calls to , , or .  
**Returns**  
---  
**Type** | **Description**  
`[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)` | {Filter} The created [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter).  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    // doc.foo == 'bar' && doc.baz > 0
    let andFilter = Filter.and(Filter.where('foo', '==', 'bar'), Filter.where('baz', '>', 0));
    
    collectionRef.where(andFilter).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### or(filters)
    
    
    static or(...filters: Filter[]): Filter;

Creates and returns a new [Filter][Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter) that is a disjunction of the given [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s. A disjunction filter includes a document if it satisfies any of the given [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s.

The returned Filter can be applied to [Query.where()], [Filter.or()], or [Filter.and()]. When applied to a [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) it requires that documents must satisfy one of the provided [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s.

**Parameter**  
---  
**Name** | **Description**  
`filters` |  `[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)[]`   
Optional. The [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)s for OR operation. These must be created with calls to , , or .  
**Returns**  
---  
**Type** | **Description**  
`[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)` | {Filter} The created [Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter).  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    // doc.foo == 'bar' || doc.baz > 0
    let orFilter = Filter.or(Filter.where('foo', '==', 'bar'), Filter.where('baz', '>', 0));
    
    collectionRef.where(orFilter).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

### where(fieldPath, opStr, value)
    
    
    static where(fieldPath: string | firestore.FieldPath, opStr: firestore.WhereFilterOp, value: unknown): Filter;

Creates and returns a new [Filter][Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter), which can be applied to [Query.where()], [Filter.or()], or [Filter.and()]. When applied to a [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query) it requires that documents must contain the specified field and that its value should satisfy the relation constraint provided.

**Parameters**  
---  
**Name** | **Description**  
`fieldPath` |  `string | FirebaseFirestore.FieldPath`   
The name of a property value to compare.  
`opStr` |  `firestore.WhereFilterOp`   
A comparison operation in the form of a string. Acceptable operator strings are "<", "<=", "==", "!=", ">=", ">", "array-contains", "in", "not-in", and "array-contains-any".  
`value` |  `unknown`   
The value to which to compare the field for inclusion in a query.  
**Returns**  
---  
**Type** | **Description**  
`[Filter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/filter)` | {Filter} The created Filter.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.where(Filter.where('foo', '==', 'bar')).get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Found document at ${documentSnapshot.ref.path}`);
      });
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
