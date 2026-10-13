---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp/
title: Class Timestamp (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:37.486514+00:00
---

# Class Timestamp (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Timestamp (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A Timestamp represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.

## Implements

firestore.Timestamp

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(seconds, nanoseconds)
    
    
    constructor(seconds: number, nanoseconds: number);

Creates a new timestamp.

**Parameters**  
---  
**Name** | **Description**  
`seconds` |  `number`   
The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  
`nanoseconds` |  `number`   
The non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanoseconds values that count forward in time. Must be from 0 to 999,999,999 inclusive.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.set({ startTime:new Firestore.Timestamp(42, 0) });
    
    

## Properties 

### nanoseconds
    
    
    get nanoseconds(): number;

The non-negative fractions of a second at nanosecond resolution.

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      let updated = snap.updateTime;
      console.log(`Updated at ${updated.seconds}s ${updated.nanoseconds}ns`);
    });
    
    

{number}

### seconds
    
    
    get seconds(): number;

The number of seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z.

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      let updated = snap.updateTime;
      console.log(`Updated at ${updated.seconds}s ${updated.nanoseconds}ns`);
    });
    
    

{number}

## Methods 

### fromDate(date)
    
    
    static fromDate(date: Date): Timestamp;

Creates a new timestamp from the given date.

**Parameter**  
---  
**Name** | **Description**  
`date` |  `Date`   
The date to initialize the `Timestamp` from.  
**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)` | {Timestamp} A new `Timestamp` representing the same point in time as the given date.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    let date = Date.parse('01 Jan 2000 00:00:00 GMT');
    documentRef.set({ startTime:Firestore.Timestamp.fromDate(date) });
    
    

### fromInstant(instant)
    
    
    static fromInstant(instant: Temporal.Instant): Timestamp;

Creates a new timestamp from the given `Temporal.Instant`.

**Parameter**  
---  
**Name** | **Description**  
`instant` |  `Temporal.Instant`   
The `Temporal.Instant` to initialize the `Timestamp` from.  
**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)` | {Timestamp} A new `Timestamp` representing the same point in time as the given instant.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    let instant = Temporal.Now.instant();
    documentRef.set({ startTime:Firestore.Timestamp.fromInstant(instant) });
    
    

### fromMillis(milliseconds)
    
    
    static fromMillis(milliseconds: number): Timestamp;

Creates a new timestamp from the given number of milliseconds.

**Parameter**  
---  
**Name** | **Description**  
`milliseconds` |  `number`   
Number of milliseconds since Unix epoch 1970-01-01T00:00:00Z.  
**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)` | {Timestamp} A new `Timestamp` representing the same point in time as the given number of milliseconds.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.set({ startTime:Firestore.Timestamp.fromMillis(42) });
    
    

### isEqual(other)
    
    
    isEqual(other: firestore.Timestamp): boolean;

Returns 'true' if this `Timestamp` is equal to the provided one.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `firestore.Timestamp`   
The `Timestamp` to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} 'true' if this `Timestamp` is equal to the provided one.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      if (snap.createTime.isEqual(snap.updateTime)) {
        console.log('Document is in its initial state.');
      }
    });
    
    

### now()
    
    
    static now(): Timestamp;

Creates a new timestamp with the current date, with millisecond precision.

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)` | {Timestamp} A new `Timestamp` representing the current date.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.set({ updateTime:Firestore.Timestamp.now() });
    
    

### toDate()
    
    
    toDate(): Date;

Returns a new `Date` corresponding to this timestamp. This may lose precision.

**Returns**  
---  
**Type** | **Description**  
`Date` | {Date} JavaScript `Date` object representing the same point in time as this `Timestamp`, with millisecond precision.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      console.log(`Document updated at: ${snap.updateTime.toDate()}`);
    });
    
    

### toInstant()
    
    
    toInstant(): Temporal.Instant;

Converts a `Timestamp` to a `Temporal.Instant` object.

**Returns**  
---  
**Type** | **Description**  
`Temporal.Instant` | {Temporal.Instant} `Temporal.Instant` object representing the same point in time as this `Timestamp`, with nanosecond precision.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      console.log(`Document updated at: ${snap.updateTime.toInstant()}`);
    });
    
    

### toMillis()
    
    
    toMillis(): number;

Returns the number of milliseconds since Unix epoch 1970-01-01T00:00:00Z.

**Returns**  
---  
**Type** | **Description**  
`number` | {number} The point in time corresponding to this timestamp, represented as the number of milliseconds since Unix epoch 1970-01-01T00:00:00Z.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(snap => {
      let startTime = snap.get('startTime');
      let endTime = snap.get('endTime');
      console.log(`Duration: ${endTime - startTime}`);
    });
    
    

### valueOf()
    
    
    valueOf(): string;

Converts this object to a primitive `string`, which allows `Timestamp` objects to be compared using the `>`, `<=`, `>=` and `>` operators.

**Returns**  
---  
**Type** | **Description**  
`string` | {string} a string encoding of this object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
