---
url: https://docs.cloud.google.com/bigtable/docs/reference/sql/conditional_expressions/
title: Conditional expressions \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:40.356824+00:00
---

# Conditional expressions  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/sql/conditional_expressions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Conditional expressions Stay organized with collections  Save and categorize content based on your preferences. 

GoogleSQL for Bigtable supports conditional expressions.

### Evaluation order and short-circuiting

In contrast to regular functions, where all inputs are evaluated before calling the function, conditional expressions impose constraints on the evaluation semantics of their inputs:

  * Conditional expressions behave as if input expressions are evaluated from left to right and only up to the chosen output expression. Evaluation errors in unchosen expressions are ignored. If an expression that must be evaluated to determine the result produces an evaluation error, the query fails with that error. You can use short-circuiting semantics for error handling, such as avoiding division-by-zero errors. For more information, see [short-circuiting](https://en.wikipedia.org/wiki/Short-circuit_evaluation).
  * If the final result and error-handling behavior match short-circuiting semantics, input expressions might be evaluated in parallel or before the conditional expression is evaluated. These input expressions include scalar expressions and scalar subqueries in unchosen branches. Because all input expressions might still execute, don't rely solely on conditional expressions for performance tuning. For more information, see [lazy physical execution](https://en.wikipedia.org/wiki/Lazy_evaluation).



### Expression list

Name | Summary  
---|---  
`CASE expr` |  Compares the given expression to each successive `WHEN` clause and produces the first result where the values are equal.   
`CASE` |  Evaluates the condition of each successive `WHEN` clause and produces the first result where the condition evaluates to `TRUE`.   
`IF` |  If an expression evaluates to `TRUE`, produces a specified result, otherwise produces the evaluation for an _else result_.   
`IFNULL` |  If an expression evaluates to `NULL`, produces a specified result, otherwise produces the expression.   
`NULLIF` |  Produces `NULL` if the first expression that matches another evaluates to `TRUE`, otherwise returns the first expression.   
  
### `CASE expr`
    
    
    CASE expr
      WHEN expr_to_match THEN result
      [ ... ]
      [ ELSE else_result ]
      END
    

**Description**

Compares `expr` to `expr_to_match` of each successive `WHEN` clause and returns the first result where this comparison evaluates to `TRUE`. The expression behaves as if the remaining `WHEN` clauses and `else_result` aren't evaluated. For more information, see Evaluation order and short-circuiting.

If the `expr = expr_to_match` comparison evaluates to `FALSE` or `NULL` for all `WHEN` clauses, returns the evaluation of `else_result` if present; if `else_result` isn't present, then returns `NULL`.

Consistent with [equality comparisons](https://docs.cloud.google.com/bigtable/docs/reference/sql/operators#logical_operators) elsewhere, if both `expr` and `expr_to_match` are `NULL`, then `expr = expr_to_match` evaluates to `NULL`, which returns `else_result`. If a CASE statement needs to distinguish a `NULL` value, then the alternate CASE syntax should be used.

`expr` and `expr_to_match` can be any type. They must be implicitly coercible to a common [supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes); equality comparisons are done on coerced values. There may be multiple `result` types. `result` and `else_result` expressions must be coercible to a common supertype.

This expression supports specifying [collation](https://docs.cloud.google.com/bigtable/docs/reference/sql/collation-concepts).

**Return Data Type**

[Supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes) of `result`[, ...] and `else_result`.

**Example**
    
    
    SELECT
      CASE MAP_KEYS(cell_plan)[0]
        WHEN b'data_plan_01gb' THEN 'Small data plan'
        WHEN b'data_plan_05gb' THEN 'Large data plan'
        ELSE 'Unknown data plan
        END
        AS result
    FROM test_table LIMIT 2
    
    /*-----------------+
     | result          |
     +-----------------+
     | Small data plan |
     | Large data plan |
     +-----------------*/
    

### `CASE`
    
    
    CASE
      WHEN condition THEN result
      [ ... ]
      [ ELSE else_result ]
      END
    

**Description**

Evaluates the condition of each successive `WHEN` clause and returns the first result where the condition evaluates to `TRUE`. The expression behaves as if any remaining `WHEN` clauses and `else_result` aren't evaluated. For more information, see Evaluation order and short-circuiting.

If all conditions evaluate to `FALSE` or `NULL`, returns evaluation of `else_result` if present; if `else_result` isn't present, then returns `NULL`.

For additional rules on how values are evaluated, see the three-valued logic table in [Logical operators](https://docs.cloud.google.com/bigtable/docs/reference/sql/operators#logical_operators).

`condition` must be a boolean expression. There may be multiple `result` types. `result` and `else_result` expressions must be implicitly coercible to a common [supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes).

This expression supports specifying [collation](https://docs.cloud.google.com/bigtable/docs/reference/sql/collation-concepts).

**Return Data Type**

[Supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes) of `result`[, ...] and `else_result`.

**Example**
    
    
    SELECT
      CASE
        WHEN MAP_KEYS(cell_plan)[0] != b'data_plan_01gb' THEN 'Small data plan'
        WHEN MAP_KEYS(cell_plan)[0] != b'data_plan_05gb' THEN 'Large data plan'
        ELSE 'Unknown data plan'
        END
        AS result
    FROM test_table LIMIT 2
    
    /*-----------------+
     | result          |
     +-----------------+
     | Large data plan |
     | Small data plan |
     +-----------------*/
    

### `IF`
    
    
    IF(expr, true_result, else_result)
    

**Description**

If `expr` evaluates to `TRUE`, returns `true_result`, else returns the evaluation for `else_result`. The expression behaves as if `else_result` isn't evaluated when `expr` evaluates to `TRUE`, and as if `true_result` isn't evaluated when `expr` evaluates to `FALSE` or `NULL`. For more information, see Evaluation order and short-circuiting.

`expr` must be a boolean expression. `true_result` and `else_result` must be coercible to a common [supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes).

**Return Data Type**

[Supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes) of `true_result` and `else_result`.

**Examples**
    
    
    SELECT
      10 AS A,
      20 AS B,
      IF(10 < 20, 'true', 'false') AS result
    
    /*------------------+
     | A  | B  | result |
     +------------------+
     | 10 | 20 | true   |
     +------------------*/
    
    
    
    SELECT
      30 AS A,
      20 AS B,
      IF(30 < 20, 'true', 'false') AS result
    
    /*------------------+
     | A  | B  | result |
     +------------------+
     | 30 | 20 | false  |
     +------------------*/
    

### `IFNULL`
    
    
    IFNULL(expr, null_result)
    

**Description**

If `expr` evaluates to `NULL`, returns `null_result`. Otherwise, returns `expr`.

If `expr` is non-`NULL`, the expression behaves as if `null_result` isn't evaluated: evaluation errors in `null_result` are ignored, even though both input expressions might still be evaluated. If `expr` evaluates to `NULL` and `null_result` produces an evaluation error, the query fails with that error. For more information, see Evaluation order and short-circuiting.

`expr` and `null_result` can be any type and must be implicitly coercible to a common [supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes). Synonym for `COALESCE(expr, null_result)`.

**Return Data Type**

[Supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes) of `expr` or `null_result`.

**Examples**
    
    
    SELECT IFNULL(NULL, 0) as result
    
    /*--------+
     | result |
     +--------+
     | 0      |
     +--------*/
    
    
    
    SELECT IFNULL(10, 0) as result
    
    /*--------+
     | result |
     +--------+
     | 10     |
     +--------*/
    
    
    
    -- The first expression is non-NULL, so it's used. The division-by-zero error
    -- from the second expression isn't produced.
    SELECT IFNULL(10, 1 / 0) as result
    
    /*--------+
     | result |
     +--------+
     | 10     |
     +--------*/
    

### `NULLIF`
    
    
    NULLIF(expr, expr_to_match)
    

**Description**

Returns `NULL` if `expr = expr_to_match` evaluates to `TRUE`, otherwise returns `expr`.

`expr` and `expr_to_match` must be implicitly coercible to a common [supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes), and must be comparable.

This expression supports specifying [collation](https://docs.cloud.google.com/bigtable/docs/reference/sql/collation-concepts).

**Return Data Type**

[Supertype](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_rules#supertypes) of `expr` and `expr_to_match`.

**Example**
    
    
    SELECT NULLIF(0, 0) as result
    
    /*--------+
     | result |
     +--------+
     | NULL   |
     +--------*/
    
    
    
    SELECT NULLIF(10, 0) as result
    
    /*--------+
     | result |
     +--------+
     | 10     |
     +--------*/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
