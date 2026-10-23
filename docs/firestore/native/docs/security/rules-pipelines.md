---
url: https://docs.cloud.google.com/firestore/native/docs/security/rules-pipelines/
title: Security Rules for Pipeline operations \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:48.387562+00:00
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
  * `allow create` permissions: Triggered by `insert()` stages, and `upsert()` stages when creating new documents.
  * `allow update` permissions: Triggered by `update()` stages, and `upsert()` stages when updating existing documents.
  * `allow delete` permissions: Triggered by `delete()` stages.
  * `allow write` permissions: Applies to all DML operations (`insert()`, `update()`, `upsert()`, and `delete()`).
  * Field modification stages: Rules only operate on stored data and not derived values. If a pipeline includes stages that modify fields (For example, `AddFields`, `ReplaceWith`, `Select`), the Rules engine stops applying filter constraints after that stage is encountered.
  * Literals stage: The `literals()` stage does not read from the database but can incur costs. To prevent abuse, it must be paired with another stage (like `collection()`) that can be verified by rules.



## Data manipulation language (DML) stages and Security Rules

When executing Data manipulation language (DML) stages (`insert()`, `update()`, `upsert()`, and `delete()`), Security Rules evaluate permissions differently than for read queries:

  * **Per-document rule evaluation** : Unlike read pipelines, which require filter expressions up front to constrain the query at planning time, DML operations evaluate security rules against each individual document mutation.
  * **Rule variables** : 
    * `request.resource`: Contains the proposed document data for `insert()`, `update()`, and `upsert()` operations.
    * `resource`: Contains the current document data stored in the database prior to modification (available for `update()`, `delete()`, and `upsert()` of existing documents).



### System limits and execution behavior with DML

When running DML operations with Security Rules, keep the following system limits and execution behaviors in mind:

#### The twenty-lookup limit on `get()` and `exists()`

Firebase Security Rules allows a maximum of 20 document lookups (`get()` or `exists()`) across an entire request.

When a DML pipeline runs outside of an explicit transaction, documents are processed in batches. Because each batch executes in its own transaction and documents might be modified concurrently between batches, security rules and document lookups are re-evaluated for **each write batch**.

Even if your security rules evaluate against a single static document, for example, checking whether a user is an administrator:
    
    
    rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {
        match /posts/{postId} {
          allow write: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.isAdmin == true;
        }
      }
    }
    

Each write batch of documents performs a lookup. As a result, after writing all possible documents, the 20 lookup limit for the request is reached, and the pipeline fails with a `PERMISSION_DENIED` error. In addition, each lookup performed per write batch incurs its own read billing.

**Tip:** To avoid hitting the 20 lookup limit on bulk DML operations, use [Custom Claims](https://firebase.google.com/docs/auth/admin/custom-claims) on Firebase Authentication tokens (for example, `request.auth.token.isAdmin == true`) instead of `get()` or `exists()` lookups. Custom claims are validated in memory directly from the authentication token, avoiding document reads and lookup limits entirely.

#### Partial success and `PERMISSION_DENIED`

When executing outside of a transaction, DML operations commit writes in sequential batches. If a batch fails—either because a document fails a rule condition or because the 20-lookup limit is exceeded—the pipeline halts and returns a `PERMISSION_DENIED` error.

However, **batches that were already committed are not rolled back**. The database remains in a partially updated state. Because the client receives an error without a list of modified documents, you must query your data to inspect which writes succeeded.

**Tip:** If your workload requires all-or-nothing execution, run the DML pipeline within an explicit user transaction (for example, using `runTransaction` and `transaction.execute(pipeline)`). In a transaction, all operations either commit together or roll back completely on error. Note that transactions are subject to Firestore Enterprise edition transaction limits.

#### Diagnosing rule failures with Cloud Audit Logs

For security reasons, client-facing `PERMISSION_DENIED` errors don't disclose which security rule condition failed or whether the 20-lookup limit was reached.

To diagnose rule evaluation failures, project administrators can inspect Cloud Audit Logs in the Google Cloud console (under **Firestore** > **Monitoring** or in **Logs Explorer**) to view detailed `EvaluationError` entries.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
