---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression
title: Class Pipelines.BooleanExpression (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:32.653260+00:00
---

# Class Pipelines.BooleanExpression (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.BooleanExpression (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

An expression that evaluates to a boolean value.

This expression type is useful for filter conditions.

## Inheritance

[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) > Pipelines.BooleanExpression

## Implements

firestore.Pipelines.BooleanExpression

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Properties 

### _expr
    
    
    abstract get _expr(): Expression;

## Methods 

### _toProto(serializer)
    
    
    _toProto(serializer: Serializer): api.IValue;

**Parameter**  
---  
**Name** | **Description**  
`serializer` |  `Serializer`   
  
**Returns**  
---  
**Type** | **Description**  
`api.IValue` |   
  
### _validateUserData(ignoreUndefinedProperties)
    
    
    _validateUserData(ignoreUndefinedProperties: boolean): void;

**Parameter**  
---  
**Name** | **Description**  
`ignoreUndefinedProperties` |  `boolean`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### conditional(thenExpr, elseExpr)
    
    
    conditional(thenExpr: Expression, elseExpr: Expression): FunctionExpression;

Creates a conditional expression that evaluates to the 'then' expression if `this` expression evaluates to `true`, or evaluates to the 'else' expression if `this` expressions evaluates `false`.
    
    
    // If 'age' is greater than 18, return "Adult"; otherwise, return "Minor".
    field("age").greaterThanOrEqual(18).conditional(constant("Adult"), constant("Minor"));
    

**Parameters**  
---  
**Name** | **Description**  
`thenExpr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to evaluate if the condition is true.  
`elseExpr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to evaluate if the condition is false.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the conditional expression.  
  
### countIf()
    
    
    countIf(): AggregateFunction;

Creates an aggregation that finds the count of input documents satisfying this boolean expression.
    
    
    // Find the count of documents with a score greater than 90
    field("score").greaterThan(90).countIf().as("highestScore");
    

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'countIf' aggregation.  
  
### ifError(catchValue)
    
    
    ifError(catchValue: BooleanExpression): BooleanExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.
    
    
    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    constant(50).divide('length').gt(1).ifError(constant(false));
    

**Parameter**  
---  
**Name** | **Description**  
`catchValue` |  `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`   
The value that will be returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expr` representing the 'ifError' operation.  
  
### ifError(catchValue)
    
    
    ifError(catchValue: boolean): BooleanExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.
    
    
    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    constant(50).divide('length').gt(1).ifError(false);
    

**Parameter**  
---  
**Name** | **Description**  
`catchValue` |  `boolean`   
The value that will be returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expr` representing the 'ifError' operation.  
  
### ifError(catchValue)
    
    
    ifError(catchValue: Expression): FunctionExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.
    
    
    // Create an expression that protects against a divide by zero error.
    constant(50).divide('length').gt(1).ifError(constant(0));
    

**Parameter**  
---  
**Name** | **Description**  
`catchValue` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The value that will be returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the 'ifError' operation.  
  
### ifError(catchValue)
    
    
    ifError(catchValue: unknown): FunctionExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.
    
    
    // Create an expression that protects against a divide by zero error.
    constant(50).divide('length').gt(1).ifError(0);
    

**Parameter**  
---  
**Name** | **Description**  
`catchValue` |  `unknown`   
The value that will be returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the 'ifError' operation.  
  
### not()
    
    
    not(): BooleanExpression;

Creates an expression that negates this boolean expression.
    
    
    // Find documents where the 'tags' field does not contain 'completed'
    field("tags").arrayContains("completed").not();
    

**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the negated filter condition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
