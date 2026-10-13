---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bytes/
title: Class Bytes (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:33.433105+00:00
---

# Class Bytes (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bytes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Bytes (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

An immutable object representing an array of bytes.

## Implements

firestore.Bytes

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Properties 

### data
    
    
    readonly data: Uint8Array;

### subtype
    
    
    readonly subtype: number;

## Methods 

### fromBase64String(base64, subtype)
    
    
    static fromBase64String(base64: string, subtype?: number): Bytes;

Creates a new `Bytes` object from the given Base64 string, converting it to bytes.

**Parameters**  
---  
**Name** | **Description**  
`base64` |  `string`   
The Base64 string used to create the `Bytes` object.  
`subtype` |  `number`   
Optional subtype value.  
**Returns**  
---  
**Type** | **Description**  
`[Bytes](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bytes)` |   
  
### fromUint8Array(array, subtype)
    
    
    static fromUint8Array(array: Uint8Array, subtype?: number): Bytes;

Creates a new `Bytes` object from the given Uint8Array.

**Parameters**  
---  
**Name** | **Description**  
`array` |  `Uint8Array`   
The Uint8Array used to create the `Bytes` object.  
`subtype` |  `number`   
Optional subtype value.  
**Returns**  
---  
**Type** | **Description**  
`[Bytes](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bytes)` |   
  
### isEqual(other)
    
    
    isEqual(other: unknown): boolean;

Returns true if this `Bytes` object is equal to the provided one.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `unknown`   
The `Bytes` object to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | true if this `Bytes` object is equal to the provided one.  
  
### toBase64()
    
    
    toBase64(): string;

Returns the underlying bytes as a Base64-encoded string.

**Returns**  
---  
**Type** | **Description**  
`string` | The Base64-encoded string created from the `Bytes` object.  
  
### toString()
    
    
    toString(): string;

Returns a string representation of the `Bytes` object.

**Returns**  
---  
**Type** | **Description**  
`string` | A string representation of the `Bytes` object.  
  
### toUint8Array()
    
    
    toUint8Array(): Uint8Array;

Returns the underlying bytes in a new `Uint8Array`.

**Returns**  
---  
**Type** | **Description**  
`Uint8Array` | The Uint8Array created from the `Bytes` object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
