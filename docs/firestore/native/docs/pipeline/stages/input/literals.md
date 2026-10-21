---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/literals/
title: Literals (Input Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:59.055927+00:00
---

# Literals (Input Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/literals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Literals (Input Stage)

## Description

Returns documents from a fixed set of predefined document objects.

This stage is commonly used for testing other stages in isolation, though it can also be used as input to join conditions.

## Examples

### Node.js
    
    
    const results = await db.pipeline()
      .literals({ name: "joe", age: 10 }, { name: "bob", age: 30 }, { name: "alice", age: 40 })
      .where(field("age").lessThan(35))
      .execute();
    

## Behavior

The `literals(...)` stage can only be used as the first stage in a pipeline (or sub-pipeline). The order of documents returned from the `literals(...)` matches the order in which they are defined.

While literal values are the most common, it is also possible to pass in expressions, which will be evaluated and returned, making it possible to test out different query / expression behavior without first needing to create some test data.

For example, the following shows how to quickly test out the `length(...)` function on some constant test sets:

### Node.js
    
    
    const results = await db.pipeline()
      .literals({ x: constant("foo-bar-baz").length() }, { x: constant("bar").length() })
      .execute();
    
    ...
    
    [
      { x: 11 },
      { x: 3 }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
