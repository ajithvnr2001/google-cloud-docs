---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/let/
title: Let (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:50.382995+00:00
---

# Let (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/let/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Let (Transformation Stage)

## Description

Define temporary variables that can be referenced in subsequent stages of the pipeline.

Variables created in the `let(...)` stage are not included in the final results unless they are explicitly assigned to a field in a later stage (e.g., using [`add_fields(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields) or [`select(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/select)). This lets you simplify complex logic by breaking it into smaller, reusable components without cluttering the output documents. The `let(...)` stage is particularly useful for **correlated sub-pipelines** , where a sub-pipeline needs to reference a value from the parent document's scope.

## Examples

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/awards")
      // `let(...)` referred to as `define(...)` in the Web SDK.
      .define(rand().as("r"))
      .addFields(
        switchOn(
          lessThan(variable("r"), 0.05), constant("rare"),
          lessThan(variable("r"), 0.25), constant("uncommon"),
          constant("common")).as("random_score"))
      .execute();
    

## Behavior

### Variables versus Fields

While **fields** represent data stored within documents, **variables** are temporary values that exist only during the execution of the pipeline.

| Fields | Variables  
---|---|---  
Purpose | access or store fields into documents | generate or access temporary values during pipeline execution  
SDK Usage | `field("name")` | `variable("name")`  
Scope | local to current document | global to pipeline and sub-pipelines  
Undefined References | evaluates to `absent` | generates runtime error  
  
**Scope:**

While fields are scoped to the local document, variables are defined in a separate scope and remain accessible across stages until the first occurrence of a stage that "merges" multiple documents together (like [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate) or [`distinct(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/distinct)). Stages that "merges" multiple documents don't allow variable references to be used afterwards as by merging the previous stage's results together there is no longer one value for the variable.

Do: Reference a variable after filtering the document's fields.

### Node.js
    
    
    const results = db.pipeline()
      .collection("/awards")
      .define(min(field("score").abs(), constant(100)).as("normalized_score"))
      .select(field("__name__"), field("owner_id"))
      // Successfully able to use the variable.
      .where(variable("normalized_score").greaterThan(10))
      .execute();
    

Don't: Reference a variable **after** an aggregation.

### Node.js
    
    
    const results = db.pipeline()
      .collection("/awards")
      .define(min(field("score").abs(), constant(100)).as("normalized_score"))
      .aggregate({
        accumulators: [ field("score").avg().as("avg_score") ],
        groups: [ field("owner_id") ]
      })
      // Attempting to use the variable throws a request validation error.
      .where(variable("normalized_score").greaterThan(10))
      .execute();
    

**Undefined References:**

While referencing an undefined field is fine (and just evaluates to `absent`), attempting to reference an undefined variable will fail during request validation. In this sense, field references can be viewed as performing a lookup in a map at runtime while variable references are more akin to variables in a statically compiled programming language.

### Global Scope and Subqueries

Variables are essential when working with nested pipelines. A sub-pipeline executes in its own scope and can only access the fields of the documents it is currently processing. To use a value from the "parent" document inside a subquery, you must first define it as a variable using the `let(...)` stage.

### Node.js
    
    
    // Fetch reviewers alongside their negative reviews.
    const pipeline = db.pipeline()
      .collection("/reviewers")
      // `let(...)` referred to as `define(...)` in the Web SDK.
      .define(field("__name__").as("reviewer_name"))
      .select("__name__", array(db.pipeline().collectionGroup("reviews")
        .where(field("author").equals(variable("reviewer_name")))
        .where(field("rating").lessThan(2))
        .select("review", "rating")).as("negative_reviews"))
      .execute();
    

### Overlapping Variables

Defining a variable with a name that was already defined in a previous `let(...)` stage will overwrite the previous variable. This can be used to update temporary state as the pipeline progresses.

Variables referenced in sub-pipeline follow [lexical scoping rules](https://en.wikipedia.org/wiki/Scope_\(computer_programming\)#Lexical_scope) as found in many programming languages and refers to the variables under the same name defined by the closest (parent) pipeline.

### Comparison with `add_fields(...)`

The `let(...)` stage behaves similarly to the [`add_fields(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields) stage, but instead of adding fields to the document, it assigns values to variables.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
