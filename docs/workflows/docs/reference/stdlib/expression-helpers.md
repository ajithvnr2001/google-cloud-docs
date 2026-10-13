---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers/
title: Expression helpers \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:02.374105+00:00
---

# Expression helpers  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Expression helpers Stay organized with collections  Save and categorize content based on your preferences. 

In addition to the [standard library modules](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview), Workflows supports a number of other built-in helper functions such as for data type and format conversions.

For examples, see the [Syntax cheat sheet](https://docs.cloud.google.com/workflows/docs/reference/syntax/syntax-cheat-sheet).

### Conversion functions

Convert values from one data type to another.

Functions  
---  
`double()` | Accepts an attribute of type string or integer and returns a double.  
`int()` | Accepts an attribute of type string or double and returns an integer.  
`string()` | Accepts an attribute of type integer, double, or boolean and returns a string.  
  
### Data type functions

Operate on lists, maps, and strings.

Functions  
---  
`in()` | Checks whether a given key is present in a list or map. See [Check existence of a key in a list](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists#check-key) or [Check existence of a key in a map](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps#checking-key).   
`keys()` | Accepts an attribute of type map and returns a list of key elements in the map.  
`len()` | Computes the length of a value according to its type. Accepts an attribute of type list, map, or string and returns an integer.

  * A **list** returns the number of elements in the list.
  * A **map** returns the number of key-value entries stored in the map.
  * A **string** returns the number of characters in the string.

  
  
### Conditional functions

Support conditions within expressions.

Functions  
---  
`default(val, defaultVal)` | Returns a value if it is not null; otherwise returns a default value.

  * If not `null`, `val` is returned.
  * If `val` is `null`, `defaultVal` is returned.

You can use `default` with the standard library function, [map.get](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get), to safely access optional values in a map, returning null if the key is not found. For an example, see [Read map values](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps#reading-map). You can also use `default` to access optional runtime arguments, and return a default value if the key is not found. For an example, see [ Access runtime arguments](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments#access-run-args).   
`if(condition, ifTrue, ifFalse)` | Evaluates a condition and returns one of two arguments depending on what the condition evaluates to. 

  * If `condition` evaluates to true, `ifTrue` is returned.
  * If `condition` evaluates to false or `null`, `ifFalse` is returned.

Note that arguments passed to `if` are always evaluated and that the function does not control processing flow. To conditionally execute an expression, use a `switch` statement. For more information, see [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions).  
  
### Type functions

Return data type.

Functions  
---  
`get_type(arg)` | Returns a string indicating the data type of `arg`: one of `boolean`, `bytes`, `double`, `integer`, `list`, `map`, `string`, or `null`. If the operand is a function or a subworkflow, a `TypeError` is raised.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
