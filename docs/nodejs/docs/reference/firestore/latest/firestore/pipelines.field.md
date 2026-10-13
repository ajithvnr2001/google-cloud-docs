---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.field
title: Class Pipelines.Field (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:34.680011+00:00
---

# Class Pipelines.Field (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.field

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.Field (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Represents a reference to a field in a Firestore document, or outputs of a `Pipeline` stage.

Field references are used to access document field values in expressions and to specify fields for sorting, filtering, and projecting data in Firestore pipelines.

You can create a `Field` instance using the static `field` method:
    
    
    // Create a Field instance for the 'name' field
    const nameField = field("name");
    
    // Create a Field instance for a nested field 'address.city'
    const cityField = field("address.city");
    

## Inheritance

[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) > Pipelines.Field

## Implements

firestore.Pipelines.Selectable

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Field` class.

## Properties 

### _alias
    
    
    get _alias(): string;

### _expr
    
    
    get _expr(): Expression;

### expressionType
    
    
    readonly expressionType: firestore.Pipelines.ExpressionType;

### fieldName
    
    
    get fieldName(): string;

### selectable
    
    
    selectable: true;

## Methods 

### geoDistance(location)
    
    
    geoDistance(location: GeoPoint | Expression): Expression;

Evaluates to the distance in meters between the location specified by this field and the query location.

**Parameter**  
---  
**Name** | **Description**  
`location` |  `[GeoPoint](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/geopoint) | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
Compute distance to this GeoPoint.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | An `Expression` representing the geoDistance function.  
**Remarks**

This Expression can only be used within a `search` stage.

**Example**
    
    
    typescript
    const geoDistanceToUser = field('location').geoDistance(new GeoPoint(39.7541, -105.0002));
    
    db.pipeline().collection('restaurants').search({
      query: geoDistanceToUser.lessThanOrEqual(2000),
      sort: geoDistanceToUser.ascending()
    })
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
