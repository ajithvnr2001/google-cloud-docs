---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression
title: Class Pipelines.Expression (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:02.309346+00:00
---

# Class Pipelines.Expression (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.Expression (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Represents an expression that can be evaluated to a value within the execution of a `Pipeline`.

Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:

  * **Field references:** Access values from document fields. - **Literals:** Represent constant values (strings, numbers, booleans). - **Function calls:** Apply functions to one or more expressions.



The `Expression` class provides a fluent API for building expressions. You can chain together method calls to create complex expressions.

## Implements

firestore.Pipelines.Expression

HasUserData

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Properties 

### _protoValueType
    
    
    _protoValueType: "ProtoValue";

### expressionType
    
    
    abstract expressionType: firestore.Pipelines.ExpressionType;

## Methods 

### abs()
    
    
    abs(): FunctionExpression;

Creates an expression that computes the absolute value of a numeric value.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the absolute value of the numeric value.  
**Example**
    
    
    typescript
    // Compute the absolute value of the 'price' field.
    field("price").abs();
    

### add(second, others)
    
    
    add(second: firestore.Pipelines.Expression | unknown, ...others: Array<firestore.Pipelines.Expression | unknown>): FunctionExpression;

Creates an expression that adds this expression to another expression.

**Parameters**  
---  
**Name** | **Description**  
`second` |  `FirebaseFirestore.Pipelines.Expression | unknown`   
The expression or literal to add to this expression.  
`others` |  `Array<FirebaseFirestore.Pipelines.Expression | unknown>`   
Optional additional expressions or literals to add to this expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the addition operation.  
**Example**
    
    
    typescript
    // Add the value of the 'quantity' field and the 'reserve' field.
    field("quantity").add(field("reserve"));
    

### arrayAgg()
    
    
    arrayAgg(): AggregateFunction;

Creates an aggregation that collects all values of an expression across multiple stage inputs into an array.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Example**
    
    
    typescript
    // Collect all tags from books into an array
    field("tags").arrayAgg().as("allTags");
    

### arrayAggDistinct()
    
    
    arrayAggDistinct(): AggregateFunction;

Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'array_agg_distinct' aggregation.  
**Remarks**

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Example**
    
    
    typescript
    // Collect all distinct tags from books into an array
    field("tags").arrayAggDistinct().as("allDistinctTags");
    

### arrayConcat(secondArray, otherArrays)
    
    
    arrayConcat(secondArray: Expression | unknown[], ...otherArrays: Array<Expression | unknown[]>): FunctionExpression;

Creates an expression that concatenates an array expression with one or more other arrays.

**Parameters**  
---  
**Name** | **Description**  
`secondArray` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]`   
Second array expression or array literal to concatenate.  
`otherArrays` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown[]>`   
Optional additional array expressions or array literals to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the concatenated array.  
**Example**
    
    
    typescript
    // Combine the 'items' array with another array field.
    field("items").arrayConcat(field("otherItems"));
    

### arrayContains(expression)
    
    
    arrayContains(expression: Expression): BooleanExpression;

Creates an expression that checks if an array contains a specific element.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'sizes' array contains the value from the 'selectedSize' field
    field("sizes").arrayContains(field("selectedSize"));
    

### arrayContains(value)
    
    
    arrayContains(value: unknown): BooleanExpression;

Creates an expression that checks if an array contains a specific value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The element to search for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'colors' array contains "red"
    field("colors").arrayContains("red");
    

### arrayContainsAll(values)
    
    
    arrayContainsAll(values: Array<Expression | unknown>): BooleanExpression;

Creates an expression that checks if an array contains all the specified elements.

**Parameter**  
---  
**Name** | **Description**  
`values` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
**Example**
    
    
    typescript
    // Check if the 'tags' array contains both the value in field "tag1" and the literal value "tag2"
    field("tags").arrayContainsAll([field("tag1"), "tag2"]);
    

### arrayContainsAll(arrayExpression)
    
    
    arrayContainsAll(arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if an array contains all the specified elements.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_all' comparison.  
**Example**
    
    
    typescript
    // Check if the 'tags' array contains both of the values from field "tag1" and the literal value "tag2"
    field("tags").arrayContainsAll(array([field("tag1"), "tag2"]));
    

### arrayContainsAny(values)
    
    
    arrayContainsAny(values: Array<Expression | unknown>): BooleanExpression;

Creates an expression that checks if an array contains any of the specified elements.

**Parameter**  
---  
**Name** | **Description**  
`values` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
**Example**
    
    
    typescript
    // Check if the 'categories' array contains either values from field "cate1" or "cate2"
    field("categories").arrayContainsAny([field("cate1"), field("cate2")]);
    

### arrayContainsAny(arrayExpression)
    
    
    arrayContainsAny(arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if an array contains any of the specified elements.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The elements to check for in the array.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'array_contains_any' comparison.  
**Example**
    
    
    typescript
    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    field("groups").arrayContainsAny(array([field("userGroup"), "guest"]));
    

### arrayFilter(alias, filter)
    
    
    arrayFilter(alias: string, filter: BooleanExpression): FunctionExpression;

Creates an expression that filters an array using a provided alias and predicate expression.

**Parameters**  
---  
**Name** | **Description**  
`alias` |  `string`   
The variable name to use for each element.  
`filter` |  `[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)`   
The predicate boolean expression to evaluate for each element.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the filtered array.  
**Example**
    
    
    typescript
    // Filter "scores" to include only values greater than 50
    field("scores").arrayFilter("score", greaterThan(variable("score"), 50));
    

### arrayFirst()
    
    
    arrayFirst(): FunctionExpression;

Returns the first element of the array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first element.  
**Example**
    
    
    typescript
    // Get the first element of the 'myArray' field.
    field("myArray").arrayFirst();
    

### arrayFirstN(n)
    
    
    arrayFirstN(n: number): FunctionExpression;

Returns the first `n` elements of the array.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
**Example**
    
    
    typescript
    // Get the first 3 elements of the 'myArray' field.
    field("myArray").arrayFirstN(3);
    

### arrayFirstN(n)
    
    
    arrayFirstN(n: Expression): FunctionExpression;

Returns the first `n` elements of the array.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the first `n` elements.  
**Example**
    
    
    typescript
    // Get the first n elements of the 'myArray' field.
    field("myArray").arrayFirstN(field("count"));
    

### arrayGet(index)
    
    
    arrayGet(index: number): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and returns the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.

**Parameter**  
---  
**Name** | **Description**  
`index` |  `number`   
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
**Example**
    
    
    typescript
    // Return the value in the 'tags' field array at index `1`.
    field('tags').arrayGet(1);
    

### arrayGet(indexExpr)
    
    
    arrayGet(indexExpr: Expression): FunctionExpression;

Creates an expression that indexes into an array from the beginning or end and returns the element. If the index exceeds the array length, an error is returned. A negative index, starts from the end.

**Parameter**  
---  
**Name** | **Description**  
`indexExpr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An Expression evaluating to the index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new Expression representing the 'arrayGet' operation.  
**Example**
    
    
    typescript
    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    field('tags').arrayGet(field('favoriteTag'));
    

### arrayIndexOf(search)
    
    
    arrayIndexOf(search: unknown): FunctionExpression;

Returns the first index of the search value in the array, or -1 if not found.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `unknown`   
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
**Example**
    
    
    typescript
    // Get the first index of the value 3 in the 'myArray' field.
    field("myArray").arrayIndexOf(3);
    

### arrayIndexOf(search)
    
    
    arrayIndexOf(search: Expression): FunctionExpression;

Returns the first index of the search value in the array, or -1 if not found.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
**Example**
    
    
    typescript
    // Get the first index of the value in 'searchVal' field in the 'myArray' field.
    field("myArray").arrayIndexOf(field("searchVal"));
    

### arrayIndexOfAll(search)
    
    
    arrayIndexOfAll(search: unknown): FunctionExpression;

Returns all indices of the search value in the array.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `unknown`   
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the indices.  
**Example**
    
    
    typescript
    // Get all indices of the value 3 in the 'myArray' field.
    field("myArray").arrayIndexOfAll(3);
    

### arrayIndexOfAll(search)
    
    
    arrayIndexOfAll(search: Expression): FunctionExpression;

Returns all indices of the search value in the array.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the indices.  
**Example**
    
    
    typescript
    // Get all indices of the value in 'searchVal' field in the 'myArray' field.
    field("myArray").arrayIndexOfAll(field("searchVal"));
    

### arrayLast()
    
    
    arrayLast(): FunctionExpression;

Returns the last element of the array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last element.  
**Example**
    
    
    typescript
    // Get the last element of the 'myArray' field.
    field("myArray").arrayLast();
    

### arrayLastIndexOf(search)
    
    
    arrayLastIndexOf(search: unknown): FunctionExpression;

Returns the last index of the search value in the array, or -1 if not found.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `unknown`   
The value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
**Example**
    
    
    typescript
    // Get the last index of the value 3 in the 'myArray' field.
    field("myArray").arrayLastIndexOf(3);
    

### arrayLastIndexOf(search)
    
    
    arrayLastIndexOf(search: Expression): FunctionExpression;

Returns the last index of the search value in the array, or -1 if not found.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the value to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index.  
**Example**
    
    
    typescript
    // Get the last index of the value in 'searchVal' field in the 'myArray' field.
    field("myArray").arrayLastIndexOf(field("searchVal"));
    

### arrayLastN(n)
    
    
    arrayLastN(n: number): FunctionExpression;

Returns the last `n` elements of the array.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
**Example**
    
    
    typescript
    // Get the last 3 elements of the 'myArray' field.
    field("myArray").arrayLastN(3);
    

### arrayLastN(n)
    
    
    arrayLastN(n: Expression): FunctionExpression;

Returns the last `n` elements of the array.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the last `n` elements.  
**Example**
    
    
    typescript
    // Get the last n elements of the 'myArray' field.
    field("myArray").arrayLastN(field("count"));
    

### arrayLength()
    
    
    arrayLength(): FunctionExpression;

Creates an expression that calculates the length of an array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the array.  
**Example**
    
    
    typescript
    // Get the number of items in the 'cart' array
    field("cart").arrayLength();
    

### arrayMaximum()
    
    
    arrayMaximum(): FunctionExpression;

Returns the maximum value in the array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the maximum value.  
**Example**
    
    
    typescript
    // Get the maximum value of the 'myArray' field.
    field("myArray").arrayMaximum();
    

### arrayMaximumN(n)
    
    
    arrayMaximumN(n: number): FunctionExpression;

Returns the largest `n` elements of the array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
**Example**
    
    
    typescript
    // Get the largest 3 elements of the 'myArray' field.
    field("myArray").arrayMaximumN(3);
    

### arrayMaximumN(n)
    
    
    arrayMaximumN(n: Expression): FunctionExpression;

Returns the largest `n` elements of the array.

Note: Returns the n largest non-null elements in the array, in descending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the largest `n` elements.  
**Example**
    
    
    typescript
    // Get the largest n elements of the 'myArray' field.
    field("myArray").arrayMaximumN(field("count"));
    

### arrayMinimum()
    
    
    arrayMinimum(): FunctionExpression;

Returns the minimum value in the array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the minimum value.  
**Example**
    
    
    typescript
    // Get the minimum value of the 'myArray' field.
    field("myArray").arrayMinimum();
    

### arrayMinimumN(n)
    
    
    arrayMinimumN(n: number): FunctionExpression;

Returns the smallest `n` elements of the array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `number`   
The number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
**Example**
    
    
    typescript
    // Get the smallest 3 elements of the 'myArray' field.
    field("myArray").arrayMinimumN(3);
    

### arrayMinimumN(n)
    
    
    arrayMinimumN(n: Expression): FunctionExpression;

Returns the smallest `n` elements of the array.

Note: Returns the n smallest non-null elements in the array, in ascending order. This does not use a stable sort, meaning the order of equivalent elements is undefined.

**Parameter**  
---  
**Name** | **Description**  
`n` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression evaluating to the number of elements to return.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the smallest `n` elements.  
**Example**
    
    
    typescript
    // Get the smallest n elements of the 'myArray' field.
    field("myArray").arrayMinimumN(field("count"));
    

### arrayReverse()
    
    
    arrayReverse(): FunctionExpression;

Creates an expression that reverses an array.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed array.  
**Example**
    
    
    typescript
    // Reverse the value of the 'myArray' field.
    field("myArray").arrayReverse();
    

### arraySlice(offset, length)
    
    
    arraySlice(offset: number | Expression, length?: number | Expression): FunctionExpression;

Creates an expression that returns a slice of an array from `offset` with `length` elements.

**Parameters**  
---  
**Name** | **Description**  
`offset` |  `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The starting offset.  
`length` |  `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The optional length of the slice.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the sliced array.  
**Example**
    
    
    typescript
    // Get 5 elements from the 'items' array starting from index 2
    field("items").arraySlice(2, 5);
    
    // Get n number of elements from the 'items' array starting from index 2
    field("items").arraySlice(2, field("count"));
    

### arraySum()
    
    
    arraySum(): FunctionExpression;

Creates an expression that computes the sum of the elements in an array.
    
    
    // Compute the sum of the elements in the 'scores' field.
    field("scores").arraySum();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the sum of the elements in the array.  
  
### arrayTransform(elementAlias, transform)
    
    
    arrayTransform(elementAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array.

**Parameters**  
---  
**Name** | **Description**  
`elementAlias` |  `string`   
The variable name to use for each element.  
`transform` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The lambda expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the arrayTransform operation.  
**Example**
    
    
    typescript
    // Transform the 'scores' array by multiplying each score by 10
    field("scores").arrayTransform("score", multiply(variable("score"), 10));
    

### arrayTransformWithIndex(elementAlias, indexAlias, transform)
    
    
    arrayTransformWithIndex(elementAlias: string, indexAlias: string, transform: Expression): FunctionExpression;

Creates an expression that applies a provided transformation to each element in an array, providing the element's index to the transformation expression.

**Parameters**  
---  
**Name** | **Description**  
`elementAlias` |  `string`   
The variable name to use for each element.  
`indexAlias` |  `string`   
The variable name to use for the current index.  
`transform` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The lambda expression used to transform the elements.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the arrayTransformWithIndex operation.  
**Example**
    
    
    typescript
    // Transform the 'scores' array by adding the index to each score
    field("scores").arrayTransformWithIndex("score", "i", add(variable("score"), variable("i")));
    

### as(name)
    
    
    as(name: string): AliasedExpression;

Assigns an alias to this expression.

Aliases are useful for renaming fields in the output of a stage or for giving meaningful names to calculated values.
    
    
    // Calculate the total price and assign it the alias "totalPrice" and add it to the output.
    firestore.pipeline().collection("items")
      .addFields(field("price").multiply(field("quantity")).as("totalPrice"));
    

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The alias to assign to this expression.  
**Returns**  
---  
**Type** | **Description**  
`[AliasedExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aliasedexpression)` | A new `AliasedExpression` that wraps this expression and associates it with the provided alias.  
  
### asBoolean()
    
    
    asBoolean(): BooleanExpression;

Wraps the expression in a [BooleanExpression].

**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A `BooleanExpression` representing the same expression.  
  
### ascending()
    
    
    ascending(): Ordering;

Creates an `Ordering` that sorts documents in ascending order based on this expression.
    
    
    // Sort documents by the 'name' field in ascending order
    pipeline().collection("users")
      .sort(field("name").ascending());
    

**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for ascending sorting.  
  
### average()
    
    
    average(): AggregateFunction;

Creates an aggregation that calculates the average (mean) of a numeric field across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'average' aggregation.  
**Example**
    
    
    typescript
    // Calculate the average age of users
    field("age").average().as("averageAge");
    

### byteLength()
    
    
    byteLength(): FunctionExpression;

Creates an expression that calculates the length of this string expression in bytes.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string in bytes.  
**Example**
    
    
    typescript
    // Calculate the length of the 'myString' field in bytes.
    field("myString").byteLength();
    

### ceil()
    
    
    ceil(): FunctionExpression;

Creates an expression that computes the ceiling of a numeric value.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the ceiling of the numeric value.  
**Example**
    
    
    typescript
    // Compute the ceiling of the 'price' field.
    field("price").ceil();
    

### charLength()
    
    
    charLength(): FunctionExpression;

Creates an expression that calculates the character length of a string in UTF-8.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string.  
**Example**
    
    
    typescript
    // Get the character length of the 'name' field in its UTF-8 form.
    field("name").charLength();
    

### coalesce(replacement, others)
    
    
    coalesce(replacement: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

Creates an expression that returns the first non-null, non-absent argument, without evaluating the rest of the arguments. When all arguments are null or absent, returns the last argument.

**Parameters**  
---  
**Name** | **Description**  
`replacement` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`   
The value to use if this expression evaluates to null.  
`others` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
Optional additional values to check if previous values are null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new [Expression] representing the coalesce operation.  
**Example**
    
    
    typescript
    // Returns the value of the first non-null, non-absent field among 'preferredName', 'fullName',
    // or the last argument if all previous fields are null.
    field("preferredName").coalesce(field("fullName"), "Anonymous");
    

### collectionId()
    
    
    collectionId(): FunctionExpression;

Creates an expression that returns the collection ID from a path.
    
    
    // Get the collection ID from a path.
    field("__path__").collectionId();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the collectionId operation.  
  
### concat(second, others)
    
    
    concat(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

Creates an expression that concatenates expression results together.

**Parameters**  
---  
**Name** | **Description**  
`second` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`   
The additional expression or literal to concatenate.  
`others` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
Optional additional expressions or literals to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the concatenated value.  
**Example**
    
    
    typescript
    // Combine the 'firstName', ' ', and 'lastName' fields into a single value.
    field("firstName").concat(constant(" "), field("lastName"));
    

### cosineDistance(vectorExpression)
    
    
    cosineDistance(vectorExpression: Expression): FunctionExpression;

Calculates the cosine distance between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vectorExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The other vector (represented as an Expression) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the cosine distance between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    field("userVector").cosineDistance(field("itemVector"));
    

### cosineDistance(vector)
    
    
    cosineDistance(vector: firestore.VectorValue | number[]): FunctionExpression;

Calculates the Cosine distance between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vector` |  `FirebaseFirestore.VectorValue | number[]`   
The other vector (as a VectorValue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Cosine distance between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the Cosine distance between the 'location' field and a target location
    field("location").cosineDistance(new VectorValue([37.7749, -122.4194]));
    

### count()
    
    
    count(): AggregateFunction;

Creates an aggregation that counts the number of stage inputs with valid evaluations of the expression or field.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'count' aggregation.  
**Example**
    
    
    typescript
    // Count the total number of products
    field("productId").count().as("totalProducts");
    

### countDistinct()
    
    
    countDistinct(): AggregateFunction;

Creates an aggregation that counts the number of distinct values of the expression or field.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'count_distinct' aggregation.  
**Example**
    
    
    typescript
    // Count the distinct number of products
    field("productId").countDistinct().as("distinctProducts");
    

### descending()
    
    
    descending(): Ordering;

Creates an `Ordering` that sorts documents in descending order based on this expression.
    
    
    // Sort documents by the 'createdAt' field in descending order
    firestore.pipeline().collection("users")
      .sort(field("createdAt").descending());
    

**Returns**  
---  
**Type** | **Description**  
`[Ordering](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.ordering)` | A new `Ordering` for descending sorting.  
  
### divide(divisor)
    
    
    divide(divisor: Expression): FunctionExpression;

Creates an expression that divides this expression by another expression.

**Parameter**  
---  
**Name** | **Description**  
`divisor` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
**Example**
    
    
    typescript
    // Divide the 'total' field by the 'count' field
    field("total").divide(field("count"));
    

### divide(divisor)
    
    
    divide(divisor: number): FunctionExpression;

Creates an expression that divides this expression by a constant value.

**Parameter**  
---  
**Name** | **Description**  
`divisor` |  `number`   
The constant value to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the division operation.  
**Example**
    
    
    typescript
    // Divide the 'value' field by 10
    field("value").divide(10);
    

### documentId()
    
    
    documentId(): FunctionExpression;

Creates an expression that returns the document ID from a path.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the documentId operation.  
**Example**
    
    
    typescript
    // Get the document ID from a path.
    field("__path__").documentId();
    

### dotProduct(vectorExpression)
    
    
    dotProduct(vectorExpression: Expression): FunctionExpression;

Calculates the dot product between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vectorExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The other vector (as an array of numbers) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the dot product between a feature vector and a target vector
    field("features").dotProduct([0.5, 0.8, 0.2]);
    

### dotProduct(vector)
    
    
    dotProduct(vector: firestore.VectorValue | number[]): FunctionExpression;

Calculates the dot product between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vector` |  `FirebaseFirestore.VectorValue | number[]`   
The other vector (as an array of numbers) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the dot product between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the dot product between a feature vector and a target vector
    field("features").dotProduct(new VectorValue([0.5, 0.8, 0.2]));
    

### endsWith(suffix)
    
    
    endsWith(suffix: string): BooleanExpression;

Creates an expression that checks if a string ends with a given postfix.

**Parameter**  
---  
**Name** | **Description**  
`suffix` |  `string`   
The postfix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
**Example**
    
    
    typescript
    // Check if the 'filename' field ends with ".txt"
    field("filename").endsWith(".txt");
    

### endsWith(suffix)
    
    
    endsWith(suffix: Expression): BooleanExpression;

Creates an expression that checks if a string ends with a given postfix (represented as an expression).

**Parameter**  
---  
**Name** | **Description**  
`suffix` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The postfix expression to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'ends with' comparison.  
**Example**
    
    
    typescript
    // Check if the 'url' field ends with the value of the 'extension' field
    field("url").endsWith(field("extension"));
    

### equal(expression)
    
    
    equal(expression: Expression): BooleanExpression;

Creates an expression that checks if this expression is equal to another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for equality.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
**Example**
    
    
    typescript
    // Check if the 'age' field is equal to 21
    field("age").equal(21);
    

### equal(value)
    
    
    equal(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is equal to a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for equality.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the equality comparison.  
**Example**
    
    
    typescript
    // Check if the 'city' field is equal to "London"
    field("city").equal("London");
    

### equalAny(values)
    
    
    equalAny(values: Array<Expression | unknown>): BooleanExpression;

Creates an expression that checks if this expression is equal to any of the provided values or expressions.

**Parameter**  
---  
**Name** | **Description**  
`values` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
The values or expressions to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
**Example**
    
    
    typescript
    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    field("category").equalAny("Electronics", field("primaryType"));
    

### equalAny(arrayExpression)
    
    
    equalAny(arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if this expression is equal to any of the provided values or expressions.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression that evaluates to an array of values to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'IN' comparison.  
**Example**
    
    
    typescript
    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    field("category").equalAny(array(["Electronics", field("primaryType")]));
    

### euclideanDistance(vectorExpression)
    
    
    euclideanDistance(vectorExpression: Expression): FunctionExpression;

Calculates the Euclidean distance between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vectorExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The other vector (as an array of numbers) to calculate with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the Euclidean distance between the 'location' field and a target location
    field("location").euclideanDistance([37.7749, -122.4194]);
    

### euclideanDistance(vector)
    
    
    euclideanDistance(vector: firestore.VectorValue | number[]): FunctionExpression;

Calculates the Euclidean distance between two vectors.

**Parameter**  
---  
**Name** | **Description**  
`vector` |  `FirebaseFirestore.VectorValue | number[]`   
The other vector (as a VectorValue) to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the Euclidean distance between the two vectors.  
**Example**
    
    
    typescript
    // Calculate the Euclidean distance between the 'location' field and a target location
    field("location").euclideanDistance(new VectorValue([37.7749, -122.4194]));
    

### exists()
    
    
    exists(): BooleanExpression;

Creates an expression that checks if a field exists in the document.

**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'exists' check.  
**Example**
    
    
    typescript
    // Check if the document has a field named "phoneNumber"
    field("phoneNumber").exists();
    

### exp()
    
    
    exp(): FunctionExpression;

Creates an expression that computes e to the power of this expression.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the exp of the numeric value.  
**Example**
    
    
    typescript
    // Compute e to the power of the 'value' field.
    field("value").exp();
    

### first()
    
    
    first(): AggregateFunction;

Creates an aggregation that finds the first value of an expression across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'first' aggregation.  
**Example**
    
    
    typescript
    // Find the first value of the 'rating' field
    field("rating").first().as("firstRating");
    

### floor()
    
    
    floor(): FunctionExpression;

Creates an expression that computes the floor of a numeric value.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the floor of the numeric value.  
**Example**
    
    
    typescript
    // Compute the floor of the 'price' field.
    field("price").floor();
    

### getField(key)
    
    
    getField(key: string | Expression): Expression;

Creates an expression that returns the value of a field from the document that results from the evaluation of this expression.

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The field to access in the document.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new `Expression` representing the value of the field in the document.  
**Example**
    
    
    typescript
    // Get the value of the "city" field in the "address" document.
    field("address").getField("city")
    

### greaterThan(expression)
    
    
    greaterThan(expression: Expression): BooleanExpression;

Creates an expression that checks if this expression is greater than another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for greater than.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
**Example**
    
    
    typescript
    // Check if the 'age' field is greater than the 'limit' field
    field("age").greaterThan(field("limit"));
    

### greaterThan(value)
    
    
    greaterThan(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is greater than a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for greater than.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than comparison.  
**Example**
    
    
    typescript
    // Check if the 'price' field is greater than 100
    field("price").greaterThan(100);
    

### greaterThanOrEqual(expression)
    
    
    greaterThanOrEqual(expression: Expression): BooleanExpression;

Creates an expression that checks if this expression is greater than or equal to another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for greater than or equal to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
**Example**
    
    
    typescript
    // Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
    field("quantity").greaterThanOrEqual(field('requirement').add(1));
    

### greaterThanOrEqual(value)
    
    
    greaterThanOrEqual(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is greater than or equal to a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for greater than or equal to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the greater than or equal to comparison.  
**Example**
    
    
    typescript
    // Check if the 'score' field is greater than or equal to 80
    field("score").greaterThanOrEqual(80);
    

### ifAbsent(elseValue)
    
    
    ifAbsent(elseValue: unknown): Expression;

Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of the this expression evaluation.
    
    
    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    field("optional_field").ifAbsent("default_value")
    

**Parameter**  
---  
**Name** | **Description**  
`elseValue` |  `unknown`   
The value that will be returned if this Expression evaluates to an absent value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new [Expression] representing the ifAbsent operation.  
  
### ifAbsent(elseExpression)
    
    
    ifAbsent(elseExpression: unknown): Expression;

Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of this expression evaluation.
    
    
    // Returns the value of the optional field 'optional_field', or if that is
    // absent, then returns the value of the field `
    field("optional_field").ifAbsent(field('default_field'))
    

**Parameter**  
---  
**Name** | **Description**  
`elseExpression` |  `unknown`   
The Expression that will be evaluated if this Expression evaluates to an absent value.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new [Expression] representing the ifAbsent operation.  
  
### ifError(catchExpr)
    
    
    ifError(catchExpr: Expression): FunctionExpression;

Creates an expression that returns the result of the `catchExpr` argument if there is an error, else return the result of this expression.

**Parameter**  
---  
**Name** | **Description**  
`catchExpr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The catch expression that will be evaluated and returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the 'ifError' operation.  
**Example**
    
    
    typescript
    // Returns the first item in the title field arrays, or returns
    // the entire title field if the array is empty or the field is another type.
    field("title").arrayGet(0).ifError(field("title"));
    

### ifError(catchValue)
    
    
    ifError(catchValue: unknown): FunctionExpression;

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.
    
    
    // Returns the first item in the title field arrays, or returns
    // "Default Title"
    field("title").arrayGet(0).ifError("Default Title");
    

**Parameter**  
---  
**Name** | **Description**  
`catchValue` |  `unknown`   
The value that will be returned if this expression produces an error.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the 'ifError' operation.  
  
### ifNull(elseExpression)
    
    
    ifNull(elseExpression: Expression): FunctionExpression;

Creates an expression that returns the `elseValue` argument if this expression evaluates to null, else return the result of this expression evaluation.

**Parameter**  
---  
**Name** | **Description**  
`elseExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The Expression that will be evaluated if this Expression evaluates to null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new [Expression] representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

**Example**
    
    
    typescript
    // Returns the user's preferred name, or if that is null, returns their full name.
    field("preferredName").ifNull(field("fullName"))
    

### ifNull(elseValue)
    
    
    ifNull(elseValue: unknown): FunctionExpression;

Creates an expression that returns the `elseValue` argument if this expression evaluates to null, else return the result of this expression evaluation.

**Parameter**  
---  
**Name** | **Description**  
`elseValue` |  `unknown`   
The value that will be returned if this Expression evaluates to null.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new [Expression] representing the ifNull operation.  
**Remarks**

This function provides a fallback for both absent and explicit null values. In contrast, only triggers for missing fields.

**Example**
    
    
    typescript
    // Returns the user's display name, or returns "Anonymous" if the field is null.
    field("displayName").ifNull("Anonymous")
    

### isAbsent()
    
    
    isAbsent(): BooleanExpression;

Creates an expression that returns `true` if the result of this expression is absent. Otherwise, returns `false` even if the value is `null`.
    
    
    // Check if the field `value` is absent.
    field("value").isAbsent();
    

**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `BooleanExpression` representing the 'isAbsent' check.  
  
### isError()
    
    
    isError(): BooleanExpression;

Creates an expression that checks if a given expression produces an error.

**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `BooleanExpression` representing the 'isError' check.  
**Example**
    
    
    typescript
    // Check if the result of a calculation is an error
    field("title").arrayContains(1).isError();
    

### isType(type)
    
    
    isType(type: string): BooleanExpression;

Creates an expression that checks if the result of this expression is of the given type.

**Parameter**  
---  
**Name** | **Description**  
`type` |  `string`   
The type to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `BooleanExpression` that evaluates to true if the expression's result is of the given type, false otherwise.  
**Remarks**

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data. Supported values for `type` are: `'null'`, `'array'`, `'boolean'`, `'bytes'`, `'timestamp'`, `'geo_point'`, `'number'`, `'int32'`, `'int64'`, `'float64'`, `'decimal128'`, `'map'`, `'reference'`, `'string'`, `'vector'`, `'max_key'`, `'min_key'`, `'object_id'`, `'regex'`, `'request_timestamp'`.

**Example**
    
    
    typescript
    // Check if the 'price' field is specifically an integer (not just 'number')
    field('price').isType('int64');
    

### join(delimiterExpression)
    
    
    join(delimiterExpression: Expression): Expression;

Creates an expression that joins the elements of an array into a string.
    
    
    // Join the elements of the 'tags' field with the delimiter from the 'separator' field.
    field("tags").join(field("separator"))
    

**Parameter**  
---  
**Name** | **Description**  
`delimiterExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression that evaluates to the delimiter string.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### join(delimiter)
    
    
    join(delimiter: string): Expression;

Creates an expression that joins the elements of an array field into a string.
    
    
    // Join the elements of the 'tags' field with a comma and space.
    field("tags").join(", ")
    

**Parameter**  
---  
**Name** | **Description**  
`delimiter` |  `string`   
The string to use as a delimiter.  
**Returns**  
---  
**Type** | **Description**  
`[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)` | A new Expression representing the join operation.  
  
### last()
    
    
    last(): AggregateFunction;

Creates an aggregation that finds the last value of an expression across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'last' aggregation.  
**Example**
    
    
    typescript
    // Find the last value of the 'rating' field
    field("rating").last().as("lastRating");
    

### length()
    
    
    length(): FunctionExpression;

Creates an expression that calculates the length of a string, array, map, vector, or bytes.
    
    
    // Get the length of the 'name' field.
    field("name").length();
    
    // Get the number of items in the 'cart' array.
    field("cart").length();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the string, array, map, vector, or bytes.  
  
### lessThan(experession)
    
    
    lessThan(experession: Expression): BooleanExpression;

Creates an expression that checks if this expression is less than another expression.

**Parameter**  
---  
**Name** | **Description**  
`experession` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for less than.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
**Example**
    
    
    typescript
    // Check if the 'age' field is less than 'limit'
    field("age").lessThan(field('limit'));
    

### lessThan(value)
    
    
    lessThan(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is less than a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for less than.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than comparison.  
**Example**
    
    
    typescript
    // Check if the 'price' field is less than 50
    field("price").lessThan(50);
    

### lessThanOrEqual(expression)
    
    
    lessThanOrEqual(expression: Expression): BooleanExpression;

Creates an expression that checks if this expression is less than or equal to another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for less than or equal to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
**Example**
    
    
    typescript
    // Check if the 'quantity' field is less than or equal to 20
    field("quantity").lessThanOrEqual(constant(20));
    

### lessThanOrEqual(value)
    
    
    lessThanOrEqual(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is less than or equal to a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for less than or equal to.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the less than or equal to comparison.  
**Example**
    
    
    typescript
    // Check if the 'score' field is less than or equal to 70
    field("score").lessThanOrEqual(70);
    

### like(pattern)
    
    
    like(pattern: string): BooleanExpression;

Creates an expression that performs a case-sensitive string comparison.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `string`   
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
**Example**
    
    
    typescript
    // Check if the 'title' field contains the word "guide" (case-sensitive)
    field("title").like("%guide%");
    

### like(pattern)
    
    
    like(pattern: Expression): BooleanExpression;

Creates an expression that performs a case-sensitive string comparison.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The pattern to search for. You can use "%" as a wildcard character.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'like' comparison.  
**Example**
    
    
    typescript
    // Check if the 'title' field contains the word "guide" (case-sensitive)
    field("title").like("%guide%");
    

### ln()
    
    
    ln(): FunctionExpression;

Creates an expression that computes the natural logarithm of a numeric value.
    
    
    // Compute the natural logarithm of the 'value' field.
    field("value").ln();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the natural logarithm of the numeric value.  
  
### log10()
    
    
    log10(): FunctionExpression;

Creates an expression that computes the base-10 logarithm of a numeric value.
    
    
    // Compute the base-10 logarithm of the 'value' field.
    field("value").log10();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the base-10 logarithm of the numeric value.  
  
### logicalMaximum(second, others)
    
    
    logicalMaximum(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

Creates an expression that returns the larger value between this expression and another expression, based on Firestore's value type ordering.

**Parameters**  
---  
**Name** | **Description**  
`second` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`   
The second expression or literal to compare with.  
`others` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
Optional additional expressions or literals to compare with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical max operation.  
**Example**
    
    
    typescript
    // Returns the larger value between the 'timestamp' field and the current timestamp.
    field("timestamp").logicalMaximum(Function.currentTimestamp());
    

### logicalMinimum(second, others)
    
    
    logicalMinimum(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

Creates an expression that returns the smaller value between this expression and another expression, based on Firestore's value type ordering.

**Parameters**  
---  
**Name** | **Description**  
`second` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown`   
The second expression or literal to compare with.  
`others` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
Optional additional expressions or literals to compare with.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the logical min operation.  
**Example**
    
    
    typescript
    // Returns the smaller value between the 'timestamp' field and the current timestamp.
    field("timestamp").logicalMinimum(Function.currentTimestamp());
    

### ltrim(valueToTrim)
    
    
    ltrim(valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Parameter**  
---  
**Name** | **Description**  
`valueToTrim` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string.  
**Example**
    
    
    typescript
    // Trim whitespace from the beginning of the 'userInput' field
    field("userInput").ltrim();
    
    // Trim quotes from the beginning of the 'userInput' field
    field("userInput").ltrim('"');
    

### mapEntries()
    
    
    mapEntries(): FunctionExpression;

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the entries of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Example**
    
    
    typescript
    // Get the entries of the 'address' map
    field("address").mapEntries();
    

### mapGet(subfield)
    
    
    mapGet(subfield: string): FunctionExpression;

Accesses a value from a map (object) field using the provided key.

**Parameter**  
---  
**Name** | **Description**  
`subfield` |  `string`   
The key to access in the map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the value associated with the given key in the map.  
**Example**
    
    
    typescript
    // Get the 'city' value from the 'address' map field
    field("address").mapGet("city");
    

### mapKeys()
    
    
    mapKeys(): FunctionExpression;

Creates an expression that returns the keys of a map.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the keys of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Example**
    
    
    typescript
    // Get the keys of the 'address' map
    field("address").mapKeys();
    

### mapMerge(secondMap, otherMaps)
    
    
    mapMerge(secondMap: Record<string, unknown> | Expression, ...otherMaps: Array<Record<string, unknown> | Expression>): FunctionExpression;

Creates an expression that merges multiple map values.
    
    
    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    field('settings').mapMerge({ enabled: true }, conditional(field('isAdmin'), { admin: true}, {})
    

**Parameters**  
---  
**Name** | **Description**  
`secondMap` |  `Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
A required second map to merge. Represented as a literal or an expression that returns a map.  
`otherMaps` |  `Array<Record<string, unknown> | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)>`   
Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `FirestoreFunction` representing the 'mapMerge' operation.  
  
### mapRemove(key)
    
    
    mapRemove(key: string): FunctionExpression;

Creates an expression that removes a key from the map produced by evaluating this expression.
    
    
    // Removes the key 'baz' from the input map.
    map({foo: 'bar', baz: true}).mapRemove('baz');
    

**Parameter**  
---  
**Name** | **Description**  
`key` |  `string`   
The name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `FirestoreFunction` representing the 'mapRemove' operation.  
  
### mapRemove(keyExpr)
    
    
    mapRemove(keyExpr: Expression): FunctionExpression;

Creates an expression that removes a key from the map produced by evaluating this expression.
    
    
    // Removes the key 'baz' from the input map.
    map({foo: 'bar', baz: true}).mapRemove(constant('baz'));
    

**Parameter**  
---  
**Name** | **Description**  
`keyExpr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression that produces the name of the key to remove from the input map.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `FirestoreFunction` representing the 'mapRemove' operation.  
  
### mapSet(key, value, moreKeyValues)
    
    
    mapSet(key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

Creates an expression that returns a new map with the specified entries added or updated.

**Parameters**  
---  
**Name** | **Description**  
`key` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The key to set. Must be a string or a constant string expression.  
`value` |  `unknown`   
The value to set.  
`moreKeyValues` |  `unknown[]`   
Additional key-value pairs to set.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the map with the entries set.  
**Remarks**

Note that `mapSet` only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

**Example**
    
    
    typescript
    // Set the 'city' to "San Francisco" in the 'address' map
    field("address").mapSet("city", "San Francisco");
    

### mapValues()
    
    
    mapValues(): FunctionExpression;

Creates an expression that returns the values of a map.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the values of the map.  
**Remarks**

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Example**
    
    
    typescript
    // Get the values of the 'address' map
    field("address").mapValues();
    

### maximum()
    
    
    maximum(): AggregateFunction;

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'max' aggregation.  
**Example**
    
    
    typescript
    // Find the highest score in a leaderboard
    field("score").maximum().as("highestScore");
    

### minimum()
    
    
    minimum(): AggregateFunction;

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'min' aggregation.  
**Example**
    
    
    typescript
    // Find the lowest price of all products
    field("price").minimum().as("lowestPrice");
    

### mod(expression)
    
    
    mod(expression: Expression): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing this expression by another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
**Example**
    
    
    typescript
    // Calculate the remainder of dividing the 'value' field by the 'divisor' field
    field("value").mod(field("divisor"));
    

### mod(value)
    
    
    mod(value: number): FunctionExpression;

Creates an expression that calculates the modulo (remainder) of dividing this expression by a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `number`   
The constant value to divide by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the modulo operation.  
**Example**
    
    
    typescript
    // Calculate the remainder of dividing the 'value' field by 10
    field("value").mod(10);
    

### multiply(second, others)
    
    
    multiply(second: Expression | number, ...others: Array<Expression | number>): FunctionExpression;

Creates an expression that multiplies this expression by another expression.

**Parameters**  
---  
**Name** | **Description**  
`second` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | number`   
The second expression or literal to multiply by.  
`others` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | number>`   
Optional additional expressions or literals to multiply by.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the multiplication operation.  
**Example**
    
    
    typescript
    // Multiply the 'quantity' field by the 'price' field
    field("quantity").multiply(field("price"));
    

### notEqual(expression)
    
    
    notEqual(expression: Expression): BooleanExpression;

Creates an expression that checks if this expression is not equal to another expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to compare for inequality.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
**Example**
    
    
    typescript
    // Check if the 'status' field is not equal to "completed"
    field("status").notEqual("completed");
    

### notEqual(value)
    
    
    notEqual(value: unknown): BooleanExpression;

Creates an expression that checks if this expression is not equal to a constant value.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `unknown`   
The constant value to compare for inequality.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the inequality comparison.  
**Example**
    
    
    typescript
    // Check if the 'country' field is not equal to "USA"
    field("country").notEqual("USA");
    

### notEqualAny(values)
    
    
    notEqualAny(values: Array<Expression | unknown>): BooleanExpression;

Creates an expression that checks if this expression is not equal to any of the provided values or expressions.

**Parameter**  
---  
**Name** | **Description**  
`values` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | unknown>`   
The values or expressions to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NotEqAny' comparison.  
**Example**
    
    
    typescript
    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    field("status").notEqualAny(["pending", field("rejectedStatus")]);
    

### notEqualAny(arrayExpression)
    
    
    notEqualAny(arrayExpression: Expression): BooleanExpression;

Creates an expression that checks if this expression is not equal to any of the values in the evaluated expression.

**Parameter**  
---  
**Name** | **Description**  
`arrayExpression` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The values or expressions to check against.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'NotEqAny' comparison.  
**Example**
    
    
    typescript
    // Check if the 'status' field is not equal to any value in the field 'rejectedStatuses'
    field("status").notEqualAny(field('rejectedStatuses'));
    

### parent()
    
    
    parent(): FunctionExpression;

Creates an expression that returns the parent document of a document reference.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the parent operation.  
**Example**
    
    
    typescript
    // Get the parent document of a document reference.
    field("__path__").parent();
    

### pow(exponent)
    
    
    pow(exponent: Expression): FunctionExpression;

Creates an expression that returns the value of this expression raised to the power of another expression.
    
    
    // Raise the value of the 'base' field to the power of the 'exponent' field.
    field("base").pow(field("exponent"));
    

**Parameter**  
---  
**Name** | **Description**  
`exponent` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression to raise this expression to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### pow(exponent)
    
    
    pow(exponent: number): FunctionExpression;

Creates an expression that returns the value of this expression raised to the power of a constant value.
    
    
    // Raise the value of the 'base' field to the power of 2.
    field("base").pow(2);
    

**Parameter**  
---  
**Name** | **Description**  
`exponent` |  `number`   
The constant value to raise this expression to the power of.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the power operation.  
  
### regexContains(pattern)
    
    
    regexContains(pattern: string): BooleanExpression;

Creates an expression that checks if a string contains a specified regular expression as a substring.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `string`   
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'description' field contains "example" (case-insensitive)
    field("description").regexContains("(?i)example");
    

### regexContains(pattern)
    
    
    regexContains(pattern: Expression): BooleanExpression;

Creates an expression that checks if a string contains a specified regular expression as a substring.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The regular expression to use for the search.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'description' field contains the regular expression stored in field 'regex'
    field("description").regexContains(field("regex"));
    

### regexFind(pattern)
    
    
    regexFind(pattern: string): FunctionExpression;

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `string`   
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
**Example**
    
    
    typescript
    // Extract the domain from an email address
    field("email").regexFind("@.+")
    

### regexFind(pattern)
    
    
    regexFind(pattern: Expression): FunctionExpression;

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the regular expression find function.  
**Example**
    
    
    typescript
    // Extract the domain from an email address
    field("email").regexFind(field("domain"))
    

### regexFindAll(pattern)
    
    
    regexFindAll(pattern: string): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `string`   
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
**Example**
    
    
    typescript
    // Extract all hashtags from a post content field
    field("content").regexFindAll("#[A-Za-z0-9_]+")
    

### regexFindAll(pattern)
    
    
    regexFindAll(pattern: Expression): FunctionExpression;

Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The regular expression to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` that evaluates to an array of matched substrings.  
**Example**
    
    
    typescript
    // Extract all names from a post content field
    field("content").regexFindAll(field("names"))
    

### regexMatch(pattern)
    
    
    regexMatch(pattern: string): BooleanExpression;

Creates an expression that checks if a string matches a specified regular expression.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `string`   
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
**Example**
    
    
    typescript
    // Check if the 'email' field matches a valid email pattern
    field("email").regexMatch("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");
    

### regexMatch(pattern)
    
    
    regexMatch(pattern: Expression): BooleanExpression;

Creates an expression that checks if a string matches a specified regular expression.

**Parameter**  
---  
**Name** | **Description**  
`pattern` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The regular expression to use for the match.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the regular expression match.  
**Example**
    
    
    typescript
    // Check if the 'email' field matches a regular expression stored in field 'regex'
    field("email").regexMatch(field("regex"));
    

### reverse()
    
    
    reverse(): FunctionExpression;

Creates an expression that reverses this string or bytes expression.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string or bytes.  
**Example**
    
    
    typescript
    // Reverse the value of the 'myString' field.
    field("myString").reverse();
    

### round()
    
    
    round(): FunctionExpression;

Creates an expression that rounds a numeric value to the nearest whole number.
    
    
    // Round the value of the 'price' field.
    field("price").round();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the rounded value.  
  
### round(decimalPlaces)
    
    
    round(decimalPlaces: number): FunctionExpression;

Creates an expression that rounds a numeric value to the specified number of decimal places.
    
    
    // Round the value of the 'price' field to two decimal places.
    field("price").round(2);
    

**Parameter**  
---  
**Name** | **Description**  
`decimalPlaces` |  `number`   
A constant specifying the rounding precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the rounded value.  
  
### round(decimalPlaces)
    
    
    round(decimalPlaces: Expression): FunctionExpression;

Creates an expression that rounds a numeric value to the specified number of decimal places.
    
    
    // Round the value of the 'price' field to two decimal places.
    field("price").round(constant(2));
    

**Parameter**  
---  
**Name** | **Description**  
`decimalPlaces` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression specifying the rounding precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the rounded value.  
  
### rtrim(valueToTrim)
    
    
    rtrim(valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Parameter**  
---  
**Name** | **Description**  
`valueToTrim` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the trimmed string or byte array.  
**Example**
    
    
    typescript
    // Trim whitespace from the end of the 'userInput' field
    field("userInput").rtrim();
    
    // Trim quotes from the end of the 'userInput' field
    field("userInput").rtrim('"');
    

### split(delimiter)
    
    
    split(delimiter: string): FunctionExpression;

Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter.

**Parameter**  
---  
**Name** | **Description**  
`delimiter` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
**Example**
    
    
    typescript
    // Split the 'scoresCsv' field on delimiter ','
    field('scoresCsv').split(',')
    

### split(delimiter)
    
    
    split(delimiter: Expression): FunctionExpression;

Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter.

**Parameter**  
---  
**Name** | **Description**  
`delimiter` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the split function.  
**Example**
    
    
    typescript
    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    field('scores').split(conditional(field('format').equal('csv'), constant(','), constant(':'))
    

### sqrt()
    
    
    sqrt(): FunctionExpression;

Creates an expression that computes the square root of a numeric value.
    
    
    // Compute the square root of the 'value' field.
    field("value").sqrt();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the square root of the numeric value.  
  
### startsWith(prefix)
    
    
    startsWith(prefix: string): BooleanExpression;

Creates an expression that checks if a string starts with a given prefix.

**Parameter**  
---  
**Name** | **Description**  
`prefix` |  `string`   
The prefix to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
**Example**
    
    
    typescript
    // Check if the 'name' field starts with "Mr."
    field("name").startsWith("Mr.");
    

### startsWith(prefix)
    
    
    startsWith(prefix: Expression): BooleanExpression;

Creates an expression that checks if a string starts with a given prefix (represented as an expression).

**Parameter**  
---  
**Name** | **Description**  
`prefix` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The prefix expression to check for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'starts with' comparison.  
**Example**
    
    
    typescript
    // Check if the 'fullName' field starts with the value of the 'firstName' field
    field("fullName").startsWith(field("firstName"));
    

### stringConcat(secondString, otherStrings)
    
    
    stringConcat(secondString: Expression | string, ...otherStrings: Array<Expression | string>): FunctionExpression;

Creates an expression that concatenates string expressions together.

**Parameters**  
---  
**Name** | **Description**  
`secondString` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string`   
The additional expression or string literal to concatenate.  
`otherStrings` |  `Array<[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | string>`   
Optional additional expressions or string literals to concatenate.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the concatenated string.  
**Example**
    
    
    typescript
    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    field("firstName").stringConcat(constant(" "), field("lastName"));
    

### stringContains(substring)
    
    
    stringContains(substring: string): BooleanExpression;

Creates an expression that checks if a string contains a specified substring.

**Parameter**  
---  
**Name** | **Description**  
`substring` |  `string`   
The substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'description' field contains "example".
    field("description").stringContains("example");
    

### stringContains(expr)
    
    
    stringContains(expr: Expression): BooleanExpression;

Creates an expression that checks if a string contains the string represented by another expression.

**Parameter**  
---  
**Name** | **Description**  
`expr` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression representing the substring to search for.  
**Returns**  
---  
**Type** | **Description**  
`[BooleanExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.booleanexpression)` | A new `Expression` representing the 'contains' comparison.  
**Example**
    
    
    typescript
    // Check if the 'description' field contains the value of the 'keyword' field.
    field("description").stringContains(field("keyword"));
    

### stringIndexOf(search)
    
    
    stringIndexOf(search: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Parameter**  
---  
**Name** | **Description**  
`search` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
The substring or byte sequence to search for.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the index of the first occurrence.  
**Example**
    
    
    typescript
    // Find the index of "foo" in the 'text' field
    field("text").stringIndexOf("foo");
    

### stringRepeat(repetitions)
    
    
    stringRepeat(repetitions: number | Expression): FunctionExpression;

Creates an expression that repeats a string or byte array a specified number of times.

**Parameter**  
---  
**Name** | **Description**  
`repetitions` |  `number | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The number of times to repeat the string or byte array.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the repeated string or byte array.  
**Example**
    
    
    typescript
    // Repeat the 'label' field 3 times
    field("label").stringRepeat(3);
    

### stringReplaceAll(find, replacement)
    
    
    stringReplaceAll(find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`find` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
The substring or byte sequence to search for.  
`replacement` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the string or byte array with replacements.  
**Example**
    
    
    typescript
    // Replace all occurrences of "foo" with "bar" in the 'text' field
    field("text").stringReplaceAll("foo", "bar");
    

### stringReplaceOne(find, replacement)
    
    
    stringReplaceOne(find: string | Expression | Uint8Array | Buffer, replacement: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Parameters**  
---  
**Name** | **Description**  
`find` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
The substring or byte sequence to search for.  
`replacement` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
The replacement string or byte sequence.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the string or byte array with the replacement.  
**Example**
    
    
    typescript
    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    field("text").stringReplaceOne("foo", "bar");
    

### stringReverse()
    
    
    stringReverse(): FunctionExpression;

Creates an expression that reverses a string.
    
    
    // Reverse the value of the 'myString' field.
    field("myString").stringReverse();
    

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the reversed string.  
  
### substring(position, length)
    
    
    substring(position: number, length?: number): FunctionExpression;

Creates an expression that returns a substring of the results of this expression.

**Parameters**  
---  
**Name** | **Description**  
`position` |  `number`   
Index of the first character of the substring.  
`length` |  `number`   
Length of the substring. If not provided, the substring will end at the end of the input.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### substring(position, length)
    
    
    substring(position: Expression, length?: Expression): FunctionExpression;

Creates an expression that returns a substring of the results of this expression.

**Parameters**  
---  
**Name** | **Description**  
`position` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression returning the index of the first character of the substring.  
`length` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression returning the length of the substring. If not provided the substring will end at the end of the input.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` |   
  
### subtract(subtrahend)
    
    
    subtract(subtrahend: firestore.Pipelines.Expression): FunctionExpression;

Creates an expression that subtracts another expression from this expression.

**Parameter**  
---  
**Name** | **Description**  
`subtrahend` |  `firestore.Pipelines.Expression`   
The expression to subtract from this expression.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
**Example**
    
    
    typescript
    // Subtract the 'discount' field from the 'price' field
    field("price").subtract(field("discount"));
    

### subtract(subtrahend)
    
    
    subtract(subtrahend: number): FunctionExpression;

Creates an expression that subtracts a constant value from this expression.

**Parameter**  
---  
**Name** | **Description**  
`subtrahend` |  `number`   
The constant value to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the subtraction operation.  
**Example**
    
    
    typescript
    // Subtract 20 from the value of the 'total' field
    field("total").subtract(20);
    

### sum()
    
    
    sum(): AggregateFunction;

Creates an aggregation that calculates the sum of a numeric field across multiple stage inputs.

**Returns**  
---  
**Type** | **Description**  
`[AggregateFunction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.aggregatefunction)` | A new `AggregateFunction` representing the 'sum' aggregation.  
**Example**
    
    
    typescript
    // Calculate the total revenue from a set of orders
    field("orderAmount").sum().as("totalRevenue");
    

### timestampAdd(unit, amount)
    
    
    timestampAdd(unit: Expression, amount: Expression): FunctionExpression;

Creates an expression that adds a specified amount of time to this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`unit` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'.  
`amount` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluates to amount of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
**Example**
    
    
    typescript
    // Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
    field("timestamp").timestampAdd(field("unit"), field("amount"));
    

### timestampAdd(unit, amount)
    
    
    timestampAdd(unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that adds a specified amount of time to this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`unit` |  `firestore.Pipelines.TimeUnit`   
The unit of time to add (e.g., "day", "hour").  
`amount` |  `number`   
The amount of time to add.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
**Example**
    
    
    typescript
    // Add 1 day to the 'timestamp' field.
    field("timestamp").timestampAdd("day", 1);
    

### timestampDiff(start, unit)
    
    
    timestampDiff(start: Expression, unit: Expression): FunctionExpression;

Creates an expression that calculates the difference between this timestamp and another timestamp.

**Parameters**  
---  
**Name** | **Description**  
`start` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluating to the starting timestamp.  
`unit` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluates to a unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
**Example**
    
    
    typescript
    // Calculate the difference determined by fields 'startTime' and 'unit'.
    field("endTime").timestampDiff(field("startTime"), field("unit"));
    

### timestampDiff(start, unit)
    
    
    timestampDiff(start: string | Expression, unit: firestore.Pipelines.TimeUnit): FunctionExpression;

Creates an expression that calculates the difference between this timestamp and another timestamp.

**Parameters**  
---  
**Name** | **Description**  
`start` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The field name of the starting timestamp or an expression evaluating to a timestamp.  
`unit` |  `firestore.Pipelines.TimeUnit`   
The unit of time for the difference (e.g., "day", "hour").  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the difference as an integer.  
**Example**
    
    
    typescript
    // Calculate the difference in days between 'endTime' and 'startTime' fields.
    field("endTime").timestampDiff("startTime", "day");
    

### timestampExtract(part, timezone)
    
    
    timestampExtract(part: firestore.Pipelines.TimePart, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`part` |  `firestore.Pipelines.TimePart`   
The part to extract from the timestamp (e.g., "year", "month", "day").  
`timezone` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
**Example**
    
    
    typescript
    // Extract the year from the 'createdAt' field.
    field('createdAt').timestampExtract('year')
    

### timestampExtract(part, timezone)
    
    
    timestampExtract(part: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that extracts a specified part from this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`part` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluating to the part to extract.  
`timezone` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The timezone to use for extraction. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1." Defaults to "UTC" if not specified.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the extracted part as an integer.  
**Example**
    
    
    typescript
    // Extract the part specified by the field 'extractionPart' from 'createdAt'.
    field('createdAt').timestampExtract(field('extractionPart'))
    

### timestampSubtract(unit, amount)
    
    
    timestampSubtract(unit: Expression, amount: Expression): FunctionExpression;

Creates an expression that subtracts a specified amount of time from this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`unit` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'.  
`amount` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The expression evaluates to amount of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
**Example**
    
    
    typescript
    // Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
    field("timestamp").timestampSubtract(field("unit"), field("amount"));
    

### timestampSubtract(unit, amount)
    
    
    timestampSubtract(unit: firestore.Pipelines.TimeUnit, amount: number): FunctionExpression;

Creates an expression that subtracts a specified amount of time from this timestamp expression.

**Parameters**  
---  
**Name** | **Description**  
`unit` |  `firestore.Pipelines.TimeUnit`   
The unit of time to subtract (e.g., "day", "hour").  
`amount` |  `number`   
The amount of time to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the resulting timestamp.  
**Example**
    
    
    typescript
    // Subtract 1 day from the 'timestamp' field.
    field("timestamp").timestampSubtract("day", 1);
    

### timestampToUnixMicros()
    
    
    timestampToUnixMicros(): FunctionExpression;

Creates an expression that converts this timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of microseconds since epoch.  
**Example**
    
    
    typescript
    // Convert the 'timestamp' field to microseconds since epoch.
    field("timestamp").timestampToUnixMicros();
    

### timestampToUnixMillis()
    
    
    timestampToUnixMillis(): FunctionExpression;

Creates an expression that converts this timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of milliseconds since epoch.  
**Example**
    
    
    typescript
    // Convert the 'timestamp' field to milliseconds since epoch.
    field("timestamp").timestampToUnixMillis();
    

### timestampToUnixSeconds()
    
    
    timestampToUnixSeconds(): FunctionExpression;

Creates an expression that converts this timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the number of seconds since epoch.  
**Example**
    
    
    typescript
    // Convert the 'timestamp' field to seconds since epoch.
    field("timestamp").timestampToUnixSeconds();
    

### timestampTruncate(granularity, timezone)
    
    
    timestampTruncate(granularity: firestore.Pipelines.TimeGranularity, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`granularity` |  `firestore.Pipelines.TimeGranularity`   
The granularity to truncate to.  
`timezone` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
**Example**
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the beginning of the day.
    field('createdAt').timestampTruncate('day')
    

### timestampTruncate(granularity, timezone)
    
    
    timestampTruncate(granularity: Expression, timezone?: string | Expression): FunctionExpression;

Creates an expression that truncates a timestamp to a specified granularity.

**Parameters**  
---  
**Name** | **Description**  
`granularity` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The granularity to truncate to.  
`timezone` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1".  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the truncated timestamp.  
**Example**
    
    
    typescript
    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    field('createdAt').timestampTruncate(field('granularity'))
    

### toLower()
    
    
    toLower(): FunctionExpression;

Creates an expression that converts a string to lowercase.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the lowercase string.  
**Example**
    
    
    typescript
    // Convert the 'name' field to lowercase
    field("name").toLower();
    

### toUpper()
    
    
    toUpper(): FunctionExpression;

Creates an expression that converts a string to uppercase.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the uppercase string.  
**Example**
    
    
    typescript
    // Convert the 'title' field to uppercase
    field("title").toUpper();
    

### trim(valueToTrim)
    
    
    trim(valueToTrim?: string | Expression | Uint8Array | Buffer): FunctionExpression;

Creates an expression that removes leading and trailing characters from a string or byte array.

**Parameter**  
---  
**Name** | **Description**  
`valueToTrim` |  `string | [Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression) | Uint8Array | "\"buffer\"".__global.Buffer`   
Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expr` representing the trimmed string or byte array.  
**Example**
    
    
    typescript
    // Trim whitespace from the 'userInput' field
    field("userInput").trim();
    
    // Trim quotes from the 'userInput' field
    field("userInput").trim('"');
    

### trunc()
    
    
    trunc(): FunctionExpression;

Creates an expression that truncates the numeric value to an integer.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
**Example**
    
    
    typescript
    // Truncate the 'rating' field.
    field("rating").trunc();
    

### trunc(decimalPlaces)
    
    
    trunc(decimalPlaces: number): FunctionExpression;

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Parameter**  
---  
**Name** | **Description**  
`decimalPlaces` |  `number`   
A constant specifying the truncation precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
**Example**
    
    
    typescript
    // Truncate the value of the 'rating' field to two decimal places.
    field("rating").trunc(2);
    

### trunc(decimalPlaces)
    
    
    trunc(decimalPlaces: Expression): FunctionExpression;

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Parameter**  
---  
**Name** | **Description**  
`decimalPlaces` |  `[Expression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.expression)`   
An expression specifying the truncation precision in decimal places.  
**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the truncated value.  
**Example**
    
    
    typescript
    // Truncate the value of the 'rating' field to two decimal places.
    field("rating").trunc(constant(2));
    

### type()
    
    
    type(): FunctionExpression;

Creates an expression that returns the data type of this expression's result, as a string.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new {Expression} representing the data type.  
**Example**
    
    
    typescript
    // Get the data type of the value in field 'title'
    field('title').type()
    

### unixMicrosToTimestamp()
    
    
    unixMicrosToTimestamp(): FunctionExpression;

Creates an expression that interprets this expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
**Example**
    
    
    typescript
    // Interpret the 'microseconds' field as microseconds since epoch.
    field("microseconds").unixMicrosToTimestamp();
    

### unixMillisToTimestamp()
    
    
    unixMillisToTimestamp(): FunctionExpression;

Creates an expression that interprets this expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
**Example**
    
    
    typescript
    // Interpret the 'milliseconds' field as milliseconds since epoch.
    field("milliseconds").unixMillisToTimestamp();
    

### unixSecondsToTimestamp()
    
    
    unixSecondsToTimestamp(): FunctionExpression;

Creates an expression that interprets this expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the timestamp.  
**Example**
    
    
    typescript
    // Interpret the 'seconds' field as seconds since epoch.
    field("seconds").unixSecondsToTimestamp();
    

### vectorLength()
    
    
    vectorLength(): FunctionExpression;

Creates an expression that calculates the length (number of dimensions) of this Firestore Vector expression.

**Returns**  
---  
**Type** | **Description**  
`[FunctionExpression](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.functionexpression)` | A new `Expression` representing the length of the vector.  
**Example**
    
    
    typescript
    // Get the vector length (dimension) of the field 'embedding'.
    field("embedding").vectorLength();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
