---
url: https://docs.cloud.google.com/data-studio/case-simple/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:36.541133+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/case-simple/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CASE (simple)

Simple `CASE` returns a result based on the value of a single input expression, or a default result if none of the comparison values match.

**Note:** There are two forms of the `CASE` statement: _searched_ `CASE` and _simple_ `CASE`. Searched `CASE` statements allow you to use more sophisticated logic, while simple `CASE` statements are simpler to construct.

See also: [IF](https://docs.cloud.google.com/data-studio/if).

## Sample usage

Replace payment codes with intuitive names:
    
    
        CASE Payment Type
            WHEN "CC" THEN "Credit Card"
            WHEN "DC" THEN "Debit Card"
            WHEN "GC" THEN "Gift Card"
            WHEN "CA" THEN "Cash"
            ELSE "Other"
        END
    

## Syntax
    
    
        CASE input_expression
            WHEN expression_to_match THEN result
            [WHEN expression_to_match THEN result]
            [...]
            [ELSE else_result]
        END
    

### Parameters

  * `input_expression` \- Any valid field or expression.
  * [`expression_to_match` \- Any valid field or expression. The `WHEN` clause compares `input_expression` to `input_expression` and returns true if the two are equal, or false if they aren't.]{#when-conditions}
  * `result ` \- Any valid field or expression. Each `WHEN` clause must have a matching `THEN` clause, which specifies the results to return if that condition is true. If there are multiple `WHEN` clauses, the `CASE` statement returns the result for the first true clause.
  * ```else_result` (optional) - Any valid field or expression. The `ELSE` _else_result_ clause specifies a default result for the `CASE` statement. This clause is returned if none of the `WHEN` clauses are true. If a `CASE` statement has no `ELSE` clause, and none of the `WHEN` clauses are true, the `CASE` statement returns `NULL`.

**Note:** All of the `THEN` clauses in a `CASE` statement must return the same type of result. For example, if the first `THEN` clause returns the **Text** data type, additional `THEN` clauses must also return the **Text** data type.

## How simple `CASE` works

A simple `CASE` statement consists of the following elements:

  * The `CASE` keyword, followed by an input expression.
  * `WHEN` : the value against which to compare the `input_expression` : if the value equals the `input_expression`, then this clause is true. You can have multiple `WHEN` clauses in a single `CASE` statement.
  * `THEN` : the result to return if the `WHEN` clause's condition is true. You must have one `THEN` clause for each `WHEN` clause in your `CASE` statement.
  * `ELSE` : Optional. If none of the `WHEN` clause conditions are true, `CASE` returns the value in the `ELSE` clause, or `NULL` if no `ELSE` clause is specified.
  * The `END` keyword.



`CASE` evaluates each successive `WHEN` clause and returns the first result where the condition is true. Any remaining `WHEN` clauses and the `ELSE` result are not evaluated. If all `WHEN` conditions are false or `NULL`, `CASE` returns the `ELSE` result, or if no `ELSE` clause is present, returns `NULL`.

## Example

Provide customized links for your premium customers:
    
    
        CASE Premium Status
            WHEN "Platinum" THEN CONCAT(Site URL, "platinum_welcome.html")
            WHEN "Gold" THEN CONCAT(Site URL, "gold_welcome.html")
            WHEN "Silver" THEN CONCAT(Site URL, "silver_welcome.html")
            ELSE CONCAT(Site URL, "welcome.html")
        END
    

## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
