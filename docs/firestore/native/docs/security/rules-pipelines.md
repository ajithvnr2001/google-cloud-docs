---
url: https://docs.cloud.google.com/firestore/native/docs/security/rules-pipelines/
title: Security Rules for Pipeline operations \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:55.591273+00:00
---

# Security Rules for Pipeline operations  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/security/rules-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security Rules for Pipeline operations

[Pipeline operations](https://docs.cloud.google.com/firestore/native/docs/query-data/understanding-core-pipelines#pipeline_operations) rules let you match the filtering capabilities of the existing Rules engine. While Pipeline operations offer a rich set of features, the Rules engine is restricted to recognizing simple filters to ensure query satisfiability and security.

### Edition and mode requirements

This document applies to Firestore Enterprise edition in Native mode.

## Supported Filter Expressions

For a query to be constrained by your rules, it must use standard comparison operators against constants. The following filter types are recognized by the Rules engine:

  * Equality and Inequality: `eq`, `neq`.
  * Comparisons: `gt`, `gte`, `lt`, `lte`.
  * Membership: `in`, `arrayContains`.



Here are some examples:

  * `where(eq("foo", 2))`
  * `where(lt("foo", 2))`
  * `documents("/user/1", "/user/2").where(...)`

**Note:** Complex expressions, such as arithmetic within a filter (for example, `where(eq("foo" * 2, 10))`) or string functions like `strContains`, are not recognized for constraining queries.

## Request Properties

You can continue to use the `request` object to validate authentication and query context, though some properties available in standard queries are not supported in pipelines.

### Supported properties

The new engine continues to support the following properties:

  * `request.auth`: Access user uid and token data.
  * `request.method`: Identifies the operation (For example, `get`, `list`).
  * `request.path`: The path of the resource being accessed.
  * `request.time`: The server-side timestamp of the request.



### Unsupported properties

The `request.query` properties such as `limit`, `offset`, and `orderBy` are unsupported for Pipelines rule checks due to the complexity of determining these values in multi-stage queries.

## Pipeline stage handling and permissions

There are different pipeline stages that map to specific granular operations in security rules:

  * `allow list` permissions: Triggered by `collection()`, `collectionGroup()`, and `database()` stages.
  * `allow get` permissions: Triggered by the `documents()` stage, which is treated similarly to a batch `get` operation.
  * Field modification stages: Rules only operate on stored data and not derived values. If a pipeline includes stages that modify fields (For example, `AddFields`, `ReplaceWith`, `Select`), the Rules engine stops applying filter constraints after that stage is encountered.
  * Literals stage: The `literals()` stage does not read from the database but can incur costs. To prevent abuse, it must be paired with another stage (like `collection()`) that can be verified by rules.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
