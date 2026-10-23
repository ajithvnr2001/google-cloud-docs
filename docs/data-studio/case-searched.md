---
url: https://docs.cloud.google.com/data-studio/case-searched/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:59.323516+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/case-searched/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CASE (Searched)

`CASE` statements evaluate one or more conditions and return a result when the first condition is met, or a default result if none of the conditions are met.

**Note:** there are two forms of the `CASE` statement: _searched_ `CASE` and _simple_ `CASE`. Searched `CASE` statements allow you to use more sophisticated logic, while simple `CASE` statements are simpler to construct.

See also: [IF](https://docs.cloud.google.com/data-studio/if).

## Sample usage

A common use for `CASE` is to create new categories or groupings of data. For example, to group selected country values into a Sales Region dimension, you might create a `CASE` statement like this:
    
    
    
        CASE
            WHEN Country IN ("USA","Canada","Mexico") THEN "North America"
            WHEN Country IN ("England","France") THEN "Europe"
            ELSE "Other"
        END
    
    

## Syntax
    
    
    
        CASE
            WHEN condition THEN result
            [WHEN condition THEN result]
            [...]
            [ELSE else_result]
        END
    
    

### Parameters

  * `condition` \- A logical field or expression. `WHEN` clauses evaluate `condition` and return true if the specified condition is met, or false if the condition isn't met.

  * `result` \- A field or expression of any type. Each `WHEN` clause must have a matching `THEN` clause, which specifies the results if that `WHEN condition` is true. If there are multiple `WHEN` clauses, the `CASE` statement returns the `result` for the first true `condition`.

  * `else_result` (optional) - A field or expression of any type. The `ELSE` `else_result ` clause specifies a default result for the `CASE` statement. This clause is returned if none of the `WHEN` clauses are true. If a `CASE` statement has no `ELSE` clause, and none of the `WHEN` clauses are true, the `CASE` statement returns `NULL`.




A `CASE` statement can have only one `ELSE` clause.

**Note:** All of the `THEN` clauses in a `CASE` statement must return the same data type. For example, if the first `THEN` clause returns the **Text** data type, additional `THEN` clauses must also return the **Text** data type.

## How searched `CASE` works

A searched `CASE` statement begins with the `CASE` keyword and ends with the `END` keyword. In between, you'll have a number of sections or clauses:

  * `WHEN`: A condition that you want to evaluate. You can have multiple `WHEN` clauses in a single `CASE` statement.
  * `THEN`: The result to return if the `WHEN` clause's condition is true. You must have one `THEN` clause for each `WHEN` clause in your `CASE` statement.
  * `ELSE`: Optional. If none of the `WHEN` clause conditions are true, `CASE` returns the value in the `ELSE` clause, or `NULL` if no `ELSE` clause is specified.



`CASE` evaluates each successive `WHEN` clause and returns the first result where the condition is true. Any remaining `WHEN` clauses and the `ELSE` result are not evaluated. If all `WHEN` conditions are false or `NULL`, `CASE` returns the `ELSE` result, or if no `ELSE` clause is present, returns `NULL`.

## Examples

### Check for inequality
    
    
        CASE WHEN Medium != "cpc" THEN "free" ELSE "paid" END
    

**Tip:** For simple scenarios, consider using the [IF function](https://docs.cloud.google.com/data-studio/if).

### Classify numeric dimension values into discrete buckets

For example, you can separate orders into "Small", "Medium", or "Large" based on order amount:
    
    
        CASE
            WHEN Amount < 20 THEN "Small"
            WHEN Amount >= 20 and Amount < 100 THEN "Medium"
            WHEN Amount >= 100 THEN "Large"
        END
    

**Note:** You can also use a [Group calculated field](https://docs.cloud.google.com/data-studio/create-a-custom-group) to create ad hoc groups for dimension values.

### Classify date dimension values into discrete buckets

For example, you can separate a year into semesters based on specific dates:
    
    
        CASE
            WHEN Date >= DATE(2018, 9, 23) and Date < DATE(2018, 12, 13) THEN "Fall Semester 2018"
            WHEN Date >= DATE(2018, 1, 3) and Date < DATE(2019, 3, 21) THEN "Winter Semester 2019"
            WHEN Date >= DATE(2019, 3, 27) and Date < DATE(2019, 6, 12) THEN "Spring Semester 2019"
            ELSE "Uncategorized"
        END
    

### Evaluate a logical AND condition
    
    
        CASE
            WHEN Country ISO Code = "US" AND Medium = "cpc"
            THEN "US - Paid"
            ELSE "other"
        END
    

### Evaluate a logical AND/OR condition
    
    
        CASE
            WHEN REGEXP_MATCH(Video Title, ".*Google Analytics*")
            AND is_livestream = TRUE
            OR Video Length > 600
            THEN "GA Livestream or long video"
        END
    

### Return a different field or value depending on a parameter value

**Example 1** : Return a dimension based on the parameter value selected. You can use this technique to let users switch the breakdown dimension used by a chart.
    
    
        CASE
            WHEN Breakdown = "Product Category" THEN Product Category
            WHEN Breakdown = "Store" THEN Store
        END
    

You could also write this using [simple CASE syntax](https://docs.cloud.google.com/data-studio/case-simple):
    
    
        CASE Breakdown
            WHEN "Product Category" THEN Product Category
            WHEN "Store" THEN Store
        END
    

**Example 2** : Return a different metric based on a parameter value.
    
    
    CASE WHEN Show Adjusted Cost = TRUE THEN Cost + Adjustments ELSE Cost END
    

### Nested `CASE` statements

You can nest `CASE` statements to create more complex branching logic:
    
    
        CASE WHEN REGEXP_CONTAINS(SKU, "Hats") THEN
            CASE WHEN Color = "blue"
                THEN "BLUE HAT" ELSE "JUST A HAT"
            END
            ELSE "NOT A HAT"
        END
    

## Related resources

  * [CASE (simple)](https://docs.cloud.google.com/data-studio/case-simple)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
