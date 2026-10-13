---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequerysnapshot/
title: Class AggregateQuerySnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:32.412699+00:00
---

# Class AggregateQuerySnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequerysnapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class AggregateQuerySnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

The results of executing an aggregation query.

## Implements

FirebaseFirestore.AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `AggregateQuerySnapshot` class.

## Properties 

### query
    
    
    get query(): AggregateQuery<AggregateSpecType, AppModelType, DbModelType>;

The query that was executed to produce this result.

### readTime
    
    
    get readTime(): Timestamp;

The time this snapshot was read.

## Methods 

### data()
    
    
    data(): firestore.AggregateSpecData<AggregateSpecType>;

Returns the results of the aggregations performed over the underlying query.

The keys of the returned object will be the same as those of the `AggregateSpec` object specified to the aggregation method, and the values will be the corresponding aggregation result.

**Returns**  
---  
**Type** | **Description**  
`FirebaseFirestore.AggregateSpecData<AggregateSpecType>` | The results of the aggregations performed over the underlying query.  
  
### isEqual(other)
    
    
    isEqual(other: firestore.AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>): boolean;

Compares this object with the given object for equality.

Two `AggregateQuerySnapshot` instances are considered "equal" if they have the same data and their underlying queries compare "equal" using `AggregateQuery.isEqual()`.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>`   
The object to compare to this object for equality.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | `true` if this object is "equal" to the given object, as defined above, or `false` otherwise.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
