---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue/
title: Class FieldValue (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:26.479061+00:00
---

# Class FieldValue (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class FieldValue (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Sentinel values that can be used when writing documents with set(), create() or update().

FieldValue

## Implements

firestore.FieldValue

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)()
    
    
    constructor();

Constructs a new instance of the `FieldValue` class

## Methods 

### arrayRemove(elements)
    
    
    static arrayRemove(...elements: unknown[]): FieldValue;

Returns a special value that can be used with set(), create() or update() that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.

**Parameter**  
---  
**Name** | **Description**  
`elements` |  `unknown[]`   
The elements to remove from the array.  
**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` | {FieldValue} The FieldValue sentinel for use in a call to set(), create() or update().  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update(
      'array', Firestore.FieldValue.arrayRemove('foo')
    ).then(() => {
      return documentRef.get();
    }).then(doc => {
      // doc.get('array') no longer contains field 'foo'
    });
    

### arrayUnion(elements)
    
    
    static arrayUnion(...elements: unknown[]): FieldValue;

Returns a special value that can be used with set(), create() or update() that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.

**Parameter**  
---  
**Name** | **Description**  
`elements` |  `unknown[]`   
The elements to union into the array.  
**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` | {FieldValue} The FieldValue sentinel for use in a call to set(), create() or update().  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update(
      'array', Firestore.FieldValue.arrayUnion('foo')
    ).then(() => {
      return documentRef.get();
    }).then(doc => {
      // doc.get('array') contains field 'foo'
    });
    

### delete()
    
    
    static delete(): FieldValue;

Returns a sentinel for use with update() or set() with {merge:true} to mark a field for deletion.

**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` | {FieldValue} The sentinel value to use in your objects.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    let data = { a: 'b', c: 'd' };
    
    documentRef.set(data).then(() => {
      return documentRef.update({a: Firestore.FieldValue.delete()});
    }).then(() => {
      // Document now only contains { c: 'd' }
    });
    

### increment(n)
    
    
    static increment(n: number): FieldValue;

Returns a special value that can be used with set(), create() or update() that tells the server to increment the field's current value by the given value.

If either current field value or the operand uses floating point precision, both values will be interpreted as floating point numbers and all arithmetic will follow IEEE 754 semantics. Otherwise, integer precision is kept and the result is capped between -2^63 and 2^63-1.

If the current field value is not of type 'number', or if the field does not yet exist, the transformation will set the field to the given value.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The value to increment by.  
**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` | {FieldValue} The FieldValue sentinel for use in a call to set(), create() or update().  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update(
      'counter', Firestore.FieldValue.increment(1)
    ).then(() => {
      return documentRef.get();
    }).then(doc => {
      // doc.get('counter') was incremented
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.FieldValue): boolean;

Returns true if this `FieldValue` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `firestore.FieldValue`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `FieldValue` is equal to the provided value.  
**Example**
    
    
    let fieldValues = [
      Firestore.FieldValue.increment(-1.0),
      Firestore.FieldValue.increment(-1),
      Firestore.FieldValue.increment(-0.0),
      Firestore.FieldValue.increment(-0),
      Firestore.FieldValue.increment(0),
      Firestore.FieldValue.increment(0.0),
      Firestore.FieldValue.increment(1),
      Firestore.FieldValue.increment(1.0)
    ];
    
    let equal = 0;
    for (let i = 0; i < fieldvalues.length;="" ++i)="" {="" for="" (let="" j="i" +="" 1;="" j="">< fieldvalues.length;="" ++j)="" {="" if="" (fieldvalues[i].isequal(fieldvalues[j]))="" {="" ++equal;="" }="" }="" }="" console.log(`found="" ${equal}="" equalities.`);="">

### maximum(n)
    
    
    static maximum(n: number): FieldValue;

Returns a special value that can be used with `set()`, `create()` or `update()` that tells the server to set the field to the numeric maximum of the field's current and the given value.

If the current field value is not of type 'number', or if the field does not yet exist, the transformation will set the field to the given value.

If the existing value and the operand are equivalent, then the field does not change. For example, `0`, `0.0`, and `-0.0` are all equivalent. If the operand is `NaN` then the result is always `NaN`.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The value to compare to the exiting field value. {FieldValue} The `FieldValue` for use in a call to `set()`, `create()` or `update()`.  
**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` |   
**Example**
    
    
    typescript
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update(
      'counter', Firestore.FieldValue.maximum(1)
    ).then(() => {
      return documentRef.get();
    }).then(doc => {
      // doc.get('counter') is the maximum of either the existing value or 1
    });
    

### minimum(n)
    
    
    static minimum(n: number): FieldValue;

Returns a special value that can be used with `set()`, `create()` or `update()` that tells the server to set the field to the numeric minimum of the field's current and the given value.

If the current field value is not of type 'number', or if the field does not yet exist, the transformation will set the field to the given value.

If the existing value and the operand are equivalent, then the field does not change. For example, `0`, `0.0`, and `-0.0` are all equivalent. If the operand is `NaN` then the result is always `NaN`.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The value to compare to the exiting field value. {FieldValue} The FieldValue for use in a call to `set()`, `create()` or `update()`.  
**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` |   
**Example**
    
    
    typescript
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update(
      'counter', Firestore.FieldValue.minimum(1)
    ).then(() => {
      return documentRef.get();
    }).then(doc => {
      // doc.get('counter') is the minimum of either the existing value or 1
    });
    

### serverTimestamp()
    
    
    static serverTimestamp(): FieldValue;

Returns a sentinel used with set(), create() or update() to include a server-generated timestamp in the written data.

**Returns**  
---  
**Type** | **Description**  
`[FieldValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldvalue)` | {FieldValue} The FieldValue sentinel for use in a call to set(), create() or update().  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.set({
      time: Firestore.FieldValue.serverTimestamp()
    }).then(() => {
      return documentRef.get();
    }).then(doc => {
      console.log(`Server time set to ${doc.get('time')}`);
    });
    

### vector(values)
    
    
    static vector(values?: number[]): VectorValue;

Creates a new `VectorValue` constructed with a copy of the given array of numbers.

**Parameter**  
---  
**Name** | **Description**  
`values` |  `number[]`   
Create a `VectorValue` instance with a copy of this array of numbers.  
**Returns**  
---  
**Type** | **Description**  
`[VectorValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorvalue)` | A new `VectorValue` constructed with a copy of the given array of numbers.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
