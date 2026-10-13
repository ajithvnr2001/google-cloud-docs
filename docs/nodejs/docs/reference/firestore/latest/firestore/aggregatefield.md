---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield/
title: Class AggregateField (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:32.277141+00:00
---

# Class AggregateField (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class AggregateField (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Represents an aggregation that can be performed by Firestore.

## Implements

FirebaseFirestore.AggregateField<T>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `AggregateField` class.

## Properties 

### aggregateType
    
    
    readonly aggregateType: AggregateType;

### type
    
    
    readonly type = "AggregateField";

A type string to uniquely identify instances of this class.

## Methods 

### average(field)
    
    
    static average(field: string | FieldPath): AggregateField<number | null>;

Create an AggregateField object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

**Parameter**  
---  
**Name** | **Description**  
`field` |  `string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
Specifies the field to average across the result set.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateField](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)<number | null>` |   
  
### count()
    
    
    static count(): AggregateField<number>;

Create an AggregateField object that can be used to compute the count of documents in the result set of a query.

**Returns**  
---  
**Type** | **Description**  
`[AggregateField](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)<number>` |   
  
### isEqual(other)
    
    
    isEqual(other: AggregateField<T>): boolean;

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if `other` performs the same kind of aggregation on the same field (if any).

**Parameter**  
---  
**Name** | **Description**  
`other` |  `[AggregateField](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)<T>`   
The object to compare to this object for equality.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | `true` if this object is "equal" to the given object, as defined above, or `false` otherwise.  
  
### sum(field)
    
    
    static sum(field: string | FieldPath): AggregateField<number>;

Create an AggregateField object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

**Parameter**  
---  
**Name** | **Description**  
`field` |  `string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
Specifies the field to sum across the result set.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateField](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatefield)<number>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
