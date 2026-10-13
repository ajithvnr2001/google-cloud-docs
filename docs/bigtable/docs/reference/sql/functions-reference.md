---
url: https://docs.cloud.google.com/bigtable/docs/reference/sql/functions-reference/
title: Function calls \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:45.459077+00:00
---

# Function calls  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/sql/functions-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Function calls Stay organized with collections  Save and categorize content based on your preferences. 

When you call a function, specific rules may apply. You can also add the `SAFE.` prefix, which prevents functions from generating some types of errors. To learn more, see the next sections.

## Function call rules

The following rules apply to all built-in GoogleSQL functions unless explicitly indicated otherwise in the function description:

  * If an operand is `NULL`, the function result is `NULL`.
  * For functions that are time zone sensitive, the default time zone, UTC, is used when a time zone isn't specified.



## Named arguments
    
    
    named_argument => value
    

You can provide parameter arguments by name when calling some functions and procedures. These arguments are called _named arguments_. An argument that isn't named is called a _positional argument_.

  * Named arguments are optional, unless specified as required in the function signature.
  * Named arguments don't need to be in order.
  * You can specify positional arguments before named arguments.
  * You can't specify positional arguments after named arguments.
  * An optional positional argument that isn't used doesn't need to be added before a named argument.



**Examples**

These examples reference a function called `CountTokensInText`, which counts the number of tokens in a paragraph. The function signature looks like this:
    
    
    CountTokensInText(paragraph STRING, tokens ARRAY<STRING>, delimiters STRING)
    

`CountTokensInText` contains three arguments: `paragraph`, `tokens`, and `delimiters`. `paragraph` represents a body of text to analyze, `tokens` represents the tokens to search for in the paragraph, and `delimiters` represents the characters that specify a boundary between tokens in the paragraph.

This is a query that includes `CountTokensInText` without named arguments:
    
    
    SELECT token, count
    FROM CountTokensInText(
      'Would you prefer softball, baseball, or tennis? There is also swimming.',
      ['baseball', 'football', 'tennis'],
      ' .,!?()')
    

This is the query with named arguments:
    
    
    SELECT token, count
    FROM CountTokensInText(
      paragraph => 'Would you prefer softball, baseball, or tennis? There is also swimming.',
      tokens => ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()')
    

If named arguments are used, the order of the arguments doesn't matter. This works:
    
    
    SELECT token, count
    FROM CountTokensInText(
      tokens => ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()',
      paragraph => 'Would you prefer softball, baseball, or tennis? There is also swimming.')
    

You can mix positional arguments and named arguments, as long as the positional arguments in the function signature come first:
    
    
    SELECT token, count
    FROM CountTokensInText(
      'Would you prefer softball, baseball, or tennis? There is also swimming.',
      tokens => ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()')
    

This doesn't work because a positional argument appears after a named argument:
    
    
    SELECT token, count
    FROM CountTokensInText(
      paragraph => 'Would you prefer softball, baseball, or tennis? There is also swimming.',
      ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()')
    

If you want to use `tokens` as a positional argument, any arguments that appear before it in the function signature must also be positional arguments. If you try to use a named argument for `paragraph` and a positional argument for `tokens`, this will not work.
    
    
    -- This doesn't work.
    SELECT token, count
    FROM CountTokensInText(
      ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()',
      paragraph => 'Would you prefer softball, baseball, or tennis? There is also swimming.')
    
    -- This works.
    SELECT token, count
    FROM CountTokensInText(
      'Would you prefer softball, baseball, or tennis? There is also swimming.',
      ['baseball', 'football', 'tennis'],
      delimiters => ' .,!?()')
    

## SAFE. prefix

**Syntax:**
    
    
    SAFE.function_name()
    

**Description**

If you begin a function with the `SAFE.` prefix, it will return `NULL` instead of an error. The `SAFE.` prefix only prevents errors from the prefixed function itself: it doesn't prevent errors that occur while evaluating argument expressions. The `SAFE.` prefix only prevents errors that occur because of the value of the function inputs, such as "value out of range" errors; other errors, such as internal or system errors, may still occur. If the function doesn't return an error, `SAFE.` has no effect on the output.

**Exclusions**

  * [Operators](https://docs.cloud.google.com/bigtable/docs/reference/sql/operators), such as `+` and `=`, don't support the `SAFE.` prefix. To prevent errors from a division operation, use [SAFE_DIVIDE](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_divide).
  * Some operators, such as `ARRAY`, and `UNNEST`, resemble functions but don't support the `SAFE.` prefix.
  * The `CAST` and `EXTRACT` functions don't support the `SAFE.` prefix. To prevent errors from casting, use [SAFE_CAST](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_functions#safe_casting).



**Example**

In the following example, the first use of the `SUBSTR` function would normally return an error, because the function doesn't support length arguments with negative values. However, the `SAFE.` prefix causes the function to return `NULL` instead. The second use of the `SUBSTR` function provides the expected output: the `SAFE.` prefix has no effect.
    
    
    SELECT SAFE.SUBSTR('foo', 0, -2) AS safe_output UNION ALL
    SELECT SAFE.SUBSTR('bar', 0, 2) AS safe_output;
    
    /*-------------+
     | safe_output |
     +-------------+
     | NULL        |
     | ba          |
     +-------------*/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
